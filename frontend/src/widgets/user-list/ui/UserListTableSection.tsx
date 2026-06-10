import { flattenInfinitePages, getInfiniteTotal } from "@/shared/lib";
import { createQueryListLabels, InfiniteQueryListSection } from "@/shared/ui";

import { useUsersListData } from "../model/useUsersListData";

import { UserTable } from "./UserTable/UserTable";

export function UserListTableSection() {
  const query = useUsersListData();
  const users = flattenInfinitePages(query.data?.pages);
  const total = getInfiniteTotal(query.data?.pages);

  return (
    <section className="user-list__section">
      <div className="user-list__meta">
        <p className="user-list__count">
          Showing {users.length} of {total} users
        </p>
      </div>

      <InfiniteQueryListSection
        query={query}
        labels={createQueryListLabels("users")}
        areaClassName="user-list__table-area"
        hasItems={users.length > 0}
      >
        <UserTable users={users} />
      </InfiniteQueryListSection>
    </section>
  );
}
