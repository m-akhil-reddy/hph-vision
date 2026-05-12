import {describe, expect, it} from '@jest/globals';

import {evaluateTriage, getTriageQuestions} from '..';

describe('evaluateTriage', () => {
  it('allows self-test when all answers are negative', () => {
    const answers = getTriageQuestions().map(question => ({
      questionId: question.id,
      value: false,
    }));

    expect(evaluateTriage(answers)).toMatchObject({
      canContinueSelfTest: true,
      recommendation: 'continue',
    });
  });

  it('blocks self-test on red flags', () => {
    const answers = getTriageQuestions().map(question => ({
      questionId: question.id,
      value: question.id === 'sudden-vision-loss',
    }));

    expect(evaluateTriage(answers)).toMatchObject({
      canContinueSelfTest: false,
      recommendation: 'urgentCare',
    });
  });
});
