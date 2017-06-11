var nm2 = ["Centre","Centre","Center","Center","Exhibition","Gallery","Gallery","Hall","Hall","Institute","Institution","Museum","Museum","Museum","Treasury","Vault"];
var nm3 = ["National","International","Grand","Great","Central","Royal","","","","","","","","","","","","","",""];
function nameGen(){
	var nm1 = ["Accident","Aerial","Aerospace","Amphibian","Analysis","Anatomy","Ancestry","Anthropology","Apparatus","Aquatic","Archaeology","Architecture","Art","Artillery","Astronomy","Audiovisual","Auditory","Blossoms","Carnival","Changing","Childhood","Children","Chrono","Cryonic","Circus","Contemporary","Cooking","Costume","Creativity","Cryptology","Crystal","Cultural","Culture","Curiosity","Dance","Darkness","Data","Decorative","Design","Digital","Dinosaur","Disaster","Discovery","Dream","Dynamics","Earth","Electric","Emergency","Estate","Eternity","Expedition","Experiment","Experimentation","Exploration","Explorers","Fame","Fantasy","Fashion","Fear","Fiction","Film","Fire","Firepower","Forest","Fortune","Frost","Future","Gadget","Galaxy","Game","Garden","Genius","Gift","Gizmo","Glass","Globe","Gold","Guardian","Happiness","Harmony","Hazard","Heritage","History","Hope","Horror","Illusion","Imagination","Immersion","Infinity","Ingenuity","Inheritance","Innovation","Insect","Inspiration","Instrument","Invention","Jewel","Kinetics","Language","Learning","Legacy","Liberty","Light","Literature","Living","Locomotion","Love","Lunar","Machine","Magic","Magnetic","Manor","Manuscript","Maritime","Master","Mechanical","Medical","Micro","Mind","Mineral","Mistake","Movement","Music","Musical","Natural","Nature","Neurological","Night","Nightingale","Nightmare","Novelty","Open","Optical","Origin","Origins","Party","Passage","Passion","People","Perception","Pet","Petrified","Pinnacle","Play","Portrait","Prediction","Puppet","Pyro","Reconnaissance","Religion","Reptile","Research","Revelation","Rush","Sail","Science","Science Fiction","Secrets","Sensory","Serpent","Sight","Sightings","Silent","Skeleton","Snow","Solar","Space","Speech","Spinning","Sports","Stimulation","Submarine","Submerged","Sugar","Summer","Surprise","Tactile","Taste","Testing","Theater","Time","Toy","Tradition","Tragedy","Transport","Travel","Treasure","Trinket","Underground","Universe","Video","Virtual","Virtuoso","Visual","War","Water","Weirdness","Wild","Wind","Winter","Youth","Zoology"];
	var nm4 = ["Accidents","Aerial Technology","Aerospace","Amphibians","Analysis","Anatomy","Ancestry","Anthropology","Aquatic Life","Archaeology","Architecture","Art","Artillery","Astronomy","Audio","Audiovisual Arts","Blossoms","Carnivals","Change","Childhood","Children","Cryonic Technology","Circuses","Contemporary Arts","Cooking","Costumes","Creativity","Cryptology","Crystals","Cultural History","Culture","Curiosity","Dance","Darkness","Data","Decoration","Design","Digital Arts","Dinosaurs","Disaster","Discovery","Dreams","Dynamics","Earth","Electricity","Emergencies","Eternity","Expeditions","Experimentations","Experiments","Exploration","Explorers","Fame","Fantasy","Fashion","Fear","Fiction","Film","Fire","Firepower","Forests","Fortune","Frost","Gadgets","Games","Gardens","Geniuses","Gifts","Gizmos","Glass","Gold","Guardians","Happiness","Harmony","Hazards","Heritage","History","Hope","Horrors","Illusions","Imagination","Immersion","Infinity","Ingenuity","Inheritance","Innovation","Insects","Inspiration","Instruments","Inventions","Jewels","Kinetics","Language","Learning","Legacies","Liberty","Light","Literature","Living","Locomotion","Love","Lunar History","Machines","Magic","Magnetics","Manors","Manuscripts","Maritime History","Masters","Mechanics","Medicine","Micro Life","Minerals","Mistakes","Movement","Music","Musicals","Natural History","Nature","Neurological Science","Nightmares","Novelties","Openness","Optical Illusions","Origins","Parties","Passages","Passion","People","Perception","Petrification","Pets","Pinnacles","Play","Portraits","Predictions","Puppets","Pyromania","Reconnaissance","Religion","Reptiles","Research","Revelations","Rush Hours","Sailing","Science","Science Fiction","Secrets","Sensory Science","Serpents","Sight","Sightings","Silence","Skeletons","Snow","Solar History","Space","Speech","Sports","Stimulation","Submarines","Submersion","Sugar","Summer","Surprises","Tactics","Taste","Testing","Theater","Time","Toys","Traditions","Tragedy","Transport","Travel","Treasures","Trinkets","Video","Virtual Reality","Visual Arts","War","Water","Weirdness","Wind","Winter","Youth","Zoology","the Future","the Galaxy","the Globe","the Mind","the Night","the Nightingale","the Underground","the Universe","the Wild"];
	var br = "";

	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		if(i < 5){
			rnd = Math.floor(Math.random() * nm4.length);
			names = nm3[rnd3] + " " + nm2[rnd2] + " of " + nm4[rnd];
			nm4.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm3[rnd3] + " " + nm1[rnd] + " " + nm2[rnd2];
			nm1.splice(rnd, 1);
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