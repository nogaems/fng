var names1 = ["","","","","","","","","","","","","","","","","","","","","","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","ch","sh","ph","br","cr","dr","gr","kr","pr","str","vr","wr","","bl","cl","gl","fl","kl","pl","sl"];
var names2 = ["a","e","i","o","u"];
var names3 = ["sh","ch","ph","cr","dr","gr","str","cl","gl","kl","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","bb","cc","dd","gg","kk","ll","mm","nn","pp","rr","ss","tt"];
var names4 = ["a","e","i","o","u","ea","eo","ia","io"];
var names5 = [" Fruit"," Nut"," Root"," Shoot","baco","bage","bana","bola","bosu","cado","can","ccoli","chee","chini","choke","cket","cona","cory","cot","cress","curi","damia","darin","dilla","dine","dish","dnut","flower","fruit","gette","guaro","gus","jube","kin","kra","ku","lal","lasan","le","lery","lini","lly","lon","loupe","mansi","mato","mber","mbi","mble","me","melo","mia","mmon","mon","mond","mquat","na","nach","nana","nate","nce","nda","ndu","ne","nge","nger","ngo","nip","ntine","nut","paw","paya","pe","per","ple","quat","quila","rac","ragus","rana","rang","rant","ranth","rd","rel","riac","rian","ricot","riman","rin","rind","rine","rlan","ro","rola","rra","rrot","rry","rula","san","shew","snip","tain","tato","taya","te","til","tillo","tine","to","tron","tuce","va","ve","ves","wan","wesh","wi","ya","yote"];

var names6 = ["Abyss","Angel","Arctic","Ash","Autumn","Baby","Beach","Bitter","Bittersweet","Black","Blood","Blue","Bronze","Brown","Bush","Candy","Cave","Cavern","Cinder","Cliff","Crimson","Daydream","Demon","Desert","Dessert","Devil","Dew","Dragon","Drake","Dream","Earth","Eastern","Elder","Elephant","Ember","Fade","False","Fire","Flowered","Flux","Forest","Golden","Green","Ground","Hairless","Hairy","Hard","Hate","Hazel","Heart","Ice","Island","Lake","Love","Mage","Mammoth","Mellow","Mimic","Miracle","Mist","Mock","Monster","Moon","Mountain","Mud","Mutant","Mystery","Mystical","Native","Night","Nightmare","Northern","Ocean","Peace","Pigmy","Pygmy","Rain","Red","River","Rose","Salty","Sanguine","Sea","Shimmer","Silk","Silver","Smelly","Soft","Sorrow","Sour","Southern","Spring","Star","Storm","Summer","Sun","Swamp","Sweet","Thorn","Thorny","Thunder","Tiger","Tropical","Tundra","Violet","Void","Water","Western","White","Wild","Winter","Wonder","Wood","Yellow","Young"];
var names7 = ["Acerola","Almond","Amaranth","Apple","Apricot","Artichoke","Asparagus","Avocado","Babaco","Bacuri","Bael","Banana","Bean","Berry","Bilimbi","Bolwarra","Boquila","Bramble","Breadnut","Broccoli","Broccolini","Cabbage","Calamansi","Cantaloupe","Carambola","Carrot","Cashew","Cauliflower","Cawesh","Celeriac","Celery","Celtuce","Ceriman","Chayote","Cherry","Chestnut","Chicory","Chives","Choy","Citron","Clementine","Cocona","Coconut","Courgette","Cucumber","Currant","Date","Dill","Duku","Durian","Fig","Fruit","Ginger","Gourd","Granadilla","Grape","Grapefruit","Guanabana","Guarana","Guava","Hazelnut","Jujube","Kabosu","Kale","Kiwi","Korlan","Kumquat","Laurel","Leek","Lemon","Lentil","Lettuce","Lillypilly","Lime","Loquat","Lychee","Macadamia","Mandarin","Mango","Mangosteen","Marang","Marula","Melon","Morinda","Mundu","Muscadine","Nectarine","Okra","Olive","Onion","Orange","Papaya","Paracress","Parsnip","Pawpaw","Pea","Peach","Pear","Pecan","Pepper","Persimmon","Pitaya","Plantain","Plum","Pomegranate","Pomelo","Pommerac","Potato","Prune","Pulasan","Pumpkin","Quince","Radish","Rocket","Root","Rowan","Saguaro","Salal","Spinach","Sprout","Squash","Tamarind","Tangerine","Tomatillo","Tomato","Turnip","Walnut","Yam","Zucchini"];

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * names1.length);
			rnd2 = Math.floor(Math.random() * names2.length);
			rnd3 = Math.floor(Math.random() * names3.length);
			if(rnd > 41){
				while(rnd3 < 11){
					rnd3 = Math.floor(Math.random() * names3.length);
				}
			}
			rnd4 = Math.floor(Math.random() * names4.length);
			rnd5 = Math.floor(Math.random() * names5.length);
			names = names1[rnd] + names2[rnd2] + names3[rnd3] + names4[rnd4] + names5[rnd5];
		}else{
			rnd = Math.floor(Math.random() * names6.length);
			rnd2 = Math.floor(Math.random() * names7.length);
			names = names6[rnd] + " " + names7[rnd2];
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