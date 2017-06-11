var nm1 = ["Abbington","Abbot","Abner","Abraham","Alastair","Albert","Albus","Alexander","Alfred","Alistair","Andrew","Angus","Anslo","Archibald","Arlington","Ashby","Ashton","Atwood","Bailey","Baines","Baldrick","Baldwin","Barkley","Barnabus","Barnaby","Barrett","Bartholomew","Baxter","Beauregard","Belvadair","Benedict","Benson","Bentley","Bernard","Bertram","Bishop","Caldwell","Carlisle","Carlton","Carstair","Carter","Cedric","Charles","Chester","Christopher","Clarence","Clark","Claud","Claude","Clement","Cornelius","Crawford","Dalton","Darby","Darcy","Dorian","Edgar","Edmun","Edmund","Edward","Edwin","Elliot","Emerson","Francis","Franklin","Geoffrey","George","Gerald","Gerard","Gideon","Giles","Godfrey","Godwin","Graham","Gregory","Hamilton","Harold","Harris","Hartley","Hastings","Henry","Herbert","Hobbes","Hobson","Horace","Hubert","Humphrey","Hymphrey","Jacob","James","Jameson","Jasper","Jeeves","Jeremy","Johnathan","Kenworth","Kingsley","Lambert","Laurance","Leighton","Lombard","Lucious","Manfred","Maxwell","Milton","Montgomery","Mortimer","Nathaniel","Nicholas","Niles","Norman","Olin","Oliver","Orson","Oswald","Palmer","Percival","Percy","Philip","Pierce","Pierre","Piers","Porter","Prescott","Preston","Quentin","Quimby","Ramsey","Randolph","Reginald","Remington","Richard","Roderick","Roger","Roland","Rupert","Sebastian","Seymour","Sinclair","Smith","Sterling","Stuart","Theobold","Theodore","Tobin","Valentine","Wallace","Walter","Watson","Wentworth","Wilfred","Wilkins","Willard","Wilson","Winston"];
var nm2 = ["Abigail","Addison","Adelaide","Adeline","Alexandra","Alice","Anastasia","Angela","Angelina","Annabella","Annabelle","Anne","Annebella","Audrey","Beatrice","Belinda","Bernice","Blanche","Briana","Bridgette","Brittany","Caitlin","Camilla","Camille","Carolina","Cassandra","Cecilia","Celeste","Celia","Charity","Charlene","Charlotte","Claire","Clara","Clarissa","Clementine","Corline","Cynthia","Danielle","Daphne","Darlene","Delilah","Diana","Dora","Dorothy","Edit","Elaine","Eleanor","Eleanore","Elena","Elizabeth","Elsie","Emily","Eva","Evangeline","Eve","Evelyn","Fiona","Fleur","Florence","Francine","Genevieve","Georgina","Geraldine","Gertrude","Gloria","Grace","Gwendoline","Gwendolyn","Heather","Helen","Helena","Helene","Helga","Henrietta","Hillary","Ingrid","Isabella","Jeanette","Jessica","Johanna","Josephina","Josephine","Judith","Julia","Julianna","Julie","Juliet","June","Justine","Katherine","Kathlyn","Laura","Leah","Lillian","Lily","Lisabet","Lorelei","Louise","Lucille","Lydia","Madeline","Maisy","Margery","Marie","Marion","Martha","Mary","Mary Anne","Mary Grace","Matilda","Melanie","Meredith","Mildred","Miranda","Nadine","Naomi","Natalaia","Nicolette","Noelene","Nora","Ophelia","Penelope","Phoebe","Pippa","Portia","Priscilla","Prudence","Rose","Rosemary","Ruth","Sabrina","Samantha","Samara","Sarah","Scarlet","Selena","Selma","Serena","Shirley","Sophia","Stella","Tiffany","Valerie","Vanessa","Veronica","Victoria","Viola","Violet","Virginia","Vivian","Wendy","Wilhelmina","Zoe"];
var br = "";
var names = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd];
		}
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}