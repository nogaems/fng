var nm1 = ["Matter Master","Skye","Conjurer","Invincible","Shift","Telescope","Wormhole","Reptile","Insect","Bullet","Venus","Puma","Lunar","Wireless","Vaccine","Perception","Springboard","Eclipse","Demon","Siren","Steelskin","Ace","Anarchy","Ape","Arachnid","Ash","Ashes","Augury","Aura","Bandit","Barrage","Bearpaw","Behemoth","Blaze","Blight","Blizzard","Bolt","Bones","Boulder","Brute","Bubble","Chaos","Chronos","Clairity","Clone","Cloud","Creature","Cryptic","Crystal","Daydream","Decay","Demon","Dice","Discharge","Disperse","Dragonfly","Dynamo","Echo","Electrode","Enigma","Fallout","Fangs","Feline","Fiend","Flint","Flow","Flux","Frost","Fury","Fuse","Gamble","Gargoyle","Ghost","Gimmick","Glutton","Granite","Grimm","Hazard","Hue","Hypnotic","Inferno","Infinity","Jackal","Jester","Katana","Knightmare","Light","Liquid","Luna","Lupine","Lupus","Mammoth","Mist","Mouse","Myth","Naught","Nightmare","Nightowl","Nightshade","Noise","Ogre","Omen","Onesize","Ooze","Optic","Oracle","Paladin","Pandemonium","Paradox","Particle","Pebble","Phonic","Phonix","Physique","Pipsqueak","Plague","Plasma","Pygmy","Pyre","Quake","Rime","Ruse","Savage","Scepter","Scout","Scramble","Seismic","Sentinel","Serenity","Serpent","Shade","Shadow","Shockwave","Sight","Siphon","Siren","Slither","Sliver","Sly","Snake","Snowflake","Solaris","Spark","Splinter","Stardust","Steel","Stretch","Swine","Switch","Thunder","Timber","Timeles","Tranquillity","Twin","Valkyrie","Vapor","Vermin","Viper","Virtue","Void","Vortex","Weasel","Whisper","Wisp","X-Ray","Yce"];
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