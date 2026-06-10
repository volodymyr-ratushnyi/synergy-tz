import type { ButtonHTMLAttributes, ReactNode } from "react";

import "./Button.scss";

type ButtonVariant = "primary" | "secondary" | "danger" | "ghost";

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: ButtonVariant;
  children: ReactNode;
};

const variantClass: Record<ButtonVariant, string> = {
  primary: "btn btn--primary",
  secondary: "btn btn--secondary",
  danger: "btn btn--danger",
  ghost: "btn btn--ghost",
};

export function Button({ variant = "primary", className, children, ...props }: ButtonProps) {
  const classes = [variantClass[variant], className].filter(Boolean).join(" ");

  return (
    <button type="button" className={classes} {...props}>
      {children}
    </button>
  );
}
