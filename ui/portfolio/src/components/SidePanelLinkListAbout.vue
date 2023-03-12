<template>
  <div class="grid grid-rows-1">
    <li>
      <button class="hover:underline underline-offset-1">
        <p class="font-mono">
          <router-link to="/about/">About/Contact</router-link>
        </p>
      </button>
    </li>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";

@Options({})
export default class SidePanelLinkListAbout extends Vue {}
</script>
