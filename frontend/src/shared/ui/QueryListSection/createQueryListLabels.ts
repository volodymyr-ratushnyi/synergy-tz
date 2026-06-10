import type { QueryListLabels } from "./types";

export function createQueryListLabels(entityPlural: string): QueryListLabels {
  const label = entityPlural.toLowerCase();

  return {
    errorTitle: `Failed to load ${label}`,
    errorFallbackMessage: `Failed to load ${label}. Please try again.`,
    initialLoadLabel: `Loading ${label}...`,
    updatingLabel: "Updating...",
    loadingMoreLabel: `Loading more ${label}...`,
    allLoadedLabel: `All ${label} loaded`,
  };
}
