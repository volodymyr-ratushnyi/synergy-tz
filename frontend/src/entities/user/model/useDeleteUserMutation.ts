import { useMutation, useQueryClient } from "@tanstack/react-query";

import { userApi } from "../api/userApi";
import { userQueryKeys } from "./user-query-keys";

export function useDeleteUserMutation() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (externalId: number) => userApi.delete(externalId),
    onSuccess: () => {
      void queryClient.invalidateQueries({ queryKey: userQueryKeys.all });
    },
  });
}
