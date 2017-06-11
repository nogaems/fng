var names1 = ["Acid Bath","Acid Face","Alligator","Angel Eye","Angel Smile","Angel Wings","Anniversary","Archangel","Axe","Baby-Sit","Babyface","Back Alley","Backpack","Backstab","Bald","Bedroom","Bike Path","Birthmark","Bitemark","Black Forest","Blackout","Bleach","Blind","Blind Date","Blood Drop","Blood Painting","Blood Spatter","Blue Moon","Blunt Force","Bonbon","Boulder","Boulevard","Breakfast","Brewery","Brick","Bride","Broomstick","Brunch","Business","Busride","Campsite","Candy","Cannibal","Canvas","Casanova","Challenge","Chameleon","Chocolate","Cinder Block","Citizen","Classified","Claw","Clean","Clownface","Cocktail","Collection","Comic","Commute","Concrete","Confidential","Construction Site","Copy Cat","Corridor","Cosmetic","Cropfield","Cross-Country","Customer","Cyber","Dawn","Daybreak","Demon","Demon Eyes","Dessert","Dinner","Discount","Disguised","Dollhouse","Door To Door","Doorbell","Downtown","Drama","Dumpster","Dusk","Education","Effigy","Emergency","Evening","Evil Eye","Exorcism","Eyeless","Fast Food","Festival","Fetish","Figurine","Final Station","First Aid","Freeway","Full Moon","Ghost","Giggling","Grainfield","Groomsman","Guest","Guest Room","Habit","Hair Band","Hairless","Half-Moon","Hallway","Hammock","Handcuff","Happy Face","Harborview","Harlequin","Hatchet","Highscore","Highway","Hillside","Hitchhiker","Holiday","Homesick","Hook","Hospital","Hostel","Hotel","Identical","Incognito","Institution","Jolly","Knock Knock","Knockout","Lipstick","Lobby","Lonely","Lonely Heart","Luck","Lunch","Machete","Mad Dog","Makeup","Manacle","Marionette","Masked","Melonball","Midnight","Midtown","Mirror","Monday","Morning","Motel","Mountain","Naked","Network","Newlywed","Night Stalker","Nightfall","Nylon","Obsession","Odd Job","Online","Painting","Pancake","Parallel","Pastry","Pathway","Phantom","Phoenix","Phonecall","Phony","Pixy","Plain","Portrait","Pretend","Protocol","Pub","Pubcrawl","Pudding","Pygmy","Rabid","Ragdoll","Recycle","Red Petal","Resident","Ritual","Routine","Royal","Rubberneck","Sad Face","Sailing","Sandwich","Sanguine","Scarlet","Scholarship","Scissors","Score Keeper","Scrapyard","Seashore","Serpent","Servant","Shackle","Shoebox","Shopping Bag","Shotgun","Sickle","Silk","Sleeping","Spider","Spotless","Stocking","Strawberry","Streetlight","Stripping","Sunday","Sundown","Sunrise","Sunset","Symmetric","Talon","Tavern","Tomahawk","Toothless","Torment","Torso","Tortoise","Torture","Tourist","Toybox","Trailer Park","Trailside","Trainride","Trash Bag","Trash Can","Twilight","Twin","Two Coin","Undercover","Vampire","Visitor","Voodoo","Wanted-Ad","Wayfare","Weekend","Werewolf","White Rose","Widow","Witchcraft","Woodwork","World Record","Zoo"];
var names2 = ["Murderer","Killer","Butcher","Slayer"];
var names3 = ["Alien","Alligator","Seductress","Angel of Death","Angelmaker","Babyface","Baker","Bandit","Barbarian","Barber","Basher","Beast","Behemoth","Bigot","Biter","Bloodhound","Bomber","Bonekeeper","Brute","Butcher","Butler","Buzzard","Cannibal","Casanova","Chef","Chopper","Claw","Cleaver","Clobber","Clown","Cook","Copy Cat","Creature","Degenerate","Delirious","Demon","Dentist","Dicer","Disfigured","Doctor","Dog","Dummy","Executioner","Fang","Fiend","Fist","Frankenstein","Freak","Gambler","Ghost","Ghoul","Glutton","Grappler","Grave Robber","Hacker","Hook","Hunter","Informant","Insane","Jester","Kidnapper","Lunatic","Mad Dog","Man Eater","Maniac","Medic","Mime","Mincer","Model","Monster","Mutant","Night Stalker","Nurse","Nutcase","Outsider","Pale","Phantom","Pied Piper","Poisoner","Primitive","Professor","Psycho","Reaper","Ripper","Savage","Scalpel","Scar","Scientist","Scissors","Scythe","Senior","Serpent","Servant","Shadow","Shaver","Skeleton","Skinner","Skull","Slasher","Slayer","Slice and Dicer","Slicer","Snatcher","Sniper","Snitch","Spectator","Spider","Stalker","Stranger","Strangler","Stripper","Surgeon","Terminator","Therapist","Tourist","Tracker","Trapper","Vampire","Vermin","Watcher","Weasel","Weirdo","Werewolf","Whale","Whip","Whisper","Widow Maker","Wolf","Zombie"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * names1.length);
			rnd2 = Math.floor(Math.random() * names2.length);
			names = "The " + names1[rnd] + " " + names2[rnd2];
		}else{
			rnd = Math.floor(Math.random() * names3.length);
			names = "The " + names3[rnd];
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