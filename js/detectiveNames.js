var nm1 = ["Ace","Adam","Adrian","Alec","Alex","Andrew","Arthur","Barry","Bill","Brad","Braden","Brian","Bruce","Carl","Chad","Charles","Chris","Clive","Conan","Conor","Craig","Dale","Dan","Darryl","Dave","David","Denzel","Derek","Don","Donald","Drake","Dwayne","Ed","Edgar","Ethan","Frank","Fred","Gavin","George","Glenn","Gordon","Graham","Grant","Greg","Gus","Hal","Hank","Harold","Harris","Harry","Hector","Henry","Jack","Jacob","Jake","James","Jason","Jim","Joe","Jon","Kurt","Lance","Larry","Lars","Leo","Logan","Lou","Luke","Marcus","Martin","Marvin","Matt","Max","Michael","Mike","Miles","Moe","Morgan","Nic","Oscar","Owen","Oz","Paul","Pete","Peter","Phil","Pierce","Ray","Raymond","Rex","Rick","Rob","Robert","Roger","Russ","Russell","Ryan","Sam","Samuel","Saul","Scott","Sean","Seth","Shawn","Sid","Stan","Stephen","Steven","Terry","Thomas","Tom","Tony","Trevor","Victor","Vince","Walter","Wayne","Will","William","Zac","Zack"];
var nm2 = ["Abby","Adriana","Agnes","Alex","Alice","Amber","Angela","Ann","Annabel","Anne","Arya","Audra","Aurora","Avril","Barbara","Beth","Brenda","Bridget","Brittany","Brooke","Brynn","Caitlin","Carolyn","Cassie","Catlyn","Charlotte","Christie","Clare","Cleo","Debra","Diana","Dianne","Edit","Eleanor","Elizabeth","Ellen","Ellie","Elza","Emma","Erika","Erin","Eve","Fiona","Fran","Grace","Gwen","Hanna","Hazel","Helen","Hilda","Irene","Iris","Jaime","Jane","Janis","Jean","Jenna","Jennifer","Jessica","Jill","Jo","Joan","Joanne","Judith","Julia","June","Karen","Kat","Kate","Kim","Lara","Laura","Lauren","Lillian","Lois","Lucy","Marilyn","Marion","Mary","Meg","Megan","Meryl","Michelle","Myra","Nadia","Natalie","Nicole","Nikki","Nora","Pam","Paula","Rachel","Renee","Robin","Rose","Roxanne","Ruth","Sage","Sam","Sandra","Sarah","Serena","Sharon","Skye","Stella","Sue","Susan","Tess","Vera","Vicky","Vivian","Ziva"];
var nm3 = ["Abbott","Ace","Adams","Alexander","Anderson","Archer","Armstrong","Ashton","Bates","Bishop","Booth","Brady","Briggs","Brown","Burn","Burnham","Burns","Caine","Campbell","Carter","Carver","Chase","Clark","Clarkson","Cole","Collins","Cooper","Cox","Cross","Daniels","Darwin","Davidson","Davis","Dawson","Dixon","Donovan","Dukes","Duncan","Eckart","Finn","Ford","Foreman","Fox","Freeman","Frost","Gibbs","Gibson","Gold","Granger","Graves","Grey","Gunn","Hackman","Hammer","Harris","Hastings","Hawkes","Hayes","Heath","Higgins","Hill","Horn","Hunter","Jackson","Johnson","Jones","Jordan","Kane","King","Knight","Knott","Lambert","Law","Lawson","Lawton","Lawyer","Lee","Lincoln","Locke","MacLeod","Marshall","Mason","Matthews","Maxwell","Moore","Morgan","Morris","Murray","Newton","Nicholson","Nixon","Nolan","Palmer","Parker","Prescott","Price","Quinn","Reagan","Robinson","Roth","Sanders","Sawyer","Seals","Sharpe","Shepherd","Shields","Simons","Skinner","Smith","Snow","Spade","Steel","Stone","Sullivan","Tanner","Taylor","Thorn","Walker","Ward","Watson","West","White","Williams","Winder","Wolfe","Woods","Woolf","Wright","Zeal"];
var nm4 = ["Aaren","Addison","Aidan","Ainsley","Alex","Angel","Arin","Ash","Ashton","Avery","Bailey","Blair","Blake","Blythe","Brett","Brook","Cameron","Casey","Cass","Charlie","Chris","Cory","Dakota","Danny","Daryl","Drew","Dylan","Eli","Emerson","Gale","Harley","Harper","Hayden","Jackie","Jaden","Jaiden","Jamie","Jay","Jesse","Jo","Jordan","Jules","Kasey","Kerry","Lane","Lee","Logan","Lynn","Marley","Mell","Merle","Mo","Morgan","Nat","Quinn","Raegan","Reese","Riley","River","Robin","Rowan","Sam","Shannon","Shawn","Skyler","Stevie","Sydney","Tanner","Taylor","Tristan","Tyler","Val","Vic","Wil"];

function nameGen(type){
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			rnd2 = Math.floor(Math.random() * nm3.length);
			names = nm2[rnd] + " " + nm3[rnd2];
		}else if(tp === 2){
			rnd = Math.floor(Math.random() * nm4.length);
			rnd2 = Math.floor(Math.random() * nm3.length);
			names = nm4[rnd] + " " + nm3[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm3.length);
			names = nm1[rnd] + " " + nm3[rnd2];
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