
function nameGen(){
	var nm1 = ["Apparate","Beam","Blink","Body Flicker","Bounce","Broadcast","Bunnyhop","Burst","Bypass","Conversion","Cross","Crosscut","Crossover","Depart","Detour","Deviate","Dimension Door","Discharge","Echo","Escape","Ether Leap","Ethereal Pass","Etheric Transfer","Fae Walk","Flash","Flicker","Flip-flop","Flutter","Flux","Fluxuate","Geo Burst","Geo Dash","Geo Deflect","Geo Leap","Geo Pass","Geo Relocation","Geocast","Geodrift","Geoflect","Geogenerate","Geomorphosis","Geoport","Geostep","Geotemper","Geovolve","Glimmer","Jolt","Light Step","Lightning Step","Localeap","Omit","Pass","Pass Through","Plane Step","Plane Walk","Portal","Pulse","Pulse Pass","Quantum Leap","Quick Shift","Quick Switch","Quick Transit","Quick Travel","Quickstep","Radiate","Relocaleap","Relocate","Relocation","Relocus","Resurge","Shadowstep","Shift","Shortcut","Sidestep","Skip","Skipstep","Skirt","Slipstream","Space Jump","Split Step","Stream","Streamstep","Switch","Take Flight","Tele","Tele Out","Telecast","Teleskip","Transfer","Transflux","Transkip","Translocation","Transmaterialize","Transmit","Transtep","Transwarp","Tripskip","Void Step","Warp","Wink"];

	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd];
		nm1.splice(rnd, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}