var nm1 = ["Accord of","Aeon of","Affinity of","Ambience of","Ambition of","Ashes of","Aspiration of","Aura of","Aurora of","Balance Brings","Balance of","Bornstellar Makes","Bright Wind of","Bringer of","Cautious Voice of","Choice of","Comet of","Darkness of","Dawn of","Desire of","Destiny of","Divinity from","Divinity of","Dreams of","Drift of","Dusk of","Dust of","Echo of","Empathy of","Eos of","Equilibrium Grants","Equilibrium of","Essence of","Eternal Rest of","Eternity Bears","Fabor of","Fallen Beneath","First Light Weaves","Fragment of","Future of","Galaxy Grants","Gift of","Glorious Light of","Gravity Grants","Harmony Gives","Harmony of","Heirloom of","Heritage of","Hope of","Hunger of","Infinity Brings","Legacy of","Life Gives","Life Grants","Light Brings","Light of","Love of","Memories of","Moment of","Nebula of","New Dawn Grants","Order of","Paradox of","Particle of","Peace of","Pleasure of","Prayer of","Pursuer of","Rays of","Resilience of","Resonance of","Rest of","Retinence Bears","Seeker of","Shadow of","Shard of","Silver Moon Brings","Sliver of","Sound of","Speed of","Spirit of","Splendid Dust of","Sympathy Makes","Tempest of","Time of","Tone of","Torrent of","Tranquility of","Truth Dreams","Truth of","Vision of","Twist of","Unity Weaves","Unity of","Veil of","Veiled Dream of","Veiled Light","Vengeance of","Voice of","Wanderer of","Wish of"];
var nm2 = ["Ancient Stars","Animation and Life","Awareness","Black Void","Broken Nebula","Broken World","Caution and Poise","Celestial Body","Clarity and Purity","Clarity and Reason","Confident Future","Cosmic Infinity","Crimson Light","Curiosity","Darkness","Desire","Desired Future","Discipline","Distant Planet","Diversity","Divided World","Dying Stars","Dying World","Endless Void","Endurance and Durability","Eternal Cycles","Eternal Day","Eternal Happiness","Eternal Knowledge","Eternal Lasting","Eternal Legacies","Eternal Night","Eternal Stars","Eventual Redemption","Falling Skies","Fate and Destiny","Fire and Water","Fleeting Dreams","Fleeting Globe","Fleeting Memories","Fleeting Space","Floating Worlds","Forgotten Moon","Fortitude","Hopeful Legacy","Humble Mind","Ice and Water","Illumination","Inevitability","Infinite Knowledge","Infinite Moonlight","Infinite Starlight","Infinite Struggle","Inspiration","Intricate Design","Judgment","Knowledge and Power","Last Words","Life and Death","Light and Darkness","Limunous Bodies","Living Song","Living World","Lost Vision","Lost Worlds","Love and Grace","Luminous Light","Mind and Power","Neutrality","Night and Day","Orbital Life","Past Legacy","Perpetual Conflict","Perpetual Motion","Planetary Life","Pleasure","Primordial Light","Prominence","Quality and Purity","Reason","Reborn Planet","Redemption","Reflection and Retrospection","Renewed Faith","Sands of Time","Serenity and Trust","Shooting Star","Simplicity","Stability and Balance","Stars Eternal","Stars and Planets","Sundered Star","Symmetry","Trust and Faith","Twisted Fate","Value and Virtue","Wandering Star","Warped Space","Will and Might","Wisdom and Knowlege"];

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