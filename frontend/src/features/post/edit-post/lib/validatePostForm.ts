import { isNonEmpty, isWithinMaxLength } from "@/shared/lib";

export type PostFormValues = {
  title: string;
  body: string;
  views: string;
  tags: string;
};

export type PostFormErrors = Partial<Record<keyof PostFormValues, string>>;

const MAX_TITLE = 512;

export function validatePostForm(values: PostFormValues): PostFormErrors {
  const errors: PostFormErrors = {};

  if (!isNonEmpty(values.title)) {
    errors.title = "Required field";
  } else if (!isWithinMaxLength(values.title, MAX_TITLE)) {
    errors.title = `Max ${MAX_TITLE} characters`;
  }

  if (!isNonEmpty(values.body)) {
    errors.body = "Required field";
  }

  const views = Number(values.views);
  if (!isNonEmpty(values.views)) {
    errors.views = "Required field";
  } else if (!Number.isInteger(views) || views < 0) {
    errors.views = "Must be a non-negative integer";
  }

  return errors;
}

export function parseTags(value: string): string[] {
  return value
    .split(",")
    .map((tag) => tag.trim())
    .filter(Boolean);
}

export function formatTags(tags: string[]): string {
  return tags.join(", ");
}
