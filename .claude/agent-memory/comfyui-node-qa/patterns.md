# Codebase Patterns

## Dynamic Inputs Pattern (NSVideoConcatMulti)
- Python: `video_1` required, `video_2` optional, `**kwargs` in execute
- JS: counts by name prefix (`video_*`), not type
- JS detach/reattach pattern for settings inputs ordering:
  1. Remove settings inputs (save connection info)
  2. Add new video inputs
  3. Re-add settings inputs at end (restore connections)
- Settings inputs: transition_settings, effects_settings, overlay_settings, visual_cues_settings, caption_settings

## Settings Node Pattern
- Pure-data nodes that output a dict as a custom type (e.g. TRANSITION_SETTINGS)
- No comfy_api imports needed
- Consumer node reads dict keys directly: `settings["type"]`, etc.
- NSVideoConcatMulti consumes all 5 settings types and delegates to helper nodes

## Video Processing Pipeline (NSVideoConcatMulti)
1. Save all VIDEO inputs to temp mp4 files
2. Apply per-clip effects (NSVideoEffects) if effects_settings connected
3. Concat/xfade via FFmpeg
4. Apply overlay (NSVideoOverlay) to result
5. Apply visual cues (NSVisualOverlay) to result
6. Apply captions (NSCaptionOverlay) to result
7. Return as InputImpl.VideoFromFile()

## Sibling Module Imports
- Always inside execute(), never at module level
- Pattern: `from .video_effects import NSVideoEffects`
- Used to call `_process_file()` methods on sibling nodes

## Temp File Cleanup
- All nodes use try/finally with temp_files list
- `os.unlink(f)` in finally block, wrapped in try/except OSError
