var nm1 = ["b","ch","cr","dr","d","j","g","k","kr","r","sk","sr","sg","sc","v"];
var nm2 = ["a","u","a","u","o","e","a","u","a","u","o","e","a","u","a","u","o","e","ou"];
var nm3 = ["d","dr","g","gg","gr","gv","h","k","kk","kr","kdr","kv","kd","kl","n","nn","ndr","nr","ng","nk","rr","rk","rg","rrg","rt","rv","zg","zk","zr"];
var nm4 = ["c","d","k","l","n","rg","rd"];

var nm5 = ["amber","ash","axe","axel","barren","battle","bitter","blaze","blood","bone","boon","boulder","cinder","cold","cruel","dark","dawn","deep","dire","doom","down","durk","ember","far","fir","fist","flesh","flow","frost","full","fury","gloom","gore","grand","grave","great","hammer","hard","haze","heart","hearth","hell","high","hill","ice","keen","lair","loam","lone","low","mad","marsh","molten","nether","night","pale","rage","rough","shade","shadow","sharp","shatter","skull","sky","solid","splinter","star","stern","stone","storm","stout","strong","taint","thunder","wild"];
var nm6 = ["bane","bark","basher","beard","bellow","bleeder","blower","bough","brace","breaker","breath","bringer","brow","cage","chaser","chewer","cleaver","cloud","comber","crag","crest","crusher","cutter","doom","dozer","dragger","drinker","fall","fire","fist","flaw","flayer","follower","fray","fury","grave","grinder","grip","grove","growl","guard","hammer","hand","heim","hewer","hold","land","mark","maul","mist","pulper","rage","raker","reaper","reaver","ridge","ripper","roar","seeker","shield","shock","shot","shroud","skull","snarl","sorrow","splinter","splitter","stalker","stoke","stone","stride","strider","striker","sworn","thorn","trunk","wake","ward","watch","watcher","weaver","wood"];
var nm7 = ["Behemoth","Colossus","Cyclops","Giant","Goliath","Titan"];

var nm8 = ["abandoned","aged","agile","amber","ancient","angry","arctic","armory","ash","average","barren","battle","bitter","blaze","blind","blood","bold","bone","border","bossy","boulder","broken","bruised","caravan","carefree","careless","chief","cinder","clever","clumsy","craven","cruel","daring","dark","dawn","deep","defiant","desolation","dim","dire","dirty","doom","ember","far","fearless","focused","forsaken","free","frost","frosty","fury","gentle","gloom","gore","grand","grave","great","greedy","grim","hard","heavy","hell","high","hill","hungry","ice","idle","intrepid","lair","last","limping","lone","low","lumpy","mad","marsh","molten","monstrous","nether","night","oblivious","pale","powerful","prime","pyre","rage","remote","selfish","shadow","silent","stark","stone","storm","swift","thunder","vengeful","vigilant","wild"];
var nm9 = ["Bearer","Behemoth","Brute","Butcher","Champion","Colossus","Crusher","Custodian","Cyclops","Drifter","Enforcer","Explorer","Giant","Goliath","Graybeard","Grunt","Guard","Guardian","Harbinger","Heavyweight","Intimidator","Keeper","Legionnaire","Meanderer","Mentor","Nomad","Oaf","Overseer","Pilgrim","Protector","Ranger","Recruit","Roamer","Savage","Scout","Sentinel","Shaman","Shepherd","Slavedriver","Stroller","Taskmaster","Titan","Traveler","Tyrant","Vagabond","Valleymaker","Wanderer","Warchief","Warden","Watcher"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm2.length);
			rnd5 = Math.floor(Math.random() * nm4.length);
			while(nm3[rnd3] === nm1[rnd]){
				rnd3 = Math.floor(Math.random() * nm3.length);
			}
			while(nm3[rnd3] === nm4[rnd5]){
				rnd5 = Math.floor(Math.random() * nm4.length);
			}
			if(i < 2){
				names = nm1[rnd] + nm2[rnd2] + nm4[rnd5];
			}else{
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
			}
		}else if(i < 8){
			rnd = Math.floor(Math.random() * nm5.length);
			rnd2 = Math.floor(Math.random() * nm6.length);
			while(nm5[rnd] === nm6[rnd2]){
				rnd2 = Math.floor(Math.random() * nm6.length);
			}
			rnd3 = Math.floor(Math.random() * nm7.length);
			names = nm5[rnd] + nm6[rnd2] + " " + nm7[rnd3];
		}else{
			rnd = Math.floor(Math.random() * nm8.length);
			rnd2 = Math.floor(Math.random() * nm9.length);
			names = nm8[rnd] + " " + nm9[rnd2];
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