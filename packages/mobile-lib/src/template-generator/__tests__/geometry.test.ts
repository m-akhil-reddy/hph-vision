import {describe, expect, it} from '@jest/globals';

import {fixtureTemplateInput} from '../../fixtures';
import {generateTemplateDocument} from '..';

describe('generateTemplateDocument', () => {
  it('creates an A4 template document with calibration square', () => {
    const result = generateTemplateDocument(
      fixtureTemplateInput.phone,
      fixtureTemplateInput.options,
    );

    expect(result.ok).toBe(true);
    if (!result.ok) {
      return;
    }
    expect(result.value.pages[0].pageSize).toBe('A4');
    expect(result.value.calibrationMarks[0]).toMatchObject({
      kind: 'square',
      expectedSizeMm: 50,
    });
  });
});
