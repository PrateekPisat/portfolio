<template>
  <div class="flex flex-row">
    <div class="basis-1/6 p-3 lg:m-2">
      <SidePanel />
    </div>
    <div class="basis-5/6 p-3 lg:m-2">
      <Gallery :images="images" />
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SidePanel from "../components/SidePanel.vue";
import Gallery from "../components/Gallery.vue";
import { Image } from "../types";
import { getImages } from "../api";
import { Prop } from "vue-property-decorator";

@Options({
  components: { SidePanel, Gallery },
})
export default class GalleryView extends Vue {
  @Prop() groupId!: number;

  images: Image[] = [];

  async mounted() {
    this.images = await getImages(this.groupId);
  }

  async beforeCreate() {
    this.images = await getImages(this.groupId);
  }
}
</script>
