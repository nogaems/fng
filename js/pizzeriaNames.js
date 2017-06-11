
function nameGen(){
	var nm1 = ["The All Around","The Bake 'n Take","The Balance of Flour","The Basil 'n Peel","The Belle Pepper","The Bits and Pizzas","The Black Olive","Chateau Dough","The Cheese Base","The Cheese Connection","Cheese Louise","The Cheese Piece","Cheese and Kisses","Cheesus","Cheesus Crust","The Clay Oven","The Commandough","The Conversation Pizza","The Corner Grill","Cravings","Crazy Dough","The Crispy Crust","Crust Lust","Cut the Cheese","The Deep Dish","The Dough Bro","Dough Business","The Dough Must Go On","Dough Nuts","Dough Oh","Dough Re Mi","Dough of Hands","The Doughbie Brothers","The Doughfather","The Doughfellas","Doughy Delights","Feeling Saucy","The Flippin'","Flour Girl","Flour Power","Flour Up","Flour to You","For Pizza's Sake","From Top to Dough","From Topping to Dough","The Full Moon","The Funky Anchovy","Get to the Toppings","The Gluteus Maximus","The Gluteus Minimus","The Happy Flour","The Home Slice","The Hot Oven","The Hot Spot","The Hot Stone","Il Tricolore","In One Pizza","Knead Pizza","Knead to Know","Luscious Layers","The Lust for Crust","Master Pieces","The Meadough","Molten Delights","Napoli","Oh Cheese","The Olive","The Olive Branch","On Toppings","Onomotopizza","Oven Baked","The Oven and Shaker","Over the Toppings","Papa Pizza","Pepperoni's","Pi Pie","Pieology","The Pizza Bro","Pizza Cake","The Pizza Connection","Pizza Me","Pizza Mind","Pizza My Heart","Pizza Pals","Pizza Pan","Pizza Paradise","Pizza Squared","Pizza Together","Pizza Work","The Pizza de Resistance","Pizza di Mama","Pizza the Action","The Pizzageddon","The Pizzasmith","Pizzazz","Pizzazza","The Pizzone","The Prime","The Prime Dough","Rest 'n Pizza","Rise to the Toppings","Rolling in Dough","The Round Table","Rounded Down","The Sassy Sauce","Say Cheese","Slice of Heaven","Slice of Italy","Slice of Life","The Stone Hot","Stuffed","Sweet Sensations","That Cheese Dough","That's Amore","The Tomato Base","The Tomato Pie","The Top Slice","The Topspin","The Tri-Slice","The Upper Crust","We Knead","The Pizzazy","The Pizzander","The Pizzaffar","The Pizzamarra","The Pizzaga","The Pizza Saga","Pizz'ahoy","The Pizzamba","The Pizzanity","The Pizzavant","The Scampizza","The Octopizza","The Papizza","The Tipizza"];
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		names = nm1[rnd] + " Pizzeria";
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