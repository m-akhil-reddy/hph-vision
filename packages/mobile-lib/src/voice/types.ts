export type VoiceCommand =
  | 'better'
  | 'worse'
  | 'same'
  | 'one'
  | 'two'
  | 'left'
  | 'right'
  | 'up'
  | 'down'
  | 'repeat'
  | 'stop'
  | 'unknown';

export type VoiceRecognitionCandidate = {
  transcript: string;
  confidence?: number;
  locale: string;
};
