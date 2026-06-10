import type { SortOrder } from "@/shared/types/pagination";

type SortState<TField extends string> = {
  sortBy: TField;
  sortOrder: SortOrder;
};

export function getNextSortState<TField extends string>(
  current: SortState<TField>,
  field: TField,
): SortState<TField> {
  if (current.sortBy === field) {
    return {
      sortBy: field,
      sortOrder: current.sortOrder === "asc" ? "desc" : "asc",
    };
  }

  return { sortBy: field, sortOrder: "asc" };
}
