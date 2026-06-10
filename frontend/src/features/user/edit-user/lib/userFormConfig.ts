import { USER_ROLE_OPTIONS, type User } from "@/entities/user";
import type { FormFieldConfig } from "@/shared/ui";

import type { UserFormValues } from "./validateUserForm";

export const USER_FORM_FIELDS: FormFieldConfig<UserFormValues>[] = [
  { kind: "input", name: "first_name", label: "First name" },
  { kind: "input", name: "last_name", label: "Last name" },
  { kind: "input", name: "email", label: "Email", type: "email" },
  { kind: "input", name: "username", label: "Username" },
  { kind: "input", name: "image", label: "Image URL" },
  {
    kind: "select",
    name: "role",
    label: "Role",
    options: [...USER_ROLE_OPTIONS],
  },
];

export function toUserFormValues(user: User): UserFormValues {
  return {
    first_name: user.first_name,
    last_name: user.last_name,
    email: user.email,
    username: user.username,
    image: user.image,
    role: user.role,
  };
}
