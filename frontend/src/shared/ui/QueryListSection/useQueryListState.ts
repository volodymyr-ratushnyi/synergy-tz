type QueryListStateInput = {
  isPending: boolean;
  isFetching: boolean;
  hasData: boolean;
};

export function useQueryListState({ isPending, isFetching, hasData }: QueryListStateInput) {
  return {
    isInitialLoad: isPending && !hasData,
    isRefetching: isFetching && !isPending,
  };
}
