var nm1 = ["","","","","b","d","g","h","j","k","m","r","s","v","z"];
var nm2 = ["a","e","i","o","u"];
var nm3 = ["d","g","h","k","j","l","m","n","nth","r","rh","s","t","z"];
var nm4 = ["g","m","mg","nd","r","rg","s","v","z"];
var nm5 = ["g","k","j","l","m","n","r","s","t","z"];
var nm6 = ["b","c","d","m","r"];
var nm7 = ["Djinn","Loremaster","Weaver","Sage","Djinn","Djinn","Djinn","Djinn","Djinn","Djinn","Master","Mahatma","Savant"];
var nm8 = ["Amusement","Autumn","Balance","Chance","Chances","Change","Competition","Deceit","Deception","Desire","Destinations","Destinies","Favors","Fear","Fire","Flames","Flight","Frost","Games","Harmony","Humor","Ice","Illumination","Invention","Jewels","Knowledge","Laughs","Laughter","Lies","Light","Magic","Music","Passages","Play","Pleasure","Purpose","Questions","Requests","Rewards","Riddles","Servitude","Slavery","Smiles","Smoke","Smoke and Mirrors","Snow","Solitude","Spirits","Spring","Summer","Surprises","Thoughts","Thrills","Thunder","Time","Truth","Vacation","Voyages","Water","Wind","Winter","Wisdom","Wishes","the Air","the Clouds","the Destiny","the Forest","the Labyrinth","the Lamp","the Maze","the Mountain","the Realm","the Sea","the Senses","the Sky","the Swamp","the Voyage","the Weather","the World"];
var nm9 = ["Aerial","Aura","Aurora","Autumn","Avian","Balance","Borealis","Brine","Chance","Competition","Cyclone","Deception","Desire","Destiny","Dew","Favor","Fire","Flame","Flight","Frost","Gale","Game","Gust","Harmony","Hellion","Ice","Illumination","Invention","Jewel","Knowledge","Laughter","Light","Music","Nebula","Ozone","Passage","Pleasure","Riddle","Servitude","Smiles","Smoke","Snow","Solitude","Spirits","Spring","Storm","Summer","Surprise","Thrill","Thunder","Time","Truth","Vapor","Voyage","Water","Wind","Winter","Wisdom","Zephyr"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm2.length);
			rnd5 = Math.floor(Math.random() * nm5.length);
			rnd6 = Math.floor(Math.random() * nm7.length);
			if(i < 3){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + " " + nm7[rnd6];
			}else if(i < 5){
				rnd8 = Math.floor(Math.random() * nm4.length);
				rnd9 = Math.floor(Math.random() * nm2.length);
				while(nm4[rnd8] === nm3[rnd3]){
					rnd8 = Math.floor(Math.random() * nm4.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd8] + nm2[rnd9] + nm5[rnd5] + " " + nm7[rnd6];
			}else{
				rnd8 = Math.floor(Math.random() * nm4.length);
				rnd9 = Math.floor(Math.random() * nm2.length);
				rnd10 = Math.floor(Math.random() * nm5.length);
				rnd11 = Math.floor(Math.random() * nm2.length);
				while(nm4[rnd8] === nm3[rnd3]){
					rnd8 = Math.floor(Math.random() * nm4.length);
				}
				while(nm5[rnd10] === nm3[rnd3] || nm5[rnd10] === nm4[rnd8]){
					rnd10 = Math.floor(Math.random() * nm5.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd8] + nm2[rnd9] + nm5[rnd10] + nm2[rnd11] + nm5[rnd5] + " " + nm7[rnd6];
			}
		}else if(i < 8){
			rnd = Math.floor(Math.random() * nm7.length);
			rnd2 = Math.floor(Math.random() * nm8.length);
			names = nm7[rnd] + " of " + nm8[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm9.length);
			rnd2 = Math.floor(Math.random() * nm7.length);
			names = nm9[rnd] + " " + nm7[rnd2];
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