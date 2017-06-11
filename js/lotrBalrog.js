var nm1 = ["b","bh","d","dh","g","h","kh","n","r","v","z"];
var nm2 = ["a","o","u","a","o","u","a","o","u","e","i"];
var nm3 = ["br","bn","dh","dr","dhr","gn","gr","gd","gz","kn","kg","kv","kz","ld","lg","lm","ln","lv","lz","mz","mg","md","nz","ng","nd","thr","thm","tr","zc","zg","zk","zz"];
var nm4 = ["b","d","k","l","m","n","t","v","z"];
var nm5 = ["c","d","g","k","l","n","r"];

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
		rnd5 = Math.floor(Math.random() * nm5.length);
		if(i < 6){
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
		}else{
			rnd6 = Math.floor(Math.random() * nm4.length);
			rnd7 = Math.floor(Math.random() * nm2.length);
			if(i < 8){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
			}else{
				names = nm1[rnd] + nm2[rnd2] + nm4[rnd6] + nm2[rnd7] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
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