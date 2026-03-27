# ABOUTME: Shared binary path resolution for all nodes.
# ABOUTME: Searches PATH, macOS Homebrew, and common Linux locations.

import os
import shutil


def find(name):
    """Find a binary in PATH, common macOS, and common Linux locations."""
    found = shutil.which(name)
    if found:
        return found
    for d in ["/opt/homebrew/bin", "/usr/local/bin", "/usr/bin"]:
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    return name  # last resort — let subprocess raise if missing


FFMPEG = find("ffmpeg")
FFPROBE = find("ffprobe")
NODE_BIN = find("node")
NPX_BIN = find("npx")
NPM_BIN = find("npm")
