<template>
  <div>
    <a :href="link">
      <font-awesome-icon :icon="name" />
    </a>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";

@Options({})
export default class SidePanelSocialsItem extends Vue {
  @Prop() iconName!: string;
  @Prop() linkUrl!: string;

  get name() {
    return this.iconName;
  }

  get link() {
    return this.linkUrl;
  }
}
</script>
