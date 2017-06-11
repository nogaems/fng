var nm1 = ["","","","","b","br","cr","d","dr","g","gr","j","k","kr","m","n","r","v","w","z"];
var nm2 = ["a","i","o","u"];
var nm3 = ["dg","dz","dr","g","gd","gg","gh","gk","gr","gz","hg","hz","hzr","hrz","hr","k","kd","kg","kz","kr","l","ld","lz","lr","ldr","lgr","m","mg","mh","mgr","mz","mzr","mdr","md","nd","ndr","nz","nzr","ng","r","rb","rrz","rg","rgh","rz","rzr","rk","rl","t","tg","tk","tr","tgr","tz","tzr","z","zh","zn"];
var nm4 = ["c","d","g","k","r","t","z"];
var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		rnd4 = Math.floor(Math.random() * nm2.length);
		rnd5 = Math.floor(Math.random() * nm4.length);
		names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}