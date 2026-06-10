export function isNonEmpty(value: string): boolean {
  return value.trim().length > 0;
}

export function isWithinMaxLength(value: string, max: number): boolean {
  return value.trim().length <= max;
}

export function isValidEmail(value: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.trim());
}

export function hasFormErrors<T extends string>(errors: Partial<Record<T, string>>): boolean {
  return Object.keys(errors).length > 0;
}
