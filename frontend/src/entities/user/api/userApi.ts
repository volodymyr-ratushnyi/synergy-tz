import { apiClient, buildPaginationQuery } from "@/shared/api";
import type { PaginatedResponse, PaginationParams } from "@/shared/types/pagination";

import type { UpdateUserPayload, User, UserSortField } from "../model/types";

const BASE_PATH = "/api/v1/users";

export const userApi = {
  getList(params: PaginationParams<UserSortField>): Promise<PaginatedResponse<User>> {
    return apiClient<PaginatedResponse<User>>(`${BASE_PATH}${buildPaginationQuery(params)}`);
  },

  update(externalId: number, payload: UpdateUserPayload): Promise<User> {
    return apiClient<User>(`${BASE_PATH}/${externalId}`, {
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
