var names1 = ["Ash","Awful","Bad","Black","Blue","Bottom","Broken","Brown","Cheap","Dirt","Dirty","Down","Drab","Dreck","Dust","Feeble","Filthy","Foul","Fragile","Frail","Garbage","Grease","Grey","Grim","Grime","Grisly","Gross","Grotesque","Hideous","Horrid","Ill","Inferior","Infirm","Junk","Lesser","Little","Lousy","Low","Meager","Measly","Mediocre","Menial","Messy","Minor","Monstrous","Muck","Mud","Murky","Nasty","Paltry","Peon","Pesky","Poor","Puny","Raunchy","Red","Repulsive","Revolting","Sad","Scant","Scrap","Shame","Shoddy","Sick","Slag","Slimey","Slop","Smut","Soil","Soot","Stink","Tiny","Trash","Trashy","Trivial","Ugly","Vile","Waste","Worthless","Wracked","Wretched"];
var names2 = ["Ant","Beetle","Bug","Crawler","Creep","Creeper","Cricket","Curse","Dog","Flea","Fly","Frog","Grub","Insect","Larva","Leech","Maggot","Mite","Mole","Mongrel","Moth","Mouse","Mule","Mutt","Nit","Parasite","Pest","Pig","Rabbit","Rat","Roach","Rodent","Scrub","Shrimp","Snail","Spider","Squirmer","Termite","Tick","Toad","Vermin","Weasel","Weevil","Whelp","Worm","Wriggler","Runt","Slug","Oaf","Prawn","Louse","Skunk"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		rnd2 = Math.floor(Math.random() * names2.length);
		names = names1[rnd] + " " + names2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}