import type {AcuityResult} from '../acuity';
import type {DeviceProfile} from '../device-profile';
import type {RefractionResult} from '../refraction';
import type {ReliabilityResult} from '../reliability';
import type {DomainWarning, ISODateString} from '../types';
import type {TriageResult} from '../triage';
import type {TemplateMetadata} from '../template-generator';

export type ProtocolVersions = {
  acuity?: string;
  refraction?: string;
  template?: string;
  report?: string;
};

export type PatientContext = {
  ageRange?: string;
  currentGlasses?: boolean;
  previousPrescription?: boolean;
};

export type EnvironmentContext = {
  ambientLightLux?: number;
  screenBrightness?: number;
  distanceConfidence?: number;
  tiltConfidence?: number;
};

export type TestSession = {
  id: string;
  createdAt: ISODateString;
  appVersion?: string;
  libraryVersion?: string;
  protocolVersions?: ProtocolVersions;
  deviceProfile?: DeviceProfile;
  templateMetadata?: TemplateMetadata;
  patientContext: PatientContext;
  environment: EnvironmentContext;
  triageResult?: TriageResult;
  acuityResults: AcuityResult[];
  refractionResult?: RefractionResult;
  reliability?: ReliabilityResult;
  reliabilityScore: number;
  warnings: DomainWarning[];
};
