
function nameGen(type){
	var nm1 = ["Alligator","Amida","Ammit","Amun","Ape","Arachnid","Arbal","Ash","Asseg","Asvin","Atl","Ax","Babi","Baboon","Badger","Ballis","Barong","Bayo","Bayonit","Bazoo","Bear","Beast","Bicks","Blade","Blight","Blits","Blyght","Brant","Brawl","Bruizer","Brutus","Buck","Buster","Butcher","Bynd","Cage","Cane","Cano","Carkas","Carn","Carpse","Carris","Carse","Carver","Cast","Cloud","Cobra","Combe","Coyote","Crane","Croc","Cudge","Cyn","Cynder","Cypher","Dagg","Darum","Dash","Daver","Davi","Dino","Draco","Draegon","Dragon","Dragonfly","Drake","Dynamo","Ebis","Enigma","Exxec","Falcon","Ferno","Fiend","Flame","Frag","Fume","Glive","Gorilla","Grave","Gritt","Grym","Gryme","Guillo","Hale","Haros","Hawk","Helia","Hippo","Hitt","Howitz","Ibis","Imp","Izana","Jackal","Jag","Kagu","Kame","Kangiten","Kannon","Komodo","Kriz","Kublai","Laki","Lance","Leech","Luce","Machet","Magnum","Magnus","Malyc","Mammoth","Manta","Mantis","Marat","Massac","Merce","Mercer","Mise","Mongoose","Mort","Necros","Nide","Nightingale","Nightowl","Nuke","Nunchu","Oblivion","Obsidian","Onyx","Oracle","Osir","Panther","Pest","Phoenix","Pulse","Pyre","Quake","Quaz","Queen Bee","Quelz","Quiv","Rackas","Radic","Raijin","Raptor","Rath","Rattle","Raze","Razor","Reaper","Rex","Rhino","Riot","Rudas","Ruzh","Ryze","Sabe","Sabre","Samit","Scarch","Scarn","Scatter","Scimi","Scourge","Scrimm","Scythe","Sekh","Semet","Serpent","Shav","Shiver","Silen","Siris","Skelt","Skirm","Skiv","Skiver","Slate","Slayer","Sliver","Slyce","Snyde","Soot","Spike","Splinter","Spyte","Stal","Stark","Storm","Surge","Sybre","Sylver","Tank","Tenac","Tiger","Torm","Torren","Tugs","Vapor","Viger","Vissu","Visus","Weasel","Wildcat","Wolf","Wolverine","Wrangler","Xerox","Yce","Zizor","Zyn"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd];
		nm1.splice(rnd, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}