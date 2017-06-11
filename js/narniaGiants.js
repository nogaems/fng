function nameGen(){
	var nm1 = ["anger","band","basin","bitter","bother","boulder","bramble","bubble","bumble","butter","button","cannon","cattle","cloud","cobble","common","copper","crumble","dabble","dimple","double","garden","good","grand","ground","long","lumber","marble","middle","moon","mud","mumble","night","nimble","pebble","plane","pocket","powder","puddle","ramble","range","rich","riddle","river","rock","rumble","scratch","shadow","shock","silver","simple","slumber","spark","stone","storm","struggle","tackle","thunder","trouble","tumble","weather","whistle","wild","wobble","wonder"];
	var nm2 = ["back","balance","basin","bead","berry","block","bottom","boulder","branch","breath","bubble","buffer","buffin","button","chin","cloud","coat","cover","crown","cushion","dance","dock","drag","dream","drum","feature","foot","force","friend","grace","growth","guard","guide","habit","hand","heart","hide","kin","kind","knot","link","loaf","lock","lumber","marble","march","mask","might","mind","mountain","move","noise","paint","patch","plate","plot","point","pound","pride","rest","rhythm","ride","roll","root","run","rush","scratch","shift","shine","shock","shot","slumber","spark","spell","stand","storm","stream","string","swing","thunder","tool","tremor","tune","wave","weather","wind","wire","zephyr","zone"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0;
		if(nm1[rnd] === nm2[rnd2]){
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