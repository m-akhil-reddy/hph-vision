import type {DomainWarning} from '../types';

export const dedupeWarnings = (warnings: DomainWarning[]): DomainWarning[] => {
  const seen = new Set<string>();
  return warnings.filter(warning => {
    const key = `${warning.source ?? 'unknown'}:${warning.code}`;
    if (seen.has(key)) {
      return false;
    }
    seen.add(key);
    return true;
  });
};
