var nm1 = ["Aegis","Aerospace","Air Space Independence","Allied","Amalgamation","Amity","Ancestral","Angelic","Anti-Terror","Arcane","Archangel","Archetype","Armament","Armistice","Ashed","Assembled","Assisted","Axis","Bastion","Blessed","Bulwark","Cardinal","Celestial","Central","Cerberus","Champion","Citadel","Commanding","Confederated","Confederation","Cooperation","Cosmic","Cosmos","Counter Terror","Crimson","Curator","Custodian","Custody","Defenders","Defending","Diplomatic","Divine","Domination","Dread","Dual","Earthen","Ebon","Empire","Environment Defense","Epitome","Equilibrium","Eternal","Faithful","First","First Aid","Fortification","Freedom","Fundamental","Galactic","Galactic Security","Galaxy Supervision","Galaxy Watch","Ghost","Global Authority","Global Combat","Global Economic","Global Financial","Global Food","Global Immunity","Global Industry","Global Inquisition","Global Insurance","Global Integrity","Global Intelligence","Global Jurisdiction","Global Justice","Global Prosperity","Global Protection","Global Sanctuary","Global Shield","Global Support","Global Surveillance","Global War","Global Watch","Global Welfare","Golden","Good Will","Grand","Guardian","Guardianship","Hallowed","Harmony","Harvest","Heavenly","Highborn","Holy","Immunity","Imperial","Independent","Industry","Inquisition","Integration","Integrity","Intercontinental Security","Interference","Intergalactic","International Security","Interstellar Administration","Interstellar Domination","Intimidation","Invulnerability","Ivory","Jewel","Kinship","Liberated","Little","Magistracy","Mutual Defense","Mutual Support","Mystic","Mythic","Nature","Nature Preservation","Next World","Noble","Nonaggression","Nuclear","Nuclear Protection","Obsidian","Occult","Onyx","Oracle","Pacifist","Paladin","Paragon","Paramount","Peace","Peacekeeper","Peacemonger","Phantom","Phoenix","Pious","Preservation","Prime","Primeval","Primordial","Prophecy","Protection","Quadruple","Radical","Rampart","Redemption","Regal","Reincarnation","Reinforcement","Resistance","Resurrection","Retribution","Revelation","Revitalization","Righteous","Royal","Sacred","Sacred World","Salvation","Sanctified","Sanctuary","Sanguine","Scientific Progress","Security","Self-Defense","Sentinel","Seraphic","Shepherd","Silver","Sovereign","Space Combat","Space Command","Stabilization","Steward","Strike Force","Supreme","Surveillance","Terror Defiance","Terror Opposition","Terror Response","Terror Supervision","Triple","Truce","Undivided","Unified","United","Unity","Utopian","Vigilante","Vortex","Watchdog","Wildlife Conservation","Wildlife Preservation","Wildlife Shelter","World Aid","World Authority","World Equilibrium","World Freedom","World Health","World Keeper","World Peace","World Preservation","World Provision","World Supervision","World Sustenance"];
var nm2 = ["Alliance","Bond","Coalition","League","Nations","Treaty","Union","Federation","Confederation","Syndicate"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = "The " + nm1[rnd] + " " + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}