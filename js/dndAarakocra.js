var nm1 = ["","","","","","c","cl","cr","d","g","gr","h","k","kh","kl","kr","q","qh","ql","qr","r","rh","s","y","z"];
var nm2 = ["a","e","i","u","a","e","i","u","a","e","i","u","a","e","i","u","a","e","i","u","a","e","i","u","a","e","i","u","ae","aia","ee","oo","ou","ua","uie"];
var nm3 = ["c","cc","k","kk","l","ll","q","r","rr"];
var nm4 = ["a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","aa","ea","ee","ia","ie"];
var nm5 = ["","","","","c","ck","d","f","g","hk","k","l","r","rr","rc","rk","rrk","s","ss"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
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
	rnd3 = Math.random() * nm5.length | 0;
	if(i < 5){
		while(nm1[rnd] === nm3[rnd3]){
			rnd3 = Math.random() * nm5.length | 0;
		}
		nMs = nm1[rnd] + nm2[rnd2] + nm5[rnd3];
	}else{
		rnd4 = Math.random() * nm3.length | 0;
		rnd5 = Math.random() * nm4.length | 0;
		nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm4[rnd5] + nm5[rnd3];
	}
	testSwear(nMs);
}