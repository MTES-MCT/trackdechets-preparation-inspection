import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "path";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  css: {},
  root: resolve("./src"),
  base: "/static/",
  build: {
    manifest: "manifest.json",
    outDir: resolve("../ui_app/dist"),
    rollupOptions: {
      input: "src/main.jsx",
    },
  },
});
