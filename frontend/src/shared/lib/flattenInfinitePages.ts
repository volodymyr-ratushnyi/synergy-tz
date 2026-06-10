import type { PaginatedResponse } from "@/shared/types/pagination";

export function flattenInfinitePages<T>(pages: PaginatedResponse<T>[] | undefined): T[] {
  return pages?.flatMap((page) => page.items) ?? [];
}

export function getInfiniteTotal<T>(pages: PaginatedResponse<T>[] | undefined): number {
  return pages?.[0]?.total ?? 0;
}

export function getOffsetNextPageParam<T>(lastPage: PaginatedResponse<T>): number | undefined {
  const nextOffset = lastPage.offset + lastPage.limit;
  return nextOffset < lastPage.total ? nextOffset : undefined;
}
