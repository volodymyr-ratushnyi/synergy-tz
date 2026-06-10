import type { ReactNode } from "react";

import { Spinner } from "../Spinner/Spinner";

import { FetchingTableArea } from "./FetchingTableArea";
import { QueryErrorAlert } from "./QueryErrorAlert";
import type { QueryListLabels } from "./types";
import { useQueryListState } from "./useQueryListState";

type QueryListSectionProps = {
  isPending: boolean;
  isFetching: boolean;
  isError: boolean;
  error: Error | null;
  refetch: () => void;
  hasData: boolean;
  labels: QueryListLabels;
  areaClassName?: string;
  children: ReactNode;
  footer?: ReactNode;
};

export function QueryListSection({
  isPending,
  isFetching,
  isError,
  error,
  refetch,
  hasData,
  labels,
  areaClassName,
  children,
  footer,
}: QueryListSectionProps) {
  const { isInitialLoad, isRefetching } = useQueryListState({
    isPending,
    isFetching,
    hasData,
  });

  const { errorTitle, errorFallbackMessage, initialLoadLabel, updatingLabel } = labels;

  if (isInitialLoad) {
    return <Spinner label={initialLoadLabel} />;
  }

  return (
    <>
      <QueryErrorAlert
        error={error}
        isError={isError}
        onRetry={refetch}
        title={errorTitle}
        fallbackMessage={errorFallbackMessage}
      />

      {!isError ? (
        <>
          <FetchingTableArea
            isRefetching={isRefetching}
            updatingLabel={updatingLabel}
            areaClassName={areaClassName}
          >
            {children}
          </FetchingTableArea>
          {footer}
        </>
      ) : null}
    </>
  );
}
