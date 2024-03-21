let container = null;
let card_template = null;
let subtitle_container = null;

let DOMContentLoaded = false;
document.addEventListener('DOMContentLoaded', _ => {
	DOMContentLoaded = true;
	container = document.querySelector('.cards-container');
	card_template = document.querySelector('[template]');
	subtitle_container = document.querySelector('.subtitles span');
});

function waitForDOM() {
	while(!DOMContentLoaded) {
		// wait for DOMContentLoaded
	}
}

const data = [];

function drawCards(products) {
	waitForDOM();

	container.innerHTML = '';

	container.classList.remove('one-card', 'two-cards', 'more-cards');
	switch(products.length) {
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

	products.forEach(product => {
		const card = card_template.cloneNode(true);
		card.removeAttribute('template');
		card.addEventListener('click', _ => {
			window.location = product.link;
		});
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

let current_subtitle = '';
const subtitles = [];
let subtitle_number = 0;

function checkIfNewSubtitle(subtitle) {
	return current_subtitle !== subtitle
}

function tokenizeSubtitles(subtitle) {
	subtitles.length = 0;
	subtitle_number = 0;
	current_subtitle = subtitle;
	const words = subtitle.split(' ');
	const subtitleSize = 6;
	for (let i = 0; i < words.length; i += subtitleSize) {
		const row = words.slice(i, i + subtitleSize).join(' ');
		subtitles.push(row);
	}
}

function getNextSubtitle() {
	const subtitle = subtitles[Math.round(subtitle_number/10)];
	subtitle_number++
	return subtitle || '';
}

function drawSubtitles(subtitle) {
	waitForDOM();
	if(checkIfNewSubtitle(subtitle)) {
		tokenizeSubtitles(subtitle);
	}
	subtitle_container.dataset.text = getNextSubtitle();
}

const socket = new WebSocket('ws://192.168.71.173:8766');

socket.onopen = (e) => {
	console.log('[open] Connection established');
};

socket.onmessage = (e) => {
	console.log(`[message] Data received from server ${e.data}`);

	data.length = 0;
	Object.assign(data, JSON.parse(e.data));
	//console.log(data);
	drawCards(data.products);
	drawSubtitles(data.subtitle);
};

socket.onclose = (e) => {
	if (e.wasClean) {
		console.log(`[close] Connection closed cleanly, code=${e.code} reason=${e.reason}`);
	} else {
		console.error('[close] Connection died');
	}
};