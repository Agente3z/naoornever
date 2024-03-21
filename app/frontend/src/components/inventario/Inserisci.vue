<script setup>
import { ref } from 'vue';

const headers = ref([]);
const currentCategory = ref('');
const headersLoaded = ref(false);

fetch('http://127.0.0.1:5000/headers')
.then(res => res.json())
.then(json => {
	headers.value = json;
	headersLoaded.value = true;
});

function submitForm(e) {
	const formData = new FormData(e.target);
	const data = [];
	formData.forEach((value, key) => data.push(`${key}=${value}`));
	const bodyString = data.join('&');
	fetch('http://127.0.0.1:5000/add', {
		method: 'POST',
		headers: {
    		'Content-Type': 'application/x-www-form-urlencoded'
  		},
		body: bodyString
	}).then(res => res.json())
	.then(json => alert(json));
}
</script>

<template>
	<form @submit.prevent="submitForm">
		<h1 class="page-title"></h1>
		<div v-if="headersLoaded" class="input-wrapper">
			<label>
				Categoria
				<select name="categoria" v-model="currentCategory">
					<option default v-for="option in headers.find(header => header.name == 'categoria').selectOptions" :value="option">{{ option }}</option>
				</select>
			</label>
			<label>
				Sottocategoria
				<select name="sottocategoria">
					<option v-for="option in headers.find(header => header.name == 'sottocategoria').selectOptions[currentCategory]" :value="option">{{ option }}</option>
				</select>
			</label>
			<label v-for="header in headers.filter(header => !['categoria', 'sottocategoria'].includes(header.name))">
				{{ header.name }}
				<input v-if="header.type != 'select'" :type="header.type" :name="header.name" min="0">
			</label>
		</div>
		<button type="submit"></button>
	</form>
</template>

<style scoped lang="scss">
@import '../../style/colors.scss';
form {
	height: 100%;
	display: flex;
	flex-direction: column;
	gap: 1rem;

	.page-title {
		margin-bottom: 1rem;

		&::before {
			content: 'Inserisci un nuovo prodotto';
		}
	}

	.input-wrapper {
		display: flex;
		flex-direction: column;
		gap: 1rem;
		overflow: auto;
		
		label {
			display: flex;
			flex-direction: column;
			gap: .5rem;
			font-size: 1.5rem;
			text-transform: capitalize;

			input, select {
				font-size: 1.2rem;
				padding: .5rem;
				border: none;
				border-radius: 5px;
			}
		}
	}
	button {
		padding: 1rem;
		color: $primary-color-text;
		background-color: $primary-color;
		font-size: 1.5rem;
		border: none;
		border-radius: 5px;
		cursor: pointer;
		
		&::before {
			content: 'Inserisci';
		}

		&:hover {
			background-color: $primary-color-hover;
		}
	}
}
</style>