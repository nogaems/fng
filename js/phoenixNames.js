var nm1 = ["Ash","Ashes","Aura","Aurora","Beacon","Beak","Beam","Blaze","Blazetalon","Blink","Bonfi","Brilliancy","Brim","Cinder","Cinders","Crux","Dawn","Dazzle","Deja","Dusty","Elemence","Ember","Eos","Eterna","Eternus","Feathers","Ferno","Fiere","Flambeau","Flame","Flametalon","Flare","Flash","Flayme","Fume","Fury","Fye","Fyre","Genesis","Glaze","Glint","Gloss","Glow","Heat","Icarus","Ignite","Illume","Illumine","Inferno","Juvenate","Kindle","Light","Lucent","Lumino","Luminos","Morte","Nether","Nite","Onyx","Pharos","Pire","Plume","Pyre","Radiance","Raise","Ray","Raye","Revi","Rise","Ryse","Ryze","Scorch","Scorchey","Sheen","Shimmer","Shine","Slag","Soar","Sol","Solar","Solaris","Soleil","Soot","Soots","Soul","Spark","Sparkle","Sparkles","Spirit","Sprout","Smoke","Sunbeam","Sunny","Surge","Tinder","Torch","Vitality","Vitally","Viva","Vu","Zeal"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}