var nm2 = ["Chronicle","Daily","Digest","Focus","Gazette","Guide","Illustrated","Journal","Life","Magazine","Monthly","Monthly Magazine","Report","Reports","Review","Times","Today","Week","Weekly","Weekly Magazine","Magazine","Magazine"];

function nameGen(type){
	var nm1 = ["A Cappella","Academy","Acoustic","Advisor","Affairs","Alliance","Ambience","Analysis","Analyze","Angle","Animal","Apex","Applause","Appraisal","Architecture","Artist","Artistry","Assessment","Audio","Bargain","Beast","Bite Bits","Blueprint","Board","Boost","Boyfriend","Brain","Brainstorm","Breaking","Breakthrough","Business","Carnival","Case Study","Champion","Chance","Chic","Chief","Cinema","Coalition","Color","Comedian","Comedy","Comic","Communication","Connection","Constitution","Consumer","Context","Contract","Convention","Cookery","Cooking","Cosmos","Countdown","Craft","Craze","Crazy","Creation","Creative","Creativity","Critique","Cuddle","Cuisine","Culture","Custom","DIY","Darling","Data","Daydream","Dear","Debate","Design","Destiny","Destruction","Development","Diagnosis","Discovery","Divine","Doodle","Dragon","Dream","Earth","Eat","Edict","Egghead","Electronic","Electronics","Emotion","Engineering","Enterprise","Entertainment","Entrepreneur","Essence","Eternity","Etiquette","Euphoria","Evaluation","Examination","Executive","Expertise","Exposition","Fad","Fan","Fanatic","Fantasy","Fashion","Fate","Festival","Fiesta","Figure","Film","Finance","Fitness","Flick","Flux","Food","Foodstuff","Form","Fortune","Foundation","Fun","Fun Fest","Fun and Games","Fusion","Future","Gala","Game","Game On","Garden","Girlfriend","Globe","Grin","Growth","Harmony","Hazard","Health","Heart","Hero","Highbrow","Highlight","Holy","Home","Home Improvement","Illusion","Imagination","Imagine","Improv","Industry","Infinity","Innovation","Inquiry","Insight","Inspection","Inspiration","Inspire","Instrument","Intelligence","Invention","Investment","Jazz","Jester","Joker","Jubilee","Kiss","Landscape","Laugh","Life Style","Lime Light","Living","Love","Luck","Lumination","Lustrous","Magic","Make Up","Management","Manager","Mansion","Mastermind","Meal Time","Mech","Mecha","Mechanical","Meditation","Melody","Metal","Mind","Minor","Mode","Model","Modern","Monster","Motion","Muse","Music","Mystery","Myth","Mythic","Nature","Numbers","Nutrition","Observer","Opera","Oracle","Outlook","Ovation","Paint","Painting","Panorama","Parade","Paradox","Paramour","Partner","Partnership","Passion","Pastel","Pastry","Peace","Perspective","Pet","Photography","Physique","Picture","Pinnacle","Pleasure","Portrait","Power","Print","Prodigy","Progress","Prospect","Quiz","Ragtime","Reality","Realm","Reflection","Relax","Relaxation","Repair","Research","Resource","Revelation","Review","Riches","Rise","Satire","Scholar","Scope","Search","Sense","Sentience","Sketch","Smile","Snack","Snapshot","Solitude","Soul","Sound","Space","Sport","Spotlight","Stage","Stand-Up","Status","Strength","Study","Survey","Survival","Sweet","Sweetheart","Swing","Tattoo","Teen","Theater","Titans","Tone","Trance","Tranquility","Transfer","Treatment","Trend","Trending","Truelove","Turbine","Valuation","Value","Vertex","View","Viewpoint","Vision","Vista","Vitality","Vogue","Wealth","Web","Wheeler","Wheels","Wild","Wildlife","Word","World","Youth"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		nm1.splice(rnd, 1);
		names = nm1[rnd] + " " + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}