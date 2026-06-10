import { useCallback, useState } from "react";

import type { SortOrder } from "@/shared/types/pagination";

import { getNextSortState } from "./getNextSortState";

type SortState<TField extends string> = {
  sortBy: TField;
  sortOrder: SortOrder;
};

export function useSortState<TField extends string>(
  initialField: TField,
  initialOrder: SortOrder = "asc",
) {
  const [sort, setSort] = useState<SortState<TField>>({
    sortBy: initialField,
    sortOrder: initialOrder,
  });

  const toggleSort = useCallback((field: TField) => {
    setSort((current) => getNextSortState(current, field));
  }, []);

  return { sortBy: sort.sortBy, sortOrder: sort.sortOrder, toggleSort };
}
