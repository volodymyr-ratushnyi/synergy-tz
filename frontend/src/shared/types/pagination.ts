export const LIST_PAGE_SIZE = 20;

export type SortOrder = "asc" | "desc";

export type PaginationParams<TSortField extends string = string> = {
  offset: number;
  limit: number;
  sort_by: TSortField;
  sort_order: SortOrder;
};

export type PaginatedResponse<T> = {
  items: T[];
  total: number;
  offset: number;
  limit: number;
};
