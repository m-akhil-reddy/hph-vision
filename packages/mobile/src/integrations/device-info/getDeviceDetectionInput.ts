import {Dimensions, PixelRatio, Platform} from 'react-native';
import type {DeviceDetectionInput} from '@hiperhealth/hphvision-lib';

export const getDeviceDetectionInput = (): DeviceDetectionInput => {
  const window = Dimensions.get('window');
  const scale = PixelRatio.get();

  return {
    os: Platform.OS === 'ios' ? 'ios' : 'android',
    screenWidthPx: Math.round(window.width * scale),
    screenHeightPx: Math.round(window.height * scale),
    pixelDensity: scale,
  };
};
