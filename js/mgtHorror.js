var nm1 = ["b","br","cr","ch","d","dr","g","gr","k","kr","n","q","qr","r","s","sr","str","t","tr","v","x","z"];
var nm2 = ["a","e","o","u","a","e","o","u","a","e","o","u","a","e","o","u","ee","ai","au","ao","ou","ei"];
var nm3 = ["dn","dl","dr","dd","gn","gl","gd","k","kk","kl","kn","kr","lr","ln","ld","ldr","lg","lgr","lk","lkr","m","mk","md","mg","mgr","mdr","ng","ngr","nd","ndr","nk","nkr","nr","nz","r","rg","rl","rk","rd","rdr","rgr","rb","rbr","s","sg","sgr","sl","sr","st","str","t","tr","tl","v","vr","vl","vk","z","zg","zgr","zd","zdr","zl","zk","zkr"];
var nm4 = ["c","ch","d","l","m","n","t","x","z"];

var nm5 = ["","","","","","br","dr","g","gr","l","m","n","q","qr","r","t","tr","th","v","y","z"];
var nm6 = ["a","e","i","u"];
var nm7 = ["d","g","j","m","n","r","s","st","t","th","tr","v","y"];
var nm8 = ["g","l","m","n","q","r","s","x","z"];

var nm9 = ["","","","","","d","h","k","l","n","m","r","s","t","v","y","z"];
var nm10 = ["a","e","i","o"];
var nm11 = ["c","ch","g","j","k","n","q","t","v","x","z"];
var nm12 = ["c","l","m","n","r","s","v","x","z"];
var nm13 = ["c","d","n","r","s","t","th","x"];

var nm14 = ["amber","arc","ash","bale","barb","bitter","blaze","blister","blood","blunt","bone","boulder","brick","broad","cave","chaos","chasm","cinder","crag","creak","crypt","dark","dawn","dead","death","dirge","doom","dread","dusk","dust","ember","fire","flame","flesh","flint","fore","forge","fright","frost","fuse","gloom","gnarl","gore","gray","great","grey","grim","haze","hell","horn","krag","lash","lone","long","mind","mist","molten","moon","mourn","mud","murk","myco","necro","nether","night","onyx","pyre","rage","rapid","rough","saur","shade","shadow","silent","skull","slate","spell","spells","stitch","stone","storm","strom","tall","tangle","thunder","twilight","under","wild","wood"];
var nm15 = ["bane","bash","bender","blaze","blight","blood","bone","born","bough","bound","breaker","bringer","brow","burn","claw","cleaver","copse","crag","crawler","crest","crown","crusher","doom","fall","fang","fiend","fire","flame","flaw","force","forge","fury","gaze","gen","growl","growth","grub","gut","head","heart","hell","horn","howl","husk","kirk","kite","lash","leech","rage","reaper","reaver","run","scar","shadow","shard","shell","spark","spine","stalk","stalker","stand","strike","striker","stub","synth","thorn","weed","wing","wood","wrack","wraith","writher"];
var nm16 = ["Aberration","Abomination","Annihilator","Barbarian","Brute","Butcher","Champion","Conduit","Corrupter","Courier","Crawler","Creation","Creeper","Crusher","Destroyer","Devourer","Dreadlord","Driller","Emissary","Enforcer","Eviscerator","Fiend","Form","Gargantuan","Gatekeeper","Gorger","Gouger","Harvester","Hatchling","Horror","Host","Howler","Infiltrator","Intimidator","Mangler","Mass","Mauler","Maw","Monster","Monstrosity","Negator","Nemesis","Nomad","Obliterator","Oppressor","Overlord","Parasite","Pest","Phalanx","Prowler","Rager","Raker","Reaper","Reaver","Remains","Reveler","Ruinator","Scavenger","Scourge","Scudder","Shambler","Shedder","Skulker","Slag","Slasher","Slaver","Spitter","Stinger","Swarm","Swarmlord","Thing","Tormenter","Tyrant"];

