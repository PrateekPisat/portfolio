<template>
  <div>
    <ImageHeader />
  </div>
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { Image, User } from "@/types";
import ImageHeader from "@/components/ImageHeader.vue";
// import ImageDisplay from "@/components/ImageDisplay.vue";
// import ImageStats from "@/components/ImageStats.vue";
import { getUser } from "../api";

@Options({
  components: {
    ImageHeader,
    // ImageDisplay,
    // ImageStats,
  },
})
export default class GalleryImage extends Vue {
  @Prop() id!: number;

  user?: User | null = null;
  image?: Image | null = null;

  async mounted() {
    this.user = await getUser(1);
    // this.image = await get_image(this.image_id);
  }
}
</script>
