import { describe, expect, it } from "vitest";

import { formatTags, parseTags, validatePostForm } from "./validatePostForm";

const validValues = {
  title: "Hello world",
  body: "Post body",
  views: "10",
  tags: "life, travel",
};

describe("validatePostForm", () => {
  it("returns no errors for valid values", () => {
    expect(validatePostForm(validValues)).toEqual({});
  });

  it("marks required fields", () => {
    expect(validatePostForm({ ...validValues, title: "", body: " " })).toEqual({
      title: "Required field",
      body: "Required field",
    });
  });

  it("rejects title over max length", () => {
    expect(validatePostForm({ ...validValues, title: "a".repeat(513) })).toEqual({
      title: "Max 512 characters",
    });
  });

  it("rejects negative or non-integer views", () => {
    expect(validatePostForm({ ...validValues, views: "-1" })).toEqual({
      views: "Must be a non-negative integer",
    });
    expect(validatePostForm({ ...validValues, views: "1.5" })).toEqual({
      views: "Must be a non-negative integer",
    });
  });
});

describe("parseTags", () => {
  it("splits, trims, and drops empty entries", () => {
    expect(parseTags(" life ,, travel ,")).toEqual(["life", "travel"]);
  });

  it("returns empty array for blank input", () => {
    expect(parseTags("  ")).toEqual([]);
  });
});

describe("formatTags", () => {
  it("joins tags with comma and space", () => {
    expect(formatTags(["life", "travel"])).toBe("life, travel");
  });
});
