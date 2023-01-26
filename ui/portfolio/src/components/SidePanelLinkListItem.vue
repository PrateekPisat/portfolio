<template>
  <div class="grid grid-rows-1 gap-4">
    <div>
      <button class="hover:underline underline-offset-1">{{ name }}</button>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";

@Options({})
export default class SidePanelLinkList extends Vue {
  @Prop() name!: string;
}
</script>
