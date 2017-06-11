var nm1 = ["b","c","d","g","j","k","q","t","v","z"];
var nm2 = ["a","o","u","a","o","u","a","o","u","e","i"];
var nm3 = ["cc","dd","gg","gh","lc","lg","lk","lm","ln","nd","ng","nk","nq","nt","rb","rd","rc","rg","rk","rm","rn","rr","rt","sc","sh","sk","st","th"];

var nm4 = ["amber","arc","ash","blight","boulder","bright","bronze","cinder","clear","cold","crystal","dark","ember","even","flame","flint","fore","full","fuse","glass","glow","grand","great","hard","haze","hex","high","iron","keen","light","micro","molten","moon","mourn","nehter","plain","pure","pyre","rough","rumble","rune","saber","shadow","soft","solid","soul","steel","stone","storm","strong","terra","thunder","twilight","void"];
var nm5 = ["bane","bash","beam","bend","bough","bound","braid","brand","brow","claw","crest","crown","dust","fist","flaw","force","forge","forged","fury","glow","grip","guard","hammer","helm","husk","limb","mane","mark","maul","might","plate","ridge","shard","shield","spark","spine","splint","stalk","stand","steel","stride","surge","synth","tether","ward","watch"];
var nm6 = ["Attendant","Automaton","Beast","Beast of Burden","Brawler","Bruiser","Champion","Colossus","Construct","Curator","Custodian","Drifter","Golem","Guard","Guardian","Herald","Hulk","Keeper","Monstrosity","Nomad","Overseer","Pilgrim","Protector","Rambler","Reclaimer","Retainer","Roamer","Sentinel","Shepherd","Statue","Stroller","Titan","Vagabond","Voyager","Wanderer","Warden","Warrior","Watcher","Golem","Golem","Golem","Golem","Golem","Golem","Golem","Construct","Construct","Construct"];

var nm7 = ["Acidic","Advanced","Alabaster","Alloy","Altar","Ancestral","Anchored","Ancient","Animated","Basalt","Battered","Brass","Broken","Bruised","Buoyant","Clay","Cobalt","Complex","Corrupt","Corrupted","Crimson","Crumbling","Crystal","Defiant","Dense","Emblazoned","Enchanted","Etched","Flint","Frost","Frozen","Gaseous","Glass","Gold","Grand","Grave","Grim","Hematite","Hollow","Igneous","Iron","Jade","Jagged","Junk","Lead","Limestone","Lodestone","Lunar","Malachite","Monstrous","Mossy","Motionless","Obedient","Obsidian","Onyx","Opal","Ornate","Platinum","Primal","Prime","Pristine","Pungent","Radiant","Ruby","Rusted","Sand","Sandstone","Sanguine","Sapphire","Shadow","Shadowy","Silent","Silver","Skeletal","Solar","Spire","Steel","Straw","Titanium","Twin","Vacant","Vibrant","Volatile","Winged"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm3.length | 0;
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3];
		}else if(i < 8){
			rnd = Math.random() * nm4.length | 0;
			rnd2 = Math.random() * nm5.length | 0;
			while(nm4[rnd] === nm5[rnd2]){
				rnd2 = Math.random() * nm5.length | 0;
			}
			rnd3 = Math.random() * nm6.length | 0;
			names = nm5[rnd] + nm5[rnd2] + " " + nm6[rnd3];
		}else{
			rnd = Math.random() * nm7.length | 0;
			rnd2 = Math.random() * nm6.length | 0;
			names = nm7[rnd] + " " + nm6[rnd2];
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