var nm1 = ["","","","d","j","kh","l","m","n","r","rh","th","v"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","a","e","i","o","e","a","o","eo","ea","aa"];
var nm3 = ["f","g","l","ll","m","n","r","s","ss","v","z","dr","f","g","l","ll","lm","ln","m","mn","n","nm","r","rl","s","ss","v","z"];
var nm4 = ["d","ll","ld","ln","lm","mn","mr","nr","s","r","v","z"];
var nm5 = ["","","","c","d","l","ll","ld","m","n","nn","r","s","th"];

var nm6 = ["","","","","","dw","gl","gw","h","k","m","n","ph","r","s","t","th","y"];
var nm7 = ["a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","o","u","o","u","a","e","i","ae","ea","ia"];
var nm8 = ["dh","ff","l","lv","lr","lm","ll","m","mm","n","nh","nn","ny","ph","s","ss","sh","shm","th","v","vr","y","ys"];
var nm9 = ["l","ll","n","nn","r","rr","t","y","z"];
var nm10 = ["","","","","","","","","","","","","","","","h","l","n","s","th"];

var nm11 = ["g","h","k","l","m","n","r","s","t","th","v","z"];
var nm12 = ["a","e","i","o","u","a","i"];
var nm13 = ["g","gg","l","ll","m","mm","n","nn","r","rr","s","ss","v","vv","z","zz","gr","gn","hr","hn","ldr","ld","lr","ln","lm","mr","mdr","mv","mn","nd","nr","nm","ngr","ndr","rdr","rl","rg","rgr","rv","st","sk","sl","str","tr","thr","vr","vn","zr","zdr","zd"];
var nm14 = ["g","l","n","s","t","th"];

var nm15 = ["alder","alpen","amber","autumn","beech","birch","bitter","blight","blood","border","boulder","bramble","bright","bronze","cedar","cliff","cloud","copper","coven","crag","crest","dark","dawn","deep","dense","dew","dream","dusk","elm","ever","eye","fall","far","fern","fir","flint","fore","free","glade","glow","gnarl","gold","grand","grass","great","green","grove","hallow","hard","haven","hazel","heart","high","keen","knot","larch","life","light","lone","long","low","luna","lunar","maple","marsh","meadow","mild","moon","moss","nettle","night","noble","nor","oak","oaken","oat","peace","pine","plain","pride","proud","pyre","rapid","rich","rover","scrub","seed","silver","sky","snow","solar","splinter","spring","spruce","stag","star","still","stone","storm","stout","strong","summer","sun","swift","terra","thistle","thorn","thunder","timber","tree","true","tusk","vast","vine","weather","whit","wild","willow","wind","wire","wise","wood","yew"];
var nm16 = ["arrow","bane","bark","bellow","bender","binder","blade","blight","bloom","blossom","bluff","bough","bow","braid","bramble","branch","brand","breath","breeze","brook","brow","caller","chaser","cloud","copse","cover","covert","cradle","crag","crest","crown","dancer","dew","down","draft","drifter","eye","fall","fern","fir","flare","force","forge","gaze","glade","gleam","glide","glory","glove","glow","grip","grove","guard","gust","hand","hart","haven","heart","hide","hilt","horn","hunter","husk","lance","land","larch","lash","leaf","light","limb","lore","mane","mantle","mark","more","needle","nettle","pike","ridge","root","runner","scape","seed","shade","shadow","shard","shine","shroud","shrub","side","soil","spire","spring","surge","sworn","talon","tender","thorn","trunk","vine","watch","weald","wind","wood","woods"];
var nm17 = ["Acclaimed","Adept","Advanced","Agile","Ambush","Arbor","Armored","Athletic","Attentive","Aura","Aurora","Blind","Bloom","Boreal","Bright","Brilliant","Bruised","Calm","Carapace","Careful","Cautious","Composed","Crafty","Crazed","Dapper","Deadly","Defiant","Determined","Devoted","Diligent","Discrete","Eager","Essence","Exalted","Exemplary","False","Famous","Fauna","Fearless","Feisty","Fierce","Flora","Focused","Forsaken","Frontier","Gifted","Grand","Great","Grim","Hidden","Honored","Illustrious","Infamous","Keen","Light","Loyal","Menacing","Mysterious","Powerful","Prestigious","Prime","Quick","Quiet","Radiant","Reckless","Renegade","Savant","Shady","Silent","Suspicious","Swift","Trained","Vengeful","Vicious","Vigilant","Violent","Wicked","Wrathful","Wretched"];
var nm18 = ["Acolyte","Animist","Archdruid","Archer","Architect","Archmage","Artisan","Assassin","Barbarian","Bard","Battalion","Battlemage","Battlerider","Battlewarden","Beastcaller","Beastmaster","Berserker","Biomancer","Blademaster","Bladesinger","Bowmaster","Branchbender","Branchcaller","Brigade","Cavalier","Cavalry","Champion","Channeler","Commander","Conduit","Courier","Crafter","Cultivator","Dancer","Denizen","Druid","Elder","Elite","Emissary","Empath","Enforcer","Entourage","Exiled","Explorer","Forger","Gamekeeper","Gatekeeper","Guardian","Guide","Guildmage","Handservant","Harbinger","Healer","Herald","Herder","Hero","Hexhunter","Hivemaster","Hunter","Initiate","Knight","Leader","Ledgewalker","Lookout","Lorebearer","Mage","Magistrate","Messenger","Mystic","Operative","Oracle","Outrider","Paragon","Pathcutter","Pathfinder","Pathwarden","Patrol","Pioneer","Piper","Preserver","Priest","Ranger","Rider","Rogue","Rootbreeder","Rootcaller","Rootspeaker","Runner","Sage","Savage","Scout","Scrapper","Seeker","Seer","Sentinel","Sentry","Servant","Shaman","Shepherd","Skyrider","Skysweeper","Spirit Guide","Spy","Spymaster","Strider","Summoner","Sunsinger","Swordmaster","Tender","Tracer","Tracker","Trailblazer","Trapper","Treespeaker","Trooper","Vanguard","Vinebender","Vinebreeder","Vinecaller","Vinespeaker","Visionary","Wanderer","Warcaller","Warden","Warrior","Watcher","Wayfinder","Whisperer","Wolf-Rider","Woodcloaker","Zealot"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm11.length);
		rnd2 = Math.floor(Math.random() * nm12.length);
		rnd3 = Math.floor(Math.random() * nm13.length);
		rnd4 = Math.floor(Math.random() * nm12.length);
		rnd5 = Math.floor(Math.random() * nm14.length);
		lName = nm11[rnd] + nm12[rnd2] + nm13[rnd3] + nm12[rnd2] + nm14[rnd5];
		if(tp === 1){
			if(i < 6){
				rnd = Math.floor(Math.random() * nm6.length);
				rnd2 = Math.floor(Math.random() * nm7.length);
				rnd3 = Math.floor(Math.random() * nm8.length);
				rnd4 = Math.floor(Math.random() * nm7.length);
				rnd5 = Math.floor(Math.random() * nm10.length);
				while(nm10[rnd5] === nm8[rnd3]){
					rnd5 = Math.floor(Math.random() * nm10.length);
				}
				if(i < 3){
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm10[rnd5] + " " + lName;
				}else{
					rnd6 = Math.floor(Math.random() * nm7.length);
					rnd7 = Math.floor(Math.random() * nm9.length);
					while(nm9[rnd7] === nm8[rnd3]){
						rnd7 = Math.floor(Math.random() * nm9.length);
					}
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd7] + nm7[rnd6] + nm10[rnd5] + " " + lName;
				}
			}else if(i < 8){
				rnd = Math.floor(Math.random() * nm17.length);
				rnd2 = Math.floor(Math.random() * nm18.length);
				names = nm17[rnd] + " " + nm18[rnd2];
			}else{
				rnd = Math.floor(Math.random() * nm15.length);
				rnd2 = Math.floor(Math.random() * nm16.length);
				while(nm15[rnd] === nm16[rnd2]){
					rnd2 = Math.floor(Math.random() * nm16.length);
				}
				rnd3 = Math.floor(Math.random() * nm18.length);
				names = nm15[rnd] + nm16[rnd2] + " " + nm18[rnd3];
			}
		}else{
			if(i < 6){
				rnd = Math.floor(Math.random() * nm1.length);
				rnd2 = Math.floor(Math.random() * nm2.length);
				rnd3 = Math.floor(Math.random() * nm3.length);
				rnd4 = Math.floor(Math.random() * nm2.length);
				rnd5 = Math.floor(Math.random() * nm5.length);
				while(nm5[rnd5] === nm3[rnd3]){
					rnd5 = Math.floor(Math.random() * nm5.length);
				}
				if(i < 3){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + " " + lName;
				}else{
					rnd6 = Math.floor(Math.random() * nm2.length);
					rnd7 = Math.floor(Math.random() * nm4.length);
					while(nm4[rnd7] === nm3[rnd3]){
						rnd7 = Math.floor(Math.random() * nm4.length);
					}
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd7] + nm2[rnd6] + nm5[rnd5] + " " + lName;
				}
			}else if(i < 8){
				rnd = Math.floor(Math.random() * nm17.length);
				rnd2 = Math.floor(Math.random() * nm18.length);
				names = nm17[rnd] + " " + nm18[rnd2];
			}else{
				rnd = Math.floor(Math.random() * nm15.length);
				rnd2 = Math.floor(Math.random() * nm16.length);
				while(nm15[rnd] === nm16[rnd2]){
					rnd2 = Math.floor(Math.random() * nm16.length);
				}
				rnd3 = Math.floor(Math.random() * nm18.length);
				names = nm15[rnd] + nm16[rnd2] + " " + nm18[rnd3];
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