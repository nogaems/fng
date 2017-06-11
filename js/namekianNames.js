var names1 = ["Abut","Accordi","Alsetto","Amisen","Andoli","Andolin","Armon","Armoni","Armonic","Arp","Astropo","Axopho","Azoo","Balalai","Banji","Banjo","Barito","Baritone","Base","Bass","Bassoo","Bassoon","Batu","Carina","Cello","Clarin","Cordi","Cordio","Cordion","Didger","Didgeri","Dolin","Eleluku","Escar","Escargo","Fiddel","Fiddle","Fidel","Flute","Gastro","Gastropo","Geridoo","Guitar","Guitara","Guls","Guytar","Harmo","Harmon","Harp","Horn","Horne","Iolin","Iren","Istle","Itar","Kazoo","Keyta","Keytar","Kotai","Kulele","Lalaika","Larinet","Lians","Lire","Lophone","Lug","Lusc","Lute","Lyre","Mando","Mandolin","Mollus","Mollusc","Murd","Neris","Oboe","Oboo","Ocari","Ocarin","Okiat","Ollusc","Oozak","Oragan","Organ","Organa","Orn","Piani","Picco","Piyano","Prano","Ratis","Riangle","Rombon","Rombone","Rumpet","Saxo","Saxofo","Scargo","Scargot","Senshami","Shami","Sirren","Sitar","Snai","Snayle","Sopra","Sopran","Sulug","Taiko","Tooba","Triango","Trombo","Trombon","Tropod","Trump","Trumpe","Tuba","Ukule","Ukulel","Ukulele","Viol","Violin","Vuvu","Vuzela","Whist","Xophone","Xylo","Xylofo","Zooka"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		names = names1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}