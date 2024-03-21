<script setup>
import { ref } from 'vue'

import VenditaCard from './VenditaCard.vue';

const products = ref([])

function update() {
    fetch('http://127.0.0.1:5000/control')
    .then(res => res.json())
    .then(json => products.value = json)
}
update()
</script>

<template>
    <div class="sells-wrapper">
        <VenditaCard v-for="product in products" :product="product" @update="update()"/>
        <span v-if="!products.length">Nessuna vendita in sospeso.</span>
    </div>
</template>

<style scoped lang="scss">
@import '../../style/colors.scss';
.sells-wrapper {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}
</style>