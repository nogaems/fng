function nameGen(type){
	var nm1 = ["Aether","Ancient","Ancient Oak","Aurora","Azure","Balance","Beating Heart","Blue Moon","Boulder","Bramble Root","Brilliant Light","Cascade","Cedar Grove","Chalice","Charity","Clarity","Community","Compassion","Convert","Crescent","Crescent Moon","Crystal Flower","Crystal Garden","Crystal Lake","Crystal Rose","Discovery","Divine","Divine Dream","Divine Energy","Divine Journey","Divine Spirit","Divine Teachings","Divine Touch","Dream","Earth Spirit","Earth Temple","Earthen","Eclipse","Elder Flame","Elder Grove","Elemental","Elemental Grove","Elysium","Ember","Enchanted","Enchanted Moon","Enchanted Tree","Enlightened","Equinox","Eternal Flame","Eternal Garden","Eternal Light","Eternal Teachings","Eternity","Fae Woods","Faery Tree","Forest Grove","Forest Path","Fortuna","Freedom","Full Moon","Goddess","Grass Roots","Grove","Guiding Hand","Hallowed","Hallowed Guide","Harmony","Harvest","Healing","Hyacinth","Ice Garden","Illuminated","Illumination","Independence","Infinity","Knowledge","Lady Fortune","Liberty","Light","Lode Star","Lone Star","Lunar","Lunar Owl","Medicine","Midnight","Mirror","Mirror Lake","Moon","Moon Oasis","Moon Siren","Moon Temple","Moon Thicket","Moon Thread","Moonlight","Moonlit","Moonlit Cloud","Moonrise","Morning Dew","Morning Star","Mountain Rose","Mystic","Mystic Grove","Night Garden","Night Grove","Nightshade","Nightshadow","Nightsky","Oak Spirit","Oasis","Observation","Patience","Pentacle","Phoenix Fire","Presence","Quiet Meadows","Radiant Heart","Raven","Raven's Nest","Requiem","Revolution","Rising Sun","River","Rowan Tree","Sacred","Sacred Flame","Sacred Journey","Sacred Meadows","Sacred Voyage","Sacred Well","Serenity","Setting Sun","Shadowmoon","Silver","Silver Branch","Silver Cloud","Silver Flame","Silver Flock","Silver Grace","Silver Grass","Silver Lake","Silver Moon","Silver Reserve","Silver Sliver","Silver Star","Silver Thread","Silverbark","Solar","Spiral Tree","Spirit Drum","Spirit Energy","Spirit Lake","Stardust","Starfall","Starlight","Sunset","Tree Roots","Trillium Moon","Trinity","Twilight","Twilight Flame","Twilight Goddess","Twilight Grove","Unseen Moon","Voyage","White Lotus","White Tree","Willow","Wisdom","World Tree"];
	var nm2 = ["Azure","Balance","Charity","Clarity","Community","Compassion","Discovery","Divine Energy","Divine Teachings","Elysium","Ember","Eternal Teachings","Eternity","Fortuna","Freedom","Harmony","Healing","Illumination","Independence","Infinity","Knowledge","Lady Fortune","Liberty","Medicine","Midnight","Moonlight","Morning Dew","Nightshade","Nightshadow","Observation","Patience","Phoenix Fire","Presence","Requiem","Sacred Meadows","Serenity","Shadowmoon","Silver","Silver Grace","Silver Grass","Spirit Energy","Stardust","Starfall","Starlight","Tree Roots","Twilight","Wisdom","the Aether","the Ancient","the Ancient Oak","the Aurora","the Beating Heart","the Blue Moon","the Boulder","the Bramble Root","the Brilliant Light","the Cascade","the Cedar Grove","the Chalice","the Convert","the Crescent","the Crescent Moon","the Crystal Flower","the Crystal Garden","the Crystal Lake","the Crystal Rose","the Divine","the Divine Dream","the Divine Journey","the Divine Spirit","the Divine Touch","the Dream","the Earth Spirit","the Earth Temple","the Earthen","the Eclipse","the Elder Flame","the Elder Grove","the Elemental","the Elemental Grove","the Enchanted","the Enchanted Moon","the Enchanted Tree","the Enlightened","the Equinox","the Eternal Flame","the Eternal Garden","the Eternal Light","the Fae Woods","the Faery Tree","the Forest Grove","the Forest Path","the Full Moon","the Goddess","the Grass Roots","the Grove","the Guiding Hand","the Hallowed","the Hallowed Guide","the Harvest","the Hyacinth","the Ice Garden","the Illuminated","the Light","the Lode Star","the Lone Star","the Lunar Owl","the Mirror","the Mirror Lake","the Moon","the Moon Oasis","the Moon Siren","the Moon Temple","the Moon Thicket","the Moon Thread","the Moonlit","the Moonlit Cloud","the Moonrise","the Morning Star","the Mountain Rose","the Mystic","the Mystic Grove","the Night Garden","the Night Grove","the Night Sky","the Oak Spirit","the Oasis","the Pentacle","the Quiet Meadows","the Radiant Heart","the Raven","the Raven's Nest","the Revolution","the Rising Sun","the River","the Rowan Tree","the Sacred Flame","the Sacred Journey","the Sacred One","the Sacred Voyage","the Sacred Well","the Setting Sun","the Silver Branch","the Silver Cloud","the Silver Flame","the Silver Flock","the Silver Lake","the Silver Moon","the Silver Reserve","the Silver Sliver","the Silver Star","the Silver Thread","the Silverbark","the Spiral Tree","the Spirit Drum","the Spirit Lake","the Sun","the Sunset","the Trillium Moon","the Trinity","the Twilight Flame","the Twilight Goddess","the Twilight Grove","the Unseen Moon","the Voyage","the White Lotus","the White Tree","the Willow","the World Tree"];
	var nm3 = ["Coven","Circle","Sisters","Wives","Witches","Coven","Coven","Circle","Circle","Coven"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.random() * nm3.length | 0;
		if(i < 5){
			rnd = Math.random() * nm1.length | 0;
			names = "The " + nm1[rnd] + " " + nm3[rnd2];
			nm1.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm2.length | 0;
			names = nm3[rnd2] + " of " + nm2[rnd];
			nm2.splice(rnd, 1);
		}
		nm3.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}