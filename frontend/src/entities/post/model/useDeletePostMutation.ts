import { useMutation, useQueryClient } from "@tanstack/react-query";

import { postApi } from "../api/postApi";
import { postQueryKeys } from "./post-query-keys";

export function useDeletePostMutation() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (externalId: number) => postApi.delete(externalId),
    onSuccess: () => {
      void queryClient.invalidateQueries({ queryKey: postQueryKeys.all });
    },
  });
}
