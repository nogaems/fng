var nm1 = ["c","cr","h","k","kr","m","n","ph","v","x","z"];
var nm2 = ["a","e","i","o","u"];
var nm3 = ["d","fr","g","l","ll","lr","n","ph","r","rph","rv","rc","rk","rl","th","thr","v","z"];
var nm4 = ["a","i","o","a","i","o","io","ia","oa","eo"];
var nm5 = ["b","d","g","l","n","r","t","z"];
var nm6 = ["d","s","t","th","x","s","s","x","x","s","s","s"];

var nm7 = ["c","f","h","k","l","m","n","ph","th"];
var nm8 = ["a","e","i","a","e","i","y"];
var nm9 = ["l","ll","m","n","ph","r","rr","s","sh","ss","th"];
var nm10 = ["a","e","i","a","e","i","ea","ae","ia","oe"];
var nm11 = ["c","h","k","l","n","r","ss","tr","y"];

var nm12 = ["Abundance","Agriculture","Animals","Battle","Beauty","Beer","Beginnings","Blacksmiths","Chaos","Children","Chivalry","Commerce","Conquest","Dawn","Day","Death","Destiny","Destruction","Dreams","Dusk","Duty","Earth","Education","Endings","Envy","Fall","Fame","Fertility","Finance","Fire","Forgiveness","Fortune","Freedom","Funerals","Good Luck","Governance","Harvest","Hatred","Health","Home","Honesty","Honor","Hope","Hunting","Infamy","Jealousy","Judgement","Justice","Law","Life","Life & Death","Light","Logic","Love","Loyalty","Magic","Marriage","Medicine","Mercy","Messages","Miracles","Misfortune","Music","Nature","Night","Night & Day","Oracles","Order","Peace","Penance","Pleasure","Poetry","Prosperity","Revenge","Science","Secrecy","Shadows","Sleep","Spring","Strength","Success","Summer","Thunder","Time","Torture","Trade","Tranquility","Tricks","Truth","Vengeance","Victory","Virtues","War","Water","Weddings","Wind","Wine","Winter","Wisdom","Work","Youth","the Afterlife","the Dark","the Hearth","the Hunt","the Insane","the Land","the Military","the Moon","the Mountains","the Ocean","the Ostracized","the Rivers","the Sea","the Sky","the Stars","the Sun","the Underworld"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd12 = Math.floor(Math.random() * nm12.length);
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm7.length);
			rnd2 = Math.floor(Math.random() * nm8.length);
			rnd3 = Math.floor(Math.random() * nm9.length);
			rnd4 = Math.floor(Math.random() * nm10.length);
			if(i < 5){
				while(nm9[rnd3] === nm7[rnd]){
					rnd3 = Math.floor(Math.random() * nm9.length);
				}
				names = nm7[rnd] + nm8[rnd2] + nm9[rnd3] + nm10[rnd4] + ", God of " + nm12[rnd12];
			}else{
				rnd5 = Math.floor(Math.random() * nm8.length);
				rnd6 = Math.floor(Math.random() * nm11.length);
				if(i < 7){
					names = nm7[rnd] + nm8[rnd2] + nm9[rnd3] + nm10[rnd4] + nm11[rnd6] + nm8[rnd5] + ", God of " + nm12[rnd12];
				}else{
					names = nm7[rnd] + nm8[rnd2] + nm9[rnd3] + nm8[rnd5] + nm11[rnd6] + nm10[rnd4] + ", God of " + nm12[rnd12];
				}
			}
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm4.length);
			rnd5 = Math.floor(Math.random() * nm6.length);
			if(i < 5){
				while(nm3[rnd3] === nm1[rnd]){
					rnd3 = Math.floor(Math.random() * nm3.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm6[rnd5] + ", God of " + nm12[rnd12];
			}else{
				rnd6 = Math.floor(Math.random() * nm2.length);
				rnd7 = Math.floor(Math.random() * nm5.length);
				if(i < 7){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm5[rnd7] + nm2[rnd6] + nm6[rnd5] + ", God of " + nm12[rnd12];
				}else{
					names = nm1[rnd] + nm2[rnd2] + nm5[rnd7] + nm2[rnd6] + nm3[rnd3] + nm4[rnd4] + nm6[rnd5] + ", God of " + nm12[rnd12];
				}
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