import { apiClient, buildPaginationQuery } from "@/shared/api";
import type { PaginatedResponse } from "@/shared/types/pagination";

import type { Post, PostListParams, UpdatePostPayload } from "../model/types";

const BASE_PATH = "/api/v1/posts";

export const postApi = {
  getList(params: PostListParams): Promise<PaginatedResponse<Post>> {
    return apiClient<PaginatedResponse<Post>>(`${BASE_PATH}${buildPaginationQuery(params)}`);
  },

  update(externalId: number, payload: UpdatePostPayload): Promise<Post> {
    return apiClient<Post>(`${BASE_PATH}/${externalId}`, {
      method: "PUT",
      body: payload,
    });
  },

  delete(externalId: number): Promise<void> {
    return apiClient<void>(`${BASE_PATH}/${externalId}`, {
      method: "DELETE",
    });
  },
};
