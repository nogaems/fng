var nm2 = ["Tower","Spire","Lookout","Pillar","Obelisk","Tower","Tower","Tower"];
var nm3 = ["a","e","i","o","u","","","","","","","",""];
var nm4 = ["","","","","","b","br","c","cr","d","dr","g","gr","j","k","kr","kn","p","pr","q","qr","r","st","str","t","tr","v","vr","w","x","z"];
var nm5 = ["a","e","i","o","u","a"];
var nm6 = ["bahn","barin","baris","belle","beus","bin","bine","bus","dalf","dali","deis","del","delis","disum","dium","dore","dores","dus","faeh","farihm","faris","fea","feus","flyn","fora","forn","fyne","gaell","garis","gast","geor","georis","gis","gorim","grith","groln","grur","haen","hagan","harad","haris","harise","harith","hione","hith","hone","jahr","jamar","jeik","jelle","jes","jest","jiane","jior","jor","jyll","kalis","kealis","kely","key","kius","kon","kora","kore","kron","laes","leas","lenor","leus","lin","lius","lore","lune","lyn","maev","maex","mari","marim","mazz","meazz","monar","monora","morith","morn","naxix","naxx","neas","neus","nilor","nior","nirn","nitor","nora","norim","paen","pan","phi","phior","pianne","pius","pniar","prix","prixys","pyx","qian","qille","qiohn","qiohr","qium","qix","qor","qora","qrax","quam","ras","rhan","rihan","ris","rius","ro","ronin","rune","saem","shan","sim","sinor","sior","soph","sorin","strea","strum","taris","tarum","taz","thal","thar","tior","tosh","trix","vae","veus","via","viar","vior","vira","vius","vras","vys","waelle","wahl","weahl","wix","wras","wrick","wrys","wyn","xarif","xaryl","xea","xeor","xis","xium","xius","xon","xone","xyll","ydae","ydor","yeas","yna","ynas","yora","yorn","yrin","yus","zahn","zahr","zax","zif","zohr","zohra","zor","zora","zyxi"];
var br = "";

function nameGen(){
	
	var nm1 = ["Aberrant","Alluring","Ambition","Anchored","Ancient","Apparatus","Arcane","Arch","Aromatic","Austere","Banished","Bizarre","Blind","Bone","Breathing","Brilliant","Burrowing","Cackling","Canvas","Catalyst","Chained","Changing","Chaos","Clarity","Cloud","Command","Corrupting","Coursing","Crackling","Crazed","Creeping","Crumbling","Curious","Cycle","Dangling","Dark","Dead","Death","Deception","Defiant","Delirious","Demon","Demonic","Devil","Dimension","Discovery","Dream","Dreamscape","Drunk","Dynamic","Elementary","Enchanted","Enhancement","Enigma","Enlightened","Eternal","Eternity","Ethereal","Expanding","Experiment","Experimental","Exploration","Fading","Fairy","False","Feedback","Flickering","Floating","Flowing","Fluke","Fragrant","Friction","Frozen","Galaxy","Grand","Growing","Hallucination","Hanging","Hexed","Hocus","Ice","Icicle","Impulse","Infernal","Infinite","Infinity","Inked","Invention","Inverted","Invisible","Juvenile","Knowledge","Laughing","Lightning","Living","Lone","Lonely","Mad","Makeshift","Marble","Masked","Midnight","Migrating","Mind","Mirror","Morphing","Moving","Mumbling","Mysterious","Mystery","Night","Nocturnal","Novice","Obedient","Observant","Observing","Omen","Oracle","Parallel","Particle","Perpetual","Phase","Phased","Planar","Plane","Playful","Possessed","Prodigy","Prophecy","Pulse","Pulsing","Radiant","Riddle","Scented","Sentient","Servant","Serving","Shifting","Silent","Skeletal","Sleeping","Slumbering","Smiling","Smoking","Smoldering","Sparking","Sparkling","Spell","Spellbound","Surprise","Talking","Temporal","Thunder","Timeless","Tired","Toppling","Tranquil","Traveling","Turning","Vanishing","Veiled","Vessel","Volatile","Wandering","Warped","Watching","Whispering","Wicked","Wild","Winged","Wisdom"];
	
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm2.length);
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			names = "The " + nm1[rnd] + " " + nm2[rnd2];
			nm1.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			rnd3 = Math.floor(Math.random() * nm4.length);
			rnd4 = Math.floor(Math.random() * nm5.length);
			rnd5 = Math.floor(Math.random() * nm6.length);
			if(rnd > 4){
				while(rnd3 < 5){
					rnd3 = Math.floor(Math.random() * nm4.length);
				}
			}
			names = nm3[rnd] + nm4[rnd3] + nm5[rnd4] + nm6[rnd5] + " " + nm2[rnd2];
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