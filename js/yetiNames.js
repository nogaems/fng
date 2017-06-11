var nm1 = ["","","","","","b","ch","dz","dj","g","gy","h","j","k","ky","l","m","n","r","s","sz","sh","t","th","v","z"];
var nm2 = ["a","e","i","o","u","a","o","u"];
var nm3 = ["dd","h","k","l","ll","m","n","r","s","t","z","dd","h","k","kk","l","ll","lr","m","n","ng","nr","nz","r","rr","s","sh","sr","t","ts","vr","y","z"];
var nm4 = ["","","c","hn","hl","l","m","n","ng","r","rs","s","sh"];
var nm4b = ["h","k","l","ll","m","n","r","s","t","z"];

var nm5 = ["","","","","","f","gy","h","k","ky","l","m","n","ph","r","s","sh","th","w","y","z"];
var nm6 = ["a","e","i","o","u","a","e","i"];
var nm7 = ["b","f","g","h","k","l","ll","m","n","r","rr","s","t","w","z","b","f","g","gy","h","hn","hl","k","l","ll","m","n","ng","nn","r","rr","rl","ry","rs","s","sh","t","ty","th","w","z"];
var nm8 = ["","","","","","","","","","","","","","","","h","hn","l","m","n","ng","ph","s","sh","th","y"];
var nm9 = ["b","f","g","h","k","l","ll","m","n","r","rr","s","t","w","z"];

