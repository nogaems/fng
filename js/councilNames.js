function nameGen(){
	var nm1 = ["Abandoned","Adamant","Aegis","Ageless","All-Knowing","Ancient","Angelic","Arachnid","Arch","Austere","Balance","Blind","Brilliant","Bronze","Champion","Chief","Climate","Cloud","Clover","Creation","Crimson","Crown","Dark","Diamond","Dire","Dream","Dual","Earth","Earthen","Ebon","Elated","Elderly","Elite","Ember","Empath","Enchanted","Enlightened","Eternal","Ethereal","Exalted","Fearless","Flame","Forsaken","Garden","Ghost","Golden","Grand","Granite","Hallowed","Harmonious","Harmony","Heavenly","High","Ice","Infernal","Infinite","Infinity","Iris","Iron","Ivory","Jade","Judgment","Justice","Last","Legion","Liberty","Light","Living","Lone","Lunar","Mad","Marked","Masked","Memory","Mercy","Midnight","Moon","Mute","Mystery","Nightmare","Obsidian","Omen","Onyx","Oracle","Oval","Paradox","Parallel","Phantom","Portal","Primal","Prime","Private","Prism","Radiant","Round","Royal","Sanguine","Serpent","Shadow","Silent","Silver","Skeletal","Skeleton","Snow","Solar","Spirit","Storm","Sun","Supreme","Thunder","Tranquil","Tree","Twilight","Twin","Union","Unity","Velvet","Vessel","Voiceless","War","Wicked","Wisdom","Wise","Zephyr"];
	var nm2 = ["Council","Board","Convocation","Congregation","Conclave","Council","Council","Council","Council","Council","Board"];
	var nm3 = ["Advice","Ancients","Angels","Averages","Balance","Beginnings","Birth","Bliss","Blood","Borders","Brilliance","Candles","Chains","Champions","Chaos","Clarity","Corruption","Darkness","Death","Defiance","Dreams","Dust","Duty","Eternity","Evil","Experience","Faith","Fate","Fertility","Ghosts","Glass","Glory","God","Gods","Grace","Harmony","Heaven","Hell","Honor","Hope","Ice","Independence","Infinity","Iron","Justice","Knowledge","Life","Light","Lights","Memories","Mercy","Minds","Mithril","Nightmares","Omens","Opportunity","Peace","Phantoms","Protection","Reality","Rebels","Redemption","Reflection","Riddles","Shadows","Solitude","Spirits","Statues","Time","Tomorrow","Trade","Tranquility","Truth","Twilight","Unity","Victors","Voices","War","Whispers","Widows","Wisdom","the Abandoned","the Afterlife","the Ages","the Ancient","the Blind","the Brave","the Chosen","the Chosen One","the Clouds","the Colossus","the Corrupt","the Crown","the Dark","the Dead","the Defiant","the Enchanted","the End","the Enigma","the Enlightened","the Eternal","the Exalted","the Father","the Few","the Flawed","the Flawless","the Flock","the Forest","the Forgotten","the Forsaken","the Free","the Gifted","the God","the Gods","the Grim","the Hallowed","the Hive","the Hollow","the Honored","the Infinite","the Lake","the Light","the Living","the Many","the Mind","the Mother","the Mountain","the Next Realm","the Night","the Nocturnal","the Ocean","the Oracle","the Owl","the People","the Primal","the Prime","the Radiant","the Rebellion","the River","the Ruins","the Serene","the Storm","the Supreme","the Tempest","the Underworld","the Union","the Wolf"];

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