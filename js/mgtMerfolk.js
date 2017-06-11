var nm1 = ["d","g","j","n","s","t","v","z"];
var nm2 = ["a","e","i","o","a","e","i","o","u"];
var nm3 = ["d","dd","dr","fr","fl","l","ll","lr","ln","n","nn","nd","r","rd","rz","rs","rv","t","tt","tr","y","z","zz"];
var nm4 = ["d","g","gg","l","n","nd","ng","t"];

var nm5 = ["","","","c","g","h","j","k","l","m","n","t","th"];
var nm6 = ["a","a","i","o","o","u"];
var nm7 = ["d","l","m","n","r","s","t","z"];
var nm8 = ["d","h","l","m","n","r","y"];

var nm9 = ["","","","","","b","d","g","k","m","n","r","v","z"];
var nm10 = ["a","e","a","e","a","e","a","e","o","i","u"];
var nm11 = ["d","dd","g","gg","l","ll","n","nn","r","rr","t","tt","z","zz"];
var nm12 = ["c","k","l","m","n","r"];

var nm13 = ["azure","blue","bright","clear","cloud","coral","coven","crystal","deep","depth","down","dream","fallow","fore","grand","gravel","haze","ink","keen","light","low","mellow","mer","mild","moon","night","ocean","orb","pale","prism","pure","razor","rip ","root","rough","sand","sea","shadow","shore","silver","soft","star","storm","strong","surge","swift","tidal","tide","void","wake","wander","water","wave","well","whit","wild","wind"];
var nm14 = ["bar","bend","bender","bind","binder","bough","bow","brand","breath","breeze","brine","brook","brooke","brow","caller","channel","crag","crash","creek","crest","dancer","dew","dream","dreamer","fallow","fathom","fin","flow","front","gabber","gill","glade","glide","helm","line","might","more","rider","ridge","river","sage","scape","seeker","shaper","shard","shine","sigh","singer","soar","spanner","spout","stand","stream","surge","sworn","tail","tide","trapper","tread","vigor","wake","ward","water","weaver","wine"];
var nm15 = ["Adept","Ambassador","Angler","Apothecary","Assassin","Bouncer","Commander","Disciple","Diver","Douser","Drowner","Elite","Entangler","Explorer","Fighter","Fluxmage","Guard","Guardian","Guide","Harbinger","Hero","Hunter","Hypnotist","Illusionist","Infiltrator","Knight","Legate","Mage","Mentor","Merchant","Merfolk","Mesmerist","Mystic","Patrol","Pilferer","Priest","Prophet","Raider","Rider","Sage","Scout","Scryer","Seer","Selkie","Sentinel","Shaman","Spy","Stalker","Summoner","Thief","Tracker","Trader","Trapper","Trasher","Triton","Visionary","Warrior","Watch","Weaver"];

var nm16 = ["Abyss","Abyssal","Agile","Arctic","Atoll","Azure","Barrier","Basin","Bay","Brave","Buoyant","Cape","Careful","Careless","Coral","Coven","Darting","Defiant","Depth","Diligent","Diving","Enclave","Energetic","Esteemed","Exalted","Expanse","Experienced","Fearless","Gifted","Glorious","Grand","Gulf","Harbor","Hasty","Intrepid","Jolting","Juvenile","Keen","Lagoon","Marine","Maritime","Nautical","Nimble","Oceanic","Prime","Prism","Radiant","Reckless","Reef","Salty","Shore","Slippery","Stark","Storm","Surf","Surfing","Surge","Swift","Tidal","Tide","Turbulent","Vicious","Vigilant","Void","Wake","Wave","Webbed","Wharf","Whirlpool","Wild","Zealous"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm9.length);
		rnd2 = Math.floor(Math.random() * nm10.length);
		rnd3 = Math.floor(Math.random() * nm12.length);
		if(i % 2 === 0){
			lName = nm9[rnd] + nm10[rnd2] + nm12[rnd3];
		}else{
			rnd4 = Math.floor(Math.random() * nm11.length);
			rnd5 = Math.floor(Math.random() * nm10.length);
			lName = nm9[rnd] + nm10[rnd2] + nm11[rnd4] + nm10[rnd5] + nm12[rnd3];
		}
		if(tp === 1){
			if(i < 6){
				rnd = Math.floor(Math.random() * nm5.length);
				rnd2 = Math.floor(Math.random() * nm6.length);
				rnd3 = Math.floor(Math.random() * nm7.length);
				rnd4 = Math.floor(Math.random() * nm6.length);
				if(i < 3){
					names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + " " + lName;
				}else{
					while(nm7[rnd3] === nm5[rnd]){
						rnd3 = Math.floor(Math.random() * nm7.length);
					}
					rnd5 = Math.floor(Math.random() * nm6.length);
					rnd6 = Math.floor(Math.random() * nm8.length);
					names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm8[rnd6] + nm6[rnd5] + " " + lName;
				}
			}else if(i < 8){
				rnd = Math.floor(Math.random() * nm13.length);
				rnd2 = Math.floor(Math.random() * nm14.length);
				while(nm13[rnd] === nm14[rnd2]){
					rnd2 = Math.floor(Math.random() * nm14.length);
				}
				rnd3 = Math.floor(Math.random() * nm15.length);
				names = nm13[rnd] + nm14[rnd2] + " " + nm15[rnd3];
			}else{
				rnd = Math.floor(Math.random() * nm15.length);
				rnd2 = Math.floor(Math.random() * nm16.length);
				names = nm15[rnd] + " " + nm16[rnd2];
			}
		}else{
			if(i < 6){
				rnd = Math.floor(Math.random() * nm1.length);
				rnd2 = Math.floor(Math.random() * nm2.length);
				rnd3 = Math.floor(Math.random() * nm4.length);
				if(i < 3){
					names = nm1[rnd] + nm2[rnd2] + nm4[rnd3] + " " + lName;
				}else{
					rnd4 = Math.floor(Math.random() * nm3.length);
					rnd5 = Math.floor(Math.random() * nm2.length);
					while(nm3[rnd4] === nm1[rnd]){
						rnd4 = Math.floor(Math.random() * nm3.length);
					}
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm2[rnd5] + nm4[rnd3] + " " + lName;
				}
			}else if(i < 8){
				rnd = Math.floor(Math.random() * nm13.length);
				rnd2 = Math.floor(Math.random() * nm14.length);
				while(nm13[rnd] === nm14[rnd2]){
					rnd2 = Math.floor(Math.random() * nm14.length);
				}
				rnd3 = Math.floor(Math.random() * nm15.length);
				names = nm13[rnd] + nm14[rnd2] + " " + nm15[rnd3];
			}else{
				rnd = Math.floor(Math.random() * nm15.length);
				rnd2 = Math.floor(Math.random() * nm16.length);
				names = nm15[rnd] + " " + nm16[rnd2];
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