function nameGen(){
	var nm1 = ["A New View","About Time","Age of Vintage","Aged Goodness","Anecdotes","Another Man's Treasures","Another's Treasures","Antique Appeal","Antique Cache","Antique Cuties","Antique Hut","Antique Trove","Antiques and Artifacts","Antiquities","Authentic Antiquities","Beautiful Salvage","Blasts from the Past","Bought Again","Bygones","Checkered Pasts","Cozy Collectibles","Dinky and Dainty","Discoveries","Drab to Fab","Echoes of the Past","Established Goods","Focus of the Past","Focus on the Past","Forget Me Nots","Forgotten Furnishings","Fortunes in Time","Found in Time","From Oblivion","From Time Immemorial","Frozen in Time","General Goods","Good As New","Good Goods","Good Ol' Days","Hodge Podge Lodge","Honest Heirlooms","In-Of-Date","Joys For Forever","Junk Deluxe","Just in Time","Knick-knack Paddywhack Shack","Legends of Their Time","Little Collectibles","Little House of Trinkets","Live in the Past","Living Memories","Long Time No See","Lost and Found in Time","Matters of Time","Memory Lane","Miracles of the Past","Mod Life","Modern Memories","Modern Vintage","Needful Things","Odd Types","Old Gold","Old Roots","Old Stuff","Old and Bold","Oldies and Goldies","Once upon a time","One Time or Another","Out of the Attic","Pandora's Box","Paragon Prizes","Pass On the Past","Pass The Time","Past Caring","Past Meets Present","Past On","Past Over","Past Passed On","Past Repast","Pockets of Time","Precious Past","Precious Things","Presents for the Present","Presents of the Past","Preserved","Primes of the Past","Rags and Riches","Recent Memories","Recollect Them All","Recollectibles","Relics and Rarities","Relics and Riches","Relics of Time","Reliquary","Remains to be Seen","Remember","Remember This","Remember, Remember","Renewed Life","Renewed Memories","Retro Relics","Revered Relics","Revival","Salvage Garden","Secrets of the Past","Shared Memories","Stuff and Things","Sweet Memories","Taken for Granted","Tales Resold","Tales of the Past","Tales Retold","Tales Untold","Tests of Time","The Antiki-Wiki","The Antique Market","The Salvage Beast","The Shuffle of Things","The Time is Ripe","The Treasure Chest","The Treasure Trove","Things Past","Things of the Past","Thingymabobs","Time Honored","Time Not Forgotten","Time Recovered","Time of One's Life","Timeless Treasures","Timeless Trinkets","Times Remembered","Top Drawer Antiques","Treasures and Trinkets","Treasures of Time","Trinkets and Traditions","Trinkets of Time","Twosided","Utter Clutter","Vagabond Vendor","Vestiges of the Past","Vintage","Vintage Baby","Vintage Treasures","Vintage Vogue","Vintage Wares","Warm Wares","Wayward Wealths","Wealth of Time","Well of a Time","Whispers of the Past","Wonders of the Past"];
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
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