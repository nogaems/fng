var nm1 = ["b","d","g","j","n","m","r","v","z"];
var nm2 = ["a","e","o","a","e","o","u"];
var nm3 = ["g","l","m","n","r","v","z","fr","g","gr","gd","l","lg","ld","lm","m","mn","ml","n","ng","nd","nl","nr","nz","r","rg","rv","rd","rl","v","vr","vl","z","zr","zl"];
var nm4 = ["d","g","l","m","n","r","t","v","z"];
var nm5 = ["","","","","","","d","g","l","ld","m","n","nd","nt","s","sk","t","th"];

var nm6 = ["alpen","amber","autumn","bark","blade","blanch","bog","branch","bristle","broad","cloud","copse","coven","crag","dawn","dead","dew","dun","dusk","ever","far","fern","forest","grand","grass","grim","heart","husk","iron","jade","leaf","lumber","marsh","meadow","mirror","mist","moss","needle","noble","orb","petal","pulp","root","rough","seed","shade","shadow","shrub","silent","splinter","sprig","stalk","tall","thorn","timber","weald","weather","wicker","wild","wood","young"];
var nm7 = ["bark","beard","blade","bloom","blossom","bough","bramble","branch","breeze","copse","covert","crest","crown","dew","fern","fir","glade","glow","gnarl","grove","knot","limb","root","seed","shade","shadow","shrub","splint","splinter","sprout","spruce","stalk","stand","trunk","twig","ward","wood"];
var nm8 = ["Abomination","Agent","Ambassador","Ancient","Cerberus","Champion","Chaperone","Cohort","Consul","Custodian","Delegate","Elder","Emissary","Envoy","Forerunner","Guard","Guardian","Harbinger","Healer","Keeper","Mystic","Oak","Oberserver","Oracle","Patrol","Prime","Protector","Safeguard","Sage","Scion","Seer","Sentinel","Shaman","Shepherd","Summoner","Tower","Treefolk","Warden","Warrior","Watcher","Acacia","Alder","Ash","Aspen","Azalea","Balsa","Bamboo","Baobab","Bayonet","Beech","Birch","Box","Buckeye","Buckthorn","Bunya","Bush","Cassava","Catalpa","Cedar","Conifer","Cycad","Cypress","Elder","Elm","Eucalyptus","Fir","Hawthorn","Hazel","Hemlock","Hickory","Holly","Hornbeam","Juniper","Larch","Leaf","Locust","Magnolia","Mahogany","Mangrove","Maple","Medlar","Milkbark","Oak","Oleander","Palm","Palmetto","Persimmon","Pine","Poplar","Privet","Rhododendron","Rowan","Sequoia","Spruce","Strongbark","Sumac","Sycamore","Tree","Viburnum","Willow","Wood","Yew","Yucca"];

var nm9 = ["Abomination","Agent","Ambassador","Ancient","Cerberus","Champion","Chaperone","Cohort","Consul","Custodian","Delegate","Elder","Emissary","Envoy","Forerunner","Guard","Guardian","Harbinger","Healer","Keeper","Mystic","Oak","Oberserver","Oracle","Patrol","Prime","Protector","Safeguard","Sage","Scion","Seer","Sentinel","Shaman","Shepherd","Summoner","Tower","Treefolk","Warden","Warrior","Watcher"];
var nm10 = ["Acacia","Alder","Ash","Aspen","Azalea","Balsa","Bamboo","Baobab","Bayonet","Beech","Birch","Box","Buckeye","Buckthorn","Bunya","Bush","Cassava","Catalpa","Cedar","Conifer","Cycad","Cypress","Elder","Elm","Eucalyptus","Fir","Hawthorn","Hazel","Hemlock","Hickory","Holly","Hornbeam","Juniper","Larch","Leaf","Locust","Magnolia","Mahogany","Mangrove","Maple","Medlar","Milkbark","Oak","Oleander","Palm","Palmetto","Persimmon","Pine","Poplar","Privet","Rhododendron","Rowan","Sequoia","Spruce","Strongbark","Sumac","Sycamore","Tree","Viburnum","Willow","Wood","Yew","Yucca"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm5.length | 0;
			while(nm5[rnd3] === nm1[rnd]){
				rnd3 = Math.random() * nm5.length | 0;
			}
			if(i < 2){
				while(rnd3 < 6 || nm5[rnd3] === nm1[rnd]){
					rnd3 = Math.random() * nm5.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm5[rnd3];
			}else{
				rnd4 = Math.random() * nm3.length | 0;
				rnd5 = Math.random() * nm2.length | 0;
				while(nm5[rnd3] === nm3[rnd4]){
					rnd3 = Math.random() * nm5.length | 0;
				}
				if(i < 4){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm2[rnd5] + nm5[rnd3];
				}else{
					rnd6 = Math.random() * nm4.length | 0;
					rnd7 = Math.random() * nm2.length | 0;
					while(nm5[rnd3] === nm4[rnd6]){
						rnd6 = Math.random() * nm4.length | 0;
					}
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm2[rnd5] + nm4[rnd6] + nm2[rnd7] + nm5[rnd3];
				}
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
			rnd = Math.random() * nm10.length | 0;
			rnd2 = Math.random() * nm9.length | 0;
			names = nm10[rnd] + " " + nm9[rnd2];
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