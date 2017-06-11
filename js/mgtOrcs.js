var nm1 = ["d","g","k","m","n","s","t","v","z"];
var nm1b = ["","","","","","","d","g","k","m","n","s","t","v","z"];
var nm2 = ["a","e","o","u"];
var nm3 = ["c","d","g","k","q","r","z"];
var nm4 = ["d","g","k","m","n","s","t","v","z"];
var nm5 = ["'","-"];
var nm6 = ["a","e","o","u","a","e","o","u","a","e","o","u","ua","uu","aa","au","ao","ia","ou"];
var nm7 = ["d","dh","dr","g","gr","gn","k","kn","kr","m","n","s","st","t","tr","v","z","zh"];
var nm8 = ["c","cr","cd","d","dr","dg","dk","g","gr","gn","gd","gz","k","kr","kd","kv","kz","m","mm","n","nn","ng","nd","q","qr","r","rr","rk","rz","rv","rd","rg","z","zk","zr","zz"];

var nm9 = ["","","","","","","","","","","","g","h","l","m","n","r","t","z"];
var nm10 = ["d","g","l","m","n","r","v","z"];
var nm11 = ["d","g","k","m","n","r","s","sh","t","th","v","z"];

var nm12 = ["alder","ash","bane","black","blood","boulder","brass","bronze","cinder","dark","dawn","dead","death","doom","dust","ember","fire","flame","gloom","haze","heavy","hell","iron","keen","lone","molten","mourn","nether","proud","rage","rapid","rough","scream","shadow","sharp","silent","skull","slate","steel","stern","stone","storm","swift","thunder","void","war","wild"];
var nm13 = ["bane","bellow","blade","blaze","blood","bone","brace","brand","brow","burn","claw","cleave","crest","cut","doom","eye","fang","fist","flaw","force","forge","fury","gaze","gloom","grip","growl","hand","heart","keep","mane","mantle","mark","maul","maw","mourn","rage","reach","ridge","run","scar","shade","shard","spark","stalk","stride","surge","sworn","thorn"];
var nm14 = ["Artificer","Artisan","Assailant","Assassin","Barbarian","Bigwig","Brawler","Bruiser","Brute","Cannoneer","Captain","Chief","Colonist","Conscript","Enforcer","Executioner","Fanatic","General","Gladiator","Healer","Horde","Hordechief","Hunter","Looter","Lumberjack","Maniac","Marauder","Mechanic","Mercenary","Militant","Operative","Orc","Outlaw","Overlord","Overseer","Paratrooper","Patrol","Pillager","Pioneer","Raider","Ravager","Recruit","Rider","Roughrider","Sadist","Savage","Scout","Settler","Shaman","Slayer","Soldier","Spy","Technician","Vanguard","Veteran","Warbringer","Warlord","Warmonger","Watcher","Zealot"];

var nm15 = ["Acclaimed","Aggressive","Agitated","Ambush","Angry","Anguished","Battle","Bellowing","Bitter","Blind","Broken","Brutal","Careless","Corrupt","Corrupted","Crazed","Crazy","Cruel","Daring","Defiant","Delirious","Devoted","Diligent","Disguised","Dutiful","Eager","Enraged","Fearless","Forsaken","Gleeful","Grave","Grim","Grumpy","Idle","Insane","Ire","Jealous","Mad","Merciless","Monstrous","Obedient","Pitiless","Powerful","Proud","Puzzled","Raging","Rash","Reckless","Sadistic","Shady","Stark","Swift","Terrifying","Thick","Trifling","Unfit","Unwilling","Vengeful","Vicious","Villainous","Violent","Wicked","Wild","Wretched"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(tp === 1){
			if(i < 6){
				rnd = Math.floor(Math.random() * nm9.length);
				rnd2 = Math.floor(Math.random() * nm2.length);
				rnd3 = Math.floor(Math.random() * nm10.length);
				while(nm9[rnd] === nm10[rnd3]){
					rnd3 = Math.floor(Math.random() * nm10.length);
				}
				rnd4 = Math.floor(Math.random() * nm2.length);
				rnd5 = Math.floor(Math.random() * nm11.length);
				while(nm11[rnd5] === nm10[rnd3]){
					rnd5 = Math.floor(Math.random() * nm11.length);
				}
				rnd6 = Math.floor(Math.random() * nm2.length);
				names = nm9[rnd] + nm2[rnd2] + nm10[rnd3] + nm2[rnd4] + nm11[rnd5] + nm2[rnd6];
			}else if(i < 8){
				rnd = Math.floor(Math.random() * nm12.length);
				rnd2 = Math.floor(Math.random() * nm13.length);
				while(nm12[rnd] === nm13[rnd2]){
					rnd2 = Math.floor(Math.random() * nm13.length);
				}
				rnd3 = Math.floor(Math.random() * nm14.length);
				names = nm12[rnd] + nm13[rnd2] + " " + nm14[rnd3];
			}else{
				rnd = Math.floor(Math.random() * nm15.length);
				rnd2 = Math.floor(Math.random() * nm14.length);
				names = nm15[rnd] + " " + nm14[rnd2];
			}
		}else{
			if(i < 6){
				rnd2 = Math.floor(Math.random() * nm2.length);
				rnd4 = Math.floor(Math.random() * nm4.length);
				if(i < 3){
					rnd = Math.floor(Math.random() * nm1.length);
					rnd3 = Math.floor(Math.random() * nm3.length);
					while(nm1[rnd] === nm3[rnd3]){
						rnd3 = Math.floor(Math.random() * nm3.length);
					}
					rnd5 = Math.floor(Math.random() * nm1b.length);
					rnd6 = Math.floor(Math.random() * nm6.length);
					rnd7 = Math.floor(Math.random() * nm4.length);
					while(nm1b[rnd5] === nm4[rnd7]){
						rnd7 = Math.floor(Math.random() * nm7.length);
					}
					rnd8 = Math.floor(Math.random() * nm5.length);
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm5[rnd8] + nm1b[rnd5] + nm6[rnd6] + nm4[rnd7];
				}else{
					rnd = Math.floor(Math.random() * nm7.length);
					rnd3 = Math.floor(Math.random() * nm8.length);
					rnd5 = Math.floor(Math.random() * nm6.length);
					while(nm8[rnd3] === nm7[rnd]){
						rnd3 = Math.floor(Math.random() * nm8.length);
					}
					names = nm7[rnd] + nm2[rnd2] + nm8[rnd3] + nm6[rnd5] + nm4[rnd4];
				}
			}else if(i < 8){
				rnd = Math.floor(Math.random() * nm12.length);
				rnd2 = Math.floor(Math.random() * nm13.length);
				while(nm12[rnd] === nm13[rnd2]){
					rnd2 = Math.floor(Math.random() * nm13.length);
				}
				rnd3 = Math.floor(Math.random() * nm14.length);
				names = nm12[rnd] + nm13[rnd2] + " " + nm14[rnd3];
			}else{
				rnd = Math.floor(Math.random() * nm15.length);
				rnd2 = Math.floor(Math.random() * nm14.length);
				names = nm15[rnd] + " " + nm14[rnd2];
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