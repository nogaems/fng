var names1 = ["Unit","Platform","Mod","System","SysMod","GU","G-Unit","Geth-Unit","Module"];
var names3 = ["a","b","c","e","s","x"];
var names4 = ["Armada","Batallion","Alpha","Omega","Myriad","Sundry","Horde","Brigade","Phalanx","Host","Enigma","Terminus","Prophet","Genesis","Dawn","Oracle","Anomaly","Centurion","Obelisk","Pinnacle","Goliath","Apex","Vortex","Vertex","Armageddon","Oblivion","Eternity","Daemon","Demise","Destiny"];

function nameGen(){	
	$('#placeholder').css('textTransform', 'capitalize');
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.floor(Math.random() * names1.length);
			var names2 = Math.floor((Math.random() * 250) + 1);
			rnd1 = Math.floor(Math.random() * names3.length);
			names = names1[rnd] + "-" + names2 + names3[rnd1];
		}else{
			rnd0 = Math.floor(Math.random() * names4.length);
			names = names4[rnd0];
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