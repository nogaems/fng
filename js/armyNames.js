var nm1 = ["Angels","Black Brigade","Black Devils","Black Saints","Black Sheep","Black Wings","Blessed Battalion","Blood Bandits","Blood Battalion","Blood Brigade","Broken Brigade","Cardinal Command","Cardinal Company","Cardinal Corps","Cataclysm Corps","Challengers","Chosen","Clan","Cloud","Cluster","Congregate","Contract","Covert Battalion","Covert Company","Covert Corps","Crimsom Cloud","Crimson Clan","Crimson Commander","Crimson Company","Crimson Contract","Crimson Corps","Crimson Crew","Crimson Curators","Crimson Keepers","Crimson Wings","Crush","Crushing","Culling Cavalry","Curators","Dark Division","Death Corps","Death's Angels","Death Division","Death Formation","Death Pack","Death Patrol","Death Platoon","Death Squad","Demons","Destiny Division","Dogs","Doom Corps","Doom Squad","Doomed Ones","Ebon Enders","Ebon Eyes","Ebon Wings","Eclipse","Extinction","Extras","Final Division","Final Flight","Final Flock","Final Regiment","Fire Battalion","Fire Flight","Fire Troops","Flaming Army","Flaming Battalion","Flaming Flock","Flock","Forgotten Army","Forgotten Battalion","Forgotten Soldiers","Forsaken","Forsaken Army","Forsaken Battalion","Forsaken Flock","Forsaken Soldiers","Great Army","Great Company","Great Guard","Great Guardians","Guard","Guardians","Hallowed Herd","Hallowed Horde","Hallowed Host","Hell Hosts","Hell Squad","Hellfire Horde","Hellfire Legion","Hellfire Squad","Hellhounds","Herd","Hidden","Hollow Herd","Hollow Horde","Hollow Host","Hopeless","Horde","Host","Hounds","Illustrious","Immortals","Invincibles","Keepers","Last Division","Last Hope","Last Legion","Last Regiment","Legion","Marauders","Maroon Marauders","Maroon Martyrs","Maroon Mob","Maroon Myriad","Martyrs","Mob","Myriad","New Leadership","New Order","Night","Opposition","Order","Pacifists","Peace Bringers","Peace Corps","Phalanx","Pillagers","Preservers","Prime Battalion","Prime Platoon","Prime Preservers","Punishment","Pure","Pure Battalion","Pure Platoon","Rangers","Ravagers","Rebels","Red Rangers","Red Regiment","Red Riders","Reserve","Reserve Regiment","Retired","Robed Riders","Rose Regiment","Rose Riders","Ruby Regiment","Ruby Riders","Ruthless","Ruthless Ravagers","Ruthless Regiment","Saints","Sanguine Sentinels","Sanguine Shepherds","Sanguine Shroud","Sanguine Soldiers","Sanguine Squad","Sanguine Sundry","Sanguine Swarm","Sentinels","Serpent Soldiers","Serpent Squad","Shadow","Shepherds","Shroud","Siege Battalion","Silver Lining","Silver Soldiers","Silver Squad","Silver Swarm","Sundry","Super Soldiers","Supervisors","Supreme Army","Supreme Battalion","Supreme Command","Supreme Regiment","Swarm","Terror Troops","Thunder Troops","Titans","True Order","Trust Troops","Undefeated","Unforgiven","Union","Unstoppables","Vanquishers","Velvet Vanquishers","Velvet Veil","Velvet Victors","Venom Troops","Victors","Vortex","Void","Wardens","Watchdogs","White Wardens","White Wings"];
var nm2 = ["a","e","i","o","u","ae","ai","ao","au","aa","ee","ea","ei","eo","eu","ia","ie","io","iu","oa","oe","oi","oo","ou","ua","ue","ui","uo","uu","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""];
var nm3 = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","br","cr","dr","fr","gr","kr","pr","qr","sr","tr","vr","wr","yr","zr","str","bl","cl","fl","gl","kl","pl","sl","vl","yl","zl","ch","kh","ph","sh","yh","zh"];
var nm4 = ["aell","aen","aerion","ahir","ahr","akir","alim","apex","aral","ard","argon","arid","arix","aron","arun","ate","atir","avi","ax","axis","earal","echos","efral","elin","elior","elnach","elno","elun","emir","enmir","enron","eod","eodar","ephix","ercis","erix","erum","examp","exor","ezran","iad","iann","ichor","icor","ikra","ilam","ilius","imbar","imm","inba","iphis","iprax","iqor","iris","irkus","itox","iwarn","ixior","ixor","izar","obax","och","odor","odum","oirik","oldar","olim","olm","oluwa","om","ophrax","oqir","ored","orion","ortex","ourax","outor","ouzran","oxir","ozran","uard","uern","uex","uhr","ul","ulim","ulkahr","uln","ulrik","umanir","uphis","uqiat","urad","utir","utron","uweth","uxir","uxron","uyar","uzrak"];
function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd0 = Math.floor(Math.random() * nm1.length);
			names = "The " + nm1[rnd0];
		}else{
			rnd0 = Math.floor(Math.random() * nm2.length);
			rnd1 = Math.floor(Math.random() * nm3.length);
			rnd2 = Math.floor(Math.random() * nm4.length);
			names = "The " + nm2[rnd0] + nm3[rnd1] + nm4[rnd2];
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