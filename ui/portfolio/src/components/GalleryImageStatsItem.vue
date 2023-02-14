<template>
  <div class="flex space-x-4">
    <span><font-awesome-icon :icon="iconName" /></span>
    <span class="text-slate-500">{{ text }}</span>
  </div>
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";

@Options({})
export default class GalleryImageStatsItem extends Vue {
  @Prop() iconName!: string;
  @Prop() text!: string;
}
</script>
