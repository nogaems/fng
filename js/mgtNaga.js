var nm1 = ["","","","","","c","g","h","j","kh","n","r","s","t","th","y","z"];
var nm2 = ["a","e","i","a","e","i","o","u"];
var nm3 = ["d","g","k","l","n","r","s","t","d","g","k","l","n","r","s","t","d","dd","dr","g","gg","gr","gl","gn","gd","k","kk","kl","kn","kd","kdr","kr","l","ll","lk","ld","lg","ldr","lgr","lkr","n","nn","nd","ndr","ng","ngr","r","rr","rh","rn","s","sh","shr","sr","shn","sn","t","thn","thr","tr"];
var nm4 = ["d","g","k","l","n","r","s","t"];
var nm5 = ["Archer","Assassin","Augur","Bonekeeper","Brute","Butcher","Champion","Clairvoyant","Conqueror","Conscript","Deceiver","Defender","Defiant","Diviner","Drowner","Enforcer","Executioner","Fiend","Flayer","Guerrilla","Insurgent","Keeper","Mutineer","Oracle","Ranger","Rebel","Renegade","Resistance","Savage","Scout","Seer","Shepherd","Skullkeeper","Slayer","Soothsayer","Spell-Eater","Spellcaster","Spellcatcher","Spellsnatcher","Spy","Strangler","Subjugator","Swindler","Tyrant","Vandal","Vanquisher","Victor","Vigilante","Vindicator","Vizier","Wanderer","Warrior"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		rnd4 = Math.floor(Math.random() * nm2.length);
		while(nm3[rnd3] === nm1[rnd]){
			rnd3 = Math.floor(Math.random() * nm3.length);
		}
		if(i % 2 === 0){
			lName = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4];
		}else{
			rnd5 = Math.floor(Math.random() * nm4.length);
			rnd6 = Math.floor(Math.random() * nm2.length);
			while(nm3[rnd3] === nm4[rnd5]){
				rnd5 = Math.floor(Math.random() * nm4.length);
			}
			lName = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5] + nm2[rnd6];
		}
		if(i < 6){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm2.length);
			if(i < 3){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + " " + lName;
			}else{
				rnd5 = Math.floor(Math.random() * nm4.length);
				rnd6 = Math.floor(Math.random() * nm2.length);
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5] + nm2[rnd6] + " " + lName;
			}
		}else{
			rnd = Math.floor(Math.random() * nm5.length);
			names = lName + " " + nm5[rnd];
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