var nm1 = ["","","","","","b","ch","d","g","gh","h","j","k","kh","m","n","r","sh","t","v","y","z"];
var nm2 = ["a","a","a","e","i","u","u","a","a","a","e","i","u","u","a","a","a","e","i","u","u","a","a","a","e","i","u","u","ia","ou","oo","ee"];
var nm3 = ["fr","hk","hm","hr","kb","khg","kr","lt","lv","m","n","pr","r","rh","rkh","rm","rr","rsh","rt","ry","rz","sh","shk","t","v","vg","z","zy"];
var nm4 = ["b","dd","dv","dy","gm","gn","j","khz","lf","ll","md","nb","nd","ndy","nsh","r","rb","rd","rt","rz","s","shy","v","y","zh","zm"];
var nm5 = ["","","","","","","b","d","hr","k","kh","n","nd","r","rd","rz","sh","shk","v","z","zl"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0;
		rnd3 = Math.random() * nm5.length | 0;
		while(nm1[rnd] === nm5[rnd3]){
			rnd3 = Math.random() * nm5.length | 0;
		}
		if(i < 3){
			while(rnd < 5){
				rnd = Math.random() * nm1.length | 0;
			}
			while(rnd3 < 6){
				rnd3 = Math.random() * nm5.length | 0;
			}
			names = nm1[rnd] + nm2[rnd2] + nm5[rnd3];
		}else{
			rnd4 = Math.random() * nm3.length | 0;
			rnd5 = Math.random() * nm2.length | 0;
			while(nm3[rnd4] === nm5[rnd3]){
				rnd4 = Math.random() * nm3.length | 0;
			}
			if(i < 7){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm2[rnd5] + nm5[rnd3];
			}else{
				rnd6 = Math.random() * nm4.length | 0;
				rnd7 = Math.random() * nm2.length | 0;
				while(nm4[rnd6] === nm5[rnd3]){
					rnd6 = Math.random() * nm5.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm2[rnd5] + nm4[rnd6] + nm2[rnd7] + nm5[rnd3];
			}
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