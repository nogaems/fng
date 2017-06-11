function nameGen(){
	var nm1 = ["Ashes","Ace","Anarchy","Anger","Apparition","Arch","Ash","Aura","Band","Bandit","Banshee","Barbarian","Barrage","Beam","Beast","Behemoth","Bite","Blade","Blaze","Blight","Blow","Bolt","Bones","Boulder","Brass","Brute","Burn","Cast","Cavalier","Chain","Champ","Chance","Chaos","Cherub","Cloud","Crack","Critter","Crook","Crow","Crux","Daemon","Death","Demon","Design","Desire","Devil","Diablo","Dice","Dragon","Dragonfly","Dusk","Dust","Echo","Eclipse","Edge","End","Enigma","Fang","Fiend","Fire","Flame","Flint","Flow","Flux","Force","Fragment","Freak","Frost","Fury","Fuse","Gargoyle","Gem","Ghost","Giant","Glutton","Goliath","Grim","Guide","Hazard","Heart","Hellion","Hook","Horn","Horror","Hound","Ice","Imp","Impulse","Iron","Jackal","Jester","Jewel","Judge","Knife","Knight","Leviathan","Limbo","Mammoth","Maniac","Martyr","Mask","Merit","Mime","Mind","Mist","Monster","Motion","Myth","Naught","Needle","Night","Ogre","Omen","Oracle","Owl","Paladin","Paradox","Paragon","Pest","Phantom","Phoenix","Plasma","Purpose","Pyre","Quake","Quiver","Rain","Rat","Ray","Revenant","Riddle","Rime","Robin","Rogue","Ruse","Saint","Salt","Sand","Savage","Scale","Scout","Secret","Sentinel","Seraph","Serenity","Serpent","Shade","Shadow","Shift","Shock","Shockwave","Silver","Siren","Sky","Slip","Slither","Sliver","Sly","Snake","Snow","Song","Soul","Specter","Sphinx","Spider","Splinter","Sprite","Steel","Stitch","Storm","Summer","Surprise","Switch","Taint","Temper","Templar","Thunder","Titan","Toad","Touch","Trick","Twist","Umbra","Vamp","Varmint","Veil","Vermin","Villain","Viper","Virtue","Vision","Void","Vortex","Wave","Weasel","Whip","Whisper","Winter","Wraith","Zealot"];
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * 50);
		names = nm1[rnd] + "-" + rnd2;
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