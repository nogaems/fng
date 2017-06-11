var nm1 = ["","","","","","","","","","","","","","","","","","","","","","Adaptable","Altered","Amplified","Analytical","Animal Powered","Aquatic","Atmospheric","Augmented","Automated","Auxiliary","Bionic","Comprehensive","Computerized","Diagnostic","Electromagnetic","Electronic","Encrypted","Enhanced","Experimatic","Experitron","Explosive","Extended","Extraordinary","Extrematic","Gizmatic","Global","Heavy","Heavy-Duty","Improved","Light","Lunar","Medical","Medium","Military","Mini","Miniature","Mobile","Modified","Multifunctional","Omni","Optimal","Optimized","Portable","Precise","Progressive","Reformed","Reinforced","Revised","Robotic","Robotized","Selfaware","Solar","Super","Superior","Surface","Synthesized","Synthetic","Systematic","Tactical","Titanium","Versatile","Volatile"];
var nm2 = ["A.I.","Aid","Air","Ammo","Antidote","Antivenom","Assist","Aura","Barrier","Battle","Biopsy","Blackout","Blockade","Blood","Bomb","Bone","Broadcast","Care","Casualty","Cell","Chemical","Clay","Cloud","Code","Combat","Comfort","Construction","Cooking","Crime","Crop","Cure","Data","Defence","Disaster","Disease","Dream","Echo","Emergency","Essence","Exam","Farm","Fire","First Aid","Flame","Flood","Food","Ghost","Guidance","Hazard","Heal","Hologram","Ice","Idea","Laser","Life","Light","Load","Luggage","Lumination","Magnet","Measurement","Medicine","Message","Mimic","Mine","Mold","Moon","Motion","Mountain","Navigation","Noise","Nutrition","Obstacle","Ocean","Ore","Package","Pet","Plague","Plant","Pollution","Probe","Propulsion","Radiation","Ray","Relief","Remedy","Rescue","Road","Sample","Scan","Science","Sea","Security","Service","Shadow","Shield","Shock","Simulation","Smog","Snow","Soil","Sound","Soundwave","Spell","Spirit","Stealth","Stone","Storage","Strategy","Strife","Sun","Support","Surgeon","Survival","Termination","Tool","Toxin","Trade","Transport","Tree","Venom","View","Virus","Vitality","Warfare","Water","Weather","Wound"];
var nm3 = ["Alterator","Alternator","Analytron","Analyzer","Assembler","Attractomatic","Augmentron","Automatron","Catalyzer","Circulator","Communicator","Concealer","Concealotron","Conductron","Controller","Conveyor","Decoder","Detector","Detectron","Diagnoser","Director","Disconnector","Dislocator","Disseminator","Distrubutor","Enchanter","Encrypter","Enhancomatic","Enthraller","Enticer","Evaluator","Exchangomatic","Generator","Gyrator","Incubator","Inducer","Intensitron","Jumbler","Magnetizer","Magnificator","Manipulator","Manipulsator","Maximizer","Mechanizer","Minimizer","Mobilizer","Modificator","Modulator","Monitron","Morphomatic","Mutator","Obscurator","Possessor","Processor","Pullomatic","Reanimator","Refiner","Regenerator","Rejuvenator","Relocator","Reproducer","Revealotron","Revitalizer","Scrambler","Secretor","Separatron","Telelocator","Teleporter","Transferator","Transfigurator","Transformer","Transmitter","Transmogrifier","Transmutator","Transporter","Unscrambler","Zapper"];
var nm4 = ["","","","Kit","Network","Network","Interface","Interface","Matrix","Tool","Engine","Gizmo","Device","MachineKit","Matrix","Tool","Engine","Apparatus","Apparatus","Device","Machine","Doodad","Widget","Thingymajig","Mechanism","Doohickey"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		rnd4 = Math.floor(Math.random() * nm4.length);
		names = nm1[rnd] + " " + nm2[rnd2] + " " + nm3[rnd3] + " " + nm4[rnd4];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}