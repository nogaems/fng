var nm1 = ["Adu","Ama","Ani","Ar","Arsha","Ashi","Ashtu","Bala","Bara","Basha","Beles","Delu","Di","Dura","Duru","Enu","Eri","Eshu","Hua","Hun","Il","Ilu","Ira","Ish","Ku","Kua","Kuba","Lu","Mani","Mara","Mashi","Na","Nara","Nashi","Nu","Rua","Run","Sana","Sari","Selu","Shir","Suma","Tab","Tin","Tiru","Uba","Uku","Ura","Ut","Zaki"];
var nm2 = ["ba","bam","bani","bu","ha","hara","hu","ka","ku","lazu","lua","mea","nar","nara","naram","naru","nashtu","ni","niri","nu","nua","pana","ram","ranu","rashi","raya","ri","rin","runu","shara","shari","shi","shti","shtu","shu","sunu","ta","tana","tani","tari","ti","tira","tiru","tua","tum","wia","ya","yara","yua","zu"];

function nameGen(){
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		nameMas();
		while(nMs === ""){
			nameMas();
		}
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(nMs));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}

function nameMas(){
	rnd = Math.floor(Math.random() * nm1.length);
	rnd2 = Math.floor(Math.random() * nm2.length);
	nMs = nm1[rnd] + nm2[rnd2];
	testSwear(nMs);
}