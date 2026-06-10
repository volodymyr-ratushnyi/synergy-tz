import type { ReactNode } from "react";

import "./Alert.scss";

type AlertVariant = "error" | "info";

type AlertProps = {
  variant?: AlertVariant;
  title?: string;
  children: ReactNode;
  onRetry?: () => void;
};

export function Alert({ variant = "error", title, children, onRetry }: AlertProps) {
  return (
    <div className={`alert alert--${variant}`} role="alert">
      {title ? <strong className="alert__title">{title}</strong> : null}
      <p className="alert__message">{children}</p>
      {onRetry ? (
        <button type="button" className="alert__retry" onClick={onRetry}>
          Try again
        </button>
      ) : null}
    </div>
  );
}
