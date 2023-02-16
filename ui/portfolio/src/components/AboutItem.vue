<template>
  <div class="pb-8">
    <p class="font-bold">{{ title }}</p>
    <p
      class="text-sm text-blue-500 hover:underline underline-offset-1 hover:text-blue-900"
    >
      <a :href="link">{{ value }}</a>
    </p>
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";

export default class AboutItem extends Vue {
  @Prop() title!: string;
  @Prop() value!: string;
  @Prop() link!: string;
}
</script>
