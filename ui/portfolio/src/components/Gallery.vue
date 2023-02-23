<template>
  <div
    class="grid gap-4 xs:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 3xl:grid-cols-4"
  >
    <GalleryItem v-for="image in images" :key="image.id" :image="image" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import GalleryItem from "./GalleryItem.vue";
import { Image } from "../types";
import { Prop } from "vue-property-decorator";

@Options({ components: { GalleryItem } })
export default class Gallery extends Vue {
  @Prop() images!: Image[];
}
</script>
