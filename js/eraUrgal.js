var nm1 = ["","","b","d","g","kh","k","r","sk","skg","t","y","v","z"];
var nm2 = ["a","e","o","u"];
var nm3 = ["b","br","bv","bgr","bdr","d","dv","dz","dzgr","dgr","gr","gn","gz","hgr","hr","lk","lv","r","rg","rd","rb","rv","rtv","rzhv","tv","tr","thb","tz","zg","zb","zr","ztr","zhgr"];
var nm4 = ["c","g","k","sz","shz","zh","z"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd4 = Math.floor(Math.random() * nm4.length);
		if(i < 3){
			names = nm1[rnd] + nm2[rnd2] + nm4[rnd4];
		}else if(i < 7){
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd5 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd5] + nm4[rnd4];
		}else{
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd5 = Math.floor(Math.random() * nm2.length);
			rnd6 = Math.floor(Math.random() * nm3.length);
			rnd7 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd5] + nm3[rnd6] + nm2[rnd7] + nm4[rnd4];
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