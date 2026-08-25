---
name: github-attachments
description: Attach a local image, video, or other file to a GitHub issue body/comment or pull request description/comment.
---

# GitHub Attachments

Use the third-party [`drogers0/gh-image`](https://github.com/drogers0/gh-image) extension to turn a local file into GitHub attachment markup, then place that markup in the requested issue or pull request text.

1. Resolve the exact repository, issue or pull request, destination surface, and local files. Inspect each file before uploading; finish when every upload target is unambiguous and contains no unintended sensitive content.
2. Check `gh auth status` and `gh image --help`. If `gh image` is unavailable, install it with `gh extension install drogers0/gh-image`, then rerun the check. This extension uses GitHub's undocumented attachment-upload mechanism, so report a changed or failed interface rather than improvising another uploader.
3. Upload each file with `gh image <path> --repo OWNER/REPO` and capture stdout exactly. Treat the returned image Markdown or attachment URL as opaque text.
4. Compose the complete comment or body with the returned text. Preserve existing issue bodies and pull request descriptions unless replacement was requested. Prefer the relevant `gh issue` or `gh pr` command's `--body-file` option for multiline content.
5. Submit once, then fetch the resulting GitHub body or comment and verify that every returned attachment URL is present. If submission fails after upload, return the uploaded markup so it can be recovered.

Finish when the requested GitHub surface contains every attachment and all pre-existing or requested prose is intact.
