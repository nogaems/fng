
function nameGen(){
	var nm1 = ["Ah Choo","Alfie","Antsy","Augustus","Baggy","Bam Bam","Bashful","Bee","Beebee","Berry","Bim Bam","Bimbo","Bingo","Binky","Blinky","Blossom","Bobo","Bonbon","Bongo","Bonzo","Booboo","Boom Boom","Boxy","Bozo","Britches","Bronco","Bucket","Buddy","Buffo","Buffoon","Buster","Buttercup","Buttons","Candy","Casey","Charlie","Cheeky","Cheery","Chester","Choco","Choochoo","Chubby","Chuckles","Clarabell","Clueless","Clumsy","Coocoo","Cookie","Cornflake","Crafty","Cupcake","Curly","Daffy","Daisy","Dazzle","Dazzler","Digger","Dimdim","Dimple","Dimples","Dinky","Ditso","Doodles","Duckie","Dumbo","Dumpling","Dumpty","Dusty","Echo","Feathers","Floppy","Flopsy","Flower","Fluffy","Flutter","Freckles","Frosty","Giggle","Giggles","Gogo","Goofy","Googles","Happy","Harpo","Humpty","Jazzy","Jester","Jimbo","Jingles","Joey","Jojo","Joy","Jumbo","Junior","Kicker","Knicknack","Koko","Lala","Loko","Lollypop","Loof","Loofy","Loopy","Lucky","Lulu","Luna","Marble","Marbles","Mickey","Miko","Milo","Minstrel","Mittens","Molly","Monkey","Nanners","Noodles","Oddball","Pancake","Patch","Patches","Pickles","Pockets","Pogo","Poodles","Popsy","Puddles","Pumpkin","Raffles","Riddles","Ruffles","Scooter","Scruffy","Shaggy","Shorty","Skippy","Skittles","Smiley","Snickers","Snoots","Snuggles","Soots","Sparkle","Sparkles","Sparks","Sparky","Squeaks","Squigley","Squishy","Sugar","Sunshine","Tatters","Tickle","Tickles","Tiny","Toodles","Tootsy","Topsy","Trixy","Tubby","Twinkles","Velvet","Waldo","Wally","Whistle","Wiggles","Witty","Yoyo","Zeppy","Zippy"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
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