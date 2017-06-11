function nameGen(){
			var nm1 = ["7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"];
			var nm2 = ["marches as one","moves as if a single being","advances as a whole","strides along as one","moves as one","strides onwards as a whole","moves forward, all together as one","marches onwards as one body","marches forward as if a single being","moves forward","marches onwards","strides onwards","moves onwards","marches forward","advances","marches along","strides forward","advances steadily"];
			var nm3 = ["Each step in unison with the others","Every step in perfect harmony with the others","A constant beat of step after step","A constant drumming of synchronized steps","A symphony of steps, each perfectly alligned with the one next to it","Every step alligned to the beat of the marching drums","Step after step on the rhythm of the marching drums","A cadence of steps after steps, all alligned with each other","Thousands of feet, all moving as individuals","Thousands of feet trample the ground beneath it","Step after step of an unsynchronized march","A cacophony of sound from a disharmonious march","A barrage of noise from thousands of individual steps","A storm of sound from disorganized steps after steps","A thunder of thousands of unsynchronized steps","A constant roar of thousand of steps after steps after steps","A continous noise of thousands of feet trampling the ground beneath it","An endless barrage of the sound of thousands of feet marching onwards"];
			var nm4 = ["the thundering sound alone is enough to put fear into even the bravest of souls","the sheer size of this army is enough to make any enemy tremble in fear","it would take a brave or stupid soul to not be intimidated by this army","there's not a single creature around for miles who's unaware of this army","the vibrations in the ground will make sure even the deaf know this army is coming","only a fool might mistake the march of this army for a small earthquake","leaving only scores of tracks in its wake, a clear sign for anybody passing by","there's not a soul nearby who's oblivious to this army's march","even the dead can feel there's an army on the move","even the most ignorant of souls will know there's an army marching onwards","there's no need for a scout to state the obvious: there's an army marching forward","drowning out all other sound from the vicinity","like a giant snake sliding smoothly across the lands"];
			var nm5 = ["sound of chainmail and armor clashing together","clanging of heavy armor","rustling of chainmail and leather","rustling of cloth and the jingling of chainmail","squeaking of leather and clanging of armor","sound of heavy armor clashing together","sound of leather, chainmail and armor clashing together","squeaking of leather and jingling of chainmail"];
			var nm6 = ["creaking of wood of the ballistae and siege engines","creaking of metal of the siege engines","thumping steps of the armored giants","creaking of wood of the catapults","creaking of wood and metal of the siege engines","creaking of wood of the supply carts and siege engines","creaking of metal of the siege engines and supply carts","thumping steps of the war elephants"];
			var nm7 = ["sounds of the horses","growls of the war hounds","growlsg and grunts of the war animals","sounds of the war mounts","complaints of the soldiers","voices of the soldiers","growls of the war tigers","groans of the foot soldiers"];
			var nm8 = ["Nobody speaks a word to each other, partially due to the overwhelming noise around them, but mostly due to their focus","Nobody speaks a word to each other, some because they're focused on the task ahead, others because they dread what might happen next","Nobody speaks a word to each other, whether it's because of fear, focus or something else is uncertain, but there's too much noise to talk anyway","Not a word is spoken among the soldiers, some are simply too exhausted from the long march, others are still focused on the enevitable battle","Not a word is spoken among the soldiers, exhaustion and some fear have set in now that the long march is nearing its destination","The noise is too overwhelming to allow for any conversation to take place, but the soldiers are far too focused on the battle ahead anyway","The noise is too overwhelming to allow for conversations between the soldiers, for many this helps to stay focused, for others it adds to the fear of battle","The soldiers are talking to each other despite the barrage of noise around them. Most speak of home, others speak of a longing for the battle ahead","The soldiers are chatting away, noise or no noise the soldier need to take their minds of of what's ahead, talking is the best way to do so","Despite all the noise the soldiers are talking and laughing with each other, many are eager for the battle ahead, at least for now","Despite all the noise the soldiers are talking, laughing and joking around, it's unclear whether this is a means to take their mind of the battle ahead or if they look forward to it","Virtually all soldiers are talking to each other despite the noise around them. It seems most are eager to fight the battle they're marching towards","Virtually all soldiers are talking despite the noise around them. Laughter is a common sight, many soldiers seem to be looking forward to the battle ahead ","The soldiers are talking amongst themselves despite the noise around them. Some need it to take their minds of the battle ahead, some need it to hype themselves up for it"];
			var nm9 = ["The entire army is as one, a well oiled machine ready to take on and defeat their enemy","The entire army is as one, one collective mind with a single goal: Defeat the enemy","The entire army is as one, as if they all share a single mind with a single purpose, which is to crush their enemies","The entire army is as one. Everybody has the same mindset and the same goal in mind: crush the enemy and enjoy it while it lasts","The entire army is as one. All with the same goal in mind and all eager to fulfill it. Destroy the enemy or die trying","The entire army is as one. A single collective mind with a single goal ahead of them: Annihilate the enemy and have fun doing it","The entire army is as one, not a single soul with a different mindset. The enemy will be crushed or they'll die trying","The army is a collection of separate groups, but they all share the same goal: Defeat the enemy and make it out alive","The army is a collection of separate groups without a single mindset, but they all want the same: Make it out alive","The army is a mismatch of separate groups, but despite this they do share the same goal: Kill the enemy and make it back home","The army is a mismatch of isolated groups, but they'll work together as they share the same goal: Destroy the enemy and make it back home","The army lacks unity, there's not a single mindset, but there is a single goal: Make sure you survive the war and get back home safely","The army lacks unity, but despite their differences they do share the same goal: Crush the enemy, enjoy it while it lasts and make it out alive","The army lacks unity, there's no collective mindset besides the fact they all want to make it out alive"];
			var nm10 = ["footsoldiers armed with swords, shields and pikes","footsoldiers armed with swords and large shields","bowmen with incredible range","crossbow units ready to fire the first salvo","charge units armed with pikes","charge units armed with sword and shield","charge units armed with two swords","charge units armed with huge maces and axes","flintlock units ready to fire the first salvo","footsoldiers armed with spears and large shields","charge cavalry armed with bows and swords","charge cavalry armed with spears, shields and swords","charge cavalry armed with javelins, shields and swords","charge cavalry armed with bombs, shields and swords"];
			var nm11 = ["footsoldiers armed with swords and shields","footsoldiers armed with powerful two-handed swords","bowmen ready for short range salvos","crossbow units ready to fire","footsoldiers armed with pikes","footsoldiers armed with long sword and huge shields","footsoldiers armed with two swords","footsoldiers armed with huge maces and axes","bomb throwers ready to unleash hell","footsoldiers armed with spears and large shields","cavalry armed with bows, shields and swords","cavalry armed with spears, shields and swords","cavalry armed with several swords","cavalry armed with shields and swords"];
			var nm12 = ["elite footsoldiers armed with swords and shields","elite footsoldiers armed powerful with two-handed swords","elite bowmen with high precision aim","elite crossbow units with deadly precision","elite footsoldiers armed with pikes","elite footsoldiers armed with long sword and huge shield","elite footsoldiers armed with two swords","elite footsoldiers armed with huge maces and axes","elite spearmen on horseback","elite footsoldiers armed with spears and large shields","elite swordsmen on horseback","elite archers on horseback","elite soldiers on horseback","elite sword cavalry"];
			var nm13 = ["dozens of other warrior regiments","many other regiments, including mercenaries and allied soldiers","many other regiments, including mercenaries and slave soldiers","many other regiments, including allied soldiers, as well as slave soldiers"];
			var nm14 = ["several cavalry units","different types of archery units","stealth units","several bomb units","various flanking units","various charging units","many elite units","several defensive units","artillery units","units of war animals"];
			
			var rnd1 = parseInt(Math.floor(Math.random() * nm1.length));
			var rnd2 = parseInt(Math.floor(Math.random() * nm2.length));
			var rnd3 = parseInt(Math.floor(Math.random() * nm3.length));
			if(rnd2 < 10){
				while(rnd3 > 9){
					rnd3 = parseInt(Math.floor(Math.random() * nm3.length));
				}
			}
			var rnd4 = parseInt(Math.floor(Math.random() * nm4.length));
			var rnd5 = parseInt(Math.floor(Math.random() * nm5.length));
			var rnd6 = parseInt(Math.floor(Math.random() * nm6.length));
			var rnd7 = parseInt(Math.floor(Math.random() * nm7.length));
			var rnd8 = parseInt(Math.floor(Math.random() * nm8.length));
			var rnd9 = parseInt(Math.floor(Math.random() * nm9.length));
			var rnd10 = parseInt(Math.floor(Math.random() * nm10.length));
			var rnd11 = parseInt(Math.floor(Math.random() * nm11.length));
			while(rnd10 === rnd11){
				rnd11 = parseInt(Math.floor(Math.random() * nm11.length));
			}
			var rnd12 = parseInt(Math.floor(Math.random() * nm12.length));
			while(rnd12 === rnd11 || rnd12 === rnd10){
				rnd12 = parseInt(Math.floor(Math.random() * nm12.length));
			}
			var rnd13 = parseInt(Math.floor(Math.random() * nm13.length));
			var rnd14a = parseInt(Math.floor(Math.random() * nm14.length));
			var rnd14b = parseInt(Math.floor(Math.random() * nm14.length));
			while(rnd14b === rnd14a){
				rnd14b = parseInt(Math.floor(Math.random() * nm14.length));
			}
			var rnd14c = parseInt(Math.floor(Math.random() * nm14.length));
			while(rnd14b === rnd14c || rnd14a === rnd14c){
				rnd14c = parseInt(Math.floor(Math.random() * nm14.length));
			}
			var rnd14d = parseInt(Math.floor(Math.random() * nm14.length));
			while(rnd14d === rnd14a || rnd14d === rnd14b || rnd14d === rnd14c){
				rnd14d = parseInt(Math.floor(Math.random() * nm14.length));
			}
			
			var name = "The ground trembles as an army of " + nm1[rnd1] + "0,000 " + nm2[rnd2] + ". " + nm3[rnd3] + ", " + nm4[rnd4] + ".";				
			
			var name2 = "Up close it's the " + nm5[rnd5] + " which overpowers all other sounds. The " + nm6[rnd6] + " can be heard only faintly and the " + nm7[rnd7] + " are all but drowned out completely.";
			var name3 = nm8[rnd8] + ". " + nm9[rnd9] + ".";
			
			var name4 = "The front is lead by eager " + nm10[rnd10] + ". They're followed by " + nm11[rnd11] + ", who in turn are followed by " + nm12[rnd12] + ".";
			var name5 = "The ranks are filled with " + nm13[rnd13] + ", including " + nm14[rnd14a] + ", " + nm14[rnd14b] + ", " + nm14[rnd14c] + " and " + nm14[rnd14d] + ".";
			
			var br = [];
			for(i = 0; i < 6; i++){
				br[i] = document.createElement('br');	
			}
			if(document.getElementById("result")){
				document.getElementById("placeholder").removeChild(document.getElementById("result"));
			}
			
			var element = document.createElement("div");
			element.setAttribute("id", "result");
			element.appendChild(document.createTextNode(name));
			element.appendChild(br[0]);
			element.appendChild(br[1]);
			element.appendChild(document.createTextNode(name2));
			element.appendChild(br[2]);
			element.appendChild(document.createTextNode(name3));
			element.appendChild(br[3]);
			element.appendChild(br[4]);
			element.appendChild(document.createTextNode(name4));
			element.appendChild(br[5]);
			element.appendChild(document.createTextNode(name5));
			document.getElementById("placeholder").appendChild(element);
		}	