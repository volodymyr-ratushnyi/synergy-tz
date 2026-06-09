import { env } from "@/shared/config/env";

export function HomePage() {
  return (
    <main
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        minHeight: "100vh",
        gap: "0.5rem",
      }}
    >
      <h1>Synergy TZ</h1>
      <p>Frontend scaffold ready for development.</p>
      <p style={{ fontSize: "0.875rem", color: "#666" }}>API: {env.apiUrl}</p>
    </main>
  );
}
