var nm1 = ["a","o","","","","","","","",""];
var nm2 = ["b","d","g","l","ll","m","n","r","t","v"];
var nm3 = ["a","o","a","o","a","o","a","o","a","o","u","e","i"];
var nm4 = ["c","d","dh","g","kh","l","ll","n","nn","s","ss","sh","t","th","tt","v","w","z","zh"];
var nm5 = ["d","l","m","n","t","th"];

var nm6 = ["Abandoned","Acclaimed","Aggressive","Agitated","Ambitious","Ancient","Bitter","Bold","Broken","Callous","Careless","Cautious","Corrupt","Corrupted","Crooked","Cruel","Dangerous","Defiant","Delirious","Deserted","Devoted","Diligent","Discrete","Dreary","Eager","Enraged","Evil","Fearless","Fickle","Forsaken","Frightening","Grand","Grave","Grim","Gruesome","Haunting","Hideous","Husky","Infernal","Juvenile","Keen","Livid","Loathsome","Lone","Lost","Lumbering","Mad","Mindless","Monstrous","Nasty","Needy","Noxious","Obedient","Petty","Powerful","Prime","Ragged","Rash","Reckless","Somber","Spiteful","Trifling","Turbulent","Unfit","Useless","Vicious","Villainous","Violent","Weak","Wicked","Wild","Woeful","Wrathful","Wretched","Zealous"];
var nm7 = ["Agent","Aristocrat","Broker","Bully","Chandler","Charmer","Conjurer","Dealer","Defacer","Diviner","Escort","Explorer","Guard","Guardian","Illusionist","Informer","Lookout","Looter","Mage","Marauder","Mediator","Merchant","Monger","Negotiator","Noble","Operative","Oppressor","Outrider","Overlord","Overseer","Patrician","Patrol","Pillager","Pioneer","Plunderer","Ravager","Recruiter","Retailer","Sage","Scout","Sentinel","Sneak","Soothsayer","Spellbinder","Spoiler","Spy","Taskmaster","Trader","Tyrant","Vandal","Vanguard","Vendor","Watcher"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd7 = Math.floor(Math.random() * nm6.length);
		rnd8 = Math.floor(Math.random() * nm7.length);
		if(i < 6){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm4.length);
			while(nm2[rnd2] === nm4[rnd4]){
				rnd4 = Math.floor(Math.random() * nm4.length);
			}
			rnd5 = Math.floor(Math.random() * nm3.length);
			rnd6 = Math.floor(Math.random() * nm5.length);
			while(nm5[rnd6] === nm4[rnd4]){
				rnd6 = Math.floor(Math.random() * nm5.length);
			}
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm3[rnd5] + nm5[rnd6] + ", " + nm6[rnd7] + " " + nm7[rnd8];
		}else{
			names = nm6[rnd7] + " " + nm7[rnd8];
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