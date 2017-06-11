var nm1 = ["","","","","","b","h","kh","m","ms","n","ng","ps","r","s","t","ts","z"];
var nm2 = ["a","e","o","a","e","o","a","e","o","a","e","o","a","e","o","a","e","o","ai"];
var nm3 = ["b","ch","d","g","h","hm","ht","k","kh","lh","m","n","nh","nkh","nm","nn","p","ph","r","rj","rp","rs","rt","sht","ss","t","z"];
var nm4 = ["b","ch","h","hb","k","kh","l","m","mh","mm","n","p","ph","r","rr","s","t"];
var nm5 = ["","","","b","f","kh","n","nk","pt","r","s","t"];

var nm6 = ["","","","","","","","","","","b","h","k","kh","m","n","r","s","sh","t","th","z"];
var nm7 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ia","uu","ii"];
var nm8 = ["d","h","hm","ht","k","m","mm","n","nk","nkh","nn","nq","nqt","p","r","rb","rs","s","sht","sm","sn","sp","st","t","z"];
var nm9 = ["c","h","k","kh","l","m","mn","n","nh","p","pp","r","s","t","tt"];
var nm10 = ["","","","","","f","l","m","s","ts","th"];

var nm11 = ["Ageless","Analytic","Anchored","Ancient","Angelic","Argent","Austere","Azure","Basilica","Behemoth","Belltower","Beryl","Brilliant","Campanile","Carmine","Cathedral","Cenotaph","Cerulean","Charade","Charm","Cobalt","Colossal","Consecrated","Conundrum","Courteous","Crimson","Crux","Cryptogram","Defiant","Diligent","Distant","Dutiful","Ecstatic","Edifice","Elated","Elegant","Elemental","Enigma","Enlightened","Esteemed","Eternal","Fearless","Feline","Flawed","Flawless","Gargantuan","Gifted","Goliath","Graceful","Gracious","Grand","Grandiose","Harmonious","Hex","Hieroglyph","Horizon","Humongous","Hymn","Idle","Indigo","Infinite","Infinity","Intrepid","Juvenile","Knot","Leviathan","Magister","Majestic","Malachite","Mindful","Miniature","Monolith","Motionless","Mysterious","Mystery","Mystic","Mythic","Mythical","Obelisk","Observatory","Obsidian","Onyx","Oracle","Oratory","Ornate","Parable","Pictograph","Pleased","Poised","Predicament","Prestigious","Primal","Prime","Prognostic","Proud","Pyramid","Rebus","Reckless","Riddle","Rune","Sanctuary","Sandstone","Sanguine","Secret","Sharding","Shrine","Silver","Spire","Supreme","Swift","Symbol","Synagogue","Temple","Timeless","Titan","Tomb","Tremendous","Twin","Twister","Verdigris","Vermilion","Vigilant","Watchful"];
var nm12 = ["Abettor","Academic","Adjudicator","Agent","Ambassador","Appraiser","Arbiter","Attendant","Augur","Avenger","Cerberus","Champion","Chancellor","Chaperon","Conservator","Consul","Council","Curator","Defender","Dignitary","Diplomat","Disciple","Emissary","Envoy","Guard","Guardian","Handler","Judge","Keeper","Magister","Magistrate","Marshal","Master","Maven","Mediator","Moderator","Negotiator","Oracle","Preserver","Prophet","Protector","Reconciler","Sage","Savant","Scholar","Sentinel","Sentry","Servant","Shepherd","Sphinx","Steward","Treasurer","Warden","Watcher"];
var nm13 = ["Abettor","Academic","Adjudicator","Agent","Ambassador","Appraiser","Arbiter","Attendant","Augur","Avenger","Cerberus","Champion","Chancellor","Chaperon","Conservator","Consul","Council","Curator","Defender","Dignitary","Diplomat","Disciple","Emissary","Envoy","Guard","Guardian","Judge","Keeper","Magister","Magistrate","Marshal","Master","Maven","Mediator","Moderator","Negotiator","Oracle","Preserver","Prophet","Protector","Reconciler","Sage","Savant","Scholar","Sentinel","Sentry","Servant","Shepherd","Steward","Treasurer","Warden","Watcher","of Advice","of Cryptograms","of Discovery","of Eternity","of Fiction","of Games","of Gifts","of Gold","of Grace","of Great Minds","of Harmony","of Hymns","of Ideals","of Infinity","of Invention","of Jewels","of Journeys","of Judgment","of Justice","of Knowledge","of Language","of Masks","of Memories","of Minds","of Music","of Mysteries","of Observation","of Obsidian","of Onyx","of Oracles","of Pride","of Prophecies","of Prosperity","of Puzzles","of Riddles","of Rumors","of Sapphire","of Secrets","of Teachings","of Theories","of Time","of Truth","of Voices","of Whispers","of Wisdom","of the Ages","of the Basilica","of the Cathedral","of the Chimes","of the Crown","of the Crypt","of the Enigma","of the Flame","of the Flock","of the Library","of the Monolith","of the Obelisk","of the Observatory","of the Pinnacle","of the Pyramid","of the Shrine","of the Spires","of the Temple","of the Tomb","of the Tower","of the Zephyr"];

