import { memo, useCallback } from "react";

import { useDeleteUserMutation, type User, type UserSortField } from "@/entities/user";
import { UserPostsPanel } from "@/features/post";
import { useEditUserStore } from "@/features/user";
import { Button, DataTable, DataTableHeaderCell, SortableTableHeader } from "@/shared/ui";
import { useUsersListStore } from "@/widgets/user-list/model/usersListStore";

type UserTableProps = {
  users: User[];
};

const USER_COLUMNS: { field: UserSortField; label: string }[] = [
  { field: "external_id", label: "ID" },
  { field: "first_name", label: "First name" },
  { field: "last_name", label: "Last name" },
  { field: "email", label: "Email" },
  { field: "username", label: "Username" },
  { field: "role", label: "Role" },
];

export const UserTable = memo(function UserTable({ users }: UserTableProps) {
  const sortBy = useUsersListStore((state) => state.sortBy);
  const sortOrder = useUsersListStore((state) => state.sortOrder);
  const toggleSort = useUsersListStore((state) => state.toggleSort);

  if (users.length === 0) {
    return <p className="user-list__empty">No users found.</p>;
  }

  return (
    <DataTable className="user-list__table">
      <thead>
        <tr>
          <DataTableHeaderCell className="user-list__col-expand" />
          {USER_COLUMNS.map((column) => (
            <SortableTableHeader
              key={column.field}
              label={column.label}
              field={column.field}
              activeField={sortBy}
              sortOrder={sortOrder}
              onSort={(field) => toggleSort(field as UserSortField)}
            />
          ))}
          <DataTableHeaderCell className="user-list__col-actions">Actions</DataTableHeaderCell>
        </tr>
      </thead>
      <tbody>
        {users.map((user) => (
          <UserTableRow key={user.external_id} user={user} />
        ))}
      </tbody>
    </DataTable>
  );
});

type UserTableRowProps = {
  user: User;
};

const UserTableRow = memo(function UserTableRow({ user }: UserTableRowProps) {
  const isExpanded = useUsersListStore((state) => Boolean(state.expandedUserIds[user.external_id]));
  const toggleExpanded = useUsersListStore((state) => state.toggleExpanded);
  const openEdit = useEditUserStore((state) => state.openEdit);
  const { mutate, isPending } = useDeleteUserMutation();

  const handleDelete = useCallback(() => {
    if (!window.confirm(`Delete ${user.username}?`)) {
      return;
    }

    mutate(user.external_id);
  }, [mutate, user.external_id, user.username]);

  return (
    <>
      <tr>
        <td className="user-list__col-expand">
          <button
            type="button"
            className={[
              "data-table__expand-btn",
              isExpanded ? "data-table__expand-btn--expanded" : "",
            ]
              .filter(Boolean)
              .join(" ")}
            onClick={() => toggleExpanded(user.external_id)}
            aria-expanded={isExpanded}
            aria-label={isExpanded ? "Hide posts" : "Show posts"}
          >
            {isExpanded ? "−" : "+"}
          </button>
        </td>
        <td>{user.external_id}</td>
        <td>{user.first_name}</td>
        <td>{user.last_name}</td>
        <td className="data-table__cell-truncate" title={user.email}>
          {user.email}
        </td>
        <td>{user.username}</td>
        <td>
          <span className="user-list__role-badge">{user.role}</span>
        </td>
        <td className="user-list__col-actions">
          <div className="data-table__actions">
            <Button variant="secondary" onClick={() => openEdit(user)}>
              Edit
            </Button>
            <Button variant="danger" disabled={isPending} onClick={handleDelete}>
              {isPending ? "Deleting..." : "Delete"}
            </Button>
          </div>
        </td>
      </tr>
      {isExpanded ? (
        <tr className="data-table__expanded-row">
          <td colSpan={USER_COLUMNS.length + 2}>
            <UserPostsPanel userExternalId={user.external_id} />
          </td>
        </tr>
      ) : null}
    </>
  );
});
