var nm1 = ["Adamant","Angel","Animal","Apocalypse","Arachnid","Arcane","Arch","Ashen","Aura","Barbarian","Barbaric","Barbed","Beastly","Behemoth","Bleak","Blood","Bloodied","Bone","Brilliant","Broken","Burning","Burnt","Butcher","Chaos","Cold","Corpse","Corrupt","Covert","Crescent","Crimson","Crumbled","Crushed","Crystal","Cursed","Dead","Deceiver","Demon","Deranged","Desert","Destiny","Devil","Diabolic","Diamond","Dire","Dishonored","Dragon","Dragonfire","Dread","Dream","Drunk","Ebon","Elemental","Elite","Ember","Eternal","Evil","Exalted","Exile","False","Feeble","Fire","Flower","Forlorn","Forsaken","Frozen","Funereal","Gentle","Ghost","Giant","Gilded","Glass","Glistening","Glowing","God","Graceful","Grand","Granite","Grave","Great","Green","Grim","Heavenly","Hell","Hellish","High","Holy","Horror","Hostile","Ice","Illusion","Impish","Impure","Industrious","Infernal","Insane","Iron","Isolated","Ivory","Jade","Legendary","Lich","Light","Lightning","Lizard","Lonely","Loyal","Lucky","Lunar","Mad","Magic","Magma","Malicious","Marsh","Master","Midnight","Mighty","Mindless","Mithril","Molten","Monster","Mountain","Mourning","Muddy","Mutant","Mute","Mystic","Necro","Nefarious","Nightmare","Noble","Obscure","Obsidian","Occult","Ocean","Onyx","Outcast","Paragon","Peasant","Phantom","Phoenix","Placid","Plague","Primal","Prime","Prophecy","Psycho","Puppet","Rabid","Ragged","Rainbow","Reaper","Regal","Renegade","Rose","Rotten","Royal","Ruined","Rune","Sable","Sanguine","Sapphire","Savage","Serpent","Shadow","Shielded","Silent","Sinister","Sinner","Skull","Sleeping","Smoldering","Snow","Solar","Sorrow","Soul","Spider","Spine","Spirit","Spiteful","Steel","Storm","Strife","Sullen","Supreme","Surface","Talon","Terror","Thorn","Thunder","Timeless","Titan","Torment","Traitor","Tranquil","Twilight","Undead","Unholy","Venom","Vile","Violet","Volcanic","Warlord","Water","Wayward","Welfare","Wicked","Widow","Wild","Winged","Wooden","Zodiac"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = "The " + nm1[rnd] + " Throne";
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}