<script setup>
import TabMenu from '../TabMenu.vue'
import InSospeso from './InSospeso.vue'
import Cronologia from './Cronologia.vue'

import { ref } from 'vue';

const tabMenuViews = [{
	title: 'In Sospeso',
	icon: 'venditeInSospeso'
}, {
	title: 'Cronologia',
	icon: 'visualizza'
}]

const currentView = ref(tabMenuViews[0].title)
</script>

<template>
	<div class="main-content-wrapper">
		<TabMenu :views="tabMenuViews" title="Vendite NAO" @selection="currentView = $event"/>
		<div class="tab-content-wrapper">
			<InSospeso v-if="currentView == 'In Sospeso'"/>
			<Cronologia v-else-if="currentView == 'Cronologia'"/>
		</div>
	</div>
</template>

<style scoped lang="scss">
</style>./InSospeso.vue