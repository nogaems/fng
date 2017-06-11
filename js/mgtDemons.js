var nm1 = ["","","","","c","g","k","m","l","n","r","s","sh","y","t","th","z"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","yo","ei","ai","iu","aa"];
var nm3 = ["d","f","g","k","m","r","sh","th","x","z","d","f","g","k","m","r","sh","th","x","z","d","dd","dr","d'c","f","f'g","g","gr","gn","gd","k","kd","k'k","kr","kk","kz","k'z","lf","l'k","lg","l'g","l'd","ld","lr","l'c","lc","lt","l't","m","mm","r","r'z","rz","rr","rg","rs","r's","rm","shr","sh","sr","th","x","z","zr","zh","z'l","z'g"];
var nm4 = ["d","g","l","ld","lg","ll","m","n","ng","nd","nn","ph","r","rr","s","ss","sh","ts"];
var nm5 = ["","","","c","d","hl","l","n","r","s","x"];

var nm6 = ["abyss","ache","ash","blaze","blood","cinder","crypt","dark","dead","death","doom","dust","ember","fire","flame","gloom","gore","grave","grief","grim","haze","hell","hollow","mind","nether","night","pain","pit","pyre","rue","ruin","shadow","skull","soot","sore","sorrow","soul","tomb","vault","woe"];
var nm7 = ["bane","basher","bellow","binder","blade","blaze","blight","born","brand","breaker","bringer","cage","carver","claw","cleaver","cloak","cloaked","crest","dealer","drifter","fall","fang","flayer","forge","forged","fury","gaze","gift","heart","horn","lash","mane","maul","maw","more","mourn","rage","reaper","reaver","rider","ridge","ripper","scar","shard","slayer","spine","stalk","stalker","stride","strike","striker","surge","sworn","wing","wracker","wreck","wrecker"];
var nm8 = ["Overlord","Pitlord","Persecutor","Archdemon","Demon","Archfiend","Archlord","Overlord","Pitlord","Persecutor","Archdemon","Demon","Archfiend","Archlord","Annihilator","Archdemon","Archfiend","Archlord","Beast","Befouler","Defiler","Demolisher","Demon","Demonlord","Desecrator","Despoiler","Destroyer","Devourer","Eradicator","Exterminator","Fiend","Harvester","Hellion","Herald","Hunter","Infernal","Lord","Marauder","Minion","Monster","Overlord","Overseer","Persecutor","Perverter","Pilferer","Pitlord","Ravager","Reaper","Renegade","Scourge","Servant","Slaughterer","Spawn","Stalker","Taskmaster","Tyrant","Violator"];

var nm9 = ["Abhorrent","Abyssal","Aggravated","Ancient","Angry","Anguish","Anguished","Bellowing","Bitter","Bone","Bony","Broken","Burly","Cackling","Chaos","Colossal","Corrupt","Corrupted","Crooked","Cruel","Crypt","Damned","Dangerous","Dark","Deadly","Defiant","Delirious","Diligent","Dire","Disgusting","Dismal","Dread","Dreary","Enormous","Enraged","Evil","Fallen","Fearless","Ferocious","Filthy","Forceful","Forsaken","Frightening","Fury","Gargantuan","Gleeful","Grand","Grave","Greedy","Grim","Grinning","Gross","Grotesque","Gruesome","Haunting","Havoc","Heavy","Hollow","Horrible","Hungry","Indulgent","Infernal","Jaded","Jagged","Laughing","Lumbering","Mad","Mindless","Miserable","Misery","Monstrous","Noxious","Outlandish","Perverted","Powerful","Prime","Rage","Reckless","Renegade","Repulsive","Skeletal","Stark","Thunderous","Tomb","Torment","Tormented","Twilight","Twin","Vengeful","Vicious","Villainous","Violent","Wicked","Wild","Winged","Wrathful","Wretched"];
var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i % 2 === 0){
			rnd = Math.floor(Math.random() * nm6.length);
			rnd2 = Math.floor(Math.random() * nm7.length);
			while(nm6[rnd] === nm7[rnd2]){
				rnd2 = Math.floor(Math.random() * nm7.length);
			}
			rnd3 = Math.floor(Math.random() * nm8.length);
			lName = nm6[rnd] + nm7[rnd2] + " " + nm8[rnd3];
		}else{
			rnd = Math.floor(Math.random() * nm9.length);
			rnd2 = Math.floor(Math.random() * nm8.length);
			while(nm9[rnd] === nm8[rnd2]){
				rnd2 = Math.floor(Math.random() * nm8.length);
			}
			lName = nm9[rnd] + " " + nm8[rnd2];
		}
		if(i < 6){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm2.length);
			while(nm3[rnd3] === nm1[rnd]){
				rnd3 = Math.floor(Math.random() * nm3.length);
			}
			rnd5 = Math.floor(Math.random() * nm5.length);
			while(nm3[rnd3] === nm5[rnd5]){
				rnd5 = Math.floor(Math.random() * nm5.length);
			}
			if(i < 3){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + ", " + lName;
			}else{
				rnd6 = Math.floor(Math.random() * nm4.length);
				while(nm4[rnd6] === nm3[rnd3]){
					rnd6 = Math.floor(Math.random() * nm4.length);
				}
				rnd7 = Math.floor(Math.random() * nm2.length);
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5] + ", " + lName;
			}
		}else{
			names = lName;
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