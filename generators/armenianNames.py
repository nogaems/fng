__all__ = ['armenianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abaven'), Js('Abirad'), Js('Adis'), Js('Adom'), Js('Adour'), Js('Adroushan'), Js('Aghan'), Js('Aghasi'), Js('Agheksanter'), Js('Aharon'), Js('Alan'), Js('Alec'), Js('Alexan'), Js('Anag'), Js('Anania'), Js('Ananoun'), Js('Anastas'), Js('Andon'), Js('Anoushavan'), Js('Antog'), Js('Antranig'), Js('Antrias'), Js('Apas'), Js('Apel'), Js('Apisoghom'), Js('Apkar'), Js('Apraham'), Js('Ara'), Js('Arakel'), Js('Aram'), Js('Aramais'), Js('Aramaniag'), Js('Aramazt'), Js('Aran'), Js('Arantsar'), Js('Ararad'), Js('Araz'), Js('Ardag'), Js('Ardashes'), Js('Ardavan'), Js('Ardavast'), Js('Ardem'), Js('Ardzroun'), Js('Ared'), Js('Arek'), Js('Aren'), Js('Arevshad'), Js('Ari'), Js('Aris'), Js('Arisdages'), Js('Arkam'), Js('Arman'), Js('Armen'), Js('Armenag'), Js('Arnag'), Js('Arno'), Js('Arpag'), Js('Arpiar'), Js('Arpoun'), Js('Arsen'), Js('Arshag'), Js('Arshalouys'), Js('Arsham'), Js('Arshavir'), Js('Arshen'), Js('Artoun'), Js('Artsan'), Js('Arzouman'), Js('Asadour'), Js('Asbed'), Js('Asbourag'), Js('Asdvadzadour'), Js('Ashod'), Js('Askanaz'), Js('Atam'), Js('Atanas'), Js('Atapeg'), Js('Avak'), Js('Avedig'), Js('Avedis'), Js('Ayk'), Js('Azad'), Js('Azaria'), Js('Bab'), Js('Babeg'), Js('Baben'), Js('Badouagan'), Js('Badrig'), Js('Baghdasar'), Js('Bared'), Js('Barkev'), Js('Barouyr'), Js('Barsam'), Js('Bartev'), Js('Bedros'), Js('Berj'), Js('Boghos'), Js('Bsag'), Js('Dajad'), Js('Daron'), Js('Datev'), Js('Davros'), Js('Dikran'), Js('Diradour'), Js('Diran'), Js('Dirayr'), Js('Dzadour'), Js('Dzaghig'), Js('Dzeroun'), Js('Dzovag'), Js('Emin'), Js('Emmanouel'), Js('Esahag'), Js('Eshkhan'), Js('Gakig'), Js('Gamo'), Js('Gamsar'), Js('Garabed'), Js('Garbis'), Js('Garen'), Js('Garo'), Js('Gaydzag'), Js('Gdridg'), Js('Gharib'), Js('Ghazar'), Js('Ghazaros'), Js('Ghevont'), Js('Ghougas'), Js('Ghoungyanos'), Js('Giragos'), Js('Gomidas'), Js('Goryoun'), Js('Gosdan'), Js('Gosdantin'), Js('Guregh'), Js('Hagop'), Js('Haik'), Js('Hamazasb'), Js('Hamparzoum'), Js('Hapet'), Js('Haro'), Js('Harutyun'), Js('Hayasdan'), Js('Haygag'), Js('Haygaram'), Js('Haygaz'), Js('Haygazoun'), Js('Hayrabed'), Js('Hayrig'), Js('Hetoum'), Js('Hmayag'), Js('Hovagem'), Js('Hovasap'), Js('Hovhannes'), Js('Hovnan'), Js('Hovnatan'), Js('Hovsep'), Js('Hrag'), Js('Hrahad'), Js('Hrant'), Js('Hratch'), Js('Hravart'), Js('Hrayr'), Js('Hraztan'), Js('Jannig'), Js('Jirayr'), Js('Jivan'), Js('Kachig'), Js('Kakig'), Js('Kaloust'), Js('Kamer'), Js('Kapriel'), Js('Karekin'), Js('Karnig'), Js('Kasbar'), Js('Kazavon'), Js('Kegham'), Js('Keghart'), Js('Keghon'), Js('Kersam'), Js('Kesag'), Js('Kevork'), Js('Khajag'), Js('Khatchadour'), Js('Khatcheres'), Js('Khatchig'), Js('Khigar'), Js('Khoren'), Js('Khosrov'), Js('Kourken'), Js('Kousan'), Js('Krikor'), Js('Krisdapor'), Js('Kud'), Js('Lernig'), Js('Levon'), Js('Libarid'), Js('Loris'), Js('Madat'), Js('Madteos'), Js('Magar'), Js('Majag'), Js('Malkhas'), Js('Mamigon'), Js('Mampre'), Js('Manajihr'), Js('Manase'), Js('Mangasar'), Js('Manough'), Js('Manuel'), Js('Mardig'), Js('Mardiros'), Js('Mardoun'), Js('Margos'), Js('Markar'), Js('Mashdots'), Js('Masis'), Js('Matous'), Js('Matsag'), Js('Meghrig'), Js('Mekhag'), Js('Melek'), Js('Melkon'), Js('Meroujan'), Js('Mesrob'), Js('Mgrditch'), Js('Mgrdoum'), Js('Mher'), Js('Mihran'), Js('Mihrtad'), Js('Mikaiel'), Js('Minas'), Js('Misak'), Js('Mjej'), Js('Mkhitar'), Js('Mleh'), Js('Mnatsagan'), Js('Mourad'), Js('Mouron'), Js('Moushe'), Js('Moushegh'), Js('Movses'), Js('Nahabed'), Js('Nar'), Js('Narek'), Js('Natan'), Js('Navasart'), Js('Nazar'), Js('Nazaret'), Js('Nbad'), Js('Nerseh'), Js('Nerses'), Js('Nigoghos'), Js('Nigol'), Js('Njteh'), Js('Norayr'), Js('Norhad'), Js('Norvan'), Js('Noubar'), Js('Nourhan'), Js('Noy'), Js('Nshan'), Js('Oda'), Js('Ohan'), Js('Oksen'), Js('Onnig'), Js('Oshakan'), Js('Oshin'), Js('Pagour'), Js('Pakrad'), Js('Panig'), Js('Panos'), Js('Papken'), Js('Paramaz'), Js('Paren'), Js('Parkhoutar'), Js('Parnag'), Js('Parounag'), Js('Parsegh'), Js('Partogh'), Js('Partoghimeos'), Js('Paylag'), Js('Peklar'), Js('Pelibbos'), Js('Penyamin'), Js('Pertag'), Js('Purad'), Js('Puzant'), Js('Raffi'), Js('Raphael'), Js('Razmig'), Js('Reteos'), Js('Rosdom'), Js('Rupen'), Js('Sahag'), Js('Samson'), Js('Samuel'), Js('Sanasar'), Js('Sanatroug'), Js('Sarhad'), Js('Sarkis'), Js('Saro'), Js('Sasoun'), Js('Sebouh'), Js('Semag'), Js('Serj'), Js('Sero'), Js('Serop'), Js('Serovpe'), Js('Set'), Js('Setrag'), Js('Sevag'), Js('Sevan'), Js('Simon'), Js('Sinan'), Js('Sion'), Js('Sipan'), Js('Sirak'), Js('Sirekan'), Js('Sis'), Js('Sisag'), Js('Smpad'), Js('Soghomon'), Js('Sograd'), Js('Sos'), Js('Soukias'), Js('Souren'), Js('Sourmag'), Js('Srabion'), Js('Stephan'), Js('Takvor'), Js('Taniel'), Js('Tateos'), Js('Tatoul'), Js('Tavit'), Js('Tavtag'), Js('Teotig'), Js('Terenig'), Js('Tevan'), Js('Thomas'), Js('Torkom'), Js('Toros'), Js('Trasdamard'), Js('Tro'), Js('Tsakig'), Js('Tsolag'), Js('Vagharsh'), Js('Vagharshag'), Js('Vaghenag'), Js('Vahagn'), Js('Vahaken'), Js('Vahan'), Js('Vahe'), Js('Vahram'), Js('Vahrej'), Js('Vakhtang'), Js('Van'), Js('Vanadour'), Js('Vanagan'), Js('Vanant'), Js('Vanig'), Js('Vanoush'), Js('Varak'), Js('Varant'), Js('Varaztad'), Js('Varos'), Js('Varoujan'), Js('Vart'), Js('Vartan'), Js('Vartavar'), Js('Varteres'), Js('Vartivar'), Js('Vartkes'), Js('Vasag'), Js('Vasbourag'), Js('Vatche'), Js('Vazken'), Js('Vazrig'), Js('Vicken'), Js('Vigen'), Js('Vosdanig'), Js('Vosgan'), Js('Vram'), Js('Vrej'), Js('Vrtanes'), Js('Yeghiazar'), Js('Yeghisheh'), Js('Yeghya'), Js('Yeprem'), Js('Yeranos'), Js('Yerimya'), Js('Yervant'), Js('Yesayi'), Js('Yetvart'), Js('Yeznig'), Js('Yezras'), Js('Zadig'), Js('Zakariya'), Js('Zareh'), Js('Zarmayr'), Js('Zarmig'), Js('Zarzant'), Js('Zaven'), Js('Zohrab'), Js('Zohrag'), Js('Zoravar')]))
var.put('nm2', Js([Js('Adrine'), Js('Aghavni'), Js('Aida'), Js('Akabi'), Js('Akac'), Js('Aldz'), Js('Alice'), Js('Alids'), Js('Alidz'), Js('Alik'), Js('Aline'), Js('Almasd'), Js('Alvart'), Js('Anahid'), Js('Anais'), Js('Ani'), Js('Ankine'), Js('Anna'), Js('Annman'), Js('Anoush'), Js('Antaram'), Js('Araks'), Js('Araksi'), Js('Aramouhi'), Js('Araz'), Js('Arda'), Js('Ardanoush'), Js('Areknaz'), Js('Arev'), Js('Arevalous'), Js('Arevhad'), Js('Arevig'), Js('Arine'), Js('Arkina'), Js('Armanoush'), Js('Armenouhi'), Js('Armine'), Js('Arousyag'), Js('Arpenig'), Js('Arpi'), Js('Arpineh'), Js('Arshagouhi'), Js('Arshalous'), Js('Arsine'), Js('Artzouig'), Js('Asdghig'), Js('Ashkhen'), Js('Avids'), Js('Azadouhi'), Js('Azkanoush'), Js('Azniv'), Js('Barzig'), Js('Baydzar'), Js('Berjanoush'), Js('Berjouhi'), Js('Dalita'), Js('Datevig'), Js('Dikranouhi'), Js('Dirouhi'), Js('Dzaghganoush'), Js('Dzaghig'), Js('Dziadzan'), Js('Dzovig'), Js('Dzovinar'), Js('Eghtsanoush'), Js('Elise'), Js('Eliz'), Js('Emasdouhi'), Js('Emma'), Js('Endza'), Js('Endzanoush'), Js('Erato'), Js('Esgouhi'), Js('Euphemia'), Js('Euphrosina'), Js('Eva'), Js('Gacia'), Js('Gadar'), Js('Gadarine'), Js('Gaiane'), Js('Gakavig'), Js('Garine'), Js('Gayane'), Js('Ghadam'), Js('Gorandoukht'), Js('Goulizar'), Js('Goulnaz'), Js('Gumach'), Js('Hagint'), Js('Hamaspouyr'), Js('Hamesdouhi'), Js('Hasmig'), Js('Haverj'), Js('Hayganoush'), Js('Haygouhi'), Js('Heghineh'), Js('Heghnar'), Js('Hera'), Js('Heranoush'), Js('Hereknaz'), Js('Hermineh'), Js('Hnazant'), Js('Houdit'), Js('Hourher'), Js('Houri'), Js('Houshig'), Js('Hranoush'), Js('Hrantouhi'), Js('Hranush'), Js('Hrarpi'), Js('Hratchouhi'), Js('Hreghen'), Js('Hripsimeh'), Js('Hrout'), Js('Isabel'), Js('Isabella'), Js('Jbdouhi'), Js('Jebid'), Js('Juliana'), Js('Kaghtzrig'), Js('Karni'), Js('Kayaneh'), Js('Keghanoush'), Js('Keghetzig'), Js('Keghouhi'), Js('Keran'), Js('Khatchouhi'), Js('Khatoun'), Js('Khngeni'), Js('Khonarh'), Js('Khorodig'), Js('Khosrovanoush'), Js('Khosrovidookht'), Js('Khosrovitoughd'), Js('Khoumar'), Js('Khoyan'), Js('Kinevart'), Js('Klkhatir'), Js('Knar'), Js('Knkoush'), Js('Kohar'), Js('Koharig'), Js('Lara'), Js('Lelag'), Js('Lena'), Js('Leniya'), Js('Lili'), Js('Lilit'), Js('Lori'), Js('Lorig'), Js('Louseres'), Js('Lousig'), Js('Lousine'), Js('Lousntak'), Js('Lousvart'), Js('Lucy'), Js('Madlene'), Js('Manoushag'), Js('Maral'), Js('Marem'), Js('Margaret'), Js('Maria'), Js('Marie'), Js('Marineh'), Js('Maritsa'), Js('Mariyam'), Js('Markrid'), Js('Marmar'), Js('Maro'), Js('Marta'), Js('Mayda'), Js('Mayranoush'), Js('Medax'), Js('Meghranoush'), Js('Melineh'), Js('Mirna'), Js('Nane'), Js('Nanor'), Js('Nare'), Js('Nargiz'), Js('Narineh'), Js('Narod'), Js('Nartouhi'), Js('Nashkhoun'), Js('Natel'), Js('Nayat'), Js('Nayirouhi'), Js('Nayree'), Js('Nazani'), Js('Nazeli'), Js('Nazenig'), Js('Negdar'), Js('Nora'), Js('Noune'), Js('Nouritsa'), Js('Noushig'), Js('Noyemi'), Js('Nunuphar'), Js('Nvart'), Js('Nver'), Js('Ovsanna'), Js('Pakradouhi'), Js('Palasan'), Js('Parantsem'), Js('Parantzem'), Js('Parouhi'), Js('Patil'), Js('Pavagan'), Js('Payl'), Js('Pergrouhi'), Js('Persape'), Js('Pounig'), Js('Pouragn'), Js('Pourasdan'), Js('Pouregh'), Js('Raqel'), Js('Razmouhi'), Js('Rehan'), Js('Repega'), Js('Rhiphsime'), Js('Rita'), Js('Rouzan'), Js('Rozin'), Js('Rubina'), Js('Sahaganoush'), Js('Salpi'), Js('Sanam'), Js('Santoukhd'), Js('Sara'), Js('Satenig'), Js('Selma'), Js('Serig'), Js('Serine'), Js('Seta'), Js('Sevana'), Js('Sevoug'), Js('Shahanig'), Js('Shakeh'), Js('Shamiram'), Js('Sharmagh'), Js('Shnorhig'), Js('Shoghagat'), Js('Shogher'), Js('Shoghig'), Js('Shoushan'), Js('Shoushanig'), Js('Sibyl'), Js('Sima'), Js('Siran'), Js('Siranoush'), Js('Sirarpi'), Js('Siroun'), Js('Sirvart'), Js('Soffi'), Js('Soffiya'), Js('Soghome'), Js('Sona'), Js('Soseh'), Js('Sosi'), Js('Srpouhi'), Js('Stepanie'), Js('Stephanie'), Js('Sussan'), Js('Suzan'), Js('Sybilla'), Js('Sylva'), Js("T'aguhi"), Js('Takouhi'), Js('Takoush'), Js('Talar'), Js('Taline'), Js('Tamar'), Js('Tangakin'), Js('Tania'), Js('Tarouhi'), Js('Teghtsanig'), Js('Teghtsoun'), Js('Theodora'), Js('Titer'), Js('Tsangali'), Js('Tsdrig'), Js('Tshoghig'), Js('Tsoler'), Js('Tsoline'), Js('Tsvig'), Js('Vana'), Js('Vanouhi'), Js('Vanoush'), Js('Varsenig'), Js('Vartanoush'), Js('Varteni'), Js('Varteshah'), Js('Vartiter'), Js('Vartivar'), Js('Vartouhi'), Js('Varvara'), Js('Varvare'), Js('Vazkanoush'), Js('Vehanoush'), Js('Vehantsnouhi'), Js('Verjin'), Js('Verjouhi'), Js('Verkine'), Js('Vertchalous'), Js('Vosgedzam'), Js('Vosgehad'), Js('Vosgemad'), Js('Vosgetel'), Js('Vosgi'), Js('Yeghisapet'), Js('Yeghnig'), Js('Yeghsan'), Js('Yeprouhi'), Js('Yeranuhi'), Js('Yerazig'), Js('Yerchanig'), Js('Yester'), Js('Yeter'), Js('Yeva'), Js('Yevkeneh'), Js('Yranig'), Js('Zabel'), Js('Zanazan'), Js('Zapel'), Js('Zarmantoukht'), Js('Zarmineh'), Js('Zarmouhi'), Js('Zarouhi'), Js('Zartar'), Js('Zarvart'), Js('Zepour'), Js('Zmroukhd'), Js('Zoulal'), Js('Zvart')]))
var.put('nm3', Js([Js('Aintablian'), Js('Altounian'), Js('Altunian'), Js('Andonian'), Js('Antebian'), Js('Antonian'), Js('Antreasian'), Js('Arabian'), Js('Arakelian'), Js('Arakelyan'), Js('Aramian'), Js('Aramyan'), Js('Araradian'), Js('Araratian'), Js('Ardashessian'), Js('Ardzivian'), Js('Ardzruni'), Js('Aronyan'), Js('Aroyan'), Js('Arshaguni'), Js('Arshagunian'), Js('Arshakuni'), Js('Arslanian'), Js('Artashessian'), Js('Artinian'), Js('Arzumanian'), Js('Asatrian'), Js('Ashjian'), Js('Aslanyan'), Js('Assadourian'), Js('Assarian'), Js('Assayan'), Js('Astvadzadourian'), Js('Atanosian'), Js('Atchabahian'), Js('Avakian'), Js('Avaliani'), Js('Avedikian'), Js('Avedissian'), Js('Avetisyan'), Js('Aviet'), Js('Avietissian'), Js('Avtomian'), Js('Azadian'), Js('Azarian'), Js('Azatyan'), Js('Azizian'), Js('Aznavourian'), Js('Babaian'), Js('Babajanian'), Js('Babayan'), Js('Baboian'), Js('Badalian'), Js('Bagdazarian'), Js('Baghdadlian'), Js('Bagratuni'), Js('Balabanian'), Js('Balasian'), Js('Balian'), Js('Balikian'), Js('Baltaian'), Js('Bamanian'), Js('Banaian'), Js('Bancayan'), Js('Baronian'), Js('Barsamian'), Js('Basmajian'), Js('Bedrosian'), Js('Belekdanian'), Js('Berberian'), Js('Bizdikian'), Js('Boboian'), Js('Boghosian'), Js('Bogosian'), Js('Boshian'), Js('Boyajian'), Js('Bozian'), Js('Bozigian'), Js('Burian'), Js('Chakmakian'), Js('Chilingirian'), Js('Cholakian'), Js('Cibrian'), Js('Dadashian'), Js('Dadekian'), Js('Dadourian'), Js('Danielian'), Js('Darbinian'), Js('Davidian'), Js('Demirjian'), Js('Derderian'), Js('Dermovsesian'), Js('Deukmejian'), Js('Deyrmenjian'), Js('Djansezian'), Js('Dzaghgouni'), Js('Eghian'), Js('Ekizian'), Js('Ekmekjian'), Js('Ekshian'), Js('Eskandarian'), Js('Esmerian'), Js('Ezzatian'), Js('Fanoosian'), Js('Farajian'), Js('Fermanian'), Js('Gabrelyan'), Js('Galinyan'), Js('Galoustyan'), Js('Galoyan'), Js('Galstanyan'), Js('Galstyan'), Js('Gambaryan'), Js('Gamburyan'), Js('Gamerikian'), Js('Games'), Js('Garabedian'), Js('Garcha'), Js('Gasparyan'), Js('Gazanian'), Js('Gevorgyan'), Js('Gharakhanian'), Js('Ghazaryan'), Js('Ghukasian'), Js('Ghukasyan'), Js('Ginosyan'), Js('Giragosian'), Js('Girogosian'), Js('Gogbashian'), Js('Gorgodian'), Js('Grigorian'), Js('Gulazarian'), Js('Gulbenkian'), Js('Hadjetian'), Js('Hagopian'), Js('Hakobjanian'), Js('Hakobyan'), Js('Haladjian'), Js('Haroutiunian'), Js('Haroutunian'), Js('Harpootlian'), Js('Hayrapetyan'), Js('Hazarapetyan'), Js('Hekimyan'), Js('Hintlian'), Js('Horozian'), Js('Houssian'), Js('Hovanessian'), Js('Hovhanesian'), Js('Hovhannisian'), Js('Hovhannisyan'), Js('Hovnanian'), Js('Hovnatanian'), Js('Hovsepian'), Js('Igityan'), Js('Inguilizian'), Js('Isagholian'), Js('Isahakian'), Js('Ishkhanian'), Js('Iskenderian'), Js('Ismailyan'), Js('Ispiryan'), Js('Israyelyan'), Js('Istamboulian'), Js('Istanboulian'), Js('Izmirlian'), Js('Jalalyan'), Js('Jambazian'), Js('Janikyan'), Js('Jizmejian'), Js('Kadoyan'), Js('Kalanjian'), Js('Kalousdian'), Js('Kapoian'), Js('Kaprielian'), Js('Karadjian'), Js('Karapetian'), Js('Karapetyan'), Js('Kardashian'), Js('Karmarian'), Js('Karmaryan'), Js('Kasabian'), Js('Kasajian'), Js('Kasbarian'), Js('Kasparian'), Js('Kassarjian'), Js('Kassouni'), Js('Kazandjian'), Js('Kechichian'), Js('Kellejian'), Js('Keosseian'), Js('Kevranian'), Js('Keyishian'), Js('Kezerian'), Js('Khachadurian'), Js('Khachatourian'), Js('Khachaturian'), Js('Khederian'), Js('Khederlarian'), Js('Kherlakian'), Js('Khorozian'), Js('Khrlakian'), Js('Kinosyan'), Js('Kirakosian'), Js('Klanian'), Js('Kocharian'), Js('Kocharyan'), Js('Kostanian'), Js('Kostikyan'), Js('Kostoyan'), Js('Kotoyan'), Js('Koumjian'), Js('Koundakjian'), Js('Kouyoumjian'), Js('Krikorian'), Js('Krjalian'), Js('Ksajikian'), Js('Kupelian'), Js('Lylozian'), Js('Malkhassian'), Js('Mamigonian'), Js('Mamikonian'), Js('Manoogian'), Js('Manoukian'), Js('Manukyan'), Js('Manvelian'), Js('Marashian'), Js('Mardikian'), Js('Mardirosian'), Js('Margaryan'), Js('Margossian'), Js('Marjanian'), Js('Markarian'), Js('Markossian'), Js('Maroutian'), Js('Martirosyan'), Js('Marutyan'), Js('Matevosian'), Js('Mechigian'), Js('Melkonyan'), Js('Mentsoyan'), Js('Merdinian'), Js('Merjanian'), Js('Mesdjian'), Js('Mesropian'), Js('Mikaelian'), Js('Mikoyan'), Js('Minassian'), Js('Mirakian'), Js('Mirzoyan'), Js('Mkhmeljian'), Js('Mkrtchyan'), Js('Mooskian'), Js('Mouradian'), Js('Mousissian'), Js('Moutafian'), Js('Movsesian'), Js('Muratian'), Js('Musaelian'), Js('Musayelyan'), Js('Nabavian'), Js('Nadanian'), Js('Nakashian'), Js('Nalbandian'), Js('Narcessian'), Js('Naroyan'), Js('Natanian'), Js('Natlinian'), Js('Nazaryan'), Js('Nazlikian'), Js('Nerguizian'), Js('Nigoghosian'), Js('Nigosian'), Js('Ohanian'), Js('Ohanyan'), Js('Ojaghian'), Js('Orogian'), Js('Ourfalian'), Js('Ovakimian'), Js('Ovanesian'), Js('Ovasapian'), Js('Ovesian'), Js('Paboojian'), Js('Pakradouni'), Js('Pakradounian'), Js('Panoosian'), Js('Panosian'), Js('Papazian'), Js('Parisyan'), Js('Paronyan'), Js('Pashayan'), Js('Pashian'), Js('Petrosian'), Js('Petrosyan'), Js('Piliposian'), Js('Pilosyan'), Js('Piruzian'), Js('Pogosian'), Js('Poponian'), Js('Portoian'), Js('Reizian'), Js('Rodnoian'), Js('Sahakian'), Js('Samuelian'), Js('Sandrosyan'), Js('Sandruni'), Js('Sarafian'), Js('Sargsyan'), Js('Sarian'), Js('Sarkisian'), Js('Sarkissian'), Js('Saroyan'), Js('Sasounian'), Js('Sasounyan'), Js('Seferian'), Js('Seropian'), Js('Sevan'), Js('Sevhonkian'), Js('Shahverdyan'), Js('Sibrian'), Js('Simonian'), Js('Simonyan'), Js('Skendarian'), Js('Smoulian'), Js('Smullyan'), Js('Soghomonian'), Js('Stepanyan'), Js('Suzmeian'), Js('Suzmeyan'), Js('Tachdjian'), Js('Takoushian'), Js('Tankian'), Js('Tarpinian'), Js('Taslakian'), Js('Tateossian'), Js('Tatilian'), Js('Tatiossian'), Js('Tavitian'), Js('Tjeknavorian'), Js('Topalian'), Js('Torigian'), Js('Torossian'), Js('Toumanian'), Js('Tovmasian'), Js('Trdatyan'), Js('Tufenkian'), Js('Tumanyan'), Js('Tumasyan'), Js('Vardanyan'), Js('Vartanian'), Js('Vartoogian'), Js('Virabyan'), Js('Vosgrichian'), Js('Vratsyan'), Js('Yardumian'), Js('Yeghiayan'), Js('Yeghiazarian'), Js('Yeghoyan'), Js('Yerevanian'), Js('Yeterian'), Js('Zadian'), Js('Zakaryan'), Js('Zakoyan'), Js('Zeitunian'), Js('Zeitunlian'), Js('Zentuntsian'), Js('Zildjian'), Js('Ziririan'), Js('Zohrabyan'), Js('Zornakyan')]))
pass
pass


# Add lib to the module scope
armenianNames = var.to_python()