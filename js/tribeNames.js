var names1 = ["Ancient","Angry","Arcane","Arctic","Berserk","Big","Bitter","Black","Blessed","Blind","Blue","Brave","Bright","Broken","Bronze","Brown","Burned","Clay","Cold","Crazy","Crimson","Cruel","Dark","Dead","Diamond","Dirty","Ebon","Eternal","Evil","Falling","False","First","Free","Frozen","Gentle","Giant","Gifted","Golden","Grave","Gray","Green","Grim","Half","Hard","Hell","Hidden","High","Impure","Infamous","Invincible","Iron","Large","Last","Light","Lost","Loyal","Magic","Master","Mean","Middle","Miracle","Misty","Molten","Murky","Mute","Night","Nightmare","Original","Pale","Poison","Prime","Pure","Quiet","Rabid","Rapid","Reckless","Red","Risen","Rising","Rude","Salty","Sapphire","Savage","Shadow","Silent","Silver","Small","Smelly","Standing","Steel","Stone","Strong","Swift","True","Twilight","Twin","Undead","Vicious","White","Yellow"];
var names2 = ["Ancestor","Angel","Ant","Arrow","Ash","Aura","Axe","Bat","Bear","Bison","Bone","Bones","Boulder","Bow","Brothers","Cave","Claw","Cloak","Coyote","Crow","Crown","Dagger","Demon","Dragon","Eagle","Ear","Earth","Ember","Eye","Feet","Finger","Fire","Fish","Fist","Foot","Forest","Fox","Fury","Ghost","Giant","God","Hammer","Hand","Hawk","Heaven","Hill","Hounds","Hunt","Island","Lake","Lightning","Lion","Mage","Mammoth","Moon","Mountain","Mouth","Oracle","Owl","Paw","Phantom","Phoenix","Rage","Raven","Ribbon","River","Rock","Sand","Scar","Scorpion","Sea","Seer","Shark","Shield","Sisters","Skeleton","Skull","Snake","Snow","Spear","Spider","Spirit","Stag","Stalker","Star","Storm","Sun","Swamp","Sword","Thunder","Titan","Tooth","Tower","Watch","Water","Whisper","Wing","Witch","Wolf","Woods"];
var names3 = ["Tribe","Kin","Clan","Warriors","Children","Caste","Horde","Tribe"];
var br = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		rnd2 = Math.floor(Math.random() * names2.length);
		rnd3 = Math.floor(Math.random() * names3.length);
		names = "The " + names1[rnd] + " " + names2[rnd2] + " " + names3[rnd3];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}