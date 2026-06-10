import type { PostListParams } from "./types";

export type PostsByUserQueryParams = Pick<
  PostListParams,
  "limit" | "sort_by" | "sort_order" | "user_external_id"
>;

export const postQueryKeys = {
  all: ["posts"] as const,
  lists: () => [...postQueryKeys.all, "list"] as const,
  infiniteList: (params: PostsByUserQueryParams) =>
    [...postQueryKeys.lists(), "infinite", params] as const,
};
