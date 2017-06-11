function nameGen(){
	var nm1 = ["babble","banter","bashing","bicker","blather","boggle","bristle","bubble","bumble","bundle","burble","burrow","bustle","caper","chuckle","clamor","cobble","crackle","crinkle","crumble","cuddle","dabble","dally","dandle","dangle","dazzle","dibble","dimple","dither","doodle","drabble","dribble","fiddle","fidget","flatter","flitter","flutter","fumble","gambol","gibber","giggle","gobble","grapple","heckle","hiccup","hinder","hobble","huddle","hustle","jabber","jangle","jiggle","jingle","jitter","jostle","juggle","jumble","lumber","meddle","mingle","muffle","mumble","murmur","mutter","nibble","paddle","patter","pebble","pedal","ponder","prattle","puddle","quarrel","quibble","ramble","rattle","riddle","ruffle","rumble","rustle","scuttle","shiver","shuffle","skitter","slumber","snicker","sniffle","spatter","spattle","spitter","spittle","splutter","sprinkle","startle","tickle","trickle","tumble","twiddle","twinkle","twitter","waddle","wander","whistle","wiggle","wobble"];
	var nm2 = ["badge","band","bean","bell","bells","berry","bit","bug","bun","cheek","cheeks","chess","chest","chin","chip","chips","click","cloud","coat","coin","cord","cork","cup","dig","dish","doll","dot","drop","fan","feat","feet","flow","fluke","foot","gift","glove","hat","heart","jam","joint","joke","joy","kiss","knot","leaf","link","mark","mask","patch","pie","piece","pitch","ray","ring","rub","run","rush","shine","side","slide","slip","spark","spot","star","step","straw","strip","tail","tale","teeth","tip","toe","toes","tooth","top","trick","tune","twig","twigs","twist","will","wish","wit"];
	
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