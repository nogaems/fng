var nm1 = ["Aggressive","Agitated","Agony","Aggressive","Ancient","Angel","Angry","Animated","Anxious","Arachnid","Autumn","Avian","Bacterial","Banshee","Beer","Black","Boar","Brain","Brittle","Buzzing","Canine","Cat","Cave","Chicken","Chilling","Cold","Collapsing","Contagious","Cow","Crazy","Creeping","Crippling","Crumbling","Crying","Crystal","Curable","Deadly","Death's","Deathbell","Decaying","Delirious","Demon","Desert","Desolation","Deteriorating","Devil's","Dog","Dragon","Dream","Dreaming","Duck","Dwarf","Dying","Elastic","Elephant","Enlarged","Ethereal","Exhausting","Explosive","Fading","Failing","Fall","Falling","Fatal","Feline","Fickle","Fiery","Fisherman's","Flower","Forceful","Forest","Frenzied","Frost","Frozen","Ghastly","Ghost","Goblin","Golden","Goose","Grave","Green","Growing","Guttural","Happy","Harmless","Heaven's","Hell","Hellish","Hiccup","Hopeless","Horse","Hostile","Hot","Humming","Hyper","Icy","Immobilizing","Impossible","Incurable","Intense","Iron","Ironbark","Island","Jumping","Jungle","King's","Lady","Laughing","Lifeless","Limp","Lion","Lizard","Man","Marsh","Memory","Mild","Milk","Mortal","Mountain","Mouse","Necrotic","Nervous","Numb","Numbing","Ogre","Orange","Pale","Paralyzing","Peaceful","Permanent","Pestilent","Petrifying","Phantom","Pig","Pink","Pygmy","Queen's","Quiet","Quivering","Rabbit","Rabid","Rasping","Rat","Red","Restless","Rickety","Rock","Rodent","Rooster","Rotting","Running","Sage","Screaming","Sedated","Serpent","Shadow","Shaking","Shaky","Sheep","Shivering","Shriveling","Silent","Silver","Sinister","Sleep","Smiling","Snake","Sniffeling","Soft","Soul","Spastic","Spider","Spine","Spirit","Spring","Steel","Sterile","Stiff","Stiffening","Stimulated","Stinging","Stomach","Stranger's","Stressed","Stressful","Stunned","Summer","Swamp","Swine","Temporary","Terrifying","Thorny","Ticklish","Tiring","Tomb","Tranquil","Tree","Trembling","Trivial","Twitching","Ugly","Undead","Vein","Violet","Volatile","Warping","Water","Weak","Weakening","Whispering","Wicked","Wild","Winter","Wired","Witch","Withering","Wizard","Wolf","Wooden","Worn","Wraith","Yellow","Zombie"];
var nm2 = ["Ache","Aching","Acne","Allergy","Amnesia","Anemia","Anthrax","Anxiety","Arthritis","Asthma","Baldness","Blight","Blindness","Blisters","Body","Bones","Bronchitis","Cancer","Cannibalism","Chills","Chlamydia","Cholera","Cold","Cough","Cramps","Deafness","Death","Decay","Deficiency","Dehydration","Delirium","Delusion","Delusions","Depression","Diptheria","Disease","Dysfunctions","Ears","Ebola","Epilepsy","Euphoria","Eye","Eyes","Fatigue","Feet","Fever","Finger","Flu","Foot","Gangrene","Gonorrhea","Hallucinations","Hands","Head","Heart","Hepatitis","Herpes","Illness","Infection","Infertility","Inflammation","Influenza","Insanity","Insomnia","Intolerance","Irritation","Leprosy","Lupus","Malaria","Measles","Meningitis","Migraine","Mouth","Mutation","Nausea","Nose","Panic","Paralysis","Paranoia","Parasite","Plague","Pneumonia","Poisoning","Pox","Rabies","Rage","Rash","Salmonella","Scarring","Schizophrenia","Scurvy","Shock","Skin","Sleep Disorder","Sneeze","Soreness","Sores","Spasms","Stiffness","Stomach","Swelling","Syndrome","Syphilis","Tetanus","Throat","Tongue","Tumor","Ulcers","Vampirism","Virus","Warts"];

function nameGen(){
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + " " + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}