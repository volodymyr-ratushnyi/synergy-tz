import { useMemo } from "react";
import { useShallow } from "zustand/react/shallow";

import { useUsersInfiniteQuery, type UsersListQueryParams } from "@/entities/user";

import { useUsersListStore } from "./usersListStore";

export function useUsersListParams(): UsersListQueryParams {
  const { limit, sortBy, sortOrder } = useUsersListStore(
    useShallow((state) => ({
      limit: state.limit,
      sortBy: state.sortBy,
      sortOrder: state.sortOrder,
    })),
  );

  return useMemo(
    () => ({
      limit,
      sort_by: sortBy,
      sort_order: sortOrder,
    }),
    [limit, sortBy, sortOrder],
  );
}

export function useUsersListData() {
  const params = useUsersListParams();
  return useUsersInfiniteQuery(params);
}
