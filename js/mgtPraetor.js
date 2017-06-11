var nm1 = ["ch","d","g","j","k","kh","n","ph","q","r","s","sh","t","th","v","z"];
var nm2 = ["a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","u","eo","ia","io","ea"];
var nm3 = ["d","dr","dd","g","gn","gr","gl","k","kk","kl","kn","kr","l","ll","lgl","gr","ld","ln","lr","lv","lz","lq","lqr","ldr","n","nn","nq","nqr","ng","ngr","nd","ndr","nz","nv","nl","q","qq","qr","ql","qn","r","rk","rl","rn","rv","rz","rr","rqr","rdr","rl","sh","str","sc","scl","skr","sk","t","th","tr","thr","v"];
var nm4 = ["d","g","gg","k","l","ll","n","nn","q","r","rr","sh","t","tt","v","z"];
var nm5 = ["d","g","k","ks","n","nd","q","rn","s","sh","sk","x","z"];

var nm6 = ["Adept","Aged","Ancient","Banished","Barbed","Barrage","Bitter","Blazing","Blind","Bold","Bony","Bright","Broken","Cackling","Careless","Chaos","Cinder","Colossal","Core","Corrupt","Corrupted","Crimson","Crooked","Cruel","Crystal","Dark","Deaf","Delirious","Deserted","Ebon","Ember","Eternal","Fallen","Fearless","Feisty","Fickle","Fiery","Flame","Forge","Forked","Forsaken","Frost","Gargantuan","Grand","Grave","Grim","Grinning","Growing","Gruesome","Haunting","Haze","Hidden","Hollow","Hungering","Hungry","Idle","Infernal","Jaded","Jagged","Juvenile","Laughing","Lone","Lost","Mammoth","Mute","Nether","Noxious","Obsidian","Powerful","Primal","Prime","Pyre","Radiant","Ragged","Rash","Reckless","Sanguine","Scornful","Shade","Shadow","Shallow","Silent","Smiling","Smirking","Stark","Swift","Thunderous","Titan","Torn","Twilight","Twin","Tyrant","Unknown","Vain","Vengeful","Vicious","Villainous","Vile","Warped","Whispering","Wicked","Woeful","Wrathful","Wretched","Writhing"];
var nm7 = ["Annihilator","Augur","Befouler","Being","Brute","Cenobite","Creature","Degenerate","Demolisher","Desecrator","Despoiler","Destroyer","Diviner","Fiend","Harbinger","Harvester","Herald","Infernal","Keeper","Marauder","Minion","Monster","Oracle","Overlord","Overseer","Persecutor","Praetor","Ravager","Reaper","Renegade","Savage","Scourge","Seer","Sentinel","Sentry","Soothsayer","Taskmaster","Tyrant","Warden"];

var nm8 = ["Being","Brute","Creature","Fiend","Herald","Keeper","Minion","Overlord","Overseer","Praetor","Reaper","Renegade","Scourge","Seer","Tyrant","Voice","Warden"];
var nm9 = ["Acrimony","Agony","Anger","Anguish","Annihilation","Anxiety","Blood","Bones","Calamity","Catastrophe","Chaos","Darkness","Death","Desolation","Despair","Destruction","Ember","Extinction","Fire","Flame","Frenzy","Furor","Fury","Gloom","Grief","Hate","Hatred","Hunger","Hysteria","Ire","Isolation","Loss","Mania","Melancholy","Misery","Misfortune","Nightmares","Obsidian","Onyx","Pain","Perdition","Pestilence","Pride","Regret","Rue","Ruin","Ruins","Shadows","Silence","Solitude","Sorrow","Thunder","Tragedy","Twilight","Umbrage","Vengeance","Venom","Woe"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm5.length | 0;
			while(nm1[rnd] === nm5[rnd3]){
				rnd3 = Math.random() * nm5.length | 0;
			}
			if(i % 2 === 0){
				lName = nm1[rnd] + nm2[rnd2] + nm5[rnd3];
			}else{
				rnd4 = Math.random() * nm4.length | 0;
				rnd5 = Math.random() * nm2.length | 0;
				while(nm4[rnd4] === nm5[rnd3]){
					rnd4 = Math.random() * nm4.length | 0;
				}
				lName = nm1[rnd] + nm2[rnd2] + nm4[rnd4] + nm2[rnd5] + nm5[rnd3];
			}
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm5.length | 0;
			while(nm1[rnd] === nm5[rnd3]){
				rnd3 = Math.random() * nm5.length | 0;
			}
			if(i < 3){
				names = nm1[rnd] + nm2[rnd2] + nm5[rnd3] + " " + lName;
			}else{
				rnd4 = Math.random() * nm4.length | 0;
				rnd5 = Math.random() * nm2.length | 0;
				while(nm4[rnd4] === nm5[rnd3]){
					rnd4 = Math.random() * nm4.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm4[rnd4] + nm2[rnd5] + nm5[rnd3] + " " + lName;
			}
		}else if(i < 8){
			rnd = Math.random() * nm6.length | 0;
			rnd2 = Math.random() * nm7.length | 0;
			names = nm6[rnd] + " " + nm7[rnd2];
		}else{
			rnd = Math.random() * nm8.length | 0;
			rnd2 = Math.random() * nm9.length | 0;
			names = nm8[rnd] + " of " + nm9[rnd2];
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