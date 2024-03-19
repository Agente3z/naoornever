<script setup>
import Icon from './Icon.vue'

import { inject, ref } from 'vue'

defineProps(['currentView'])
defineEmits(['selection'])

const user = inject('user')
const isSidebarClosed = ref(false)
</script>

<template>
	<div class="sidebar-body" :class="{'closed': isSidebarClosed}">
		<div class="header">
			<Icon type="sidebar" color="white" class="icon" @click="isSidebarClosed=!isSidebarClosed"/>
		</div>
		<button class="venditeNao" :class="{'selected': currentView == 'venditeNao'}" @click="$emit('selection', 'venditeNao')">
			<Icon type="venditeNao" color="white" class="icon"/>
			<span></span>
		</button>
		<button class="inventario" :class="{'selected': currentView == 'inventario'}" @click="$emit('selection', 'inventario')">
			<Icon type="inventario" color="white" class="icon"/>
			<span></span>
		</button>
		<button class="esci" @click="user = null">
			<Icon type="esci" color="white" class="icon"/>
			<span></span>
		</button>
	</div>
</template>

<style scoped lang="scss">
@import '../style/colors.scss';
$sidebar-border-color: #ffffff26;

.icon {
	height: 3rem;
	width: 3rem;
}

.sidebar-body {
	min-width: 20rem;
	height: 100%;
	display: flex;
	overflow-y: auto;
	flex-direction: column;
	background-color: $primary-color;
	
	.header {
		padding-block: 1rem;
		padding-inline: 1rem;
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 1rem;
		font-size: 2rem;
		color: $primary-color-text;
		font-weight: bold;
		text-transform: uppercase;
		color: $primary-color-text;

		&::before {
			content: 'NAO Manager';
			white-space: nowrap;
		}

		.icon {
			transition: rotate 0.5s ease-out;
			rotate: z 0;
			
			&:hover {
				cursor: pointer;
			}
		}
	}
	
	button {
		display: flex;
		gap: 0.75rem;
		align-items: center;
		font-family: 'Ubuntu', sans-serif;
		font-size: 2rem;
		padding: 0.75rem;
		color: $secondary-color-text;
		background-color: transparent;
		border: none;
		border-top: 1px solid $sidebar-border-color;
		transition: background-color 0.3s;

		&.selected {
			background-color: $primary-color-hover;
		}

		&:nth-last-child(2) {
			border-bottom: 1px solid $sidebar-border-color;
		}

		&:hover {
			background-color: $primary-color-active;
			cursor: pointer;
		}

		&.inventario span::before {
			content: 'Inventario';
		}

		&.venditeNao span::before {
			content: 'Vendite NAO';
		}

		&.esci {
			width: 100%;
			margin-top: auto;
			
			span::before {
				content: 'Esci';
			}
		}
	}

	&.closed {
		min-width: fit-content;

		.header {
			padding-inline: 0;
			justify-content: center;
			gap: 0;

			&::before {
				content: '';
			}

			.icon {
				rotate: z 180deg;
			}
			
		}

		
		button {
			width: fit-content;

			span {
				display: none;
			} 
		}
	}
}
</style>