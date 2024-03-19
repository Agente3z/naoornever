<script setup>
import Login from './views/Login.vue'
import Mainpage from './views/Mainpage.vue'

import { provide, ref } from 'vue'

const user = ref({})
provide('user', user);
</script>

<template>
	<div class="wrapper">
		<Mainpage v-if="user" :user="user"/>
		<Login v-else/>
	</div>
</template>

<style scoped lang="scss">
.wrapper {
	height: 100vh;
	width: 100vw;
}
</style>
