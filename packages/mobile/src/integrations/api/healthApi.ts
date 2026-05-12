import {buildApiUrl, type ApiClientConfig} from './client';

export type HealthStatus = {
  ok: boolean;
  status?: string;
};

export const getHealthStatus = async (
  config?: ApiClientConfig,
): Promise<HealthStatus> => {
  try {
    const response = await fetch(buildApiUrl('/health', config));
    if (!response.ok) {
      return {ok: false, status: `${response.status}`};
    }

    return {ok: true, status: 'reachable'};
  } catch {
    return {ok: false, status: 'offline'};
  }
};
