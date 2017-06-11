var nm1 = ["Ace","Acrobat","Ajax","Angel","Apollo","Archangel","Artemis","Ash","Azar","Azral","Baltazar","Bandit","Bane","Basil","BatPitt","Batista","Batley","Baxter","Beaker","Bigglesworth","Bitz","Blackjack","Blade","Blaze","Blitz","Bloodwing","Blues","Booboo","Bruce","Brutus","Bubba","Bubbles","Bullet","Buster","Butch","Buttons","Chaos","Char","Chocula","Cole","Comet","Cookie","Count","Cupcake","Darkess","Darth","Dexter","Diablo","Dimitri","Ding","Dodge","Dodger","Doom","Drac","Dracula","Draculon","Drake","Echo","Equinox","Fangs","Flapper","Flappy","Flaps","Flash","Flicker","Fuzz","Gambat","Gargle","Gargles","Gargoyle","Gavalon","Ghost","Gizmo","Glider","Gloom","Glyde","Golbat","Gouge","Grey","Guano","Hannibal","Hawke","Hunter","Hyperion","Impaler","Jet","Kane","Khan","Kindle","Lecter","Lockjaw","Lucifer","Marble","Matrix","Merlin","Midas","Midnight","Mirage","Monty","Moon","Mothra","Muse","Nerf","Nibbles","Nightmare","Nightwing","Nugget","Nukem","Nyx","Onyx","Orion","Ozzy","Patch","Patches","Pebbles","Phantom","Pickle","Psych","Quickfang","Quilla","Rabies","Rainbow","Rascal","Remus","Render","Rhonin","Ripmaw","Rocky","Rufus","Sabath","Sawyer","Screech","Screechy","Shade","Shadow","Shreek","Shrike","Slate","Slithe","Snuffle","Sonar","Sonny","Spectre","Spitfire","Spudnik","Spuds","Swoops","Thunder","Tiberius","Titan","Twinkle","Umber","Vamp","Vlad","Vladimir","Vulkan","Wayne","Wiggles","Wingnut","Xanadu","Zion"];
var nm2 = ["Abby","Aerial","Aine","Alexia","Alexis","Amber","Angel","Angie","Apple","Ash","Atilla","Aura","Aurora","Azraelle","Azure","Azurys","Babes","Bandetta","Batsy","Batty","Beauty","Biscuit","Blaze","Breeze","Bubble","Bubbles","Buttercup","Buttons","Calypso","Cerulean","Chuckles","Cinderella","Cinnamon","Clementine","Cleo","Cookie","Cosmo","Cuddles","Cupcake","Dakota","Daphne","Dawn","Dawne","Dawnstar","Dot","Draculette","Ebony","Echo","Eclipse","Ember","Enigma","Equina","Equinox","Fang","Fangie","Faune","Fierra","Fizzle","Flappy","Fluffy","Flutters","Gadget","Gargles","Giggles","Grace","Guani","Harmony","Haze","Hazel","Honey","Huntress","Iggy","Illumina","Indigo","Iris","Ivory","Ivy","Jinx","Jynx","Lady","Liberty","Lucy","Lullaby","Luna","Mable","Marbles","Maya","Melody","Mirage","Mittens","Moonbeam","Moone","Moonlight","Morning","Morticia","Myst","Mystique","Nibbles","Nighte","Noodles","Nova","Nugget","Oracle","Peaches","Pebbles","Pepper","Phoenix","Pickle","Pickles","Plume","Precious","Princess","Psyche","Raine","Raven","Rebel","Rhyme","Rogue","Ruth","Sade","Sage","Scarlett","Shade","Shadow","Shay","Shine","Siren","Skye","Skylar","Snuffles","Sona","Sora","Star","Stardust","Starlight","Sugar","Tinkerbell","Trixie","Trixy","Twilight","Twinkle","Twinkles","Vanity","Velvet","Violet","Vixen","Wiggles","Xena"];

function nameGen(type){
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd];
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