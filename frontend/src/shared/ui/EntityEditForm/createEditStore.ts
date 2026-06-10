import { create } from "zustand";

type EditStore<TEntity> = {
  editingEntity: TEntity | null;
  openEdit: (entity: TEntity) => void;
  closeEdit: () => void;
};

export function createEditStore<TEntity>() {
  return create<EditStore<TEntity>>((set) => ({
    editingEntity: null,
    openEdit: (entity) => set({ editingEntity: entity }),
    closeEdit: () => set({ editingEntity: null }),
  }));
}
