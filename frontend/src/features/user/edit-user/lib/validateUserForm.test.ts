import { describe, expect, it } from "vitest";

import { validateUserForm } from "./validateUserForm";

const validValues = {
  first_name: "John",
  last_name: "Doe",
  email: "john@example.com",
  username: "johndoe",
  image: "",
  role: "user" as const,
};

describe("validateUserForm", () => {
  it("returns no errors for valid values", () => {
    expect(validateUserForm(validValues)).toEqual({});
  });

  it("marks required fields", () => {
    expect(validateUserForm({ ...validValues, first_name: "" })).toEqual({
      first_name: "Required field",
    });
  });

  it("validates email format", () => {
    expect(validateUserForm({ ...validValues, email: "not-an-email" })).toEqual({
      email: "Invalid email format",
    });
  });
});
