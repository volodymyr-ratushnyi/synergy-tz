export const USER_ROLE_OPTIONS = [
  { value: "user", label: "User" },
  { value: "admin", label: "Admin" },
  { value: "moderator", label: "Moderator" },
] as const;

export type UserRole = (typeof USER_ROLE_OPTIONS)[number]["value"];

export type User = {
  external_id: number;
  first_name: string;
  last_name: string;
  email: string;
  username: string;
  image: string;
  role: UserRole;
};

export type UpdateUserPayload = {
  first_name?: string;
  last_name?: string;
  email?: string;
  username?: string;
  image?: string;
  role?: UserRole;
};

export type UserSortField =
  | "external_id"
  | "first_name"
  | "last_name"
  | "email"
  | "username"
  | "role";
