export const mobileLibraryName = '@hiperhealth/hphvision-lib';
export const HPHVISION_LIB_VERSION = '0.0.1';

export const SCREENING_DISCLAIMER =
  'This result is a screening and estimation output. It is not a complete eye health examination.';

export type ISODateString = string;

export type Eye = 'left' | 'right' | 'binocular';

export type InputMethod = 'voice' | 'touch' | 'external';

export type ResultRecommendation =
  | 'continue_self_monitoring'
  | 'repeat_test'
  | 'clinician_review_recommended'
  | 'professional_exam_recommended'
  | 'urgent_care_recommended'
  | 'invalid_result';

export type DomainWarning = {
  code: string;
  message: string;
  severity: 'info' | 'warning' | 'critical';
  source?: string;
};

export type ApiResult<T> = {
  data: T;
  error?: string;
};
