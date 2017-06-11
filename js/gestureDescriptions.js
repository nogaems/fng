var nm1 = ["area","city","country","district","empire","nation","province","realm","region","remote town","remote village","state","territory","town","village"];
var nm2 = ["B","C","D","F","G","H","I","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"];
var nm3 = ["a","e","o","u"];
var nm4 = ["br","cr","dr","fr","gr","pr","str","tr","bl","cl","fl","gl","pl","sl","sc","sk","sm","sn","sp","st","sw","ch","sh","th","wh"];
var nm5 = ["ia","a","en","ar","istan","aria","ington","ua","ijan","ain","ium","us","esh","os","ana","il","ad","or","ea","eau","ax","on","ana","ary","ya","ye","yae","ait","ein","urg","al","ines","ela"];
var nm6 = ["right","left"];
var nm7 = ["your face","someone else","the side","the sky","the ground"];
var nm8 = [", four fingers crossed and the last fully clenched",", four fingers crossed and the last fully stretched",", four fingers crossed and the last half clenched",", four fingers fully stretched and one fully clenched",", four fingers fully stretched and one half clenched",", one finger fully stretched and four half clenched",", one finger fully stretched and the other four fully clenched",", one finger fully stretched, one finger half clenched and the other three fully clenched",", one finger fully stretched, three finger half clenched and one fully clenched",", one finger fully stretched, two fingers half clenched and the other two fully clenched",", three fingers crossed and the other two fully clenched",", three fingers crossed and the other two fully stretched",", three fingers crossed, one fully clenched and one half clenched",", three fingers crossed, one fully stretched and one fully clenched",", three fingers crossed, one fully stretched and one half clenched",", three fingers fully stretched and the other two fully clenched",", three fingers fully stretched and two fingers half clenched",", three fingers fully stretched, one half clenched and one fully clenched",", thumb and one finger forming a circle and three fingers fully clenched",", thumb and one finger forming a circle and three fingers fully stretched",", thumb and one finger forming a circle and three fingers half clenched",", thumb and one finger forming a circle, one finger fully clenched and two fingers fully stretched",", thumb and one finger forming a circle, one finger fully clenched and two fingers half clenched",", thumb and one finger forming a circle, one finger fully clenched, one half clenched and one fully clenched",", thumb and one finger forming a circle, two fingers fully clenched and one fully clenched",", thumb and one finger forming a circle, two fingers fully clenched and one half clenched",", thumb and one finger forming a circle, two fingers half clenched and one fully stretched",", thumb and one finger forming a circle, two fingers half clenched and one fully clenched",", thumb and three fingers forming a circle and one finger fully clenched",", thumb and three fingers forming a circle and one finger fully stretched",", thumb and three fingers forming a circle and one finger half clenched",", thumb and two fingers forming a circle and two fingers fully clenched",", thumb and two fingers forming a circle and two fingers fully stretched",", thumb and two fingers forming a circle and two fingers half clenched",", thumb and two fingers forming a circle, one finger fully clenched and one finger fully stretched",", thumb and two fingers forming a circle, one finger fully clenched and one finger half clenched",", thumb and two fingers forming a circle, one finger half clenched and one finger fully stretched",", two fingers crossed and the other three fully clenched",", two fingers crossed and the other three fully stretched",", two fingers crossed and three fingers half clenched",", two fingers crossed, one finger fully stretched and the other two fully clenched",", two fingers crossed, one fully clenched and two half clenched",", two fingers crossed, one fully stretched and two half clenched",", two fingers crossed, two fingers fully stretched and the last one fully clenched",", two fingers crossed, two fully clenched and one half clenched",", two fingers crossed, two fully stretched and one half clenched",", two fingers fully stretched and the other three fully clenched",", two fingers fully stretched and three fingers half clenched",", two fingers fully stretched, one finger half clenched and the other two fully clenched",", two fingers fully stretched, two fingers half clenched and one fully clenched"," and a clenched fist"," and five fingers crossed"," and five fingers fully stretched"," and five fingers half clenched"];
var nm9 = ["expresses you or a situation is under control","expresses you're doing great","conveys you're sorry","conveys you're terribly sorry","expresses a beckon","conveys the equivalent of 'welcome to my home'","expresses the equivalent of 'my god bless you'","expresses the equivalent of 'my fortune shine upon you'","expresses that you think the person who's talking to you is talking nonsense","conveys you're trying to politely attract the attention of somebody else","politely expresses you'd like the person who's talking to you to stop talking","impolitely expresses you'd like the person who's talking to you to stop talking","expresses you feel solidarity with another person","expresses you're furious","is a form of intimidation or threat of violence towards another person","expresses you, another person or a situation is crazy or out of control","conveys a plead for aid, often used to emphasize what you say","expresses you wish the other person to be cursed, but is now more used as an insult","is used as a good luck charm","expresses boredom or being tired","is used as an obscene gesture","expresses a strong insult, often used when emotions are very high","expresses a feeling of mutual respect","conveys the equivalent of 'I feel your pain'","expresses the celebration of a victory","expresses the equivalent of 'I am here to help' or 'how can I help you?'","expresses a deep love for another, often used when you're unable to get close to the other person","expresses the equivalent of 'you may be cursed, stay away'","is used as a minor insult and is often used as a joke","is used after an unfortunate event and is meant to prevent it from repeating","is used after a fortunate event and is meant to cause it to prolong or repeat","is used to ward of evil influences","expresses money and is often used when haggling or dealing with large amounts of money","conveys the equivalent of 'stay away from me'","conveys the equivalent of 'I approve of this'","politely expresses a wish for others to be quiet","impolitely expresses a wish for others to be quiet","conveys a bond of friendship","expresses you have no idea what is going on or what is being talked about","expresses you're not doing great, but not too bad either","expresses you're not feeling or doing great","expresses you'd like to talk with another person and is often used from a distance","conveys the equivalent of 'I disapprove of this'","is used as an expression of you or something being cute","expresses a failure","expresses a success","expresses a lack of sympathy or a feeling of sarcasm","expresses you're not serious about what you're saying","is used to put emphasis on what you're saying","expresses a feeling of awkwardness and is often used to describe a situation","conveys the equivalent of 'this is wrong on so many levels'","conveys the equivalent of 'get out of my sight'","expresses you're feeling cold","expresses you're feeling hot","conveys a feeling of expectation and anticipation","conveys the equivalent of 'you win, I give up'","conveys the equivalent of 'please do not hurt me'","expresses the equivalent of 'do not worry, I mean you no harm'","conveys a feeling of strong disbelief","expresses love, similar to how you can make a heart shape with your hands","conveys the equivalent of 'this is/you are not worth my time'","expresses you have no idea and is often used as an answer to a question","conveys a plead for help or assistance","conveys the equivalent of 'you are dead to me'","conveys the equivalent of 'I will kill you'","expresses the equivalent of 'I am here for you'","is used as a salute and has a meaning similar to 'strength and honor'","expresses that the food you just ate is delicious","expresses gratitude for a gift you've just been given","expresses the equivalent of 'stop, do not move'","is used to strengthen an agreement similar to making a promise","is used as a formal greeting","is used as an informal greeting","expresses the equivalent of 'I got this'","expresses the equivalent of 'calm down'"];
var nm10 = ["against","next to","above","under","diagonally from","against","next to","against","next to","above","under"];

