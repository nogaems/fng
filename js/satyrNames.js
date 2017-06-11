var nm1 = ["","","","br","c","ch","cr","cl","d","dr","dh","f","g","gr","gh","gl","gn","h","j","k","kr","kn","m","n","pr","p","q","r","rh","s","sh","st","str","sn","sm","t","tr","v","vr","wr","x","xh","z","zr","zh","c","d","f","g","j","j","k","m","n","p","q","r","s","t","v","x","z"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","y","y","ai","ae","au","aa","ea","eo","ee","ia","ie","io"];
var nm3 = ["b","c","d","f","g","h","k","l","m","n","p","q","r","s","t","v","x","z"];
var nm4 = ["","","","","","","","","","b","c","d","f","g","h","k","l","m","n","p","r","s","t","w","x","z"];
var nm5 = ["c","ck","g","h","k","l","m","n","q","r","s","sh","t","th","x","z"];
var nm6 = ["e","i","u","a","o","y","ia","ea","ae"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		if(tp === 1){
			if(i < 5){
				rnd4 = Math.floor(Math.random() * nm6.length);
				while(rnd < 3){
					rnd = Math.floor(Math.random() * nm1.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm6[rnd4];
			}else{
				rnd4 = Math.floor(Math.random() * nm4.length);
				rnd5 = Math.floor(Math.random() * nm2.length);
				rnd6 = Math.floor(Math.random() * nm5.length);
				rnd7 = Math.floor(Math.random() * nm6.length);
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm2[rnd5] + nm5[rnd6] + nm6[rnd7];
			}
		}else{
			if(i < 5){
				while(rnd < 3){
					rnd = Math.floor(Math.random() * nm1.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3];
			}else{
				rnd4 = Math.floor(Math.random() * nm4.length);
				rnd5 = Math.floor(Math.random() * nm2.length);
				rnd6 = Math.floor(Math.random() * nm5.length);
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm2[rnd5] + nm5[rnd6];
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