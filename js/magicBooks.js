var nm1 = ["Dragons","Fae","Fairies","Alicorns","Unicorns","Griffins","Pixies","Hippogriffs","Jackalopes","Kelpies","Vampires","Vampiric Creatures","Phoenixes","Roc","Cockatrice","Sirin","Tengu","Harpies","Minotaurs","Centaurs","Hellhounds","Demons","Minor Demons","Lesser Demons","Werewolves","Satyrs","Fauns","Pegasi","Chimeras","Manticores","Hippocamps","Sirens","Nature Spirits","Nymphs","Goblins","Bunyips","Wolpertingers","Moon Rabbits","Basilisks","Wyverns","Drakes","Gorgons","Hydras","Naga","Lamia","Kappa","Cyclopses","Giants","Brownies","Banshees","Gnomes","Golems","Gnolls","Gargoyles","Ents","Elementals","Dryads","Dragonkin","Lizardfolk","Merfolk","Kobolds","Imps","Ogres","Trolls"];
var nm2 = ["Fungi","Herbs","Trees","Flowers","Plants","Shrubs","Roots","Petals","Blossoms","Aquatic Plants","Aquatic Flora","Flora","Crystals","Cave Crystals"];
var nm3 = ["Alchemy","Arcane Familiars","Arithmancy","Astral Projection","Astronomy","Blood Magic","Charms","Chi","Chi Bending","Chronomancy","Clairvoyance","Conjuration","Counter-Curses","Cryomancy","Curse Protection","Curses","Dark Arts","Defensive Arts","Dispelling","Divination","Dreams","Elemental Magic","Emotional Sorcery","Healing Rituals","Illusions","Jinxes","Lucid Dreams","Lunar Magic","Magical Companions","Medimagic","Mutations","Necromancy","Omens","Permutations","Portals","Potions","Projections","Pyromancy","Rituals","Runes","Solar Magic","Spellcasting","Summoning","Technomancy","Teleportation","Transfigurations","Transformations","Transmutations","Voiceless Spellcasting","Wandless Spellcasting","Warding"];
var nm4 = ["Accidents","Areas","Castles","Celebrations","Ceremonies","Devices","Displays","Exhibitions","Festivals","Gadgets","History","Holidays","Incidents","Innovations","Inventions","Libraries","Locations","Memorials","Milestones","Performances","Permutations","Phenomena","Ruins","Sights","Sites","Spectacles","Towers","Triumphs","Wonders"];
var nm5 = ["","","","","","","","","","","","","","","","Abridged","Advanced","Basic","Beginner","Compact","Companion","Complete","Complex","Comprehensive","Core","Definitive","Detailed","Effective","Elemental","Essential","Extensive","Fundamental","Intermediate","New","Newbie","Novice","Pocket","Portable","Practical","Standard","Unabridged","Vital"];

var nm6 = ["Arcane","Challenging","Cursed","Dangerous","Delicate","Demanding","Difficult","Divine","Ethereal","Fragile","Holy","Legendary","Magical","Mild","Mythical","Novice","Popular","Potent","Powerful","Precious","Rare","Strange","Uncommon","Unholy","Unusual"];
var nm7 = ["Details of","Information on","Guide to","Dangers of","Handbook of","Guidebook of","Compendium of","Fundamentals of","Risks of","Stories of","Advice on","Data on"];
var nm8 = ["Abnormal","Ancient","Arcane","Bizarre","Brilliant","Common","Dangerous","Deadly","Delightful","Distant","Dynamic","Enchanted","Enchanting","Ethereal","Evasive","Everlasting","Exotic","Extinct","Fabulous","Famous","Fantastic","Favorite","Fierce","Forgotten","Frozen","Gentle","Grand","Grave","Great","Grim","Harmless","Hidden","Infamous","Interesting","Juvenile","Lost","Magic","Magical","Magnificent","Mighty","Mysterious","Mystical","Mythical","Nocturnal","Outlandish","Popular","Powerful","Protected","Rare","Scaly","Secret","Simple","Spiritual","Strange","Uncommon","Unique","Unknown","Unseen","Unwelcome","Vicious","Vital","Volatile","Weird","Wild"];


var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.random() * nm3.length | 0;
		if(i < 3){
			rnd = Math.random() * nm5.length | 0;
			rnd2 = Math.random() * nm7.length | 0;
			rnd3 = Math.random() * 3 | 0;
			if(rnd3 === 0){
				nmL = nm1[Math.random() * nm1.length | 0];
			}else if(rnd3 === 1){
				nmL = nm2[Math.random() * nm2.length | 0];
			}else{
				nmL = nm3[Math.random() * nm3.length | 0];
			}
			names = nm7[rnd2] + " " + nmL;
		}else if(i < 5){
			rnd = Math.random() * nm5.length | 0;
			rnd2 = Math.random() * nm7.length | 0;
			rnd3 = Math.random() * nm8.length | 0;
			rnd4 = Math.random() * nm4.length | 0;
			names = nm5[rnd] + " " + nm7[rnd2] + " " + nm8[rnd3] + " " + nm4[rnd4];
		}else if(i < 7){
			rnd = Math.random() * nm4.length | 0;
			rnd2 = Math.random() * nm8.length | 0;
			rnd3 = Math.random() * nm3.length | 0;
			names = nm4[rnd] + " of " + nm8[rnd2] + " " + nm3[rnd3];
		}else{
			rnd = Math.random() * nm8.length | 0;
			rnd3 = Math.random() * 3 | 0;
			if(rnd3 === 0){
				nmL = nm1[Math.random() * nm1.length | 0];
			}else if(rnd3 === 1){
				nmL = nm2[Math.random() * nm2.length | 0];
			}else{
				nmL = nm3[Math.random() * nm3.length | 0];
			}
			names = nm8[rnd] + " " + nmL;
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