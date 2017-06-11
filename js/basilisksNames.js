var nm1 = ["","","","ch","h","j","n","r","s","sh","th","x","y","z"];
var nm2 = ["a","e","i","o","u","a","e","u","a","e","i","o","u","a","e","u","a","e","i","o","u","a","e","u","aa","au","ei","ou","ua"];
var nm3 = ["c","g","j","k","n","q","s","x","z","c","g","j","k","n","q","s","x","z","c","cc","ch","cs","cr","hs","hg","hx","hn","g","gg","gr","gy","gsh","j","k","kh","ksh","ks","kz","kr","n","ns","nsh","nz","nq","q","qh","s","sh","sz","x","z","zh"];
var nm4 = ["c","g","j","k","n","q","s","x","z"];
var nm5 = ["","","","c","h","q","s","sh","t","th","x","z"];

var check = ["anal","anus","arse","ass","balls","bastard","biatch","bigot","bitch","bollock","bollok","boner","boob","bugger","bum","butt","clitoris","cock","coon","crap","cunt","damn","dick","dildo","dyke","fag","feck","felching","fellate","fellatio","flange","fuck","gay","lust","goddamn","homo","jackass","jerk","jizz","knobend","labia","muff","nigga","nigger","niggers","penis","piss","poop","prick","pube","pussy","queer","scrotum","sex","shit","slut","smegma","spunk","tit","tosser","turd","twat","vagina","wank","whore","wtf"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0;
		rnd3 = Math.random() * nm3.length | 0;
		rnd4 = Math.random() * nm2.length | 0;
		rnd5 = Math.random() * nm5.length | 0;
		while(nm1[rnd] === nm3[rnd3]){
			rnd3 = Math.random() * nm3.length | 0;
		}
		while(nm5[rnd5] === nm3[rnd3]){
			rnd5 = Math.random() * nm5.length | 0;
		}
		if(i < 5){
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
			for(j = 0; j < check.length; j++){
				while(names === check[j]){
					rnd = Math.floor(Math.random() * nm1.length);
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
				}
			}
		}else if(i < 9){
			rnd6 = Math.random() * nm4.length | 0;
			rnd7 = Math.random() * nm2.length | 0;
			if(i < 7){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
				for(j = 0; j < check.length; j++){
					while(names === check[j]){
						rnd = Math.floor(Math.random() * nm1.length);
						names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
					}
				}
			}else{
				names = nm1[rnd] + nm2[rnd2] + nm4[rnd6] + nm2[rnd7] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
				for(j = 0; j < check.length; j++){
					while(names === check[j]){
						rnd = Math.floor(Math.random() * nm1.length);
						names = nm1[rnd] + nm2[rnd2] + nm4[rnd6] + nm2[rnd7] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
					}
				}
			}
		}else{
			rnd6 = Math.random() * nm3.length | 0;
			rnd7 = Math.random() * nm2.length | 0;
			while(nm3[rnd6] === nm3[rnd3]){
				rnd6 = Math.random() * nm3.length | 0;
			}
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm3[rnd6] + nm2[rnd7] + nm5[rnd5];
			for(j = 0; j < check.length; j++){
				while(names === check[j]){
					rnd = Math.floor(Math.random() * nm1.length);
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm3[rnd6] + nm2[rnd7] + nm5[rnd5];
				}
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