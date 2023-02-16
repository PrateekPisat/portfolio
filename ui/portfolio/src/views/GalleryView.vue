<template>
  <div class="flex flex-row m-2 p-1 md:m-4 md:p-3 lg:m-4 lg:p-3 xl:m-8 xl:p-6">
    <div class="xs:basis-1/5">
      <SidePanel />
    </div>
    <div class="xs:basis-4/5">
      <Gallery />
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SidePanel from "../components/SidePanel.vue";
import Gallery from "../components/Gallery.vue";

@Options({
  components: {
    SidePanel,
    Gallery,
  },
})
export default class GalleryView extends Vue {}
</script>
