export type AudioReadiness = {
  canPlayPrompts: boolean;
  message: string;
};

export const getAudioReadiness = (): AudioReadiness => ({
  canPlayPrompts: false,
  message: 'Audio prompt playback is not enabled in the initial app shell.',
});
