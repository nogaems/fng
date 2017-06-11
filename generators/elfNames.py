__all__ = ['elfNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('nameLast', (var.get('nm3').get(var.get('rnd2'))+var.get('nm4').get(var.get('rnd3'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nameLast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nameLast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Mnementh'), Js('Wirenth'), Js('Feyrith'), Js('Sataleeti'), Js('Leofrick'), Js('Abarat'), Js('Adamar'), Js('Adorellan'), Js('Adresin'), Js('Aelrindel'), Js('Aerendyl'), Js('Aeson'), Js('Afamrail'), Js('Agandaur'), Js('Agis'), Js('Aias'), Js('Aiduin'), Js('Aien'), Js('Ailas'), Js('Ailduin'), Js('Ailen'), Js('Ailluin'), Js('Ailmar'), Js('Ailmer'), Js('Ailmon'), Js('Ailre'), Js('Ailred'), Js('Ailuin'), Js('Ailwin'), Js('Aimar'), Js('Aimer'), Js('Aimon'), Js('Airdan'), Js('Aire'), Js('Aired'), Js('Aithlin'), Js('Aiwin'), Js('Akkar'), Js('Alabyran'), Js('Alaion'), Js('Alas'), Js('Albondiel'), Js('Alduin'), Js('Alen'), Js('Alinar'), Js('Alluin'), Js('Almar'), Js('Almer'), Js('Almon'), Js('Alok'), Js('Alosrin'), Js('Alre'), Js('Alred'), Js('Althidon'), Js('Alwin'), Js('Amrynn'), Js('Andrathath'), Js('Anfalen'), Js('Anlyth'), Js('Aolis'), Js('Aquilan'), Js('Arathorn'), Js('Arbane'), Js('Arbelladon'), Js('Ardreth'), Js('Ardryll'), Js('Arl'), Js('Arlen'), Js('Arun'), Js('Ascal'), Js('Athtar'), Js('Aubron'), Js('Aumanas'), Js('Aumrauth'), Js('Avourel'), Js('Ayas'), Js('Ayduin'), Js('Ayen'), Js('Ayluin'), Js('Aymar'), Js('Aymer'), Js('Aymon'), Js('Ayre'), Js('Ayred'), Js('Aywin'), Js('Belanor'), Js('Beldroth'), Js('Bellas'), Js('Beluar'), Js('Biafyndar'), Js('Bialaer'), Js('Braern'), Js('Cailu'), Js('Cameron'), Js('Camus'), Js('Castien'), Js('Chathanglas'), Js('Cheyrth'), Js('Cluhurach'), Js('Cluym'), Js('Cohnal'), Js('Conall'), Js('Connak'), Js('Cornaith'), Js('Corym'), Js('Cyran'), Js('Dain'), Js('Dakath'), Js('Dalyor'), Js('Darcassan'), Js('Darfin'), Js('Darthoridan'), Js('Darunia'), Js('Deldrach'), Js('Delmuth'), Js('Delsaran'), Js('Devdan'), Js('Drannor'), Js('Druindar'), Js('Durlan'), Js('Durothil'), Js('Dyffros'), Js('Edwyrd'), Js('Edyrm'), Js('Ehlark'), Js('Ehrendil'), Js('Eilauver'), Js('Elnaril'), Js('Elaith'), Js('Elandorr'), Js('Elas'), Js('Elashor'), Js('Elbauthin'), Js('Eldaernth'), Js('Eldar'), Js('Eldrin'), Js('Elduin'), Js('Elen'), Js('Elephon'), Js('Elidyr'), Js('Elion'), Js('Elkhazel'), Js('Ellisar'), Js('Elluin'), Js('Elmar'), Js('Elmer'), Js('Elmon'), Js('Elorshin'), Js('Elpaerae'), Js('Elre'), Js('Elred'), Js('Eltaor'), Js('Elwin'), Js('Elyon'), Js('Emmyth'), Js('Entrydal'), Js('Erendriel'), Js('Erglareo'), Js('Eriladar'), Js('Erlan'), Js('Erlathan'), Js('Eroan'), Js('Erolith'), Js('Eschallus'), Js('Estelar'), Js('Ethlando'), Js('Ettrian'), Js('Evindal'), Js('Eyrynnhv'), Js('Faelar'), Js('Faelyn'), Js('Faeranduil'), Js('Falael'), Js('Felaern'), Js('Fenian'), Js('Feno'), Js('Fhaornik'), Js('Filarion'), Js('Filvendor'), Js('Filverel'), Js('Flardryn'), Js('Flinar'), Js('Folas'), Js('Folduin'), Js('Folen'), Js('Folluin'), Js('Folmar'), Js('Folmer'), Js('Folmon'), Js('Folre'), Js('Folred'), Js('Folwin'), Js('Foxfire'), Js('Fylson'), Js('Gaeleath'), Js('Gaelin'), Js('Galaeron'), Js('Galan'), Js('Galather'), Js('Ganamede'), Js('Gantar'), Js('Garrik'), Js('Garynnon'), Js('Giullio'), Js('Glanduil'), Js('Glarald'), Js('Glorandal'), Js('Goll'), Js('Goras'), Js('Gorduin'), Js('Goren'), Js('Gorluin'), Js('Gormar'), Js('Gormer'), Js('Gormon'), Js('Gorre'), Js('Gorred'), Js('Gorwin'), Js('Grathgor'), Js('Haemir'), Js('Hagas'), Js('Hagduin'), Js('Hagen'), Js('Hagluin'), Js('Hagmar'), Js('Hagmer'), Js('Hagre'), Js('Hagred'), Js('Hagwin'), Js('Haladavar'), Js('Halafarin'), Js('Halamar'), Js('Haldir'), Js('Haldreithen'), Js('Halflar'), Js('Halueth'), Js('Halueve'), Js('Hamon'), Js('Haryk'), Js('Hastos'), Js('Hatharal'), Js('Hoccar'), Js('Horith'), Js('Hubyr'), Js('Iefyr'), Js('Ievos'), Js('Ilbryn'), Js('Ilimitar'), Js('Iliphar'), Js('Illianaro'), Js('Illithor'), Js('Illitran'), Js('Ilphas'), Js('Ilrune'), Js('Ilthuryn'), Js('Inchel'), Js('Inialos'), Js('Injros'), Js('Intevar'), Js('Iolas'), Js('Iolrath'), Js('Itham'), Js('Ivsaar'), Js('Ivlisar'), Js('Ivran'), Js('Iymbryl'), Js('Iyrandrar'), Js('Jandar'), Js('Jannalor'), Js('Jaonos'), Js('Jassin'), Js('Jhaan'), Js('Jhaartael'), Js('Jhaeros'), Js('Jharak'), Js('Jharym'), Js('Jonik'), Js('Jorildyn'), Js('Josidiah'), Js('Juppar'), Js('Kailu'), Js('Katar'), Js('Katyr'), Js('Keletheryl'), Js('Kellam'), Js('Kelvhan'), Js('Kendel'), Js('Kerym'), Js('Keryth'), Js('Kesefehon'), Js('Kharis'), Js('Khatar'), Js('Khidell'), Js('Khiiral'), Js('Khilseith'), Js('Khuumal'), Js('Khyrmn'), Js('Kieran'), Js('Kiirion'), Js('Kindroth'), Js('Kivessin'), Js('Kiyuigh'), Js('Klaern'), Js('Kolvar'), Js('Kuornos'), Js('Kuskyn'), Js('Kymil'), Js('Kyrenic'), Js('Kyrtaar'), Js('Laeroth'), Js('Lafarallin'), Js('Lamruil'), Js('Laosx'), Js('Larongar'), Js('Larrel'), Js('Lashul'), Js('Lathai'), Js('Lathlaeril'), Js('Leojym'), Js('Lhoris'), Js('Lianthorn'), Js('Llarm'), Js('Llewellenar'), Js('Llombaerth'), Js('Lorsan'), Js('Luirlan'), Js('Luthais'), Js('Luvon'), Js('Lyari'), Js('Lyklor'), Js('Lysanthir'), Js('Maeraddyth'), Js('Maeral'), Js('Maiele'), Js('Malgath'), Js('Malon'), Js('Mardeiym'), Js('Marikoth'), Js('Marlevaur'), Js('Melandrach'), Js('Merellien'), Js('Merith'), Js('Methild'), Js('Mhaenal'), Js("Mi'tilarro"), Js('Mihangyl'), Js('Miirphys'), Js('Mirthal'), Js('Mlartlar'), Js('Molonym'), Js('Molostroi'), Js('Montagor'), Js('Morgan'), Js('Morthil'), Js('Myrddin'), Js('Myriil'), Js('Myrin'), Js('Mythanthar'), Js('Naertho'), Js('Naeryndam'), Js('Naesala'), Js('Narbeth'), Js('Nardual'), Js('Nasir'), Js('Navarre'), Js('Nelaeryn'), Js('Neldor'), Js('Nesterin'), Js('Nevarth'), Js('Nhamashal'), Js('Nieven'), Js('Nindrol'), Js('Ninleyn'), Js('Ninthalor'), Js('Nlossae'), Js('Nopos'), Js('Nremyn'), Js('Nuvian'), Js('Nylian'), Js('Nym'), Js('Nyvorlas'), Js('Oacenth'), Js('Oenel'), Js('Ohmbryn'), Js('Olaurae'), Js('Onas'), Js('Oncith'), Js('Onvyr'), Js('Orist'), Js('Orlpar'), Js('Orndacil'), Js('Ornthalas'), Js('Orrian'), Js('Orym'), Js('Oslarelar'), Js('Otaehryn'), Js('Othorion'), Js('Paeral'), Js('Paeris'), Js('Pelleas'), Js('Phaendar'), Js('Pharom'), Js('Phraan'), Js('Pirphal'), Js('Pleufan'), Js('Purtham'), Js('Pyrder'), Js('Pyrravym'), Js('Pywaln'), Js('Qildor'), Js('Quynn'), Js('Raeranthur'), Js('Raibyr'), Js('Ralikanthae'), Js('Ralnor'), Js('Rathal'), Js('Raunaeril'), Js('Rauvelore'), Js('Reluraun'), Js('Reluvethel'), Js('Rennyn'), Js('Reptar'), Js('Respen'), Js("Rhaac'var"), Js('Rhalyf'), Js('Rhangyl'), Js('Rhistel'), Js('Rhothomir'), Js('Rhys'), Js('Rilitar'), Js('Riluaneth'), Js('Rolim'), Js('Rothilion'), Js('Ruardh'), Js('Ruehar'), Js('Ruith'), Js('Ruvaen'), Js('Ruven'), Js('Ruvyn'), Js('Rychell'), Js('Rydel'), Js('Ryfon'), Js('Ryo'), Js('Ryul'), Js('Saelethil'), Js('Saevel'), Js('Saleh'), Js('Samblar'), Js('Sandevv'), Js('Seiveril'), Js('Selanlar'), Js('Selgauth'), Js('Sharian'), Js('Shaundyl'), Js('Shihon'), Js('Shyrrik'), Js('Siirist'), Js('Silvyr'), Js('Simimar'), Js('Sinaht'), Js('Skalanis'), Js('Sontar'), Js('Sorfildor'), Js('Sudryl'), Js('Sundamar'), Js('Sylvar'), Js('Symkalr'), Js('Sythaeryn'), Js('Taanyth'), Js('Taegen'), Js('Taenaran'), Js('Taeral'), Js('Taerntym'), Js('Taleisin'), Js('Tamnaeuth'), Js('Tanithil'), Js('Tannivh'), Js('Tannyll'), Js('Tanyl'), Js('Taranath'), Js('Tarathiel'), Js('Taredd'), Js('Tarron'), Js('Tasar'), Js('Tassarion'), Js('Tathaln'), Js('Tehlmar'), Js('Teirist'), Js('Thalanil'), Js('Thallan'), Js('Theodas'), Js('Theodemar'), Js('Theoden'), Js('Theodluin'), Js('Theodmer'), Js('Theodmon'), Js('Theodre'), Js('Theodred'), Js('Theoduin'), Js('Theodwin'), Js('Thurdan'), Js('Tiarshus'), Js('Tinlef'), Js('Tlannatar'), Js('Tolthe'), Js('Tordynnar'), Js('Toross'), Js('Traeliorn'), Js('Travaran'), Js('Triandal'), Js('Ualair'), Js('Uevareth'), Js('Uldreiyn'), Js('Urddusk'), Js('Usunaar'), Js('Uthorim'), Js('Vaalyun'), Js('Vaeril'), Js('Vamir'), Js('Vander'), Js('Vartan'), Js('Velethuil'), Js('Venali'), Js('Vesperr'), Js('Vesryn'), Js('Vesstan'), Js('Virion'), Js('Volodar'), Js('Voron'), Js('Vuduin'), Js('Vulas'), Js('Vulen'), Js('Vulluin'), Js('Vulmar'), Js('Vulmer'), Js('Vulmon'), Js('Vulre'), Js('Vulred'), Js('Vulwin'), Js('Wistari'), Js('Wylchyr'), Js('Wyn'), Js('Wyninn'), Js('Wyrran'), Js('Xalph'), Js('Xanotter'), Js('Xhalh'), Js('Xhalth'), Js('Xharlion'), Js('Yalathanil'), Js('Yeschant'), Js('Yhendorn'), Js('Ylyndar'), Js('Zabbas'), Js('Zaltarish'), Js('Zandro'), Js('Zaor'), Js('Zaos'), Js('Zelphar'), Js('Zeno'), Js('Zhoron')]))
var.put('nm2', Js([Js('Sataleeti'), Js('Leena'), Js('Lithoniel'), Js('Vanya'), Js('Alasse'), Js('Zentha'), Js('Myantha'), Js('Eloimaya'), Js('Faraine'), Js('Kylantha'), Js('Celaena'), Js('Aenwyn'), Js('Maescia'), Js('Tyrael'), Js('Shearah'), Js('Elisven'), Js('Llorva'), Js('Nimue'), Js('Zaleria'), Js('Aelrue'), Js('Aelynthi'), Js('Aerilaya'), Js('Aerith'), Js('Ahrendue'), Js('Ahskahala'), Js('Aila'), Js('Alaglossa'), Js('Alais'), Js('Alanis'), Js('Alavara'), Js('Alea'), Js('Aleesia'), Js('Alenia'), Js('Alerathla'), Js('Allannia'), Js('Allisa'), Js('Alloralla'), Js('Allynna'), Js('Almedha'), Js('Almithara'), Js('Alvaerele'), Js('Alyndra'), Js('Amara'), Js('Amaranthae'), Js('Amedee'), Js('Ameria'), Js('Amkissra'), Js('Amlaruil'), Js('Amnestria'), Js('Amra'), Js('Anarzee'), Js('Aneirin'), Js('Anhaern'), Js('Annallee'), Js('Ara'), Js('Araushnee'), Js('Aravae'), Js('Arcaena'), Js('Ariawyn'), Js('Arielimnda'), Js('Arlayna'), Js('Arnarra'), Js('Arryn'), Js('Arthion'), Js('Artin'), Js('Ashera'), Js('Ashryn'), Js('Auluua'), Js('Aurae'), Js('Ava'), Js('Axilya'), Js('Ayda'), Js('Ayla'), Js('Azariah'), Js('Bellaluna'), Js('Bemere'), Js('Blythswana'), Js('Bonnalurie'), Js('Braerindra'), Js('Burolia'), Js('Caeda'), Js('Caerthynna'), Js('Calarel'), Js('Cellica'), Js('Chaenath'), Js('Chalia'), Js('Chalsarda'), Js('Chandrelle'), Js('Chasianna'), Js('Chomylla'), Js('Cilivren'), Js('Ciyradyl'), Js('Claire'), Js('Cremia'), Js('Cyithrel'), Js('Daratrine'), Js('Darshee'), Js('Darunia'), Js('Dasyra'), Js('Dathlue'), Js('Delimbiyra'), Js('Delshandra'), Js('Dessous'), Js('Deularla'), Js('Duilya'), Js('Duru'), Js('Eallyrl'), Js('Ecaeris'), Js('Edea'), Js('Edraele'), Js('Eirika'), Js('Elanalue'), Js('Elanil'), Js('Elasha'), Js('Elenaril'), Js('Eletha'), Js('Elincia'), Js('Ellarian'), Js('Elmyra'), Js('Eloen'), Js('Elora'), Js('Elyon'), Js('Ena'), Js('Enania'), Js('Eshenesra'), Js('Essaerae'), Js('Esta'), Js('Esyae'), Js('Falenas'), Js('Farryn'), Js('Faunalyn'), Js('Fayeth'), Js('Faylen'), Js('Fhaertala'), Js('Fi'), Js('Fieryat'), Js('Filaurel'), Js('Filauria'), Js('Fildaerae'), Js('Gaelira'), Js('Gaerradh'), Js('Gaylia'), Js('Gemstarzah'), Js('Ghilanna'), Js('Glynnii'), Js('Gweyr'), Js('Gwynnestri'), Js('Gylledha'), Js('Hacathra'), Js('Haera'), Js('Halaema'), Js('Halanaestra'), Js('Hamalitia'), Js('Haramara'), Js('Helartha'), Js('Holone'), Js('Huquethae'), Js('Hycis'), Js('Ialantha'), Js('Ikeshia'), Js('Ildilyntra'), Js('Ilmadia'), Js('Ilsevel'), Js('Ilyana'), Js('Ilyrana'), Js('Ilythyrra'), Js('Imizael'), Js('Immianthe'), Js('Imra'), Js('Imryll'), Js('Ioelena'), Js('Irhaal'), Js('Isilfarrel'), Js('Isilynor'), Js('Itiireae'), Js('Itylra'), Js('Iythronel'), Js('Jastra'), Js('Jeardra'), Js('Jhanandra'), Js('Jhaumrithe'), Js('Jhiilsraa'), Js('Kali'), Js('Kasula'), Js('Kavrala'), Js('Kaylessa'), Js('Kaylin'), Js('Keenor'), Js('Keerla'), Js('Keishara'), Js('Kenia '), Js('Kethryllia'), Js('Keya'), Js('Kilyn'), Js('Kythaela'), Js('Laamtora'), Js('Laerdya'), Js('Lazziar'), Js('Leilatha'), Js('Lenna'), Js('Lensa'), Js('Lethhonel'), Js('Lierin'), Js('Liluth'), Js('Lixiss'), Js('Llamryl'), Js('Lorelei'), Js('Lura'), Js('Lusha'), Js('Lusherina'), Js('Lyeecia'), Js('Lyeyeru'), Js('Lyithion'), Js('Lymsleia'), Js('Lyndis'), Js('Lyra'), Js('Lyre'), Js('Maelyrra'), Js('Maeralya'), Js('Makaela'), Js('Malon'), Js('Malruthiia'), Js('Mariona'), Js('Martainn'), Js('Maylin'), Js('Meira'), Js('Melarue'), Js('Merethyl'), Js('Merialeth'), Js('Meriel'), Js('Merlara'), Js('Micaiah'), Js('Mladris'), Js('Mnuvae'), Js('Morgwais'), Js('Moryggan'), Js('Muerlara'), Js('Mylaela'), Js('Mylaerla'), Js('Myriani'), Js('Myrrh'), Js('Nabooru'), Js('Naesala'), Js('Naevys'), Js('Nakiasha'), Js('Nambra'), Js('Nanthleene'), Js('Naumys'), Js('Nei'), Js('Nephenee'), Js('Nexxis'), Js('Nimronyn'), Js('Nithenoel'), Js('Nithroel'), Js('Nlaea'), Js('Nuala'), Js('Nueleth'), Js('Nuovis'), Js('Nushala'), Js('Nylaathria'), Js('Nyna'), Js('Ochyllyss'), Js('Omylia'), Js('Osonia'), Js('Penelo'), Js('Phaerl'), Js('Phelorna'), Js('Phuingara'), Js('Phyrra'), Js('Pyria'), Js('Quamara'), Js('Radelia'), Js('Raejiisa'), Js('Raerauntha'), Js('Rania'), Js('Ratha'), Js('Rathiain'), Js('Renestrae'), Js('Renna'), Js('Rina'), Js('Riniya'), Js('Rosaria'), Js('Rosario'), Js('Roshi'), Js('Roshia'), Js('Rubrae'), Js('Ryllae'), Js('Salihn'), Js('Saelihn'), Js('Saida'), Js('Sakaala'), Js('Sana'), Js('Saria'), Js('Sariandi'), Js('Sarya'), Js('Seirye'), Js('Seldanna'), Js('Selphie'), Js('Selussa'), Js('Shadowmoon'), Js('Shalana'), Js('Shalendra'), Js('Shalheira'), Js('Shandalar'), Js('Shanyrria'), Js('Sharaera'), Js('Sharia'), Js('Sheedra'), Js('Sheera'), Js('Shialaevar'), Js('Shyael'), Js('Shyilia'), Js('Shyonia'), Js('Sinnafain'), Js('Solana'), Js('Soliania'), Js('Soora'), Js('Sorsasta'), Js('Sphiel'), Js('Sumia'), Js('Susklahava'), Js('Sylmae'), Js('Symrustar'), Js('Syndra'), Js('Syviis'), Js('Taenya'), Js('Taionia'), Js('Talanashta'), Js('Talila'), Js('Talindra'), Js('Tanelia'), Js('Tanulia'), Js('Tarasynora'), Js('Teharissa'), Js('Teryani'), Js('Tethys'), Js('Thalia'), Js('Thaola'), Js('Thasitalia'), Js('Thessalia'), Js('Tiatha'), Js('Tinesia'), Js('Tiriara'), Js('Tisharu'), Js('Tsarra'), Js('Uiathen'), Js('Ulelesse'), Js('Umrielyth'), Js('Urmicca'), Js('Uschymna'), Js('Valindra'), Js('Vashti'), Js('Velatha'), Js('Verrona'), Js('Vestele'), Js('Viansola'), Js('Viessa'), Js('Wynnter'), Js('Yaereene'), Js('Yalanilue'), Js('Yathlanae'), Js('Ygrainne'), Js('Ynshael'), Js('Yrlissa'), Js('Yrneha'), Js('Yrthraethra'), Js('Ysmyrlda'), Js('Yulmanda'), Js('Yunalesca'), Js('Zilyana'), Js('Zoastria'), Js('Vaeri')]))
var.put('nm3', Js([Js('Ad'), Js('Ae'), Js('Ara'), Js('Bal'), Js('Bei'), Js('Bi'), Js('Bry'), Js('Cai'), Js('Car'), Js('Chae'), Js('Cra'), Js('Da'), Js('Dae'), Js('Dor'), Js('Eil'), Js('El'), Js('Ela'), Js('En'), Js('Er'), Js('Fa'), Js('Fae'), Js('Far'), Js('Fen'), Js('Gen'), Js('Gil'), Js('Glyn'), Js('Gre'), Js('Hei'), Js('Hele'), Js('Her'), Js('Hola'), Js('Ian'), Js('Iar'), Js('Ili'), Js('Ina'), Js('Jo'), Js('Kea'), Js('Kel'), Js('Key'), Js('Kris'), Js('Leo'), Js('Lia'), Js('Lora'), Js('Lu'), Js('Mag'), Js('Mia'), Js('Mira'), Js('Mor'), Js('Nae'), Js('Neri'), Js('Nor'), Js('Ola'), Js('Olo'), Js('Oma'), Js('Ori'), Js('Pa'), Js('Per'), Js('Pet'), Js('Phi'), Js('Pres'), Js('Qi'), Js('Qin'), Js('Qui'), Js('Ralo'), Js('Rava'), Js('Rey'), Js('Ro'), Js('Sar'), Js('Sha'), Js('Syl'), Js('The'), Js('Tor'), Js('Tra'), Js('Tris'), Js('Ula'), Js('Ume'), Js('Uri'), Js('Va'), Js('Val'), Js('Ven'), Js('Vir'), Js('Waes'), Js('Wran'), Js('Wyn'), Js('Wysa'), Js('Xil'), Js('Xyr'), Js('Yel'), Js('Yes'), Js('Yin'), Js('Ylla'), Js('Zin'), Js('Zum'), Js('Zyl')]))
var.put('nm4', Js([Js('balar'), Js('banise'), Js('bella'), Js('beros'), Js('can'), Js('caryn'), Js('ceran'), Js('cyne'), Js('dan'), Js('di'), Js('dithas'), Js('dove'), Js('faren'), Js('fiel'), Js('fina'), Js('fir'), Js('geiros'), Js('gella'), Js('golor'), Js('gwyn'), Js('hana'), Js('harice'), Js('hice'), Js('horn'), Js('jeon'), Js('jor'), Js('jyre'), Js('kalyn'), Js('kas'), Js('kian'), Js('krana'), Js('lamin'), Js('lana'), Js('lar'), Js('lee'), Js('len'), Js('leth'), Js('lynn'), Js('maer'), Js('maris'), Js('menor'), Js('moira'), Js('myar'), Js('mys'), Js('na'), Js('nala'), Js('nan'), Js('neiros'), Js('nelis'), Js('norin'), Js('peiros'), Js('petor'), Js('phine'), Js('phyra'), Js('qen'), Js('qirelle'), Js('quinal'), Js('ra'), Js('ralei'), Js('ran'), Js('rel'), Js('ren'), Js('ric'), Js('rie'), Js('rieth'), Js('ris'), Js('ro'), Js('rona'), Js('rora'), Js('roris'), Js('salor'), Js('sandoral'), Js('satra'), Js('stina'), Js('sys'), Js('thana'), Js('thyra'), Js('toris'), Js('tris'), Js('tumal'), Js('valur'), Js('varis'), Js('ven'), Js('vyre'), Js('warin'), Js('wenys'), Js('wraek'), Js('wynn'), Js('xalim'), Js('xidor'), Js('xina'), Js('xisys'), Js('yarus'), Js('ydark'), Js('ynore'), Js('yra'), Js('zana'), Js('zeiros'), Js('zorwyn'), Js('zumin')]))
pass
pass


# Add lib to the module scope
elfNames = var.to_python()