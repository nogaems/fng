var nm2 = ["us","ius","os","in","as"];
var nm3 = ["ia","ia","a","ia"];

function nameGen(type){
	var tp = type;
	var nm1 = ["Abder","Absyr","Abyd","Acast","Achat","Achel","Acher","Achil","Achl","Acris","Act","Adelph","Adm","Adon","Adr","Adras","Aeg","Aeol","Aggel","Alcin","Ald","Ambr","Amyc","Anast","Anat","Anc","And","Andr","Ant","Apost","Arc","Arg","Arist","Ars","Ast","Aster","Bacc","Bas","Bast","Bauc","Ceph","Cerb","Ces","Cet","Char","Cim","Cir","Corb","Cyr","Daem","Dam","Dar","Darr","Dem","Dim","Dion","Dor","Dun","Egid","Elefth","Eleuth","Endr","Eras","Ereb","Eum","Eur","Eust","Ev","Fan","Fed","Feodr","Gael","Gal","Gil","Gor","Greg","Haem","Hect","Hel","Ias","Ic","Idom","Ignat","Inach","Ivank","Jas","Kadm","Kir","Konst","Korud","Kost","Krat","Kyr","Lad","Lak","Land","Laz","Leand","Lich","Louk","Lox","Lyc","Maur","Ment","Mich","Myl","Nark","Nem","Nik","Nil","Nill","Ocn","Oen","Oenom","Or","Orthr","Pal","Panag","Par","Pell","Petr","Pil","Pirr","Preb","Prot","Rhod","Sav","Savv","Sim","Sot","Stam","Stavr","Stel","Sterg","Tak","Tal","Than","Thaum","Tim","Timm","Tit","Tod","Tol","Tox","Trit","Vas","Yan","Yann","Yor","Yrig","Zar","Zen","Zeph","Zolt"];

	var br = "";

	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm3.length | 0;
			names = nm1[rnd] + nm3[rnd2];
			nm1.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			names = nm1[rnd] + nm2[rnd2];
			nm1.splice(rnd, 1);
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