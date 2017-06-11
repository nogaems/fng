var nm1 = ["","","","","c","f","h","l","n","r","s","w","z"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","y","oo","ia","ea","ee"];
var nm3 = ["b","d","l","ll","m","mm","n","nn","r","s","v","b","d","dw","l","ll","lw","lr","lm","ln","m","mr","mm","n","nm","nr","nv","r","rl","rn","rm","sh","sn","sr","vl","vr"];
var nm4 = ["c","d","l","n","r","s","th","z"];
var nm5 = ["","","","","","","","","","","","","","","","h","l","n","ph","s","th"];

var nm6 = ["acorn","alder","alpen","amber","autumn","barely","beech","birch","briar","bright","cedar","cherry","cinder","cloud","crystal","dawn","dew","dream","dusk","elm","ember","feather","fern","fog","forest","free","frost","gentle","grand","grass","great","green","haven","hazel","heart","holly","humble","keen","kind","leaf","light","lone","maple","marble","marsh","mellow","mist","moon","moss","nettle","night","oaken","orb","peach","pine","plain","pride","proud","rain","rapid","ring","river","rock","rose","rune","silent","silk","silver","sky","snow","spell","spring","spruce","star","stern","stout","sun","swift","thorn","vine","water","weather","willow","wood","yew"];
var nm7 = ["","","","","","","","","","","","","","","bash","beam","belly","bend","berry","bind","blossom","blow","bough","brace","braid","bramble","branch","brand","breath","breeze","brook","brooke","bush","cloud","copse","covert","crest","crown","dance","dancer","dew","down","draft","dream","drift","drop","dust","fall","fern","fir","flow","gaze","gem","glade","gleam","glide","glow","grove","gust","heart","husk","larch","leaf","lock","ridge","river","rock","run","seed","shade","shine","shrub","skipper","snow","soar","song","spell","spirit","sprout","spur","stand","star","stone","stride","stutter","sun","thorn","track","trap","twig","ward","water","wind","wing","wings"];
var nm8 = ["Dancer","Faerie","Flitter","Leprechaun","Pixie","Prankster","Schemer","Spinner","Sprite","Swarm"];

var nm9 = ["Autumn","Blizzard","Brush","Bush","Cloud","Dew","Dewdrop","Dirt","Dream","Dust","Fan","Feather","Fire","Flight","Flock","Flower","Fog","Forest","Frost","Garden","Glen","Gust","Honey","Ice","Icicle","Jewel","Kite","Leaf","Lift","Light","Lunar","Marble","Marsh","Meadow","Mist","Moon","Mountain","Nectar","Night","Nightshade","Ocean","Plane","Rain","Riddle","River","Sand","Sea","Shade","Shadow","Shore","Shrub","Silk","Snow","Solar","Spring","Storm","Stream","Summer","Sun","Thorn","Thunder","Water","Wind","Winter","Zephyr"];
var nm10 = ["Archmage","Blackguard","Caretaker","Clique","Cohort","Dancer","Dewdancer","Disciple","Faerie","Flitter","Gatewarden","Guard","Guardian","Harbinger","Invader","Keeper","Lancer","Leprechaun","Mage","Mechanist","Noble","Overseer","Pixie","Prankster","Priestess","Prowler","Ranger","Rascal","Rover","Sage","Schemer","Scout","Seer","Singer","Skipper","Soulsinger","Spinner","Sprite","Spy","Squadron","Swarm","Thief","Trickster","Wanderer","Warden","Witch"];

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
			while(nm3[rnd3] === nm1[rnd]){
				rnd3 = Math.floor(Math.random() * nm3.length);
			}
			if(i < 2){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
			}else{
				rnd6 = Math.floor(Math.random() * nm4.length);
				rnd7 = Math.floor(Math.random() * nm2.length);
				while(nm3[rnd3] === nm4[rnd6]){
					rnd6 = Math.floor(Math.random() * nm4.length);
				}
				if(i < 4){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
				}else{
					names = nm1[rnd] + nm2[rnd4] + nm4[rnd6] + nm2[rnd2] + nm3[rnd3] + nm2[rnd7] + nm5[rnd5];
				}
			}
		}else if(i < 8){
			rnd = Math.floor(Math.random() * nm6.length);
			rnd2 = Math.floor(Math.random() * nm7.length);
			while(nm6[rnd] === nm7[rnd2]){
				rnd2 = Math.floor(Math.random() * nm7.length);
			}
			rnd3 = Math.floor(Math.random() * nm8.length);
			names = nm6[rnd] + nm7[rnd2] + " " + nm8[rnd3];
		}else{
			rnd = Math.floor(Math.random() * nm9.length);
			rnd2 = Math.floor(Math.random() * nm10.length);
			names = nm9[rnd] + " " + nm10[rnd2];
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