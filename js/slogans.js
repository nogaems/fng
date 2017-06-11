function nameGen(type){
	var nm1 = ["A moment of harmony","A slice of heaven","A solid foundation","Ahead of our time","All as one","Always in front","Art of excellence","Art of perfection","As always","Baby steps","Be better","Be bold","Be cool","Be more","Be stronger","Be the best","Be the best you can be","Be the change","Be the leader","Be the power","Be the revolution","Beautiful experiences","Beauty of simplicity","Because diamonds are forever","Because you're special","Become your best","Before you know it","Best performance","Better care, better life","Better standards","Beyond boundaries","Beyond comfort","Beyond perfection","Beyond the limit","Beyond the sky","Bigger by being smaller","Bite sized business","Blissful knowledge","Born for success","Bottom's up","Bring it on","Bringing solutions","Building the future","Change a life","Change the future","Changing tomorrow","Comfort in our hands","Comfort of your home","Creative solutions","Dare to be","Designed for you","Doing the impossible","Driven to perfection","Easy as can be","Empower you","Endless possibilities","Enjoy","Eternal pursuit","Everybody needs a break","Expanding horizons","Expect excellence","Experience in our hands","Experience is key","Fit for a king","Fit for a queen","Follow the leader","For champions","For love","For the good times","For those who care","Going the extra mile","Hand in hand","Hearts united","Hold the power","Imagination at work","Imagine the impossible","Imagine this","Imagine tomorrow","Improved happiness","Infinite possibilities","It's in your hands","It's on","It's on us","It's our business","It's our passion","It's our pleasure","It's time","It's your choice","Just enjoy","Just for you","Just imagine","Just relax","Just the beginning","King and queen","Lead the way","Life experience","Life without strife","Limitless","Listen","Little miracles","Little pleasures, great joys","Live in the moment","Live today, dream of tomorrow","Live your dreams","Live. Love. Play","Long endurance","Love of life","Make it happen","Mark of excellence","Mastered perfection","Maximize life","Moments of bliss","Moments of clarity","More than just a taste","Moving forwards","Moving mountains","Never stop dreaming","No problem","Nothing beats the best","Nothing's better","Now's the time","Obsession for details","On the front line","One step at a time","Only the best","Onward","Open your eyes to the possibilities","Opening doors","Outside the box","Powered by you","Pure delight","Push the boundaries","Pushing the limits","Quality first","Raising the bar","Recipe for success","Redefining the box","Redefining impossible","Relax, we got this","Relive the moment","Remember","Road to success","See you next time","Sheer pleasure","Shh, it's a secret","Simplicity","Simply outstanding","Simply perfection","Smile","Standards of excellence","Standing out","Success","Surprise","The future","The good feeling","The next generation","The other side","The possibilities are endless","The show goes on","The sky's not the limit","The sky's the limit","The time is now","There's nothing else like it","There's nothing like it","Think about it","Think creative","Think positive","Thinking ahead","Thinking solutions","To the extreme","Trial and success","True sensations","Trust us","Unbreakable bonds","Unbreakable spirit","Unbroken promises","Uniquely the best","Unleash the power","We are one","We believe","We believe in you","We care","We have your back","We keep our promises","We never stop","We promise the best","We provide excellence","We won't contain it","We're forever","We're here for you","We've got you covered","Welcome","Welcome back","With love","With pleasure","With style","With you for life","Work hard. Play harder","You come first","Your wish is our command"];

	var br = "";

	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd] + ".";
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