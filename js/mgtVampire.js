var nm1 = ["","","","","cr","ch","gr","k","kr","m","n","r","rh","s","sz","v","z"];
var nm2 = ["a","e","i","o","u","a","o"];
var nm3 = ["b","br","d","dr","dd","j","k","kh","l","lk","lv","lr","n","nk","nv","nz","rq","rk","rr","rv","rl","sk","sv","sz","v","vk","vz","vn","z","zk","zn","zl"];
var nm4 = ["c","d","k","n","r","t","v","w","z"];
var nm5 = ["","","","c","ch","g","k","n","s","sh","x"];

var nm6 = ["","","","","","d","dh","dr","g","gh","j","m","n","r","s","sh","th","v","z"];
var nm7 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","au","ia","ou","ai"];
var nm8 = ["d","dd","dn","dv","dz","fn","f","ff","fn","k","kh","kn","kv","l","lz","lv","lr","ln","lg","n","nv","ny","ng","nz","rv","ry","rn","rg","rz","vn","vl","vz","z","zn","zr","zl"];
var nm9 = ["g","l","m","n","r","t","z","v"];

var nm10 = ["ch","g","k","m","n","r","s","v","z"];
var nm11 = ["a","e","i","o","u","a","e","o"];
var nm12 = ["gd","gn","gv","gl","lv","lz","lg","ld","ng","nd","nv","nz","rg","rv","rz","ry","sg","sk","sz","sv","sd","vd","vg","vn","vz","zd","zg","zl","zn"];
var nm13 = ["g","l","n","r","v","z"];
var nm14 = ["d","dh","g","l","n","r","s","ss","sk","x"];

var nm15 = ["ash","beast","bitter","blaze","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","blood","bone","chain","chaos","cliff","cloud","coven","crag","cross","cull","dark","dawn","dead","death","dim","doom","down","dread","dusk","ember","fore","fury","gloom","glum","gore","grand","grim","haven","haze","hell","iron","lone","mist","mourn","nether","night","onyx","pale","pride","ruby","saur","shade","shadow","sky","storm","strom","swift","void","whit"];
var nm16 = ["bane","blade","blaze","blight","blood","bond","bone","born","bound","brand","burn","chief","claw","cloak","copse","crest","crown","curse","down","drawn","fall","fang","flaw","flow","force","forged","fury","gaze","gleam","glory","grog","gut","hall","haven","heart","hell","howl","hunter","husk","jaw","keeper","lash","line","mad","mane","mantle","mark","maul","maw","more","mourn","rage","root","run","seeker","shade","shadow","shard","shroud","song","spine","stalk","stalker","surge","sworn","thorn","throne","tide","tooth","way"];
var nm17 = ["arbiter","aristocrat","ascendant","assassin","barbarian","bloodchief","bloodlord","bloodseeker","bloodsucker","bloodsworn","brawler","bruiser","brute","butcher","captain","champion","chancellor","collector","condemned","crusader","cullblade","cutthroat","denizen","dreadknight","dreadlord","drinker","duelist","emissary","enigma","executioner","exterminator","feaster","fiend","gorger","harbinger","healer","heir","hexmage","highborn","horror","host","hunter","impaler","interloper","knight","lacerator","mage","marauder","mentor","merc","mercenary","nighthawk","nightmare","nightowl","nightwatch","noble","nocturnus","occulist","oracle","outcast","outrider","overseer","pariah","patrol","prophet","prowler","reaper","reaver","regent","reveler","revenant","ripper","ritualist","sage","savage","scourge","scout","seer","sentinel","servant","soothsayer","stalker","terror","thief","thrall","tormentor","torturer","tracker","traitor","tyrant","vampire","vanguard","visitor","warlord","watch","zealot"];

var nm18 = ["Aggressive","Agile","Agitated","Ancient","Arrogant","Asylum","Balcony","Balustrade","Bleak","Blind","Bloodied","Bold","Broken","Careless","Catacomb","Chosen","Corrupt","Corrupted","Courteous","Crafty","Crawling","Crimson","Crooked","Cruel","Crypt","Cursed","Dark","Defiant","Delirious","Discrete","Dusk","Eager","Energetic","Enraged","Eternal","Fearless","Feisty","Forsaken","Grave","Graveyard","Grim","Haunting","Hollow","Hopeless","Hungering","Hungry","Indulgent","Insatiable","Insolent","Juvenile","Lone","Lost","Loyal","Mad","Mania","Meek","Meger","Midnight","Mindless","Mysterious","Necropolis","Night","Nightmare","Nimble","Noxious","Obelisk","Powerful","Primal","Prime","Quick","Rapid","Rash","Ravenous","Reckless","Rooftop","Ruin","Ruthless","Sanguine","Shady","Silent","Skeletal","Sneaky","Soaked","Stalking","Stark","Swift","Thirsting","Tomb","Tombstone","Troubled","Twin","Vengeful","Vicious","Vile","Villainous","Void","Wicked","Wrathful","Wretched"];
var br = "";

