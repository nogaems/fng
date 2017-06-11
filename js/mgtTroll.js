var nm1 = ["b","bh","br","d","dh","dr","g","gh","gr","kh","khr","r","th","tr","thr","v","z","zh"];
var nm2 = ["u","u","u","u","u","o","a"];
var nm3 = ["b","bv","bb","bl","d","dd","dr","dv","dz","g","gg","gl","gn","gv","gz","k","kk","kl","kv","lb","ld","lg","l","ll","ln","lr","lt","lz","lv","m","md","mg","ml","mr","mz","nd","nv","nz","nl","nd","ndr","ng","ngr","ngb","ngz","r","rr","rl","rv","rz","v","vl","vn","z","zd","zg","zl","zn"];
var nm4 = ["c","d","g","l","lg","ld","n","ng","nd","rd","rg"];

var nm5 = ["amber","ash","bitter","blaze","blunt","bone","boulder","brick","bristle","broad","cave","cinder","claw","crag","dim","dirge","dust","far","fern","flask","flint","fog","fore","forge","gloom","grand","gravel","grim","heavy","hill","horn","keen","krag","lone","low","moss","mourn","mud","oat","orb","pale","pyre","rend","saur","shadow","skull","sky","slate","snake","spore","stone","tall","terra","tree","tusk","whit","wild"];
var nm6 = ["back","bane","beam","belly","belt","bend","blade","blight","bough","braid","branch","brand","breath","brew","bridge","brow","claw","crag","crest","flare","flaw","force","fury","gaze","grip","grog","gut","hide","hood","horn","howl","husk","jaw","lance","lash","limb","lock","mane","mark","maw","scar","scrub","shard","shroud","snarl","spine","stride","strike","stub","surge","toe","trap"];
var nm7 = ["Aggressor","Assailant","Barbarian","Battler","Brawler","Bruiser","Brute","Bully","Castaway","Degenerate","Derelict","Exile","Fiend","Hireling","Merc","Mercenary","Outcast","Sadist","Savage","Scrapper","Shaman","Slugger","Troll","Troll","Troll","Troll","Troll","Troll","Troll","Troll","Troll","Troll","Troll","Troll","Troll","Trow","Trow","Trow","Trow","Trow","Trow","Vagabond","Vagrant","Warrior","Wildcat","Wildling","Wretch"];

var nm8 = ["Abandoned","Aching","Aged","Aggressive","Albino","Ancient","Angry","Anxious","Arctic","Bitter","Blind","Bony","Broken","Bruised","Bush","Careless","Cave","Cavern","Charging","Clever","Clueless","Clumsy","Colossal","Confused","Corrupt","Corrupted","Crafty","Crooked","Cruel","Defiant","Diligent","Dull","Eager","Elder","Enraged","Fearless","Feisty","Fickle","Forest","Forsaken","Fungus","Gloomy","Grave","Greedy","Grim","Grotesque","Harvester","Haunting","Hedge","Hidden","Horned","Hungry","Hunting","Jaded","Jungle","Juvenile","Lanky","Limping","Lone","Lost","Lumbering","Marsh","Meager","Mountain","Noxious","Numb","Oblivious","Ocean","Powerful","Primal","Prime","Pygmy","Rash","Reckless","River","Sea","Selfish","Shady","Shameless","Skinny","Sneaking","Sneaky","Sniveling","Swamp","Swift","Troubled","Twin","Vicious","Vile","Wicked","Wrathful","Wretched"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm4.length | 0;
			while(nm4[rnd3] === nm1[rnd]){
				rnd3 = Math.random() * nm4.length | 0;
			}
			if(i < 3){
				names = nm1[rnd] + nm2[rnd2] + nm4[rnd3];
			}else{
				rnd4 = Math.random() * nm3.length | 0;
				rnd5 = Math.random() * nm2.length | 0;
				while(nm4[rnd3] === nm3[rnd4]){
					rnd4 = Math.random() * nm3.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm2[rnd5] + nm4[rnd3];
			}
		}else if(i < 8){
			rnd = Math.random() * nm5.length | 0;
			rnd2 = Math.random() * nm6.length | 0;
			while(nm5[rnd] === nm6[rnd2]){
				rnd2 = Math.random() * nm6.length | 0;
			}
			rnd3 = Math.random() * nm7.length | 0;
			names = nm5[rnd] + nm6[rnd2] + " " + nm7[rnd3];
		}else{
			rnd = Math.random() * nm8.length | 0;
			rnd2 = Math.random() * nm7.length | 0;
			names = nm8[rnd] + " " + nm7[rnd2];
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