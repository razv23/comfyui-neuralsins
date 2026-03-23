// ABOUTME: Remotion composition for animated caption overlay on transparent background
// ABOUTME: Renders spring-animated word-by-word captions with emoji support

import React, { useMemo } from "react";
import {
  AbsoluteFill,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { CaptionProps, Word, WordChunk as WordChunkType } from "./types";
import { TEMPLATES } from "./templates";
import { findEmoji } from "./emoji-map";
import { WordChunk } from "./components/WordChunk";

function buildChunks(
  words: Word[],
  wordsPerLine: number,
  withEmoji: boolean
): WordChunkType[] {
  const chunks: WordChunkType[] = [];

  for (let i = 0; i < words.length; i += wordsPerLine) {
    const chunkWords = words.slice(i, i + wordsPerLine);
    const startTime = chunkWords[0].start;
    const endTime = chunkWords[chunkWords.length - 1].end;

    const emoji = withEmoji
      ? findEmoji(chunkWords.map((w) => w.word))
      : undefined;

    chunks.push({ words: chunkWords, startTime, endTime, emoji });
  }

  return chunks;
}

export const CaptionOverlay: React.FC<CaptionProps> = ({
  words,
  template: templateName,
  position,
  fontSize,
  wordsPerLine,
  fontColor: fontColorOverride,
  highlightColor: highlightColorOverride,
  emojis,
  animation,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const template = TEMPLATES[templateName] ?? TEMPLATES.Hormozi;

  const fontColor = fontColorOverride || template.fontColor;
  const highlightColor = highlightColorOverride || template.highlightColor;

  const chunks = useMemo(
    () => buildChunks(words, wordsPerLine, emojis),
    [words, wordsPerLine, emojis]
  );

  // Find which chunk is active at the current time
  const currentTime = frame / fps;
  const activeChunk = chunks.find(
    (c) => currentTime >= c.startTime && currentTime <= c.endTime
  );

  // Position: 0 = top (5%), 100 = bottom (90%)
  const topPercent = 5 + (position / 100) * 85;

  return (
    <AbsoluteFill style={{ backgroundColor: "transparent" }}>
      <div
        style={{
          position: "absolute",
          top: `${topPercent}%`,
          left: "5%",
          right: "5%",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        {activeChunk && (
          <WordChunk
            chunk={activeChunk}
            template={template}
            fontSize={fontSize}
            fontColor={fontColor}
            highlightColor={highlightColor}
            showEmoji={emojis}
            animation={animation}
          />
        )}
      </div>
    </AbsoluteFill>
  );
};
