import { useState, type FormEvent } from "react";

import { hasFormErrors } from "@/shared/lib";

export function useFormState<T extends Record<string, string>>(
  initialValues: T,
  validate: (values: T) => Partial<Record<keyof T, string>>,
  onSubmit: (values: T) => void,
) {
  const [values, setValues] = useState<T>(initialValues);
  const [errors, setErrors] = useState<Partial<Record<keyof T, string>>>({});

  const handleChange = (field: keyof T, value: string) => {
    setValues((prev) => ({ ...prev, [field]: value }));
    setErrors((prev) => {
      const next = { ...prev };
      delete next[field];
      return next;
    });
  };

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const validationErrors = validate(values);
    setErrors(validationErrors);

    if (hasFormErrors(validationErrors)) {
      return;
    }

    onSubmit(values);
  };

  return { values, errors, handleChange, handleSubmit };
}
