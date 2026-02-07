# ABOUTME: Main initialization file for NeuralSins ComfyUI custom nodes
# Registers all custom nodes from the py/ directory

import importlib
import sys
from pathlib import Path

# Add py directory to Python path
py_dir = Path(__file__).parent / "py"
if str(py_dir) not in sys.path:
    sys.path.insert(0, str(py_dir))

# Import all node modules
from py.wavespeed_client import NODE_CLASS_MAPPINGS as wavespeed_client_mappings, NODE_DISPLAY_NAME_MAPPINGS as wavespeed_client_display
from py.wavespeed_flux_kontext_dev import NODE_CLASS_MAPPINGS as flux_kontext_dev_mappings, NODE_DISPLAY_NAME_MAPPINGS as flux_kontext_dev_display
from py.wavespeed_flux_kontext_max import NODE_CLASS_MAPPINGS as flux_kontext_max_mappings, NODE_DISPLAY_NAME_MAPPINGS as flux_kontext_max_display
from py.wavespeed_flux_kontext_pro import NODE_CLASS_MAPPINGS as flux_kontext_pro_mappings, NODE_DISPLAY_NAME_MAPPINGS as flux_kontext_pro_display
from py.wavespeed_flux_controlnet_union_pro_2 import NODE_CLASS_MAPPINGS as flux_controlnet_mappings, NODE_DISPLAY_NAME_MAPPINGS as flux_controlnet_display
from py.wavespeed_image_upscaler import NODE_CLASS_MAPPINGS as image_upscaler_mappings, NODE_DISPLAY_NAME_MAPPINGS as image_upscaler_display
from py.wavespeed_infinitetalk import NODE_CLASS_MAPPINGS as infinitetalk_mappings, NODE_DISPLAY_NAME_MAPPINGS as infinitetalk_display
from py.wavespeed_infinitetalk_multi import NODE_CLASS_MAPPINGS as infinitetalk_multi_mappings, NODE_DISPLAY_NAME_MAPPINGS as infinitetalk_multi_display
from py.wavespeed_nano_banana_edit import NODE_CLASS_MAPPINGS as nano_banana_edit_mappings, NODE_DISPLAY_NAME_MAPPINGS as nano_banana_edit_display
from py.wavespeed_nano_banana_pro_edit import NODE_CLASS_MAPPINGS as nano_banana_pro_edit_mappings, NODE_DISPLAY_NAME_MAPPINGS as nano_banana_pro_edit_display
from py.wavespeed_nano_banana_pro_edit_multi import NODE_CLASS_MAPPINGS as nano_banana_pro_edit_multi_mappings, NODE_DISPLAY_NAME_MAPPINGS as nano_banana_pro_edit_multi_display
from py.wavespeed_nano_banana_pro_edit_ultra import NODE_CLASS_MAPPINGS as nano_banana_pro_edit_ultra_mappings, NODE_DISPLAY_NAME_MAPPINGS as nano_banana_pro_edit_ultra_display
from py.wavespeed_nano_banana_text_to_image import NODE_CLASS_MAPPINGS as nano_banana_t2i_mappings, NODE_DISPLAY_NAME_MAPPINGS as nano_banana_t2i_display
from py.wavespeed_nano_banana_pro_text_to_image import NODE_CLASS_MAPPINGS as nano_banana_pro_t2i_mappings, NODE_DISPLAY_NAME_MAPPINGS as nano_banana_pro_t2i_display
from py.wavespeed_nano_banana_pro_text_to_image_multi import NODE_CLASS_MAPPINGS as nano_banana_pro_t2i_multi_mappings, NODE_DISPLAY_NAME_MAPPINGS as nano_banana_pro_t2i_multi_display
from py.wavespeed_nano_banana_pro_text_to_image_ultra import NODE_CLASS_MAPPINGS as nano_banana_pro_t2i_ultra_mappings, NODE_DISPLAY_NAME_MAPPINGS as nano_banana_pro_t2i_ultra_display
from py.wavespeed_qwen_edit import NODE_CLASS_MAPPINGS as qwen_edit_mappings, NODE_DISPLAY_NAME_MAPPINGS as qwen_edit_display
from py.wavespeed_qwen_edit_plus import NODE_CLASS_MAPPINGS as qwen_edit_plus_mappings, NODE_DISPLAY_NAME_MAPPINGS as qwen_edit_plus_display
from py.wavespeed_qwen_edit_lora import NODE_CLASS_MAPPINGS as qwen_edit_lora_mappings, NODE_DISPLAY_NAME_MAPPINGS as qwen_edit_lora_display
from py.wavespeed_qwen_edit_plus_lora import NODE_CLASS_MAPPINGS as qwen_edit_plus_lora_mappings, NODE_DISPLAY_NAME_MAPPINGS as qwen_edit_plus_lora_display
from py.wavespeed_qwen_text_to_image import NODE_CLASS_MAPPINGS as qwen_t2i_mappings, NODE_DISPLAY_NAME_MAPPINGS as qwen_t2i_display
from py.wavespeed_qwen_text_to_image_lora import NODE_CLASS_MAPPINGS as qwen_t2i_lora_mappings, NODE_DISPLAY_NAME_MAPPINGS as qwen_t2i_lora_display
from py.wavespeed_runway_upscale import NODE_CLASS_MAPPINGS as runway_upscale_mappings, NODE_DISPLAY_NAME_MAPPINGS as runway_upscale_display
from py.wavespeed_seedream_v4 import NODE_CLASS_MAPPINGS as seedream_v4_mappings, NODE_DISPLAY_NAME_MAPPINGS as seedream_v4_display
from py.wavespeed_seedream_v4_sequential import NODE_CLASS_MAPPINGS as seedream_v4_seq_mappings, NODE_DISPLAY_NAME_MAPPINGS as seedream_v4_seq_display
from py.wavespeed_seedream_v4_edit import NODE_CLASS_MAPPINGS as seedream_v4_edit_mappings, NODE_DISPLAY_NAME_MAPPINGS as seedream_v4_edit_display
from py.wavespeed_seedream_v4_edit_sequential import NODE_CLASS_MAPPINGS as seedream_v4_edit_seq_mappings, NODE_DISPLAY_NAME_MAPPINGS as seedream_v4_edit_seq_display
from py.wavespeed_sora2_text_to_video import NODE_CLASS_MAPPINGS as sora2_t2v_mappings, NODE_DISPLAY_NAME_MAPPINGS as sora2_t2v_display
from py.wavespeed_sora2_text_to_video_pro import NODE_CLASS_MAPPINGS as sora2_t2v_pro_mappings, NODE_DISPLAY_NAME_MAPPINGS as sora2_t2v_pro_display
from py.wavespeed_sora2_image_to_video import NODE_CLASS_MAPPINGS as sora2_i2v_mappings, NODE_DISPLAY_NAME_MAPPINGS as sora2_i2v_display
from py.wavespeed_sora2_image_to_video_pro import NODE_CLASS_MAPPINGS as sora2_i2v_pro_mappings, NODE_DISPLAY_NAME_MAPPINGS as sora2_i2v_pro_display
from py.wavespeed_veo31_text_to_video import NODE_CLASS_MAPPINGS as veo31_t2v_mappings, NODE_DISPLAY_NAME_MAPPINGS as veo31_t2v_display
from py.wavespeed_veo31_fast_text_to_video import NODE_CLASS_MAPPINGS as veo31_fast_t2v_mappings, NODE_DISPLAY_NAME_MAPPINGS as veo31_fast_t2v_display
from py.wavespeed_veo31_image_to_video import NODE_CLASS_MAPPINGS as veo31_i2v_mappings, NODE_DISPLAY_NAME_MAPPINGS as veo31_i2v_display
from py.wavespeed_veo31_fast_image_to_video import NODE_CLASS_MAPPINGS as veo31_fast_i2v_mappings, NODE_DISPLAY_NAME_MAPPINGS as veo31_fast_i2v_display
from py.wavespeed_veo31_reference_to_video import NODE_CLASS_MAPPINGS as veo31_ref2v_mappings, NODE_DISPLAY_NAME_MAPPINGS as veo31_ref2v_display
from py.wavespeed_wan22_animate import NODE_CLASS_MAPPINGS as wan22_animate_mappings, NODE_DISPLAY_NAME_MAPPINGS as wan22_animate_display
from py.wavespeed_wan22_i2v_720p import NODE_CLASS_MAPPINGS as wan22_i2v_mappings, NODE_DISPLAY_NAME_MAPPINGS as wan22_i2v_display
from py.wavespeed_wan25_text_to_image import NODE_CLASS_MAPPINGS as wan25_t2i_mappings, NODE_DISPLAY_NAME_MAPPINGS as wan25_t2i_display
from py.wavespeed_wan25_text_to_video import NODE_CLASS_MAPPINGS as wan25_t2v_mappings, NODE_DISPLAY_NAME_MAPPINGS as wan25_t2v_display
from py.wavespeed_wan25_text_to_video_fast import NODE_CLASS_MAPPINGS as wan25_t2v_fast_mappings, NODE_DISPLAY_NAME_MAPPINGS as wan25_t2v_fast_display
from py.wavespeed_wan25_image_to_video import NODE_CLASS_MAPPINGS as wan25_i2v_mappings, NODE_DISPLAY_NAME_MAPPINGS as wan25_i2v_display
from py.wavespeed_wan25_image_to_video_fast import NODE_CLASS_MAPPINGS as wan25_i2v_fast_mappings, NODE_DISPLAY_NAME_MAPPINGS as wan25_i2v_fast_display
from py.wavespeed_wan25_image_edit import NODE_CLASS_MAPPINGS as wan25_edit_mappings, NODE_DISPLAY_NAME_MAPPINGS as wan25_edit_display
from py.llm_chat import NODE_CLASS_MAPPINGS as llm_chat_mappings, NODE_DISPLAY_NAME_MAPPINGS as llm_chat_display
from py.prompt_list_node import NODE_CLASS_MAPPINGS as prompt_list_mappings, NODE_DISPLAY_NAME_MAPPINGS as prompt_list_display
from py.qwen_resolution_node import NODE_CLASS_MAPPINGS as qwen_resolution_mappings, NODE_DISPLAY_NAME_MAPPINGS as qwen_resolution_display
from py.grok_client import NODE_CLASS_MAPPINGS as grok_client_mappings, NODE_DISPLAY_NAME_MAPPINGS as grok_client_display
from py.grok_imagine_image import NODE_CLASS_MAPPINGS as grok_image_mappings, NODE_DISPLAY_NAME_MAPPINGS as grok_image_display
from py.grok_imagine_video import NODE_CLASS_MAPPINGS as grok_video_mappings, NODE_DISPLAY_NAME_MAPPINGS as grok_video_display

