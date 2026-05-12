import {HPHVISION_LIB_VERSION} from '../types';
import {ACUITY_PROTOCOL_VERSION} from '../acuity';
import {REFRACTION_PROTOCOL_VERSION} from '../refraction';
import {TEMPLATE_VERSION} from '../template-generator';
import type {ProtocolVersions} from './types';

export const REPORT_SCHEMA_VERSION = 'report-v0.1';

export const getDefaultProtocolVersions = (): ProtocolVersions => ({
  acuity: ACUITY_PROTOCOL_VERSION,
  refraction: REFRACTION_PROTOCOL_VERSION,
  template: TEMPLATE_VERSION,
  report: REPORT_SCHEMA_VERSION,
});

export const getLibraryVersion = (): string => HPHVISION_LIB_VERSION;
