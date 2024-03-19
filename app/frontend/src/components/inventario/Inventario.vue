<script setup>
import TabMenu from '../TabMenu.vue';
import Visualizza from './Visualizza.vue';
import Inserisci from './Inserisci.vue';

import { ref } from 'vue';

const tabMenuViews = [
	{ 
		title: 'visualizza',
		icon: 'visualizza'
	},
	{
		title: 'inserisci',
		icon: 'inserisci'
	}
]

const currentView = ref(tabMenuViews[0].title)
</script>

<template>
	<div class="main-content-wrapper">
		<TabMenu title="Inventario" :views="tabMenuViews" @selection="currentView = $event"/>
		<div class="tab-content-wrapper">
			<Visualizza v-if="currentView == 'visualizza'"/>
			<Inserisci v-else-if="currentView == 'inserisci'"/>
		</div>
	</div>
</template>

<style scoped lang="scss">
</style>