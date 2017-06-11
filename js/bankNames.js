var nm1 = ["Bancorp","Bancshares","Bank","Bank Corp.","Bank Group","Bank Inc.","Bank System","Banks","Banks Inc.","Corporation","Credit Union","Financial","Financial Corp.","Financial Group","Financial Holdings","Financial Inc.","Financial Services","Holding Company","Holdings","Holdings Inc.","Trust","Trust Corp."];

function nameGen(){
	var nm2 = ["Absolute","Ace","Aegis","Agnate","Allied","Alpha","Apex","Apogee","Arcadia","Archetype","Armament","Ascension","Aspire","Associated","Assurance","Aurora","Azure","Bastion","Better Life","Big Heart","Bolt","Boon","Bright Horizon","Bulwark","Caliber","Capital","Celestial","Central","Champion","Citadel","Citizen Service","Citizen Union","Citizens First","City Ward","Cloud Nine","Clover","Cognate","Commonwealth","Community","Concorde","Connection","Core","Credence","Credit","Crest","Crown","Dawn","Diamond","Diligence","Domestic","Dominion","Duty","Edge","Elite","Elysium","Emblem","Eminence","Epitome","Essence","Esteem","Evolution","Excellence","Faith","Federal","Felicity","Fidelity","First","First Choice","First Guaranty","Flow","Focus","Foundation","Fountain","Free Citizen","Fundament","Gemstone","General","Generation","Genesis","Global Network","Globe","Gold Alliance","Gold Credit","Goldcorp","Golden Gates","Goldguard","Goldleaf","Goldward","Goodlife","Grade","Grand Credit","Grand Fortune","Grand Market","Grand Mutual","Grand Spire","Grand Summit","Green Market","Green Valley","Groundwork","Her Majesty","High Rise","His Majesty","Joint","Jones","Kindred","Life Essence","Life Tree","Lifespark","Lightning","Marshall","Meridian","Midland","Miracle","Monolith","Nation","National","New Alliance","New Blossom","New Civil","New Connection","New Corporate","New Edge","New Generation","New Heights","New Horizon","New Leaf","New Life","New National","New Sense","New Wave","New Wealth","Obelisk","Obsidian","Ocean","Oculus","Omega","One Capital","One Duty","One Nation","Origin","Padlock","Paradise","Paragon","Paramount","Phoenix","Pillar","Pinnacle","Polestar","Premium","Prime","Primo","Principal","Principle","Private","Private Citizen","Prominence","Prosperity","Provenance","Pulse","Purity","Pursuit","Reliance","Repose","Republic Citizens","Resolution","Rose","Royal Crown","Sky High","Skyward","Snowflake","Soar","Solace","Soul","South Trust","Sparkle","Spotlight","Spring","Springwell","Sprout","State","Sublime","Summit","Sunray","Surge","Syndicate","Trust","Trustcorp","United","Value","Velvet","Vertex","Victory","Vigor","Virtue","Vitality","Voyage","Ward","Wellness","Wellspring","Zenith","Zion"];
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm2[rnd2] + " " + nm1[rnd];
		nm2.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}