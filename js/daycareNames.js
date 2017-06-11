var nm1 = ["A Place To Grow","Above And Beyond","Alphabet Kids","Angel Academy","Apple Blossoms","Baby Steps","Beach Babies","Big Dreams","Big Hearts","Big Playhouse","Big Smiles","Blooming Kids","Bright Beginnings","Bright Eyes","Bright Future","Bright Horizons","Bright Minds","Brighter Horizons","Buds and Blooms","Building Blocks","Bumble Bees","Bundles of Joy","Busy Bees","Butterflies","Candy Cane","Caring Hearts","Caring and Sharing","Castle Gardens","Caterpillar Corner","Cheeky Monkeys","Chickadees","Children's Den","Comfort Zone","Cornerstone","Cradles of Love","Creative Care","Creative Castle","Creative Cubs","Creative Hearts","Cutie Pies","Dandelily","Dandelion","Daydreams","Do Re Mi","Dollhouse","Dragonfly","Dreamland","Duck Duck Goose","Early Learners","EduKids","Educastle","Enchanted Forest","Everyday Sunshine","Fairy Godmother","Fairytales","Family Tree","Firefly","First Steps","Fun In The Sun","Fundecational","Funny Bunnies","Funshine","Gingerbread House","Great Adventures","Growing Everyday","Growing Pains","Growing Patch","Growing Tree","Happy Days","Happy Faces","Happy Feet","Happy Hands","Happy Hearts","Happy Memories","Happy Trails","Helping Hands","Hop Scotch","Itty Bitties","Jelly Bean","Jitter Bug","Kids Castle","Kids Clubhouse","Kids Corner","Kids Garden","Kids Palace","Kids Paradise","Kidspace","Laugh and Learn","Laugh-a-lot","Leaps and Bounds","Learning Forest","Learning Ladder","Learning Tree","Lilypad","Little Adventures","Little Angels","Little Bugs","Little Cubs","Little Devils","Little Ducklings","Little Einsteins","Little Feet Big Steps","Little Giggles","Little Gumdrops","Little Hands and Feet","Little Haven","Little Journeys","Little Lambs","Little Lives","Little Lookout","Little Miracles","Little Orchids","Little Rabbits","Little Rascals","Little Rockers","Little Sprouts","Little Stars","Little Wonders","Live and Learn","Lots of Love","Love, Learn, Play","Lovebugs","Loving Arms","Loving Hands","Lullabies","Lullabies and Laughter","Lullaby Babies","Magical Moments","Making Memories","Mama Bear's","Miles of Smiles","Milk and Cookies","Mini Miracles","Mini Munchkins","Mother Goose","Mother Hen","Mother Hen's Little Chicks","Mother Land","Munchkins","New Beginnings","Nurture Zone","Once Upon A Time","Open Arms","Over the Rainbow","Owl's Nest","Peace of Mind","Piggyback Ride","Pigtails","Playful Minds","Playhouse","Precious Gems","Precious Moments","Pumpkin Patch","Rainbow","Rainbow Grove","Rainbow Kids","Rainbow Path","Rainbows and Sunshine","Raising Stars","Rascals","Reading Rainbows","Ready, Set, Go","Rising Stars","Robin's Nest","Rock-A-By Baby","Rugrats","Small World","Step by Step","Stepping Stones","Story Time","Strong Roots","Sunrise and Shine","Sunshine","Sweet Hearts","Sweet Peas","Teachable Moments","Teddy Bear","Tender Moments","The Cocoon","Tiny Blessings","Tiny Toddlers","Tiny Toes","Tiny Town","Tiny Treasures","Tippy Toes","Toddler Town","Tot Spot","Treetops","Tutor Time","Twinkle Toes","Under My Wings","Wee Care","Wee Hours","Wee Watch","Wiggles and Giggles","Wish Upon A Star","Wiz Kids","Wonder Kids","Wonderland","Young Explorers"];
var nm2 = ["Childcare","Childcare Center","Daycare","Daycare Center","Kindergarten","Nursery School","Playgroup","Pre-School"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
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