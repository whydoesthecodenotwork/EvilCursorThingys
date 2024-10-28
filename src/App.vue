<template>
  <div class="flex flex-col w-screen h-screen items-center">
    <h1 class="text-4xl">Skibidi Toilet</h1>
    <p>test trackpad below...</p>
    <div ref="trackpad" class="w-full h-full flex-grow bg-gray-200" @mousemove="log"></div>
    <output>{{ output }}</output>
    <button @click="invoke('init')">crash lmao 2</button>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, useTemplateRef } from "vue";
import { invoke } from "@tauri-apps/api/core";

const trackpad = useTemplateRef("trackpad");
const rect = computed(() => trackpad.value?.getBoundingClientRect());
const output = ref("");

onMounted(() => {});

async function log(e: MouseEvent) {
  if (!rect.value) return;
  // output.value = `${e.offsetX}, ${e.offsetY}`;
  output.value = await invoke("draw", { x: e.offsetX / rect.value.width, y: e.offsetY / rect.value.height });
}
</script>

<style scoped></style>
