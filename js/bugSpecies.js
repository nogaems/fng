
function nameGen(){
	var nm1 = ["Abnormal","Abrasive","Absorbtion","Abstract","Acid","Acidic","Acoustic","Actor","Adapting","Aggressive","Anchor","Ancient","Angel","Angelic","Arctic","Arid","Aromatic","Assault","Attack","Audience","Bamboo","Barren","Basin","Basking","Battle","Bell","Berserker","Betrayal","Biting","Bitter","Black","Blade","Blind","Blood","Blossom","Blue","Bold","Bomber","Bone","Bony","Boulder","Brain","Brass","Bright","Brilliant","Bronze","Bubble","Bulb","Burrowing","Bush","Butter","Button","Cacti","Candid","Cannon","Cemetery","Champion","Chaos","Chimera","Cloud","Coast","Colossal","Community","Conquerer","Corrupting","Corruption","Creeping","Crimson","Crooked","Crown","Crypt","Curved","Dancing","Dark","Darling","Death","Deceit","Defender","Defiant","Defiler","Delivery","Demonic","Diamond","Diligent","Disguise","Draconian","Dragon","Dread","Dream","Drone","Drunk","Dueling","Ebon","Echo","Electric","Emerald","Emigrating","Emigration","Enchanted","Enchanting","Entangling","Ethereal","Evasive","Exalted","Exploring","Faded","Faint","Fake","False","Familiar","Fancy","Fire","Flamboyant","Flower","Fog","Forging","Fragrant","Frigid","Furry","Fuzzy","Garden","Gardening","Gatherer","Ghost","Giant","Gilded","Glass","Gliding","Gold","Golden","Grand","Grave","Great","Green","Grim","Grooming","Guardian","Gummy","Hairy","Hammer","Harvest","Harvester","Hill","Hissing","Hollow","Humming","Hypnotic","Ice","Infernal","Iron","Ivory","Jade","Jewel","Jolly","Juvenile","Lavish","Leather","Light","Lumber","Luminous","Macabre","Majestic","Mammoth","Marble","Marked","Masked","Milk","Minor","Monster","Monstrous","Mud","Mushy","Night","Nimble","Nocturnal","Noxious","Nursing","Oceanic","Ornate","Perfumed","Phoenix","Plump","Primal","Prime","Putrid","Radiant","Rainbow","Red","Regal","Rigid","Ring","Ringed","River","Rock","Royal","Rubble","Ruby","Ruin","Sanguine","Sapphire","Scaly","Scented","Servant","Shadow","Silk","Silky","Skeletal","Skeleton","Skinny","Smiling","Smoke","Sorrow","Spiked","Spiky","Spotted","Stone","Storm","Striped","Sugar","Thicket","Throne","Tomb","Tower","Tree","Tube","Umbrella","Vagabond","Velvet","Vibrant","Volatile","Volcano","Wandering","Wax","White","Wicked"];
	var nm2 = ["Amphipod","Ant","Aphid","Arachnid","Bee","Beetle","Billbug","Borer","Bug","Bumblebee","Butterfly","Caterpillar","Centipede","Chigger","Cicada","Cockroach","Crawler","Cricket","Damselfly","Dragonfly","Earwig","Flatworm","Flea","Fly","Grasshopper","Grub","Hopper","Horntail","Katydid","Lacewing","Ladybird","Larva","Leech","Locust","Longhorn","Louse","Maggot","Mantid","Mantis","Mayfly","Millipede","Mite","Mosquito","Moth","Nepidae","Parasite","Peripatus","Pseudoscorpion","Psocid","Pupa","Scarab","Silverfish","Slater","Slug","Snail","Sowbug","Spider","Spittlebug","Springtail","Stick Insect","Stonefly","Termite","Thrip","Tick","Wasp","Weevil","Weta","Worm"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd] + " " + nm2[rnd2];
		nm1.splice(rnd, 1);
		nm2.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}