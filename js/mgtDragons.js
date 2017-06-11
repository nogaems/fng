var nm1 = ["","","","","","b","br","cr","d","dr","j","k","kr","n","p","pr","r","s","sk","t","v","z"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","aa","uu","ae","au"];
var nm3 = ["c","g","k","l","ll","lt","ld","m","mn","n","nn","nd","nt","r","rt","rk","rd","th","s","sh","v","z"];
var nm4 = ["ct","d","dr","dg","g","gr","gd","gh","kt","kd","ld","lg","lt","lgr","lk","mg","mk","r","rg","rk","rd","sk","sg"];
var nm5 = ["b","n","r","s","ss","ssh","t","th","x","z"];

var nm6 = ["","","","","","c","d","dr","g","k","kh","n","r","s","t","th","tr","y"];
var nm7 = ["a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","ei","ai","ae"];
var nm8 = ["d","g","j","k","m","n","r","s","sh","t","th","v","z"];
var nm9 = ["c","d","dr","g","gn","gr","k","kl","kr","r","rr","rk","rt","s","ss","sh","t","th"];

var nm10 = ["amber","arcane","ash","ashen","bale","battle","bell","blade","blaze","bolt","breeze","bright","burning","cinder","crystal","dark","dawn","death","doom","dream","ember","ever","fire","flame","forge","fury","fuse","gore","grand","haze","hell","high","hollow","ice","light","lightning","lone","molten","mourn","necro","night","prey","pyre","rage","rime","rune","saur","shadow","shield","shock","silent","storm","sun","thunder","titan","twilight","vent","void","war","ward","wild"];
var nm11 = ["bane","bellow","belly","bend","binder","blaze","blight","born","bough","brand","break","breaker","breath","bringer","brow","burn","burner","chewer","claw","crest","crown","crusher","dancer","draft","drift","drifter","fall","fang","fire","flame","flare","flow","force","forge","fury","glade","glide","grip","heart","hide","horn","kite","lash","mane","master","maw","more","mourn","rage","reaver","roar","scale","scales","scar","scorch","seizer","shadow","shard","shield","slayer","soar","spark","spine","spire","stalk","steel","stoker","storm","surge","sworn","talon","toll","ward","wing"];
var nm12 = ["Behemoth","Brood","Charger","Despot","Dragon","Dragon","Dragon","Dragon","Dragon","Dragon","Dragon","Dragonlord","Dragonlord","Dragonlord","Dragonlord","Guardian","Heir","Hunter","Igniter","Marauder","Oppressor","Pillager","Predator","Raider","Ravager","Regent","Scion","Scourge","Sentinel","Sentry","Skyraider","Sovereign","Stalker","Titan","Tormentor","Tyrant","Warmonger","Worldgorger"];

var nm13 = ["Aged","Agile","Alabaster","Anchored","Ancient","Belated","Bitter","Blight","Blind","Bold","Brimstone","Broken","Bronze","Bruised","Canopy","Careless","Catacomb","Clockwork","Cloud","Colossal","Corrupt","Corrupted","Covetous","Crimson","Crooked","Cruel","Crypt","Crystal","Cunning","Deafening","Defiant","Delirious","Diligent","Dream","Dreary","Drifting","Elated","Elder","Enchanted","Enduring","Enraged","Eternal","Exalted","Fearless","Fickle","Fire","Flame","Fog","Forge","Forsaken","Furnace","Fury","Gargantuan","Giant","Gigantic","Glorious","Grand","Grave","Grim","Grounded","Grumpy","Hateful","Heavenly","Hell","Hollow","Honored","Humongous","Hypersonic","Infernal","Inferno","Infinity","Iron","Juvenile","Light","Lightning","Lone","Lost","Lunar","Mad","Majestic","Mist","Moon","Mysterious","Nocturnal","Obedient","Phantasmal","Powerful","Predator","Primal","Prime","Pristine","Proud","Quick","Quicksilver","Radiant","Rapid","Reckless","Ruthless","Sadistic","Sanguine","Savage","Scornful","Selfish","Shady","Siege","Silent","Silver","Snarling","Solar","Spellbound","Spiteful","Stark","Steel","Storm","Sun","Supersonic","Swift","Thunder","Thunderous","Tomb","Turbulent","Twin","Vain","Venerated","Vengeful","Vicious","Villainous","Violent","Volcanic","Whirlwind","Wicked","Wild","Wrathful"];

var br = "";

function nameGen(type){
	var tp = type;
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i % 2 === 0){
			rnd = Math.random() * nm10.length | 0;
			rnd2 = Math.random() * nm11.length | 0;
			while(nm10[rnd] === nm11[rnd2]){
				rnd2 = Math.random() * nm11.length | 0;
			}
			rnd3 = Math.random() * nm12.length | 0;
			lName = nm10[rnd] + nm11[rnd2] + " " + nm12[rnd3];
		}else{
			rnd = Math.random() * nm13.length | 0;
			rnd2 = Math.random() * nm12.length | 0;
			lName = nm13[rnd] + " " + nm12[rnd2];
		}
		if(tp === 1){
			if(i < 6){
				rnd = Math.random() * nm6.length | 0;
				rnd2 = Math.random() * nm7.length | 0;
				rnd3 = Math.random() * nm8.length | 0;
				rnd4 = Math.random() * nm7.length | 0;
				while(nm8[rnd3] === nm6[rnd]){
					rnd = Math.random() * nm6.length | 0;
				}
				if(i < 3){
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + ", " + lName;
				}else{
					rnd5 = Math.random() * nm9.length | 0;
					rnd6 = Math.random() * nm7.length | 0;
					while(nm9[rnd5] === nm8[rnd3]){
						rnd5 = Math.random() * nm9.length | 0;
					}
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd5] + nm7[rnd6] + ", " + lName;
				}
			}else{
				names = lName;
			}
		}else{
			if(i < 6){
				rnd = Math.random() * nm1.length | 0;
				rnd2 = Math.random() * nm2.length | 0;
				rnd3 = Math.random() * nm3.length | 0;
				rnd4 = Math.random() * nm2.length | 0;
				rnd5 = Math.random() * nm5.length | 0;
				while(nm3[rnd3] === nm1[rnd]){
					rnd = Math.random() * nm1.length | 0;
				}
				while(nm3[rnd3] === nm5[rnd5]){
					rnd5 = Math.random() * nm5.length | 0;
				}
				if(i < 3){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + ", " + lName;
				}else{
					rnd6 = Math.random() * nm4.length | 0;
					rnd7 = Math.random() * nm2.length | 0;
					while(nm4[rnd6] === nm5[rnd5]){
						rnd6 = Math.random() * nm4.length | 0;
					}
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5] + ", " + lName;
				}
			}else{
				names = lName;
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