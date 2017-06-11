var nm1 = ["Agnes","Alfie","Allie","Amber","Amy","Anabell","Angel","Angela","Angie","Apache","Archie","Aurora","Autumn","Awall","Baby","Bailey","Baldrick","Basil","Beans","Beauty","Bell","Belle","Benny","Bernie","Beryl","Betty","BettyButton","BigTrudie","Blackberry","Blake","Blanche","Blondie","Boingo","Bonnie","Bonnie","Boomer","Boots","Botticelli","Brownie","Buckmeister","Buddy","Bugsy","Bumble","Buster","Capricorn","Capricorny","Chad","ChewChew","Chief","Chloe","Cinderella","Cinnamon","Cisco","Clover","Clyde","Cocoa","CoffeeBean","Colleen","Comet","Cookie","Cornbread","Cornelious","Cosmo","CottonBall","CottonTail","Creole","Daffodil","Daisy","Daisy","Dana","Dash","Delilah","Diamond","Dinner","Doc","Doe","Dottie","Duke","DumDum","Duncan","Ella","Fancy","Fern","Garfunkle","Gary","Gladys","Gladys","Gloria","Grace","Gunther","Gypsy","Hailey","Haley","Halle","Harvey","Heidi","Hemingway","Holly","Hoover","Hornless","Houdini","Hudson","Hyacinth","Isabell","Isabelle","Ivy","Jeremy","Jessie","Julius","July","Kaytee","Kebab","Kebob","Kisses","Lady","Lancelot","Lane","Legend","Lena","Lily","Lucky","Lucky","Lucy","Lybris","Lydia","Lynn","MaeFlower","Maggie","MaggieMay","Mandy","Manny","Marisa","Marshall","Martini","Mary","Matilda","Maybell","Mercury","Meridian","Midnight","Milkshake","Milky","Mimi","Miracle","Missy","Mocha","Molly","Molly","Montana","Montgomery","Moose","Morty","MrBongo","Nanna","Nellie","Nibbler","Nibler","Niblets","Noelle","Nova","Omega","Oreo","Orion","Osiris","Pansy","Patches","Peaches","Pearl","Peepers","Penelope","Penny","Peony","Pepper","Pepper","Petticoat","Pettigoat","Petunia","Petunia","Pierre","Poppy","Prancer","Precious","Princess","Promise","Pumpkin","Rack","Ramses","Ramzy","Remington","Riley","Ringo","Rodney","Rosa","Rose","Rowdy","Rufus","Russell","Rusty","Sable","Sabrina","Sage","Salem","Samantha","Sammy","Sandy","Sandy","Saphire","Sassafras","Scruffy","Shack","Shadow","Shaggy","Shane","Sierra","Simon","Skittles","Skooter","Smokey","Smoky","Snickers","Snowball","Snowwhite","Socks","Socks","Sonny","Sophie","Spanky","Spartacus","Spice","Spicey","Spirit","Spot","Stevie","Strawberry","Suleyman","Summer","Sunstar","Surya","Susie","Swiper","Tabitha","Tanya","Tapioca","Tasha","Tavia","Taz","Teeny","Tex","Thunder","Tinkerbelle","TinyDancer","Tonya","Topaz","Trixie","Trouble","Truffles","Tulip","Tullie","Twiggy","Twinkle","Twister","Tyler","Tyrone","Valentine","Velvet","Veronica","Victoria","Violet","Walden","Walnut","Weeny","Willie","Winter","Wizzer","Wonder","Yerba","Zeus","Ziggy","Zoe","Zuku","Zylonna"];
var nm2 = ["AlfredHedgehog","AlphaHog","Aquila","Aramis","Archie","Bandit","Bean","Bell","Bill","Biscuit","Boarcupine","Bob","Boris","Brillo","BruceQuillis","Bruno","Bubbles","Caboodles","CactusJack","CaptainPrickard","Carlzander","Casper","Chad","Chester","ChuckNorris","Cinderquilla","Comet","CpnPrickard","Cyndaquill","Daggett","DavidHasselhog","DrQuillis","Ducks","EinSpine","Fernando","Flower","Fluffy","Frodo","Gabby","Genie","Gizmo","Grover","Harley","Harvey","Hayden","Hazel","HeathHedger","Hedgebert","Hedgehawg","Herbert","Hissyfit","HodgePodge","HogEatHog","Hogarth","Hokey","HokeyPokey","Isabella","Jacque","Journey","Kahlua","Kako","KatnissEverhog","Kenya","KillQuill","Kisses","Kit","Knarla","Lance","Lancelot","Liberty","LittleDipper","Luna","MaiseQuilliams","Maliha","MarkHamquill","Marshmallow","Marvin","McPricklesworth","Moxie","MrCactus","MrPrickles","MrPriclesworth","Muffy","Natasha","Needle","Needles","Norbert","Obie","Oscar","Pablo","Peanut","Penelope","Penny","Perry","Pinecone","Pinhead","Pointer","Poke","PokeRface","Pokey","Poky","Porcu","Porcupest","Porcupowned","Porki","Porkies","Porky","PrickAstley","Prickly","PrickyGervais","PrickyMartin","PrinceQuilliam","Priscilla","Punky","Q-Tip","Quilbert","Quilfrid","Quill.I.Am","QuillClinton","QuillFerrel","QuillMurray","QuillNighy","QuillRyker","QuillSmith","QuillWheaton","QuillYoung","QuillemDafoe","Quillen","Quilliam","QuilliamShatner","QuillieNelson","Quillow","QuillyWonka","Quinn","Rico","RobbieQuilliams","RobinQuilliams","Romeo","Sam","Shredder","Skeezix","SnoopHoggyHog","Snuggles","Sonar","Spike","SpikeBeaver","Spikey","Splinter","StickWithMe","StickyPig","Thiery","TomBombaquill","Tuffnel","Tumble","WinstonChurchquill"];

function nameGen(type){
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd];
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