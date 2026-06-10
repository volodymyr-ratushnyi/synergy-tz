import { useUpdatePostMutation, type UpdatePostPayload } from "@/entities/post";
import { useEditMutationSubmit, Modal } from "@/shared/ui";

import { toPostPayload } from "../lib/toPostPayload";
import type { PostFormValues } from "../lib/validatePostForm";
import { useEditPostStore } from "../model/editPostStore";
import { PostEditForm } from "./PostEditForm";

export function PostEditModal() {
  const post = useEditPostStore((state) => state.editingEntity);
  const closeEdit = useEditPostStore((state) => state.closeEdit);
  const { mutateAsync, isPending, error, reset } = useUpdatePostMutation();

  const { handleSubmit, submitError } = useEditMutationSubmit<PostFormValues, UpdatePostPayload>({
    externalId: post?.external_id ?? 0,
    mutateAsync,
    reset,
    error,
    onClose: closeEdit,
    fallbackMessage: "Failed to save post. Please try again.",
    toPayload: toPostPayload,
  });

  if (!post) {
    return null;
  }

  return (
    <Modal title={`Edit post #${post.external_id}`} onClose={closeEdit}>
      <PostEditForm
        post={post}
        isSubmitting={isPending}
        submitError={submitError}
        onSubmit={handleSubmit}
        onCancel={closeEdit}
      />
    </Modal>
  );
}
