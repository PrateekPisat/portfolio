<template>
  <div class="mb-10">
    <ul class="flex flex-col space-y-3">
      <SidePanelLinkListItem
        v-for="group in groups"
        :key="group.id"
        :groupName="group.name"
        :groupId="group.id"
      />
      <SidePanelLinkListAbout />
    </ul>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SidePanelLinkListItem from "./SidePanelLinkListItem.vue";
import { listGroups } from "../api";
import { Group } from "../types";
import SidePanelLinkListAbout from "./SidePanelLinkListAbout.vue";

@Options({ components: { SidePanelLinkListItem, SidePanelLinkListAbout } })
export default class SidePanelLinkList extends Vue {
  groups: Group[] = [];

  async mounted() {
    this.groups = await listGroups();
  }
}
</script>
