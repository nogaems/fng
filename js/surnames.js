var nm1 = ["alpen","amber","ash","autumn","axe","barley","battle","bear","black","blade","blaze","blood","blue","bone","boulder","bright","bronze","burning","cask","chest","cinder","clan","claw","clear","cliff","cloud","cold","common","coven","crag","crest","crow","crystal","dark","dawn","day","dead","death","deep","dew","dirge","distant","doom","down","dragon","dream","dusk","dust","eagle","earth","elf","ember","even","fallen","far","farrow","feather","fern","fire","fist","flame","flat","flint","fog","fore","forest","four","free","frost","frozen","full","fuse","gloom","glory","glow","gold","gore","grand","grass","gray","great","green","grizzly","hallow","hallowed","hammer","hard","haven","hawk","haze","heart","heavy","hell","high","hill","holy","honor","horse","humble","hydra","ice","iron","keen","laughing","leaf","light","lightning","lion","lone","long","low","luna","marble","marsh","master","meadow","mild","mirth","mist","molten","monster","moon","morning","moss","mountain","mourn","mourning","nether","nickle","night","noble","nose","oat","ocean","orb","pale","peace","phoenix","pine","plain","pride","proud","pyre","rage","rain","rapid","raven","red","regal","rich","river","rock","rose","rough","rumble","rune","sacred","sage","saur","sea","serpent","shade","shadow","sharp","shield","silent","silver","simple","single","skull","sky","slate","smart","snake","snow","soft","solid","spider","spirit","spring","stag","star","steel","stern","still","stone","storm","stout","strong","summer","sun","swift","tall","tarren","terra","three","thunder","titan","tree","true","truth","tusk","twilight","two","void","war","water","wheat","whisper","whit","white","wild","willow","wind","winter","wise","wolf","wood","wooden","wyvern","young"];
var nm2 = ["arm","arrow","ash","axe","bane","bash","basher","beam","beard","belly","bend","bender","binder","blade","blaze","bleeder","blight","blood","bloom","blossom","blower","bluff","bone","bough","bow","brace","braid","branch","brand","breaker","breath","breeze","brew","bringer","brook","brooke","brow","caller","chaser","chewer","claw","cleaver","cloud","crag","creek","crest","crusher","cut","cutter","dancer","dane","dew","doom","down","draft","dream","dreamer","drifter","dust","eye","eyes","fall","fallow","fang","feather","fire","fist","flame","flare","flaw","flayer","flow","flower","follower","force","forest","forge","fury","gaze","gazer","gem","glade","gleam","glide","gloom","glory","glow","grain","grip","grove","guard","gust","hair","hammer","hand","heart","hell","helm","hide","horn","hunter","jumper","keep","keeper","killer","lance","lash","leaf","less","light","mane","mantle","mark","maul","maw","might","moon","more","mourn","oak","orb","ore","peak","pelt","pike","punch","rage","reaper","reaver","rider","ridge","ripper","river","roar","rock","root","run","runner","scar","scream","scribe","seeker","shade","shadow","shaper","shard","shield","shine","shot","shout","singer","sky","slayer","snarl","snout","snow","soar","song","sorrow","spark","spear","spell","spire","spirit","splitter","sprinter","stalker","star","steam","steel","stone","stream","strength","stride","strider","strike","striker","sun","surge","swallow","swift","sword","sworn","tail","taker","talon","thorn","thorne","tide","toe","track","trap","trapper","tree","vale","valor","vigor","walker","ward","watcher","water","weaver","whirl","whisk","whisper","willow","wind","winds","wing","wolf","wood","woods","wound"];
var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		while(nm1[rnd] === nm2[rnd2]){
			rnd2 = Math.floor(Math.random() * nm2.length);
		}
		names = nm1[rnd] + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}