import type { ReactNode } from "react";

import type { SortOrder } from "@/shared/types/pagination";

import "./DataTable.scss";

type DataTableProps = {
  children: ReactNode;
  className?: string;
};

export function DataTable({ children, className }: DataTableProps) {
  const classes = ["data-table", className].filter(Boolean).join(" ");

  return (
    <div className="data-table__wrapper">
      <table className={classes}>{children}</table>
    </div>
  );
}

type SortableHeaderProps = {
  label: string;
  field: string;
  activeField: string;
  sortOrder: SortOrder;
  onSort: (field: string) => void;
  className?: string;
};

export function SortableTableHeader({
  label,
  field,
  activeField,
  sortOrder,
  onSort,
  className,
}: SortableHeaderProps) {
  const isActive = activeField === field;
  const indicator = isActive ? (sortOrder === "asc" ? "↑" : "↓") : "↕";

  return (
    <th className={className} scope="col">
      <button
        type="button"
        className={["data-table__sort-btn", isActive ? "data-table__sort-btn--active" : ""]
          .filter(Boolean)
          .join(" ")}
        onClick={() => onSort(field)}
        aria-sort={isActive ? (sortOrder === "asc" ? "ascending" : "descending") : "none"}
      >
        <span>{label}</span>
        <span className="data-table__sort-indicator" aria-hidden="true">
          {indicator}
        </span>
      </button>
    </th>
  );
}

type DataTableHeaderCellProps = {
  children?: ReactNode;
  className?: string;
};

export function DataTableHeaderCell({ children, className }: DataTableHeaderCellProps) {
  return (
    <th className={className} scope="col">
      {children}
    </th>
  );
}
