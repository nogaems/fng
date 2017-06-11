var nm1 = ["b","d","h","l","m","n","r","t","v","z"];
var nm2 = ["e","o","u","e","o","u","a","i"];
var nm3 = ["b","d","k","l","m","n","s","t","z"];

var nm4 = ["e","a","o","e","a","o","e","a","o","e","a","o","i","i","u"];
var nm5 = ["b","d","f","g","l","m","n","r","s","t","v","y","z"];
var nm6 = ["b","d","g","h","l","m","n","r","s","t","y","z"];

var nm7 = ["Ambassador","Ascendant","Breezecaller","Cerberus","Cloud-Conjurer","Floodbringer","Cloudchaser","Cloudguard","Cloudkeeper","Cloudskater","Cloudwatcher","Conjurer","Conservator","Consul","Custodian","Defender","Delegate","Diplomat","Diviner","Emissary","Enchanter","Envoy","Guard","Guardian","Gustcaller","Illusionist","Keeper","Legate","Mage","Messenger","Mindsweeper","Mirror-Mage","Overseer","Prophet","Protector","Raincaller","Rainchaser","Rainmaker","Rainshaper","Sage","Savant","Sear","Seer","Sentinel","Sentry","Shepherd","Soothsayer","Sorcerer","Spellbinder","Vicar","Ward","Warden","Watch","Windcaller"];
var nm8 = ["","","","","","b","d","h","l","m","n","r","t","v","z"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd9 = Math.floor(Math.random() * nm7.length);
		if(tp === 1){
			if(i < 6){
				rnd = Math.floor(Math.random() * nm4.length);
				rnd2 = Math.floor(Math.random() * nm5.length);
				rnd3 = Math.floor(Math.random() * nm4.length);
				if(i < 3){
					names = nm4[rnd] + nm5[rnd2] + nm4[rnd3] + ", " + nm7[rnd9];
				}else{
					rnd4 = Math.floor(Math.random() * nm6.length);
					rnd5 = Math.floor(Math.random() * nm4.length);
					names = nm4[rnd] + nm5[rnd2] + nm4[rnd3] + nm6[rnd4] + nm4[rnd5] + ", " + nm7[rnd9];
				}
			}else{
				rnd = Math.floor(Math.random() * nm8.length);
				rnd2 = Math.floor(Math.random() * nm4.length);
				rnd3 = Math.floor(Math.random() * nm3.length);
				rnd4 = Math.floor(Math.random() * nm4.length);
				rnd5 = Math.floor(Math.random() * nm3.length);
				rnd6 = Math.floor(Math.random() * nm4.length);
				while(nm8[rnd] === nm3[rnd3]){
					rnd3 = Math.floor(Math.random() * nm3.length);
				}
				while(nm3[rnd5] === nm3[rnd3]){
					rnd5 = Math.floor(Math.random() * nm3.length);
				}
				if(i < 8){
					names = nm8[rnd] + nm4[rnd2] + nm3[rnd3] + nm4[rnd4] + nm3[rnd5] + nm4[rnd6] + " " + nm7[rnd9];
				}else{
					rnd7 = Math.floor(Math.random() * nm3.length);
					rnd8 = Math.floor(Math.random() * nm4.length);
					while(nm3[rnd5] === nm3[rnd7]){
						rnd7 = Math.floor(Math.random() * nm3.length);
					}
					names = nm8[rnd] + nm4[rnd2] + nm3[rnd3] + nm4[rnd4] + nm3[rnd5] + nm4[rnd6] + nm3[rnd7] + nm4[rnd8] + " " + nm7[rnd9];
				}
			}
		}else{
			if(i < 6){
				rnd = Math.floor(Math.random() * nm1.length);
				rnd2 = Math.floor(Math.random() * nm2.length);
				rnd3 = Math.floor(Math.random() * nm3.length);
				rnd4 = Math.floor(Math.random() * nm2.length);
				rnd5 = Math.floor(Math.random() * nm3.length);
				rnd6 = Math.floor(Math.random() * nm2.length);
				while(nm3[rnd3] === nm1[rnd]){
					rnd3 = Math.floor(Math.random() * nm3.length);
				}
				while(nm3[rnd3] === nm3[rnd5]){
					rnd5 = Math.floor(Math.random() * nm3.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm3[rnd5] + nm2[rnd6] + ", " + nm7[rnd9];
			}else{
				rnd = Math.floor(Math.random() * nm8.length);
				rnd2 = Math.floor(Math.random() * nm4.length);
				rnd3 = Math.floor(Math.random() * nm3.length);
				rnd4 = Math.floor(Math.random() * nm4.length);
				rnd5 = Math.floor(Math.random() * nm3.length);
				rnd6 = Math.floor(Math.random() * nm4.length);
				while(nm8[rnd] === nm3[rnd3]){
					rnd3 = Math.floor(Math.random() * nm3.length);
				}
				while(nm3[rnd5] === nm3[rnd3]){
					rnd5 = Math.floor(Math.random() * nm3.length);
				}
				if(i < 8){
					names = nm8[rnd] + nm4[rnd2] + nm3[rnd3] + nm4[rnd4] + nm3[rnd5] + nm4[rnd6] + " " + nm7[rnd9];
				}else{
					rnd7 = Math.floor(Math.random() * nm3.length);
					rnd8 = Math.floor(Math.random() * nm4.length);
					while(nm3[rnd5] === nm3[rnd7]){
						rnd7 = Math.floor(Math.random() * nm3.length);
					}
					names = nm8[rnd] + nm4[rnd2] + nm3[rnd3] + nm4[rnd4] + nm3[rnd5] + nm4[rnd6] + nm3[rnd7] + nm4[rnd8] + " " + nm7[rnd9];
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