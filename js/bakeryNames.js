function nameGen(){
	var nm1 = ["Ahead of Bread","Awake & Bake","Babycakes","Bake Awake","Baked","Baked Bites","Bakers Delight","Balance of Flour","Batter Spatter","Best Thing Since Sliced Bread","Blends of Flour","Blissful Bites","Born and Bread","Bottom of the Flour","Bread & Butter","Bread Ahead","Bread and Batter","Bread and Custards","Bread and Peanut Butter","Breadline","Breadsmith","Break Bread","Budding Tastes","Bun Boutique","Buns in the Oven","Buns of Steel","Cake Bakes","Cake Break","Cake Couture","Cake Outbreak","Cake Zone","Cake a Diem","Cake's Sake","Cake's at Stake","Cake-A-Licious","Cakes and Ale","Cakewalk","Cakewalkers","Cakey Bakey","Chateau Dough","Cocoa Nutter","Coffee Break 'n Cake","Commandough","Common Scents","Cookie-Clutter","Cookie-Cutter","Cookoo for Cookies","Creamy Creations","Creative Treats","Crumbs","Crumbs and Bites","Crunchy Crumbles","Cups and Cakes","Cut the Cake","Dough Business","Dough Re Mi","Dough must go on","Dough of Hands","Doughing Pains","Doughy Delights","Dripping Drizzles","Emergency Cake","Finest Flour","Flour Down","Flour Girl","Flour Leaves","Flour Meadough","Flour Play","Flour Power","Flour Up","Flours for Hours","Fondante's Inferno","For Flours on End","For Goodness Cakes","Fresh from the Oven","Ginger Snapped","Give and Cake","Glazed and Glorious","Gluteus Maximus","Gluteus Minimus","Glutton for Punishment","Grains of Scents","Great Buns","Happy Flour","Have Your Cake & Eat It","Hearts and Flours","Hot Buns","Hour of the Bread","Icing on the Cake","Irresistible Indulgence","Ivory Flour","Knead Bread?","Knead for Sweets","Knead to Know","Let Them Eat Cake","Loaf Oaf","Love Flour","Love of Loaves","Luscious Layers","Lush & Luscious","Lust for Flour","Mad Batters","Makes Scents","Mayflour","Monster Cookies","More Flour to You","Muffin Top","Naturally Delicious","One-Man Dough","Oven Lovin'","Path of Crumbs","Piece of Cake","Piece of the Pie","Premier Cakes","Prime Dough","Quakey Cakeys","Raisin Dough","Rise of the Buns","Risk it for a Biscuit","Rolling Scones","Scents Time Immemorial","Scents of Humor","Sensational Goodies","Sifted Gifts","Sinful Temptations","Sixth Scents","Slow Dough","Smell the Flours","Snack Rack","Snack Shack","Snackamuffins","Sprinkles of Joy","Status Dough","Steal the Dough","Sugar Beat","Sugar Bliss","Sweet Beat","Sweet Cakes","Sweet Cheeks","Sweet Dreams","Sweet Sensations","Sweetie Pies","Sweets and Such","Swirls and Pearls","Take the Cake","Takes the Cake","Taste of Heaven","The Cake is a Pie","The Confection Connection","The Cookie Cook","The Cookie Rookie","The Cooling Rack","The Dough Below","The Dough Flow","The Flour Tower","The Fruitcake","The Glaze Maze","The Glaze Phase","The Grateful Bread","The Mistledough","The Pastry Corner","The Pastry Sheet","The Secret Ingredient","The Shadough","The Sweet Spot","The Torpedough","There's Nothing Batter","Those Buns Dough","Tiers of Delight","Tiers of Joy","Tokens of my Confection","Top of the Flour","Top of the Muffin","Torte Reform","Tough Cookies","Tout de Sweet","Up the Cakes","Wakey Bakey","Wallflour","We Knead Dough","We Take the Cake","Wee Flours","Whisk it for a Biscuit","Whoopie Cakes","Witching Flours","You Take the Cake"];
	var br = "";

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