var names1 = ["Agile","Black","Blue","Bronze","Cloaked","Crimson","Crouching","Dark","Deadly","Elegant","Falling","Fast","Floating","Flying","Ghost","Golden","Graceful","Hidden","Hollow","Invisible","Iron","Jade","Light","Masked","Muffled","Muzzled","Mysterious","Mystic","Nimble","Phantom","Quick","Quiet","Rapid","Red","Ruby","Sanguine","Sapphire","Scarlet","Serpent","Shrouded","Silent","Silver","Slender","Smiling","Smooth","Snake","Soothing","Steel","Still","Swift","Thin","Tranquil","Unheard","Unknown","Unmoving","Unseen","Veiled","White","Winged","Wise"];
var names2 = ["Angel","Assassin","Avalanche","Basilisk","Beast","Blaze","Breath","Cat","Child","Cipher","Crane","Dagger","Death","Demise","Demon","Devil","Dragon","Drake","Dream","Echo","Enigma","Eye","Eyes","Figure","Fire","Flame","Ghost","Grin","Hawk","Hunter","Illusion","Image","Jackal","Knife","Laugh","Lion","Lotus","Mamba","Mark","Mask","Master","Mime","Mimic","Mind","Mirage","Moon","Mute","Oracle","Paradox","Phantom","Phoenix","Player","Rain","Ranger","Raven","Reflection","Rock","Rover","Saber","Samaritan","Scar","Scorpion","Scythe","Secret","Serpent","Shade","Shadow","Silence","Smile","Smirk","Smoke","Snake","Snow","Soldier","Spider","Stalker","Star","Striker","Sword","Thunder","Tiger","Viper","Vision","Wanderer","Warden","Watcher","Whisper","Wind","Wolf","Wrath"];
var names3 = ["Black","Blood","Bullet","Crimson","Dark","Dead","Death","Dream","Ghost","Golden","Hollow","Iron","Jade","Kill","Lethal","Light","Lightning","Phantom","Quick","Rabid","Rapid","Red","Scarlet","Silent","Silver","Snow","Steel","Still","Swift","Thunder"];
var names4 = ["bang","bash","beat","blade","claw","crash","eye","eyes","fall","flake","flash","flow","kill","lock","mark","moon","saw","scar","shade","shadow","shiv","shot","sign","slinger","stain","strike","streak","strikes","stroke","tooth"];
var names5 = ["Bang","Bash","Beat","Blade","Claw","Crash","Eye","Eyes","Fall","Flake","Flash","Flow","Kill","Lock","Mark","Moon","Saw","Scar","Shade","Shadow","Shiv","Shot","Sign","Slinger","Stain","Strike","Streak","Strikes","Stroke","Tooth"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * names1.length);
			rnd2 = Math.floor(Math.random() * names2.length);
			names = "The " + names1[rnd] + " " + names2[rnd2];
		}else{
			rnd = Math.floor(Math.random() * names3.length);
			if(i < 8){
				rnd2 = Math.floor(Math.random() * names4.length);
				names = names3[rnd] + names4[rnd2];
			}else{
				rnd2 = Math.floor(Math.random() * names5.length);
				names = names3[rnd] + " " + names5[rnd2];
			}
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