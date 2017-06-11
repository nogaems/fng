var nm1 = ["b","g","k","m","n","t","s","t","v","z"];
var nm2 = ["a","e","i","o","u"];
var nm3 = ["d","g","gg","k","kk","n","ng","sh","z","zz"];
var nm4 = ["","","","b","d","k","m","n","t"];

var nm5 = ["","","","","b","br","d","dr","g","gr","kr","sk","sl","sq","tr","t","z"];
var nm6 = ["a","e","i","o","u"];
var nm7 = ["b","bz","d","dz","dv","gr","gg","gn","gq","kr","kn","kz","kq","lk","lq","mz","mk","mg","nk","nz","nv","qv","qz","qr","rg","rl","rv","rz","zr","zl","zz"];
var nm8 = ["","","","","d","g","kk","k","rt","rd","sk","t","x"];

var nm9 = ["adder","alder","ash","asp","beetle","blister","boar","bone","cask","claw","coal","dew","dust","earth","ember","face","feather","fern","fire","fist","flame","flint","frog","frost","fuse","gem","goat","grass","hearh","heart","ice","iron","knuckle","lava","leaf","locust","marble","moss","mud","nettle","oat","orb","peach","pebble","pine","pyre","rock","sheep","slate","snake","spider","spike","spit","steam","sting","stink","thistle","toad","tusk","vine","wood"];
var nm10 = ["back","basher","belly","blade","blower","bone","brawler","breaker","breath","brow","button","chaser","dancer","drifter","fall","fang","fire","fist","flare","flinger","flogger","fright","fume","gazer","glider","guard","hunter","jumper","keeper","limbs","mantle","mark","napper","palm","rider","ripper","runner","scourger","seeker","shot","singer","speaker","splitter","sprinter","staff","stalker","stand","step","stick","striker","taker","thorn","tosser","trapper","tusk","vaulter","walker","watcher","wave","weaver","wild","wilde"];
var nm11 = ["Assassin","Bandit","Blaster","Bomber","Boss","Brigade","Buffoon","Bully","Butcher","Cohort","Commander","Commando","Conscript","Crackshot","Crew","Cultist","Daredevil","Dealer","Enforcer","Engineer","Explorer","Fanatic","Goblin","Gorger","Grappler","Grenadier","Grunt","Grunts","Guide","Handler","Harasser","Hermit","Hero","Hobgoblin","Hooligan","Hopper","Hunter","Initiate","Instigator","Jailer","Jocker","Kaboomist","Legionnaire","Lookout","Machinist","Maniac","Marauder","Marshal","Mason","Matron","Medic","Mob Boss","Mountaineer","Mutant","Outlander","Outrider","Patrol","Piker","Pilferer","Prospector","Psychopath","Punisher","Pyromancer","Rackateer","Raider","Recruiter","Rider","Ringleader","Roughrider","Ruffian","Runner","Sapper","Scout","Scrapper","Sentry","Sergeant","Settler","Shaman","Shortcutter","Sky Raider","Skycutter","Sledder","Snitch","Soothsayer","Spelunker","Spy","Squad","Striker","Tactician","Taskmaster","Tinkerer","Trader","Tunneler","Turncoat","Underling","Underminer","Vandal","Warchief","Warden","Wardriver","Welder","Witch","Wizard"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 8){
			if(i < 2){
				rnd = Math.floor(Math.random() * nm1.length);
				rnd2 = Math.floor(Math.random() * nm2.length);
				rnd3 = Math.floor(Math.random() * nm4.length);
				while(nm4[rnd3] === nm1[rnd]){
					rnd3 = Math.floor(Math.random() * nm4.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm4[rnd3] + "-" + nm1[rnd] + nm2[rnd2] + nm4[rnd3];
			}else if(i < 4){
				rnd = Math.floor(Math.random() * nm2.length);
				rnd2 = Math.floor(Math.random() * nm3.length);
				rnd3 = Math.floor(Math.random() * nm2.length);
				names = nm2[rnd] + nm3[rnd2] + nm2[rnd3] + "-" + nm2[rnd] + nm3[rnd2] + nm2[rnd3];
			}else{
				rnd = Math.floor(Math.random() * nm5.length);
				rnd2 = Math.floor(Math.random() * nm6.length);
				rnd3 = Math.floor(Math.random() * nm7.length);
				rnd4 = Math.floor(Math.random() * nm6.length);
				rnd5 = Math.floor(Math.random() * nm8.length);
				names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm8[rnd5];
			}
		}else{
			rnd = Math.floor(Math.random() * nm9.length);
			rnd2 = Math.floor(Math.random() * nm10.length);
			while(nm9[rnd] === nm10[rnd2]){
				rnd2 = Math.floor(Math.random() * nm10.length);
			}
			rnd3 = Math.floor(Math.random() * nm11.length);
			names = nm9[rnd] + nm10[rnd2] + " " + nm11[rnd3];
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