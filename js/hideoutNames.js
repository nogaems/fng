var nm1 = ["Abyss","Adorned","Aeon","Amber","Ancient","Angelic","Animus","Arachnid","Arc","Arcane","Arch","Arctic","Argent","Armada","Ash","Ashen","Aspect","Aura","Aurora","Autumn","Avian","Azure","Barrage","Basilisk","Bastion","Blackout","Blind","Blitz","Blue Moon","Brass","Bristle","Broken","Brotherhood","Bulwark","Canine","Cardinal","Cerulean","Cinder","Cloak","Clover","Cobalt","Concave","Convex","Copper","Core","Corona","Covert","Creed","Crescent","Crimson","Crooked","Crown","Dark","Dawn","Defiance","Defiant","Demilune","Diablo","Diligence","Dirge","Division","Dragon","Dread","Duplicity","Dusk","Ebon","Echo","Eclipse","Elysium","Enigma","Eos","Epiphany","Epoch","Eternity","Eventide","Exalted","Exile","Falcon","Feather","Fel","Feline","Fickle","Fire","Flame","Flower","Fog","Frayed","Fury","Glass","Globe","Glum","Golden","Grand","Granite","Grave","Grim","Hallowed","Halo","Harmony","Hellion","Hollow","Infinity","Iron","Ironclad","Ivory","Jade","Jagged","Jewel","Juggernaut","Karma","Keen","Livid","Low","Luna","Lune","Meridian","Miracle","Mirage","Misty","Molten","Monolith","Murk","Mute","Mystery","Needle","Nemo","Nether","Night","Nightfall","Nightmare","Odyssey","Opulent","Outcast","Outlandish","Parapet","Penumbra","Phoenix","Pilgrim","Pinnacle","Prime","Quill","Quiver","Rabbit","Reaper","Renegade","Requiem","Retribution","Rotten","Runaway","Rune","Sabre","Salvation","Sanguine","Sapphire","Scale","Scaly","Scarlet","Serpent","Shadow","Shroud","Sickle","Silent","Silver","Sisterhood","Snowflake","Solar","Starfall","Stark","Starlight","Storm","Sub","Syncope","Syndicate","Talon","Tempest","Thorn","Thunder","Titan","Tramp","Tribute","Trident","Trinity","Triumph","Twilight","Twin","Vagabond","Vagrant","Valhalla","Vanguard","Veil","Velvet","Visage","Vortex","Warden","Watcher","Wicked","Wild","Winter","Wrath","Zephyr","Zodiac"];
var nm2 = ["Base","Burrow","Cave","Cover","Covert","Den","Escape","Garrison","Harbor","Haunt","Hideaway","Hideout","Lair","Nest","Retreat","Sanctuary","Sanctum"];
var nm3 = ["amber","arch","ash","ashen","bitter","black","blood","boulder","chaos","cinder","clear","cloud","cold","crest","crimson","deep","dragon","dream","dusk","ember","fire","flame","fore","free","frost","grand","grass","hallow","high","iron","jade","jugger","keen","light","lone","long","lunar","moon","mourn","nether","nettle","night","noble","path","pride","proud","rune","saur","shadow","silent","silver","skull","sky","solar","spire","spirit","star","stone","storm","sun","swift","tall","thunder","trail","van ","whisper","white","wild","wolf"];
var nm4 = ["bane","bark","blade","bloom","bond","born","brace","bramble","claw","crest","fall","flame","force","forge","guard","hand","heart","horn","howl","keep","keeper","lance","land","light","lock","mane","mantle","maul","might","ridge","run","shield","spell","spire","stand","star","stone","storm","strike","sword","sworn","tail","thorn","tide","tooth","vale","ward","watch","whisper","wing","word","work"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm2.length);
		if(i < 5){
			rnd2 = Math.floor(Math.random() * nm3.length);
			rnd3 = Math.floor(Math.random() * nm4.length);
			while(nm3[rnd2] === nm4[rnd3]){
				rnd3 = Math.floor(Math.random() * nm4.length);
			}
			names = nm3[rnd2] + nm4[rnd3] + " " + nm2[rnd];
		}else{
			rnd2 = Math.floor(Math.random() * nm1.length);
			names = "The " + nm1[rnd2] + " " + nm2[rnd];
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