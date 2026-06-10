import { useMutation, useQueryClient } from "@tanstack/react-query";

import { postApi } from "../api/postApi";
import type { UpdatePostPayload } from "./types";
import { postQueryKeys } from "./post-query-keys";

type UpdatePostVariables = {
  externalId: number;
  payload: UpdatePostPayload;
};

export function useUpdatePostMutation() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ externalId, payload }: UpdatePostVariables) =>
      postApi.update(externalId, payload),
    onSuccess: () => {
      void queryClient.invalidateQueries({ queryKey: postQueryKeys.all });
    },
  });
}
