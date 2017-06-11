var nm1 = ["b","c","d","f","g","h","k","r","v","w","z"];
var nm2 = ["a","e","o","u","a","e","o","u","a","e","o","u","i"];
var nm3 = ["br","dd","dr","fn","fg","kn","km","kd","kg","kr","ld","lth","lg","lb","ldr","lz","lv","mg","md","mk","mz","ng","nk","nd","nv","rb","rd","rg","rk","rt","sg","sk","sr","tr","tk","tg","yl","yr","yg","yz","yv","zr","zg","zn"];
var nm4 = ["c","d","g","m","n","r"];

var nm5 = ["","","","","c","d","h","k","n","m","r","t","v","z"];
var nm6 = ["a","e","i","a","e","i","o","a","e","i","a","e","i","o","a","e","i","o","ee","aa"];
var nm7 = ["d","g","k","p","r","v","z"];
var nm8 = ["d","g","j","g","k","l","m","n","r","v","z"];
var nm9 = ["d","l","n","s"];

var nm10 = ["b","d","j","g","k","n","r","s","t","v","z"];
var nm11 = ["a","e","i","o","a","e","i","o","a","e","i","o","u"];
var nm12 = ["bb","br","gg","gn","gr","gl","kr","km","kn","kl","lg","lm","lr","lv","mb","md","mv","ml","ng","nd","nb","nl","rm","rk","rg","rl","rn","tn","tl"];
var nm13 = ["d","m","n","r","s","t"];

var nm14 = ["Academic","Acclaimed","Accomplished","Adept","Advanced","Aerial","Aviary","Bomb","Brave","Bridge","Brilliant","Bruised","Cautious","Chief","Consul's","Dapper","Defensive","Defiant","Demolition","Devoted","Diligent","Dutiful","Dwarven","Eager","Esteemed","Exalted","Examplar","Examplary","Expert","Fearless","Gearshift","Gifted","Grand","Great","Illustrious","Infamous","Junior","Liberated","Lone","Lost","Loyal","Master","Nimble","Powerful","Prestigious","Prime","Reckless","Robust","Rough","Rowdy","Savant","Sneaky","Sturdy","Swift","Thunderous","Trained","Troubled","Venerated","Vengeful","Veteran","Villainous","Violent","Visionary","Wicked","Wild","Wrathful"];
var nm15 = ["Armorer","Artificer","Artisan","Assailant","Augmenter","Berserker","Blacksmith","Blastminer","Cadet","Captain","Conjurer","Crafter","Craftsman","Defender","Digger","Driller","Excavator","Gearshift","Grease Monkey","Grunt","Guard","Machinist","Mage","Mechanic","Mender","Mercenary","Miner","Motorist","Nomad","Operator","Patrol","Pilot","Prospector","Recruit","Recruiter","Scorcher","Scout","Sentinel","Sentry","Shieldguard","Soldier","Specialist","Swordsmith","Technician","Thaumaturgist","Tinketeer","Toolcraft","Trader","Trinketeer","Trooper","Veteran","Vigilante","Ward","Warden","Warrior","Weaponsmith","Wizard","Wright"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm10.length);
		rnd2 = Math.floor(Math.random() * nm11.length);
		rnd3 = Math.floor(Math.random() * nm12.length);
		rnd4 = Math.floor(Math.random() * nm11.length);
		rnd5 = Math.floor(Math.random() * nm13.length);
		lName = nm10[rnd] + nm11[rnd2] + nm12[rnd3] + nm11[rnd2] + nm13[rnd5];
		if(tp === 1){
			if(i < 6){
				rnd = Math.floor(Math.random() * nm5.length);
				rnd2 = Math.floor(Math.random() * nm6.length);
				rnd3 = Math.floor(Math.random() * nm7.length);
				rnd4 = Math.floor(Math.random() * nm6.length);
				while(nm7[rnd3] === nm5[rnd]){
					rnd3 = Math.floor(Math.random() * nm7.length);
				}
				if(i < 3){
					rnd5 = Math.floor(Math.random() * nm8.length);
					rnd6 = Math.floor(Math.random() * nm6.length);
					while(nm8[rnd5] === nm7[rnd3]){
						rnd5 = Math.floor(Math.random() * nm8.length);
					}
					names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm8[rnd5] + nm6[rnd6] + " " + lName;
				}else{
					rnd5 = Math.floor(Math.random() * nm9.length);
					while(nm9[rnd5] === nm7[rnd3]){
						rnd5 = Math.floor(Math.random() * nm9.length);
					}
					names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm9[rnd5] + " " + lName;
				}
			}else{
				rnd = Math.floor(Math.random() * nm14.length);
				rnd2 = Math.floor(Math.random() * nm15.length);
				names = nm14[rnd] + " " + nm15[rnd2];
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
				while(nm4[rnd5] === nm3[rnd3]){
					rnd5 = Math.floor(Math.random() * nm4.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5] + " " + lName;
			}else{
				rnd = Math.floor(Math.random() * nm14.length);
				rnd2 = Math.floor(Math.random() * nm15.length);
				names = nm14[rnd] + " " + nm15[rnd2];
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