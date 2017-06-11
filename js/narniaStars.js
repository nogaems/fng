var nm1 = ["","","","c","d","g","k","m","n","r","s","t","z"];
var nm2 = ["a","i","o","u","a","i","o","u","a","i","o","u","a","i","o","u","a","i","o","u","ia","ea","ua"];
var nm3 = ["g","gn","l","lm","ln","m","mn","n","r","rv","v","w","z"];
var nm4 = ["c","d","g","gn","gd","k","kn","l","ll","ld","lg","ln","mb","mn","m","ml","nd","ng","nm","nn","n","nt","nz","rn","rl","sn","sl","s","z"];
var nm5 = ["","","","","d","l","m","n","s"];

var check = ["anal","anus","arse","ass","balls","bastard","biatch","bigot","bitch","bollock","bollok","boner","boob","bugger","bum","butt","clitoris","cock","coon","crap","cunt","damn","dick","dildo","dyke","fag","feck","felching","fellate","fellatio","flange","fuck","gay","lust","goddamn","homo","jackass","jerk","jizz","knobend","labia","muff","nigga","nigger","penis","piss","poop","prick","pube","pussy","queer","scrotum","sex","shit","slut","smegma","spunk","tit","tosser","turd","twat","vagina","wank","whore","wtf"];

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
		if(i < 5){
			if(rnd < 3){
				while(rnd5 < 4){
					rnd5 = Math.random() * nm5.length | 0;
				}
			}
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
			for(j = 0; j < check.length; j++){
				while(names === check[j]){
					rnd3 = Math.floor(Math.random() * nm3.length);
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
				}
			}
		}else{
			rnd6 = Math.random() * nm4.length | 0;
			rnd7 = Math.random() * nm2.length | 0;
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
			for(j = 0; j < check.length; j++){
				while(names === check[j]){
					rnd3 = Math.floor(Math.random() * nm3.length);
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
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