import type {Eye, InputMethod, ISODateString} from '../types';

export type OptotypeKind = 'tumblingE' | 'landoltC';
export type OptotypeOrientation = 'up' | 'down' | 'left' | 'right';

export type AcuityTrial = {
  id: string;
  eye: Eye;
  optotype: OptotypeKind;
  orientation: OptotypeOrientation;
  sizeLogMar: number;
  isPractice: boolean;
  startedAt?: ISODateString;
};

export type AcuityResponse = {
  trialId: string;
  answer: OptotypeOrientation | 'unknown' | 'skipped';
  responseTimeMs?: number;
  inputMethod: InputMethod;
  confidence?: number;
  createdAt: ISODateString;
};

export type AcuitySessionOptions = {
  id?: string;
  eye: Eye;
  optotype?: OptotypeKind;
  randomSeed?: string;
  practiceTrials?: number;
  sizeLogMarSequence?: number[];
};

export type AcuitySession = {
  id: string;
  protocolVersion: 'acuity-v0.1';
  eye: Eye;
  optotype: OptotypeKind;
  trials: AcuityTrial[];
  responses: AcuityResponse[];
  completed: boolean;
};

export type AcuityResult = {
  eye: Eye;
  logMarEstimate?: number;
  snellenEquivalent?: string;
  completed: boolean;
  confidence: number;
  reliabilityWarnings: string[];
  trials: AcuityTrial[];
  responses: AcuityResponse[];
};
