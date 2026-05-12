import type {AcuityTrial} from '../acuity';
import type {RefractionTrial} from '../refraction';
import type {VoiceCommand, VoiceRecognitionCandidate} from './types';

const COMMAND_SYNONYMS: Record<VoiceCommand, string[]> = {
  better: ['better', 'clearer', 'best'],
  worse: ['worse', 'blurrier', 'bad'],
  same: ['same', 'equal', 'no difference'],
  one: ['one', '1', 'first', 'option one'],
  two: ['two', '2', 'second', 'option two'],
  left: ['left'],
  right: ['right'],
  up: ['up', 'top'],
  down: ['down', 'bottom'],
  repeat: ['repeat', 'again'],
  stop: ['stop', 'cancel', 'quit'],
  unknown: ['unknown', "i don't know", 'dont know', 'skip'],
};

const normalizeTranscript = (value: string): string =>
  value
    .trim()
    .toLowerCase()
    .replace(/[’']/g, '')
    .replace(/[^a-z0-9 ]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();

export const mapTranscriptToCommand = (
  candidate: VoiceRecognitionCandidate,
): VoiceCommand => {
  const normalized = normalizeTranscript(candidate.transcript);

  for (const [command, synonyms] of Object.entries(COMMAND_SYNONYMS) as [
    VoiceCommand,
    string[],
  ][]) {
    if (synonyms.some(synonym => normalizeTranscript(synonym) === normalized)) {
      return command;
    }
  }

  return 'unknown';
};

export const getAllowedCommandsForTrial = (
  trial: AcuityTrial | RefractionTrial,
): VoiceCommand[] => {
  if ('orientation' in trial) {
    return ['up', 'down', 'left', 'right', 'repeat', 'stop', 'unknown'];
  }
  if (trial.promptKey.includes('oneOrTwo')) {
    return ['one', 'two', 'same', 'repeat', 'stop', 'unknown'];
  }
  return ['better', 'worse', 'same', 'repeat', 'stop', 'unknown'];
};
