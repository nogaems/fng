var nm1 = ["Angel","Angel Eyes","Angelface","Babe","Babes","Baboo","Baby","Baby Bear","Baby Bird","Baby Boo","Baby Cakes","Baby Girl","Babydoll","Big Kitty","Biscuit","Blossom","Bonbon","Boo Bear","Booboo","Bright Eyes","Bubba","Bubbies","Bubbles","Bunbun","Bunny","Buttercup","Buttons","Cacao","Cakes","Candy","Cheesecake","Cherry Blossom","Cherry Pie","Chipmunk","Chocolate","Cinnamon","Cocoa","Cookie","Cuddle Bear","Cuddle Muffin","Cuddlebug","Cuddles","Cupcake","Cupid","Cuppy Cake","Cuteness","Cutie","Cutie Patootie","Cutie Pie","Darlin'","Darling","Darlington","Dashing","Dear","Dearheart","Deary","Dewdrop","Dimples","Donut","Doodle","Dove","Dreambuns","Dreamlove","Duckling","Ducky","Dummy","Dumpling","Everything","Flower","Fluffkin","Flufs","Fruit Cake","Fruit Loop","Funny Bunny","Giggles","Goofball","Gorgeous","Gumdrop","Handsome","Happiness","Hon","Hon' Bun","Honey","Honey Bear","Honey Bee","Honey Bunny","Honey Buns","Honey Pie","Honey Pot","Hot Cakes","Hot Honey","Hot Stuff","Hottie","Hubby Wubby","Huggy Bear","Jelly Bean","Joy","Kissy Face","Kit Kat","Kitten","Kittycat","Lemon Drop","Lemonpie","Little Dove","Love","Love Bug","Love Nugget","Lovebird","Loveylove","Lovie","Lucky Charm","Magic","Marshmallow","Melody","Mooky","Muffin","Muggles","Munchkin","Muppet","My Dear","My Everything","My World","Nugget","Numnums","Pancake","Pandabear","Paradise","Passion Fruit","Peach","Peach Blossom","Peachy Pie","Peanut","Petal","Pookums","Porkchop","Precious","Puddin'","Pumpkin'","Puppy","Pussycat","Rubber Ducky","Schmooky","Scrumptious","Shmoops","Short Cake","Silly Goose","Smiles","Smooch","Smoochie","Smoochie Poo","Snickerdoodle","Snoogypuss","Snookie","Snookums","Snow Pea","Snowflake","Snuggems","Snuggle Bear","Snuggle Bunny","Snuggles","Snuggly","Soda Pop","Songbird","Sparkles","Sparky","Spring","Sprinkles","Star","Starlight","Starshine","Steambuns","Stud Muffin","Sugar","Sugar Bear","Sugar Biscuit","Sugar Britches","Sugar Buns","Sugar Lips","Sugar Puff","Sugarplum","Summer","Summerpie","Sunshine","Sweet Baby","Sweet Cheeks","Sweet Pea","Sweet Peach","Sweet Potato","Sweetheart","Sweetie","Sweetie Bird","Sweetkins","Sweetness","Sweets","Sweetstuff","Sweetums","Sweety Cakes","Tator-tot","Teddy Bear","Toots","Tootsie","Tumtums","Twinkie","Twinkle Toes","Waffles","Wiggles","Wookie","Wookums","Yummy","Yumyum"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}