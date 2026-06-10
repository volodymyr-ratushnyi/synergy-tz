import type { UserRole } from "@/entities/user";
import { isNonEmpty, isValidEmail, isWithinMaxLength } from "@/shared/lib";

export type UserFormValues = {
  first_name: string;
  last_name: string;
  email: string;
  username: string;
  image: string;
  role: UserRole;
};

export type UserFormErrors = Partial<Record<keyof UserFormValues, string>>;

const MAX_LENGTH: Record<keyof UserFormValues, number> = {
  first_name: 255,
  last_name: 255,
  email: 255,
  username: 255,
  image: 512,
  role: 50,
};

const REQUIRED_FIELDS: (keyof UserFormValues)[] = [
  "first_name",
  "last_name",
  "email",
  "username",
  "role",
];

export function validateUserForm(values: UserFormValues): UserFormErrors {
  const errors: UserFormErrors = {};

  for (const field of REQUIRED_FIELDS) {
    if (!isNonEmpty(values[field])) {
      errors[field] = "Required field";
    } else if (!isWithinMaxLength(values[field], MAX_LENGTH[field])) {
      errors[field] = `Max ${MAX_LENGTH[field]} characters`;
    }
  }

  if (!errors.email && values.email && !isValidEmail(values.email)) {
    errors.email = "Invalid email format";
  }

  if (!errors.image && values.image && !isWithinMaxLength(values.image, MAX_LENGTH.image)) {
    errors.image = `Max ${MAX_LENGTH.image} characters`;
  }

  return errors;
}
