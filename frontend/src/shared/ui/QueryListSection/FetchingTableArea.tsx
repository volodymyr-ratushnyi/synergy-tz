import type { ReactNode } from "react";

import { Spinner } from "../Spinner/Spinner";

import "./FetchingTableArea.scss";

type FetchingTableAreaProps = {
  isRefetching: boolean;
  updatingLabel?: string;
  areaClassName?: string;
  children: ReactNode;
};

export function FetchingTableArea({
  isRefetching,
  updatingLabel = "Updating...",
  areaClassName = "",
  children,
}: FetchingTableAreaProps) {
  const classes = [areaClassName, isRefetching ? `${areaClassName}--fetching` : ""]
    .filter(Boolean)
    .join(" ");

  return (
    <div className={classes}>
      {isRefetching ? (
        <div className="fetching-table-area__overlay" aria-hidden="true">
          <Spinner label={updatingLabel} />
        </div>
      ) : null}
      {children}
    </div>
  );
}
