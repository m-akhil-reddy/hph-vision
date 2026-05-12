import {toPhoneGeometry} from '../device-profile';
import type {TemplateInput} from '../template-generator';
import {fixtureMediumPhone} from './devices';

export const fixtureTemplateInput: TemplateInput = {
  phone: toPhoneGeometry(fixtureMediumPhone),
  options: {
    pageSize: 'A4',
    cardboardThicknessMm: 1.5,
    eyeToScreenDistanceMm: 250,
    includeAssemblyInstructions: true,
  },
};
