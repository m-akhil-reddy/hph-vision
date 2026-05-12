export type ApiClientConfig = {
  baseUrl: string;
  timeoutMs: number;
};

export const defaultApiClientConfig: ApiClientConfig = {
  baseUrl: 'http://localhost:8000',
  timeoutMs: 10000,
};

export const buildApiUrl = (
  path: string,
  config: ApiClientConfig = defaultApiClientConfig,
): string => {
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  return `${config.baseUrl}${normalizedPath}`;
};
