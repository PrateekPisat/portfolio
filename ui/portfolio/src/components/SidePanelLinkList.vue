<template>
  <div class="grid grid-rows-1 gap-4">
    <SidePanelLinkListItem name="Editorial" />
    <SidePanelLinkListItem name="Lifestyle" />
    <SidePanelLinkListItem name="Beauty" />
    <SidePanelLinkListItem name="Music" />
    <SidePanelLinkListItem name="Motion" />
    <SidePanelLinkListItem name="Product Still Life" />
    <SidePanelLinkListItem name="Fine Art/Personal" />
    <SidePanelLinkListItem name="About + Contact" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SidePanelLinkListItem from "@/components/SidePanelLinkListItem.vue";

@Options({ components: { SidePanelLinkListItem } })
export default class SidePanelLinkList extends Vue {}
</script>
