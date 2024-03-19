<script setup>
import Sidebar from '../components/Sidebar.vue'
import Inventario from '../components/inventario/Inventario.vue'
import VenditeNao from '../components/venditeNao/VenditeNao.vue'

import { ref } from 'vue'

defineProps(['user'])

const currentView = ref('venditeNao')

</script>

<template>
	<div class="mainpage-wrapper">
		<Sidebar class="sidebar" :currentView="currentView" @selection="currentView = $event"/>
		<div class="mainpage">
			<VenditeNao v-if="currentView == 'venditeNao'"/>
			<Inventario v-else-if="currentView == 'inventario'"/>
		</div>
	</div>
</template>

<style scoped lang="scss">
@import '../style/colors.scss';

.mainpage-wrapper {
	height: 100%;
	width: 100%;
	display: flex;
	background-color: $background-color;

	.sidebar {
		width: fit-content;
		height: 100%;
	}

	.mainpage {
		width: 100%;
		height: 100%;
		overflow-y: hidden;
		overflow-x: auto;
	}
}
</style>
