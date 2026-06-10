import type { Post } from "@/entities/post";
import { createEditStore } from "@/shared/ui";

export const useEditPostStore = createEditStore<Post>();
