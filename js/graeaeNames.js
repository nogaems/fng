var nm1 = ["","","c","d","h","l","m","n","p","s","t","th","v","w"];
var nm2 = ["a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","ei","ae","ea"];
var nm3 = ["d","f","ff","h","l","ll","m","n","ny","r","rr","t","th","v","y"];
var nm4 = ["lph","lphr","lr","lm","ln","mphr","mn","mph","nh","nr","nph","phr","sh","sn","sl","sph","sphr","thr"];
var nm5 = ["o","o","o","o","o","o","ei","i","ae"];

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
	while(nm3[rnd3] === nm1[rnd]){
		rnd3 = Math.random() * nm3.length | 0;
	}
	if(i < 6){
		nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm5[rnd4];
	}else{	
		rnd6 = Math.random() * nm2.length | 0;
		rnd7 = Math.random() * nm4.length | 0;
		while(nm4[rnd7] === nm3[rnd3]){
			rnd7 = Math.random() * nm4.length | 0;
		}
		if(i < 8){
			nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd6] + nm4[rnd7] + nm5[rnd4];
		}else{
			nMs = nm1[rnd] + nm2[rnd6] + nm4[rnd7] + nm2[rnd2] + nm3[rnd3] + nm5[rnd4];
		}
	}
	testSwear(nMs);
}