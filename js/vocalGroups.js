function nameGen(){
	var nm2 = ["A Bridge Too Far","A Choir","A Choired Taste","A due a due","Acapellaca","Acoustricks","Alcuna Licenza","Alcuna Matata","Alive and Singing","Allophones","Amadeus Amadeus","Amici","Amor Amore","Angel Voices","Angelicus","Anima","Anima Animals","Animatomatoes","Ascension","Audacity","Aural Fixation","Aurora","Bella Voci","Bellacapella","Bravo Bravura","Cameos","Canon The Barbarian","Celestial Voices","Change of Tone","Change of Tune","Choir Courage","Choir Generation","Choir of my Heart","Choral Beauty","Choral Life","Choral Reef","Chord on Blues","Chords of Illusion","Chorus","Classic Harmonies","Clef Hangers","Cleftomaniacs","Cloud Nine Harmonies","Colossale Colossal","Comodo Comodus","ConChords","Cordless Chords","Crescendo","Crescendoos","Crescendudes","Dawn Chorus","Decibelles","Descant Get Enough","Dolce Vita","Double Treble","Dressed to Trill","Drop the Bass","Duly Noted","Dynamic Dynamics","Echo Echo","Echo Echo Echo","Eclectic Voices","Enchorus","Encore","Encore Choir","Encore Ensemble","Ending On High Notes","Epiphony","Euphonics","Euphonism","Euphonix","Euphony","Fire Choir","Floral Chorals","Fortissimo","Found Your Voice","Full Score","Future Notes","Gathered Voices","Grace Notes","Gryphonics","Harmless Harmonies","Harmonious Harmonies","Harmonium","Heart 'n Soul","Heritage Voices","High Notes","Homophonics","Hymn and Her","Illume","Impromptu","Improvvisato","In Choir","Inspire","Interlude","Joy","Just Sing","Keytones","Lady Treble","Light My Choir","Little Lyres","Little Voices","Local Vocals","Loose Canons","Lost Sounds","Loud and Proud","Luminos","Magico Magnifico","Man Treble","Mended Chords","Messa di voce","Mouth Noise","Nothing But Treble","Octavius","On a side note","Our Voices","Out On A Hymn","Pandamonium","Phil's Harmonics","Poco a poco","Polyphones","Polyphonics","Potpourri","Prima Volta","Public Hearing","Quite a choir","Ransom Notes","Re-Choir","Reign of Choir","Rivertones","Rolling Tones","S-Choir","Saved by the Belles","Semplice","Senza Misura","Serenata","Singing About You","Siren Serenade","Sons of Pitches","Spinal Chords","Spirit Vocals","Spiritoso Spirito","Symphonies","Take Note","Take a chant","Teeny Tones","The Barbaro","The Big Chorus","The Choir Factor","The Danger Tone","The Double Dots","The Drones","The Intonations","The Singalongs","The Sound Collective","The Sound Crowd","The Tone Commandments","The Voice Collective","Timbre!","Time to Trill","Tonal Eclipse","Tone Collectors","Tone Wolves","Top Notes","Treble Rebels","Treble Tones","Treble in Paradise","Tremoloco","Trill of the Night","Triller","Trinity","Tune In","Valley Voices","Varia Zone","Variazioni","Viva Vivace","Vocal Affinity","Vocal Chords","Vocal Harmony","Vocal Movement","Voce Pienna","Voce Vita","Voice of the People","Voices In Our Head","Voicestra","Vox Anima","Vox Humana","Vox Populi","Wicked Pitch of the West","Young Voices","Prime Chorus"];

	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm2.length);
		names = nm2[rnd];
		nm2.splice(rnd, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}