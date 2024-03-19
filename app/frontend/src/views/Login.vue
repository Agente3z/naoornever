<script setup>
import { inject } from 'vue'

const user = inject('user')
</script>

<template>
	<div class="wrapper">
		<div class="login-card">
			<h2></h2>
			<div class="login-form">
				<button type="submit" @click="user = {}"></button>
			</div>
		</div>
	</div>
</template>


<style scoped lang="scss">
@import '../style/colors.scss';

.wrapper {
	height: 100vh;
	display: grid;
	place-items: center;
	background-image: url('../assets/login_background.svg');
	background-repeat: no-repeat;
	background-size: cover;
	background-position: center;
	color: black;
	animation: rotate 6s infinite alternate linear;
}

.login-card {
	width: 25rem;
	display: flex;
	flex-direction: column;
	gap: 2rem;
	position: relative;
	padding: 2rem;
	border-radius: 1.25rem;
	background: $background-color;
	text-align: center;

	h2 {
		font-size: 2.5rem;
		font-weight: 600;
		margin: 0 0 1rem;
		text-transform: capitalize;

		&::before {
			content: 'Login';
		}
	}
}

.login-form {
	width: 100%;
	margin: 0;
	display: grid;
	gap: 1rem;
	button {
		width: 100%;
		height: 4rem;
		padding: 1rem;
		border-radius: 20px;
		background: $primary-color;
		color: #f9f9f9;
		border: 0;
		font-family: Arial, Helvetica, sans-serif;
		font-size: 1.5rem;
		font-weight: 600;
		text-align: center;
		transition: all 0.375s;
		cursor: pointer;

		&:hover {
			background: $primary-color-hover;
		}

		&::before {
			content: 'Entra';
		}
	}
}
</style>