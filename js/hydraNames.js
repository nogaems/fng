var nm1 = ["","","","","","ch","g","gh","j","jh","k","kh","kr","m","mr","mg","n","ng","nr","tr","v","z","zh","zr"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","au","ou","ua","ia","ai","ae"];
var nm3 = ["g","k","m","n","r","v","z","g","h","k","m","n","r","v","z","g","k","m","n","r","v","z","g","k","m","n","r","v","z","g","gg","k","kk","ll","m","mm","n","nn","r","ss","v","z","zz","ch","g","gz","gr","gn","gg","h","hj","hsh","hz","k","kk","kh","ll","m","mm","mz","n","ng","nn","nz","nk","ngr","r","rd","rg","rz","sh","ss","shg","shk","sk","ssh","ssk","sz","v","vh","z","zr","zsh","zg","zk","zz"];
var nm4 = ["","","","","","","","h","hs","hz","j","n","s","sh","z"];
var nm5 = ["g","k","m","n","r","v","z","g","k","m","n","r","v","z","g","k","m","n","r","v","z","g","k","m","n","r","v","z","g","gg","k","kk","ll","m","mm","n","nn","r","ss","v","z","zz"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		rnd4 = Math.floor(Math.random() * nm2.length);
		rnd5 = Math.floor(Math.random() * nm4.length);
		if(i < 4){
			if(rnd < 5){
				while(rnd5 < 7){
					rnd5 = Math.floor(Math.random() * nm4.length);
				}
			}
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
		}else if(i < 6){
			rnd6 = Math.floor(Math.random() * nm2.length);
			rnd7 = Math.floor(Math.random() * nm5.length);
			while(nm3[rnd3] === nm5[rnd7]){
				rnd7 = Math.floor(Math.random() * nm5.length);
			}
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd7] + nm2[rnd6] + nm4[rnd5];
		}else if(i < 8){
			rnd6 = Math.floor(Math.random() * nm2.length);
			rnd7 = Math.floor(Math.random() * nm5.length);
			while(nm3[rnd3] === nm5[rnd7]){
				rnd7 = Math.floor(Math.random() * nm5.length);
			}
			names = nm1[rnd] + nm2[rnd2] + nm5[rnd7] + nm2[rnd6] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
		}else{
			rnd6 = Math.floor(Math.random() * nm2.length);
			rnd7 = Math.floor(Math.random() * nm3.length);
			while(nm3[rnd3] === nm3[rnd7]){
				rnd7 = Math.floor(Math.random() * nm3.length);
			}
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd7] + nm2[rnd6] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
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