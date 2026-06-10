import type { FormEvent, ReactNode } from "react";

import { Button } from "../Button/Button";

import "./EditFormLayout.scss";

type EditFormLayoutProps = {
  isSubmitting: boolean;
  submitError: string | null;
  onCancel: () => void;
  onSubmit: (event: FormEvent<HTMLFormElement>) => void;
  children: ReactNode;
};

export function EditFormLayout({
  isSubmitting,
  submitError,
  onCancel,
  onSubmit,
  children,
}: EditFormLayoutProps) {
  return (
    <form className="edit-form" onSubmit={onSubmit} noValidate>
      <div className="edit-form__grid">{children}</div>

      {submitError ? <p className="edit-form__submit-error">{submitError}</p> : null}

      <div className="edit-form__actions">
        <Button type="button" variant="ghost" disabled={isSubmitting} onClick={onCancel}>
          Cancel
        </Button>
        <Button type="submit" disabled={isSubmitting}>
          {isSubmitting ? "Saving..." : "Save changes"}
        </Button>
      </div>
    </form>
  );
}
