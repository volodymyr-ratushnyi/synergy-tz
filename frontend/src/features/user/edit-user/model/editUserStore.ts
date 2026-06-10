import type { User } from "@/entities/user";
import { createEditStore } from "@/shared/ui";

export const useEditUserStore = createEditStore<User>();
