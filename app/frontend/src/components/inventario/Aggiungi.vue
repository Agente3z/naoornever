<script setup>
import Multiselect from 'vue-multiselect'
import 'vue-multiselect/dist/vue-multiselect.css'

import { ref } from 'vue';

const products = ref([]);
const selectedProducts = ref([]);

fetch('http://127.0.0.1:5000/get')
.then(res => res.json())
.then(json => products.value = json);

function submitForm(e) {
	console.log((new FormData(e.target)).set);
	fetch('http://127.0.0.1:5000/', {
		method: 'POST',
		body: new FormData(e.target)
	}).then(res => res.json())
	.then(json => alert(json));
}
</script>

<template>
	<form @submit.prevent="submitForm">
		<h1 class="page-title"></h1>
			<div class="input-wrapper">
			<label class="items-selector">
				<Multiselect
					class="selector"
					v-model="selectedProducts"
					:options="products"
					:multiple="true"
					:hide-selected="true"
					:close-on-select="false"
					placeholder="Seleziona"
					select-label=""
					label="nome"
					track-by="nome"
				>
					<template #option="{ option }">
						{{ option.nome }}
					</template>
					<template #noResult>Nessun risultato.</template>monitor/assets/logo.png
				</Multiselect>
			</label>
			<label class="quantity-selector">
				<input type="number" name="quantità" value="1" min="0" required>
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
			content: 'Aggiungi prodotti all\'inventario';
		}
	}

	.input-wrapper {
		display: flex;
		flex-direction: column;
		gap: 1rem;

		label {
			display: flex;
			flex-direction: column;
			gap: .5rem;
			font-size: 1.5rem;
			text-transform: capitalize;


			&.items-selector::before {
				content: 'Seleziona prodotti';
			}

			&.quantity-selector::before {
				content: 'Inserisci la quantità';
			}

			input {
				font-size: 1.2rem;
				padding: .5rem;
				border: none;
				border-radius: 5px;
			}
			
			.selector {
				box-sizing: border-box;
				max-width: 100%;
				cursor: pointer;
			}
		}
	}
	button {
		margin-top: auto;
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