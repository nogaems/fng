var nm2 = ["Heist","Sting","Robbery","Heist","Robbery","Heist"];

function nameGen(type){
	var nm1 = ["10,000 Mile","Acrobatics","Aerial","Alpha","Anarchy","Angel","Animal","Annihilation","Apex","Aquatic","Assassination","Asset","Avian","Backfire","Baited","Balance","Bankrupt","Basket Case","Benign","Black Diamond","Blind","Blood Diamond","Bloody","Blunder","Bogus","Bread","Breadcrumb","Breakdown","Bribery","Bulldozer","Bully","Business","Butcher","CEO","Cannibal","Champion","Chaos","Charade","Child's Play","Cipher","Civil","Clown","Clumsy","Copycat","Corpse","Corruption","Counterfeit","Crooked","Decimation","Demolition","Demon","Desperation","Dilemma","Diplomat","Dirty","Disaster","Diversion","Divine","Dread","Duped","Duplicate","Earthquake","Echo","Enigma","Epitome","Equality","Escort","Ethereal","Evanescence","Evaporation","Evil Incarnate","Extermination","Fake Out","False","Family","Feral","Fire","Floating","Flood","Fluke","Flying","Fool's","Fool's Errand","Foolproof","Forsaken","Framed","Fruitcake","Fury","Gambit","Genocide","Getaway","Ghost","Gopher","Grave","Grease","Great Food","Grim","Grim Reaper","Guardian","Gunpowder","Hallowed","Happy","Harrier","Hollow","Homicide","Honeycomb","Honorable","Hostage","Hummiliation","Hurricane","Hysteria","Ignition","Illusion","Imaginary","Inferno","Insanity","Insider","Intimidation","Investment","Ire","Junior","Killing","Labyrinth","Landmine","Laughing","Lethal","Lightning","Limbo","Liquid","Lookalike","Lottery","Lucky","Lunatic","Mad","Magician","Maniac","Martyr","Masked","Massacre","Medieval","Meteor","Midnight","Mile High","Mime","Mirror","Misdirection","Mobile","Mock","Mole","Mulligan","Mystery","Naked","Neglect","Neighbor","Noble","Noon","Obliteration","Oblivion","Omega","Paragon","Parallel","Pawn","Perfect","Phantom Thief","Picnic","Plague","Poison","Polite","Premium","Prime","Prototype","Pseudo","Psycho","Punishment","Rampage","Red Herring","Refund","Repeat","Replica","Reverse","Riddle","Robin Hood","Rookie","Ruthless","Sacrificial","Savage","Scapegoat","Seduction","Senior","Sentinel","Shepherd","Shock and Awe","Slayer","Sleaze","Smoke Screen","Smoke and Mirrors","Smooth","Smut","Stained","Sugarcoated","Sullied","Switcheroo","Termination","Terror","Textbook","Thunder","Titan","Torture","Treasure","Twin","Tyrant","Undead","Underdog","Vanishing","Venom","Vigilante","Void","Voodoo","Walking Dead","Warden","Watchdog","Wild Goose","Witchcraft","Worthless","Zero","Zombie"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = "The " + nm1[rnd] + " " + nm2[rnd2];
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