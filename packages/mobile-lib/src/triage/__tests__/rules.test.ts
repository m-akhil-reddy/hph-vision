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

  it('blocks self-test on eye pain', () => {
    const answers = getTriageQuestions().map(question => ({
      questionId: question.id,
      value: question.id === 'eye-pain',
    }));

    expect(evaluateTriage(answers)).toMatchObject({
      canContinueSelfTest: false,
      recommendation: 'urgentCare',
    });
  });

  it('blocks self-test on flashes-or-floaters', () => {
    const answers = getTriageQuestions().map(question => ({
      questionId: question.id,
      value: question.id === 'flashes-or-floaters',
    }));

    expect(evaluateTriage(answers)).toMatchObject({
      canContinueSelfTest: false,
      recommendation: 'urgentCare',
    });
  });

  it('blocks self-test on double-vision', () => {
    const answers = getTriageQuestions().map(question => ({
      questionId: question.id,
      value: question.id === 'double-vision',
    }));

    expect(evaluateTriage(answers)).toMatchObject({
      canContinueSelfTest: false,
      recommendation: 'seekProfessionalCare',
    });
  });

  it('blocks self-test on recent-eye-trauma', () => {
    const answers = getTriageQuestions().map(question => ({
      questionId: question.id,
      value: question.id === 'recent-eye-trauma',
    }));

    expect(evaluateTriage(answers)).toMatchObject({
      canContinueSelfTest: false,
      recommendation: 'urgentCare',
    });
  });

  it('blocks self-test on severe-redness', () => {
    const answers = getTriageQuestions().map(question => ({
      questionId: question.id,
      value: question.id === 'severe-redness',
    }));

    expect(evaluateTriage(answers)).toMatchObject({
      canContinueSelfTest: false,
      recommendation: 'seekProfessionalCare',
    });
  });

  it('blocks self-test on known-glaucoma', () => {
    const answers = getTriageQuestions().map(question => ({
      questionId: question.id,
      value: question.id === 'known-glaucoma',
    }));

    expect(evaluateTriage(answers)).toMatchObject({
      canContinueSelfTest: false,
      recommendation: 'seekProfessionalCare',
    });
  });

  it('blocks self-test on diabetes-related-risk', () => {
    const answers = getTriageQuestions().map(question => ({
      questionId: question.id,
      value: question.id === 'diabetes-related-risk',
    }));

    expect(evaluateTriage(answers)).toMatchObject({
      canContinueSelfTest: false,
      recommendation: 'seekProfessionalCare',
    });
  });

  it('blocks self-test on recent-eye-surgery', () => {
    const answers = getTriageQuestions().map(question => ({
      questionId: question.id,
      value: question.id === 'recent-eye-surgery',
    }));

    expect(evaluateTriage(answers)).toMatchObject({
      canContinueSelfTest: false,
      recommendation: 'seekProfessionalCare',
    });
  });
});
