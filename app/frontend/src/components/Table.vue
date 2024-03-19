<script setup>
import Multiselect from 'vue-multiselect'
import 'vue-multiselect/dist/vue-multiselect.css'
import Icon from './Icon.vue'

import { ref } from 'vue';

/* TODOs:
	fix position sticky not working
*/

const props = defineProps(['data'])

const filters = ref({})
const searchQuery = ref('')

function getFilterOptions(header) {
	const filterOptions = [];
	props.data.rows.forEach(row => {
		filterOptions.find(option => option.name == row[header]) || filterOptions.push({ name: row[header]});
	});
	return filterOptions;
}

function getFilterValues() {
	const filterValues = {};
	for(const header in filters.value) {
		filterValues[header] = filters.value[header].map(option => option.name);
	}
	return filterValues;
}

function isRowVisible(row) {
	const filterValues = getFilterValues();
	for(const header in filterValues) {
		if(filterValues[header].length == 0)
			continue;
		if(!filterValues[header].includes(row[header]))
			return false;
	}
	if(searchQuery.value.length > 0) {
		for(const field in row) {
			if(searchQuery.value.length > row[field].toString().length) {
				if(searchQuery.value.toLowerCase().includes(row[field].toString().toLowerCase()))
					return true;
			} else {
				if(row[field].toString().toLowerCase().includes(searchQuery.value.toLowerCase()))
					return true;
			}
		}
		return false;
	}
	return true;
}

</script>

<template>
	<div class="table-wrapper">
		<div class="searchbar-wrapper">
			<Icon type="cerca" color="primary" class="icon"/>
			<input type="text" class="searchbar" placeholder="Cerca..." v-model="searchQuery">
		</div>
		<div class="body-wrapper">
			<table class="body">
				<tr class="row">
					<th class="header" v-for="header, index in data.headers">
						<div class="inner">
							<label :for="index">{{ header }}</label>
							<Multiselect
								class="filter"
								v-model="filters[header]"
								:options="getFilterOptions(header)"
								:multiple="true"
								:hide-selected="true"
								:close-on-select="false"
								placeholder="Seleziona"
								select-label=""
								label="name"
								track-by="name"
							>
								<template #option="{ option }">
									{{ option.name }}
								</template>
								<template #noResult>Nessun risultato.</template>
							</Multiselect>
						</div>
					</th>
				</tr>
				<tr class="row" v-for="row in data.rows" v-show="isRowVisible(row)">
					<td v-for="header in data.headers" class="cell">
						<div class="inner">
							{{ row[header] }}
						</div>
					</td>
				</tr>
			</table>
		</div>
	</div>
</template>

<style scoped lang="scss">
@import '../style/colors.scss';
.table-wrapper {
	max-height: 100%;
	width: 100%;
	display: flex;
	flex-direction: column;
	gap: 2rem;

	.searchbar-wrapper {
		width: 100%;
		height: 3rem;
		display: flex;
		align-items: center;
		gap: 0.5rem;
		padding: 0.5rem;
		border: 2px $primary-color solid;
		border-radius: 5px;
		background-color: $components-color;
		
		.searchbar {
			height: 100%;
			width: 100%;
			border: none;
			font-size: 1.2rem;
			background-color: transparent;
			outline: none;
		}
	}

	table, tr, th, td {
		padding: 0;
		height: fit-content;
		border-collapse: collapse;
		border: 1px $primary-color solid;
	}

	table {
		border-style: hidden;
	}
	
	.body-wrapper {
		width: 100%;
		height: 100%;
		overflow: auto;
		border: 1px black solid;

		.body {
			position: relative;
			width: 100%;
			background-color: $components-color;

			.row {
				
				.header .inner {
					height: 100%;
					position: sticky;
					top: 0;
					display: flex;
					justify-content: space-between;
					align-items: center;
					gap: 1rem;
					padding: 0.5rem 1rem;
					text-align: center;
					text-transform: capitalize;
					background-color: $primary-color;
					color: $primary-color-text;
					font-size: 1.2rem;
					font-weight: 500;
					
					.filter {
						width: 10rem;
					}
				}

				.cell .inner {
					padding: 0.5rem 1rem;
					display: flex;
					align-items: center;
					text-wrap: nowrap;
				}
			}
		}
	}
}
</style>