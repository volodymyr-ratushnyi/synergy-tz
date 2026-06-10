import type { Post } from "@/entities/post";
import { EntityEditForm } from "@/shared/ui";

import { POST_FORM_FIELDS, toPostFormValues } from "../lib/postFormConfig";
import { validatePostForm, type PostFormValues } from "../lib/validatePostForm";

type PostEditFormProps = {
  post: Post;
  isSubmitting: boolean;
  submitError: string | null;
  onSubmit: (values: PostFormValues) => void;
  onCancel: () => void;
};

export function PostEditForm({ post, ...formProps }: PostEditFormProps) {
  return (
    <EntityEditForm
      key={post.external_id}
      initialValues={toPostFormValues(post)}
      fields={POST_FORM_FIELDS}
      validate={validatePostForm}
      {...formProps}
    />
  );
}
