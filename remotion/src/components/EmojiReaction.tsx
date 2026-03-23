// ABOUTME: Emoji pop-in component with bouncy spring animation
// ABOUTME: Scales from 0→1.2→1.0 when appearing alongside a word chunk

import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

interface Props {
  emoji: string;
  appearFrame: number;
  fontSize: number;
}

export const EmojiReaction: React.FC<Props> = ({
  emoji,
  appearFrame,
  fontSize,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const framesSince = frame - appearFrame;
  if (framesSince < 0) return null;

  const springVal = spring({
    frame: framesSince,
    fps,
    config: { damping: 8, stiffness: 180 },
  });

  const scale = interpolate(springVal, [0, 1], [0, 1]);
  const rotate = interpolate(springVal, [0, 0.5, 1], [-20, 10, 0]);

  return (
    <span
      style={{
        display: "inline-block",
        fontSize: fontSize * 0.9,
        transform: `scale(${scale}) rotate(${rotate}deg)`,
        marginLeft: fontSize * 0.2,
      }}
    >
      {emoji}
    </span>
  );
};
