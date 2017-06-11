
function nameGen(){
	var nm1 = ["Achievement","Adventure","Alien","Amazing","Animal","Animaniac","Animatron","Animatronic","Arc","Astral","Awesome","Banter","Battle","Blissful","Blown Mind","Bountiful","Brave","Brilliant","Carefree","Carnival","Celebration","Change","Cheat Code","Classic","Cloud","Cloud Nine","Co-op","Connection","Creature","Critical","Critical Hit","Crown","Curtain","Dapper","Dark","Defiance","Defiant","Digital","Discovery","Dragon","Enchanted","Exalted","Exchange","Experience","Expert","Fantastic","Fantasy","Feast","Festival","Fiesta","Focus","Focused","Game","Game On","Gleeful","Glorious","Glory","Grand","Great","Highscore","Holiday","Humble","Illusion","Imagination","Impulse","Infinite","Infinity","Jamboree","Jewel","Jubilant","Jubilee","Jumbo","Juvenile","Level","Level Up","Little","Lost","Lucky","Magic","Mana","Mellow","Merry","Mind","Miracle","Mystery","Mythic","Natural Twenty","Nightowl","Nostalgia","Oddball","One Up","Original","Outcast","Parallel","Phantom","Phoenix","Playful","Playground","Plus One","Prestige","Prime","Pristine","Quaint","Radiant","Reality","Record","Revelation","Rhythm","Riddle","Secret","Sensation","Sidewalk","Small Change","Space","Space Station","Spirit","Summer","Surprise","Throne","Treasure","Treasure Trove","Trophy","VR","Velvet","Victorious","Victory","Virtual","Vision","Voyage","Whimsical","Wicked","Wild","Wilder","Winter","Wonder","XP"];
	var nm2 = ["Amuscore","Amusecade","Amusehall","Amusemania","Amusepolis","Avatarcade","Barcade","Barscore","Bazarcade","Bizarcade","Bliss Palace","Blisscore","Blisshall","Blissmania","Blisspalace","Blissplace","Blissplay","Blisspolis","Blisspot","Bull's Eyescore","Caesarcade","Capercade","Capolis","Cheerpolis","Cheerscore","Coinpalace","Coinscore","Coinstop","Comicade","Comiscore","Cougarcade","Embarcade","Excelsiscore","Exemplay","Felicicade","Felicipolis","Feliscore","Festicade","Festihall","Festiscore","Festocade","Festomania","Festopolis","Flyscore","Foolcade","Foolplay","Foolscore","Fubarcade","Funcade","Funcore","Funmania","Funpolis","Funscore","Funspot","Gamecade","Gamecore","Gamehall","Gamemania","Gameplace","Gamepolis","Gamescore","Gamespot","Gearmania","Gearplay","Gearscore","Gemcade","Gemplay","Guitarcade","Guyscore","Happicade","Happiscore","Happlay","Happycade","Happyscore","Jarcade","Jokecade","Jokepolis","Jokescore","Joycade","Joyhall","Joypalace","Joyplace","Joypolis","Joyscore","Jubicade","Jubihall","Jubilamania","Jubileecade","Jubileemania","Jubilopolis","Jubiscore","Kawaiiscore","Lunarcade","Merricade","Merripalace","Merriplace","Merriscore","Nostalcade","Nostalgicade","Ocularcade","Piescore","Pillarcade","Quarterpalace","Quarterscore","Recrecade","Relaxacade","Relaxcore","Relaxscore","Rethrone","Retrocade","Retrocity","Retrophy","Retropolis","Retroscore","Retrove","Skyscore","Solarcade","Sparcade","Standbyscore","Starcade","Stelarcade","Tokencade","Tokenstop","Toycade","Toymania","Toyplace","Toyscore","Toyspot","Tsarcade","Wifiscore","Wondercade","Wonderhall","Wonderplace","Wonderscore"];
	var nm3 = ["Arcade","Game Hall","Gaming Center","Game Center","Game Junction","Arcade","Arcade","Gamer Club","Gamer Center","Arcade","Arcade","Arcade"];

	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm3.length);
		if(i < 5){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd] + " " + nm3[rnd2];
			nm2.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = "The " + nm1[rnd] + " " + nm3[rnd2];
			nm1.splice(rnd, 1);
		}
		nm3.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}