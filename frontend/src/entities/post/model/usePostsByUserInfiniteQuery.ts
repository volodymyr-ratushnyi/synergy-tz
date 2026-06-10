import { useInfiniteQuery } from "@tanstack/react-query";

import { getOffsetNextPageParam } from "@/shared/lib";
import { LIST_PAGE_SIZE } from "@/shared/types/pagination";

import { postApi } from "../api/postApi";
import { postQueryKeys, type PostsByUserQueryParams } from "./post-query-keys";

export function usePostsByUserInfiniteQuery(
  userExternalId: number,
  params: Pick<PostsByUserQueryParams, "limit" | "sort_by" | "sort_order">,
) {
  const fullParams: PostsByUserQueryParams = {
    ...params,
    user_external_id: userExternalId,
  };

  return useInfiniteQuery({
    queryKey: postQueryKeys.infiniteList(fullParams),
    queryFn: ({ pageParam }) => postApi.getList({ ...fullParams, offset: pageParam }),
    initialPageParam: 0,
    getNextPageParam: getOffsetNextPageParam,
  });
}

export { LIST_PAGE_SIZE as POSTS_PAGE_SIZE };
