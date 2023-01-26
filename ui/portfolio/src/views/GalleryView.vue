<template>
  <div class="container m-10 p-10 flex flex-row">
    <div class="basis-1/3">
      <SidePanel />
    </div>
    <div class="basis-2/3">
      <Gallery />
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SidePanel from "@/components/SidePanel.vue";
import Gallery from "@/components/Gallery.vue";

@Options({
  components: {
    SidePanel,
    Gallery,
  },
})
export default class GalleryView extends Vue {}
</script>
