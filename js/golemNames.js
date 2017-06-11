var nm1 = ["b","br","bh","d","dr","dh","g","gr","gh","kh","r","rh","v","z"];
var nm2 = ["a","e","o","u","a","o","u","a","e","o","u","a","o","u","a","e","o","u","a","o","u","aa","au"];
var nm3 = ["b","bb","br","d","dd","dl","dr","fl","g","gg","gn","gm","gl","ggl","gv","gz","k","kk","kl","kv","l","ll","lg","lgr","lv","lb","ld","ldr","ng","nk","rb","rd","rg","zg","zzg","zzl","zl"];
var nm4 = ["","","","","c","d","hm","hk","hn","k","m","mm","n","nn","r"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm4.length);
		if(i < 5){
			while(rnd3 < 4){
				rnd3 = Math.floor(Math.random() * nm4.length);
			}
			names = nm1[rnd] + nm2[rnd2] + nm4[rnd3];
		}else{
			rnd4 = Math.floor(Math.random() * nm2.length);
			rnd5 = Math.floor(Math.random() * nm3.length);
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd5] + nm2[rnd4] + nm4[rnd3];
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