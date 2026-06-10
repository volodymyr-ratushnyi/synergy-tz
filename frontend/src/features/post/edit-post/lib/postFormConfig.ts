import type { Post } from "@/entities/post";
import type { FormFieldConfig } from "@/shared/ui";

import { formatTags, type PostFormValues } from "./validatePostForm";

export const POST_FORM_FIELDS: FormFieldConfig<PostFormValues>[] = [
  { kind: "input", name: "title", label: "Title" },
  { kind: "input", name: "body", label: "Body" },
  { kind: "input", name: "views", label: "Views", type: "number", min: 0 },
  { kind: "input", name: "tags", label: "Tags (comma-separated)" },
];

export function toPostFormValues(post: Post): PostFormValues {
  return {
    title: post.title,
    body: post.body,
    views: String(post.views),
    tags: formatTags(post.tags),
  };
}
