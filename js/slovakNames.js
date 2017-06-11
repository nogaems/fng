
function nameGen(type){
	var nm1 = ["Ľuboš","Ľubomír","Šimon","Štefan","Žigmund","Adam","Aleš","Alexander","Alexej","Alojz","Andrej","Augustín","Aurel","Bartolomej","Benjamín ","Blažej","Bohumír","Bohumil","Bohuslav","Branislav","Branko","Bronislav","Ctirad","Cyril","Dávid","Dalibor","Dalimil","Daniel","Denis","Dionýz","Dominik","Drahoslav","Dušan","Eduard","Erik","Eugen","Filip","Gabriel","Gregor","Havel","Henrich","Imrich","Ivan","Ján","Július","Jakub","Janko","Jaroslav","Jonáš","Jozef","Juraj","Kajetán","Kamil","Karol","Kazimír","Klement","Koloman","Konrád","Kornel","Krištof","Ladislav","Lukáš","Marcel","Marek","Marián","Martin","Matúš","Matej","Maximilián","Metod","Michal","Mikuláš","Milan","Miloš","Miloslav","Mirek","Miroslav","Oldrich","Oliver","Ondrej","Patrik","Pavol","Peter","Radovan","René","Riško","Rišo","Richard","Robert","Roman","Samuel","Silvester","Slavomír","Stanislav","Tadeáš","Teodor","Tibor","Timotej","Tomáš","Václav","Vít","Valentín","Vavrinec","Vendelín","Viktor","Viliam","Vincent","Vladan","Vladimír","Vladislav","Vlado","Vojtech","Vratislav","Zdenko","Zdeno"];
	var nm2 = ["Štefánia","Žofia","Adriana","Agnesa","Alžbeta","Albína","Alena","Alexandra","Alica","Alojzia","Amália","Anastázia","Andrea","Angela","Angelika","Anna","Antónia","Apolena","Barbora","Beáta","Blanka","Božena","Braňka","Branislava","Bronislava","Cecília","Dagmar","Dana","Danica","Daniela","Danka","Darina","Denisa","Dominika","Dorota","Dušana","Edita","Elena","Eliška","Emília","Ema","Estera","Eulália","Eva","Gabriela","Gertrúda","Hana","Hedviga","Helena","Imriška","Iva","Ivana","Ivanka","Iveta","Ivka","Ivona","Júlia","Jana","Janka","Jarmila","Jaroslava","Jela","Jolana","Jozefína","Judita","Justína","Kamila","Katarína","Katka","Klára","Klaudia","Kristína","Lýdia","Ladislava","Lenka","Linda","Luba","Lubica","Lucia","Mária","Margita","Marianna","Marika","Markéta","Marta","Martina","Melánia","Michaela","Miroslava","Monika","Nadežda","Natália","Nela","Nikola","Nina","Olívia","Olga","Patka","Patrícia","Paulína","Petra","Petronela","Renáta","Romana","Sára","Silvia","Simona","Soňa","Sofia","Stanislava","Svetlana","Tamara","Tatiana","Terézia","Valéria","Valentína","Vanda","Vanesa","Veronika","Viktória","Vilma","Vladimíra","Zita","Zlata","Zlatica","Zorka","Zuza","Zuzana","Zuzanka","Zuzka"];
	var nm3 = ["Čížik","Čiernik","Čierny","Řezník","Šťastný","Široký","Bača","Baník","Bartoš","Biely","Biskup","Bosko","Chren","Chrobák","Cibuľka","Cuda","Dobrovodský","Doležal","Dolina","Hodža","Holič","Holub","Hornick","Hornik","Ján","Jahoda","Jankovic","Jelen","Kľúčiar","Kočiš","Kocur","Kolar","Koleno","Komár","Koreň","Kostra","Kováč","Kovac","Kráľ","Križ","Kuchár","Láska","Mäsiar","Malý","Maliar","Malina","Mečiar","Medvedík","Medved","Mlynár","Mokrý","Mráz","Nedved","Novák","Otčenáš","Pekár","Pokorny","Rybár","Skalicky","Sklenár","Slaný","Slavik","Smutný","Strnad","Suchý","Surový","Tesar","Tesarik","Tichý","Zima"];
	var nm4 = ["Čiliaká","Čiliaková","Šafařiková","Šafiřiká","Bartá","Bartková","Bellá","Bellová","Bláhá","Bláhová","Bottá","Bottoca","Chlebovcá","Chlebovcová","Cudová","Grgasá","Grgasová","Hodžová","Hrljacá","Hrljacová","Jánošíká","Jánošíková","Jilemničká","Jillemničková","Kočišová","Koleničká","Koleničková","Kollará","Kollarová","Kostrová","Kováčová","Kráľová","Lucáčá","Lucáčov'","Mišurá","Mišurová","Novomedská","Novomedsková","Orszaghá","Orszaghova","Paučulá","Paučuloá","Pivovarčá","Pivovarčová","Razusá","Razusová","Repká","Repková","Smreká","Smreková","Turošíká","Turošíkova","Urbaná","Urbanová","Vajanská","Vajanskvá","Záhorecá","Záhorecová"];
	

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.random() * nm2.length | 0;
			rnd2 = Math.random() * nm4.length | 0;
			names = nm2[rnd] + " " + nm4[rnd2];
			nm2.splice(rnd, 1);
			nm4.splice(rnd2, 1);
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm3.length | 0;
			names = nm1[rnd] + " " + nm3[rnd2];
			nm1.splice(rnd, 1);
			nm3.splice(rnd2, 1);
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