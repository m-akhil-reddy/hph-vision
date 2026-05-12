import type {ValidationResult} from '../validation';

export type NotchMask = {
  kind: 'none' | 'notch' | 'punch-hole' | 'dynamic-island' | 'unknown';
  xMm?: number;
  yMm?: number;
  widthMm?: number;
  heightMm?: number;
};

export type DeviceProfile = {
  id: string;
  manufacturer: string;
  modelName: string;
  modelNumber?: string;
  bodyWidthMm: number;
  bodyHeightMm: number;
  thicknessMm: number;
  screenWidthPx: number;
  screenHeightPx: number;
  pixelDensity: number;
  screenWidthMm?: number;
  screenHeightMm?: number;
  activeDisplayOffsetXmm?: number;
  activeDisplayOffsetYmm?: number;
  notchMask?: NotchMask;
  templateFamily: string;
};

export type PhoneGeometry = {
  modelName: string;
  bodyWidthMm: number;
  bodyHeightMm: number;
  thicknessMm: number;
  screenWidthMm?: number;
  screenHeightMm?: number;
  screenOffsetXmm?: number;
  screenOffsetYmm?: number;
};

export type DeviceDetectionInput = {
  manufacturer?: string;
  modelName?: string;
  modelNumber?: string;
  os?: 'ios' | 'android';
  screenWidthPx?: number;
  screenHeightPx?: number;
  pixelDensity?: number;
};

export type DeviceProfileMatch = {
  profile?: DeviceProfile;
  confidence: number;
  reason: string;
  alternatives: DeviceProfile[];
  requiresManualConfirmation: boolean;
};

export type DeviceProfileValidationResult = ValidationResult<DeviceProfile>;
