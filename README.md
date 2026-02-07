# NeuralSins ComfyUI Custom Nodes

A collection of custom nodes for ComfyUI, including WaveSpeed API integrations and utility nodes.

## Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "NeuralSins"
3. Click Install

### Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/razv23/comfyui-neuralsins.git
   ```

3. Install dependencies:
   ```bash
   cd comfyui-neuralsins
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

## Configuration

### WaveSpeed API Key Setup

You have three options to provide your WaveSpeed API key:

1. **Via Node Input**: Enter your API key directly in the WaveSpeed Client node
2. **Via config.ini**: Create a `config.ini` file in the root directory:
   ```ini
   [API]
   api_key = YOUR_API_KEY_HERE
   ```
3. **Via Environment Variable**: Set the `WAVESPEED_API_KEY` environment variable

Get your API key at [https://wavespeed.ai](https://wavespeed.ai)

## Node Categories

### WaveSpeed Nodes (`neuralsins/WaveSpeed`)
- **Client**: WaveSpeed API authentication
- **Flux Models**: Kontext Dev/Max/Pro, ControlNet Union Pro 2
- **Image Generation**: Nano Banana, Qwen, Wan25, SeeDream V4
- **Image Editing**: Nano Banana Edit, Qwen Edit, Wan25 Image Edit
- **Video Generation**: Sora2, Veo31, Wan22/25, InfiniteTalk
- **Upscaling**: Image Upscaler, Runway Upscale

### LLM Nodes (`neuralsins/LLM`)
- **LLM Chat**: Multi-provider LLM chat (Claude, Gemini, GPT)

### Utility Nodes (`neuralsins/Utils`)
- **Prompt List**: Dynamic prompt list builder with configurable inputs
- **Qwen Resolution**: Resolution selector with visual preview

## Requirements

- ComfyUI
- Python 3.8+
- Dependencies listed in `requirements.txt`

## License

See [LICENSE](LICENSE) file for details.

## Support

For issues and feature requests, please use the [GitHub Issues](https://github.com/razv23/comfyui-neuralsins/issues) page.
