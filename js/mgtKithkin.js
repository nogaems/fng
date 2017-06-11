var nm1 = ["b","g","h","m","n","r","s","v","z"];
var nm2 = ["a","o","e","i","u","a","o"];
var nm3 = ["b","bb","d","dd","l","ll","lr","lm","ln","m","mm","mn","mr","ml","n","nn","nm","nd","nl","nt","nr","nz","r","rr","rl","rd","rb","rv","rz","v","vr","vl"];
var nm4 = ["c","ck","d","g","k","t","z"];

var nm5 = ["b","br","d","dr","g","n","s","v","w","z"];
var nm6 = ["e","i","e","i","a","o"];
var nm7 = ["c","ch","g","j","l","ll","n","nn","r","rl","rs","rv","rw","sr","str","sg","sl","sm","sn","tr","thr","ts","z","zz","zg","zl"];
var nm8 = ["d","f","h","n","t","th"];

var nm9 = ["d","k","l","m","n","r","t","z"];
var nm10 = ["ee","ie","ia","ea","ei","ai","oo"];
var nm11 = ["c","g","j","k","l","p","z"];

var nm12 = ["alder","amber","bally","bare","barren","blan","bon","bri","bright","burren","char","cin","cinder","cloud","col","cold","crest","dawn","day","dew","dusk","ember","even","far","fir","fog","fore","glum","gold","grin","haze","hazel","hil","hill","keen","kin","kins","ligh","light","lon","lone","long","low","marsh","mil","mild","mist","moon","moss","nettle","night","plain","rain","rose","sage","saur","shade","shadow","snow","spring","stone","stout","sun","tall","thistle","whit","wil"];
var nm13 = ["baile","ban","beam","bend","blossom","bluff","bough","bow","brace","bramble","branch","brand","breeze","bron","brook","brooke","brow","caer","copse","crag","crest","dane","dew","down","fall","flaw","flow","for","forest","gaze","gem","glade","gleam","glide","glow","grove","gust","heart","jack","keep","leaf","less","lock","mane","mark","maw","meadow","moon","more","nock","nut","pad","ridge","river","root","run","scaer","shade","shadow","shine","snow","song","spark","spell","spine","spire","sprout","spur","stand","star","tide","ton","vale","ward","wind"];
var nm14 = ["Adept","Alchemist","Balloonist","Bombardier","Bomber","Borderguard","Captain","Cavalier","Champion","Cleric","Cohort","Dodger","Escort","Explorer","Guard","Guardian","Guide","Harbinger","Harpoonist","Harrier","Healer","Hero","Initiate","Kithkin","Knight","Liege","Lookout","Mage","Medic","Mentor","Patrol","Pioneer","Recruiter","Rogue","Runner","Sage","Scout","Seeker","Sentinel","Shepherd","Shield-Bearer","Skirmisher","Soldier","Spellduster","Spy","Squad","Stalwart","Tactician","Tender","Trapper","Vanguard","Warrior","Watch","Watcher","Witch","Zealot"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd12 = Math.floor(Math.random() * nm2.length);
		if(tp === 1){
			if(i < 6){
				rnd = Math.floor(Math.random() * nm5.length);
				rnd2 = Math.floor(Math.random() * nm6.length);
				rnd3 = Math.floor(Math.random() * nm7.length);
				rnd4 = Math.floor(Math.random() * nm6.length);
				rnd5 = Math.floor(Math.random() * nm8.length);
				while(nm7[rnd3] === nm5[rnd]){
					rnd3 = Math.floor(Math.random() * nm7.length);
				}
				rnd6 = Math.floor(Math.random() * nm9.length);
				rnd7 = Math.floor(Math.random() * nm10.length);
				rnd8 = Math.floor(Math.random() * nm11.length);
				names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm8[rnd5] + " " + nm9[rnd6] + nm10[rnd7] + nm11[rnd8];
			}else{
				rnd = Math.floor(Math.random() * nm12.length);
				rnd2 = Math.floor(Math.random() * nm13.length);
				while(nm12[rnd] === nm13[rnd2]){
					rnd2 = Math.floor(Math.random() * nm13.length);
				}
				rnd3 = Math.floor(Math.random() * nm14.length);
				names = nm12[rnd] + nm13[rnd2] + " " + nm14[rnd3];
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
				rnd6 = Math.floor(Math.random() * nm9.length);
				rnd7 = Math.floor(Math.random() * nm10.length);
				rnd8 = Math.floor(Math.random() * nm11.length);
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5] + " " + nm9[rnd6] + nm10[rnd7] + nm11[rnd8];
			}else{
				rnd = Math.floor(Math.random() * nm12.length);
				rnd2 = Math.floor(Math.random() * nm13.length);
				while(nm12[rnd] === nm13[rnd2]){
					rnd2 = Math.floor(Math.random() * nm13.length);
				}
				rnd3 = Math.floor(Math.random() * nm14.length);
				names = nm12[rnd] + nm13[rnd2] + " " + nm14[rnd3];
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