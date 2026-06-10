import { useMutation, useQueryClient } from "@tanstack/react-query";

import { userApi } from "../api/userApi";
import type { UpdateUserPayload } from "./types";
import { userQueryKeys } from "./user-query-keys";

type UpdateUserVariables = {
  externalId: number;
  payload: UpdateUserPayload;
};

export function useUpdateUserMutation() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ externalId, payload }: UpdateUserVariables) =>
      userApi.update(externalId, payload),
    onSuccess: () => {
      void queryClient.invalidateQueries({ queryKey: userQueryKeys.all });
    },
  });
}
