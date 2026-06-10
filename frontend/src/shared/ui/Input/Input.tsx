import type { InputHTMLAttributes } from "react";

import "./Input.scss";

type InputProps = InputHTMLAttributes<HTMLInputElement> & {
  label: string;
  error?: string;
};

export function Input({ label, error, id, className, ...props }: InputProps) {
  const inputId = id ?? label.toLowerCase().replace(/\s+/g, "-");
  const classes = ["input", error ? "input--error" : "", className].filter(Boolean).join(" ");

  return (
    <label className="field" htmlFor={inputId}>
      <span className="field__label">{label}</span>
      <input id={inputId} className={classes} aria-invalid={Boolean(error)} {...props} />
      {error ? <span className="field__error">{error}</span> : null}
    </label>
  );
}
