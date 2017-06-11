var nm1 = ["","","","","d","g","h","k","m","n","r","s","sn","t","v","z"];
var nm2 = ["a","e","i","o","u"];
var nm3 = ["b","bl","d","dr","g","gg","gl","gn","gr","hz","hr","hl","hs","k","kk","kr","kl","kb","kd","l","ld","lb","lt","ll","lp","lg","p","pl","pp","r","rt","rp","rb","rk","t","tr","tl","v","vl","vn"];
var nm4 = ["","","","","","d","g","gs","k","ks","m","n","r","rn","s","ss","tt","v","x"];

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
		names = nMs;
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
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
	rnd4 = Math.random() * nm4.length | 0;
	if(i < 4){
		while(rnd < 4){
			rnd = Math.random() * nm1.length | 0;
		}
		while(rnd4 < 5 || nm4[rnd4] === nm1[rnd]){
			rnd4 = Math.random() * nm4.length | 0;
		}
		nMs = nm1[rnd] + nm2[rnd2] + nm4[rnd4];
	}else{
		rnd3 = Math.random() * nm3.length | 0;
		rnd5 = Math.random() * nm2.length | 0;
		if(rnd < 4){
			while(rnd4 < 5){
				rnd4 = Math.random() * nm4.length | 0;
			}
		}
		while(nm3[rnd3] === nm1[rnd] || nm3[rnd3] === nm4[rnd4]){
			rnd3 = Math.random() * nm3.length | 0;
		}
		nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd5] + nm4[rnd2];
	}
	
	testSwear(nMs);
}