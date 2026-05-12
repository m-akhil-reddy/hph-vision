import {HPHVISION_LIB_VERSION} from '../types';
import {getDefaultProtocolVersions} from './versioning';
import type {TestSession} from './types';

export const createEmptyTestSession = (
  id: string,
  createdAt: string,
): TestSession => ({
  id,
  createdAt,
  libraryVersion: HPHVISION_LIB_VERSION,
  protocolVersions: getDefaultProtocolVersions(),
  patientContext: {},
  environment: {},
  acuityResults: [],
  reliabilityScore: 0,
  warnings: [],
});
