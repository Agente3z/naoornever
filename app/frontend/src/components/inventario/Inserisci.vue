<script setup>
import { ref } from 'vue';

const headers = ref([]);

fetch('http://127.0.0.1:5000/headers')
.then(res => res.json())
.then(json => headers.value = json);

function submitForm(e) {
	fetch('http://127.0.0.1:5000/add', {
		method: 'POST',
		headers: {
    		'Content-Type': 'application/x-www-form-urlencoded'
  		},
		body: new FormData(e.target)
	}).then(res => res.json())
	.then(json => alert(json));
}
</script>

<template>
	<form @submit.prevent="submitForm">
		<h1 class="page-title"></h1>
			<div class="input-wrapper">
				<label v-for="header in headers">
				{{ header.name }}
					
<!-- 
				<select v-else name="categoria">
							   <option v-for="option in header.selectOptions" :value="option">{{ option }}</option>
						   </select>
						   <select v-else name="sottocategoria">
							   <option v-for="option in header.selectOptions" :value="option">{{ option }}</option>
						   </select>
			-->			
	
				<input v-if="header.type != 'select'" :type="header.type" :name="header.name">
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