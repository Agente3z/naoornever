<script setup>
import Table from '../Table.vue';

import { ref } from 'vue';

const data = ref({
	headers: [
		'macrocategoria',
		'categoria',
		'sottocategoria',
		'nome',
		'colore',
		'prezzo',
		'dimensioni',
		'peso',
		'materiali',
		'features',
		'descrizione_intorto',
		'foto',
		'link',
		/* Rimuovere?
		'descrizione_tecnica',
		'disegno',
		'variante1',
		'variante2',
		'variante3' */
	], 
	rows: []
});
fetch('http://127.0.0.1:5000/get')
.then(res => res.json())
.then(json => data.value.rows = json);

</script>

<template>
    <Table :data="data"/>
</template>

<style scoped lang="scss">

</style>