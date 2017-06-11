var nm2 = ["Animal Care Center","Animal Haven","Animal Sanctuary","Animal Shelter","Exotic Pets","Pet Care Center","Pet Haven","Pet House","Pet Land","Pet Market","Pet Shop","Pet Store","Pets"];
var nm4 = ["Animal Grooming","Pet Grooming","Grooming","Pet Parlor","Animal Parlor","Pet Salon","Animal Salon","Grooming Spa","Animal Health","Animal Care","Pet Health","Pet Care","Boutique","Animal Boutique","Pet Boutique"];
function nameGen(){
	var nm1 = ["Alley Cats","AniMall","Animal Crackers","Animal Garden","Animal House","Animal Kingdom","Balls of Fluff","Bark Avenue","Barking Lot","Beaks and Whiskers","Beast of the Best","Beastly Beauties","Beauties of the Beast","Beowuff","Best of the Beast","Besty Beasties","Big Bad Woof","Blue Collar","Bon-A-Pet-Treat","Bone Appetit","Bow Wow Meow","Cats and Critters","Central Bark","Chew Time","Citizen Canine","Clean Paws","Companions","Cosmopawliton","Creature Comforts","Critter Companions","Critter Creatures","Critters and Creatures","Critters and Litters","DeTails","Diamonds in the Ruff","Dog's Life","Doggie Do Do","Doggie Dreamland","Doggone It","Dogmatic","Don't Be a Chicken","Double Dog Dare Ya","Endless Pawsabilities","Feather Falling","Fee Fido Fo Fum","Fluffies","For Pet's Sake","Four Your Paws Only","Fresh Paws","Friendly Furs","Fur Fluff","Fur Get Me Not","Fur Real","Fur University","Fur de Leash","Fur the Herd","Fur, Feathers and Fins","Furr-eedom","Furry Family","Furry Fiesta","Furry Friends","Furry Tales","Furs and Feathers","Furtastic","Fuzzy Wuzzy","Great Tails","Green Pastures","Growls and Howls","Grr and Purr","Hairballs","Happy Feet","Happy Paws","Heads to Tails","Heavy Petting","Hop On By","Hot Diggity Dog","House of Paws","Just Four Paws","Just Pets","Licks and Kisses","Litters of Love","Little Paws","Little Whiskers","Lots of Woof","Maw and Paw","Meow or Never","Meow's the Time","Meows and Growls","Monkey Business","Muttropolian","Natural Critters","Of the Chain","On the Growl","Pampurred","Pandemonium","Paw Prints","Paw Season","Pawing Packs","Paws 'n Claws","Paws a While","Paws and Pooches","Paws for Applause","Paws for Effect","Pawsitive Attitude","Pawsitively Purfect","Pawticular Beasts","Pet Agree","Pet Paradise","Pet Peeves","Pet Project","Petacular","Petarama","Petcetera","Petopolis","Pick of the Critter","Pick of the Litter","Playing Paws","Plumes and Feathers","Pouncing Paws","Pretty Paws","Pride and Groom","Pugs and Bugs","Pup Purri","Puppy Love","Puppy Paws","Puptown Girls","Purfect Paws","Purr Usual","Raise the Woof","Release the Hounds","Right Meow","Round of Apaws","Ruff It Up","Ruff and Tumble","Salty Dog","Scales of Love","Scruffy Fluffies","Semper Fido","Snouts","Spot On","Squeakies","Squirrel!","Stay Pawsitive","Tails of the Beast","Tails of the City","The Ark","The Bark Station","The Barkery","The Cat Nap","The Fairy Dogmother","The Flock","The Happy Wag","The Hound Bar","The Leaping Frog","The Lily Pad","The Little Nest","The Naked Dog","The Nightowl","The Pack","The Paw Pack","The Pet Tree","The Tails","The Wet Nose","The Wiggle","The Woof","The Woofer","Tweeter Dee's","Urban Tails","Vanity Fur","Wag Tales","Wag Time","Waggamuffins","Wagging Tails","Wagging Welcome","Wags to Riches","Welcome Whiskers","Who's the Paws?","Wiggle Waggles","Wild Wagging","Wizard of Paws","Wuf Love","Zookeeper"];
	var nm3 = ["A Fur Affair","Bark 'n Bubbles","Barker Shop","Barking Barber","Barks 'n Recreation","Beautify the Beast","Canine Clips","Clip 'n Dip","Clip-n-Dales","Clippity Doo","Comb and Collar","Cosmopawliton","Cut Above The Rest","Cuts for Mutts","Dashing Dogs","Dazzling Dogs","Diamonds in the Ruff","Doggy Divine","Doggy Do's","Doggy Style","Dogs in Style","Fur Styling","Furtastic","Groomed to Purfection","Groomingdales","Hair of the Dog","Haute Dogs","Hot Dogs","K9 Couture","LaundroMutt","Mucky Pups","Mutley Makeover","Mutley Makeovers","Pampered Paws","Pampered Pets","Paw Spa","Paws and Relax","Pawsitively Divine","Pooch Parlor","Posh Paws","Posh Pooches","Pretty Paws","Pride and Groom","Pristine Pups","Purfect Touch","Ruff Cuts","Scrubadub Doggie","Scruffy to Fluffy","Shampooch","Shampoodles","Shear Critters","Top to Tail","Tossled Tails","Wags to Riches","Wash and Wag","Yuppy Puppy"];
	var br = "";

	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 7){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + " - " + nm2[rnd2];
			nm1.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			rnd2 = Math.floor(Math.random() * nm4.length);
			names = nm3[rnd] + " - " + nm4[rnd2];
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