var nm1 = ["Abandon","Angel","Angel's ","Anger","Aurora ","Bad","Bare","Barren","Barren ","Big","Bitter","Black","Blank","Bleak","Blind","Bliss","Bold","Bone","Boulder","Brave","Break","Broken","Bronze","Bruise","Bull","Bull's ","Buzzard's ","Cattle","Clear","Clear ","Coal","Copper","Copper ","Court","Coyote's ","Craze","Crazy","Crime","Crimson","Cripple ","Crook","Crooked","Crow's ","Cruel","Cruelty ","Dark","Dead","Dead Man's ","Death's ","Defiant ","Demon","Demon's ","Desert","Desert ","Desolation ","Devil","Devil's ","Dodge","Dread","Dry","Dry ","Dull","Dust","Dusty ","Elder","Evil ","Evil's ","Fair","False ","Far","Farm","Filth","Flat","Forsaken ","Frail","Free","Freedom ","Ghost","Ghost's ","Giant's ","Glum","Gold","Golden","Grand","Grand ","Grave","Grave ","Gray","Greed","Grim","Grime","Grind","Grub","Gun","Harmony ","High","Hell","Hope's ","Idle","Imp","Infernal ","Iron","Jagged","Last ","Lawless ","Lead","Light","Limbo ","Limp","Little","Little ","Living","Lone ","Lonely ","Long","Lords","Lost","Lost ","Lost Hope's ","Low","Marrow","Meek","Mellow ","Mud","Narrow ","New ","Numb","Oat","Obsidian ","Old ","Onyx","Over","Ox","Pale","Phantom","Pistol","Plain","Plain ","Pride ","Prospector ","Prospector's ","Proud","Pure","Purgatory ","Purity ","Quick","Rag","Ragged","Ragged ","Rapid","Rattle","Red","Rich","Rich ","Rot","Ruby ","Rust","Rusty ","Sand","Sandy ","Scorn","Scorpion","Scorpion's ","Serenity ","Serpent","Serpent's ","Shade ","Shadow","Shady ","Shallow ","Short","Silent ","Silver","Sin","Skeleton ","Skinny ","Skull","Slim","Slow","Smooth ","Snake","Sneak","Soft","Sore","Sour","Stag","Stale","Stark","Stark ","Steel","Steep","Stiff","Stiff's ","Storm","Strong","Sunny","Swift","Swift ","Talon","Talon's ","Tame","Tan","Thin","Thorn","Thunder","Tight","Tomb","Torn","Tucker","Twin ","Vain","Vapid","Vast","Venom","Vicious ","Violence ","Violent ","Warm","Warp","Whisper","White","Wide","Wild","Wild ","Willow","Windy ","Wolf","Wolf's ","Wrath","Wrath ","Wry","Yellow"];
var nm2 = ["alley","bank","banks","bend","brook","burg","butte","canyon","chapel","city","creak","creek","cross","edge","field","flats","ford","fort","gate","gulch","hallow","hill","hollow","lake","landing","mesa","mountain","pass","peak","stream","branch","ridge","bluff","dune","downs","range","summit","rise","cliff","crag","scar","stand","gorge","vale","gorge","glen","dale","snag","tusk","howl","bellow","peaks","plains","point","port","post","reach","ridge","river","rock","roost","run","spring","springs","stead","stone","tooth","town","trail","trails","ville","water","wood","worth"];
var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}