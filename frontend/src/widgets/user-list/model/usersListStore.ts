import { create } from "zustand";

import type { UserSortField } from "@/entities/user";
import { getNextSortState } from "@/shared/lib";
import { LIST_PAGE_SIZE, type SortOrder } from "@/shared/types/pagination";

type UsersListStore = {
  limit: number;
  sortBy: UserSortField;
  sortOrder: SortOrder;
  expandedUserIds: Record<number, true>;
  toggleSort: (field: UserSortField) => void;
  toggleExpanded: (userId: number) => void;
};

export const useUsersListStore = create<UsersListStore>((set) => ({
  limit: LIST_PAGE_SIZE,
  sortBy: "external_id",
  sortOrder: "asc",
  expandedUserIds: {},

  toggleSort: (field) =>
    set((state) => ({
      ...getNextSortState(state, field),
      expandedUserIds: {},
    })),

  toggleExpanded: (userId) =>
    set((state) => {
      const next = { ...state.expandedUserIds };

      if (next[userId]) {
        delete next[userId];
      } else {
        next[userId] = true;
      }

      return { expandedUserIds: next };
    }),
}));
