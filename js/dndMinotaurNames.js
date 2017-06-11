var nmFF = ["Aam","Ane","Are","Ase","Duu","Em","Enti","Este","Fen","Hene","Hes","Hila","Hine","Ias","Ire","Ki","Kia","Kuo","Laan","Line","Loo","Muu","Nan","Nea","Neo","Noo","Nuo","Oen","Oes","Raas","Ras","Sees","Seo","Sina","Tee","Tes","Tia","Tina","Uova","Weo"];
var nmFL = ["dra","fin","kane","kea","la","las","len","lin","lo","mas","me","mi","min","na","nan","nas","nim","nu","pen","pe","ra","ren","res","rin","ris","ru","sen","sia","ta","ter","tin","tra","tred","tri","trin","tris","ven","vena","vera","vin"];
var nmMF = ["Ar","Are","Aste","Bjor","Car","Cod","Da","Djar","Djun","Doen","Dor","Dur","Foos","Gar","Goe","Gra","Gran","Gun","Hun","Ja","Jar","Kar","Kin","Kir","Koo","Koor","Krum","Kur","Man","Min","Mir","Noo","Pod","Rak","Te","Toon","Trak","Tur","Zam","Zun"];
var nmML = ["ban","baran","bur","dak","daran","dor","fajar","faruk","furan","gajan","garak","gur","jar","kan","kar","karat","kun","kurat","kus","manuk","maruk","nark","narun","paran","raduk","rak","rakar","ranak","rapak","ras","rat","rios","ron","rus","rut","tagar","taruk","toron","turok","tus"];
var nmSF = ["Agile","Bear","Bold","Boulder","Brave","Bright","Fearless","Fist","Glory","Goblin","Great","Heavy","Honor","Iron","Jagged","Keen","Nimble","Orc","Rock","Rugged","Sharp","Silent","Single","Steady","Steel","Stone","Storm","Stout","Strong","Swift","Thick","Thunder","Tough","Truth","Valiant","Vigil","Wolf"];
var nmSL = ["bane","body","eye","fighter","fist","fury","hand","heart","hide","hoof","horn","horns","hunter","leader","mind","pelt","roar","runner","skin","skull","slash","slayer","speaker","step","striker","vigor","walker","warrior"];

function nameGen(type){
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nmSF.length);
		rnd2 = Math.floor(Math.random() * nmSL.length);
		nSr = nmSF[rnd] + nmSL[rnd2];
		if(tp === 1){
			nameFem();
			while(nMs === ""){
				nameFem();
			}
		}else{
			nameMas();
			while(nMs === ""){
				nameMas();
			}
		}
		nMs = nMs + " " + nSr;
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(nMs));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}

function nameFem(){
	rnd = Math.floor(Math.random() * nmFF.length);
	rnd2 = Math.floor(Math.random() * nmFL.length);
	nMs = nmFF[rnd] + nmFL[rnd2];
	testSwear(nMs);
}

function nameMas(){
	if(i < 5){
		rnd = Math.floor(Math.random() * nmFF.length);
		rnd2 = Math.floor(Math.random() * nmFL.length);
		nMs = nmFF[rnd] + nmFL[rnd2];
	}else{
		rnd = Math.floor(Math.random() * nmMF.length);
		rnd2 = Math.floor(Math.random() * nmML.length);
		nMs = nmMF[rnd] + nmML[rnd2];
	}
	testSwear(nMs);
}