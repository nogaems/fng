var nm1 = ["","","","","ch","g","j","k","kh","m","n","ph","t","v","z"];
var nm2 = ["a","e","i","o","u","a","a","a","u","u","u","o","o","a","e","i","o","u","a","a","a","u","u","u","o","o","a","e","i","o","u","a","a","a","u","u","u","o","o","a","e","i","o","u","a","a","a","u","u","u","o","o","a","e","i","o","u","a","a","a","u","u","u","o","o","au","ou","uu","oo","aa","ao","ai"];
var nm3 = ["br","ch","cr","d","dr","g","gg","ggr","gr","gz","k","kk","kkr","kkz","kr","l","lg","lgh","lk","lr","lt","lz","mk","mkh","nk","nkh","nr","nz","r","rk","rkh","rq","rrg","rrk","sh","shr","shz","sz","xn","xr","xx","xxr","z","zz"];
var nm4 = ["d","dd","dr","g","gg","gn","gr","hm","hn","hr","hz","k","kk","kn","kr","kv","kx","kz","lg","lz","m","mh","mm","n","nd","ng","nn","r","rh","rl","rm","rn","rr","s","sh","shz","ss","sz","z","zh","zk","zq","zz"];
var nm5 = ["d","k","r","s","ss","th","x","z"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0;
		rnd3 = Math.random() * nm3.length | 0;
		while(nm1[rnd] === nm3[rnd3]){
			rnd3 = Math.random() * nm3.length | 0;
		}
		rnd4 = Math.random() * nm2.length | 0;
		rnd5 = Math.random() * nm5.length | 0;
		while(nm5[rnd5] === nm3[rnd3]){
			rnd5 = Math.random() * nm5.length | 0;
		}
		if(i < 3){
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
		}else if(i < 6){
			rnd6 = Math.random() * nm4.length | 0;
			while(nm4[rnd6] === nm5[rnd5] || nm4[rnd6] === nm3[rnd3]){
				rnd6 = Math.random() * nm4.length | 0;
			}
			rnd7 = Math.random() * nm2.length | 0;
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
		}else{
			rnd6 = Math.random() * nm1.length | 0;
			rnd7 = Math.random() * nm2.length | 0;
			rnd8 = Math.random() * nm5.length | 0;
			if(i < 8){
				names = nm1[rnd6] + nm2[rnd7] + nm5[rnd8] + " " + nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
			}else{
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + " " + nm1[rnd6] + nm2[rnd7] + nm5[rnd8];
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