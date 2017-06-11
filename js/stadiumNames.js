var nm2 = ["Stadium","Bowl","Park","Arena","Centre","Ring","Field","Ground"];
function nameGen(type){
	var nm1 = ["Accord","Adamant","Aegis","Aerie","Affinity","Alabaster","Alliance","Ancestor","Angel","Angel Wing","Animus","Anniversary","Anomaly","Apex","Arch","Aria","Arrowhead","Aurelian","Aureole","Aurora","Azure","Bamboo","Bauble","Beacon","Bell","Bird Nest","Blessing","Blossom","Blue Moon","Borealis","Burrow","Canvas","Cardinal","Celebration","Celestial","Central","Century","Ceremony","Champion","Cherub","Chimera","Chronicle","Cinder","Cipher","Cloud","Clover","Coalition","Community","Compass","Connection","Conquest","Convex","Core","Corona","Cosmos","Courage","Crescent","Crimson","Crown","Crux","Crystal","Curator","Dawn","Daydream","Delight","Den","Destination","Destiny","Diamond","Diorama","Discovery","Dominion","Dream","Ebon","Echo","Eclipse","Element","Ember","Emerald","Enclave","Eos","Epiphany","Epitome","Epoch","Essence","Eternity","Euphony","Exhibition","Expedition","Expo","Faith","Fate","Floret","Fortune","Founders","Fragment","Full Moon","Fusion","Galaxy","Gateway","Gemstone","Genie","Gilded","Gold","Gold Nugget","Grace","Grand","Grand Arc","Griffon","Halo","Harmony","Heart","Heirloom","Helix","Herald","Heritage","Hero","Homage","Honor","Horizon","Horoscope","Hourglass","Hunter","Huntress","Illusion","Imagination","Immortal","Impulse","Independence","Infinity","Iron","Ivory","Jade","Jubilee","Kindred Souls","Lantern","Legacy","Liberty","Locomotion","Lotus","Lucent","Lunar","Lyric","Marble","Marquis","Marvel","Matron","Meadow","Melody","Memorial","Metronome","Millennium","Miracle","Mirage","Mirror","Monolith","Moonlight","Mosaic","Muse","Myriad","Nebula","Night","Nimbus","Obelisk","Obsidian","Oculus","Omen","Onyx","Oracle","Orbit","Orchard","Ornament","Oval","Palace","Panorama","Panther","Parade","Paragon","Parallel","Particle","Patron","Pendulum","Phantom","Phenomenon","Phoenix","Pinnacle","Pioneer","Portal","Prestige","Pride","Prime","Prism","Prodigy","Promise","Prophecy","Prospect","Pure Heart","Purity","Quest","Rainbow","Renaissance","Revelation","Reverie","Rex","Rhythm","Riverside","Rose","Royal","Ruby","Saffron","Sanctum","Sapphire","Sensation","Seraph","Serenity","Silver","Snowflake","Solar","Solstice","Songbird","Soul","Spectacle","Spectrum","Speculum","Sphere","Spirit","Sprite","Starlight","Stasis","Stratosphere","Sunset","Supreme","Symphony","Synthesis","Tableau","Timeless","Tribute","Trinity","Triumph","Trust","Tulip","Twilight","Twin","Unity","Universe","Valley","Valor","Velvet","Venture","Vertex","Victory","Visage","Vision","Vista","Vortex","Voyage","White Stag","Willow","Wish","Zion","Zodiac"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd] + " " + nm2[rnd2];
		nm1.splice(rnd, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}