
function nameGen(type){
	var nm1 = ["A-types","Aberrants","Abnormals","Abnormies","Abnorms","Abs","Anomalies","Arcanay","Arcanil","Arcanix","Arcano","Arcanoes","Atyps","Beyonders","Blanks","Bonas","Centrics","Chimeras","Commoners","Culiars","Deviants","Eccentrics","Eccents","Extraordinaries","Extraors","Feebles","Freaks","Free","Generics","Genrics","Gens","Hollows","Humdrums","Idles","Illegits","Imps","Impures","Inerts","Irregs","Irregulars","Lawfuls","Legis","Legits","Malfors","Medians","Meras","Millers","Miscreants","Monos","Mortals","Mundanes","Munds","Mutants","Mutes","Nabracadabras","Nabras","Naturals","Naygicians","Naymagi","Nerics","Nizards","Nocana","Noccult","Nocus","Nocus Pocus","Nogician","Nomages","Nomagi","Nomalies","Nonchanters","Nonvoyants","Norcana","Norcerers","Normies","Norms","Novoyants","Oddities","Ordies","Ordinaries","Originals","Orthos","Passives","Peculiars","Propers","Reggies","Regs","Regulars","Spiritless","Standards","Standies","Strangers","Traditionals","Typicals","Typics","Unnaturals","Usuals","Vacants","Voids","Voodon't","Weirdos","Zaros"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
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