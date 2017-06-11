var nm1 = ["c","d","dh","j","jh","k","kh","m","n","r","v","z"];
var nm2 = ["a","e","i","o","u"];
var nm3 = ["d","dd","g","gl","hn","hl","hr","l","lg","lm","ld","ln","lz","m","mn","mr","n","nn","nd","nl","nr","nv","r","rl","rn","rv","rz","v","vn","z"];

var nm4 = ["","","","","","","","","b","bh","d","dh","f","fl","h","l","m","n","s","sh","vl","w","wh","y"];
var nm5 = ["a","e","o","u","a","e","o","u","i"];
var nm6 = ["d","dd","dr","gr","gl","hl","hn","l","lr","lt","lth","ml","nl","nth","nr","r","rn","rl","rr","s","sh","st","sl","sn","t","th","tr","thr","tl","thl"];
var nm7 = ["d","h","l","m","n","r"];
var nm8 = ["e","y","y","y","y","y","y"];

var nm9 = ["","","","b","bh","d","dh","j","g","l","m","n","p","r","s","v","z"];
var nm10 = ["a","u","a","u","a","u","e","o"];
var nm11 = ["b","d","g","gh","hl","hn","hm","hr","l","n","m","r","v"];
var nm12 = ["a","o","a","o","e","u"];
var nm13 = ["d","g","l","ll","ln","lm","lv","m","mn","n","ns","nz","r","rs","s","sn","x","z"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm9.length | 0;
		rnd2 = Math.random() * nm10.length | 0;
		rnd3 = Math.random() * nm11.length | 0;
		rnd4 = Math.random() * nm12.length | 0;
		rnd5 = Math.random() * nm13.length | 0;
		while(nm11[rnd3] === nm9[rnd] || nm11[rnd3] == nm13[rnd5]){
			rnd3 = Math.random() * nm11.length | 0;
		}
		nSr = nm9[rnd] + nm10[rnd2] + nm11[rnd3] + nm12[rnd4] + nm13[rnd5] + "ath";
		if(tp === 1){
			nameFem();
			while(nFm === ""){
				nameFem();
			}
			names = nFm + " " + nSr;
		}else{
			nameMas();
			while(nMs === ""){
				nameMas();
			}
			names = nMs + " " + nSr;
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

function nameFem(){
	rnd = Math.random() * nm4.length | 0;
	rnd2 = Math.random() * nm5.length | 0;
	rnd3 = Math.random() * nm6.length | 0;
	rnd4 = Math.random() * nm8.length | 0;
	while(nm6[rnd3] === nm4[rnd]){
		rnd3 = Math.random() * nm6.length | 0;
	}
	if(i < 5){
		nFm = nm4[rnd] + nm5[rnd2] + nm6[rnd3] + nm8[rnd4] + "n";
	}else{
		rnd5 = Math.random() * nm5.length | 0;
		rnd6 = Math.random() * nm7.length | 0;
		while(nm7[rnd6] === nm6[rnd3]){
			rnd6 = Math.random() * nm7.length | 0;
		}
		nFm = nm4[rnd] + nm5[rnd2] + nm6[rnd3] + nm5[rnd5] + nm7[rnd6] + nm8[rnd4] + "n";
	}
	testSwear(nFm);
}

function nameMas(){
	rnd = Math.random() * nm1.length | 0;
	rnd2 = Math.random() * nm2.length | 0;
	rnd3 = Math.random() * nm3.length | 0;
	while(nm1[rnd] === nm3[rnd3]){
		rnd3 = Math.random() * nm3.length | 0;
	}
	rnd4 = Math.random() * nm2.length | 0;
	nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd2] + "s";
	testSwear(nMs);
}