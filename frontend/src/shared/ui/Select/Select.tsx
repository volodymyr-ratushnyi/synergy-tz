import type { SelectHTMLAttributes } from "react";

import "./Select.scss";

type SelectOption = {
  value: string;
  label: string;
};

type SelectProps = SelectHTMLAttributes<HTMLSelectElement> & {
  label: string;
  options: SelectOption[];
  error?: string;
};

export function Select({ label, options, error, id, className, ...props }: SelectProps) {
  const selectId = id ?? label.toLowerCase().replace(/\s+/g, "-");
  const classes = ["select", error ? "select--error" : "", className].filter(Boolean).join(" ");

  return (
    <label className="field" htmlFor={selectId}>
      <span className="field__label">{label}</span>
      <select id={selectId} className={classes} aria-invalid={Boolean(error)} {...props}>
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      {error ? <span className="field__error">{error}</span> : null}
    </label>
  );
}
