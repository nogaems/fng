
function nameGen(){
	var nm1 = ["Abyssal","Airy","Amber","Ancient","Angelic","Arcane","Arctic","Aromatic","Aurora","Awoken","Azure","Beryl","Blossom","Blossoming","Blue Moon","Blushing","Boiling","Bold","Brilliant","Bronze","Bubbling","Carmine","Cerulean","Changing","Chasm","Chittering","Chuckling","Claret","Cleansing","Coiling","Convex","Crane","Crawling","Crescent","Croaking","Curiosity","Curious","Dahlia","Dancing","Dark","Daydream","Demilune","Discovery","Divine","Eastern","Ebony","Electric","Empty","Enchanted","Enchanting","Enigma","Enlightened","Enlightenment","Evergreen","False","Firefly","Flickering","Foggy","Forbidden","Forsaken","Fragrant","Frozen","Geiser","Glass","Gleaming","Glistening","Glowing","Golden","Grand","Great","Halcyon","Half","Harmony","Hollow","Holy","Hotspring","Infinite","Infinity","Ivory","Jade","Laughing","Lava","Little","Living","Lone","Lonely","Lost","Luminous","Lunar","Lune","Lurking","Lustrious","Lustrous","Magma","Majestic","Malachite","Mammoth","Maroon","Meditating","Meditation","Merry","Mountain","Mumbling","Mystery","Nightmare","Northern","Observing","Oracle","Ornate","Petal","Phantom","Pinnacle","Pioneer","Prime","Radiant","Raging","Repose","Resting","Roaring","Royal","Rumbling","Running","Rustling","Saffron","Sanguine","Sapphire","Savage","Scarlet","Scented","Serene","Serenity","Serpent","Shade","Shadow","Shady","Shallow","Shimmering","Shivering","Shrouded","Sickle","Silent","Silver","Skyfall","Sleeping","Sleepy","Smoldering","Sneaking","Snoring","Solitude","Soothing","Southern","Sparkling","Starfall","Sweet","Swirling","Tamed","Tempered","Tempest","Timeless","Tranquil","Tranquility","Triumph","Twin","Veiled","Velvet","Verdigris","Vertex","Vibrant","Vine","Violet","Viridian","Volcano","Vortex","Waking","Wandering","Watching","Weeping","Western","Whisper","Whispering","Whistle","Whistling","Wicked","Wilted","Windy","Wish","Wishing","Youth"];
	var nm2 = ["Oasis","Spring","Fountain","Oasis","Oasis","Oasis","Oasis","Oasis","Oasis","Oasis"];
	var nm3 = ["Afternoons","Ancestors","Angels","Animals","Arcane","Auras","Autumn","Ballance","Change","Clouds","Crimson","Crossroads","Curiosity","Daydreams","Desire","Destiny","Discovery","Dreams","Fall","Fortune","Gardens","Glass","Gold","Guidance","Harmony","Hope","Ice","Infinity","Iron","Jade","Jewels","Knowledge","Life","Light","Lights","Love","Luck","Magic","Meditation","Melodies","Memories","Metal","Music","Observation","Ornaments","Passages","Peace","Pleasure","Pleasures","Power","Prosperity","Purity","Rain","Rhythms","Riddles","Roses","Sanctity","Sanctuaries","Sapphire","Scents","Serenity","Serpents","Shadows","Shrines","Silk","Silver","Smiles","Solitude","Song","Spirits","Spring","Steam","Summer","Thought","Thoughts","Thrills","Time","Tranquility","Treasures","Voices","Voyages","Waves","Whispers","Wind","Winter","Wishes","Youth","the Aurora","the Celestial","the Clouds","the Divine","the Garden","the Light","the Moon","the Night","the Senses","the Sky","the Stars","the Sun","the Temple"];

	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm2.length);
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			names = "The " + nm1[rnd] + " " + nm2[rnd2];
			nm1.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			names = "The " + nm2[rnd2] + " of " + nm3[rnd];
			nm3.splice(rnd, 1);
		}
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}