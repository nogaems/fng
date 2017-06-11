
function nameGen(type){
	var nm1 = ["Cosmos","Dimension","Domain","Dominion","Epoch","Era","Essence","Existence","Generation","Globe","History","Life","Planet","Realm","Soul","Spirit","Time","Universe","World"];
	var nm2 = ["Advancer","Adviser","Angel","Arranger","Attender","Beholder","Caretaker","Cerberus","Champion","Chaperon","Chaperone","Cherisher","Conservator","Counsel","Cradler","Curator","Custodian","Defender","Dreamer","Embracer","Empowerer","Favor","Forger","Founder","Freer","Gardener","Groomer","Grower","Guardian","Guide","Guider","Handler","Harmonizer","Healer","Hero","Immerser","Improver","Indulger","Infuser","Inspirer","Inventer","Keeper","Leader","Liberator","Lover","Manager","Matriarch","Mediater","Mentor","Motivator","Moulder","Nourisher","Nurterer","Observer","Overseer","Patriarch","Pioneer","Preserver","Promoter","Protector","Provider","Raiser","Savior","Sentinel","Sentry","Servant","Shepherd","Spirit","Stabalizer","Steward","Stimulator","Strengthener","Supporter","Tender","Treasurer","Upholder","Warden","Watcher"];
	var nm3 = ["Adored","Ancient","Angelic","Auspicious","Brave","Cherished","Courageous","Eternal","Ethereal","Exalted","Faithful","Fearless","Flawless","Gentle","Gifted","Giving","Glorious","Golden","Gracious","Grand","Hallowed","Heavenly","Infinite","Lasting","Light","Living","Lone","Majestic","Marked","Mellow","Mighty","Mysterious","Otherworldy","Primal","Prime","Pure","Radiant","Revered","Righteous","Sacred","Serene","Shrouded","Silent","Silver","Supreme","Twin","Unseen","Unsung","Utopian","Veiled","Venerated","Vigilant","Waiting","Winged"];
	var nm4 = ["the Cosmos","Dimensions","Domains","Dominions","Epochs","Eras","Essences","Existence","Generations","Globes","History","Life","Planets","the Planet","Realms","Souls","Spirits","Time","Universes","the Universe","Worlds","the World"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 3){
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			names = "The " + nm1[rnd] + " " + nm2[rnd2];
			nm2.splice(rnd2, 1);
		}else if(i < 6){
			rnd2 = Math.random() * nm2.length | 0;
			rnd = Math.random() * nm4.length | 0;
			names = nm2[rnd2] + " of " + nm4[rnd];
			nm2.splice(rnd2, 1);
		}else if(i < 8){
			rnd = Math.random() * nm3.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			names = "The " + nm3[rnd] + " " + nm2[rnd2];
			nm2.splice(rnd2, 1);
			nm3.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm3.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm1.length | 0;
			names = "The " + nm3[rnd] + " " + nm1[rnd3] + " " + nm2[rnd2];
			nm2.splice(rnd2, 1);
			nm3.splice(rnd, 1);
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