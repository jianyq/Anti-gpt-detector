import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { resolve } from 'path';
import Components from 'unplugin-vue-components/vite';
import AutoImport from 'unplugin-auto-import/vite';
import { NaiveUiResolver } from 'unplugin-vue-components/resolvers';

export default defineConfig({
    plugins: [
        vue({
            include: [/\.vue$/],
        }),
        Components({
            resolvers: [NaiveUiResolver()],
        }),
        AutoImport({
            include: [
                /\.[tj]sx?$/, // .ts, .tsx, .js, .jsx, .vue
                /\.vue$/,
                /\.vue\?vue/, // .vue
            ],
            imports: ['vue', 'vue-router'],
        }),
    ],
    base: './',
    resolve: {
        alias: {
            '@': resolve(__dirname, './src'),
        },
    },
});
