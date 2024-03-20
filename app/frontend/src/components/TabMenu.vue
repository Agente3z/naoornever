<script setup>
import Icon from './Icon.vue'

import { ref } from 'vue'

const props = defineProps(['title', 'views'])
const emit = defineEmits(['selection'])

const currentView = ref(props.views[0].title)
function switchView(viewTitle) {
	currentView.value = viewTitle;
	emit('selection', viewTitle);
}

</script>

<template>
	<div class="header">
		<h1> {{ title }} </h1>
		<div class="buttons-wrapper"> 
			<button v-for="view in views" :class="{'selected': currentView == view.title}" @click="switchView(view.title)">
				<Icon :type="view.icon" :color="currentView != view.title ? 'primary' : 'background'" class="icon"/>
				<span> {{ view.title }} </span>
			</button>
		</div>
	</div>
</template>

<style scoped lang="scss">
@import '../style/colors.scss';

.header {
	// border: 1px solid green;
	min-width: fit-content;
	display: flex;
	gap: 1rem;
	border-bottom: 4px solid $primary-color;
	
	h1 {
		white-space: nowrap;
		margin: 0;
		font-size: 2.5rem;
		color: black;
	}

	.buttons-wrapper {
		width: 100%;
		height: 3rem;
		display: flex;
		justify-content: flex-end;

		button {
			width: fit-content;
			display: flex;
			justify-content: center;
			align-items: center;
			gap: 0.5rem;
			padding: 1.5rem 1.3rem;
			transition: background-color 0.3s;
			cursor: pointer;
			color: black;
			text-transform: capitalize;
			font-size: 1.35rem;
			font-weight: 600;
			background-color: transparent;
			border-top-left-radius: 5px;
			border-top-right-radius: 5px;
			border: 2px solid transparent;
			white-space: nowrap;


			&:hover {
				border-color: $primary-color;
			}

			&.selected {
				border-color: $primary-color;
				background: $primary-color;
				color: $background-color;
			}
		}
	}
}
</style>