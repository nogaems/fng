var nm1 = ["","","","","b","c","f","g","gr","h","j","k","l","m","n","p","r","s","sh","t","v","w","z"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","y","y","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ea","ee","au","ai","ie","ea","io"];
var nm3 = ["b","c","d","f","g","k","l","m","n","p","r","s","t","v","x","b","br","c","ch","d","dr","f","fr","g","k","l","ld","ll","lr","lt","m","n","nc","nd","ng","ngr","nn","nr","ns","nt","p","r","rbr","rm","rn","rr","rsh","rt","sg","shm","ss","sr","st","t","th","v","x"];
var nm4 = ["","","","","c","d","l","l","l","l","ll","m","n","n","n","n","n","nt","r","rg","rl","s","sh","st","t","x"];
var nm5 = ["b","br","c","d","f","g","h","j","k","l","m","n","r","s","sh","t","th","w","z"];
var nm6 = ["a","e","i","o","u","a","e","i","a","a","e","i","o","u","a","e","i","a","a","e","i","o","u","a","e","i","a","a","e","i","o","u","a","e","i","a","a","e","i","o","u","ee","io","ia","ai","ea"];
var nm7 = ["c","d","dn","k","kk","kl","l","l","l","l","lk","ll","ll","ll","lm","ln","m","mm","n","nn","r","rdr","rn","rr","s","ss","sn","sl","t","tr","v","y","z","c","d","k","l","l","m","n","r","s","t","v","y","z","kk","ll","ll","mm","nn","rr","ss"];
var nm8 = ["","","","","","","","","","","","","","","","","","h","n","m"];
var nm9 = ["b","br","c","ch","cr","d","f","g","h","j","k","l","m","p","r","s","sp","t","v","z"];
var nm10 = ["a","e","i","o","u","ia","ai","io"];
var nm11 = ["dr","g","gr","gl","k","l","lz","ld","m","n","nd","r","r","r","r","rr","rm","rn","rt","ss","sr","y","z","g","k","l","m","n","r","y","z"];
var nm12 = ["lth","nth","rth","th"];
var nm13 = ["b","br","ch","f","g","h","k","l","m","n","p","pr","r","s","t","w","z"];
var nm14 = ["a","e","i","o","u"];
var nm15 = ["d","d","l","l","l","l","ll","lm","ln","ls","m","m","n","n","nl","nr","nm","r","r","r","rl","r","s","s","yl","yr","yn"];
var check = ["anal","anus","arse","ass","balls","bastard","biatch","bigot","bitch","bollock","bollok","boner","boob","bugger","bum","butt","clitoris","cock","coon","crap","cunt","damn","dick","dildo","dyke","fag","feck","felching","fellate","fellatio","flange","fuck","gay","lust","goddamn","homo","jackass","jerk","jizz","knobend","labia","muff","nigga","nigger","penis","piss","poop","prick","pube","pussy","queer","scrotum","sex","shit","slut","smegma","spunk","tit","tosser","turd","twat","vagina","wank","whore","wtf"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm3.length);
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm5.length);
			rnd2 = Math.floor(Math.random() * nm6.length);
			rnd3 = Math.floor(Math.random() * nm7.length);
			rnd4 = Math.floor(Math.random() * nm6.length);
			rnd5 = Math.floor(Math.random() * nm8.length);
			if(i < 5){
				names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm8[rnd5];
				for(j = 0; j < check.length; j++){
					while(names === check[j]){
						rnd = Math.floor(Math.random() * nm5.length);
						names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm8[rnd5];
					}
				}
			}else{
				rnd6 = Math.floor(Math.random() * nm7.length);
				rnd7 = Math.floor(Math.random() * nm6.length);
				names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm7[rnd6] + nm6[rnd7] + nm8[rnd5];
				for(j = 0; j < check.length; j++){
					while(names === check[j]){
						rnd = Math.floor(Math.random() * nm5.length);
						names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm7[rnd6] + nm6[rnd7] + nm8[rnd5];
					}
				}
			}
		}else if(tp === 2){
				rnd5 = Math.floor(Math.random() * nm12.length);
				if(i < 5){
					rnd = Math.floor(Math.random() * nm9.length);
					rnd2 = Math.floor(Math.random() * nm10.length);
					rnd3 = Math.floor(Math.random() * nm11.length);
					rnd4 = Math.floor(Math.random() * nm10.length);
					if(i < 3){
						names = nm9[rnd] + nm10[rnd2] + nm11[rnd3] + nm10[rnd4] + nm12[rnd5];
						for(j = 0; j < check.length; j++){
							while(names === check[j]){
								rnd = Math.floor(Math.random() * nm9.length);
								names = nm9[rnd] + nm10[rnd2] + nm11[rnd3] + nm10[rnd4] + nm12[rnd5];
							}
						}
					}else{
						rnd6 = Math.floor(Math.random() * nm11.length);
						rnd7 = Math.floor(Math.random() * nm10.length);
						names = nm9[rnd] + nm10[rnd2] + nm11[rnd3] + nm10[rnd4] + nm11[rnd6] + nm10[rnd7] + nm12[rnd5];
						for(j = 0; j < check.length; j++){
							while(names === check[j]){
								rnd = Math.floor(Math.random() * nm9.length);
								names = nm9[rnd] + nm10[rnd2] + nm11[rnd3] + nm10[rnd4] + nm11[rnd6] + nm10[rnd7] + nm12[rnd5];
							}
						}
					}
				}else{
					rnd = Math.floor(Math.random() * nm13.length);
					rnd2 = Math.floor(Math.random() * nm14.length);
					rnd3 = Math.floor(Math.random() * nm15.length);
					rnd4 = Math.floor(Math.random() * nm14.length);
					if(i < 8){
						names = nm13[rnd] + nm14[rnd2] + nm15[rnd3] + nm14[rnd4] + nm12[rnd5];
						for(j = 0; j < check.length; j++){
							while(names === check[j]){
								rnd = Math.floor(Math.random() * nm13.length);
								names = nm13[rnd] + nm14[rnd2] + nm15[rnd3] + nm14[rnd4] + nm12[rnd5];
							}
						}
					}else{
						rnd6 = Math.floor(Math.random() * nm15.length);
						rnd7 = Math.floor(Math.random() * nm14.length);
						names = nm13[rnd] + nm14[rnd2] + nm15[rnd3] + nm14[rnd4] + nm15[rnd6] + nm14[rnd7] + nm12[rnd5];
						for(j = 0; j < check.length; j++){
							while(names === check[j]){
								rnd = Math.floor(Math.random() * nm13.length);
								names = nm13[rnd] + nm14[rnd2] + nm15[rnd3] + nm14[rnd4] + nm15[rnd6] + nm14[rnd7] + nm12[rnd5];
							}
						}
					}
				}
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd5 = Math.floor(Math.random() * nm4.length);
			if(i < 3){
				while(rnd < 4){
					rnd = Math.floor(Math.random() * nm1.length);
				}
				while(rnd5 < 4){
					rnd5 = Math.floor(Math.random() * nm4.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm4[rnd5];
				for(j = 0; j < check.length; j++){
					while(names === check[j]){
						rnd = Math.floor(Math.random() * nm1.length);
						names = nm1[rnd] + nm2[rnd2] + nm4[rnd5];
					}
				}
			}else if(i < 7){
				rnd3 = Math.floor(Math.random() * nm3.length);
				rnd4 = Math.floor(Math.random() * nm2.length);
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
				for(j = 0; j < check.length; j++){
					while(names === check[j]){
						rnd = Math.floor(Math.random() * nm1.length);
						names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
					}
				}
			}else{
				rnd3 = Math.floor(Math.random() * nm3.length);
				rnd4 = Math.floor(Math.random() * nm2.length);
				rnd6 = Math.floor(Math.random() * nm3.length);
				rnd7 = Math.floor(Math.random() * nm2.length);
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm3[rnd6] + nm2[rnd7] + nm4[rnd5];
				for(j = 0; j < check.length; j++){
					while(names === check[j]){
						rnd = Math.floor(Math.random() * nm1.length);
						names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm3[rnd6] + nm2[rnd7] + nm4[rnd5];
					}
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