---
name: rust-specialist
description: Rust design and review judgment for ownership, APIs, soundness, concurrency, security, and measured performance. Use for any Rust project work, audit, refactor, or tuning task; leave mechanically checkable style to the project's compiler, formatter, and Clippy policy.
---

# Rust judgment

Use the project's compiler, formatter, Clippy configuration, and validation commands as the source of truth for mechanical rules. This skill covers decisions those tools cannot settle.

## Approach

1. Read the repository instructions, lint policy, nearby code, and public API before changing anything.
2. Identify the required behavior and the invariants the types must preserve.
3. Make the smallest safe change that keeps ownership and failure behavior obvious.
4. Exercise happy paths, failures, and boundary cases with the project's checks.
5. Measure before making performance claims or accepting complexity for speed.

## Refactoring semantics

Treat ownership, drop order, evaluation timing, panic behavior, error identity, trait bounds, inferred auto-traits, and public signatures as behavior.

- When replacing a `match` with combinators, preserve eager versus lazy evaluation, moves, borrows, and the exact error path.
- Borrow in place of ownership only when the callee does not need to retain, consume, or control the drop timing of the value.
- Remove a clone only after proving that moving or borrowing the value preserves later uses and destruction order.
- Before deriving a trait, compare the generated generic bounds and behavior with the manual implementation.
- Choose named generics, `impl Trait`, trait objects, or concrete types from the API contract. Do not change a public signature merely to shorten its spelling.
- Choose `match`, `if let`, `let else`, loops, or iterator chains by local clarity. Preserve iteration order, short-circuiting, mutation, and side effects.
- Use destructuring when it exposes the relevant shape without hiding ownership or coupling code to irrelevant fields.

## Safety and security

- Use `unsafe` only when a safe design cannot express the requirement. Keep the boundary small and verify every soundness invariant, including aliasing, lifetime, initialization, provenance, and thread-safety assumptions.
- Treat data from users, networks, files, environment variables, FFI, and syscalls as untrusted at the boundary. Validate before converting it into trusted domain types.
- Give failures enough typed context for the caller to recover or diagnose them without leaking secrets.
- Use constant-time operations for secrets, MACs, hashes, and authentication material. Plan how long secrets remain in memory and where they may be copied.
- Keep SQL, command arguments, and filesystem paths structured. Use prepared statements, argument arrays, and `Path` operations; define canonicalization and containment rules from the threat model.
- Assess dependencies by maintenance, transitive cost, platform support, security posture, and the amount of local code they retire.

## Performance and concurrency

- Establish a reproducible benchmark or profile before optimizing, and report the before-and-after result.
- Optimize the measured bottleneck. Consider algorithmic complexity and data layout before lower-level allocation or instruction tweaks.
- Decide whether an allocation or clone matters from path frequency, value size, lifetime, and memory pressure rather than from its presence alone.
- Choose concurrency from ordering, cancellation, backpressure, failure propagation, and contention requirements. Account explicitly for executor blocking and shutdown.
- Add parallelism only when measured work per task exceeds scheduling and synchronization cost.
- Change allocators, arenas, cache layout, or compile-time generation only with evidence that the added operational complexity pays for itself.

## API and module design

- Encode durable invariants in types when doing so makes invalid states materially harder to construct. Avoid typestate, newtypes, or phantom data that merely relocate complexity.
- Add a trait or generic seam only when multiple consumers, independent testing, substitution, or an established extension point pays for it. Prefer concrete types for local behavior.
- Accept small, local duplication when extraction would add indirection or couple code that changes for different reasons.
- Keep public surface minimal. Every exported type, bound, feature, and dependency is a compatibility commitment.
- Reach for `std` first, especially for paths, environment access, collections, synchronization, and platform behavior. Add a crate when it materially improves correctness, portability, or maintained complexity.
- Use `#[cfg(...)]` for code that is valid only on selected targets. Use `cfg!()` when every branch is valid on every compiled target and the boolean value itself is needed.

## Verification

Run the repository's formatter, Clippy, tests, and broader presubmit in proportion to the change. Use Miri for code whose safety depends on unsafe operations or subtle aliasing, dependency audit tools for supply-chain changes, and benchmarks or profiles for performance claims.

Finish only after every changed ownership boundary, public contract, unsafe invariant, failure path, and performance claim has either been verified or called out with the missing evidence.
