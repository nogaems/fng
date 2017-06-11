var nm1 = ["Accolade","Accomplishment","Achievement","Adventure","Ancestor","Animus","Anniversary","Apex","Art","Augury","Azure","Blue Moon","Capitol","Castle Square","Cathedral","Celebration","Central","Century","Ceremony","Cerulean","Champions'","Cherry Blossom","City Hall","Civic","Clover","Coconut","Commemoration","Community","Conquest","Crescent","Crystal","Daydream","Delicacy","Democracy","Desire","Devotion","Diamond","Discovery","Divinity","Dream","Dreamer","Duty","Effigy","Elegance","Elemental","Elysium","Emerald","Enchantment","Epiphany","Eternity","Euphony","Execution","Exploration","Fantasy","Festival","Firefly","Fortitude","Fortune","Founders'","Freedom","Galaxy","Gemstone","Glory","Golden","Good Omen","Grand","Grand Fountain","Grand Gala","Grand Harbor","Grand Market","Grand Meadow","Grand Palace","Grand Sanctum","Grand Splendor","Grand Treasure","Grapevine","Harbinger","Harmony","Heart's","Heaven's","Heroes'","History","Homage","Honor","Hope","Icewater","Illumination","Illusion","Independence","Infinity","Innocence","Innovation","Inspiration","Ivory","Jubilee","Justice","King","Kinship","Legion","Lemontree","Liberation","Liberty","Light","Lilypad","Love","Lovers'","Loyalty","Luminus","Lunar","Luxury","Magic","Majesty","Marble","Market","Marriage","Marvel","Melody","Memorial","Memory","Millennium","Miracle","Mirage","Monolith","Monument","Moonlight","Muse","Myriad","Mystic","Nature's","Nebula","New Haven","New Hope","Obelisk","Observation","Obsidian","Old Town","Opulence","Oracle","Orchard","Orchestra","Palm Leaf","Paradise","Paragon","Paramount","Passion","Peace Blossom","Peace Garden","Peacock","Pearl","People's","Perseverance","Phantasm","Phenomenon","Phoenix","Pilgrimage","Pinnacle","Pioneer","Pleasantview","Preservation","Prism","Prodigy","Promise","Prophecy","Prosperity","Public","Pyramid","Rainbow","Rebirth","Reflection","Refuge","Renaissance","Republic","Resonance","Revelation","Rose Petal","Royalty","Ruby","Sanctuary","Sanguine","Sapphire","Seduction","Sensation","Serenity","Settlers'","Silk","Silver","Silver Moon","Silver Oak","Silver Shrine","Sky","Snowflake","Solar","Songbird","Spring Gardens","Starlight","Statue","Summer Gardens","Supremacy","Sweet Delight","Sweetheart","Symphony","Temple","Tenacity","Timeless","Town Hall","Tranquility","Tribulation","Tribute","Trinity","Triumph","Trophy","Truth","Umbrella","Union","Unity","Universe","University","Utopia","Valiance","Velvet","Veneration","Venture","Vertex","Victory","Vigor","Vineyard","Virtue","Visionary","White Blossom","White Willow","Wishmaster","Wonder","Yesteryear","Zion"];
var nm2 = ["Plaza","Square"];
var br = "";

function nameGen(){
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