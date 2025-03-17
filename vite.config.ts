import {resolve} from "path";

import {defineConfig} from "vite";
import react from "@vitejs/plugin-react-swc";

export default defineConfig({
    plugins: [react()],
    css: {},
    root: resolve("./src/static/ui_app_ts/src"),
    base: "/static/",
    build: {
        manifest: "manifest.json",
        outDir: resolve("./src/static/ui_app_ts/dist"),
        rollupOptions: {
            input: "./src/static/ui_app_ts/src/main.tsx",
        },
    },
});