function nameGen(type){
	var tp = type;
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnm = Math.random() * 4 | 0;
			rnd = Math.random() * nm10.length | 0;
			rnd2 = Math.random() * nm11.length | 0;
			rnd3 = Math.random() * nm14.length | 0;
			while(nm10[rnd] === nm14[rnd3]){
				rnd3 = Math.random() * nm14.length | 0;
			}
			if(rnm === 0){
				lName = nm10[rnd] + nm11[rnd2] + nm14[rnd3];
			}else if(rnm === 1){
				rnd4 = Math.random() * nm11.length | 0;
				rnd5 = Math.random() * nm12.length | 0;
				while(nm12[rnd5] === nm14[rnd3]){
					rnd3 = Math.random() * nm14.length | 0;
				}
				lName = nm10[rnd] + nm11[rnd2] + nm12[rnd5] + nm11[rnd4] + nm14[rnd3];
			}else{
				rnd4 = Math.random() * nm11.length | 0;
				rnd5 = Math.random() * nm12.length | 0;
				while(nm12[rnd5] === nm14[rnd3]){
					rnd3 = Math.random() * nm14.length | 0;
				}
				rnd6 = Math.random() * nm11.length | 0;
				rnd7 = Math.random() * nm13.length | 0;
				while(nm14[rnd3] === nm13[rnd7]){
					rnd7 = Math.random() * nm13.length | 0;
				}
				lName = nm10[rnd] + nm11[rnd2] + nm12[rnd5] + nm11[rnd4] + nm13[rnd7] + nm11[rnd6] + nm14[rnd3];
			}
			if(i < 6){
				rnd = Math.random() * nm6.length | 0;
				rnd2 = Math.random() * nm7.length | 0;
				rnd3 = Math.random() * nm8.length | 0;
				while(nm8[rnd3] === nm6[rnd]){
					rnd3 = Math.random() * nm8.length | 0;
				}
				rnd4 = Math.random() * nm7.length | 0;
				if(i < 3){
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + " " + lName;
				}else{
					rnd4 = Math.random() * nm9.length | 0;
					while(nm8[rnd3] === nm9[rnd4]){
						rnd4 = Math.random() * nm9.length | 0;
					}
					rnd5 = Math.random() * nm7.length | 0;
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd4] + nm7[rnd5] + " " + lName;
				}
			}else if(i < 8){
				rnd = Math.random() * nm15.length | 0;
				rnd2 = Math.random() * nm16.length | 0;
				rnd3 = Math.random() * nm17.length | 0;
				while(nm15[rnd] === nm16[rnd2] || nm15[rnd] + nm16[rnd2] === nm17[rnd3]){
					rnd2 = Math.random() * nm16.length | 0;
				}
				names = nm15[rnd] + nm16[rnd2] + " " + nm17[rnd3];
			}else{
				rnd = Math.random() * nm18.length | 0;
				rnd2 = Math.random() * nm17.length | 0;
				names = nm18[rnd] + " " + nm17[rnd2];
			}
		}else{
			rnm = Math.random() * 4 | 0;
			rnd = Math.random() * nm10.length | 0;
			rnd2 = Math.random() * nm11.length | 0;
			rnd3 = Math.random() * nm14.length | 0;
			while(nm10[rnd] === nm14[rnd3]){
				rnd3 = Math.random() * nm14.length | 0;
			}
			if(rnm === 0){
				lName = nm10[rnd] + nm11[rnd2] + nm14[rnd3];
			}else if(rnm === 1){
				rnd4 = Math.random() * nm11.length | 0;
				rnd5 = Math.random() * nm12.length | 0;
				while(nm12[rnd5] === nm14[rnd3]){
					rnd3 = Math.random() * nm14.length | 0;
				}
				lName = nm10[rnd] + nm11[rnd2] + nm12[rnd5] + nm11[rnd4] + nm14[rnd3];
			}else{
				rnd4 = Math.random() * nm11.length | 0;
				rnd5 = Math.random() * nm12.length | 0;
				while(nm12[rnd5] === nm14[rnd3]){
					rnd3 = Math.random() * nm14.length | 0;
				}
				rnd6 = Math.random() * nm11.length | 0;
				rnd7 = Math.random() * nm13.length | 0;
				while(nm14[rnd3] === nm13[rnd7]){
					rnd7 = Math.random() * nm13.length | 0;
				}
				lName = nm10[rnd] + nm11[rnd2] + nm12[rnd5] + nm11[rnd4] + nm13[rnd7] + nm11[rnd6] + nm14[rnd3];
			}
			if(i < 6){
				rnd = Math.random() * nm1.length | 0;
				rnd2 = Math.random() * nm2.length | 0;
				rnd3 = Math.random() * nm3.length | 0;
				rnd4 = Math.random() * nm2.length | 0;
				rnd5 = Math.random() * nm5.length | 0;
				while(nm3[rnd3] === nm1[rnd]){
					rnd3 = Math.random() * nm3.length | 0;
				}
				while(nm3[rnd3] === nm5[rnd5]){
					rnd5 = Math.random() * nm5.length | 0;
				}
				if(i < 3){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + " " + lName;
				}else{
					rnd6 = Math.random() * nm4.length | 0;
					rnd7 = Math.random() * nm2.length | 0;
					while(nm4[rnd6] === nm3[rnd3]){
						rnd6 = Math.random() * nm4.length | 0;
					}
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd4] + nm2[rnd7] + nm5[rnd5] + " " + lName;
				}
			}else if(i < 8){
				rnd = Math.random() * nm15.length | 0;
				rnd2 = Math.random() * nm16.length | 0;
				rnd3 = Math.random() * nm17.length | 0;
				while(nm15[rnd] === nm16[rnd2] || nm15[rnd] + nm16[rnd2] === nm17[rnd3]){
					rnd2 = Math.random() * nm16.length | 0;
				}
				names = nm15[rnd] + nm16[rnd2] + " " + nm17[rnd3];
			}else{
				rnd = Math.random() * nm18.length | 0;
				rnd2 = Math.random() * nm17.length | 0;
				names = nm18[rnd] + " " + nm17[rnd2];
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