var nm1 = ["Abysmal","Abyss","Adamantine","Albatros","Altar","Anchor","Ancient","Angry","Arching","Arctic","Arid","Asylum","Autumn","Bare","Barnacle","Barracuda","Barren","Black","Bland","Bleak","Blue","Boiling","Boisterous","Bone-Dry","Bottomless","Boundless","Brilliant","Bronze","Burned","Burning","Bursting","Calm","Calmest","Castaway","Charmed","Chasm","Cheering","Cheerless","Choral","Clam","Climbing","Clownfish","Cobalt","Cold","Collapsing","Colossal","Conquest","Coral","Crab","Crying","Crystal","Cunning","Cursed","Dancing","Dangerous","Dark","Darkest","Dead","Decayed","Decaying","Deep","Defeated","Dense","Depraved","Deserted","Desolate","Desolated","Diamond","Distant","Dolphin","Domination","Dominion","Dread","Dreaded","Dreadful","Dreary","Dry","Eastern","Ebony","Emerald","Empty","Enchanted","Enormous","Eroded","Ethereal","Ever Reaching","Everlasting","Fabled","Fair","Fall","Faraway","Farthest","Feared","Fearsome","Fiery","Flamingo","Flat","Floating","Flowing","Forbidden","Forested","Fountain","Fractured","Frightening","Frozen","Garden","Gargantuan","Ghost","Giant","Gigantic","Glassy","Gleaming","Glistening","Gloomy","Glowing","Gold","Golden","Grave","Gray","Green","Seagull","Grim","Gulf","Harmonious","Haunted","Heartless","Heaving","Hellish","Hissing","Hollow","Homeless","Hopeless","Hot","Howling","Huge","Humongous","Hungry","Immense","Infernal","Infinite","Invisible","Inviting","Iron","Isolated","Ivory","Jade","Jagged","Jellyfish","Killing","Lagoon","Laughing","Lifeless","Light","Lightest","Living","Lobster","Lonely","Lost","Lucent","Majestic","Malevolent","Malicious","Mammoth","Manta","Maroon","Mesmerizing","Mighty","Mirrored","Misty","Moaning","Molten","Monster","Monstrous","Moonlit","Mumbling","Mysterious","Naked","Narrow","Neglected","Neverending","New","Northern","Oasis","Octopus","Open","Oriental","Outcast","Oyster","Oyster Bay","Pain","Peaceful","Pearl","Pelican","Penguin","Perfume","Perfumed","Phantom","Piranha","Plain","Pleasant","Poseidon","Primeval","Pristine","Pufferfish","Pure","Quiet","Raging","Rain","Rainy","Ray","Red","Relentless","Remote","Renegade","Resort","Restless","Rippling","Roaring","Rocking","Rocky","Rolling","Rough","Rugged","Rushing","Sad","Sanctuary","Sanctum","Sandy","Sanguine","Savage","Scarlet","Scorching","Scuba","Seal","Seashell","Secret","Serene","Severed","Shadow","Shadowed","Shadowy","Shark","Sharktooth","Paradise","Skeleton","Seagrass","Heavenly","Shaking","Sharp-peaked","Shimmering","Shipwreck","Shouting","Shrimp","Shrine","Silent","Silver","Sleeping","Slumbering","Smoking","Snowy","Soundless","Southern","Spacious","Sparkling","Spring","Squid","Starfish","Steep","Sterile","Stern","Stingray","Storm","Storming","Stormy","Straitened","Summer","Sunny","Surging","Symmetrical","Teal","Temple","Terraced","Throbbing","Thundering","Tideless","Torpedo","Tossing","Towering","Tranquil","Treacherous","Triumphant","Tropic","Troubled","Turbulent","Turquoise","Turtle","Twisting","Ugly","Ultramarine","Uncanny","Unfathomed","Unknown","Unscaled","Unstable","Unwelcoming","Vast","Vanishing","Veiled","Vicious","Victory","Violent","Virgin","Voiceless","Volcanic","Walled","Walrus","Wasted","Wasteful","Wasting","Waterless","Waveless","Welcoming","Western","Whale","Whispering","White","Wild","Windless","Windy","Winter","Wintry","Withered","Wondering","Yearning","Yelling","Yellow"];
var nm2 = ["Ait","Archipelago","Atoll","Cay","Chain","Enclave","Haven","Holm","Island","Islands","Isle","Isles","Islet","Key","Peninsula","Reef","Refuge","Skerry"];
var nm3 = ["b","br","bl","c","cl","cr","d","dr","f","fr","fl","g","gr","gl","gn","h","j","k","kr","kl","kn","m","n","p","pr","pl","q","qr","ql","r","s","st","sr","str","sl","t","tr","tl","v","vl","vr","w","wr","x","z","","","","",""];
var nm4 = ["a","e","i","o","u","y"];
var nm5 = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z","","","","","",""];
var nm6 = ["a","e","i","o","u","y"];
var nm7 = ["b","d","g","gh","h","hr","hs","ht","hst","hsh","hn","hm","hl","hz","hx","hq","k","ks","kx","l","ll","lk","ln","lm","lz","lp","lt","ls","lst","lf","m","mn","mm","mt","ms","n","nn","nt","ns","p","ps","pt","ph","q","r","rs","rt","rst","rq","rk","rc","rf","rb","rd","s","st","ss","sh","sk","sp","t","th","ts","w","wth","x","z"];
var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm2.length);
		if(i < 4){
			rnd = Math.floor(Math.random() * nm1.length);
			names = "The " + nm1[rnd] + " " + nm2[rnd2];
		}else if(i < 7){
			rnd = Math.floor(Math.random() * nm3.length);
			rnd2 = Math.floor(Math.random() * nm4.length);
			rnd3 = Math.floor(Math.random() * nm7.length);
			names = nm3[rnd] + nm4[rnd2] + nm7[rnd3] + " " + nm2[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			rnd2 = Math.floor(Math.random() * nm4.length);
			rnd3 = Math.floor(Math.random() * nm5.length);
			rnd4 = Math.floor(Math.random() * nm6.length);
			rnd5 = Math.floor(Math.random() * nm7.length);
			names = nm3[rnd] + nm4[rnd2] + nm5[rnd3] + nm6[rnd4] + nm7[rnd5] + " " + nm2[rnd2];
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