var br = "";

function nameGen(type){
	var tp = type;
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(tp === 1){
			if(i < 6){
				rnd = Math.random() * nm6.length | 0;
				rnd2 = Math.random() * nm7.length | 0;
				rnd3 = Math.random() * nm8.length | 0;
				rnd4 = Math.random() * nm7.length | 0;
				rnd5 = Math.random() * nm10.length | 0;
				while(nm6[rnd] === nm8[rnd3]){
					rnd3 = Math.random() * nm8.length | 0;
				}
				while(nm10[rnd5] === nm8[rnd3]){
					rnd5 = Math.random() * nm10.length | 0;
				}
				if(i < 2){
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm10[rnd5];
				}else{
					rnd6 = Math.random() * nm9.length | 0;
					rnd7 = Math.random() * nm7.length | 0;
					while(nm9[rnd6] === nm8[rnd3]){
						rnd6 = Math.random() * nm9.length | 0;
					}
					if(i < 4){
						names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd6] + nm7[rnd7] + nm10[rnd5];
					}else{
						names = nm6[rnd] + nm7[rnd2] + nm9[rnd6] + nm7[rnd7] + nm8[rnd3] + nm7[rnd4] + nm10[rnd5];
					}
				}
			}else if(i < 8){
				rnd = Math.random() * nm11.length | 0;
				rnd2 = Math.random() * nm12.length | 0;
				names = nm11[rnd] + " " + nm12[rnd2];
			}else{
				rnd = Math.random() * nm13.length | 0;
				names = "Sphinx " + nm13[rnd];
			}
		}else{
			if(i < 6){
				rnd = Math.random() * nm1.length | 0;
				rnd2 = Math.random() * nm2.length | 0;
				rnd3 = Math.random() * nm3.length | 0;
				rnd4 = Math.random() * nm2.length | 0;
				rnd5 = Math.random() * nm5.length | 0;
				while(nm1[rnd] === nm3[rnd3]){
					rnd3 = Math.random() * nm3.length | 0;
				}
				while(nm5[rnd5] === nm3[rnd3]){
					rnd5 = Math.random() * nm5.length | 0;
				}
				if(i < 2){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
				}else{
					rnd6 = Math.random() * nm4.length | 0;
					rnd7 = Math.random() * nm2.length | 0;
					while(nm4[rnd6] === nm3[rnd3]){
						rnd6 = Math.random() * nm4.length | 0;
					}
					if(i < 4){
						names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
					}else{
						names = nm1[rnd] + nm2[rnd2] + nm4[rnd6] + nm2[rnd7] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
					}
				}
			}else if(i < 8){
				rnd = Math.random() * nm11.length | 0;
				rnd2 = Math.random() * nm12.length | 0;
				names = nm11[rnd] + " " + nm12[rnd2];
			}else{
				rnd = Math.random() * nm13.length | 0;
				names = "Sphinx " + nm13[rnd];
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