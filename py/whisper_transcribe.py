# ABOUTME: Local speech-to-text transcription node using faster-whisper
# ABOUTME: Extracts word-level timestamps from video audio for caption generation

import os
import subprocess
import tempfile
import shutil

FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"


class NSWhisperTranscribe:
    """
    Transcribes speech from a video using faster-whisper (local, no API).
    Produces word-level timestamps for animated caption generation.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video": ("VIDEO",),
            },
            "optional": {
                "language": (["auto", "en", "es", "fr", "de", "it", "pt", "nl",
                              "ja", "ko", "zh", "ru", "ar", "hi", "cs", "pl",
                              "tr", "uk", "ro", "sv", "da", "fi", "no", "hu"],
                             {"default": "auto"}),
                "model_size": (["tiny", "base", "small", "medium", "large-v3"],
                               {"default": "base"}),
            }
        }

    RETURN_TYPES = ("TRANSCRIPT",)
    RETURN_NAMES = ("transcript",)
    FUNCTION = "execute"
    CATEGORY = "neuralsins/Video"

    def _extract_audio(self, video_path, temp_files):
        """Extract audio from video as 16kHz mono WAV for whisper."""
        wav_path = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
        temp_files.append(wav_path)

        cmd = [
            FFMPEG, "-y", "-i", video_path,
            "-vn", "-acodec", "pcm_s16le",
            "-ar", "16000", "-ac", "1",
            wav_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            return None  # No audio stream
        return wav_path

    def execute(self, video, language="auto", model_size="base"):
        from comfy_api.latest import InputImpl
        from faster_whisper import WhisperModel

        temp_files = []
        try:
            # Save video to temp file
            video_path = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False).name
            temp_files.append(video_path)
            video.save_to(video_path, format="mp4", codec="h264")

            # Extract audio
            wav_path = self._extract_audio(video_path, temp_files)
            if wav_path is None:
                print("[NSWhisperTranscribe] No audio stream found, returning empty transcript")
                return ({"text": "", "words": []},)

            # Load model and transcribe
            print(f"[NSWhisperTranscribe] Loading model '{model_size}'...")
            model = WhisperModel(model_size, compute_type="int8")

            lang = None if language == "auto" else language
            print(f"[NSWhisperTranscribe] Transcribing (language={language})...")

            segments, info = model.transcribe(
                wav_path,
                language=lang,
                word_timestamps=True,
                vad_filter=True,
            )

            # Collect words with timestamps
            words = []
            full_text_parts = []
            for segment in segments:
                full_text_parts.append(segment.text.strip())
                if segment.words:
                    for w in segment.words:
                        words.append({
                            "word": w.word.strip(),
                            "start": round(w.start, 3),
                            "end": round(w.end, 3),
                        })

            full_text = " ".join(full_text_parts)
            print(f"[NSWhisperTranscribe] Done: {len(words)} words, "
                  f"language={info.language} (prob={info.language_probability:.2f})")

            return ({"text": full_text, "words": words},)

        finally:
            for f in temp_files:
                try:
                    os.unlink(f)
                except OSError:
                    pass


NODE_CLASS_MAPPINGS = {
    "NSWhisperTranscribe": NSWhisperTranscribe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NSWhisperTranscribe": "NS Whisper Transcribe"
}
