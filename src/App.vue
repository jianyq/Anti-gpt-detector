<script>
import View from '@/views/View.vue';
import { NConfigProvider, NNotificationProvider, useNotification } from 'naive-ui';
export default {
    components: {
        NConfigProvider,
        NNotificationProvider,
        View,
    },
};
</script>

<template>
    <n-notification-provider container-style="margin-top:3rem">
        <n-config-provider preflight-style-disabled> <View></View> </n-config-provider
    ></n-notification-provider>
</template>

<style scoped></style>
