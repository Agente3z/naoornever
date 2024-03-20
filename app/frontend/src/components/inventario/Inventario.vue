<script setup>
import TabMenu from '../TabMenu.vue';
import Visualizza from './Visualizza.vue';
import Aggiungi from './Aggiungi.vue';
import Inserisci from './Inserisci.vue';

import { ref } from 'vue';

const tabMenuViews = [
	{ 
		title: 'visualizza',
		icon: 'visualizza'
	},
	{
		title: 'aggiungi',
		icon: 'aggiungi'
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
			<Aggiungi v-else-if="currentView == 'aggiungi'"/>
			<Inserisci v-else-if="currentView == 'inserisci'"/>
		</div>
	</div>
</template>

<style scoped lang="scss">
</style>