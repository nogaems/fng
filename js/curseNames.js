var nm1 = ["Acrimony","Agony","Amber","Anger","Anguish","Annihilation","Anxiety","Ash","Asperity","Assault","Atonement","Bane","Blood","Bone","Bones","Brass","Catastrophe","Chains","Chaos","Coal","Crimson","Crystal","Darkness","Dawn","Death","Defeat","Depletion","Desire","Desolation","Despair","Destruction","Doom","Dusk","Dust","Earth","Ember","Exctinction","Failure","Fire","Flame","Flesh","Flies","Frenzy","Frost","Furor","Fury","Glass","Gold","Grief","Growth","Hate","Hatred","Heartache","Horns","Hysteria","Ice","Imbalance","Ire","Iron","Isolation","Lava","Lead","Light","Loss","Love","Mania","Marble","Metal","Misery","Misfortune","Nightmares","Obsidian","Onyx","Pain","Passion","Penance","Perdition","Pests","Poison","Poverty","Pride","Prison","Rage","Rain","Rats","Ruin","Runes","Sacrifice","Sand","Scales","Scents","Seclusion","Shadows","Silence","Silk","Silver","Smiles","Smoke","Snow","Solitude","Sorrow","Spasms","Stone","Storms","Teeth","Thunder","Truth","Twilight","Umbrage","Vengeance","Venom","Vermin","Woe","Wrath","the Arachnid","the Banshee","the Bat","the Blaze","the Boulder","the Cave","the Crow","the Crown","the Crypt","the Dark","the Dead","the Dragon","the Feast","the Fire","the Flame","the Flock","the Fog","the Forge","the Grave","the Griffin","the Hallowed","the Heart","the Horn","the Hydra","the Lone Wolf","the Lonely","the Mind","the Mist","the Moon","the Nightmare","the Phoenix","the Prison","the Quill","the Rat","the Reaper","the Ring","the Ruins","the Sanguine","the Seed","the Serpent","the Shade","the Shadows","the Snail","the Storm","the Stranger","the Sun","the Talon","the Titan","the Tomb","the Tyrant","the Veil","the Vermin","the Vessel","the Visitor","the Voice","the Void","the Wild","the Wraith","the Wreckage","the Wyvern","the Zephyr"];
var nm2 = ["Acrimony","Aggression","Agony","Ancient","Angel","Anguish","Anxiety","Arachnid","Avian","Banshee","Bat","Blaze","Boulder","Brass","Canine","Chaos","Cold","Crazy","Creeper","Creeping","Crimson","Crippling","Crow","Crown","Crumbling","Crying","Crypt","Crystal","Dark","Deathbell","Delirium","Demon","Desolation","Devil","Dragon","Dread","Elephant","Ember","Ethereal","Fickle","Flock","Flying","Fog","Forbidden","Forest","Forge","Frenzy","Frost","Frozen","Furor","Fury","Ghast","Ghastly","Ghost","Grave","Harpy","Heartache","Hell","Hellish","Hopeless","Horn","Horror","Hydra","Hyper","Hysteria","Ice","Immobile","Impossible","Ire","Iron","Ironbark","Laughing","Lifeless","Limp","Limp Limb","Mania","Mind","Misery","Misfortune","Moon","Mortal","Necro","Nercrotic","Nightmare","Numb","Paralyzing","Penance","Perdition","Phantom","Pharaoh","Pygmy","Rabid","Restless","Rodent","Rotting","Scale","Seclusion","Serpent","Shadow","Shaking","Shivering","Silence","Silent","Sinister","Smiling","Spirit","Stiffening","Stoneskin","Storm","Strange","Stranger","Sun","Swamp","Terror","Thorn","Thunder","Tomb","Twilight","Undead","Vengeance","Venom","Volatile","Wandering","Wicked","Wraith","Zombie"];
var nm3 = ["Curse","Bane","Jinx","Hex","Vex","Cure","Curse","Curse","Curse","Curse","Curse"];

var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm3.length);
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm3[rnd2] + " of " + nm1[rnd];
		}else{
			rnd = Math.floor(Math.random() * nm2.length);
			while(nm3[rnd2] === nm2[rnd]){
				rnd = Math.floor(Math.random() * nm2.length);
			}
			names = "The " + nm2[rnd] + " " + nm3[rnd2];
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