import type {OptotypeOrientation} from './types';

export const OPTOTYPE_ORIENTATIONS: OptotypeOrientation[] = [
  'up',
  'down',
  'left',
  'right',
];

export const isCorrectOptotypeAnswer = (
  expected: OptotypeOrientation,
  actual: OptotypeOrientation | 'unknown' | 'skipped',
): boolean => actual === expected;
