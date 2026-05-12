import React from 'react';
import {useHphVisionApp} from '../state/sessionStore';
import {AppProvider} from './AppProvider';
import type {AppRoute} from './routes';
import {AcuityTestScreen} from '../features/acuity-test/AcuityTestScreen';
import {ClinicianReviewScreen} from '../features/clinician-review/ClinicianReviewScreen';
import {DeviceCalibrationScreen} from '../features/device-calibration/DeviceCalibrationScreen';
import {DisclaimerScreen} from '../features/disclaimer/DisclaimerScreen';
import {OnboardingScreen} from '../features/onboarding/OnboardingScreen';
import {RefractionTestScreen} from '../features/refraction-test/RefractionTestScreen';
import {ReportScreen} from '../features/reporting/ReportScreen';
import {ResultsScreen} from '../features/results/ResultsScreen';
import {SettingsScreen} from '../features/settings/SettingsScreen';
import {TemplateGenerationScreen} from '../features/template-generation/TemplateGenerationScreen';
import {TriageScreen} from '../features/triage/TriageScreen';
import {VisorAssemblyScreen} from '../features/visor-assembly/VisorAssemblyScreen';

const screens: Record<AppRoute, React.ComponentType> = {
  disclaimer: DisclaimerScreen,
  onboarding: OnboardingScreen,
  triage: TriageScreen,
  deviceCalibration: DeviceCalibrationScreen,
  templateGeneration: TemplateGenerationScreen,
  visorAssembly: VisorAssemblyScreen,
  acuityTest: AcuityTestScreen,
  refractionTest: RefractionTestScreen,
  results: ResultsScreen,
  reporting: ReportScreen,
  clinicianReview: ClinicianReviewScreen,
  settings: SettingsScreen,
};

const CurrentScreen = () => {
  const {state} = useHphVisionApp();
  const ScreenComponent = screens[state.route];

  return <ScreenComponent />;
};

const RootApp = () => (
  <AppProvider>
    <CurrentScreen />
  </AppProvider>
);

export default RootApp;
