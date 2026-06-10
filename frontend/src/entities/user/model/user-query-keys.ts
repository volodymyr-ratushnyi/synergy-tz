import type { UserSortField } from "./types";

export type UsersListQueryParams = {
  limit: number;
  sort_by: UserSortField;
  sort_order: "asc" | "desc";
};

export const userQueryKeys = {
  all: ["users"] as const,
  lists: () => [...userQueryKeys.all, "list"] as const,
  infiniteList: (params: UsersListQueryParams) =>
    [...userQueryKeys.lists(), "infinite", params] as const,
};
