import { ApiError } from "@/shared/api";

export function getErrorMessage(
  error: Error,
  fallback = "Something went wrong. Please try again.",
): string {
  return error instanceof ApiError ? error.message : fallback;
}
