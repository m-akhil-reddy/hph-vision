export const normalizeCylinder = (cylinder: number): number =>
  Math.min(0, Math.round(cylinder / 0.25) * 0.25);

export const normalizeAxis = (axis: number): number => {
  const normalized = Math.round(axis) % 180;
  return normalized <= 0 ? normalized + 180 : normalized;
};
