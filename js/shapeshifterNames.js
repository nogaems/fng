var br = "";
function nameGen(type){
	var tp = type;
	if(tp === 1){
		var names1 = ["Angel","Fell","Anomaly","Aspect","Aura","Autumn","Banshee","Blend","Bubble","Cam (Chamelion)","Cary (Caricature)","Cat (Copycat)","Conny (Con Artist)","Copy","Daydream","Design","Ditto","Dream","Dupe","Dust","Echo","Effigy","Elle (Element)","Em (Emulate)","Enigma","Entity","Etch","Eve (Evolve)","Evo","Fable","Feign","Flow","Flux","Form","Fuse","Ghost","Harmony","Hazel","Iden (Identical)","Jen (Generate)","Kate (Duplicate)","Light","Lucy (Illusion/Hallucination)","Mai (Mime)","Mani (Manifest)","Match","Melion","Mien","Mime","Mingle","Mint","Mirage","Mirror","Mix","Nemo","Nil","Niq (Unique)","Nix","Oddity","Paradox","Parallel","Parody","Parrot","Phase","Phony","Rascal","Reflection","Repeat","Replica","Ringer","Rogue","Sam (Semblance)","Same","Scribble","Shade","Shadow","Shape","Sim (Simulate)","Sketch","Skin","Snow","Sue (Assume)","Switch","Syn (Synthesize)","Tailor","Tassy (Fantasy)","Trace","Tracy (Tracing)","Trixy","Twin","Valence (Equivalence)","Variel","Veil","Vista","Vu (Déjà Vu)","Whisper","X (Exchange)","Zero","Zip","Zot"];
	}else if(tp === 2){
		var names1 = ["Angel","Aspect","Blend","Copy","Daydream","Design","Ditto","Dream","Dupe","Dust","Echo","Effigy","Entity","Etch","Fable","Feign","Flow","Flux","Fuse","Ghost","Iden (Identical)","Light","Mani (Manifest)","Match","Melion","Mime","Mingle","Mint","Mirage","Mirror","Mix","Nemo","Nil","Niq (Unique)","Nix","Oddity","Paradox","Parallel","Parody","Parrot","Phase","Phony","Rascal","Reflection","Repeat","Replica","Ringer","Rogue","Sam (Semblance)","Same","Scribble","Shade","Shadow","Shape","Sim (Simulate)","Sketch","Skin","Snow","Switch","Syn (Synthesize)","Tailor","Trace","Twin","Valence (Equivalence)","Vista","Whisper","X (Exchange)","Zero","Zip","Zot"];
	}else{
		var names1 = ["Akin","Angel","Ape","Art (Artificial)","Aspect","Blend","Born","Carbon","Cipher","Clone","Copy","Counterpart","Daydream","Design","Ditto","Doppelganger","Dream","Dupe","Duplicate","Dust","Echo","Effigy","Entity","Etch","Fable","Face","Feign","Fester (Manifester)","Figment","Flow","Flux","Form","Fuse","Ghost","Guise","Guy (Guise)","Husk","Hybrid","Iden (Identical)","Imitation","Lance (Equivalence)","Light","Lou (Illusion/Hallucination)","Maestro","Mani (Manifest)","Match","Melion","Merge","Mick (Mimic)","Mime","Mingle","Mint","Mirage","Mirror","Mix","Mold","Morpheus (Morph)","Nemo","Nil","Niq (Unique)","Nix","Oddity","Paradox","Parallel","Parody","Parrot","Pat (Pattern)","Pete (Repeat)","Peter (Repeater)","Phantom","Phase","Phony","Pseudo","Range","Rascal","Reflection","Repeat","Replica","Ringer","Rogue","Romulus","Ruse","Sam (Semblance)","Same","Scar","Scribble","Shade","Shadow","Sham","Shape","Sim (Simulate)","Sketch","Skin","Snow","Specter","Sting","Stretch","Suit","Switch","Syn (Synthesize)","Tailor","Trace","Tracer","Turner","Twin","Valence (Equivalence)","Vice","Vice (Improvise)","Vista","Whisper","X (Exchange)","Zero","Zip","Zot"];
	}
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		names = names1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}