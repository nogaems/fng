var nm1 = ["Aaron","Adam","Aidan","Aiden","Alex","Alexander","Alfie","Andrew","Anthony","Archie","Arthur","Ashton","Bailey","Ben","Benjamin","Billy","Blake","Bobby","Bradley","Brandon","Caleb","Callum","Cameron","Charles","Charlie","Christopher","Cody","Connor","Corey","Daniel","David","Declan","Dexter","Dominic","Dylan","Edward","Elliot","Ellis","Ethan","Evan","Ewan","Finlay","Finley","Frankie","Freddie","Frederick","Gabriel","George","Harley","Harrison","Harry","Harvey","Hayden","Henry","Isaac","Jack","Jackson","Jacob","Jake","James","Jamie","Jay","Jayden","Jenson","Joe","Joel","John","Jonathan","Jordan","Joseph","Josh","Joshua","Jude","Kai","Kayden","Kian","Kieran","Kyle","Leo","Leon","Lewis","Liam","Logan","Louie","Louis","Luca","Lucas","Luke","Mason","Matthew","Max","Michael","Morgan","Nathan","Nicholas","Noah","Oliver","Ollie","Oscar","Owen","Patrick","Peter","Reece","Reuben","Rhys","Riley","Robert","Rory","Ryan","Sam","Samuel","Scott","Sean","Sebastian","Spencer","Stanley","Taylor","Theo","Thomas","Toby","Tom","Tommy","Tyler","William","Zac","Zachary","Zak"];
var nm2 = ["Abbie","Abby","Abigail","Aimee","Alexandra","Alice","Alicia","Alisha","Amber","Amelia","Amelie","Amy","Anna","Ava","Bella","Bethany","Brooke","Caitlin","Cerys","Charlie","Charlotte","Chelsea","Chloe","Courtney","Daisy","Danielle","Demi","Eleanor","Eliza","Elizabeth","Ella","Ellie","Eloise","Elsie","Emilia","Emily","Emma","Erin","Esme","Eva","Eve","Evelyn","Evie","Faith","Freya","Georgia","Georgina","Grace","Gracie","Hannah","Harriet","Heidi","Hollie","Holly","Imogen","Isabel","Isabella","Isabelle","Isla","Isobel","Jade","Jasmine","Jennifer","Jessica","Jodie","Julia","Kate","Katherine","Katie","Kayla","Kayleigh","Keira","Lacey","Lara","Laura","Lauren","Layla","Leah","Lexi","Lexie","Libby","Lilly","Lily","Lola","Louise","Lucy","Lydia","Maddison","Madeleine","Madison","Maisie","Maisy","Maria","Martha","Matilda","Maya","Megan","Melissa","Mia","Millie","Mollie","Molly","Morgan","Mya","Naomi","Natasha","Niamh","Nicole","Olivia","Paige","Phoebe","Poppy","Rachel","Rebecca","Rose","Rosie","Ruby","Samantha","Sara","Sarah","Scarlett","Shannon","Sienna","Skye","Sofia","Sophia","Sophie","Summer","Tegan","Tia","Tilly","Victoria","Willow","Yasmin","Zara","Zoe"];
var nm3 = ["Aaren","Addison","Aiden","Alex","Alexis","Ali","Angel","Ash","Ashley","Ashton","Aubrey","Avery","Bailey","Bennie","Bev","Billie","Billy","Blair","Blake","Bret","Brett","Brice","Brook","Brynn","Caden","Cameron","Carmen","Carol","Casey","Charlie","Chris","Clem","Cory","Dane","Danni","Danny","Denny","Drew","Eli","Elliot","Emerson","Erin","Fran","Frankie","Franky","Gabby","Gabe","Gail","Gale","Gene","Glen","Glenn","Haiden","Harley","Harper","Hayden","Jackie","Jaden","Jaime","Jamie","Jess","Jesse","Jessie","Jo","Jody","Jordan","Jude","Justice","Kai","Kerry","Kiran","Kit","Kris","Lane","Lee","Leigh","Lesley","Leslie","Logan","Lynn","Maddox","Marley","Mason","Mel","Mell","Morgan","Nicky","Noel","Phoenix","Quinn","Ray","Raylee","Reed","Reggie","Rene","Riley","River","Robin","Rory","Rowan","Rudy","Ryan","Sam","Sammy","Shay","Sidney","Silver","Skye","Skylar","Skyler","Steff","Tanner","Taylor","Terry","Tyler","Val","Vic","Will","Willy"];
var nm4 = ["Alder","Amber","Ash","Autumn","Beau","Belle","Black","Bran","Bright","Cart","Clear","Cliff","Cloud","Cold","Common","Coven","Crag","Dawn","Deep","Dew","Distant","Dream","Dusk","Earth","Elder","Ember","Even","Fair","Far","Feather","Fern","Fire","Flame","Flat","Forest","Free","Full","Glad","Glory","Gold","Grand","Gray","Great","Hard","Haven","Hay","Heart","Heavy","High","Hill","Honor","Humble","Keen","Kings","Light","Lone","Long","Low","Meadow","Merry","Mid","Mild","Moon","Morning","Night","Noble","Pen","Plain","Pont","Pride","Proud","Rain","Raven","Regal","River","Rose","Sage","Shadow","Sharp","Shield","Silent","Silver","Simple","Single","Sky","Snow","Soft","Spirit","Spring","Star","Stark","Stern","Still","Stout","Strong","Summer","Sun","Swift","Tall","Town","Tree","True","Way","Whisper","Whit","White","Wild","Wind","Winter","Wise","Wolf","Wood","Young"];
var nm5 = ["bane","beam","bloom","blossom","bluff","born","bough","bow","braid","branch","brand","breath","breeze","brook","brow","child","creek","crest","cross","dale","dew","down","draft","dream","fall","flare","flaw","fleur","flow","flower","force","ford","gaze","gem","glade","gleam","glide","grove","guard","hallow","heart","hood","keep","lace","land","law","less","man","mark","mercy","might","mill","more","peace","ridge","root","run","scar","send","shade","sky","smith","soar","song","spark","stern","stone","stride","sun","surge","sworn","thorn","tide","tower","tree","vale","ward","water","weather","weaver","well","whirl","wind","winds","wine","wing","winter","wood","woods","wright"];
var br = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm4.length);
		rnd3 = Math.floor(Math.random() * nm5.length);
		nl = nm4[rnd2] + nm5[rnd3];
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd] + " " + nl;
		}else if(tp === 2){
			rnd = Math.floor(Math.random() * nm3.length);
			names = nm3[rnd] + " " + nl;
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd] + " " + nl;
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