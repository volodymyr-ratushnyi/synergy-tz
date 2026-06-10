import type { ChangeEvent } from "react";

import { Input } from "../Input/Input";
import { Select } from "../Select/Select";

import { EditFormLayout } from "./EditFormLayout";
import { useFormState } from "./useFormState";

type InputFieldConfig<T extends Record<string, string>> = {
  kind: "input";
  name: keyof T & string;
  label: string;
  type?: "text" | "email" | "number";
  min?: number;
};

type SelectFieldConfig<T extends Record<string, string>> = {
  kind: "select";
  name: keyof T & string;
  label: string;
  options: { value: string; label: string }[];
};

export type FormFieldConfig<T extends Record<string, string>> =
  | InputFieldConfig<T>
  | SelectFieldConfig<T>;

type EntityEditFormProps<T extends Record<string, string>> = {
  initialValues: T;
  fields: FormFieldConfig<T>[];
  validate: (values: T) => Partial<Record<keyof T, string>>;
  isSubmitting: boolean;
  submitError: string | null;
  onSubmit: (values: T) => void;
  onCancel: () => void;
};

export function EntityEditForm<T extends Record<string, string>>({
  initialValues,
  fields,
  validate,
  isSubmitting,
  submitError,
  onSubmit,
  onCancel,
}: EntityEditFormProps<T>) {
  const { values, errors, handleChange, handleSubmit } = useFormState(
    initialValues,
    validate,
    onSubmit,
  );

  return (
    <EditFormLayout
      isSubmitting={isSubmitting}
      submitError={submitError}
      onCancel={onCancel}
      onSubmit={handleSubmit}
    >
      {fields.map((field) => {
        const fieldName = field.name;
        const commonProps = {
          label: field.label,
          value: values[fieldName],
          error: errors[fieldName],
          disabled: isSubmitting,
          onChange: (event: ChangeEvent<HTMLInputElement | HTMLSelectElement>) =>
            handleChange(fieldName, event.target.value),
        };

        if (field.kind === "select") {
          return <Select key={fieldName} {...commonProps} options={field.options} />;
        }

        return <Input key={fieldName} {...commonProps} type={field.type} min={field.min} />;
      })}
    </EditFormLayout>
  );
}