# Merge all node mappings
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

all_class_mappings = [
    wavespeed_client_mappings,
    flux_kontext_dev_mappings,
    flux_kontext_max_mappings,
    flux_kontext_pro_mappings,
    flux_controlnet_mappings,
    image_upscaler_mappings,
    infinitetalk_mappings,
    infinitetalk_multi_mappings,
    nano_banana_edit_mappings,
    nano_banana_pro_edit_mappings,
    nano_banana_pro_edit_multi_mappings,
    nano_banana_pro_edit_ultra_mappings,
    nano_banana_t2i_mappings,
    nano_banana_pro_t2i_mappings,
    nano_banana_pro_t2i_multi_mappings,
    nano_banana_pro_t2i_ultra_mappings,
    qwen_edit_mappings,
    qwen_edit_plus_mappings,
    qwen_edit_lora_mappings,
    qwen_edit_plus_lora_mappings,
    qwen_t2i_mappings,
    qwen_t2i_lora_mappings,
    runway_upscale_mappings,
    seedream_v4_mappings,
    seedream_v4_seq_mappings,
    seedream_v4_edit_mappings,
    seedream_v4_edit_seq_mappings,
    sora2_t2v_mappings,
    sora2_t2v_pro_mappings,
    sora2_i2v_mappings,
    sora2_i2v_pro_mappings,
    veo31_t2v_mappings,
    veo31_fast_t2v_mappings,
    veo31_i2v_mappings,
    veo31_fast_i2v_mappings,
    veo31_ref2v_mappings,
    wan22_animate_mappings,
    wan22_i2v_mappings,
    wan25_t2i_mappings,
    wan25_t2v_mappings,
    wan25_t2v_fast_mappings,
    wan25_i2v_mappings,
    wan25_i2v_fast_mappings,
    wan25_edit_mappings,
    llm_chat_mappings,
    prompt_list_mappings,
    qwen_resolution_mappings,
    grok_client_mappings,
    grok_image_mappings,
    grok_video_mappings,
]

