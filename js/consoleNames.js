var nm3 = ["Box","Cast","Center","Core","Cube","Drive","Sphere","Station","System","Zone","Arcade","Box","Cade","Cast","Center","Core","Cube","Drive","Player","Sphere","Station","System","Vision","Zone"];
function nameGen(){
	var nm1 = ["Aberrant","Achievement","Achiever","Adventure","Adventurer","Agent","Ambition","Assistant","Beast","Beginning","Buddy","Canvas","Challenger","Champ","Champion","Chimera","Click","Cloud","Clover","Companion","Creator","Crystal","Curiosity","Delight","Desire","Diamond","Dot","Dreamscape","Edge","Enigma","Event","Feast","Fest","Flame","Fluke","Ghost","Gift","Guest","Guide","Heart","Horn","Host","Image","Impulse","Jewel","Level Up","Light","Master","Mirage","Moment","Motion","Omen","Oracle","Particle","Phantom","Playground","Prism","Reward","Rhythm","Scene","Secret","Sense","Signal","Smile","Snowflake","Spark","Sparkle","Specter","Spell","Spirit","Sprite","Station","Taste","Tempest","Thrill","Thunder","Treat","Trick","Twist","Veil","Victory","View","Wish"];
	var nm2 = ["Aberrant","Action","Adventure","Ambition","Amusement","Awe","Beginning","Boundless","Buddy","Challenge","Challenger","Champion","Chance","Child","Childhood","Chimera","Collection","Companion","Courage","Creation","Creative","Creator","Crux","Crystal","Curiosity","Desire","Dimension","Dream","Emotion","Enigma","Entertainment","Eternity","Fantasy","Fire","Force","Fortune","Freedom","Game","Golden","Grand","Harmony","Hyper","Image","Imagination","Impulse","Infinity","Liberty","Life","Light","Master","Mirage","Mystery","Oracle","Particle","Phantom","Play","Pocket","Power","Prism","Response","Retro","Rhythm","Sentient","Silver","Smile","Source","Spark","Specialist","Specter","Spell","Start","Super","Surprise","Switch","Thrill","Thunder","Treat","Vessel","Victory","Virtual","Vision","Voyage","Voyager","Wisdom","World"];

	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.random() * nm1.length | 0;
			names = "The " + nm1[rnd];
			nm1.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm2.length | 0;
			rnd2 = Math.random() * nm3.length | 0;
			names = "The " + nm2[rnd] + " " + nm3[rnd2];
			nm2.splice(rnd, 1);
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