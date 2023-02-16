<template>
  <div class="grid grid-rows-1">
    <li>
      <button class="hover:underline underline-offset-1">
        <p class="font-mono">
          <router-link :to="to">
            {{ name }}
          </router-link>
        </p>
      </button>
    </li>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";

@Options({})
export default class SidePanelLinkList extends Vue {
  @Prop() name!: string;
  @Prop() to!: string;
}
</script>
