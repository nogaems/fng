var names1 = ["Ancient","Antique","Bad","Big","Black","Blonde","Cinnamon","Cocao","Cool","Daily","Dark","Delish","Divine","Ebony","Fatty","Featherly","Firefly","Flaming","Fluffy","Flying","Frozen","Funky","Gecko","Generous","Gentle","Ginger","Green","Handy","Happy","Hard","Harmony","Hava","Havana","Hazel","Hazelnut","Hidden","Homey","Hospitable","Hot","Incredible","Indulging","Ivory","Jasmine","Jazz","Jolly","Last","Light","Little","Little Big","Mad","Marble","Mellow","Melting","Merry","Midnight","Mini","Misty","Natural","New","Noble","Nutty","Oceanic","Old","Olive","Palm","Panama","Paragon","Peaceful","Pleasant","Pleasure","Precious","Quiet","Rainforest","Rapid","Regular","Rich","Salty","Sandy","Secret","Silent","Silk","Smooth","Soft","Strange","Sunny","Sweet","Swift","Tasty","Timeless","Tranquil","Twinkling","Unique","Universal","Unusual","Urban","Vanilla","Welcoming","Wet","Whispering","White"];
var names2 = ["Baker","Balcony","Beach","Bean","Beans","Bites","Bliss","Blossom","Blue","Boulder","Break","Breeze","Brew","Brews","Cabin","Chocolate","Cook","Cottage","Crumble","Crumbs","Cup","Deli","Delight","Delights","Distraction","Drinks","Drop","Earth","Echo","Eden","Enigma","Express","Fest","Festival","Flower","Forest","Fountain","Fruits","Gallery","Garden","Gardens","Glee","Grind","Groove","Harvest","Hat","Hatter","Haven","Heaven","Ingredients","Interlude","Java","Joy","Leaf","Lodge","Lounge","Magnolia","Marina","Mirror","Monocle","Moon","Nibble","Oasis","Panini","Patio","Pearl","Petal","Picnic","Planet","Plaza","Puzzle","Question","Questions","Rest","Retreat","Rock","Rose","Satisfaction","Shack","Shrine","Sip","Snack","Spring","Station","Tales","Teapot","Tease","Temptation","Temptations","Terrace","Time","Tower","Treasure","Treasures","Treat","Treats","Tulip","Utopia","Waterfall","Waters","Waves"];
var names3 = ["Cafe","Tearoom","Bistro","Barista","Coffee","Room","Coffee Shop","Joint","Lunchroom","Coffee Bar","Cafeteria","Cafe","Cafe","Diner","Espresso Bar"];
var names4 = ["Bacon & Eggs","Bean & Gone","Bean Bag","Bean Drinking","Bean Me Up","Bean There","Beans & Barley","Big Mugs","Bizz Buzz","Bread & Butter","Brew & Chew","Brew Crew","Brew Ha Ha","Brew for You","Brewed Awakening","Busy Bean","Cocoa Connection","Come & Go","Common Grounds","Cool Beans","Daily Grind","Ding Dong","Drive Brew","Early Rise","Eats & Treats","Espresso Lane","Express-O","Fire & Ice","Fresh Roast","Go & Get It","Grind House","Grinders","Ground Up","Hallowed Grounds","Havana Java","Here & There","High & Mighty","Hot & Cold","Hot & Steamy","Hot Shots","Impresso Espresso","In & Out","Incredible Edibles","Java Junction","Java Nice Day","Java the Hut","Javawocky","Joe & Go","Jumping Bean","Jumpstart","Knock On Wood","Last Drop","Late Latte","Lava Java","Lemon & Lime","Lettuce Retreat","Liquid Heaven","Moment of Peace","Mug Shot","Naughty & Nice","Near & Far","Needle & Thread","Peaches & Cream","Pestle & Mortar","Q & A","Quick & Easy","Rest & Relaxation","Rise & Grind","Rise & Shine","Roasted Bean","Roasters","Salt & Pepper","See You Latte","Short & Steamy","Silky & Smooth","Slice of Life","Splitting Beans","Steamy Bean","Steamy Indulgences","Sugar & Spice","Sweet & Savory","Tall, Dark and Coffee","Tea Time","Thanks a Latte","Thinking Cup","This & That","Tongue & Cheek","Trembling Cup","Tutty Fruity","Urban Grind","Vice & Virtue","Wake Up","Wakey Wakey","Whole Latte Love","Wide Awake","Yin & Yang","Yours & Mine","Yum Yum","Yummy Tummy","Zig Zag"];

function nameGen(){
	
	var names = [];
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd0 = Math.floor(Math.random() * names4.length);
			rnd1 = Math.floor(Math.random() * names3.length);
			names[i] = names4[rnd0] + " " + names3[rnd1];
		}else{
			rnd0 = Math.floor(Math.random() * names1.length);
			rnd1 = Math.floor(Math.random() * names2.length);
			rnd2 = Math.floor(Math.random() * names3.length);
			names[i] = names1[rnd0] + " " + names2[rnd1] + " " + names3[rnd2];
		}
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names[i]));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}