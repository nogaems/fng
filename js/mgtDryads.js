var nm1 = ["c","f","h","l","m","n","ph","r","s","th","w"];
var nm2 = ["a","e","i","a","e","i","o","a","e","i","a","e","i","o","a","e","i","a","e","i","o","a","e","i","a","e","i","o","a","e","i","a","e","i","o","ya","ae","ea","ia","ye","ie"];
var nm3 = ["h","l","ll","m","n","r","rr","s","ss","t","v"];
var nm4 = ["fn","fr","hn","ln","lm","ls","mn","mr","nm","n","nn","nr","ns","nph","ph","r","rr","sn","st","sh","th","thr"];
var nm5 = ["fn","fr","h","hn","l","ll","lm","ln","ls","m","mn","mr","n","nn","nr","r","rr","s","sn","sh","ss","thr"];
var nm6 = ["acorn","alder","ash","beech","birch","cedar","cherry","cypress","elm","fir","juniper","larch","locust","maple","oak","peach","pine","poplar","spruce","walnut","willow","yew","tree","hazel","thistle","autumn","bare","bark","bitter","blade","blossom","bramble","brow","bush","copse","covert","dawn","deep","fall","fern","gentle","gnarl","grove","hard","heart","husk","leaf","limb","mild","nettle","oak","pad","root","scrub","shadow","silver","snow","somber","splinter","spring","sprout","summer","tangle","tendril","thorn","trunk","twig","vine","wild","winter","wise","worm"];
var nm7 = ["","","","","","","","","bark","bellow","blade","blossom","bramble","brow","copse","covert","crown","fern","fir","flower","glade","grove","heart","husk","leaf","limb","limbs","root","scrub","shade","shrub","spine","sprout","stalk","stand","strider","stump","tendril","thorn","trunk","twig","wald","walker","wood"];
var nm8 = ["Chorus","Dancer","Dryad","Dryad","Dryad","Dryad","Dryad","Dryad","Elder","Emissary","Enchantress","Guardian","Legate","Mage","Militant","Naturalist","Outrider","Pathfinder","Ranger","Scout","Sentinel","Sophisticate","Stalker","Trickster","Vanguard","Walker"];
var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm5.length);
			rnd4 = Math.floor(Math.random() * nm2.length);
			if(i < 2){
				names = nm1[rnd] + nm2[rnd2] + nm5[rnd3] + nm2[rnd4];
			}else{
				rnd3 = Math.floor(Math.random() * nm3.length);
				rnd5 = Math.floor(Math.random() * nm4.length);
				rnd6 = Math.floor(Math.random() * nm2.length);
				while(nm3[rnd3] === nm4[rnd5]){
					rnd5 = Math.floor(Math.random() * nm4.length);
				}
				if(i < 4){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + nm2[rnd6];
				}else{
					names = nm1[rnd] + nm2[rnd4] + nm5[rnd5] + nm2[rnd2] + nm3[rnd3] + nm2[rnd6];
				}
			}
		}else{
			rnd = Math.floor(Math.random() * nm6.length);
			rnd2 = Math.floor(Math.random() * nm7.length);
			while(nm6[rnd] === nm7[rnd2]){
				rnd2 = Math.floor(Math.random() * nm7.length);
			}
			rnd3 = Math.floor(Math.random() * nm8.length);
			names = nm6[rnd] + nm7[rnd2] + " " + nm8[rnd3];
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