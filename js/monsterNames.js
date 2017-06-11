var nm1 = ["Acidic","Active","Aged","Agile","Agitated","Ancient","Angry","Anguished","Arctic","Arid","Aromatic","Awful","Barren","Bewitched","Big Bad","Bitter","Black","Bleak","Blind","Blissful","Blue","Bold","Broken","Bronze","Brown","Bruised","Calm","Canine","Cloudy","Cold","Colossal","Corrupt","Crazy","Creepy","Cruel","Dangerous","Dark","Dead","Deadly","Defiant","Delirious","Dirty","Disfigured","Disgusting","Dismal","Dreary","Electric","Empty","Enraged","Eternal","Evil","Faint","False","Feline","Fickle","Filthy","Forsaken","Giant","Gray","Greedy","Grim","Gross","Grotesque","Gruesome","Grumpy","Hairy","Half","Haunting","Hidden","Hollow","Horrible","Hungry","Icy","Infamous","Insane","Insidious","Jagged","Lanky","Lean","Living","Lone","Lonely","Mad","Meager","Mean","Monstrous","Muted","Nasty","Needy","Noxious","Outlandish","Parallel","Putrid","Quick","Quiet","Reckless","Rotten","Shady","Sick","Skeletal","Tall","Thin","Twin","Ugly","Undead","Vengeful","Volatile","White","Wild","Wretched"];
var nm2 = ["Man","Woman","Child","Mutant","Abomination","Glob","Monster","Behemoth","Beast","Freak","Horror","Fiend","Abnormality","Brute","Miscreation","Monstrosity","Savage","Deformity","Deviation","Anomaly","Weirdo","Abortion","Malformation","Blob","Lump","Bulge","Tumor","Creature","Critter","Vermin","Being","Thing","Revenant","Keeper","Guardian","Witch","Troglodyte","Charmer","Vine","Tree","Plant","Howler","Statue","Vision","Dweller","Lich","Pest","Gnoll","Ooze","Hag","Hunter","Entity","Phenomenon","Body","Figure","Presence","Corpse","Demon","Wraith","Herder","Mongrel","Hybrid","Mutt","Teeth","Eyes","Face","Screamer","Howler","Shrieker","Wailer","Babbler","Mumbler","Creeper"];
var nm3 = ["Abyss","Acid","Ash","Aura","Bane","Barb","Blade","Blaze","Blight","Bone","Boulder","Bowel","Brine","Cave","Cavern","Chaos","Cinder","Cloud","Coffin","Corpse","Crypt","Curse","Dawn","Decay","Doom","Dread","Dream","Dusk","Dust","Ember","Fetid","Flame","Fog","Foul","Fright","Frost","Gall","Gas","Germ","Gloom","Glow","Grave","Grieve","Grime","Gut","Haunt","Hell","Hollow","Horror","Infernal","Inferno","Metal","Mist","Mold","Morn","Mourn","Murk","Nether","Night","Phantom","Phase","Plague","Poison","Putrid","Razor","Rot","Rotting","Rust","Shade","Shadow","Slag","Smog","Smoke","Soil","Sorrow","Soul","Spectral","Spirit","Spite","Steam","Stench","Stink","Stone","Taint","Tangle","Terror","Thorn","Thunder","Tomb","Toxin","Trance","Umbra","Vamp","Vapor","Venom","Vex","Vile","Voodoo","Vortex","Warp","Web","Wisp"];
var nm4 = ["beast","being","body","boy","brood","morph","brute","bug","cat","child","claw","crackle","creep","deviation","face","fang","fiend","figure","flayer","foot","freak","ghoul","girl","golem","hag","hand","hood","hound","lich","ling","ling","ling","ling","man","mask","mirage","monster","mouth","mutant","paw","pest","pod","scream","screamer","seeker","serpent","snake","snare","soul","spawn","step","strike","sword","talon","taur","teeth","thing","tooth","tree","vine","wing","wings","woman","wraith"];
var nm5 = ["Agile","Amphibian","Aquatic","Arctic","Barb-Tailed","Black-Eyed","Black-Striped","Blind","Blood-Eyed","Bloodthirsty","Bright","Brutal","Burnt","Chaotic","Cobalt","Cold-Blooded","Crazed","Crimson","Crowned","Dark","Diabolical","Ebon","Electric","Elusive","Evasive","Feathered","Feral","Fiery","Furry","Giant","Glacial","Golden","Greater","Grim","Grisly","Hidden","Horned","Howling","Iron","Iron-Scaled","Ivory","Jade","Lone","Long-Horned","Mad","Malevolent","Masked","Matriarch","Monstrous","Obsidian","Onyx","Painted","Patriarch","Primeval","Primitive","Rabid","Raging","Ravaging","Red-Eyed","Ruthless","Sapphire","Savage","Scarred","Screeching","Silver","Silver-Striped","Slender","Stalking","Stormcloud","Supreme","Taloned","Tattooed","Titanic","Titanium","Tusked","Vicious","White-Eyed","Wild"];
var nm6 = ["Army","Ash","Assassin","Bane","Berserker","Blaze","Blight","Bone","Boulder","Butcher","Cave","Cavern","Cinder","Corpse","Dawn","Demon","Dire","Doom","Dread","Flame","Frost","Ghost","Grieve","Harlequin","Horror","Hunting","Jester","Killer","Mist","Mocking","Moon","Mountain","Nether","Night","Nightmare","Phantom","Predator","Preying","Raptor","Razor","Razorback","Rot","Shadow","Skeleton","Slayer","Spite","Storm","Sun","Terror","Thunder","Tomb","Torment","Vampire","Venom","Vision","Warp","World"];
var nm7 = ["Alligator","Anaconda","Ape","Bat","Bear","Beast","Bee","Behemoth","Bison","Boar","Buffalo","Bull","Cat","Cobra","Critter","Crocodile","Deer","Dog","Dragon","Drake","Elephant","Fiend","Freak","Frog","Gargoyle","Gorilla","Hawk","Hippo","Hog","Hound","Hyena","Jackal","Leopard","Leviathan","Lion","Lizard","Lynx","Monkey","Monster","Owl","Panther","Phoenix","Pig","Rat","Rhino","Scorpion","Serpent","Sheep","Snake","Spider","Swine","Tiger","Vermin","Viper","Warthog","Wolf","Yak"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 4){
			rnd = Math.floor(Math.random() * nm3.length);
			rnd2 = Math.floor(Math.random() * nm4.length);
			names = nm3[rnd] + nm4[rnd2];
		}else if(i < 7){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = "The " + nm1[rnd] + " " + nm2[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm5.length);
			rnd2 = Math.floor(Math.random() * nm6.length);
			rnd3 = Math.floor(Math.random() * nm7.length);
			names = "The " + nm5[rnd] + " " + nm6[rnd2] + " " + nm7[rnd3];
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