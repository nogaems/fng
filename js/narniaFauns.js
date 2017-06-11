var nm1 = ["","","","d","f","h","l","m","n","ph","t","v"];
var nm2 = ["a","o","u","a","o","u","a","o","u","a","o","u","a","o","u","a","o","u","a","o","u","a","o","u","au","oa","ua","aa"];
var nm3 = ["lm","ln","ll","lr","l","lb","mm","mn","mr","mt","n","nn","nt","nm","rr","rn","rm","rl","rv","r","s","ss","sm","sl","st"];
var nm4 = ["ns","ms","ls","s","s","s","s","s","s","s"];
var nm5 = ["ia","a","ea","ia","ia"];

var check = ["anal","anus","arse","ass","balls","bastard","biatch","bigot","bitch","bollock","bollok","boner","boob","bugger","bum","butt","clitoris","cock","coon","crap","cunt","damn","dick","dildo","dyke","fag","feck","felching","fellate","fellatio","flange","fuck","gay","lust","goddamn","homo","jackass","jerk","jizz","knobend","labia","muff","nigga","nigger","penis","piss","poop","prick","pube","pussy","queer","scrotum","sex","shit","slut","smegma","spunk","tit","tosser","turd","twat","vagina","wank","whore","wtf"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0
		rnd3 = Math.random() * nm3.length | 0;
		if(tp === 1){
			rnd4 = Math.random() * nm5.length | 0;
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm5[rnd4];
				for(j = 0; j < check.length; j++){
					while(names === check[j]){
						rnd = Math.floor(Math.random() * nm1.length);
						names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm5[rnd4];
					}
				}
		}else{
			rnd4 = Math.random() * nm4.length | 0;
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + "u" + nm4[rnd4];
				for(j = 0; j < check.length; j++){
					while(names === check[j]){
						rnd = Math.floor(Math.random() * nm1.length);
						names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + "u" + nm4[rnd4];
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