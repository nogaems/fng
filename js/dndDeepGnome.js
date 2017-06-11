var nm1 = ["b","br","d","dr","fr","g","gh","gr","k","kh","kr","sch","schn","sn","sh","t","th","w","z","zh"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ie","ee","ai","aa","ei"];
var nm3 = ["ck","ckt","ckh","cn","dg","dl","ddl","dm","g","gg","gn","gl","ggl","kt","kth","kl","kn","lsch","lw","lth","lk","lkr","ltr","ll","ld","ldr","nth","nt","nd","ndr","ntr","rbl","rthm","rt","rdr","t","tt","tl","ttl","tr","thr","th"];
var nm4 = ["a","e","i","u"];
var nm5 = ["","","","c","ck","d","g","l","ll","ld","n","nd","nk","r","rs","t"];

var nm6 = ["","","","","","b","d","fr","gh","gr","h","k","kh","kr","l","m","n","s","sh","sn","sch","schn","t","th","y","w","z"];
var nm7 = ["a","e","i","u"];
var nm8 = ["ckn","d","dl","dd","g","gg","gd","gn","gh","l","ll","lg","lm","lv","ls","lsch","lsh","m","mk","mg","n","nn","nt","ny","ng","nk","rb","rg","rl","rsh","rv","rt","rth","rs","s","ss","sh","sn","sk","sg","sl","th","t","tr","thr","v","vr","vy","z"];
var nm9 = ["a","e","i","a","e","i","a","e","i","a","e","i","ee","ie","ei","ai","ia"];
var nm10 = ["d","dd","l","ll","ld","ln","lk","n","nn","r","rr","ry","rt","sh","sch"];
var nm11 = ["a","e","i","a","i","a","i"];
var nm12 = ["","","","","","","","d","dd","h","l","ll","n","nn","s","ss"];

var nm13 = ["adamant","agate","alabaster","alloy","amethyst","basalt","bedrock","block","boulder","brass","brick","bronze","clay","cobalt","cobble","copper","crag","crystal","deposit","diamond","dirt","dust","emerald","flint","fossil","garnet","gem","geo","geode","gold","granite","gravel","grime","ground","ingot","iron","jade","jewel","joint","lapis","lazuli","lead","lime","lodge","lump","marble","mason","metal","mill","mineral","mold","nickel","nugget","obsidian","onyx","opal","ore","pebble","pellet","peridot","pit","quartz","rock","rough","rubble","ruby","sand","sapphire","scrap","seam","shelf","silver","slab","slate","smelt","soil","spinel","steel","stone","stony","sturdy","terra","tile","tin","topaz","turf","wedge","wire","zinc","zircon"];
var nm14 = ["back","basher","bender","biter","bleacher","bone","bones","brander","breaker","bringer","browser","brusher","carrier","carver","catcher","checker","cheek","chest","chewer","chin","chiseler","cleaner","cleanser","collector","counter","crusher","cutter","designer","digger","duster","ear","eye","eyes","face","feet","finder","finger","fingers","fist","foot","forger","gatherer","gazer","getter","grasper","grinder","hand","head","heart","hewer","holder","knuckle","leg","legs","lifter","loader","maker","marker","mask","melter","mender","merger","molder","moulder","mug","neck","nose","packer","presser","pusher","rater","recorder","rinser","saver","scanner","scratcher","sealer","searcher","seeker","seizer","senser","shaper","shoveler","skin","smasher","smelter","snatcher","sniffer","sorter","splitter","stamper","stasher","stocker","surveyor","sweeper","switcher","teeth","temperer","tooth","trader","twirler","twister","vein","viewer","warper","watcher"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm13.length | 0;
		rnd2 = Math.random() * nm14.length | 0;
		nSr = nm13[rnd] + nm14[rnd2];
		if(tp === 1){
			nameFem();
			while(nMs === ""){
				nameFem();
			}
		}else{
			nameMas();
			while(nMs === ""){
				nameMas();
			}
		}
		nMs = nMs + " " + nSr;
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(nMs));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}

function nameFem(){
	rnd = Math.random() * nm6.length | 0;
	rnd2 = Math.random() * nm7.length | 0;
	rnd3 = Math.random() * nm8.length | 0;
	rnd4 = Math.random() * nm9.length | 0;
	if(i < 5){
		rnd5 = Math.random() * nm12.length | 0;
		if(rnd < 5 && rnd5 < 7){
			while(rnd5 < 7){
				rnd5 = Math.random() * nm12.length | 0;
			}
		}
		while(nm8[rnd3] === nm6[rnd] || nm8[rnd3] === nm12[rnd5]){
			rnd3 = Math.random() * nm8.length | 0;
		}
		nMs = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm9[rnd4] + nm12[rnd5];
	}else{
		rnd5 = Math.random() * nm10.length | 0;
		rnd6 = Math.random() * nm11.length | 0;
		while(nm10[rnd5] === nm8[rnd3] || nm8[rnd3] === nm6[rnd]){
			rnd3 = Math.random() * nm8.length | 0;
		}
		nMs = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm9[rnd4] + nm10[rnd5] + nm11[rnd6];
	}
	testSwear(nMs);
}

function nameMas(){
	rnd = Math.random() * nm1.length | 0;
	rnd2 = Math.random() * nm2.length | 0;
	rnd3 = Math.random() * nm3.length | 0;
	rnd4 = Math.random() * nm4.length | 0;
	rnd5 = Math.random() * nm5.length | 0;
	while(nm3[rnd3] === nm1[rnd] || nm3[rnd3] === nm5[rnd5]){
		rnd3 = Math.random() * nm3.length | 0;
	}
	nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm5[rnd5];
	testSwear(nMs);
}