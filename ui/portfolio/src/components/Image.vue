<template>
  <div>
    <ImageHeader :user_id="user_id" />
    <ImageDisplay :image_id="image_id" />
    <ImageStats :image_id="image_id" />
  </div>
</template>
<script lang="ts">
import axios from "axios";

import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { Image, User } from "@/types";
import ImageHeader from "@/components/ImageHeader.vue";
import ImageDisplay from "@/components/ImageDisplay.vue";
import ImageStats from "@/components/ImageStats.vue";

@Options({
  components: {
    ImageHeader,
    ImageDisplay,
    ImageStats,
  },
})
export default class GalleryItem extends Vue {
  @Prop() user_id!: number;
  @Prop() image_id!: number;

  user?: User | null = null;
  image?: Image | null = null;

  async mounted() {
    await this.get_user();
    await this.get_image();
  }

  async get_user() {
    axios
      .get("/user", {
        params: {
          id: this.user_id,
        },
      })
      .then((response) => {
        this.user = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }

  async get_image() {
    axios
      .get("/image", {
        params: {
          id: this.image_id,
        },
      })
      .then((response) => {
        this.image = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }
}
</script>
