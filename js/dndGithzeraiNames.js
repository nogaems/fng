var nm1 = ["Am","Ar","Ara","Aza","Bar","Bra","Bru","Da","Dar","Dor","Dra","Dro","Du","Fa","Far","Fer","Gra","Gran","Gre","Gro","Gru","Hu","Ka","Kar","Kha","Kra","Kro","Ma","Mu","Na","Nar","Nu","Ra","Ran","Rin","Ru","Sha","Shra","Sra","Zra"];
var nm2 = ["d","dak","gh","k","kahr","kar","khar","kk","lag","llak","mag","mak","nag","rag","rak","ram","rath","rek","rg","rm","rth","ruk","th","tig","zag","zak","zar","zeg","zirg","zth"];
var nm3 = ["Ad","Alm","Arw","Ash","Dah","Dhar","Dolm","Dran","Ell","Erzh","Esz","Ezh","Grel","Halm","Han","Harn","Heln","Ihr","Iln","Imm","Iz","Kan","Kharm","Khaz","Krez","Laz","Lez","Lhash","Magd","Marm","Nagr","Nah","Nalm","Rasz","Rez","Sham","Sharm","Shund","Um","Uw"];
var nm4 = ["a","ah","aka","al","arah","arin","aya","ayah","eah","eka","el","ela","elna","elya","elzal","ena","enah","era","erah","eya","ihn","ila","ilzin","in","ina","ira","iza","mina","ya","yara"];

function nameGen(type){
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
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
	rnd = Math.floor(Math.random() * nm3.length);
	rnd2 = Math.floor(Math.random() * nm4.length);
	nMs = nm3[rnd] + nm4[rnd2];
	testSwear(nMs);
}

function nameMas(){
	rnd = Math.floor(Math.random() * nm1.length);
	rnd2 = Math.floor(Math.random() * nm2.length);
	nMs = nm1[rnd] + nm2[rnd2];
	testSwear(nMs);
}