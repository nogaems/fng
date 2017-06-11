var nm1 = ["f","s","ts","f","s","h","k","h","k","kx","l","m","n","l","m","n","ng","p","p","px","r","t","r","t","tx","v","w","y","z","v","w","y","z","'","'","","","","","","","","","","","","","","","","",""];
var nm2 = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u",,"ä","e","i","ì","o","u","aw","ay","ew","ey"];
var nm3 = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u",,"a","ä","e","i","ì","o","u","aw","ay","ew","ey","rr","ll"];
var nmEnd = ["k","k","kx","l","m","n","l","m","n","ng","p","p","px","r","t","r","t","tx"];
var nmCl = ["","","","","","","","","","","","","","","","","","","","p","t","k","p","t","k","px","tx","kx","m","n","m","n","ng","r","l","w","y","r","l","w","y"];
var nm5 = [];

var nm6 = [];
var nm7 = [];
var nm8 = [];
var nm9 = [];
var nm10 = [];

var nm11 = [];
var nm12 = [];
var nm13 = [];
var nm14 = [];
var nm15 = [];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		names = "";
		if(tp === 1){
			gEnd = "'ite";
		}else{
			gEnd = "'itan";
		}
		rndFn = Math.random() * 2 | 0 + 2;
		rndCn = Math.random() * 2 | 0 + 2;
		rndSn = Math.random() * 2 | 0 + 2;
		for(j = 0; j < rndFn; j++){
			rnd = Math.random() * nm1.length | 0;
			if(rnd < 5){
				rnd2 = Math.random() * nmCl.length | 0;
				while(nmCl[rnd2] === nm1[rnd]){
					rnd2 = Math.random() * nmCl.length | 0;
				}
			}else{
				rnd2 = 0;
			}			
			rndEnd = Math.random() * 3 | 0;
			rndDv = Math.random() * 4 | 0;
			if(rndEnd === 1){
				nm2a = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey"];
				nmEnd = ["k","kx","l","m","n","ng","p","px","r","t","tx"];
				rnd4 = Math.random() * nmEnd.length | 0;
				while(nmEnd[rnd4] === nm1[rnd]){
					rnd4 = Math.random() * nmEnd.length | 0;
				}
			}else{
				if(nm1[rnd] === ""){
					nm2a = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey"];
				}else{
					nm2a = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey","rr","ll"];
				}
				nmEnd = [""];
				rnd4 = 0;
			}
			if(rndDv === 1){
				nm2 = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey"];
				rnd5 = Math.random() * nm2.length | 0;
			}else{
				nm2 = [""];
				rnd5 = 0;
			}
			rnd3 = Math.random() * nm2a.length | 0;
			names = names + nm1[rnd] + nmCl[rnd2] + nm2a[rnd3] + nm2[rnd5] + nmEnd[rnd4];
		}
		names = names + " te ";
		for(k = 0; k < rndCn; k++){
			rnd = Math.random() * nm1.length | 0;
			if(rnd < 5){
				rnd2 = Math.random() * nmCl.length | 0;
				while(nmCl[rnd2] === nm1[rnd]){
					rnd2 = Math.random() * nmCl.length | 0;
				}
			}else{
				rnd2 = 0;
			}			
			rndEnd = Math.random() * 3 | 0;
			rndDv = Math.random() * 4 | 0;
			if(rndEnd === 1){
				nm2a = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey"];
				nmEnd = ["k","kx","l","m","n","ng","p","px","r","t","tx"];
				rnd4 = Math.random() * nmEnd.length | 0;
				rnd4 = Math.random() * nmEnd.length | 0;
				while(nmEnd[rnd4] === nm1[rnd]){
					rnd4 = Math.random() * nmEnd.length | 0;
				}
			}else{
				if(nm1[rnd] === ""){
					nm2a = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey"];
				}else{
					nm2a = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey","rr","ll"];
				}
				nmEnd = [""];
				rnd4 = 0;
			}
			if(rndDv === 1){
				nm2 = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey"];
				rnd5 = Math.random() * nm2.length | 0;
			}else{
				nm2 = [""];
				rnd5 = 0;
			}
			rnd3 = Math.random() * nm2a.length | 0;
			names = names + nm1[rnd] + nmCl[rnd2] + nm2a[rnd3] + nm2[rnd5] + nmEnd[rnd4];
		}
		names = names + " ";
		for(h = 0; h < rndSn; h++){
			rnd = Math.random() * nm1.length | 0;
			if(rnd < 5){
				rnd2 = Math.random() * nmCl.length | 0;
				while(nmCl[rnd2] === nm1[rnd]){
					rnd2 = Math.random() * nmCl.length | 0;
				}
			}else{
				rnd2 = 0;
			}			
			rndEnd = Math.random() * 3 | 0;
			rndDv = Math.random() * 4 | 0;
			if(rndEnd === 1){
				nm2a = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey"];
				nmEnd = ["k","kx","l","m","n","ng","p","px","r","t","tx"];
				rnd4 = Math.random() * nmEnd.length | 0;
				rnd4 = Math.random() * nmEnd.length | 0;
				while(nmEnd[rnd4] === nm1[rnd]){
					rnd4 = Math.random() * nmEnd.length | 0;
				}
			}else{
				if(nm1[rnd] === ""){
					nm2a = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey"];
				}else{
					nm2a = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey","rr","ll"];
				}
				nmEnd = [""];
				rnd4 = 0;
			}
			if(rndDv === 1){
				nm2 = ["a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","a","ä","e","i","ì","o","u","aw","ay","ew","ey"];
				rnd5 = Math.random() * nm2.length | 0;
			}else{
				nm2 = [""];
				rnd5 = 0;
			}
			rnd3 = Math.random() * nm2a.length | 0;
			names = names + nm1[rnd] + nmCl[rnd2] + nm2a[rnd3] + nm2[rnd5] + nmEnd[rnd4];
		}
		names = names + gEnd;
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}