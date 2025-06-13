import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import tailwindcss from "@tailwindcss/vite";
import path from 'path';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    proxy: {
      '/api': 'http://localhost:8000',
      '/graphql': 'http://localhost:8000',
    }
  },
  resolve: {
    alias: {
        '@': path.resolve(__dirname, 'src')
    }
  }
})
