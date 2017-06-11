var nm1 = ["Alpha","Anarchy","Angry","Argent","Arrowhead","Asphalt","Barbaric","Barking","Barrel","Bearded","Big","Bitter","Black","Blackhawk","Blazing","Blue","Booze","Border","Born","Broken","Burning","Burnt","Capital","Casual","Celtic","Chained","Chaos","Chasing","Chosen","Cold","Comet","Country","Crazy","Cunning","Dark","Dawn","Daylight","Dead","Derby","Devil's","Devoted","Die-Hard","Dirt","Dirty","Double","Dragon","Drunken","Dusk","Eastern","Endless","Fallen","Famous","Feral","Flying","Forward","Free","Freestyle","Freezone","Frosty","Frozen","Full Moon","Galloping","Gliding","Grave","Gravel","Grim","Hairy","Hardcore","Havoc","Horizon","Ignited","Independent","Infamous","Inferno","Inland","Insane","Iron","Jagged","Legendary","Liberty","Lightning","Little","Living","Lone","Long","Lost","Loud","Missing","Monster","Moonlight","Nameless","New","Night","Northern","Old","Phantom","Primal","Prime","Raging","Rebel","Reckless","Red","Restless","Rising","Road","Roaring","Rolling","Rough","Rugged","Rusty","Salvation","Savage","Shadow","Silent","Sleepless","Smokey","Smoking","Solo","Southern","Spartan","Spectral","Spiked","Steel","Storm","Thunder","Tribal","Triple","True","Twisted","Valley","Warped","Western","Wild"];
var nm2 = ["Aces","Alloys","Ancestors","Angels","Armada","Badgers","Bandidos","Bandits","Barbarians","Beanies","Beards","Bears","Bikers","Boars","Bones","Boots","Boys","Brotherhood","Brothers","Buzzards","Cannibals","Cats","Chariots","Chiefs","Clan","Cobras","Comets","Corps","Coyotes","Crew","Crows","Cruisers","Crusaders","Demons","Destroyers","Devils","Diablos","Disciples","Dogs","Dragons","Drakes","Drifters","Eagles","Emblems","Falcons","Fallen","Fathers","Fiends","Foxes","Freaks","Gargoyles","Ghosts","Girls","Griffins","Guardians","Heads","Hearts","Henchmen","Heretics","Highwaymen","Hogs","Horsemen","Horses","Hounds","Howlers","Hunters","Jackals","Jesters","Jokers","Keepers","Kings","Kingsmen","Knights","Legion","Legionnaires","Lions","Lords","Lovers","Machines","Marauders","Mavericks","Misfits","Mohawks","Mutants","Mutineers","Order","Outlaws","Owls","Panthers","Pirates","Pixies","Predators","Prowlers","Pythons","Raiders","Raptors","Rats","Reapers","Rebels","Renegades","Roadsters","Rockers","Rodents","Sabers","Saddles","Saints","Samurai","Scavengers","Scorpions","Sentinels","Shadows","Sidekicks","Sisterhood","Skulls","Slayers","Smugglers","Soldiers","Souls","Spades","Spiders","Spirits","Syndicate","Tigers","Travelers","Troopers","Vagabonds","Veterans","Vultures","Wanderers","Warriors","Weasels","Werewolves","Wheelers","Widows","Wings","Wolves"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm2.length);
		if(i < 2){
			names = "The " + nm2[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = "The " + nm1[rnd] + " " + nm2[rnd2];
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