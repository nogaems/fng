var nm1 = ["Acid","Aero","After","Air","Ape","Aqua","Armor","Astro","Auto","Avian","Back","Blow","Blue","Body","Bomb","Bone","Botani","Boulder","Brake","Break","Broad","Brush","Bulk","Bull","Bullet","Buzz","Cannon","Chain","Chrome","Cinder","Cliff","Cloud","Crack","Crank","Cross","Dark","Deep","Deft","Depth","Dino","Dirt","Dive","Doom","Double","Dread","Drop","Dune","Dust","Fang","Fiery","Fire","Fist","Flame","Flash","Flat","Flight","Fly","Free","Freeze","Frost","Gear","Gloom","Gold","Grand","Grim","Grind","Grizz","Groove","Ground","Growl","Gun","Hail","Half","Hammer","Hang","Hard","Heavy","Heli","High","Hook","Hot","Hydra","Hydrau","Hyper","Ice","Iron","Jaw","Jet","Jolt","Junk","Kick","Land","Lazer","Lead","Leo","Light","Lock","Long","Lunar","Magma","Magna","Mean","Mecha","Mega","Melt","Motor","Neutro","Night","Oil","Over","Phase","Photon","Power","Pyro","Quick","Rage","Rapid","Rat","Razor","Retro","Rhi","Rhino","Rip","Road","Roll","Rotor","Rough","Rumble","Savage","Scorch","Scrap","Sea","Shade","Shadow","Shock","Side","Silver","Sky","Slam","Slip","Smoke","Solar","Sound","Spark","Speed","Star","Steel","Stone","Storm","Strike","Sun","Swift","Thunder","Tiga","Tiger","Top","Turbo","Twin","Vice","Volt","Wide","Wild","Wind","Wolf","Wreck"];
var nm2 = ["back","bang","beam","beast","bird","bite","blade","blades","blast","blaze","blight","blitz","bolt","boom","bot","brawl","brawn","burn","burner","burst","buster","button","case","cast","charge","charger","circuit","clash","claw","cloud","clutch","crack","crush","crusher","cut","cycle","dash","dealer","dive","dome","drift","drive","feather","fight","fire","fist","flash","flight","flow","foot","frame","glide","glider","glitch","guard","hammer","head","heap","hide","horn","jaw","jump","kick","kill","lane","lift","light","line","load","lock","master","mine","point","pounder","punch","quake","raid","raider","rake","raker","ray","razor","runner","scope","scrap","scraps","scream","shift","shot","side","sight","siren","slide","sling","slinger","snarl","spike","spin","splitter","spot","stalker","steel","stop","storm","streak","stream","strike","strong","stuff","sweep","switch","thing","top","track","tracks","trap","tron","twitch","viper","vortex","war","watch","wave","way","ways","wheels","whip","wing","wire","wise","works"];
var nm3 = ["Abomination","Ace","Ares","Aries","Athena","Augment","Aurora","Barbarian","Barrage","Beacon","Beast","Behemoth","Blade","Blitz","Blitzkrieg","Blockaide","Brute","Cascade","Claw","Coil","Comet","Compass","Core","Creature","Critter","Crossflare","Crux","Dagger","Delirium","Ditch","Divebomb","Dread","Dynamite","Dynamo","Earthquake","Eclipse","Element","Ember","Enigma","Error","Feral","Flinch","Flow","Flutter","Flux","Freak","Fungus","Fury","Fuse","Gadget","Gleam","Grease","Growl","Harness","Havoc","Hazard","Hightop","Hitch","Honeybee","Howler","Hymn","Icicle","Inferno","Influx","Jeopardy","Landslide","Maniac","Melody","Mercy","Meteoroid","Nightlight","Oracle","Outburst","Overboard","Overflow","Overload","Paradox","Particle","Pest","Pillage","Posthaste","Prodigy","Pummel","Pursuit","Quake","Quarrel","Rabid","Racer","Rage","Remix","Requiem","Residue","Ricochet","Riot","Rodent","Rubble","Rumble","Rush","Salvo","Savage","Savvy","Scourge","Scratch","Shamble","Shift","Sidearm","Sideburns","Sidelock","Sidewire","Sky-High","Slide","Smite","Snake","Snarl","Snowdrift","Sprocket","Stampede","Starblaster","Starburst","Stormrunner","Sunblast","Sunburst","Switch","Talon","Tempest","Thrust","Thunder","Torment","Torrent","Trailfire","Trident","Turbine","Twinkle","Typhoon","Venture","Vermin","Vigor","Virtue","Volley","Voltage","Wallop","Weasel","Wheels","Whistle","Whiz","Wrangle","Wreckage","Zephyr","Zodiac"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + nm2[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			names = nm3[rnd];
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