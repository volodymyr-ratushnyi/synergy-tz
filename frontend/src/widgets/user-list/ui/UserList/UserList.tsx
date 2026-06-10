import { PostEditModal } from "@/features/post";
import { UserEditModal } from "@/features/user";

import { UserListTableSection } from "../UserListTableSection";

import "./UserList.scss";

export function UserList() {
  return (
    <section className="user-list">
      <header className="user-list__header">
        <div>
          <h1 className="user-list__title">Users</h1>
          <p className="user-list__subtitle">
            Sort columns, scroll to load more, expand a row to manage posts.
          </p>
        </div>
      </header>
      <UserListTableSection />
      <UserEditModal />
      <PostEditModal />
    </section>
  );
}
