var nm1 = ["","","","b","ch","g","j","k","kh","r","v","z"];
var nm2 = ["a","i","o","u","a","o","u","a","i","o","u","a","o","u","a","i","o","u","a","o","u","a","i","o","u","a","o","u","a","i","o","u","a","o","u","a","i","o","u","a","o","u","a","i","o","u","a","o","u","ao","au","ou","ua"];
var nm3 = ["b","bb","bl","bn","br","dr","g","gd","gg","gr","gy","gz","j","k","kd","kg","kk","kn","ks","kt","ktr","kv","kz","ld","lg","lgr","lk","lkr","m","mg","mk","mm","n","ng","ngr","nk","nkr","nt","ntr","nz","q","qr","r","rb","rd","rdr","rg","rv","rz","sg","sk","skr","sq","t","tg","th","tr","tt","tz","x","xn","xx","xz","zb","zd","zl","zn","zz"];
var nm4 = ["c","d","g","k","q","t","x","z"];

var nm5 = ["ash","bane","bitter","blight","blood","bone","boulder","brick","bruise","carrion","chain","claw","cliff","corpse","crow","curse","dark","dead","death","dim","dirt","doom","dung","dust","earth","ember","eye","face","fang","feather","filth","fire","fist","flame","flint","forge","frost","gash","giant","gloom","glop","goo","gore","gravel","grief","grim","grime","grumble","gunk","hair","hell","ice","iron","lead","leather","limb","marble","marrow","mire","muck","mud","mug","nether","ooze","pebble","pest","pine","plague","pus","rash","rock","scourge","shock","silt","skin","skull","slate","sleaze","slime","sludge","slush","smut","snow","sore","spider","steel","storm","swamp","teeth","tooth","trash","tusk","void","wood","wound"];
var nm6 = ["bane","bash","basher","bellow","belly","blight","blower","bone","brace","breaker","breath","breather","brewer","bringer","brow","buster","chaser","chewer","claw","crest","crown","crusher","cutter","delver","digger","dribbler","dripper","drooler","eye","eyes","face","fang","feet","finger","flayer","foot","froth","fury","gaze","gazer","gobbler","gorger","grip","growl","guard","gulper","gut","guzzler","hand","head","hide","hunter","keeper","leg","legs","limb","mark","maul","maw","muncher","reaper","reaver","ripper","robber","runner","scrub","seeker","shadow","shaper","shoulder","slobber","snarl","snout","sorrow","splitter","stalker","stride","strider","strike","striker","stuffer","surge","sworn","taker","walker","watcher","weaver"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm4.length | 0;
			if(i < 3){
				while(rnd < 3 || nm1[rnd] === nm4[rnd3]){
					rnd = Math.random() * nm1.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm4[rnd3];
			}else{
				rnd4 = Math.random() * nm2.length | 0;
				rnd5 = Math.random() * nm3.length | 0;
				while(nm1[rnd] === nm3[rnd5] || nm3[rnd5] === nm4[rnd3]){
					rnd5 = Math.random() * nm3.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd5] + nm2[rnd4] + nm4[rnd3];
			}
		}else{
			rnd = Math.random() * nm5.length | 0;
			rnd2 = Math.random() * nm6.length | 0;
			while(nm5[rnd] === nm6[rnd2]){
				rnd2 = Math.random() * nm6.length | 0;
			}
			names = nm5[rnd] + nm6[rnd2];
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