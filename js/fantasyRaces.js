function nameGen(type){
	var nm1 = ["Abyss","Abyssal","Acid","Aerial","Aerie","Air","Anchored","Ancient","Aquatic","Arachnid","Arcane","Arctic","Argent","Ashen","Astral","Aurelian","Aurora","Austere","Austral","Autumn","Awoken","Azure","Barren","Beast","Berserk","Berserker","Blessed","Blight","Blind","Blood","Bog","Bone","Boreal","Boulder","Brass","Broken","Bronze","Brood","Canopy","Canyon","Cave","Cavern","Celestial","Chaos","Chasm","Chromatic","Clockwork","Cloud","Common","Copper","Core","Corrupt","Corrupted","Crimson","Cursed","Dark","Dawn","Deaf","Death","Deep","Demi","Demon","Demonic","Desert","Dew","Dim","Dire","Dirt","Divine","Doom","Dread","Dream","Dusk","Earthen","Eastern","Ebon","Ebony","Edge","Eerie","Elated","Elder","Elemental","Elite","Ember","Empyrean","Enchanted","Eternal","Ethereal","Exalted","Exo","Faerie","Fair","Fallen","False","Fel","Feral","Fey","Fire","First","Flame","Fog","Forest","Forged","Forgotten","Forlorn","Forsaken","Free","Frost","Frozen","Fury","Gear","Ghastly","Ghost","Giant","Gilded","Glacial","Glass","Gold","Grand","Grave","Gray","Great","Green","Grey","Grim","Grizzled","Grizzly","Grotto","Half","Hallowed","Harmony","Haunted","Haunting","Hell","Hellish","High","Highborn","Hill","Hive","Hollow","Humble","Ice","Immortal","Impure","Infernal","Inferno","Infinite","Infinity","Iron","Island","Ivory","Jade","Jungle","Juvenile","Lake","Lava","Light","Lone","Lost","Low","Lucent","Lunar","Mad","Magma","Major","Marked","Marsh","Masked","Metal","Mimic","Minor","Mist","Moon","Morass","Moss","Mountain","Mud","Mute","Mystic","Nebula","Nether","New","Night","Nightmare","Nimbus","Noble","Nocturnal","Nomad","Northern","Numb","Oblivion","Obsidian","Occult","Ocean","Oceanic","Onyx","Painted","Pale","Paragon","Phantom","Phase","Pinnacle","Planar","Plane","Poison","Primal","Prime","Primeval","Primordial","Proto","Pure","Putrid","Pygmy","Rabid","Radiant","Regal","Reserve","River","Rock","Royal","Sable","Sabre","Sacred","Salt","Sand","Sanguine","Savage","Scaled","Scourge","Sea","Serpent","Shadow","Shard","Shore","Silent","Silver","Skeletal","Sky","Smog","Smoke","Snow","Solar","Sorrow","Southern","Spectral","Spirit","Spring","Star","Stark","Stone","Storm","Subterranean","Summer","Sun","Supreme","Surface","Swamp","Tempest","Thunder","Timber","Timeless","Titan","Tomb","Torment","Torn","Tundra","Twilight","Urban","Valley","Veil","Veiled","Velvet","Venom","Vile","Violet","Void","Volcano","Warped","Waste","Western","Wicked","Wild","Winter","Wood","World","Wrath","Wretched","Zephyr"];
	var nm2 = ["Angels","Beasts","Boggart","Centaurs","Demons","Dragonborn","Dryads","Dwarves","Elementals","Elves","Ents","Fairies","Faun","Fiends","Folk","Giants","Gnolls","Gnomes","Goblins","Golems","Goliaths","Gorgons","Gremlins","Hagravens","Hags","Halflings","Harpies","Hobbits","Hobgoblins","Humans","Imps","Kobolds","Lamia","Merfolk","Minotaurs","Naga","Nymphs","Oceanids","Ogres","Lich","Gargoyles","Grendels","Draugr","Kappa","Oni","Wendigo","Drake","Dragonborn","Ghouls","Grell","Hydra","Trogg","Orcs","People","Satyr","Siren","Spriggan","Sylphs","Trolls","Undine","Valkyrie","Vampires","Werewolves"];
	
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if($('#firChange').is(':checked')){
			val = $('.firChange').val();
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = val + " " + nm2[rnd2];
		}else if($('#secChange').is(':checked')){
			rnd = Math.floor(Math.random() * nm1.length);
			val = $('.secChange').val();
			names = nm1[rnd] + " " + val;
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + " " + nm2[rnd2];
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