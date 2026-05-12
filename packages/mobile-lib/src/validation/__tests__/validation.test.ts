import {describe, expect, it} from '@jest/globals';

import {combineValidationResults, invalid, valid, validationIssue} from '..';

describe('combineValidationResults', () => {
  it('combines errors', () => {
    const result = combineValidationResults(
      valid('ok'),
      invalid([validationIssue('bad', 'Bad value')]),
    );

    expect(result.ok).toBe(false);
  });
});
