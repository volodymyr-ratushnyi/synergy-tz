import type { UpdatePostPayload } from "@/entities/post";

import { parseTags, type PostFormValues } from "./validatePostForm";

export function toPostPayload(values: PostFormValues): UpdatePostPayload {
  return {
    title: values.title.trim(),
    body: values.body.trim(),
    views: Number(values.views),
    tags: parseTags(values.tags),
  };
}
