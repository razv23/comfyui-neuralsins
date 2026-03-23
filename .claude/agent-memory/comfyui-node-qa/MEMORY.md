# QA Agent Memory

## Codebase Structure
- ~55 Python node files in `py/`, 1 JS file in `web/js/`
- Dynamic loader in `__init__.py` catches import errors per-module (won't crash pack)
- See [nodes.md](nodes.md) for node inventory
- See [patterns.md](patterns.md) for codebase patterns

## Key Conventions
- Settings nodes (NSTransitionSettings, NSVideoEffects, etc.) output dicts as custom types
- NSVideoConcatMulti is the hub node: accepts 5 settings types + dynamic video inputs
- JS extension uses detach/reattach pattern to keep settings inputs after video inputs
- All VIDEO-handling nodes lazy-import `from comfy_api.latest import InputImpl` inside execute()
- FFmpeg/FFprobe resolved at module level with `shutil.which() or "/opt/homebrew/bin/..."`
- Remotion-based nodes (effects, captions, visual overlay) also resolve node/npx/npm paths

## Common Error Patterns
- Module-level `from comfy_api.input import VideoInput` will silently kill the module
- Sibling imports (`from .video_effects import ...`) must be inside execute() to avoid circular deps
- `_deps_checked` global pattern used by Remotion nodes to check npm install once
