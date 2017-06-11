var nm1 = ["ABC","Aeos","Algorithm","Amenity","Angel's","Anomaly","Apex","Aptitude","Art Archive","Avant-garde","Beauview","Blossoms","Book Mark","Booked","Bookworm","Calligraph","Capitol","Carpe Librum","Celestial","Central Park","Chapter","Chapter One","Charity","Chimera","Codex","Compendium","Cosmic","Courtesy","Crescent Moon","Crest","Crossroad","Crown","Curio","Curiosity","Data","Daydream","Desire","Discovery","Divine","Epiphany","Epitome","Equinox","Estate","Eternal","Evening Hour","Explorer","Figment","First Story","Forte","Freedom","Frontier","Gift's","Global","Globe","Grand","Grand Archive","Grand Duchess","Grand Isle","Grand Monastery","Grand Oak","Grand State","Grotto","Guardian's","Harborview","Harmony","Heirloom","Heritage","Holy","Idle Hour","Illusions","Imagine","Imperial","Infinity","Innovation","Inquiry","Insight","Institute","Jubilee","King's","Knight","Knowledge","Labyrinth","Legacy","Leisure","Lexicon","Liberty","Lullaby","Marvel","Memorial","Millennium","Miracle","Mirage","Mystery","National History","National Memorial","National Public","National University","Novel Idea","Obelisk","Oceanic","Open Book","Opus","Oracle","Page One","Paragon","Patrimony","Pinnacle","Pioneer","Plainfield","Prime","Prism","Probe","Prodigy","Public Scientific","Pursuit","Quest","Quietus","Rainbow","Reader's Garden","Repose","Requiem","Reticence","Revelation","Reverie","Rising Sun","Royal","Saturninity","Savant","Scholar's","Serenity","Solace","Solitude","Spectrum","Spring Harbor","Stellar","Summit","Supreme","Tempest","Temple","Titlewave","Tranquility","Treatise","Trove","Utopia","Vade Mecum","Valley","Virtue","Vision","Wonder","Zenith"];
var nm2 = ["Library","Bilbiotheca","Library","Library","Library","Library","Library","Library","Library","Library","Library","Atheneum"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + " " + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}