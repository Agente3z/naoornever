let container = null;
let card_template = null;

let DOMContentLoaded = false;
document.addEventListener('DOMContentLoaded', e => {
	DOMContentLoaded = true;
	container = document.querySelector('.cards-container');
	card_template = document.querySelector('[template]');
	drawCards(data);
});

const data = [];

function drawCards(data) {
	while (!DOMContentLoaded) {
		// wait for DOMContentLoaded
	}

	container.innerHTML = '';

	container.classList.remove('one-card', 'two-cards', 'more-cards');
	switch(data.length) {
		case 1:
			container.classList.add('one-card');
			break;
		case 2:
			container.classList.add('two-cards');
			break;
		default:
			container.classList.add('more-cards');
			break;
	}

	data.forEach(product => {
		const card = card_template.cloneNode(true);
		card.removeAttribute('template');
		const img = card.querySelector('img');
		img.src = product.photo;
		const title = card.querySelector('.title');
		title.dataset.text = product.name;
		const dimensioni = card.querySelector('.dimensioni');
		dimensioni.dataset.text = product.dim;
		const peso = card.querySelector('.peso');
		peso.dataset.text = product.weight;
		const prezzo = card.querySelector('.prezzo');
		prezzo.dataset.text = product.cost;

		container.appendChild(card);
	});
}

const socket = new WebSocket('ws://localhost:8766');

socket.onopen = (e) => {
	console.log('[open] Connection established');
};

socket.onmessage = (e) => {
	console.log(`[message] Data received from server: ${e.data}`);

	data.length = 0;
	Object.assign(data, JSON.parse(e.data));
	console.log(data);
	drawCards(data);
};

socket.onclose = (e) => {
	if (e.wasClean) {
		console.log(`[close] Connection closed cleanly, code=${e.code} reason=${e.reason}`);
	} else {
		console.error('[close] Connection died');
	}
};