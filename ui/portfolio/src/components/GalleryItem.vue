<template>
  <div>
    <button>
      <img class="aspect-auto" :src="img_src" :alt="image_id" />
    </button>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";

@Options({})
export default class GalleryItem extends Vue {
  @Prop() src!: string;
  @Prop() id!: number;

  get img_src() {
    return this.src;
  }

  get image_id() {
    return "image" + this.id;
  }
}
</script>
