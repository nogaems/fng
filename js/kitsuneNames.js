
function nameGen(type){
	var nm1 = ["a","ba","bai","be","bo","bu","chi","da","dai","ei","fu","ga","ge","gi","go","ha","hei","hi","ho","hyo","i","ie","jo","ju","ka","ke","kei","ki","ko","ku","kyu","ma","mi","mo","mu","na","nao","ni","no","o","ri","ro","ryo","ryu","sa","se","sei","shi","sho","shu","so","su","ta","te","tei","to","tsu","u","wa","ya","yo","yu"];
	var nm2 = ["bumi","buro","buru","chemon","chi","chiro","chiyo","chizo","dayu","deki","do","fu","fumi","gobei","goro","hari","haru","hide","hiko","hira","hiro","hisa","hito","ji","jio","jiro","juro","kado","kan","kao","karu","kazu","kei","ki","kichi","kin","kio","kira","ko","koto","kuchu","kudo","kumi","kuni","kusai","kushi","kusho","kuzo","mane","maro","masu","matsu","mei","miaki","michi","mio","mitsu","mon","mori","moru","moto","mune","nabu","naga","nari","nji","njiro","nkei","nko","nobu","nori","noru","noto","noye","npaku","nshiro","ntaro","nzo","rata","rei","ro","roji","roshi","ru","sada","sake","saku","sami","samu","sashi","sato","seki","setsu","shashi","shi","shige","shiko","shiro","sho","shushu","soshi","su","suke","suki","ta","tada","taka","tane","tari","taro","taru","toki","toku","tomo","tora","toshi","tsu","tsugu","tsumi","tsuna","tsune","tsuta","tsuyo","tzumi","wane","yaki","yasu","yori","yoshi","yuki","zane","zo","zuka","zuki","zuko","zuma","zumi","zumo","zushi"];
	var nm3 = ["a","ai","ba","be","chi","e","ei","fu","ge","ha","hai","hi","ho","i","jo","ka","kae","ki","ko","ku","ma","mae","me","mi","mo","mu","na","nao","ni","no","o","rai","rei","ri","ro","ru","sa","sai","se","shi","su","ta","te","to","tsu","u","wa","ya","yae","yo","yu"];
	var nm4 = ["bari","chi","chiha","chiho","chiko","cho","deko","doka","fumi","fuyu","gino","gusa","haru","hiro","ho","hoko","homi","hori","jiko","ka","kage","kako","kami","kane","kari","karu","kaze","ki","kichi","kiko","kina","kio","kira","ko","koto","kuko","kuma","kuro","kyo","maki","mako","mari","maya","meka","meko","mi","miho","mika","miki","miko","mina","miri","miya","mugi","na","nae","nai","nako","nami","natsu","neka","neko","niko","no","noka","nomi","noue","nu","nuko","nuye","nuyo","ra","rako","rante","rari","rea","ri","rika","riko","rime","rimi","rino","risa","risu","rize","ro","roe","roko","romi","roshi","ru","rui","ruka","ruko","rumi","sa","sae","sahi","saji","saki","sako","sami","samu","sano","sato","se","shi","shiko","shiyo","soko","sono","suka","suki","sumi","suzu","taba","tako","taru","to","tomi","tomo","tose","toshi","tsu","tsue","tsuka","tsuko","tsumi","tsune","tsuyo","yaka","yako","yame","yano","yeko","yo","yu","yuka","yuki","yuko","yume","yumi","yuri","zami","zu","zue","zuki","zuko","zumi","zuru","zusa"];
	var nm5 = ["Aki (Sparkle)","Akihiko (Bright Prince)","Akio (Glorious Hero)","Akira (Bright)","Dai (Great/Large)","Daichi (Great Wisdom)","Daisuke (Great Helper)","Eiju (Eternity)","Fumio (Literary Child)","Hajime (Beginning)","Haru (Sunlight)","Hideaki (Shining Excellence)","Hiro (Generous)","Hiroaki (Abundant Brightness)","Hiroshi (generous)","Hiroyuki (Abundant Happiness)","Hisashi (Long-lived)","Hisoka (Reserved Nature)","Hitoshi (Even Tempered)","Ichirou (First Son)","Isamu (Courage)","Isao (Honor)","Jun (Obedient)","Junichi (Obedient One)","Kaede (Maple)","Katsumi (Self Controlled)","Katsuo (Victorious Child)","Kazuhiro (Prosperous One)","Kei (Lucky)","Ken (Strong/Healthy)","Kenshin (Modest Truth)","Kenta (Strong/Healthy)","Kichiro (Lucky Son)","Kin (Gold)","Kiyoshi (Pure)","Kohaku (Amber)","Koichi (Light)","Kou (Happiness)","Kyou (Apricot)","Makoto (Sincere)","Mamoru (Protector)","Masa (Genuine)","Masaaki (True Brightness)","Masahiko (Just Prince)","Masanori (Model of Justice)","Masaru (Victorious)","Masayoshi (Flourishing Goodness)","Masayuki (Right Happiness)","Masumi (True Lucidity)","Michi (Pathway)","Michio (On the right path)","Minori (Truth)","Minoru (Truth)","Nao (Docile)","Noboru (Ascend)","Nobu (Faith)","Nobuyuki (Faithful Happiness)","Osamu (Disciplined)","Raiden (Thunder and Lightning)","Ryo (Brightness)","Ryota (Strong)","Ryuu (Dragon Spirit)","Sadao (Decisive)","Satoru (Wise)","Satoshi (Quick Witted)","Shigeru (Flourishing)","Shin (Humble)","Tadao (Loyal)","Takao (Respectful)","Takashi (Elevated)","Takayuki (Ascending)","Takehiko (Hero Prince)","Takeo (Valiant)","Takeshi (Warrior)","Takumi (Skilful)","Tamotsu (Defender)","Taro (Great Son)","Tatsuya (Assertive)","Teruo (Shining)","Tetsuo (Wise Hero)","Tomio (Treasured)","Toshi (Intelligent)","Toshiaki (Bright and Happy)","Toshio (Brilliant)","Toshiyuki (Clever and Happy)","Tsuneo (Eternal Hero)","Tsutomu (Worker)","Tsuyoshi (Brave)","Yasuhiro (Calm)","Yasuo (Healthy)","Yasuyoshi (Calm)","Yori (Public Servant)","Yoshi (Happy)","Yoshio (Good)","Yoshiro (Good)","Yoshito (Nice/Kind)","Yoshiyuki (Happy Way)","Yuichi (Brave)","Yuki (Snow)","Yukio (Happy Hero)","Yutaka (Wealthy)","Yuu (Superior)","Yuudai (Great Hero)"];
	var nm6 = ["Ai (Love)","Aika (Love Song)","Aiko (Love Child)","Aimi (Beloved Beauty)","Akane (Bright Red)","Akemi (Bright Beauty)","Aki (Sparkle/Bright)","Akiko (Bright Child)","Akira (Bright/Clear)","Arisu (Noble Type)","Asami (Morning Beauty)","Atsuko (Kind Child)","Aya (Colorful)","Ayaka (colorful Flower/Petal)","Ayako (Colorful Child)","Ayumi (Stroll)","Chiasa (Thousand Mornings)","Chie (Wisdom)","Chieko (Wise Child)","Chiharu (Thousand Springs)","Chinatsu (Thousand Summers)","Eiko (Long-lived Child)","Emi (Beautiful Blessing)","Emiko (Smiling Child)","Etsuko (Joyful Child)","Gina (Silvery)","Hana (Flower)","Hanako (Flower Child)","Haru (Spring/Sunlight)","Haruko (Spring Child)","Harumi (Spring Beauty)","Hikari (Radiance)","Hiro (Generous)","Hiroko (Generous Child)","Hiromi (Generous Beauty)","Hisako (Long-lived Child)","Hitomi ((Eye) Pupil)","Hoshi (Star)","Jun (Obedient)","Junko (Pure Child)","Kaede (Maple)","Kasumi (Mist)","Kayo (Beautiful)","Kazue (Harmonious)","Kazuko (Only Child)","Kazumi (Harminious Beauty)","Kei (Lucky)","Keiko (Lucky Child)","Kimi (Noble)","Kimiko (Noble Child)","Kin (Gold)","Kiyoko (Pure Child)","Kiyomi (Pure Beauty)","Ko (Light)","Kohaku (Amber)","Kou (Happiness)","Kyo (Apricot)","Kyoko (City Child)","Kyou (Apricot)","Kyuu (Nine)","Mai (Dance)","Maiko (Dancing Child)","Mana (Love)","Mariko (Village Child)","Masa (Elegant)","Masako (Elegant Child)","Masami (Elegant Beauty)","Megumi (Blessing)","Mi (Beauty)","Mika (Beautiful Fragrance)","Miki (Beautiful Princess)","Minako (Beautiful Child)","Minori (truth)","Misaki (Beautiful Bloom)","Mitsuko (Light Child)","Miwa (Harmony)","Miyako (Beautiful Night Child)","Miyuki (Beautiful Snow)","Momo (Peach)","Momoko (Peachy Child)","Moriko (Forest Child)","Nana (Seven)","Naoko (Docile Child)","Naomi (Superior Beauty)","Natsuko (Summer Child)","Natsumi (Summer Beauty)","Ran (Orchid)","Rei (Spirit)","Reiko (Lovely Child)","Ren (Water Lily)","Riko (Jasmine Child)","Rin (Cold)","Ryoko (Bright Child)","Sachiko (Happy Child)","Saki (Blossom)","Sakura (Cherry Blossom)","Sayuri (Lily)","Shizuka (Quiet)","Shizuko (Quiet Child)","Takako (Noble Child)","Takara (Treasure)","Teruko (Shining Child)","Tomoko (Friendly Child)","Toshiko (Clever Child)","Tsukiko (Moon Child)","Yasuko (Peaceful Child)","Yoko (Sunny Child)","Yoshi (Happy)","Yoshiko (Good Child)","Yuki (Snow)"];
	
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			if(i < 5){
				rnd = Math.random() * nm3.length | 0;
				rnd2 = Math.random() * nm4.length | 0;
				names = nm3[rnd] + nm4[rnd2];
				nm3.splice(rnd, 1);
				nm4.splice(rnd2, 1);
			}else{
				rnd = Math.random() * nm6.length | 0;
				names = nm6[rnd];
				nm6.splice(rnd, 1);
			}
		}else{
			if(i < 5){
				rnd = Math.random() * nm1.length | 0;
				rnd2 = Math.random() * nm2.length | 0;
				names = nm1[rnd] + nm2[rnd2];
				nm1.splice(rnd, 1);
				nm2.splice(rnd2, 1);
			}else{
				rnd = Math.random() * nm5.length | 0;
				names = nm5[rnd];
				nm5.splice(rnd, 1);
			}
		}
		nm3.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}