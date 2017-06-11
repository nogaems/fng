var names1 = ["Aegis","Ambition","Amnesty","Armor","Bastion","Blessing","Chance","Charity","Chastity","Cherish","Citadel","Clemency","Comfort","Companion","Companionship","Company","Compassion","Conquest","Control","Courage","Covenant","Custody","Daydream","Delight","Desire","Dignity","Divinity","Dominion","Dream","Duty","Ecstasy","Eden","Elation","Elysium","Euphoria","Faith","Fantasy","Favor","Felicity","Fellowship","Fortitude","Fortune","Foster","Freedom","Glee","Glory","Goodwill","Guidance","Happiness","Harmony","Heart","Honesty","Honor","Hope","Immunity","Joy","Jubilee","Karma","Kudos","Liberty","Love","Luck","Majesty","Mercy","Mirth","Nourish","Nurture","Paradise","Parry","Passion","Piety","Prestige","Pride","Privilege","Promise","Purity","Redemption","Reliance","Remedy","Resistance","Respect","Return","Revolution","Safeguard","Salvation","Sanctuary","Solitude","Supremacy","Sweetness","Sympathy","Synthesis","Tribute","Triumph","Trust","Truth","Unity","Utopia","Victory","Vindicate","Virtue","Wish","Wonder","Zeal","Zion"];
var names2 = ["Abolition","Abyss","Agony","Anarchy","Animus","Annihilation","Apathy","Assassin","Aversion","Bane","Betrayal","Blaze","Blockade","Calamity","Carnage","Chaos","Condemned","Cruelty","Decimation","Defeat","Delirium","Demolition","Denial","Desertion","Desolation","Despair","Destruction","Detention","Disarray","Disbelief","Disgrace","Dishonor","Disruption","Disunion","Dominance","Doom","Doubt","Downfall","Elimination","Entropy","Eternity","Extermination","Extinction","Fear","Ferocity","Fluke","Forfeit","Forsake","Frenzy","Fury","Hallow","Hate","Hatred","Havoc","Hazard","Hostility","Hysteria","Impotence","Inferno","Injury","Isolation","Limbo","Malevolence","Malice","Mania","Massacre","Mayhem","Melancholy","Misfortune","Murder","Nether","Nightmare","Obstruction","Overlook","Peril","Pity","Poverty","Prohibition","Rage","Rampage","Ravage","Relinquish","Restraint","Riot","Sanctity","Shatter","Silence","Slaughter","Slayer","Sorrow","Spite","Stigma","Storm","Struggle","Submission","Surrender","Torment","Treachery","Turmoil","Umbrage","Uproar","Venom","Violence","Void","Wasteland","Wilderness","Woe","Worship","Wrath","Wreckage"];
var names3 = ["Alpha","Alpine","Altar","Angel","Angel Wings","Anomaly","Aqua","Aquamarine","Arachnid","Arrowtip","Astro","Aurora","Avalanche","Azure","Bandana","Bear Paw","Black Crow","Blue Banner","Boulderfist","Braveheart","Brown Bear","Bullet","Bullettooth","Bumblebee","Butterfly","Cannonball","Castaway","Comet","Coyote","Crescent Moon","Crimson","Crossbow","Daemon","Darkwind","Dawn","Daybreak","Daylight","Demon","Diamond","Dragonfire","Dragonfly","Dragontooth","Dusk","Eagle Eye","Ebony","Echo","Eclipse","Effigy","Emerald","Energy","Enigma","Eventide","Fable","Falcon","Fallen Oak","Firefly","Frozen Lake","Full Moon","Gadget","Gemini","Gizmo","Glacier","Grasshopper","Heartbreak","Heartfire","High Tide","Highlands","Howling Wolf","Hummingbird","Hurricane","Ivory","Jadefire","Jasmine","Jester","Kite Shield","Light Beacon","Lightning","Lightning Strike","Lion Roar","Lockdown","Lockheart","Lone Wolf","Maggot","Major","Malachite","Maple Leaf","Maverick","Merlin","Midnight","Minor","Mirage","Mirror Image","Monsoon","Moonstone","Morningstar","Mountain Peak","Nemo","New Moon","Night Beacon","Night Owl","Nightfall","Nighttide","Omega","Open Door","Overlook","Pedestal","Phantasm","Phoenix","Quicksilver","Rabbit's Foot","Radiance","Raindrop","Red Banner","Saffron","Sapphire","Satellite","Scarlet","Serpent","Shark Fin","Shooting Star","Silver Lining","Silver Shadow","Snowflake","Solar Beam","Solar Flare","Solstice","Stardust","Starfall","Starlight","Stormgaze","Straight Arrow","Sundance","Sundown","Sunset","Sunshine","Thunderclap","Thunderstorm","Tiger Claw","Tiger Lilly","Torchbearer","Tortoise","Turtle Shell","Twilight","Viper","Waterfall","Whisper","Wild Card","Wild Horse","Willow","Woodpecker"];
function nameGen(){
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 3){
			rnd = Math.floor(Math.random() * names1.length);
			names = "Camp " + names1[rnd];
		}else if(i < 6){
			rnd = Math.floor(Math.random() * names2.length);
			names = "Camp " + names2[rnd];
		}else{
			rnd = Math.floor(Math.random() * names3.length);
			names = "Camp " + names3[rnd];
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