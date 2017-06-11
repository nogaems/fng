var nm1 = ["b","c","g","j","k","r","s","v","x","z"];
var nm2 = ["a","e","o","a","e","o","a","e","o","i","u"];
var nm3 = ["d","g","l","m","n","r","t","v","y","z"];
var nm4 = ["c","d","g","j","k","n","t","v","z"];
var nm5 = ["c","l","n","r","s","t","x"];
var nm5b = ["","","","","","c","l","n","r","s","t","x"];

var nm6 = ["","","c","d","f","h","l","m","n","ph","s","t"];
var nm7 = ["a","i","e","a","i","e","a","i","e","y","y","a","i","e","a","i","e","y","ea","ia","ua"];
var nm8 = ["d","h","l","m","n","r","s","t","z"];
var nm9 = ["d","f","k","l","m","n","r","s","t"];

var nm10 = ["Abandoned","Accursed","Adept","Adored","Aggravated","Aggressive","Agitated","Alienated","Angry","Animated","Austere","Battlefield","Blind","Boreal","Brave","Broken","Careful","Careless","Cautious","Centaur","Chief","Colossal","Composed","Corrupt","Corrupted","Crooked","Cruel","Defiant","Delirious","Determined","Devoted","Diligent","Disloyal","Dowsing","Faithful","Fearless","Feisty","Forsaken","Gifted","Graceful","Grand","Grim","Idle","Infamous","Juvenile","Kind","Kindhearted","Leaf","Loaming","Lone","Mindless","Misguided","Naive","Nervous","Nimble","Outlandish","Phantom","Possessed","Prestigious","Prime","Roaming","Serene","Shadowy","Sneaking","Sneaky","Spellbane","Spellbound","Spirit","Swift","Thunderous","Tired","Torn","Trusted","Turbulent","Twin","Unruly","Unwielding","Venerated","Vengeful","Warped","Watchful","Wicked","Wild","Wrathful","Wretched","Young"];
var nm11 = ["Adept","Archer","Barbarian","Battlemaster","Binder","Brawler","Brute","Caster","Centaur","Champion","Charger","Chieftain","Courser","Crusader","Dancer","Disciple","Elder","Fanatic","Guardian","Healer","Herald","Hero","Marauder","Oracle","Outrider","Protector","Raider","Ranger","Rootbinder","Rootcaster","Rootcrasher","Safeguard","Savage","Scavenger","Scout","Scrounger","Seer","Sentinel","Shaman","Slayer","Spellcaster","Stomper","Tactician","Thunderhoof","Trailblazer","Trampler","Trapper","Trickster","Veteran","Vinecaster","Vinecrasher","Warchief","Warden","Warmage","Warmaster","Weaver"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i % 3 === 0){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm2.length);
			rnd5 = Math.floor(Math.random() * nm5b.length);
			rnd6 = Math.floor(Math.random() * nm11.length);
			lName = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd2] + nm5b[rnd5] + "'s " + nm11[rnd6];
		}else{
			rnd = Math.floor(Math.random() * nm10.length);
			rnd2 = Math.floor(Math.random() * nm11.length);
			while(nm10[rnd] === nm11[rnd2]){
				rnd2 = Math.floor(Math.random() * nm11.length);
			}
			lName = nm10[rnd] + " " + nm11[rnd2];
		}
		if(tp === 1){
			if(i < 6){
				rnd = Math.floor(Math.random() * nm6.length);
				rnd2 = Math.floor(Math.random() * nm7.length);
				rnd3 = Math.floor(Math.random() * nm8.length);
				rnd4 = Math.floor(Math.random() * nm7.length);
				if(i < 3){
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + ", " + lName;
				}else{
					rnd8 = Math.floor(Math.random() * nm9.length);
					rnd9 = Math.floor(Math.random() * nm2.length);
					while(nm9[rnd8] === nm8[rnd3]){
						rnd8 = Math.floor(Math.random() * nm9.length);
					}
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd8] + nm7[rnd9] + ", " + lName;
				}
			}else{
				names = lName;
			}
		}else{
			if(i < 6){
				rnd = Math.floor(Math.random() * nm1.length);
				rnd2 = Math.floor(Math.random() * nm2.length);
				rnd3 = Math.floor(Math.random() * nm3.length);
				rnd4 = Math.floor(Math.random() * nm2.length);
				rnd5 = Math.floor(Math.random() * nm5.length);
				if(i < 3){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + ", " + lName;
				}else{
					rnd8 = Math.floor(Math.random() * nm4.length);
					rnd9 = Math.floor(Math.random() * nm2.length);
					while(nm4[rnd8] === nm3[rnd3]){
						rnd8 = Math.floor(Math.random() * nm4.length);
					}
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd8] + nm2[rnd9] + nm5[rnd5] + ", " + lName;
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