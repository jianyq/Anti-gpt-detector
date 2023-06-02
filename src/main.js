import { createApp } from 'vue';
import App from './App.vue';
import './style.css';

export const app = createApp(App);

const meta = document.createElement('meta');
meta.name = 'naive-ui-style';
document.head.appendChild(meta);

app.mount('#app');
