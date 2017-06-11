function nameGen(){
	var nm1 = ["agile","arch","bitter","blank","bold","brass","brave","broken","charge","cloud","cold","copper","copse","court","crown","dark","deep","den","diamond","dim","dirt","dream","drum","dual","dust","earth","earthen","even","fire","flame","fluke","fog","free","frost","ghost","glass","glen","gold","good","grand","great","grey","grim","grove","half","heart","ice","ink","iron","kind","light","lightning","lone","long","loud","lunar","mad","mask","meadow","might","mind","mist","moon","mud","night","phase","prime","proud","quiver","rain","rich","river","roon","rough","rush","shadow","silk","silver","single","sky","slim","smoke","snow","solar","spark","star","stark","stone","sun","swift","tall","temper","thunder","wind","wise","wood","world","young"];
	var nm2 = ["arm","back","band","bolt","chance","charge","chest","clap","cloud","clover","coil","crest","crown","dance","dream","drum","edge","fire","flame","grace","grip","heart","hoof","horn","hunt","light","lock","mane","mask","might","mind","mist","pride","reach","rest","ridge","root","run","runner","shine","star","stone","storm","tale","trail","veil","web","wish","wit","worth"];

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