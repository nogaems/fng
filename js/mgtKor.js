var nm1 = ["g","h","l","m","n","t","d","y","b","z"];
var nm2 = ["a","e","o","u"];
var nm3 = ["b","bb","bh","d","dd","dh","lb","ld","lg","ln","md","ml","m","mm","n","nd","nn","ng","nk","nl","nm"];
var nm4 = ["","","","","","","","l","n","r","y"];

var nm5 = ["f","h","l","n","t","v","y"];
var nm6 = ["a","e","i"];
var nm7 = ["hn","hl","hm","l","lm","ln","ly","lf","ll","mn","m","mm","mh","my","mw","n","ny","nm","nh","nw","ph","phr","phl","sh","sl","sn","sm","st","th","thn","thl","thy","yl","yn"];

var nm8 = ["Aged","Ambush","Ancient","Armament","Austere","Bold","Brilliant","Cruel","Defiant","Dependent","Devoted","Devout","Diligent","Discrete","Dutiful","Eager","Eternal","Exalted","Fearless","Feline","Forsaken","Ghostly","Gifted","Glorious","Grand","Great","Grim","Hollow","Honored","Illustrious","Intrepid","Juvenile","Kor","Lone","Lost","Loyal","Mellow","Minor","Monstrous","Nocturnal","Obedient","Outlandish","Powerful","Prime","Rapid","Reckless","Relief","Rigid","Selfish","Shadow","Shadowy","Shady","Silent","Sneaky","Sniveling","Somber","Spirited","Swift","Vengeful","Vicious","Vigilant","Violent","Wicked","Wild","Wrathful","Wretched"];
var nm9 = ["Aeronaut","Apprentice","Artisan","Augur","Blademaster","Brawler","Bruiser","Burglar","Captain","Champion","Cleric","Commander","Dancer","Diviner","Duelist","Enchanter","Explorer","Fighter","Firewalker","Glider","Guard","Guardian","Guide","Harbinger","Herald","Hero","Hookmaster","Infiltrator","Leader","Lookout","Medic","Mercenary","Missionary","Mole","Mystic","Navigator","Neophyte","Oracle","Outfitter","Pilgrim","Protector","Prowler","Ringleader","Sage","Sanctifier","Scout","Scythemaster","Sear","Seer","Sentinel","Shieldmate","Soothsayer","Specialist","Spiritdancer","Spy","Tender","Thief","Vanguard","Wanderer","Warrior","Watcher","Wildcat"];

var nm10 = ["alder","amber","barren","bitter","boulder","cinder","coven","crest","dark","dawn","deep","dew","down","dream","dusk","elm","ember","fall","farrow","fist","flame","flint","fore","free","frost","gloom","grand","gray","great","hard","haven","high","keen","kind","light","lone","long","meadow","mirth","mist","moon","mourn","night","plain","pride","proud","rapid","regal","river","rough","shade","shadow","silent","silken","silver","simple","single","solid","soul","spring","stern","stone","storm","tall","thunder","vine","water","whit","wild"];
var nm11 = ["bane","beam","bend","blaze","bluff","bough","bound","brace","branch","brand","breeze","brook","brooke","brow","call","copse","crag","crest","dane","down","fall","fist","flaw","flow","force","forge","fury","gaze","glade","glare","grove","guard","heart","helm","husk","keep","lance","lash","lock","mane","mantle","mark","more","mourne","ridge","root","run","shade","shard","shot","soar","song","spine","spire","stalk","stand","stride","surge","sworn","thorn","thorne","track","vale"];

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
				rnd6 = Math.floor(Math.random() * nm9.length);
				while(nm7[rnd3] === nm5[rnd]){
					rnd3 = Math.floor(Math.random() * nm7.length);
				}
				names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + ", " + nm8[rnd5] + " " + nm9[rnd6];
			}else if(i < 8){
				rnd = Math.floor(Math.random() * nm8.length);
				rnd2 = Math.floor(Math.random() * nm9.length);
				names = nm8[rnd] + " " + nm9[rnd2];
			}else{
				rnd = Math.floor(Math.random() * nm10.length);
				rnd2 = Math.floor(Math.random() * nm11.length);
				while(nm10[rnd] === nm11[rnd2]){
					rnd2 = Math.floor(Math.random() * nm11.length);
				}
				rnd3 = Math.floor(Math.random() * nm9.length);
				names = nm10[rnd] + nm11[rnd2] + " " + nm9[rnd2];
			}
		}else{
			if(i < 6){
				rnd = Math.floor(Math.random() * nm1.length);
				rnd2 = Math.floor(Math.random() * nm2.length);
				rnd3 = Math.floor(Math.random() * nm3.length);
				rnd4 = Math.floor(Math.random() * nm2.length);
				rnd1 = Math.floor(Math.random() * nm4.length);
				rnd5 = Math.floor(Math.random() * nm8.length);
				rnd6 = Math.floor(Math.random() * nm9.length);
				while(nm3[rnd3] === nm1[rnd]){
					rnd3 = Math.floor(Math.random() * nm3.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd1] + ", " + nm8[rnd5] + " " + nm9[rnd6];
			}else if(i < 8){
				rnd = Math.floor(Math.random() * nm8.length);
				rnd2 = Math.floor(Math.random() * nm9.length);
				names = nm8[rnd] + " " + nm9[rnd2];
			}else{
				rnd = Math.floor(Math.random() * nm10.length);
				rnd2 = Math.floor(Math.random() * nm11.length);
				while(nm10[rnd] === nm11[rnd2]){
					rnd2 = Math.floor(Math.random() * nm11.length);
				}
				rnd3 = Math.floor(Math.random() * nm9.length);
				names = nm10[rnd] + nm11[rnd2] + " " + nm9[rnd2];
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