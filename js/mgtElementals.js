var nm1 = ["","","","","","d","h","l","m","n","r","s","v","w","z"];
var nm2 = ["a","a","i","o","u"];
var nm3 = ["d","kl","kd","kn","km","l","ld","ll","lr","lt","lv","ln","m","mm","mr","ml","mn","n","nl","nr","nd","nt","nn","r","rd","rg","rl","rdr","rr","sn","sl","sr","sm","ss","x","z","zz","zl"];
var nm4 = ["c","l","m","n","s","th","x","z"];
var nm5 = ["d","g","l","n","r","s","th"];

var nm6 = ["amber","ash","blaze","blood","boulder","bright","chloro","cinder","elder","fire","flame","flood","forest","frost","fuse","geyser","glare","glow","gore","green","ground","heart","hell","hollow","hydro","lava","leaf","mana","meadow","molten","moss","mourn","nether","plume","primal","pyre","pyro","rage","rock","rubble","rush","scorch","shadow","shine","shore","silver","skull","slither","smoke","snow","soot","soul","spark","spawn","spite","splinter","storm","sun","talon","terra","thunder","tide","venge","vine","war","water","whisper","wild","wind","wolf","wood"];
var nm7 = ["bane","beam","bender","blaze","blight","blust","boon","born","braider","bramble","branch","brand","breaker","breeze","briar","bright","chaser","cloud","core","crag","crasher","crest","crux","dew","draft","drifter","fall","field","fiend","fire","flame","flare","flayer","flow","force","forge","fright","fury","glade","glide","growth","haze","heart","hearth","henge","horn","hulk","kin","land","lash","mare","mender","mind","morph","mulcher","muse","phant","pyre","rage","reaver","rend","roar","scar","shard","slide","spark","spitter","sprout","stoke","surge","thorn","tusk","veil","vine","walker","ward","warden","water","wend","whelk","wielder","wind","wood","wraith","writhe"];
var nm8 = ["Acolyte","Ally","Ancient","Behemoth","Brood","Cerberus","Champion","Chaser","Cohort","Conservator","Consul","Custodian","Defender","Elemental","Elemental","Elemental","Elemental","Elemental","Elemental","Elemental","Elemental","Elemental","Devourer","Drifter","Effigy","Elemental","Entity","Envoy","Fiend","Figure","Force","Forger","Glider","Guardian","Hatchling","Hulk","Hunter","Icon","Incarnate","Infantry","Knight","Legate","Liege","Mage","Mongrel","Monster","Nimbus","Overseer","Paladin","Patrol","Plasma","Protector","Rager","Ravager","Ripper","Rusher","Scavenger","Scion","Scout","Sentinel","Servant","Shaman","Shambler","Shepherd","Soldier","Soul","Spirit","Stalker","Strider","Titan","Trooper","Tyrant","Walker","Wanderer","Warden","Watcher","Zealot"];

var nm9 = ["Aqua","Blizzard","Blood","Bog","Boulder","Bramble","Bright","Brine","Celestial","Cinder","Cloud","Crater","Cyclone","Dawn","Dread","Dusk","Dust","Earth","Ember","Ethereal","Fiery","Fire","Flame","Fog","Forest","Forgotten","Frost","Frozen","Fungi","Fungus","Furnace","Fury","Fusion","Geyser","Glacial","Glaring","Grand","Granite","Grave","Greater","Grove","Hellfire","Hollow","Hurricane","Hydro","Igneous","Infernal","Inferno","Ingot","Labyrinth","Lagoon","Lake","Lightning","Lucent","Lucid","Maelstrom","Magma","Marsh","Maze","Meadow","Mist","Molten","Moon","Moss","Mountain","Mud","Nova","Oasis","Obsidian","Orchard","Plasma","Primal","Prime","Pyre","Pyro","Quicksilver","Rage","Rift","Rock","Root","Rotten","Rotting","Rumbling","Rust","Salt","Savage","Seething","Seismic","Smog","Smoke","Smoking","Smolder","Smoldering","Soot","Spark","Spectral","Stone","Storm","Sun","Tempest","Terra","Thorn","Thunder","Thundercloud","Tidal","Tide","Time","Torrent","Totem","Undergrowth","Vapor","Vengeful","Vine","Void","Volatile","Volcanic","Vortex","War","Water","Wave","Wayfaring","Wind","Wood"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.random() * nm6.length | 0;
			rnd2 = Math.random() * nm7.length | 0;
			while(nm6[rnd] === nm7[rnd2]){
				rnd2 = Math.random() * nm7.length | 0;
			}
			rnd3 = Math.random() * nm8.length | 0;
			lName = nm6[rnd] + nm7[rnd2] + " " + nm8[rnd3];
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm3.length | 0;
			rnd4 = Math.random() * nm2.length | 0;
			rnd5 = Math.random() * nm5.length | 0;
			while(nm3[rnd3] === nm1[rnd]){
				rnd = Math.random() * nm1.length | 0;
			}
			while(nm3[rnd3] === nm5[rnd5]){
				rnd5 = Math.random() * nm5.length | 0;
			}
			if(i < 3){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + ", " + lName;
			}else{
				rnd6 = Math.random() * nm4.length | 0;
				rnd7 = Math.random() * nm2.length | 0;
				while(nm4[rnd6] === nm5[rnd5]){
					rnd6 = Math.random() * nm4.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5] + ", " + lName;
			}
		}else if(i < 8){
			rnd = Math.random() * nm6.length | 0;
			rnd2 = Math.random() * nm7.length | 0;
			while(nm6[rnd] === nm7[rnd2]){
				rnd2 = Math.random() * nm7.length | 0;
			}
			rnd3 = Math.random() * nm8.length | 0;
			names = nm6[rnd] + nm7[rnd2] + " " + nm8[rnd3];
		}else{
			rnd = Math.random() * nm9.length | 0;
			rnd2 = Math.random() * nm8.length | 0;
			names = nm9[rnd] + " " + nm8[rnd2];
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