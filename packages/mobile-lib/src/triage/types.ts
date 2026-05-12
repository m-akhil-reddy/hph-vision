import type {DomainWarning} from '../types';

export type TriageCategory =
  | 'sudden_vision_loss'
  | 'eye_pain'
  | 'flashes_or_floaters'
  | 'double_vision'
  | 'recent_eye_trauma'
  | 'severe_redness'
  | 'known_glaucoma'
  | 'diabetes_related_risk'
  | 'recent_eye_surgery';

export type TriageQuestion = {
  id: string;
  promptKey: string;
  fallbackPrompt: string;
  category: TriageCategory;
  answerType: 'yesNo';
  blocksSelfTestOnPositive: boolean;
  urgentOnPositive?: boolean;
};

export type TriageAnswer = {
  questionId: string;
  value: boolean;
};

export type TriageResult = {
  canContinueSelfTest: boolean;
  redFlags: TriageCategory[];
  recommendation: 'continue' | 'seekProfessionalCare' | 'urgentCare';
  warnings: DomainWarning[];
  unansweredQuestionIds: string[];
};
