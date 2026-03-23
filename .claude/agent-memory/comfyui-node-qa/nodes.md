# Node Inventory

## Video Pipeline Nodes
- **NSVideoConcatMulti** (py/video_concat.py, web/js/video_concat.js) - Hub node, concats videos with optional transitions/effects/overlays/captions
- **NSTransitionSettings** (py/transition_settings.py) - Outputs TRANSITION_SETTINGS dict
- **NSVideoEffects** (py/video_effects.py) - Zoom/wiggle/face tracking via Remotion, outputs EFFECTS_SETTINGS
- **NSVideoOverlay** (py/video_overlay.py) - Image/video overlay compositing, outputs OVERLAY_SETTINGS
- **NSVisualOverlay** (py/visual_overlay.py) - AI-generated infographic overlays via Claude+Remotion, outputs VISUAL_CUES_SETTINGS
- **NSCaptionOverlay** (py/caption_overlay.py) - Animated captions via Remotion, outputs CAPTION_SETTINGS
- **NSWhisperTranscribe** (py/whisper_transcribe.py) - Transcription node
- **NSSubmagicCaptions** (py/submagic_captions.py) - Submagic-style captions

## API Nodes
- WaveSpeed nodes (many): wavespeed_*.py
- Grok nodes: grok_imagine_image.py, grok_imagine_video.py, grok_client.py
- LLM Chat: llm_chat.py

## Utility Nodes
- NSPromptList: py/prompt_list_node.py
- NSQwenResolution: py/qwen_resolution_node.py
