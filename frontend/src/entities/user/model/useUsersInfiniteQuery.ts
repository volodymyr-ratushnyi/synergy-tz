import { useInfiniteQuery } from "@tanstack/react-query";

import { getOffsetNextPageParam } from "@/shared/lib";

import { userApi } from "../api/userApi";
import { userQueryKeys, type UsersListQueryParams } from "./user-query-keys";

export function useUsersInfiniteQuery(params: UsersListQueryParams) {
  return useInfiniteQuery({
    queryKey: userQueryKeys.infiniteList(params),
    queryFn: ({ pageParam }) => userApi.getList({ ...params, offset: pageParam }),
    initialPageParam: 0,
    getNextPageParam: getOffsetNextPageParam,
  });
}
