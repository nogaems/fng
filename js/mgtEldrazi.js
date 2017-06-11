var nm1 = ["c","d","g","k","m","n","r","t","v","z"];
var nm2 = ["a","e","i","o","u"];
var nm3 = ["j","k","l","lm","ln","lr","ll","ld","m","mr","ml","mk","mr","md","mm","mn","n","ng","nd","nl","nk","nr","nn","rl","rn","rm","rz","rr","r","s","sl","sr","z","zg","zr"];
var nm4 = ["c","d","g","k","l","m","n","r","t"];
var nm5 = ["d","g","l","k"];

var nm6 = ["Abandoned","Acidic","Advanced","Aged","Aggressive","Anguished","Arid","Barrage","Bitter","Bleak","Blight","Blind","Blinding","Broken","Brood","Bulky","Bumpy","Careless","Catacomb","Chittering","Colossal","Corrupt","Corrupted","Crypt","Cryptic","Culling","Deaf","Deathless","Defiant","Delirious","Dimensional","Disfigured","Distended","Dread","Dreary","Droopy","Dust","Elder","Endless","Energetic","Essence","Eternal","Eyeless","Fathom","Fibrous","Fickle","Forked","Forsaken","Fragrant","Gaseous","Glistening","Gloomy","Glossy","Grave","Gravity","Great","Grim","Grubby","Gruesome","Haunting","Havoc","Hidden","Hideous","Hollow","Howling","Hungry","Icky","Impish","Incubator","Juicy","Lone","Lumpy","Matter","Measly","Mind","Mindless","Mist","Monstrous","Murk","Mushy","Nest","Nettle","Nightmare","Noxious","Oblivion","Pale","Paltry","Parched","Prickly","Prie","Pungent","Puny","Putrid","Ragged","Reckless","Repulsive","Robust","Rotten","Ruin","Ruination","Salvage","Scrawny","Silent","Sinuous","Sky","Slaughter","Sludge","Smothering","Squiggly","Stalking","Swift","Thought","Tide","Tomb","Vexing","Vicious","Vile","Violent","Void","Warped","Wicked","Wrathful","Wretched","Writhing"];
var nm7 = ["Abolisher","Abomination","Aggregate","Attendant","Bane","Behemoth","Breaker","Butcher","Carver","Conduit","Crawler","Cruiser","Crusher","Defiler","Depleter","Despoiler","Devastator","Displacer","Drifter","Drone","Eldrazi","Entangler","Feeder","Fiend","Forerunner","Grafter","Gryff","Harvester","Hatcher","Herald","Herder","Host","Hulk","Hunter","Immobilizer","Infiltrator","Intruder","Invader","Lurker","Marauder","Maw","Mimic","Monitor","Monster","Negator","Oracle","Pathfinder","Predator","Prophet","Rager","Raker","Razer","Reclaimer","Redeemer","Reshaper","Sage","Scion","Scourer","Scourge","Scout","Scuttler","Seer","Sentinel","Shaper","Shrieker","Sifter","Skimmer","Skitterer","Smasher","Sower","Spawn","Spawner","Stalker","Strangler","Strider","Summoner","Titan","Twin","Tyrant","Walker","Warden","Watcher","Winnower"];
var nm8 = ["Anarchy","Armies","Atrophy","Barbarism","Blitz","Blood","Bloodbaths","Bloodshed","Bones","Butchery","Carnage","Chaos","Death","Decay","Demolition","Depravity","Destruction","Devastation","Discord","Dismay","Dread","Entropy","Extermination","Extinction","Fear","Flesh","Gore","Havoc","Horror","Legions","Malice","Massacres","Nightmares","Plasma","Ruin","Ruination","Sadism","Savagery","Silence","Sinew","Skulls","Slaughter","Spite","Subjugation","Terror","Torment","Turmoil","Venom","Voids","Wreckages","the End","the Hollow","the Void","the Wastes"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			if(i % 2 === 0){
				rnd = Math.random() * nm6.length | 0;
				rnd2 = Math.random() * nm7.length | 0;
				lName = nm6[rnd] + " " + nm7[rnd2];
			}else{
				rnd = Math.random() * nm7.length | 0;
				rnd2 = Math.random() * nm8.length | 0;
				lName = nm7[rnd] + " of " + nm8[rnd2];
			}
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
		}else if(i < 8){
			rnd = Math.random() * nm6.length | 0;
			rnd2 = Math.random() * nm7.length | 0;
			names = nm6[rnd] + " " + nm7[rnd2];
		}else{
			rnd = Math.random() * nm7.length | 0;
			rnd2 = Math.random() * nm8.length | 0;
			names = nm7[rnd] + " of " + nm8[rnd2];
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