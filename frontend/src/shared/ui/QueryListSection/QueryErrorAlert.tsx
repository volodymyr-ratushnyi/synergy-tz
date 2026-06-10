import { getErrorMessage } from "@/shared/lib";

import { Alert } from "../Alert/Alert";

type QueryErrorAlertProps = {
  error: Error | null;
  isError: boolean;
  onRetry?: () => void;
  title?: string;
  fallbackMessage?: string;
};

export function QueryErrorAlert({
  error,
  isError,
  onRetry,
  title = "Failed to load data",
  fallbackMessage,
}: QueryErrorAlertProps) {
  if (!isError || !error) {
    return null;
  }

  return (
    <Alert title={title} onRetry={onRetry ? () => void onRetry() : undefined}>
      {getErrorMessage(error, fallbackMessage)}
    </Alert>
  );
}
