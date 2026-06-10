import { useCallback } from "react";

import { useInfiniteScrollTrigger } from "@/shared/lib/useInfiniteScrollTrigger";

import { Spinner } from "../Spinner/Spinner";

import "./LoadMoreSentinel.scss";

type LoadMoreSentinelProps = {
  hasMore: boolean;
  isLoadingMore: boolean;
  onLoadMore: () => void;
  loadingLabel?: string;
  endLabel?: string;
};

export function LoadMoreSentinel({
  hasMore,
  isLoadingMore,
  onLoadMore,
  loadingLabel = "Loading more...",
  endLabel,
}: LoadMoreSentinelProps) {
  const handleLoadMore = useCallback(() => {
    onLoadMore();
  }, [onLoadMore]);

  const sentinelRef = useInfiniteScrollTrigger({
    enabled: hasMore && !isLoadingMore,
    onLoadMore: handleLoadMore,
  });

  if (!hasMore && !isLoadingMore && endLabel) {
    return <p className="load-more-sentinel__end">{endLabel}</p>;
  }

  if (!hasMore && !isLoadingMore) {
    return null;
  }

  return (
    <div className="load-more-sentinel" ref={sentinelRef}>
      {isLoadingMore ? <Spinner label={loadingLabel} /> : null}
    </div>
  );
}
