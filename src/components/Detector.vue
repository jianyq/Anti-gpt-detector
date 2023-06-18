<template>
    <div class="mx-2 flex items-center">
        <div class="mr-2 h-6 w-6 rounded-full border-2" :class="style_dic[res]">
            <span v-if="res === true" class="w-full fill-white">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path
                        d="M 20.292969 5.2929688 L 9 16.585938 L 4.7070312 12.292969 L 3.2929688 13.707031 L 9 19.414062 L 21.707031 6.7070312 L 20.292969 5.2929688 z"
                    />
                </svg>
            </span>
            <span v-if="res === false" class="w-full fill-white">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path
                        d="M 4.7070312 3.2929688 L 3.2929688 4.7070312 L 10.585938 12 L 3.2929688 19.292969 L 4.7070312 20.707031 L 12 13.414062 L 19.292969 20.707031 L 20.707031 19.292969 L 13.414062 12 L 20.707031 4.7070312 L 19.292969 3.2929688 L 12 10.585938 L 4.7070312 3.2929688 z"
                    />
                </svg>
            </span>
        </div>
        {{ name }}
    </div>
</template>
<script setup>
import { defineProps, onMounted } from 'vue';
const props = defineProps({
    detect_func: {
        type: Function,
        required: true,
    },
    name: {
        type: String,
        required: true,
    },
});
const res = ref(null);
const style_dic = {
    null: 'border-slate-300',
    true: 'border-teal-400 bg-teal-400 opacity-75',
    false: 'border-red-400 bg-red-400 opacity-75',
};
onMounted(() => {
    props.detect_func().then((result) => {
        res.value = result;
    });
});
</script>
