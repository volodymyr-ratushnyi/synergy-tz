import { memo } from "react";

import { POSTS_PAGE_SIZE, usePostsByUserInfiniteQuery, type PostSortField } from "@/entities/post";
import { flattenInfinitePages, getInfiniteTotal, useSortState } from "@/shared/lib";
import { createQueryListLabels, InfiniteQueryListSection } from "@/shared/ui";

import { PostsTable } from "../PostsTable/PostsTable";

import "./UserPostsPanel.scss";

type UserPostsPanelProps = {
  userExternalId: number;
};

export const UserPostsPanel = memo(function UserPostsPanel({
  userExternalId,
}: UserPostsPanelProps) {
  const { sortBy, sortOrder, toggleSort } = useSortState<PostSortField>("external_id");

  const query = usePostsByUserInfiniteQuery(userExternalId, {
    limit: POSTS_PAGE_SIZE,
    sort_by: sortBy,
    sort_order: sortOrder,
  });

  const posts = flattenInfinitePages(query.data?.pages);
  const total = getInfiniteTotal(query.data?.pages);

  return (
    <div className="user-posts-panel">
      <div className="user-posts-panel__header">
        <h3 className="user-posts-panel__title">
          Posts ({posts.length} of {total})
        </h3>
      </div>

      <InfiniteQueryListSection
        query={query}
        labels={createQueryListLabels("posts")}
        areaClassName="user-posts-panel__table-area"
        hasItems={posts.length > 0}
      >
        <PostsTable posts={posts} sortBy={sortBy} sortOrder={sortOrder} onSort={toggleSort} />
      </InfiniteQueryListSection>
    </div>
  );
});