var nm17 = ["Abyss","Abyssal","Acidic","Advanced","Anchored","Animated","Arid","Awoken","Blind","Bony","Broken","Careless","Chasm","Chittering","Colossal","Core","Corrupt","Corrupted","Cosmic","Crazed","Crooked","Cruel","Cursed","Damaged","Dark","Deaf","Delirious","Despair","Dire","Disfigured","Dread","Droopy","Enslaved","Eternal","Eyeless","Faceless","Fading","Faint","Feisty","Fickle","Filthy","Flickering","Forgotten","Forsaken","Foul","Fume","Gloomy","Grave","Greater","Grief","Grim","Growing","Guilt","Hidden","Hollow","Horrible","Huge","Hungry","Inferior","Infernal","Infinite","Lanky","Lesser","Limping","Livid","Lone","Lopsided","Meager","Meaty","Menacing","Mesmeric","Mindless","Monstrous","Murky","Mysterious","Nether","Night","Nightmare","Noxious","Organic","Partial","Pit","Plague","Possessed","Powerful","Prime","Primeval","Pungent","Putrid","Ragged","Reckless","Ridged","Rotten","Rotting","Savage","Scaly","Scrawny","Sewer","Shady","Shrill","Sinuous","Skeletal","Skittering","Skulking","Slimy","Slippery","Slithering","Slithery","Sludge","Slum","Slumbering","Slushy","Smog","Smoldering","Soggy","Sorrow","Spiked","Stitched","Storm","Sweltering","Tangle","Tangled","Thorny","Thunderous","Vicious","Viscous","Void","Warped","Wicked","Wilted","Winged","Worn","Wrathful","Wretched","Writing"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			if(i < 2){
				rnd = Math.random() * nm1.length | 0;
				rnd2 = Math.random() * nm2.length | 0;
				rnd3 = Math.random() * nm3.length | 0;
				while(nm3[rnd3] === nm1[rnd]){
					rnd = Math.random() * nm1.length | 0;
				}
				rnd4 = Math.random() * nm2.length | 0;
				rnd5 = Math.random() * nm4.length | 0;
				while(nm3[rnd3] === nm4[rnd5]){
					rnd5 = Math.random() * nm4.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd2] + nm4[rnd5];
			}else if(i < 4){
				rnd = Math.random() * nm5.length | 0;
				rnd2 = Math.random() * nm6.length | 0;
				rnd3 = Math.random() * nm7.length | 0;
				while(nm7[rnd3] === nm5[rnd]){
					rnd = Math.random() * nm5.length | 0;
				}
				rnd4 = Math.random() * nm6.length | 0;
				rnd5 = Math.random() * nm8.length | 0;
				while(nm7[rnd3] === nm8[rnd5]){
					rnd5 = Math.random() * nm8.length | 0;
				}
				names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd2] + nm8[rnd5];
			}else{
				rnd = Math.random() * nm9.length | 0;
				rnd2 = Math.random() * nm10.length | 0;
				rnd3 = Math.random() * nm11.length | 0;
				while(nm11[rnd3] === nm9[rnd]){
					rnd = Math.random() * nm9.length | 0;
				}
				rnd4 = Math.random() * nm10.length | 0;
				rnd5 = Math.random() * nm12.length | 0;
				while(nm11[rnd3] === nm12[rnd5]){
					rnd5 = Math.random() * nm12.length | 0;
				}
				rnd6 = Math.random() * nm10.length | 0;
				rnd7 = Math.random() * nm13.length | 0;
				while(nm13[rnd7] === nm12[rnd5]){
					rnd7 = Math.random() * nm13.length | 0;
				}
				names = nm9[rnd] + nm10[rnd2] + nm11[rnd3] + nm10[rnd4] + nm12[rnd5] + nm10[rnd6] + nm13[rnd7];
			}
		}else if(i < 8){
			rnd = Math.random() * nm14.length | 0;
			rnd2 = Math.random() * nm15.length | 0;
			while(nm14[rnd] === nm15[rnd2]){
				rnd2 = Math.random() * nm15.length | 0;
			}
			rnd3 = Math.random() * nm16.length | 0;
			names = nm14[rnd] + nm15[rnd2] + " " + nm16[rnd3];
		}else{
			rnd = Math.random() * nm17.length | 0;
			rnd2 = Math.random() * nm16.length | 0;
			names = nm17[rnd] + " " + nm16[rnd2];
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