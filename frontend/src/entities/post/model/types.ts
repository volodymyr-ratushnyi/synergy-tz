import type { PaginationParams } from "@/shared/types/pagination";

export type Post = {
  external_id: number;
  user_external_id: number;
  title: string;
  body: string;
  views: number;
  tags: string[];
  reactions: Record<string, number>;
};

export type UpdatePostPayload = {
  title?: string;
  body?: string;
  views?: number;
  tags?: string[];
};

export type PostSortField = "external_id" | "title" | "views";

export type PostListParams = PaginationParams<PostSortField> & {
  user_external_id?: number;
};
