var nm1 = ["c","d","g","k","n","q","r","t","v","z"];
var nm2 = ["a","o","u","a","o","u","a","o","u","a","o","u","a","o","u","a","o","u","a","o","u","i","e","a","o","u","aa","au","uu"];
var nm3 = ["dr","dg","dv","hg","hn","hnd","hrg","hrd","hlg","hln","hld","hng","ng","nd","ndr","ngr","nr","nz","nv","ntr","qr","qn","ql","rc","rd","rdr","rg","rgr","rk","rq","sc","scr","sdr","skr","sq","sqr","st","str","tg","tgr","tk","tkr","tr","vd","vg","vgr","vdr","vr","zg","zr","zq"];
var nm4 = ["d","dh","g","k","q","qt","qth","r","rk","rd","rq","rt","rth","x","z"];

var nm5 = ["c","d","g","h","j","k","m","n","r","t","v","z"];
var nm6 = ["a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","u","u","u","a","e","i","o","a","e","i","o","ee","uu","ue","eu","au"];
var nm7 = ["b","bb","br","d","dd","dn","dr","g","gg","gd","gn","gr","gv","gz","k","kk","kn","kr","kz","ld","lg","lr","lz","nd","ng","nr","nv","nz","q","qr","qn","r","rr","rb","rd","rg","rgr","rq","rs","tv","rz","sc","sg","sk","sq","sr","sqr","sz","szr","t","tg","tr","thr","thn","thg","zc","zg","zk","zl","zr"];

var nm8 = ["amber","ash","battle","bitter","blade","blaze","blood","cinder","cruel","dark","dead","death","doom","elder","ember","end","fall","fel","fire","flame","flare","fright","furor","fury","gloom","gore","grim","haze","hell","mad","mourn","nether","pain","pyre","rage","rough","ruin","scorch","shade","shadow","skull","storm","taint","tinder","war","wild"];
var nm9 = ["bane","bellow","binder","blade","blaze","blood","breaker","bringer","caller","chanter","crest","doom","drifter","fall","fang","fist","flayer","force","forge","fury","guard","haze","hide","horn","hunter","mane","mantle","maul","maw","might","monger","mourn","rage","reaper","reaver","rider","ripper","roar","runner","shade","shadow","shot","slayer","stalker","stride","strider","strike","striker","surge","sworn"];
var nm10 = ["Aggressor","Ancestor","Assailant","Bodyguard","Brawler","Bruiser","Butcher","Cerberus","Champion","Commando","Crew","Defender","Disciple","Elite","Enforcer","Envoy","Executioner","Explorer","Fighter","Guard","Guardian","Guerrilla","Hero","Hunter","Illusionist","Keeper","Lookout","Mercenary","Minotaur","Outrider","Patrol","Raider","Ranger","Runner","Safeguard","Scout","Sentinel","Shaman","Shepherd","Slayer","Sorcerer","Spiritbinder","Squad","Squadron","Stalker","Tactician","Trapper","Trooper","Vanguard","Veteran","Vigilante","Warlord","Warrior"];

var nm11 = ["Adventurous","Agitated","Angered","Angry","Bitter","Blaze","Bold","Border","Borderland","Brave","Canyon","Confused","Corrupt","Courageous","Cruel","Daring","Defiant","Delirious","Diligent","Energetic","Enraged","Exhausted","Fanatic","Fearless","Focused","Forsaken","Frightening","Furious","Grim","Haunting","Heavy","Humongous","Juvenile","Keen","Labyrinth","Lone","Lost","Mad","Mysterious","Noxious","Powerful","Prime","Ragged","Raging","Rash","Reckless","Robust","Silent","Stark","Swift","Thunderous","Vengeful","Vicious","Vigilant","Violent","Vivid","Watchful","Wicked","Wild","Wrathful","Wretched"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(tp === 1){
			if(i < 6){
				rnd = Math.floor(Math.random() * nm5.length);
				rnd2 = Math.floor(Math.random() * nm6.length);
				rnd3 = Math.floor(Math.random() * nm7.length);
				rnd4 = Math.floor(Math.random() * nm6.length);
				names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4];
			}else if(i < 8){
				rnd = Math.floor(Math.random() * nm8.length);
				rnd2 = Math.floor(Math.random() * nm9.length);
				while(nm8[rnd] === nm9[rnd2]){
					rnd2 = Math.floor(Math.random() * nm9.length);
				}
				rnd3 = Math.floor(Math.random() * nm10.length);
				names = nm8[rnd] + nm9[rnd2] + " " + nm10[rnd3];
			}else{
				rnd = Math.floor(Math.random() * nm11.length);
				rnd2 = Math.floor(Math.random() * nm10.length);
				names = nm11[rnd] + " " + nm10[rnd2];
			}
		}else{
			if(i < 6){
				rnd = Math.floor(Math.random() * nm1.length);
				rnd2 = Math.floor(Math.random() * nm2.length);
				rnd3 = Math.floor(Math.random() * nm3.length);
				rnd4 = Math.floor(Math.random() * nm2.length);
				rnd5 = Math.floor(Math.random() * nm4.length);
				while(nm3[rnd3] === nm1[rnd]){
					rnd3 = Math.floor(Math.random() * nm3.length);
				}
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
			}else if(i < 8){
				rnd = Math.floor(Math.random() * nm8.length);
				rnd2 = Math.floor(Math.random() * nm9.length);
				while(nm8[rnd] === nm9[rnd2]){
					rnd2 = Math.floor(Math.random() * nm9.length);
				}
				rnd3 = Math.floor(Math.random() * nm10.length);
				names = nm8[rnd] + nm9[rnd2] + " " + nm10[rnd3];
			}else{
				rnd = Math.floor(Math.random() * nm11.length);
				rnd2 = Math.floor(Math.random() * nm10.length);
				names = nm11[rnd] + " " + nm10[rnd2];
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