var nm1 = ["Administrative","Advanced Weaponry","Aerial","Aeronautical","Air Assault","Air-Defense","Airborne","Aircraft","Airforce","Ammo Supply","Android","Angel","Animal","Antiaircraft","Aquatic","Archery","Armored","Artillery","Assault","Avian","Aviation","Ballistae","Banner","Barrage","Barricade","Battle Drum","Biological","Blitz","Blitzkrieg","Bombardment","Border","Bulwark","Camouflage","Cannon","Cartographing","Catapult","Catering","Cavalry","Challenger","Champion","Chaos","Charge","Chariot","Chemical","Chemical Defense","Chopper","Cleanup","Commando","Communications","Construction","Coordination","Correctional","Covert","Creature","Crossbow","Desert","Discipline","Domestic Communications","Domestication","Doom","Dragon","Education","Elephant","Emergency","Energy","Enforcement","Engineering","Eradication","Escort","Espionage","Ethereal","Extraction","Financial","Fire","First Response","Flamethrower","Flintlock","Forest","Galactic","Garrison","Ghost","Gladiator","Glory","Grenadier","Grunt","Guard","Guardian","Guerilla","Healer","Hidden","Honor","Hostage","Hunter","Imperial","Infantry","Information","Intergalactic","Internal Relations","International Relations","Interrogation","Invasion","Investigation","Jungle","Jurisdictional","Knight","Labor","Legal","Legionnaire","Legislative","Liberation","Light","Local Relations","Logistics","Lunar","Mage","Magic","Maintenance","Marine","Maritime","Martyr","Mastermind","Mechanical","Media","Medical","Mercenary","Mercurial","Mercy","Missile Defense","Mobile","Mortar","Mountain Division","Mounted","Nautical","Naval","Night","Nightmare","Nuclear","Nuclear Defense","Nutrition","Ocean","Offensive","Onslaught","Orbital","Orbital Defense","Overwatch","Paladin","Paratrooper","Pathfinder","Patrol","Peon","Phantom","Pirate","Plague","Preparation","Preservation","Prisoner","Private","Provision","Public Relations","Ranger","Reconnaisance","Reconstruction","Recovery","Recreation","Red Alert","Redemption","Regulation","Rehabilitation","Reinforcement","Relief","Rescue","Resistance","Restoration","Rifle","River","Robot","Rogue","Saddle","Salvage","Salvation","Sanction","Scouting","Sea","Security","Sentinel","Shadow","Shield","Shock","Siege","Signal","Skirmish","Slave","Slingshot","Sniper","Snow","Space","Spec Ops","Special Forces","Stabilisation","Stakeout","Stalker","Stealth","Storm","Stormtrooper","Strategy","Subaquatic","Submarine","Subterranean","Subterrestial","Suicide","Sunken","Supervision","Supply","Support","Surveillance","Survey","Surveyance","Sustenance","Tank","Telecommunications","Templar","Terror","Thunder","Torment","Torture","Training","Transport","Trauma","Trebuchet","Treetop","Trench","Tunneler","UAV","Undercover","Underground","Unmanned","Vanguard","Veteran","Veterinary","Victim Aid","Victory","Volunteer","War Dog","War Machine","Warband","Warhammer","Warmaster","Warrior","Weaponry","Winged"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd] + " Division";
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}