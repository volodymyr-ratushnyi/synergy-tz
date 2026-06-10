import { memo, useCallback } from "react";

import { useDeletePostMutation, type Post, type PostSortField } from "@/entities/post";
import { useEditPostStore } from "@/features/post";
import { Button, DataTable, DataTableHeaderCell, SortableTableHeader } from "@/shared/ui";
import type { SortOrder } from "@/shared/types/pagination";

type PostsTableProps = {
  posts: Post[];
  sortBy: PostSortField;
  sortOrder: SortOrder;
  onSort: (field: PostSortField) => void;
};

type PostTableColumn =
  | { kind: "sortable"; field: PostSortField; label: string }
  | { kind: "static"; label: string };

const POST_COLUMNS: PostTableColumn[] = [
  { kind: "sortable", field: "external_id", label: "ID" },
  { kind: "sortable", field: "title", label: "Title" },
  { kind: "static", label: "Body" },
  { kind: "sortable", field: "views", label: "Views" },
];

export const PostsTable = memo(function PostsTable({
  posts,
  sortBy,
  sortOrder,
  onSort,
}: PostsTableProps) {
  if (posts.length === 0) {
    return <p className="user-posts-panel__empty">No posts for this user.</p>;
  }

  return (
    <DataTable className="user-posts-panel__table">
      <thead>
        <tr>
          {POST_COLUMNS.map((column) =>
            column.kind === "sortable" ? (
              <SortableTableHeader
                key={column.field}
                label={column.label}
                field={column.field}
                activeField={sortBy}
                sortOrder={sortOrder}
                onSort={(field) => onSort(field as PostSortField)}
              />
            ) : (
              <DataTableHeaderCell key={column.label}>{column.label}</DataTableHeaderCell>
            ),
          )}
          <DataTableHeaderCell>Tags</DataTableHeaderCell>
          <DataTableHeaderCell className="user-posts-panel__col-actions">
            Actions
          </DataTableHeaderCell>
        </tr>
      </thead>
      <tbody>
        {posts.map((post) => (
          <PostTableRow key={post.external_id} post={post} />
        ))}
      </tbody>
    </DataTable>
  );
});

type PostTableRowProps = {
  post: Post;
};

const PostTableRow = memo(function PostTableRow({ post }: PostTableRowProps) {
  const openEdit = useEditPostStore((state) => state.openEdit);
  const { mutate, isPending } = useDeletePostMutation();

  const handleDelete = useCallback(() => {
    if (!window.confirm(`Delete "${post.title}"?`)) {
      return;
    }

    mutate(post.external_id);
  }, [mutate, post.external_id, post.title]);

  return (
    <tr>
      <td>{post.external_id}</td>
      <td className="data-table__cell-truncate" title={post.title}>
        {post.title}
      </td>
      <td className="data-table__cell-truncate data-table__cell-muted" title={post.body}>
        {post.body}
      </td>
      <td>{post.views}</td>
      <td className="data-table__cell-truncate" title={post.tags.join(", ")}>
        {post.tags.length > 0 ? post.tags.join(", ") : "—"}
      </td>
      <td className="user-posts-panel__col-actions">
        <div className="data-table__actions">
          <Button variant="secondary" onClick={() => openEdit(post)}>
            Edit
          </Button>
          <Button variant="danger" disabled={isPending} onClick={handleDelete}>
            {isPending ? "Deleting..." : "Delete"}
          </Button>
        </div>
      </td>
    </tr>
  );
});
