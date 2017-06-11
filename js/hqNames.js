var nm1 = ["Abyss","Allegiance","Animus","Argent","August","Basilisk","Blood's","Bravery","Brotherhood","Paradise","Bulwark","Cardinal","Bloodlust","Bloodfall","Bloodmoon","Deepwood","Dragonclaw","Dragontooth","Dreamland","Ironbark","Liontooth","Thunderstorm","Blackwing","Stormkeeper","Archangel","Dynasty","Nemesis","Blackout","Illusion","Soulseeker","Nemo","Ironwing","Ashes","Fullmoon","Diablo","Clockwork","Otherworld","Winterspell","Juggernaut","Whiteheart","Starfall","Starlight","Nova","Requiem","Armada","Ironheart","Stormwatch","Vanguard","Battlestar","Miracle","Lifeblood","Compass","Nightsong","Vengeance","Starchild","Moonsong","Shadowsong","Shadowheart","Dragonland","Dragonfire","Destiny","Stormkeeper","Battleborn","Salvation","Flameheart","Stonebend","Ironscream","Shademantle","Hallowflame","Mastervale","Doomvale","Doomwhisper","Burningtide","Blackhallow","Sacredcrest","Sungazer","Moongazer","Saurhorn","Highbreeze","Stormbreath","Frostvale","Starchaser","Embermane","Cresthelm","Whiteblood","Runeforge","Spiritcrest","Cloudspire","Brightforest","Coldhammer","Skysword","Skyward","Battlebloom","Crimsonblade","Amberwood","Frostwolf","Flamewarden","Stormweaver","Lunacrest","Solarcrest","Skullcrest","Frozenhell","Cinderbane","Moonblade","Winterwatch","Crimsonwatch","Summerguard","Autumnward","Springforge","Shadowhorn","Titanrun","Darksong","Whispervale","Swiftstrike","Pathfinder","Vagabond","Trailblazer","Centurion","Sentinel","Shepherd","Watchdog","Curator","Cerberus","Steward","Custodian","Overseer","Gamekeeper","Chaos","Cinder","Cobalt","Conquest","Creed's","Crossroad","Dawn","Daydream","Death's","Demise","Desolation","Dragon","Dusk","Echo","Eclipse","Elysium","Ember","Enigma","Epoch","Exile","Exodus","Falcon","Fortitude","Freedom","Fury","Galaxy","Glory","Grace","Grim","Harbinger","Harmony","Heaven's","Herald","Honor's","Hope's","Independence","Judgement","Justice","Karma","Liberty","Light's","Memorial","Mercy","Mirage","Mirror","Nexus","Oblivion","Oracle","Outcast","Phoenix","Pilgrimage","Pinnacle","Plague","Premonition","Promise","Prophecy","Purpose","Rebirth","Renegade","Revelation","Sabre","Salvation","Serenity","Serpent","Shadow","Shadow's","Sisterhood","Solace","Solitude","Solstice","Specter","Spirit","Tempest","The Adamantine","The Amaranthine","The Amber","The Ancestral","The Arcane","The Astral","The Azure","The Black","The Blessed","The Bronze","The Celestial","The Cerulean","The Crescent","The Crimson","The Crystal","The Divine","The Ebon","The Emerald","The Eternal","The Ethereal","The Fel","The Frozen","The Granite","The Grim","The Hallow","The Infernal","The Invincible","The Invisible","The Iron","The Ivory","The Jade","The Lost","The Matriarch","The Misty","The Mithril","The Molten","The Moon","The Mythic","The Nether","The Night","The Nightmare","The Obsidian","The Onyx","The Patriarch","The Sanguine","The Scarlet","The Shadow","The Silent","The Silver","The Solar","The Sun","The Titan","The Velvet","The Violet","The Vortex","Thunder","Titan's","Tranquility","Tribute","Triumph","Utopia","Vengeance","Victory","Virtue","Vitality","Warden","Watcher's","Wisdom"];
var nm2 = ["Base","Bastion","Castle","Citadel","Estate","Fortress","Garrison","Harbor","Headquarters","Island","Isle","Keep","Manor","Mansion","Post","Sanctuary","Sanctum","Station","Stronghold","Tower","Towers","Watchtower"];
var nm3 = ["Abyss","Aerie","Animus","Anomaly","Anvil","Apex","Archetype","Armada","Asteroid","Asylum","Aurora","Bastion","Beacon","Bulwark","Burrow","Cardinal","Centurion","Citadel","Clover","Compass","Crescent","Curiosity","Dragonclaw","Echo","Eclipse","Elysium","Ender","Enterprise","Epoch","Exodus","Felicity","Garden","Glory","Hammer","Haven","Heart","Homage","Horoscope","Jewel","Jubilee","Juggernaut","Lament","Lodestar","Majesty","Marshal","Matriarch","Matron","Memento","Minaret","Miracle","Mirage","Monolith","Nemesis","Nest","Nexus","Oasis","Obelisk","Odyssey","Omen","Onyx","Oracle","Ornament","Outcast","Paradox","Paragon","Patriarch","Patron","Phenomenon","Phoenix","Pinnacle","Prodigy","Pyre","Razor","Requiem","Sanctum","Serenity","Snowflake","Solstice","Spectacle","Spire","Talon","Tempest","Torch","Tribute","Triumph","Twin","Utopia","Veil","Vendetta","Vertex","Void","Vortex","Zenith"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + " " + nm2[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			names = "The " + nm3[rnd];
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