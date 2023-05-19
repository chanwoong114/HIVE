<template>
  <div>
    <button @click="trigger" data-fancybox data-src="#dialog-content">Launch Dialog</button>
    <div id="dialog-content" style="display:none;max-width:500px;">
      <h2>Hello, world!</h2>
      <p>
        <input type="text" value="" />
      </p>
      <p>
        Try hitting the tab key and notice how the focus stays within the dialog
        itself.
      </p>
      <p>
        To close dialog hit the esc button, click on the overlay or just click the
        close button.
      </p>
      <p>
        Element used to launch the modal would receive focus back after closing.
      </p>
    </div>
  </div>
</template>

<script>
import { Fancybox } from '@fancyapps/ui';
import '@fancyapps/ui/dist/fancybox/fancybox.css';

export default {
  methods: {
    trigger() {
      Fancybox.show([{src: "#dialog-content", type: "inline"}])
    }
  }
}
</script>

<style>

</style>