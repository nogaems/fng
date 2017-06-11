function nameGen(type){
	var nm1 = ["Abzu","Achelous","Acionna","Aegaeon","Aegir","Agunua","Agwe","Ahti","Akheilos","Alignak","Alpheus","Amathaunta","Amemasu","Amphitrite","Anahita","Anapos","Anuket","Apah","Asherah","Aspidochelone","Atlantis","Atrimpas","Bakunawa","Bandua","Belisama","Brizo","Capricorn","Carcinus","Ceto","Cetus","Charybdis","Clermeil","Condatis","Cymopoleia","Dakuwaqa","Daucina","Davy Jones","Delphin","Doris","Durius","Ebisu","Eidothea","Eingana","Electra","Enki","Euryale","Eurybia","Ezili","Fontus","Freyr","Galene","Ganga","Glaucus","Gorgon","Graeae","Haik","Hapi","Hippocampus","Hydra","Idemili","Ikatere","Illuyanka","Imoogi","Jormungandr","Juturna","Kamohoalii","Kanaloa","Khnum","Kraken","Lados","Leucothea","Leviathan","Lir","Llyr","Longma","Longmu","Lotan","Makara","Mammu","Marduk","Martuv","Mazu","Medusa","Mermaid","Merman","Mizuchi","Naiades","Namaka","Nanshe","Nehalennia","Nepra","Nepthys","Neptune","Nereides","Nereus","Neringa","Neris","Nerites","Nerthus","Nessie","Nix","Njord","Nodens","Nommos","Nu","Nyakaio","Nymph","Oceanus","Opochtli","Oshun","Osiris","Palaemon","Pan","Pandora","Pariacaca","Paricia","Phorcys","Pontus","Poseidon","Potamoi","Presno","Proteus","Psamathe","Ran","Saga","Salacia","Samundra","Satet","Sculla","Scylla","Sedna","Sequana","Sinann","Siren","Sirena","Sirsir","Siyokoy","Sobek","Stheno","Suijin","Susanoo","Tangaroa","Tapti","Tefnut","Telchine","Tethys","Thalassa","Thaumas","Thetis","Tiamat","Tiberinus","Tlaloc","Triteia","Triton","Tritone","Ukupanipo","Urashi","Varuna","Veles","Vellamo","Volturnus","Watatsumi","Wirnpa","Yam","Yami","Yemoja","Yurlungur"];
	var nm2 = ["Abalone","Albacore","Amberjack","Anemone","Angelfish","Angler","Anglerfish","Barnacle","Barracuda","Bass","Bull Shark","Carp","Clam","Cod","Conch","Crab","Crocodile","Cuttlefish","Dolphin","Dragonet","Dugong","Eel","Flounder","Fringehead","Fugu","Goblin Shark","Great White","Grouper","Haddock","Halibut","Hammerhead","Hapuka","Hermit","Hermit Crab","Herring","Humpback","Irukandji","Jellyfish","Killer Whale","Kingfish","Lionfish","Lobster","Loggerhead","Mackerel","Man o' War","Manatee","Manta","Marlin","Megalodon","Monkfish","Moray","Mulloway","Narwhal","Nautilus","Octopus","Orca","Otter","Oyster","Porpoise","Puffer","Pufferfish","Quahog","Ray","Salmon","Sea Horse","Sea Lion","Sea Snake","Seadragon","Seal","Shark","Shrimp","Snapper","Spider Crab","Squid","Starfish","Stingray","Sturgeon","Swordfish","Triggerfish","Tuna","Turtle","Urchin","Walrus","Whale","Whapuku","White Whale","Wobbegong","Wolffish","Wrasse","Xiphias","Xiphosura"];
	var nm3 = ["Achiever","Adventure","Aftermath","Agent","Ambition","Analysis","Analyst","Aspect","Authority","Blade","Boundary","Bravery","Brilliance","Brutality","Champion","Chaos","Clarity","Confidence","Consequence","Courage","Curtain","Delight","Delivery","Desire","Destiny","Determination","Dexterity","Discovery","Distribution","Elegance","Enigma","Eternity","Fluke","Focus","Fortune","Freedom","Generosity","Grace","Grandure","Guidance","Harmony","Humility","Impulse","Independence","Infinity","Intelligence","Intervention","Journey","Judgment","Justice","Liberty","Matriarch","Mercy","Miracle","Omen","Opportunity","Oracle","Patience","Patriarch","Patriot","Perseverance","Philosophy","Possibility","Precision","Pride","Principle","Priority","Psychology","Quest","Request","Requiem","Research","Respect","Response","Responsibility","Royalty","Secretary","Shadow","Signature","Solitude","Solution","Storm","Stranger","Strategy","Surgery","Sympathy","Theory","Thrill","Thunder","Tourist","Victory","Visitor","Voyage","Wonder"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 3){
			rnd = Math.random() * nm1.length | 0;
			names = "The " + nm1[rnd];
			nm1.splice(rnd, 1);
		}else if(i < 7){
			rnd = Math.random() * nm2.length | 0;
			names = "The " + nm2[rnd];
			nm2.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm3.length | 0;
			names = "The " + nm3[rnd];
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