var nm10 = ["","","","","","","f","g","gy","h","k","ky","l","m","n","ph","r","s","sh","th","v","w","y","z"];
var nm11 = ["a","e","i","o","u","a"];
var nm12 = ["b","dd","g","h","k","kk","l","ll","m","n","nn","r","rr","s","t","w","y","z","b","dd","g","gy","h","hn","k","kk","l","ll","lr","m","n","ng","nn","nr","r","rr","ry","s","sh","sr","t","th","ts","vr","w","y","z"];
var nm13 = ["","","","","","","","","h","hl","hn","l","m","n","ng","ph","r","rs","s","sh","th"];
var nm14 = ["b","dd","g","h","k","kk","l","ll","m","n","nn","r","rr","s","t","w","y","z"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm5.length);
			rnd2 = Math.floor(Math.random() * nm6.length);
			rnd3 = Math.floor(Math.random() * nm7.length);
			rnd4 = Math.floor(Math.random() * nm6.length);
			rnd5 = Math.floor(Math.random() * nm8.length);
			if(i < 6){
				while(nm5[rnd] === nm7[rnd3]){
					rnd3 = Math.floor(Math.random() * nm7.length);
				}
				if(rnd < 5){
					while(rnd5 < 15 || nm7[rnd3] === nm8[rnd5]){
						rnd5 = Math.floor(Math.random() * nm8.length);
					}
				}
				names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm8[rnd5];
			}else if(i < 8){
				rnd6 = Math.floor(Math.random() * nm9.length);
				rnd7 = Math.floor(Math.random() * nm6.length);
				while(nm5[rnd] === nm7[rnd3]){
					rnd3 = Math.floor(Math.random() * nm7.length);
				}
				while(nm9[rnd6] === nm8[rnd5]){
					rnd5 = Math.floor(Math.random() * nm8.length);
				}
				while(nm9[rnd6] === nm7[rnd3]){
					rnd6 = Math.floor(Math.random() * nm9.length);
				}
				names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm9[rnd6] + nm6[rnd7] + nm8[rnd5];
			}else{
				rnd6 = Math.floor(Math.random() * nm9.length);
				rnd7 = Math.floor(Math.random() * nm6.length);
				while(nm5[rnd] === nm7[rnd3]){
					rnd3 = Math.floor(Math.random() * nm7.length);
				}
				while(nm7[rnd3] === nm8[rnd5]){
					rnd5 = Math.floor(Math.random() * nm8.length);
				}
				while(nm9[rnd6] === nm7[rnd3]){
					rnd6 = Math.floor(Math.random() * nm9.length);
				}
				names = nm5[rnd] + nm6[rnd2] + nm9[rnd6] + nm6[rnd7] + nm7[rnd3] + nm6[rnd4] + nm8[rnd5];
			}
		}else if(tp === 2){
			rnd = Math.floor(Math.random() * nm10.length);
			rnd2 = Math.floor(Math.random() * nm11.length);
			rnd3 = Math.floor(Math.random() * nm12.length);
			rnd4 = Math.floor(Math.random() * nm11.length);
			rnd5 = Math.floor(Math.random() * nm13.length);
			if(i < 6){
				while(nm10[rnd] === nm12[rnd3]){
					rnd3 = Math.floor(Math.random() * nm12.length);
				}
				if(rnd < 5){
					while(rnd5 < 15 || nm12[rnd3] === nm13[rnd5]){
						rnd5 = Math.floor(Math.random() * nm13.length);
					}
				}
				names = nm10[rnd] + nm11[rnd2] + nm12[rnd3] + nm11[rnd4] + nm13[rnd5];
			}else if(i < 8){
				rnd6 = Math.floor(Math.random() * nm14.length);
				rnd7 = Math.floor(Math.random() * nm11.length);
				while(nm10[rnd] === nm12[rnd3]){
					rnd3 = Math.floor(Math.random() * nm12.length);
				}
				while(nm14[rnd6] === nm13[rnd5]){
					rnd5 = Math.floor(Math.random() * nm13.length);
				}
				while(nm14[rnd6] === nm12[rnd3]){
					rnd6 = Math.floor(Math.random() * nm14.length);
				}
				names = nm10[rnd] + nm11[rnd2] + nm12[rnd3] + nm11[rnd4] + nm14[rnd6] + nm11[rnd7] + nm13[rnd5];
			}else{
				rnd6 = Math.floor(Math.random() * nm14.length);
				rnd7 = Math.floor(Math.random() * nm11.length);
				while(nm10[rnd] === nm12[rnd3]){
					rnd3 = Math.floor(Math.random() * nm12.length);
				}
				while(nm14[rnd6] === nm13[rnd5]){
					rnd5 = Math.floor(Math.random() * nm13.length);
				}
				while(nm14[rnd6] === nm12[rnd3]){
					rnd6 = Math.floor(Math.random() * nm14.length);
				}
				names = nm10[rnd] + nm11[rnd2] + nm14[rnd6] + nm11[rnd7] + nm12[rnd3] + nm11[rnd4] + nm13[rnd5];
			}
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm2.length);
			rnd5 = Math.floor(Math.random() * nm4.length);
			if(i < 5){
				while(nm1[rnd] === nm3[rnd3]){
					rnd3 = Math.floor(Math.random() * nm3.length);
				}
				if(rnd < 5){
					while(rnd5 < 2 || nm3[rnd3] === nm4[rnd5]){
						rnd5 = Math.floor(Math.random() * nm4.length);
					}
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
			}else if(i < 8){
				rnd6 = Math.floor(Math.random() * nm4b.length);
				rnd7 = Math.floor(Math.random() * nm2.length);
				while(nm1[rnd] === nm3[rnd3]){
					rnd3 = Math.floor(Math.random() * nm3.length);
				}
				while(nm4b[rnd6] === nm4[rnd5]){
					rnd5 = Math.floor(Math.random() * nm4.length);
				}
				while(nm4b[rnd6] === nm3[rnd3]){
					rnd6 = Math.floor(Math.random() * nm4b.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4b[rnd6] + nm2[rnd7] + nm4[rnd5];
			}else{
				rnd6 = Math.floor(Math.random() * nm4b.length);
				rnd7 = Math.floor(Math.random() * nm2.length);
				while(nm1[rnd] === nm3[rnd3]){
					rnd3 = Math.floor(Math.random() * nm3.length);
				}
				while(nm3[rnd3] === nm4[rnd5]){
					rnd5 = Math.floor(Math.random() * nm4.length);
				}
				while(nm4b[rnd6] === nm3[rnd3]){
					rnd6 = Math.floor(Math.random() * nm4b.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm4b[rnd6] + nm2[rnd7] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
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