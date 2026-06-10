import { useUpdateUserMutation } from "@/entities/user";
import { useEditMutationSubmit, Modal } from "@/shared/ui";

import type { UserFormValues } from "../lib/validateUserForm";
import { useEditUserStore } from "../model/editUserStore";
import { UserEditForm } from "./UserEditForm";

export function UserEditModal() {
  const user = useEditUserStore((state) => state.editingEntity);
  const closeEdit = useEditUserStore((state) => state.closeEdit);
  const { mutateAsync, isPending, error, reset } = useUpdateUserMutation();

  const { handleSubmit, submitError } = useEditMutationSubmit<UserFormValues>({
    externalId: user?.external_id ?? 0,
    mutateAsync,
    reset,
    error,
    onClose: closeEdit,
    fallbackMessage: "Failed to save user. Please try again.",
  });

  if (!user) {
    return null;
  }

  return (
    <Modal title={`Edit user #${user.external_id}`} onClose={closeEdit}>
      <UserEditForm
        user={user}
        isSubmitting={isPending}
        submitError={submitError}
        onSubmit={handleSubmit}
        onCancel={closeEdit}
      />
    </Modal>
  );
}