function nameGen(){
	
	var rnd1 = parseInt(Math.floor(Math.random() * nm1.length));
	var rnd2 = parseInt(Math.floor(Math.random() * nm2.length));
	var rnd3 = parseInt(Math.floor(Math.random() * nm3.length));
	var rnd4 = parseInt(Math.floor(Math.random() * nm4.length));
	var rnd5 = parseInt(Math.floor(Math.random() * nm5.length));
	var rnd6 = parseInt(Math.floor(Math.random() * nm6.length));
	var rnd7 = parseInt(Math.floor(Math.random() * nm7.length));
	var rnd8 = parseInt(Math.floor(Math.random() * nm8.length));
	var rnd9 = parseInt(Math.floor(Math.random() * nm9.length));
	var rnd10 = parseInt(Math.floor(Math.random() * nm10.length));

	var rnd11 = parseInt(Math.floor(Math.random() * nm1.length));
	var rnd12 = parseInt(Math.floor(Math.random() * nm2.length));
	var rnd13 = parseInt(Math.floor(Math.random() * nm3.length));
	var rnd14 = parseInt(Math.floor(Math.random() * nm4.length));
	var rnd15 = parseInt(Math.floor(Math.random() * nm5.length));
	var rnd16 = parseInt(Math.floor(Math.random() * nm7.length));
	var rnd17 = parseInt(Math.floor(Math.random() * nm8.length));
	var rnd18 = parseInt(Math.floor(Math.random() * nm7.length));
	var rnd19 = parseInt(Math.floor(Math.random() * nm8.length));
	var rnd20 = parseInt(Math.floor(Math.random() * nm9.length));
	var rnd21 = parseInt(Math.floor(Math.random() * nm10.length));
	
	
	var name = "Raising your " + nm6[rnd6] + " hand with the palm towards " + nm7[rnd7] + nm8[rnd8] + " is a gesture that " + nm9[rnd9] + " in the " + nm1[rnd1] + " of " + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm5[rnd5] + ".";
	var name2 = "-----------------------------------";
	var name3 = "Holding your left hand, with the palm towards " + nm7[rnd16] + nm8[rnd17] + ", " + nm10[rnd21] + " your right hand with the palm towards " + nm7[rnd18] + nm8[rnd19] + " is a gesture that " + nm9[rnd20] + " in the " + nm1[rnd11] + " of " + nm2[rnd12] + nm3[rnd13] + nm4[rnd14] + nm5[rnd15] + ".";

	var br = [];
	for(i = 0; i < 4; i++){
		br[i] = document.createElement('br');	
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}
	
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	element.appendChild(document.createTextNode(name));
	element.appendChild(br[0]);
	element.appendChild(br[1]);
	element.appendChild(document.createTextNode(name2));
	element.appendChild(br[2]);
	element.appendChild(br[3]);
	element.appendChild(document.createTextNode(name3));
	document.getElementById("placeholder").appendChild(element);
}	