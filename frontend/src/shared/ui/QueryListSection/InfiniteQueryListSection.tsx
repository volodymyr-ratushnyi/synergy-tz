import type { UseInfiniteQueryResult } from "@tanstack/react-query";
import type { ReactNode } from "react";
import { useCallback } from "react";

import { LoadMoreSentinel } from "./LoadMoreSentinel";
import { QueryListSection } from "./QueryListSection";
import type { QueryListLabels } from "./types";

type InfiniteQueryListSectionProps = {
  query: Pick<
    UseInfiniteQueryResult<unknown, Error>,
    | "data"
    | "isPending"
    | "isFetching"
    | "isFetchingNextPage"
    | "isError"
    | "error"
    | "refetch"
    | "hasNextPage"
    | "fetchNextPage"
  >;
  labels: QueryListLabels;
  areaClassName?: string;
  hasItems?: boolean;
  children: ReactNode;
};

export function InfiniteQueryListSection({
  query,
  labels,
  areaClassName,
  hasItems = false,
  children,
}: InfiniteQueryListSectionProps) {
  const { fetchNextPage } = query;

  const handleLoadMore = useCallback(() => {
    void fetchNextPage();
  }, [fetchNextPage]);

  return (
    <QueryListSection
      isPending={query.isPending}
      isFetching={query.isFetching && !query.isFetchingNextPage}
      isError={query.isError}
      error={query.error}
      refetch={query.refetch}
      hasData={Boolean(query.data)}
      labels={labels}
      areaClassName={areaClassName}
      footer={
        <LoadMoreSentinel
          hasMore={Boolean(query.hasNextPage)}
          isLoadingMore={query.isFetchingNextPage}
          onLoadMore={handleLoadMore}
          loadingLabel={labels.loadingMoreLabel}
          endLabel={hasItems ? labels.allLoadedLabel : undefined}
        />
      }
    >
      {children}
    </QueryListSection>
  );
}
