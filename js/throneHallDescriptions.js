function nameGen(){
	var nm1 = ["Huge","Massive","Tremendous","Great","Magnificent","Bulky","Lustrous","Polished","Humble","Modest","Narrow","Slim","Slender"];
	var nm2 = ["surrounding","encompassing","enclosing","encircling","hanging from","hanging from one side of","attached to","attached to one side of","at the bottoms of","half enclosing","half encompassing"];
	var nm3 = ["twelve","fourteen","ten","eight","six","sixteen"];
	var nm4 = ["marble","sandstone","obsidian","ivory","granite","alabaster","marmoreal","limestone","onyx","travertine","basalt","soapstone"];
	var nm5 = ["the entire","most of the","the lower levels of the","every part of the"];
	var nm6 = ["bathe it in an orange glow","blanket everything in a warm glow","shroud it in a dark orange radiance","paint the hall a range of yellows and oranges","their light wraps the hall in a warm radiance","engulf the throne hall in a brilliant glimmer","coat everything in an orange glimmer","radiate warmth across this hall","mantle the hall in warm yellows","cover the hall in warm oranges and dancing shadows","cover the hall in dancing shadows and a warm radiance","allow shadows to play and dance where light cannot reach","bathe the hall in a dancing glow of orange","engulf everything in a flickering radiance"];
	var nm7 = ["gems of the many artworks on","illustration of battles on","angelic paintings on","artistic depictions of legends on","paintings of vast landscapes on","illustrations of a legendary victory on","paintings of angels and cherubs on","intricate golden patterns on","carved symmetric patterns on","relatively modest chandeliers hanging from","humongous chandeliers hanging from","thousands of gems on","large mirrors on","countless gems on","tapestries depicting the kingdom hanging from","intricately carved woodwork hanging from","intricate and symmetrical design patterns on","illustrations of a kingdom in the sky on","gemmed runes on","relatively simple stonework on","unadorned stones on ","marble stone of","illustrations of gods on","stained glass windows in","glass of the windows in"];
	var nm8 = ["domed","arched","rounded","bowed","embowed","curved","slanted","terraced","layered","oblique","askew","sloped"];
	var nm9 = ["statues","gargoyles","memorials","stone effigies","statuettes","sculptures","marble icons","carved images"];
	var nm9b = [" and statues"," and gargoyles"," and memorials"," and stone effigies"," and statuettes"," and sculptures"," and marble icons"," and carved images","","","","","",""];
	var nm10 = ["marble","stone","wooden","mahogany","granite","obsidian","oaken","limestone","slate","porcelain","mosaic","grey wood","maple","teak"];
	var nm11 = ["august","ceremonious","elegant","extravagant","glorious","grand","imposing","impressive","lavish","luxurious","magnificent","majestic","marvelous","monumental","opulent","ostentatious","radiant","regal","royal","sublime"];
	
	var nm12 = ["A beryl","A cardinal","A carmine","A chestnut","A cobalt","A coral","A crimson","A golden","A jade","A lavender","A lilac","A magenta","A malachite","A maroon","A ruby","A saffron","A sanguine","A sapphire","A scarlet","A silver","A teal","A turquoise","A verdigris","A vermilion","A violet","A viridian","An alabaster","An amber","An azure","An ebony","An ivory","An onyx","An orchid"];
	var nm12b = ["beryl","cardinal","carmine","chestnut","cobalt","coral","crimson","golden","jade","lavender","lilac","magenta","malachite","maroon","ruby","saffron","sanguine","sapphire","scarlet","silver","teal","turquoise","verdigris","vermilion","violet","viridian","alabaster","amber","azure","ebony","ivory","onyx","orchid"];
	var nm13 = ["splits the entire room in half from the doors to the throne","splits part of the room in half from the throne to midway down the hall","runs from the throne down through the center and splits into two paths leading out","runs from the throne down the center and loops back from both left and right","runs down from the throne and marks the closest spot people can stand when they address the royal highness","runs down from the throne for a few meters before coming to an end","splits the entire room in half and is matched by the thinner ones on either side of the hall","runs from the throne to the doors and is matched by smaller ones on either side of the hall","runs down from the throne and splits to encircle the entire hall","runs in a circle around the room, with two paths at the throne and the main entrance"];
	var nm14 = ["matching","forked","ribbon","pennant","burgee","guidon","winged","pointed","embattled","square dag","swallow tail","rectangular","rounded"];
	var nm15 = ["gilded","golden","emblazoned","embellished","adorned","ornate","burnished"];
	var nm16 = ["borders","corners","crowns","decorations","edges","embroideries","fringes","lacery","margins","needlework","ornaments","plumes","quilting","ridges","sides","sigils","tapestries","tassels","tips","tracery","trimmings","tufts"];
	var nm17 = ["dangle gently from","hang from","drape from","swing gently from","droop from","decorate","cover parts of",""];
	var nm18 = ["hangs a torch","hangs a lantern","hangs a small chandelier","hangs a small luster","stands a large candlestick","stands a tall candle","stand several tapers of various sizes","sits a small alter full of candles","sits a shrine-like ornament covered in candles",""];
	var nm19 = ["they've all been","many of them have been","some of them have been","a few of them have been","almost all of them have been","all but a few have been","none but a few have been"];
	var nm20 = ["paintings","tapestries","statues","statuettes","sculptures","mosaics","wall paintings","murals","portraits","depictions","artistic depictions","artistic portrayals"];
	var nm21 = ["royalty long gone","late royal family members","late rulers","gods and goddesses","divine beings","legendary creatures","conquerors and victors","heroes and legends","heroes and leaders","leaders and legends","divine beings","other leaders of the world","powerful creatures","war heroes","the fiercest creatures of this kingdom","late heroes","folk heroes and legends"];
	var nm22 = ["Tall","Broad","Wide","Narrow","Slim","Modest","High","Grand","Massive","Hefty","Huge","Vast","Thick","Extensive","Immense","Humble"];
	var nm23 = [", stained glass",", stained glass",", stained glass",", stained glass",", stained glass",", colored glass",", tinted glass",", washed glass","","",""];
	var nm23b = [""," depicting ancient legends"," of intricate mosaics"," depicting divine beings"," depicting gods and goddesses"," depicting important moments of victory"," depicting late royalty"," depicting important royal moments"," of heavenly mosaics"," of mesmerizing mosaics"," with symmetric designs"];
	var nm24 = ["covered","shrouded","hidden","concealed","bordered","contoured","framed","enclosed","edged","neighbored"];
	var nm25 = ["curtains","drapes","draperies","veils"];
	var nm26 = ["jewels","gold leaves","intricate embroidery","fine patterns","impressive needlework","gilded linings","fancy tassels","emblazoned edges","burnished corners","embellished borders","decorated tips"];
	
	var nm27 = ["A ceremonious","A dignified","A grand","A grandiose","A great","A lavish","A magnificent","A majestic","A noble","A pompous","A radiant","A regal","A stately","A striking","A sublime","A towering","An elegant","An imposing","An impressive"];
	var nm28 = ["teak","gold","silver","stone","marble","onyx","obsidian","jade","sapphire","mahogany","oak","iron","molten steel","granite","carved rock","gold","porcelain","gold","silver","bronze","brass","gold","mahogany","mahogany","oak","oak","marble","marble","stone"];
	var nm29 = ["atop an elevated platform","at the center of a small platform","amidst two large statues","below a grand chandelier","in front of a giant painting of the previous ruler","in front of a giant painting of the kingdom","in front of a large window radiating light onto the throne","within a pagoda of sorts within this hall","behind a lavish gate of gilded wood","beneath an impressively decorated baldachin (canopy)","beneath a fairly plain looking baldachin (canopy)","beneath an almost entirely close baldachin (canopy)","beneath two overlooking statues of legendary beasts","atop a tall elevated platform","atop a balcony overlooking the throne hall"];
	var nm30 = ["two","three","four","five","six","two","two","three"];
	var nm31 = ["smaller and less elaborate","equally impressive","almost identical","plain, but comfortable","equally lavish","similar, but smaller","similar, but less ornate","rather plain looking","large, but far less ornate","similar, but undecorated"];
	var nm32 = ["those closest to the royal highness","the royal highness' direct family","the royal highness' family members","visiting dignitaries","the royal highness' trustees","those aiding the royal highness in all affairs","visiting royalty of other nations","esteemed guests"];
	var nm33 = ["intricate","simple","hundreds of elaborate","nothing but labyrinthine","complicated","textured and layered","layered","gilded","tangled","byzantine","symmetric","baroque","divine","holy","hallowed","sacred","symbolic"];
	var nm34 = ["carvings","emblems","sculptures","crests","designs","engravings","motifs","emblems","images","patterns","marks","etchings","inscriptions","illustrations"];
	var nm35 = ["the backside","each of the wide armrests","each of the stubby legs","each of the ornate legs","each of the elegant armrests","the wide backside","each of the broad feet","each of the rather slim feet","each of the front legs","each of the rear legs","each of the broad ears","each of the slim ears"];
	var nm36 = ["a gemmed","an abstract","a carved","an ornate","a sparkling","a crystal","a diamond","a gem encrusted","an elegant","a gilded","a chiseled","a sapphire","a jade","a ruby","a lavish"];
	var nm37 = ["sigil","rose","flower head","lion's head","animal head","head of a legendary creature","skull","face","angel wing","demon wing","crown","sun","moon","star","trident","lantern","dragon","snake","petal","flower","tree","ship","dagger","crescent moon","divine symbol","symbolic emblem"];
	var nm38 = ["soft","thick","thin","broad","fluffy","bulky","dense","light","stiff","comfortable","modest"];
	var nm39 = ["dark","light"];
	var nm40 = ["gilded","golden","emblazoned","embellished","adorned","ornate","burnished"];
	var nm41 = ["borders","corners","edges","embroideries","fringes","lacery","margins","needlework","plumes","quilting","ridges","sigils","tassels","tips","tracery","tufts"];
	
	var nm42 = ["waiting to see","expecting an audience with","wishing to witness","awaiting to be heard by","seeking the wisdom of","listening to","wishing to listen to"];
	var nm43 = ["many","few","plethora of","countless","abundance of","several"];
	var nm44 = ["lavish, but relatively simple","decorated, but somewhat uncomfortable","rather plain looking","extravagant and comfortable","opulent, albeit uncomfortable","gilded and otherwise extravagant","modest, yet comfortable","long and rather bulky","impressively carved","luxurious and comfortable","brightly decorated","lightly illuminated"];
	var nm45 = ["wooden","stone","mahogany","oak","sandstone","marble","granite","teak","iron","brass","maple","birch","alder"];
	var nm46 = ["facing the throne","facing the center of the hall","diagonally facing the throne","facing the throne in a half circle","perfectly aligned in rows","facing the throne in a V-shape","facing the throne in a wide V-shape","lined up perfectly symmetrical"];
	var nm47 = ["more ornate","specially decorated","extremely lavish","overly luxurious","extravagant","excessively embellished","opulent","luxurious","exuberant","gorgeous","impressive","luxuriant","rather ordinary looking","embellished","ceremonial","gilded","stately","renovated","humble looking","rather plain","specially built"];
	var nm48 = ["balconies","mezzanines","balustrades"];
	var nm49 = ["overlooking the throne","overlooking the hall","overlooking the entire hall","facing the throne","facing the benches below"];

	var rnd1 = Math.random() * nm1.length | 0;
	var rnd2 = Math.random() * nm2.length | 0;
	var rnd3 = Math.random() * nm3.length | 0;
	var rnd4 = Math.random() * nm4.length | 0;
	var rnd5 = Math.random() * nm5.length | 0;
	var rnd6 = Math.random() * nm6.length | 0;
	var rnd7 = Math.random() * nm7.length | 0;
	var rnd8 = Math.random() * nm8.length | 0;
	var rnd9 = Math.random() * nm9.length | 0;
	var rnd9b = Math.random() * nm9b.length | 0;
	while(rnd9 === rnd9b){
		rnd9b = Math.random() * nm9b.length | 0;
	}
	var rnd10 = Math.random() * nm10.length | 0;
	var rnd11 = Math.random() * nm11.length | 0;
	var rnd12 = Math.random() * nm12.length | 0;
	var rnd13 = Math.random() * nm13.length | 0;
	var rnd14 = Math.random() * nm14.length | 0;
	var rnd15 = Math.random() * nm15.length | 0;
	var rnd16 = Math.random() * nm16.length | 0;
	var rnd17 = Math.random() * nm17.length | 0;
	var rnd18 = Math.random() * nm18.length | 0;
	var rnd19 = Math.random() * nm19.length | 0;
	var rnd20 = Math.random() * nm20.length | 0;
	var rnd21 = Math.random() * nm21.length | 0;
	var rnd22 = Math.random() * nm22.length | 0;
	var rnd23 = Math.random() * nm23.length | 0;
	var rnd23b = 0;
	if(rnd23 < 5){
		rnd23b = Math.random() * nm23b.length | 0;
	}
	var rnd24 = Math.random() * nm24.length | 0;
	var rnd25 = Math.random() * nm25.length | 0;
	var rnd26 = Math.random() * nm26.length | 0;
	var rnd26b = Math.random() * nm26.length | 0;
	while(rnd26 === rnd26b){
		rnd26b = Math.random() * nm26.length | 0;
	}
	var rnd27 = Math.random() * nm27.length | 0;
	var rnd28 = Math.random() * nm28.length | 0;
	var rnd29 = Math.random() * nm29.length | 0;
	var rnd30 = Math.random() * nm30.length | 0;
	var rnd31 = Math.random() * nm31.length | 0;
	var rnd32 = Math.random() * nm32.length | 0;
	var rnd33 = Math.random() * nm33.length | 0;
	var rnd34 = Math.random() * nm34.length | 0;
	var rnd35 = Math.random() * nm35.length | 0;
	var rnd36 = Math.random() * nm36.length | 0;
	var rnd37 = Math.random() * nm37.length | 0;
	var rnd38 = Math.random() * nm38.length | 0;
	var rnd39 = Math.random() * nm39.length | 0;
	var rnd40 = Math.random() * nm40.length | 0;
	var rnd41 = Math.random() * nm41.length | 0;
	var rnd42 = Math.random() * nm42.length | 0;
	var rnd43 = Math.random() * nm43.length | 0;
	var rnd44 = Math.random() * nm44.length | 0;
	var rnd45 = Math.random() * nm45.length | 0;
	var rnd46 = Math.random() * nm46.length | 0;
	var rnd47 = Math.random() * nm47.length | 0;
	var rnd48 = Math.random() * nm48.length | 0;
	var rnd49 = Math.random() * nm49.length | 0;
	
	var name = nm1[rnd1] + " braziers " + nm2[rnd2] + " each of the " + nm3[rnd3] + " " + nm4[rnd4] + " columns light up " + nm5[rnd5] + " throne hall and " + nm6[rnd6] + ". The " + nm7[rnd7] + " the " + nm8[rnd8] + " ceiling dance in the flickering light while " + nm9[rnd9] + nm9b[rnd9b] + " look down upon the " + nm10[rnd10] + " floor of this " + nm11[rnd11] + " hall.";
	
	var name2 = nm12[rnd12] + " rug " + nm13[rnd13] + " while " + nm14[rnd14] + " banners with " + nm15[rnd15] + " " + nm16[rnd16] + " " + nm17[rnd17] + " the walls. Between each banner " + nm18[rnd18] + ", " + nm19[rnd19] + " lit and in turn illuminate the " + nm20[rnd20] + " of " + nm21[rnd21] + " below them.";
	var name3 = nm22[rnd22] + nm23[rnd23] + " windows" + nm23b[rnd23b] + " are " + nm24[rnd24] + " by " + nm25[rnd25] + " colored the same " + nm12b[rnd12] + " as the banners. The curtains have been adorned with " + nm26[rnd26] + " and " + nm26[rnd26b] + "."; 
	
	var name4 = nm27[rnd27] + " throne of " + nm28[rnd28] + " sits " + nm29[rnd29] + " and is adjoined by " + nm30[rnd30] + " " + nm31[rnd31] + " seats for " + nm32[rnd32] + "."
	var name5 = "The throne is covered in " + nm33[rnd33] + " " + nm34[rnd34] + " and fixed on " + nm35[rnd35] + " is " + nm36[rnd36] + " " + nm37[rnd37] + ". The "  + nm38[rnd38] + " pillows are a " + nm39[rnd39] + " " + nm12b[rnd12] + " and these too have been adorned with " + nm40[rnd40] + " " + nm41[rnd41] + ".";

	var name6 = "Those " + nm42[rnd42] + " their royal highness can do so on the " + nm43[rnd43] + " " + nm44[rnd44] + " " + nm45[rnd45] + " benches, all of which are " + nm46[rnd46] + ". Those of higher standing can instead take seat in the " + nm47[rnd47] + " " + nm48[rnd48] + " " + nm49[rnd49] + ".";
	var br = [];
	for(i = 0; i < 8; i++){
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
	element.appendChild(document.createTextNode(name3));
	element.appendChild(br[3]);
	element.appendChild(br[4]);
	element.appendChild(document.createTextNode(name4));
	element.appendChild(br[5]);
	element.appendChild(document.createTextNode(name5));
	element.appendChild(br[6]);
	element.appendChild(br[7]);
	element.appendChild(document.createTextNode(name6));
	document.getElementById("placeholder").appendChild(element);
}	