all_display_mappings = [
    wavespeed_client_display,
    flux_kontext_dev_display,
    flux_kontext_max_display,
    flux_kontext_pro_display,
    flux_controlnet_display,
    image_upscaler_display,
    infinitetalk_display,
    infinitetalk_multi_display,
    nano_banana_edit_display,
    nano_banana_pro_edit_display,
    nano_banana_pro_edit_multi_display,
    nano_banana_pro_edit_ultra_display,
    nano_banana_t2i_display,
    nano_banana_pro_t2i_display,
    nano_banana_pro_t2i_multi_display,
    nano_banana_pro_t2i_ultra_display,
    qwen_edit_display,
    qwen_edit_plus_display,
    qwen_edit_lora_display,
    qwen_edit_plus_lora_display,
    qwen_t2i_display,
    qwen_t2i_lora_display,
    runway_upscale_display,
    seedream_v4_display,
    seedream_v4_seq_display,
    seedream_v4_edit_display,
    seedream_v4_edit_seq_display,
    sora2_t2v_display,
    sora2_t2v_pro_display,
    sora2_i2v_display,
    sora2_i2v_pro_display,
    veo31_t2v_display,
    veo31_fast_t2v_display,
    veo31_i2v_display,
    veo31_fast_i2v_display,
    veo31_ref2v_display,
    wan22_animate_display,
    wan22_i2v_display,
    wan25_t2i_display,
    wan25_t2v_display,
    wan25_t2v_fast_display,
    wan25_i2v_display,
    wan25_i2v_fast_display,
    wan25_edit_display,
    llm_chat_display,
    prompt_list_display,
    qwen_resolution_display,
    grok_client_display,
    grok_image_display,
    grok_video_display,
]

for mapping in all_class_mappings:
    NODE_CLASS_MAPPINGS.update(mapping)

for mapping in all_display_mappings:
    NODE_DISPLAY_NAME_MAPPINGS.update(mapping)

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

print("\033[34mNeuralSins Nodes: \033[92mLoaded\033[0m")
