type QueryParamValue = string | number | boolean | undefined;

export function buildPaginationQuery(params: Record<string, QueryParamValue>): string {
  const search = new URLSearchParams();

  for (const [key, value] of Object.entries(params)) {
    if (value !== undefined) {
      search.set(key, String(value));
    }
  }

  return `?${search.toString()}`;
}
