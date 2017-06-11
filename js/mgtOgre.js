var nm1 = ["c","g","j","k","m","n","r","t","v","y","z"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","uo","uu","ua","ou","au","aa"];
var nm3 = ["d","dd","dg","dr","g","gr","gg","gd","gz","gv","k","kk","kd","kz","kv","kr","lk","lg","lkr","lz","ldr","lg","lgr","ng","ngr","nd","ndr","nr","r","rd","rb","rk","rz","rg","rgr","rg","rkr","rn","rz","sg","sgr","z","zc","zcr","zd","zg","zgr","zk","zkr"];
var nm4 = ["c","d","k","l","m","n","s","sh","t","th","z"];

var nm5 = ["c","d","g","k","n","r","t","th"];
var nm6 = ["c","d","g","k","n","r","s"];

var nm7 = ["amber","ash","battle","blaze","blood","bone","boulder","burn","burning","cinder","dark","dead","death","doom","ember","fire","flame","fuse","gloom","gore","grim","grizzly","hell","hollow","molten","mourn","nether","poison","pyre","rage","rough","rumble","saur","saw","serpent","shade","shadow","skull","slate","slaughter","stone","storm","thunder","titan","twilight","void","war","wild"];
var nm8 = ["bane","belly","blade","blaze","blight","blood","bone","breath","chewer","cleaver","crest","crusher","curse","doom","eye","eyes","fall","field","fire","flame","flayer","force","forge","fury","gaze","gazer","gloom","hell","hole","house","howl","lash","limb","mourn","rage","reaper","reaver","ripper","roar","scar","stride","tooth"];
var nm9 = ["Aggressor","Annihilator","Arsonist","Assassin","Barbarian","Battler","Berserker","Bleeder","Bouncer","Brawler","Bruiser","Brute","Bully","Champion","Charmer","Contender","Destroyer","Diabolist","Dragger","Enforcer","Eradicator","Fighter","Flailer","Freebooter","Gatecrasher","Gladiator","Guardian","Heavy","Hireling","Hulk","Invader","Maniac","Marauder","Mercenary","Oaf","Ogre","Oozer","Outlaw","Pillager","Pummeler","Pyromaniac","Rager","Raider","Renegade","Savage","Scrapper","Sentry","Shaman","Slugger","Slumlord","Tanker","Taskmaster","Tyrant","Vandal","Warbrute","Ward","Warlord","Warrior","Wildcat","Wrecker"];

var nm10 = ["Aggravated","Aggressive","Agitated","Angry","Anguished","Barrage","Bitter","Blissful","Blood","Bloodthirsty","Bold","Bossy","Bruised","Careless","Colossal","Corrupt","Corrupted","Crazed","Crooked","Cruel","Crypt","Defiant","Delirious","Drooling","Energetic","Enormous","Enraged","Exhausted","Fearless","Foolish","Forsaken","Frenzied","Frightening","Grave","Greedy","Grim","Heartless","Hulking","Hungry","Husky","Idle","Infernal","Insane","Jumbo","Limping","Livid","Lone","Mad","Marsh","Mausoleum","Menacing","Monstrous","Noxious","Rash","Reckless","Robust","Savage","Shady","Tomb","Tough","Towering","Treasonous","Vengeful","Vicious","Villainous","Vindictive","Violent","Wicked","Wild","Wrathful","Wrecking","Wretched"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd6 = Math.floor(Math.random() * nm5.length);
			rnd7 = Math.floor(Math.random() * nm2.length);
			rnd8 = Math.floor(Math.random() * nm6.length);
			if(i % 2 === 0){
				lName = nm5[rnd6] + nm2[rnd7] + nm6[rnd8];
			}else{
				rnd9 = Math.floor(Math.random() * nm3.length);
				rnd10 = Math.floor(Math.random() * nm2.length);
				while(nm3[rnd9] === nm5[rnd6]){
					rnd9 = Math.floor(Math.random() * nm3.length);
				}
				lName = nm5[rnd6] + nm2[rnd7] + nm3[rnd9] + nm2[rnd10] + nm6[rnd8];
			}
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm4.length);
			if(i < 3){
				names = nm1[rnd] + nm2[rnd2] + nm4[rnd3] + " " + lName;
			}else{
				rnd4 = Math.floor(Math.random() * nm3.length);
				rnd5 = Math.floor(Math.random() * nm2.length);
				while(nm3[rnd4] === nm1[rnd]){
					rnd4 = Math.floor(Math.random() * nm3.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm2[rnd5] + nm4[rnd3] + " " + lName;
			}
		}else if(i < 8){
			rnd = Math.floor(Math.random() * nm7.length);
			rnd2 = Math.floor(Math.random() * nm8.length);
			while(nm7[rnd] === nm8[rnd2]){
				rnd2 = Math.floor(Math.random() * nm8.length);
			}
			rnd3 = Math.floor(Math.random() * nm9.length);
			names = nm7[rnd] + nm8[rnd2] + " " + nm9[rnd3];
		}else{
			rnd = Math.floor(Math.random() * nm10.length);
			rnd2 = Math.floor(Math.random() * nm9.length);
			names = nm10[rnd] + " " + nm9[rnd2];
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