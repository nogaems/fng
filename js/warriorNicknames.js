var nm1 = ["The Animal","The Anomaly","The Anvil","The Army","The Axe","The Barbarian","The Bear","The Bearclaw","The Beast","The Behemoth","The Blade","The Bloodlust","The Bloody","The Boar","The Boulder","The Boulderfist","The Brute","The Bull","The Butcher","The Challenger","The Champion","The Cobra","The Colossal","The Colossus","The Conqueror","The Corrupter","The Coyote","The Crooked","The Crow","The Cruel","The Cunning","The Cursed","The Dagger","The Danger","The Deceiver","The Defiant","The Delirious","The Demigod","The Demon","The Deserter","The Destroyer","The Devil","The Dire","The Dire Bear","The Dire One","The Dire Wolf","The Dog","The Dragon","The Dragonheart","The Drake","The Dread","The Edge","The Enigma","The Eternal Hunger","The Exalted","The Executioner","The Exile","The Fang","The Fearless","The Feisty","The Feral","The Fiend","The Fierce","The Fire","The Firestarter","The Flame","The Flurry","The Forsaken","The Freak","The Fury","The Ghost","The Giant","The Giantslayer","The Gold One","The Grave","The Gravedigger","The Gravekeeper","The Grim","The Grotesque","The Guardian","The Hallowed","The Hammer","The Hawk","The Heartless","The Hog","The Hollow","The Honorbound","The Honorless","The Horror","The Hound","The Hunger","The Hungry","The Hunter","The Hurricane","The Impure","The Insane","The Invincible","The Ironclad","The Ironfist","The Jackal","The Jester","The Legionnaire","The Limp","The Lion","The Lionheart","The Lone Wolf","The Magnificent","The Mammoth","The Maneater","The Maniac","The Marked","The Marked One","The Martyr","The Menace","The Merciful","The Miracle","The Monster","The Mountain","The Mutant","The Mute","The Nightmare","The Nightowl","The Noble","The Nobody","The Observer","The Owl","The Ox","The Paragon","The Patient","The Phantom","The Phoenix","The Prince","The Prodigy","The Pyro","The Rabid","The Raven","The Rebel","The Reckless","The Rider","The Rogue","The Sadist","The Sadistic","The Savage","The Scar","The Scarred One","The Sentinel","The Serpent","The Shadow","The Shady","The Shepherd","The Silencer","The Silent","The Silver One","The Skeleton","The Slayer","The Sleeper","The Spider","The Spook","The Storm","The Surgeon","The Swine","The Temper","The Tempest","The Terror","The Thief","The Thirst","The Thug","The Thunder","The Titan","The Tower","The Traitor","The Tyrant","The Undying","The Valiant","The Vengeful","The Venom Tongue","The Vermin","The Vicious","The Viper","The Vulture","The Whisper","The Widow Maker","The Wild","The Wildling","The Wolf","The Wonder","The Wyrm"];
var nm2 = ["Battle","Bear","Blood","Bone","Boulder","Bright","Dark","Dead","Death","Demon","Doom","Dragon","Ember","Fire","Fist","Frost","Fuse","Giant","Gold","Gore","Grand","Great","Hell","Iron","Light","Mammoth","Molten","Night","Phoenix","Proud","Rage","Raven","Red","Rock","Rumble","Shadow","Sharp","Shield","Silent","Silver","Single","Skull","Spirit","Steel","Stone","Storm","Stout","Strong","Swift","Thunder","True","Void","War","Wild","Wolf"];
var nm3 = ["bane","blade","blood","blow","bolt","bow","breaker","brow","chaser","claw","cleaver","crest","cut","eye","fang","fist","flayer","fury","gaze","grim","grimace","grip","hair","hallow","hammer","hand","head","heart","helm","hide","mane","mantle","might","pelt","rage","roar","scar","scream","shade","shadow","shield","shout","snarl","song","sorrow","stare","stride","strike","sword","sworn","talon","thorn","tongue","visage"];
var nm4 = ["",""," "];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd];
		}else{
			rnd = Math.floor(Math.random() * nm2.length);
			rnd2 = Math.floor(Math.random() * nm3.length);
			rnd3 = Math.floor(Math.random() * nm4.length);
			names = nm2[rnd] + nm4[rnd3] + nm3[rnd2];
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