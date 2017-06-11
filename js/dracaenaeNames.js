var nm1 = ["","","","","","c","d","dh","dr","g","gh","gr","l","ll","m","mn","n","p","ph","phr","s","sh","st","sth","sc","t","th","thr","v","z","zh"];
var nm2 = ["a","e","i","y","a","e","i","y","a","e","i","y","a","e","i","y","a","e","i","y","a","e","i","y","a","e","i","y","ui","oe","ia","ae","ea","eo","ie"];
var nm3 = ["b","ch","d","dd","dh","dn","f","ff","fr","fl","l","ll","lm","ln","lr","m","mp","mb","ml","mn","mr","n","nt","nz","ns","nsh","p","ph","phr","phn","phl","r","rr","rl","rn","rm","s","ss","sh","shr","st","str","sth","t","th","tt","thr","tr","ts","v"];
var nm4 = ["b","d","f","l","m","n","p","r","s","t","v"];
var nm5 = ["a","e","i","o"];
var nm6 = ["","","","","","","","","","","","","","","","f","h","n","ph","s","s","sh","sh","th"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		nameMas();
		while(nMs === ""){
			nameMas();
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

function nameMas(){
	rnd = Math.random() * nm1.length | 0;
	rnd2 = Math.random() * nm2.length | 0;
	rnd3 = Math.random() * nm3.length | 0;
	rnd4 = Math.random() * nm5.length | 0;
	rnd5 = Math.random() * nm6.length | 0;
	while(nm3[rnd3] === nm1[rnd] || nm3[rnd3] === nm6[rnd5]){
		rnd3 = Math.random() * nm3.length | 0;
	}
	if(i < 6){
		nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm5[rnd4] + nm6[rnd5];
	}else{
		rnd6 = Math.random() * nm4.length | 0;
		rnd7 = Math.random() * nm2.length | 0;
		while(nm4[rnd6] === nm3[rnd3] || nm4[rnd6] === nm6[rnd5]){
			rnd6 = Math.random() * nm4.length | 0;
		}
		nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm5[rnd4] + nm4[rnd6] + nm2[rnd7] + nm6[rnd5];
	}
	testSwear(nMs);
}