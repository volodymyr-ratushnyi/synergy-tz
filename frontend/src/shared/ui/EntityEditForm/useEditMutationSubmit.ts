import { getErrorMessage } from "@/shared/lib";

type UseEditMutationSubmitParams<TValues, TPayload> = {
  externalId: number;
  mutateAsync: (variables: { externalId: number; payload: TPayload }) => Promise<unknown>;
  reset: () => void;
  error: Error | null;
  onClose: () => void;
  fallbackMessage: string;
  toPayload?: (values: TValues) => TPayload;
};

export function useEditMutationSubmit<TValues>(
  params: UseEditMutationSubmitParams<TValues, TValues> & { toPayload?: undefined },
): { handleSubmit: (values: TValues) => Promise<void>; submitError: string | null };

export function useEditMutationSubmit<TValues, TPayload>(
  params: UseEditMutationSubmitParams<TValues, TPayload> & {
    toPayload: (values: TValues) => TPayload;
  },
): { handleSubmit: (values: TValues) => Promise<void>; submitError: string | null };

export function useEditMutationSubmit<TValues, TPayload = TValues>({
  externalId,
  mutateAsync,
  reset,
  error,
  onClose,
  fallbackMessage,
  toPayload,
}: UseEditMutationSubmitParams<TValues, TPayload>) {
  const submitError = error ? getErrorMessage(error, fallbackMessage) : null;

  const handleSubmit = async (values: TValues) => {
    reset();

    try {
      const payload = toPayload ? toPayload(values) : (values as TValues & TPayload);
      await mutateAsync({ externalId, payload });
      onClose();
    } catch {
      // Error is surfaced via mutation.error
    }
  };

  return { handleSubmit, submitError };
}
