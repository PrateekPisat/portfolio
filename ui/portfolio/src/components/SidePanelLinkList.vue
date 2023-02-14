<template>
  <div class="mb-10">
    <ul class="flex flex-col space-y-3">
      <SidePanelLinkListItem name="Editorial" />
      <SidePanelLinkListItem name="Lifestyle" />
      <SidePanelLinkListItem name="Beauty" />
      <SidePanelLinkListItem name="Music" />
      <SidePanelLinkListItem name="Motion" />
      <SidePanelLinkListItem name="Product Still Life" />
      <SidePanelLinkListItem name="Fine Art/Personal" />
      <SidePanelLinkListItem name="About + Contact" />
    </ul>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SidePanelLinkListItem from "@/components/SidePanelLinkListItem.vue";

@Options({ components: { SidePanelLinkListItem } })
export default class SidePanelLinkList extends Vue {}
</script>
