function nameGen(){
	var nm1 = ["Aether","Aethereal","Alacadabra","Angelic","Arcane","Astral","Aura","Banishing","Banshee","Basilisk","Bog","Celestial","Centaur","Chakra","Changeling","Chaos","Charm","Charmed","Chimera","Cipher","Clairvoyance","Clairvoyant","Conjuring","Coven","Crystal","Demon","Diabolical","Divine","Djinni","Dowsing","Dragon","Dryad","Echo","Ecto","Ectoplasm","Eerie","Elemental","Enchanted","Enigma","Ethereal","Evocation","Fairy","Familiar","Fire","Flashing","Flux","Flying","Fortune","Giant's","Glamour","Goblin","Griffin","Grimoire","Harpy","Haunted","Hellion","Hex","Hexing","Hocuspocus","Horror","Hypnosis","Hypnotic","Illusion","Infernal","Invisible","Juju","Kelpie","Lamia","Levitation","Lich","Lucifer","Magician's","Magnetic","Malediction","Menace","Miracle","Mojo","Morphing","Mutant","Mystic","Nether","Ogre","Omen","Oracle","Ouija","Pandora","Paragon","Paranormal","Pendulum","Pentacle","Phantom","Phoenix","Pixie","Prophecy","Prowess","Psi","Psionic","Psychic","Pyro","Qi","Rune","Scale","Scrying","Seance","Shade","Shadow","Sigil","Siren","Skeleton","Sorcerous","Specter","Spectral","Spirit","Tantra","Titan","Totem","Totemic","Transmutation","Treant","Troll","Undine","Vampire","Vanishing","Void","Voodoo","Warlock","Wendigo","Werewolf","Witcher","Witches'","Wither","Wizard","Wyvern","Zombie"];
	var nm2 = ["Ache","Aches","Affliction","Amnesia","Anemia","Blight","Blindness","Blisters","Blood","Breakdown","Burn","Chills","Cold","Cough","Cramps","Curse","Death","Decay","Delirium","Delusion","Dementia","Disease","Disorder","Doom","Drip","Fatigue","Fever","Flu","Gut","Haze","Infection","Insanity","Limb","Madness","Malady","Mark","Plague","Pox","Puffs","Rage","Rash","Rot","Shakes","Sickness","Sores","Spasm","Spasms","Syndrome","Thirst","Vapors","Virus","Warts"];
	var br = "";

	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + " " + nm2[rnd2];
		nm1.splice(rnd, 1);
		nm2.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}