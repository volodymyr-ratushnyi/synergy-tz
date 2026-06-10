import type { User } from "@/entities/user";
import { EntityEditForm } from "@/shared/ui";

import { toUserFormValues, USER_FORM_FIELDS } from "../lib/userFormConfig";
import { validateUserForm, type UserFormValues } from "../lib/validateUserForm";

type UserEditFormProps = {
  user: User;
  isSubmitting: boolean;
  submitError: string | null;
  onSubmit: (values: UserFormValues) => void;
  onCancel: () => void;
};

export function UserEditForm({ user, ...formProps }: UserEditFormProps) {
  return (
    <EntityEditForm
      key={user.external_id}
      initialValues={toUserFormValues(user)}
      fields={USER_FORM_FIELDS}
      validate={validateUserForm}
      {...formProps}
    />
  );
}
