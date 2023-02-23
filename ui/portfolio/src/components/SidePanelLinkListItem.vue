<template>
  <div class="grid grid-rows-1">
    <li>
      <router-link :to="path">
        <button class="hover:underline underline-offset-1">
          <p class="font-mono">
            {{ groupName }}
          </p>
        </button>
      </router-link>
    </li>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";

@Options({})
export default class SidePanelLinkList extends Vue {
  @Prop() groupName!: string;
  @Prop() groupId!: number;

  get path() {
    return "/gallery/" + this.groupId;
  }
}
</script>
