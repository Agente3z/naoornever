<script setup>

const props = defineProps(['product']);

function confirm(e) {
	const formData = new FormData(e.target, e.submitter);
	fetch('http://127.0.0.1:5000/control', {
		method: 'POST',
		body: formData
	})
	.then(res => res.json())
	.then(json => console.log(json))
}
</script>

<template>
	{{ props.product }}
	<div class="wrapper">
		<img :src="product.foto" alt="foto prodotto">
		<div class="infos">
			<h1>{{ props.product.nome }}</h1>
			<span>{{ 'Il ' + new Date(props.product.timestamp).toLocaleDateString() + ' alle ' + new Date(props.product.timestamp).toLocaleTimeString() }}</span>
		</div>
		{{ props.product.quantità }}
		<form v-if="props.product.conferma == null" class="confirm" @submit.prevent="confirm">
			<input type="hidden" name="id" :value="props.product.id">
			<button class="confirm" name="conferma" value="True"></button>
			<button class="refuse" name="conferma" value="False"></button>
		</form>
		<div v-else class="confirm">
			<span>{{ props.product.conferma ? 'Confermato' : 'Rifiutato' }}</span>
		</div>
	</div>
</template>

<style scoped lang="scss">
@import '../../style/colors.scss';

.wrapper {
	gap: 1rem;
	padding: 1rem;
	border-radius: 0.5rem;
	box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
	background-color: $primary-color;
	color: $primary-color-text;
	display: flex;
	align-items: center;

	img {
		width: 100px;
		height: 100px;
		object-fit: scale-down;
	}

	.infos {
		display: flex;
		flex-direction: column;
		gap: 1rem;

		h1 {
			margin: 0;
		}
	}

	.confirm {
		width: fit-content;
		margin-left: auto;
		display: flex;
		flex-direction: column;
		gap: 1rem;
		
		button {
			font-family: 'Ubuntu', sans-serif;
			font-size: 1.5rem;
			border-radius: 5px;
			color: $primary-color-text;
			border: none;
			cursor: pointer;

			&.confirm {
				background-color: #78d878;
				
				&::before {
					content: 'Conferma';
				}
			}

			&.refuse {
				background-color: #e63333;
				
				&::before {
					content: 'Rifiuta';
				}
			}
		}
	}
}
</style>