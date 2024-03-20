<script setup>
import Table from '../Table.vue';

import { ref } from 'vue';

const data = ref({
    headers: [],
    rows: []
});

fetch('http://127.0.0.1:5000/headers')
.then(res => res.json())
.then(json => data.value.headers = json.map(header => header.name));

fetch('http://127.0.0.1:5000/get')
.then(res => res.json())
.then(json => data.value.rows = json);
</script>

<template>
    <Table :data="data"/>
</template>

<style scoped lang="scss">

</style>