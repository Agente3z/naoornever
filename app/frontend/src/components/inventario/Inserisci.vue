<script setup>
import { ref } from 'vue';
import Icon from '../Icon.vue'

const headers = [
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
]

const formData = ref(null);

function submitForm(e) {
	formData.value = new FormData(e.target);
	fetch('http://127.0.0.1:5000/add', {
		method: 'POST',
		body: formData
	}).then(res => res.json())
	.then(json => console.log(json));
}

</script>

<template>
	<form @submit.prevent="submitForm">
		<label v-for="header in headers">
			{{ header }}
			<input type="text" :name="header" value="test">
		</label>
		<input v-for="header in ['descrizione_tecnica', 'disegno', 'variante1', 'variante2', 'variante3']" type="hidden" :name="header" value="-">
		<button type="submit"></button>
	</form>
</template>

<style scoped lang="scss">
@import '../../style/colors.scss';
form {
	display: flex;
	flex-direction: column;
	gap: 1rem;

	button {
		&::before {
			content: 'Inserisci';
		}
	}
}
</style>