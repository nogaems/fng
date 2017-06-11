var nm1 = ["Accord","Afterlife","Ambition","Animus","Ascendance","Augury","Azure","Bloom","Bravery","Brotherhood","Calypso","Celebration","Central","Charity","Clover","Coalition","Concord","Conquest","Courage","Creed","Crystal","Daydream","Desire","Diamond","Divine","Domination","Dominion","Dragon","Dream","Dreamland","Elemental","Elysium","Endurance","Epiphany","Epoch","Essence","Eternity","Euphony","Exhibition","Faith","Fame","Fealty","Federation","Fortitude","Fortune","Freedom","Fusion","Glory","Gold","Hallow","Harmony","Heart","Heaven's","High","High Point","History","Homage","Honor","Hope","Horoscope","Independence","Infinity","Innocence","Judgment","Justice","Kinship","Labor","Liberation","Liberty","Life","Light","Melody","Memorial","Mirage","Myriad","Observation","Obsidian","Onyx","Oracle","Orbit","Orchestra","Paradise","Parallel","Patience","Peace Blossom","Perseverance","Phoenix","Piety","Pilgrimage","Pinnacle","Pixel","Power","Prestige","Promise","Prophecy","Prospect","Prosperity","Purity","Rainbow","Rebirth","Reincarnation","Rejuvenation","Renaissance","Resolution","Resurrection","Reunion","Revelation","Reverence","Rose","Salvation","Sanguine","Sentience","Serenity","Silk","Silver","Sky","Skyreach","Snowflake","Solace","Solidarity","Solitude","Soul","Space","Spirit","Star","Starlight","Strength","Summit","Supremacy","Symbiosis","Symphony","Synthesis","Temperance","Tenacity","Trade","Tranquility","Tribulation","Tribute","Triumph","Trust","Truth","Twin","Union","Unison","Universe","Utopia","Valiance","Valor","Velvet","Victory","Vigor","Virtue","Vision","Wildlife","Zion"];
var nm2 = ["Ancestor","Ancient","Angel","Arch","Arrow","Ash","Azure","Barbarian","Bear","Behemoth","Berserker","Blade","Blood","Boar","Boulder","Broad","Bronze","Chaos","Corruption","Creed","Crescent","Crest","Crimson","Critter","Crown","Crypt","Crystal","Dagger","Dark","Daydream","Dead","Deer","Demon","Desolate","Dire","Dragon","Dread","Dream","Dust","East","Ebon","Echo","Ember","Emerald","Empyrean","Eternal","Fallen","Feral","Fiend","Fire","Forbidden","Forsaken","Fortune","Fossil","Freedom","Frenzy","Frost","Fury","Ghost","Gloom","Golden","Gossip","Grand","Gray","Great","Grim","Hallow","Harmony","Haunted","Heart","Heir","Heirloom","High","Hollow","Honor","Immortal","Imp","Imperial","Infinity","Iron","Jade","Lesser","Liberty","Light","Lily","Little","Low","Meditation","Memorial","Midsummer","Mighty","Miracle","Misty","Mithril","Monster","Monument","Mortal","Mystery","Nightmare","North","Oak","Obsidian","Onyx","Oracle","Outcast","Paradise","Peace","Pendulum","Phantom","Piety","Pine","Prestige","Primal","Prime","Primeval","Primordial","Rabid","Relic","Repose","Rose","Rotten","Rough","Royal","Ruby","Rune","Rust","Sacred","Sanctity","Sanguine","Sapphire","Savage","Secret","Serenity","Shade","Shadow","Silver","Sin","Skeleton","Sky","Smoke","Snow","Soul","South","Spirit","Spring","Stag","Steel","Storm","Summer","Talon","Terror","Thunder","Timeless","Trader","Traitor","Tranquility","Trinity","Twin","Velvet","Venom","Vestige","Vile","Weeping","West","Whisper","White","Wicked","Wild","Willow","Windy","Winter","Wisdom","Wolf","Wraith","Wrath","Wyvern"];
var nm3 = ["Atoll","Beach","Bluff","Bog","Brook","Cave","Cavern","Cliff","Coast","Copse","Creek","Den","Desert","Dune","Fen","Field","Forest","Garden","Glade","Grotto","Grounds","Grove","Hill","Isle","Jungle","Lagoon","Lake","Land","Loch","Meadow","Mire","Moor","Morass","Mound","Mountain","Park","Pasture","Peak","Plains","Range","Ridge","River","Shore","Sierra","Slope","Strand","Stream","Swale","Swamp","Territory","Thicket","Woods"];
var nm4 = ["Tower","Spire","Lookout","Mast","Pillar","Obelisk","Tower","Tower","Tower"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd4 = Math.floor(Math.random() * nm4.length);
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd] + " " + nm4[rnd4];
		}else{
			rnd = Math.floor(Math.random() * nm2.length);
			rnd2 = Math.floor(Math.random() * nm3.length);
			names = nm2[rnd] + " " + nm3[rnd2] + " " + nm4[rnd4];
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