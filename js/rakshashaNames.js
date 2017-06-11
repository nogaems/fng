var nm1 = ["","","","","","b","bg","br","c","d","dh","g","h","j","k","ks","m","n","p","pr","r","s","sh","t","v","y"];
var nm2 = ["a","i","e","o","u","a","a","a","u","u"];
var nm3 = ["b","bh","bhr","c","dr","gn","h","hm","j","jn","k","kr","l","lg","lm","m","n","nd","r","rg","rm","rp","s","shm","sk","sv","t","th","tt","v"];
var nm4 = ["b","bh","d","g","h","k","n","ng","ngh","pt","rh","rm","rt","sh","shr","sth","sv","t","thy","ty","v","vy","y"];
var nm5 = ["","","d","n","nt","r","s","sh","t","y"];

var nm6 = ["","","","","","","b","bh","c","d","dh","g","h","k","kh","l","m","n","p","pr","r","s","sh","v","y"];
var nm7 = ["a","e","i","o","u","a","e","i","u","a","a","a","a","i","i"];
var nm8 = ["b","bh","bj","d","dh","dhr","dr","dv","h","j","ks","l","ly","m","mr","n","nd","ng","nt","p","pt","rg","rk","rm","ry","s","sh","sm","t","th","tr","tt","v","vh"];
var nm9 = ["bh","c","cy","d","dh","dr","dv","j","k","ks","l","ly","m","mb","n","nd","ndh","ng","nt","p","pt","r","rg","rm","s","sh","sm","sn","t","th","tr","ts","tt","v","y"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
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
	rnd = Math.random() * nm6.length | 0;
	rnd2 = Math.random() * nm7.length | 0;
	rnd3 = Math.random() * nm8.length | 0;
	rnd4 = Math.random() * nm7.length | 0;
	if(i < 4){
		nMs = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4];
	}else{
		rnd6 = Math.random() * nm7.length | 0;
		rnd7 = Math.random() * nm9.length | 0;
		while(nm9[rnd7] === nm8[rnd3]){
			rnd7 = Math.random() * nm9.length | 0;
		}
		if(i < 8){
			nMs = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd7] + nm7[rnd6];
		}else{
			rnd8 = Math.random() * nm7.length | 0;
			rnd9 = Math.random() * nm9.length | 0;
			while(nm4[rnd7] === nm4[rnd9]){
				rnd9 = Math.random() * nm4.length | 0;
			}
			nMs = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd7] + nm7[rnd6] + nm9[rnd9] + nm7[rnd8];
		}
	}
	testSwear(nMs);
}
function nameMas(){
	rnd = Math.random() * nm1.length | 0;
	rnd2 = Math.random() * nm2.length | 0;
	rnd3 = Math.random() * nm3.length | 0;
	rnd4 = Math.random() * nm2.length | 0;
	rnd5 = Math.random() * nm5.length | 0;
	while(nm3[rnd3] === nm1[rnd] || nm3[rnd3] === nm5[rnd5]){
		rnd3 = Math.random() * nm3.length | 0;
	}
	if(i < 4){
		nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
	}else{
		rnd6 = Math.random() * nm2.length | 0;
		rnd7 = Math.random() * nm4.length | 0;
		while(nm4[rnd7] === nm3[rnd3] || nm4[rnd7] === nm5[rnd5]){
			rnd7 = Math.random() * nm4.length | 0;
		}
		if(i < 8){
			nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd7] + nm2[rnd6] + nm5[rnd5];
		}else{
			rnd8 = Math.random() * nm2.length | 0;
			rnd9 = Math.random() * nm4.length | 0;
			while(nm4[rnd7] === nm4[rnd9] || nm4[rnd9] === nm5[rnd5]){
				rnd9 = Math.random() * nm4.length | 0;
			}
			nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd7] + nm2[rnd6] + nm4[rnd9] + nm2[rnd8] + nm5[rnd5];
		}
	}
	testSwear(nMs);
}