
function nameGen(){
	var nm1 = ["Abyss","Adventure","Aftermath","Ambition","Angel","Apparatus","Arachnid","Arch","Balance","Balloon","Baron","Basin","Loophole","Expedition","Battle","Beast","Beauty","Blade","Bluff","Bomb","Bomber","Boost","Boulder","Brass","Brass Knuckle","Bridge","Brutality","Bullet","Candle","Cannon","Canyon","Chain","Chaos","Chasm","Chimera","Cliffhanger","Comet","Commando","Condor","Cork","Count","Courage","Crook","Cross","Crown","Curse","Curtain","Curve","Daemon","Death","Delight","Demon","Desire","Devil","Diamond","Dimension","Diver","Divide","Division","Dread","Dream","Dreamscape","Earthquake","Enchantment","Enigma","Eruption","Escape","Eternity","Eventide","Evolution","Explosion","Extreme","Fall","Feather","Figure","Fire","Fireball","Flake","Flame","Flight","Flock","Fluke","Flux","Fog","Force","Fortune","Freedom","Garden","Ghost","Glass","Glutton","Gravity","Heart","Heartbeat","Hook","Horror","Hurricane","Icicle","Impulse","Island","Jewel","Judgment","Justice","Knockout","Kraken","Leopard","Mammoth","Medium","Meteor","Miracle","Mirror","Mist","Motion","Night","Nightmare","Octopus","Omen","Operation","Oracle","Panther","Phantom","Phase","Prison","Pulse","Punishment","Quake","Quicksand","Quill","Reflection","Regret","Requiem","Response","Rhythm","Riddle","Ride","River","Ruin","Serpent","Servant","Shade","Shadow","Shift","Shock","Signal","Snake","Snowflake","Sparkle","Spell","Split","Star","Stitch","Storm","Switch","Switcheroo","Thrill","Throne","Thunder","Tornado","Tower","Tremor","Trick","Twist","Twister","Typhoon","Vault","Volcano","Voyage","Wave","Wipeout","Wonder","Zephyr"];
	var nm2 = ["Boat","Bungee","Coaster","Coil","Depth","Diver","Drop","Edge","Expedition","Extreme","House","Hall","Loop","Manor","Mansion","Obelisk","Palace","Pass","Passage","Pendulum","Place","Plummet","Plunge","Rapids","Release","Ride","Rider","Shot","Slide","Spire","Supreme","Swing","Tower","Tumble","Wheel"];
	var nm3 = ["Acrobatics","Action","Adventure","Amazement","Autumn","Awe","Balance","Battle","Beginnings","Belief","Blood","Bones","Bravery","Bubbles","Candy","Chains","Chaos","Clarity","Clouds","Courage","Creatures","Cushions","Dance","Darkness","Death","Delight","Desire","Discovery","Doom","Dread","Dreams","Ecstacy","Eternity","Fascination","Fear","Feasts","Fire","Flame","Flukes","Fortune","Fun","Ghosts","Glass","Gluttony","Gold","Harmony","Hilarity","Horror","Ice","Impulses","Insanity","Insects","Jelly","Jokes","Juniors","Laughter","Liberty","Light","Liquid","Luck","Magic","Masks","Mayhem","Midnight","Mirrors","Motion","Nightmares","Paradise","Pillows","Pleasure","Quicksand","Rain","Reflections","Rhythm","Riddles","Scents","Science","Secrets","Shadows","Silliness","Silly","Smiles","Snow","Sparks","Speed","Spells","Spirits","Spring","Stars","Storms","Strings","Sugar","Summer","Surprises","Terror","Thrills","Thunder","Tunes","Twists","Uncertainty","Voices","Water","Webs","Whispers","Winter","Wishes","Wonders"];
	var nm4 = ["Abandoned","Abstract","Ancient","Bizarre","Blind","Broken","Charmed","Colossal","Daffy","Dark","Defiant","Demonic","Dynamic","Enchanted","Enchanting","Ethereal","Euphoric","Forsaken","Frozen","Grand","Grave","Grim","Hollow","Horrific","Hungry","Jumbo","Living","Lone","Lonely","Merciless","Merry","Monster","Monstrous"];
	var nm5 = ["The ",""];
	
	var br = "";
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.random() * nm2.length | 0;
		if(i < 2){
			rnd = Math.random() * nm1.length | 0;
			rnd3 = Math.random() * nm5.length | 0;
			names = nm5[rnd3] + nm1[rnd] + " " + nm2[rnd2];
			nm1.splice(rnd, 1);
		}else if(i < 4){
			rnd = Math.random() * nm1.length | 0;
			names = "The " + nm1[rnd];
			nm1.splice(rnd, 1);
		}else if(i < 6){
			rnd = Math.random() * nm4.length | 0;
			names = "The " + nm4[rnd] + " " + nm2[rnd2];
			nm4.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm3.length | 0;
			names = nm2[rnd2] + " of " + nm3[rnd];
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