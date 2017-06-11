var nm2 = ["","","","","","","","","","","",""," Advanced"," Base"," Basic"," Engine"," Language"," Pro"," Script"," System","#","+","++","-2","-3","Base","Code","Edge","Pro","Script","X"];
function nameGen(){
	var nm1 = ["Abra","Ace","Aer","Agent","Ample","Ape","Asap","Ash","Aspect","Asset","Aura","Aurora","Beacon","Beat","Bindle","Blithe","Blossom","Boop","Borealis","Bundle","Cell","Chant","Chasm","Chime","Cinch","Cloud","Clout","Cluster","Clutch","Cobolt","Combi","Core","Cozy","Crux","Curator","Cure","Curio","Curious","Dawn","Digi","Ditto","Ditty","Divi","Djinni","Dodge","Domino","Dozer","Dragoon","Drake","Echo","Effigy","Efflux","Ego","Elementary","Ellipse","Ember","Emblem","Entity","Ether","Ex.","Fig","Flare","Fleet","Flex","Flix","Float","Flow","Fluo","Fuse","Galore","GameOn","Gem","Geode","Gig","Gist","Glint","Gloss","Glow","Groove","Guise","Hellion","Hex","Hiero","Hustle","Ideo","ImAge","Imp","Imput","Influx","Iris","Jade","Jewel","Jinx","Jive","Kazam","Knock","Lax","Limbo","Lithe","Lode","Lumos","Lure","Melody","Mic","Mime","Mini","Minmax","Mirage","Mirror","Mist","Mix","Mobius","Moxie","Mumbo","Myth","Neo","Neon","Nimbus","Notch","Obsidian","Oculus","Odd","Ode","Onyx","Opt","Optic","Oracle","Orbit","Paltry","Para","Paragon","Parcel","Parry","Particle","Patter","Petal","Pickle","Picnic","Picolo","Pinnacle","Pitch","Pivot","Pose","Precious","Prism","Pronto","Prospect","Pulse","Query","Rascal","Rebus","Reflect","Reverb","Ripple","Rune","Rush","Sabre","Sapphire","Scale","Scoop","Segue","Semble","Shift","Slang","Slice","Slick","Sliver","Smooth","Snap","Soar","Sonic","Spark","Sparkle","Speckle","Sphinx","Spirit","Splice","Strut","Tiger","Tremor","Tri","Triad","Trifle","Trinity","Trix","Tru","Tune","Twist","Vertex","Vibe","Vim","Virtue","Visage","Vitae","Vitality","Vortex","Voyage","Wave","Wiz","Zest"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + nm2[rnd2];
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