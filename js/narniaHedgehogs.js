function nameGen(){
	var nm1 = ["addle","aidle","babble","baffle","bashle","bindle","boggle","bondle","breezle","buffle","burple","burrow","bustle","chatle","chipple","chopple","climble","comble","crackle","craddle","cuddle","dabble","dangle","dartle","dazzle","diggle","dipple","doffle","draggle","dribble","dripple","droople","dropple","dubble","dustle","feedle","fibble","fiddle","fittle","flapple","fumble","giggle","gobble","goggle","grabble","grapple","grasple","gripple","grumple","hobble","hoggle","hopple","huddle","huggle","hustle","jabble","jangle","juggle","knittle","lisple","lurkle","meddle","meeple","muggle","nibble","paddle","peekle","pickle","plopple","popple","proddle","puffle","ramble","riddle","ripple","rumble","rustle","scramble","scribble","scrubble","smirkle","sniffle","snuggle","startle","stumble","swattle","tapple","thumble","tickle","tipple","toddle","topple","tripple","waddle","waggle","wiggle","wriggle"];;
	var nm2 = ["badge","bag","bags","band","bat","bead","bell","belt","bet","bit","book","boot","boots","bottle","box","bun","butt","cakes","cap","caps","cart","cheek","cheeks","chin","chip","comb","cord","cork","crate","crib","dig","dish","dock","dot","drop","drum","feet","fog","fold","foot","gap","gear","gift","grab","grip","hand","hat","hold","hook","host","jam","jar","keep","key","knot","lab","lock","log","luck","mess","mud","need","needle","nose","note","pack","page","pin","pir","pit","pivk","plan","play","pop","pot","quill","rod","roll","root","rub","sack","share","ship","shop","slip","split","spot","stamp","step","stick","stock","store","strip","stuff","thread","tip","top","tub","vest","wit"];

	var br = "";
	$('#placeholder').css('textTransform', 'capitalize');

	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0;
		while(nm1[rnd] === nm2[rnd2]){
			rnd2 = Math.random() * nm2.length | 0;
		}
		names = nm1[rnd] + nm2[rnd2];
		nm1.splice(rnd, 1);
		nm2.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}