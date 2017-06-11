__all__ = ['quechuaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Ñust’A'), Js('Ñust’Awillka'), Js("Ñust'a"), Js('Achik'), Js('Achikilla'), Js('Achiq'), Js('Achiyaku'), Js('Aklla'), Js('Akllasisa'), Js('Akllasumaq'), Js('Aliqora'), Js('Alliyma'), Js('Asiri'), Js('Asiriyaku'), Js('Auka'), Js('Aukasisa'), Js('Awak'), Js('Awank’Ay'), Js('Awaq'), Js('Awasiyaku'), Js('Awqa'), Js('Awqasisa'), Js('Cantuta'), Js('Ch’Aska'), Js('Ch’Ayña'), Js('Ch’Ayna'), Js('Chami'), Js('Chimpu'), Js('Chinbo'), Js('Chinpo'), Js('Chinpokusi'), Js('Chinposumak'), Js('Chinpourma'), Js('Chinpu’Urma'), Js('Chinpu'), Js('Chinpukilla'), Js('Chinpukusi'), Js('Chinpusumaq'), Js('Choke'), Js('Chuki'), Js('Chukillanthu'), Js('Chuqi'), Js('Hamk’A'), Js('Hawka'), Js('Haylli'), Js('Huch’Uy'), Js('Huch’Uykilla'), Js('Huch’Uykoya'), Js('Huch’Uysisa'), Js('Ilin'), Js('Illa'), Js('Illari'), Js('Illarisisa'), Js('Illarit’Ika'), Js('Illary'), Js('Illi'), Js('Imasumaq'), Js('Inka'), Js('Inkasisa'), Js('Inkill'), Js('Inkillay'), Js('Izhi'), Js('Jaylli'), Js('K’Antu'), Js('K’Uychi'), Js('K’antu'), Js('Karwasisa'), Js('Kayara'), Js('Khallwa'), Js('Khuyak'), Js('Khuyana'), Js('Khuyaq'), Js('Killa'), Js('Killa '), Js('Killari'), Js('Killasisa '), Js('Killasumaq'), Js('Killay'), Js('Kiwa'), Js('Koka'), Js('Kokka'), Js('Koya'), Js('Koyakusi'), Js('Koyasumaq'), Js('Kuka'), Js('Kukuri'), Js('Kukuyu'), Js('Kusi’Inkillay'), Js('Kusi'), Js('Kusichinpu'), Js('Kusimayu'), Js('Kusiqoyllur'), Js('Kusiquyllur'), Js('Kusirimay'), Js('Kusiyaya'), Js('Kuymi'), Js('Llaksa'), Js('Llasha'), Js('Lliu'), Js('Lliukilla'), Js('Lliusisa'), Js('Lliw'), Js('Lliwkilla'), Js('Lliwsisa'), Js('Loria'), Js('Loriana'), Js('Mama’Achiq'), Js('Mamaachik'), Js('Mamahamk’A'), Js('Mamak'), Js('Mamakoka'), Js('Mamakuka'), Js('Mamaoqllo'), Js('Mamaq'), Js('Mamaqhawa'), Js('Mamaqora'), Js('Mamaqura'), Js('Mamaruntu'), Js('Mamauqllu'), Js('Maysumak'), Js('Maysumaq'), Js('Mayu'), Js('Mayua'), Js('Mayuasiri'), Js('Maywa'), Js('Michik '), Js('Michiq'), Js('Misk’I '), Js('Misk’Iwayra'), Js('Nayarak'), Js('Nayaraq'), Js('Nina'), Js('Ninapajcha'), Js('Ninapakcha'), Js('Ninapaqari'), Js('Ninasisa'), Js('Ninat’Ika'), Js('Nuna'), Js('Okllo'), Js('Oqllo'), Js('P’Anqa'), Js('Pacha'), Js('Pachakusi'), Js('Palla'), Js('Paqari'), Js('Pariwana'), Js('Parwa'), Js('Pawqarqury'), Js('Phajcha'), Js('Phakcha'), Js('Phakchay'), Js('Phallcha'), Js('Phaway'), Js('Phichitanka'), Js('Phuyu'), Js('Phuyuqhawa'), Js('Pillkosisa'), Js('Pillkusisa'), Js('Pujyu'), Js('Pukyu'), Js('Puquy'), Js('Puquykilla'), Js('Qhatuk'), Js('Qhatuq'), Js('Qhawa'), Js('Qhispe'), Js('Qhispi'), Js('Qhispisisa'), Js('Qhora'), Js('Qijyusisa'), Js('Qikyusisa'), Js('Qillqa'), Js('Qispi'), Js('Qiwa'), Js('Qocha'), Js('Qollorit’I'), Js('Qollqe'), Js('Qora'), Js('Qoraokllo'), Js('Qori'), Js('Qorichullpi'), Js('Qorioqllo'), Js('Qoriqoyllur'), Js('Qorisisa'), Js('Qorit’Ika'), Js('Qoriurma'), Js('Qoriwayra'), Js('Qoya'), Js('Qoyllor'), Js('Qoyllur'), Js('Qucha'), Js('Qullqi'), Js('Qura'), Js('Quraoqllo'), Js('Quri'), Js('Qurichullpi'), Js('Quriquyllur'), Js('Qurisisa'), Js('Qurit’Ika'), Js('Quriuqllu'), Js('Quriurma'), Js('Quriwayra'), Js('Quyllur'), Js('Quyllurit’I'), Js('Raua'), Js('Rawa'), Js('Rawaoqllo'), Js('Rimak'), Js('Rimaq'), Js('Sach’A'), Js('Sach’Asisa'), Js('Sachat’Ika'), Js('Sami'), Js('Saya'), Js('Saywa'), Js('Shaya'), Js('Shulla'), Js('Sisa'), Js('Siyaya'), Js('Sumailla'), Js('Sumailli'), Js('Sumaizhi'), Js('Sumak'), Js('Sumaq'), Js('Sumat’Ika'), Js('Suri'), Js('Suyana'), Js('T’Ika'), Js('Taki’Illareq'), Js('Taki’Illariq'), Js('Taki'), Js('Talla'), Js('Tamaya'), Js('Tamia'), Js('Tamiasisa'), Js('Tamya'), Js('Tamyasisa'), Js('Tanitani'), Js('Taruka'), Js('Thani'), Js('Tica'), Js('Timta'), Js('Ttika'), Js('Tuta'), Js('Tutayan'), Js('Umiña'), Js('Uqllu'), Js('Urma'), Js('Urpi'), Js('Urpikusi'), Js('Urpillay'), Js('Urpiyanay'), Js('Urpiyurak'), Js('Urpiyuraq'), Js('Wakchilla'), Js('Waqar'), Js('Warawa'), Js('Wayanay'), Js('Wayanaysi'), Js('Waylla'), Js('Wayna'), Js('Wayra'), Js('Wayta'), Js('Waytamayu'), Js('Willka'), Js('Yachay'), Js('Yaku'), Js('Yakuy'), Js('Yana'), Js('Yanakilla'), Js('Yanakoya'), Js('Yanapoma'), Js('Yanapuma'), Js('Yanaqoyllur'), Js('Yanaquyllur'), Js('Yanawayta'), Js('Yanay'), Js('Ylin'), Js('Ylla'), Js('Ymasumak'), Js('Ynkill'), Js('Yori'), Js('Yoria'), Js('Yoriana'), Js('Yurak'), Js('Yuraq'), Js('Yuri'), Js('Yuria'), Js('Yuriana')]))
    var.put('nm2', Js([Js('Ñaupaq'), Js('Ñaupari'), Js('Ñawpaq'), Js('Ñawpari'), Js('Ñawqe'), Js('Ñawqi'), Js('Achik'), Js('Achiq'), Js('Ackonqhawaq'), Js('Akapana'), Js('Amaru'), Js('Amaruqhispe'), Js('Amarutopak'), Js('Amarutupaq'), Js('Amaruyupanki'), Js('Anka'), Js('Anku'), Js('Ankuwillka'), Js('Anqasmayu'), Js('Anqaspoma'), Js('Anqaspuma'), Js('Anta'), Js('Antawaylla'), Js('Antay'), Js('Anti'), Js('Antininan'), Js('Anyaypoma'), Js('Anyaypuma'), Js('Apo'), Js('Apu'), Js('Apuk’Achi'), Js('Apumayta'), Js('Apuqateqill'), Js('Apuqatiqill'), Js('Apurimaq'), Js('Apuyurak'), Js('Apuyuraq'), Js('Asto'), Js('Astu'), Js('Astuwaraka'), Js('Atau'), Js('Atauchi'), Js('Ataw’Anka'), Js('Ataw'), Js('Atawallpa'), Js('Atik'), Js('Atiq'), Js('Atoq'), Js('Atoqwaman'), Js('Atuq'), Js('Auk’A'), Js('Auki'), Js('Aukiyupanki'), Js('Awki'), Js('Awkipuma'), Js('Awkitupaq'), Js('Awkiyupanki'), Js('Awqa'), Js('Ayar'), Js('Ch’Uya'), Js('Chaupi'), Js('Chawar'), Js('Chawpi'), Js('Chikan'), Js('Choke'), Js('Chuki'), Js('Chukilla'), Js('Chukiwaman'), Js('Chukiwillka'), Js('Chun'), Js('Chuqi'), Js('Chusku'), Js('Hakan'), Js('Hakanpoma'), Js('Hakanpuma'), Js('Hastu'), Js('Hatuntupaq'), Js('Huksonjo'), Js('Huksunk’U'), Js('Illapha'), Js('Illapoma'), Js('Illapu'), Js('Illapuma'), Js('Illateqsi'), Js('Illatiksi'), Js('Illayuk'), Js('Illayuq'), Js('Inka'), Js('Inkaurko'), Js('Inkaurqu'), Js('Inti’Illapha'), Js('Inti'), Js('Intiawki'), Js('Intichurin'), Js('Intiwaman'), Js('Iskay'), Js('Iskaywari'), Js('K’Achi'), Js('K’Aywa'), Js('K’Enti'), Js('K’Inti'), Js('K’Uyuchi'), Js('K’Uyuk'), Js('K’Uyukusi'), Js('K’Uyuq'), Js('Karwamayu'), Js('Kashayawri'), Js('Khapaj'), Js('Kichwasamin'), Js('Killinchu'), Js('Kumya'), Js('Kunak'), Js('Kunaq'), Js('Kuntur'), Js('Kunturchawa'), Js('Kunturkanki'), Js('Kunturpoma'), Js('Kunturpuma'), Js('Kunturumi'), Js('Kunturwari'), Js('Kuri'), Js('Kusiñawi'), Js('Kusi'), Js('Kusipoma'), Js('Kusipuma'), Js('Kusirimachi'), Js('Kusiwallpa'), Js('Kusiwaman'), Js('Kusiyupanki'), Js('Libiak'), Js('Llaksa'), Js('Llanke'), Js('Llanqi'), Js('Llashapoma'), Js('Llashapuma'), Js('Llipiak'), Js('Llipiaq'), Js('Lliuyaq'), Js('Lliwyak'), Js('Lliwyaq'), Js('Lloqe'), Js('Lloqeyupanki'), Js('Lluqi'), Js('Lluqiyupanki'), Js('Mallki'), Js('Mallko'), Js('Mallku'), Js('Mallqu'), Js('Manko'), Js('Mayta'), Js('Maytaqhapaq'), Js('Mayua'), Js('Maywa'), Js('Mullu'), Js('Ninan'), Js('Ninankuyuchi'), Js('Ninaqolla'), Js('Ninawari'), Js('Ninawillka'), Js('Ollantay'), Js('Otoronqo'), Js('Pachakutek'), Js('Pachakutiq'), Js('Panti'), Js('Pariwana'), Js('Pauk’Ar'), Js('Pawk’Artupak'), Js('Pawq’Ar'), Js('Pawq’Artupaq'), Js('Phawak'), Js('Phawaq'), Js('Phawaqwallpa'), Js('Pichiu'), Js('Pichiw'), Js('Pikichaki'), Js('Pillkomayu'), Js('Pillku'), Js('Pillkumayu'), Js('Pillqo'), Js('Pillqu'), Js('Poma'), Js('Pomakana'), Js('Pomalloqe'), Js('Pomaqhawa'), Js('Pomawari'), Js('Pomawillka'), Js('Pomayauri'), Js('Puma'), Js('Pumakana'), Js('Pumalluqi'), Js('Pumaqhawa'), Js('Pumasonjo'), Js('Pumasunk’U'), Js('Pumawari'), Js('Pumawillka'), Js('Pumayawri'), Js('Purik'), Js('Puriq'), Js('Pushak'), Js('Pushaq'), Js('Q’Uñi'), Js('Q’Uñiraya'), Js('Qateqil'), Js('Qatiqil'), Js('Qatuilla'), Js('Qaylla'), Js('Qhapaq'), Js('Qhapaqwari'), Js('Qhapaqyupanki'), Js('Qhaqya'), Js('Qhari'), Js('Qhawachi'), Js('Qhawak'), Js('Qhawana'), Js('Qhawaq'), Js('Qhespi'), Js('Qhispe'), Js('Qhispi'), Js('Qhispiyupanki'), Js('Qillilliku'), Js('Qolla'), Js('Qollana'), Js('Qollaqhapaq'), Js('Qollatupak'), Js('Qollqe'), Js('Qollqiyok'), Js('Qoni'), Js('Qoniraya'), Js('Qoriñawi'), Js('Qori'), Js('Qoripoma'), Js('Qoriwaman'), Js('Quichuasamin'), Js('Qulla'), Js('Qullana'), Js('Qullaqhapaq'), Js('Qullatupaq'), Js('Qullqi'), Js('Qullqiyuq'), Js('Quriñawi'), Js('Quri'), Js('Quripuma'), Js('Quriwaman'), Js('Rauraq'), Js('Rawrak'), Js('Rawraq'), Js('Raymi'), Js('Rimachi'), Js('Rimak'), Js('Rimaq'), Js('Rumiñawi'), Js('Rumi'), Js('Rumimaki'), Js('Rumisonjo'), Js('Rumisunk’U'), Js('Runak’Oto'), Js('Runak’Utu'), Js('Runto'), Js('Runtu'), Js('Ruphay'), Js("Ruq'a"), Js('Sach’A'), Js('Sami'), Js('Samin'), Js('Sapay'), Js('Sayani'), Js('Sayarumi'), Js('Sayre'), Js('Sayri'), Js('Sayritupaq'), Js('Shañu'), Js('Shullka'), Js('Sinche'), Js('Sinchi'), Js('Sinchipuma'), Js('Sinchiroka'), Js('Sokso'), Js('Somak'), Js('Sonjok'), Js('Sonjoyoq'), Js('Sonk’O'), Js('Sonk’Oyoq'), Js('Suhay'), Js('Suksu'), Js('Sullkawaman'), Js('Sumainka'), Js('Sumaq'), Js('Sunk’U'), Js('Sunk’Uyuq'), Js('Suri'), Js('T’It’O'), Js('T’It’Oatauchi'), Js('T’It’U'), Js('T’It’Uatawchi'), Js('Takiri'), Js('Tawa'), Js('Tawaqhapaq'), Js('Thupa/ Topa'), Js('Tinkipoma'), Js('Tinkupuma'), Js('Tupa'), Js('Tupak'), Js('Tupakamaru'), Js('Tupakusi'), Js('Tupaq'), Js('Tupaqamaru'), Js('Tupaqhapaq'), Js('Tupaqyupanki'), Js('Tupayupanki'), Js('Uchu'), Js('Ukumari'), Js('Ullanta'), Js('Ullantay'), Js('Unay'), Js('Urk’O'), Js('Urqu'), Js('Urquqolla'), Js('Usqo'), Js('Usqowillka'), Js('Usqu'), Js('Usquwillka'), Js('Usuy'), Js('Uturunku'), Js('Uturunqu'), Js('Uturunqu Achachi'), Js('Wallpa'), Js('Wallpaya'), Js('Waman'), Js('Wamanachachi'), Js('Wamanchawa'), Js('Wamanchuri'), Js('Wamanpuma'), Js('Wamanqhapaq'), Js('Wamantupaq'), Js('Wamanwarank’A'), Js('Wamanyana'), Js('Wamanyuraq'), Js('Wamay'), Js('Wanka'), Js('Wanqar'), Js('Waqralla'), Js('Wari'), Js('Wariruna'), Js('Warit’It’O'), Js('Warit’It’U'), Js('Waskhar'), Js('Wawal'), Js('Wayasamin'), Js('Wayaw'), Js('Wayna'), Js('Waynaqhapaq'), Js('Waynarimaq'), Js('Waynay'), Js('Wayra'), Js('Waywa'), Js('Willak'), Js('Willaq'), Js('Willka'), Js('Willkawaman'), Js('Wiraqocha'), Js('Wiraqucha'), Js('Wisa'), Js('Yaku'), Js('Yanamayu'), Js('Yauri'), Js('Yawar'), Js('Yawarpuma'), Js('Yawarwaqaq'), Js('Yawri'), Js('Yllapa'), Js('Ynti'), Js('Yupanki'), Js('Yurak'), Js('Yuraq')]))
    var.put('nm3', Js([Js('Ñaña'), Js('Ñaccha'), Js('Ñahuis'), Js('Ñaupari'), Js('Achachau'), Js('Alca'), Js('Allauca'), Js('Allcca'), Js('Allccarima'), Js('Amaru'), Js('Anhuaman'), Js('Arotinco'), Js('Asto'), Js('Aucapuma'), Js('Auquitayasi'), Js('Cacha'), Js('Cachi'), Js('Cahua'), Js('Caipa'), Js('Callañaupa'), Js('Cancha'), Js('Canchasto'), Js('Canchon'), Js('Carhuanina'), Js('Carihuasari'), Js('Ccahua'), Js('Ccahuantico'), Js('Ccarhuarupay'), Js('Ccasani'), Js('Ccolque'), Js('Ccora'), Js('Chakana'), Js('Chalco'), Js('Chamba'), Js('Chambi'), Js('Chanca'), Js('Chaupin'), Js('Chipana'), Js('Choque'), Js('Chuquimango'), Js('Chuquipoma'), Js('Cocha'), Js('Colquehuanca'), Js('Conde'), Js('Condor'), Js('Condori'), Js('Curichimba'), Js('Cusi'), Js('Cusipuma'), Js('Cuya'), Js('Guañuna'), Js('Guaman'), Js('Huaccha'), Js('Huachalla'), Js('Hualla'), Js('Huaman'), Js('Huamanchagua'), Js('Huamancuri'), Js('Huamanga'), Js('Huamani'), Js('Huanca'), Js('Huancahuari'), Js('Huaricancha'), Js('Huayanay'), Js('Huayhua'), Js('Huayta'), Js('Humahuaca'), Js('Huyhua'), Js('Inka'), Js('Jaillita'), Js('Llactahuaman'), Js('Llancay'), Js('Macavilca'), Js('Mallma'), Js('Mallqui'), Js('Malqui'), Js('Manco'), Js('Maygua'), Js('Mayhuasca'), Js('Michi'), Js('Motocanchi'), Js('Nina'), Js('Ninahuamán'), Js('Olaya'), Js('Orccosupa'), Js('Paccsi'), Js('Pachari'), Js('Pari'), Js('Paucar'), Js('Paucarchuco'), Js('Pillihuaman'), Js('Pillpe'), Js('Pinchi'), Js('Pinto'), Js('Polloqueri'), Js('Pumacaja'), Js('Pumasupa'), Js('Qori'), Js('Quelka'), Js('Quichca'), Js('Quihue'), Js('Quillahuaman'), Js('Quispe'), Js('Quisuyupanqui'), Js('Rimayhuaman'), Js('Sayritupac'), Js('Sianquiz'), Js('Sihui'), Js('Soncco'), Js('Sulca'), Js('Surichaqui'), Js('Ticahuanca'), Js('Ticllacuri'), Js('Tomayro'), Js('Ucharima'), Js('Uchuypoma'), Js('Usucachi'), Js('Vilca'), Js('Yacupaico')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('nm3').callprop('splice', var.get('rnd3'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
quechuaNames = var.to_python()