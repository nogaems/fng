var names1 = ["aak","aal","aam","aar","aav","aaz","ag","ah","al","am","aus","bah","bein","bel","bex","beyn","bii","bo","bok","brii","brit","brod","brom","bron","daal","daan","daar","dah","dein","dez","dii","diil","diin","diiv","dir","dok","dov","draal","dreh","drem","drey","drog","drun","du","du'ul","dun","dur","dwiin","ek","faad","faas","faaz","feim","fel","feyn","fiik","fo","frin","frod","fron","frul","ful","fun","funt","fus","gaaf","gaan","gaar","geh","gein","gol","golt","golz","graag","graan","grah","gram","grik","grind","gro","gron","gruth","gut","haal","haas","hah","heim","het","heyv","hind","hon","hun","iiz","in","inhus","jer","joor","jot","jud","jul","jun","kaal","kaan","kaaz","kah","kein","kel","kest","key","keyn","kiim","kiin","kiir","kip","klo","klov","ko","kod","kol","koor","krah","kras","kreh","krein","kren","krent","krif","krii","kriid","kriist","kril","krin","kro","kron","kul","laan","laas","laat","lah","leh","lein","liiv","lir","lo","lok","lon","loost","lot","luft","lun","luv","maar","mah","mal","med","mey","meyz","mid","miin","mir","mon","mul","mun","muz","naak","naan","naar","nah","nahl","nau","nax","neh","ney","ni","nid","nii","niin","nil","nin","nir","nis","nok","nos","nus","od","okaaz","ol","om","ond","ont","oth","ov","paak","paal","paar","paaz","pah","pel","peyt","pook","praal","praan","prem","qah","qeth","qo","qoth","raan","rah","rath","rein","rek","rel","reyth","rii","riik","ro","rok","rot","ru","rul","ruth","saan","sah","sar","shaan","shul","siiv","sik","sil","slen","so","sod","sos","sot","sov","spaan","stin","strun","su","su'um","sul","tah","tey","thaarn","thu'um","thur","tiid","til","toor","tu","tum","tuz","ul","un","unt","us","uth","uv","vaal","vaat","vaaz","vah","ved","ven","vey","viik","viin","viing","viir","vith","vod","vol","vu","vul","vum","vur","vus","wahl","wen","win","wol","wuld","wuth","yah","yolx","yuvon","zaam","zaan","zah","zeim","zein","zii","zin","zind","zok","zol","zoor","zul","zun"];

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var br = [];
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 8){
			rnd = parseInt(Math.floor((Math.random() * names1.length)));
			rnd2 = parseInt(Math.floor((Math.random() * names1.length)));
				while(rnd2 === rnd){
					rnd2 = parseInt(Math.floor((Math.random() * names1.length)));
				}
			rnd3 = parseInt(Math.floor((Math.random() * names1.length)));
				while(rnd3 === rnd || rnd3 === rnd2){
					rnd3 = parseInt(Math.floor((Math.random() * names1.length)));
				}
			names = names1[rnd] + names1[rnd2] + names1[rnd3];
		}else{
			rnd = parseInt(Math.floor((Math.random() * names1.length)));
			rnd2 = parseInt(Math.floor((Math.random() * names1.length)));
				while(rnd2 === rnd){
					rn22 = parseInt(Math.floor((Math.random() * names1.length)));
				}
			names = names1[rnd] + names1[rnd2];
		}
		br[i] = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br[i]);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}