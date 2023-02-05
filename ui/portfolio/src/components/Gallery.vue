<template>
  <div
    class="grid xs:grid-cols-1 lg:grid-cols-3 md:grid-cols-2 gap-4 justify-items-center"
  >
    <GalleryItem src="" id="1" />
    <GalleryItem src="" id="1" />
    <GalleryItem src="" id="1" />
    <GalleryItem src="" id="1" />
    <GalleryItem src="" id="1" />
    <GalleryItem src="" id="1" />
    <GalleryItem src="" id="1" />
    <GalleryItem src="" id="1" />
    <GalleryItem src="" id="1" />
    <GalleryItem src="" id="1" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import GalleryItem from "./GalleryItem.vue";

@Options({ components: { GalleryItem } })
export default class Gallery extends Vue {}
</script>
