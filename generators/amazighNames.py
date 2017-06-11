__all__ = ['amazighNames']

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
    var.put('nm1', Js([Js('Abaghugh'), Js('Abakada'), Js('Abarug'), Js('Abayghur'), Js('Abazza'), Js('Abdir'), Js('Abelinut'), Js('Abelius'), Js('Aberkan'), Js('Aberwas'), Js('Abhau'), Js('Abidin'), Js('Abudrar'), Js('Acku'), Js('Adal'), Js('Adan'), Js('Adane'), Js('Adas'), Js('Aderbal'), Js('Aderfi'), Js('Adergazuz'), Js('Adghigh'), Js('Adgum'), Js('Adherbal'), Js('Adhughmas'), Js('Adi'), Js('Adid'), Js('Adidet'), Js('Adinseg'), Js('Adiusit'), Js('Adjan'), Js('Admer'), Js('Adrikan'), Js('Adrir'), Js('Adum'), Js('Adza'), Js('Afa'), Js('Afagis'), Js('Afalawas'), Js('Afalkay'), Js('Afalku'), Js('Afaraj'), Js('Afasi'), Js('Afassiv'), Js('Afaw'), Js('Afekay'), Js('Afellan'), Js('Afennich'), Js('Afennis'), Js('Afer'), Js('Afesdiyas'), Js('Affi'), Js('Affou'), Js('Affu'), Js('Afkal'), Js('Aflawas'), Js('Aflis'), Js('Afoud'), Js('Afra'), Js('Afroukh'), Js('Afrux'), Js('Afsahi'), Js('Afsan'), Js('Afsane'), Js('Aftas'), Js('Afud'), Js('Afulay'), Js('Agafay'), Js('Agag'), Js('Agam'), Js('Agama'), Js('Agaoua'), Js('Agawa'), Js('Agdada'), Js('Agdun'), Js('Agerzam'), Js('Agetun'), Js('Aggur'), Js('Aghali'), Js('Aghbalu'), Js('Aghdim'), Js('Aghecher'), Js('Aghilas'), Js('Aghiles'), Js('Aghlan'), Js('Aghulas'), Js('Aghzu'), Js('Agizul'), Js('Agnan'), Js('Agour'), Js('Agra'), Js('Agram'), Js('Aguellid'), Js('Agur'), Js('Agura'), Js('Agwama'), Js('Agwectim'), Js('Agwellidth'), Js('Agwilal'), Js('Agwillul'), Js('Agwmar'), Js('Ahar'), Js('Ahaszzi'), Js('Aher'), Js('Aheyâd'), Js('Ahmis'), Js('Ahras'), Js('Ahsiku'), Js('Ajan'), Js('Ajdir'), Js('Ajeddig'), Js('Ajeder'), Js('Ajis'), Js('Akaday'), Js('Akakouss'), Js('Akakus'), Js('Akaouar'), Js('Akar'), Js('Akatelaji'), Js('Akawar'), Js('Akawel'), Js('Akbabou'), Js('Akbabu'), Js('Akensus'), Js('Akersim'), Js('Akhalaf'), Js('Akli'), Js('Aklouf'), Js('Akluf'), Js('Akmazir'), Js('Akmin'), Js('Akorakor'), Js('Akouna'), Js('Aksel'), Js('Aksim'), Js('Aktula'), Js('Akudad'), Js('Akuna'), Js('Akunad'), Js('Akwli'), Js('Akzer'), Js('Akziz'), Js('Alenas'), Js('Alernas'), Js('Ales'), Js('Alsan'), Js('Améstida'), Js('Amêzyan'), Js('Amadsu'), Js('Amadur'), Js('Amagan'), Js('Amalu'), Js('Amanar'), Js('Amasin'), Js('Amassine'), Js('Amattaken'), Js('Amawal'), Js('Amayas'), Js('Amaynu'), Js('Amayyas'), Js('Amazigh'), Js('Amazuz'), Js('Amazzal'), Js('Amdegh'), Js('Amedras'), Js('Amellal'), Js('Amen'), Js('Amenay'), Js('Amennay'), Js('Amenzu'), Js('Ameqran'), Js('Ameqwran'), Js('Amergiw'), Js('Amermus'), Js('Amesakul'), Js('Amesan'), Js('Amesfal'), Js('Amesggin'), Js('Amess'), Js('Amessan'), Js('Amestan'), Js('Amezian'), Js('Amezwar'), Js('Amezyan'), Js('Amezza'), Js('Amgar'), Js('Amghar'), Js('Amghi'), Js('Amhaws'), Js('Amjoune'), Js('Amjun'), Js('Amma'), Js('Ammuc'), Js('Amnas'), Js('Amnay'), Js('Amoul'), Js('Amray'), Js('Amri'), Js('Amruc'), Js('Amrus'), Js('Amsag'), Js('Amud'), Js('Amul'), Js('Amulas'), Js('Amuqran'), Js('Amur'), Js('Amyaz'), Js('Amzîn'), Js('Amzal'), Js('Amzar'), Js('Amzi'), Js('Amzun'), Js('Anaba'), Js('Anamar'), Js('Anamir'), Js('Anaruz'), Js('Anazâr'), Js('Anaz'), Js('Anazir'), Js('Andara'), Js('Andaz'), Js('Anebdad'), Js('Anegmar'), Js('Anes'), Js('Angad'), Js('Anir'), Js('Anka'), Js('Annaber'), Js('Annaz'), Js('Annira'), Js('Annun'), Js('Anoune'), Js('Anqa'), Js('Antaken'), Js('Antala'), Js('Antalas'), Js('Anun'), Js('Anwal'), Js('Anzar'), Js('Anzer'), Js('Aouras'), Js('Aoureg'), Js('Aqnuc'), Js('Aqzer'), Js('Arafou'), Js('Arafu'), Js('Araken'), Js('Aramsu'), Js('Aras'), Js('Areksim'), Js('Argan'), Js('Arim'), Js('Ariuc'), Js('Arkam'), Js('Arris'), Js('Arsan'), Js('Artemit'), Js('Asaf'), Js('Asafa'), Js('Asafar'), Js('Asafu'), Js('Asafuk'), Js('Asagh'), Js('Asaru'), Js('Asaruf'), Js('Asbaku'), Js('Asemidhan'), Js('Aserdhil'), Js('Asfar'), Js('Asfru'), Js('Asghour'), Js('Asghun'), Js('Asirem'), Js('Asker'), Js('Aslal'), Js('Asmed'), Js('Asmil'), Js('Asmun'), Js('Asnani'), Js('Aspar'), Js('Asrag'), Js('Assala'), Js('Asulil'), Js('Asyan'), Js('Aszar'), Js("At'isi"), Js('Atanawsu'), Js('Atbir'), Js('Aten'), Js('Atisi'), Js('Atrar'), Js('Aurigh'), Js('Autas'), Js('Autit'), Js('Awdia'), Js('Awinagh'), Js('Awlagh'), Js('Awragh'), Js('Awras'), Js('Awreb'), Js('Awreg'), Js('Awrib'), Js('Awsim'), Js('Awzal'), Js('Axalaf'), Js('Axamuk'), Js('Axamukw'), Js('Axamux'), Js('Ayamoune'), Js('Ayamun'), Js('Aydril'), Js('Ayedril'), Js('Ayi'), Js('Ayidril'), Js('Ayigig'), Js('Ayitift'), Js('Aylal'), Js('Aylan'), Js('Aylimas'), Js('Ayrad'), Js('Aytarel'), Js('Ayuba'), Js('Ayur'), Js('Ayura'), Js('Ayyur'), Js('Azêllay'), Js('Azûlay'), Js('Azad'), Js('Azaggagh'), Js('Azal'), Js('Azan'), Js('Azar'), Js('Azarug'), Js('Azayku'), Js('Azday'), Js('Azem'), Js('Azenkwd'), Js('Azenkwed'), Js('Azenzâr'), Js('Azenzêr'), Js('Azenzer'), Js('Azerwal'), Js('Azerzour'), Js('Azerzur'), Js('Aziki'), Js('Aziwel'), Js('Azmar'), Js('Azmer'), Js('Aznag'), Js('Azouaou'), Js('Azref'), Js('Azregh'), Js('Azrur'), Js('Azulay'), Js('Azum'), Js('Azur'), Js('Azure'), Js('Azuz'), Js('Azwaw'), Js('Azwu'), Js('Azzad'), Js('BaBar'), Js('Badaz'), Js('Badda'), Js('Baddi'), Js('Badias'), Js('Badiden'), Js('Badis'), Js('Baduft'), Js('Baga'), Js('Bagay'), Js('Bagrad'), Js('Baha'), Js('Bahada'), Js('Bahasz'), Js('Baheddi'), Js('Bahemus'), Js('Bahena'), Js('Baheyyi'), Js('Bahnini'), Js('Bahsis'), Js('Bahu'), Js('Bahus'), Js('Bajja'), Js('Bakada'), Js('Bakdid'), Js('BakeBu'), Js('Bakezda'), Js('Baki'), Js('Baku'), Js('Balidir'), Js('Balilek'), Js('Balluk'), Js('Baloua'), Js('Balsilek'), Js('Balwa'), Js('Bamu'), Js('Banay'), Js('Bani'), Js('Banini'), Js('Baqaks'), Js('Barehu'), Js('Bargbal'), Js('Bari'), Js('Barour'), Js('Barsa'), Js('Barugsen'), Js('Barur'), Js('Basi'), Js('Bassou'), Js('Bassu'), Js('Basu'), Js('Batus'), Js('Bawar'), Js('Bawttu'), Js('Bayddu'), Js('Bayghur'), Js('Bayna'), Js('Bayru'), Js('Bayu'), Js('Bazga'), Js('Baziw'), Js('Bazza'), Js('Bazzi'), Js('Beddis'), Js('Bekathen'), Js('Belkin'), Js('Bellenen'), Js('Bellou'), Js('Bellu'), Js('Bencor'), Js('Berjas'), Js('Berkan'), Js('Bersi'), Js('Berzal'), Js('Betalsa'), Js('Betsin'), Js('Bezza'), Js('Bezzi'), Js('Bidas'), Js('Bidin'), Js('Birzal'), Js('Bizar'), Js('Bocchus'), Js('Bochus'), Js('Bostar'), Js('Bouda'), Js('Bougoud'), Js('Briruc'), Js('Buba'), Js('Buda'), Js('Bughud'), Js('Bugud'), Js('Buhanu'), Js('Buhasu'), Js('Bukar'), Js('Bukkus'), Js('Bukus'), Js('Bulughin'), Js('Bumilkar'), Js('Buna'), Js('Burri'), Js('Buxthuc'), Js('Buxus'), Js('Buzattu'), Js('Buzid'), Js('Cana'), Js('Caras'), Js('Cehdir'), Js('Charas'), Js('Chiboub'), Js('Cibub'), Js('Cicungh'), Js('Cucanq'), Js('Cucunq'), Js('Culam'), Js('Curdid'), Js('Dabar'), Js('Dadduh'), Js('Dahi'), Js('Dali'), Js('Daliz'), Js('Dalmas'), Js('Daris'), Js('Darri'), Js('Dasamu'), Js('Dasi'), Js('Dehhu'), Js('Demer'), Js('Demmou'), Js('Demmu'), Js('Deren'), Js('DeriI'), Js('Derri'), Js('Djana'), Js('Drusila'), Js('Elïas'), Js('Elyes'), Js('Eynan'), Js('Eysan'), Js('Faday'), Js('Faghis'), Js('Faraksen'), Js('Faras'), Js('Farinas'), Js('Fayed'), Js('Fejjer'), Js('Fekkus'), Js('Fekus'), Js('Fela'), Js('Felysam'), Js('Fenas'), Js('Fennas'), Js('Fergan'), Js('Ferkal'), Js('Ferkus'), Js('Ferouane'), Js('Ferwan'), Js('Fidas'), Js('Fiden'), Js('Filal'), Js('Filgou'), Js('Filgu'), Js('Firhun'), Js('Firman'), Js('Firmus'), Js('Firwus'), Js('Foughal'), Js('Founen'), Js('Fourou'), Js('Frawsen'), Js('Fudina'), Js('Fughal'), Js('Fuhal'), Js('Funen'), Js('Furu'), Js('Gana'), Js('Gaoua'), Js('Garam'), Js('Garas'), Js('Garayin'), Js('Garmul'), Js('Garnan'), Js('Gauda'), Js('Gawa'), Js('Gaya'), Js('Gectul'), Js('Geta'), Js('Geznay'), Js('Gezul'), Js('Ghanim'), Js('Gharmul'), Js('Ghaysum'), Js('Ghenima'), Js('Ghilas'), Js('Ghumer'), Js('Ghumran'), Js('Gildon'), Js('Gildun'), Js('Gimer'), Js('Giss'), Js('Giwi'), Js('Gouda'), Js('Goula'), Js('Gourane'), Js('Gourzil'), Js('Gubul'), Js('Guda'), Js('Gudjil'), Js('Guechtoul'), Js('Guimer'), Js('Guioui'), Js('Gula'), Js('Gulalsa'), Js('Gulusa'), Js('Gulussa'), Js('Guran'), Js('Gurayin'), Js('Gurzil'), Js('Gwafa'), Js('Gwasila'), Js('Gwejdthi'), Js('Hacnaq'), Js('Hadu'), Js('Haggi'), Js('Hakku'), Js('Hamu'), Js('Hdidou'), Js('Hdidu'), Js('Heddi'), Js('Heddu'), Js('Hella'), Js('Hellu'), Js('Hemmu'), Js('Hesu'), Js('Hetu'), Js('Hiba'), Js('Hibel'), Js('Hiemsal'), Js('Himmi'), Js('Hintat'), Js('Hotha'), Js('Huwar'), Js('Iafis'), Js('Ialdas'), Js('Iarbas'), Js('Iarbuhan'), Js('Iba'), Js('Ibba'), Js('Ibiza'), Js('Ibzatha'), Js('Iccu'), Js('Ichchou'), Js('Ichou'), Js('Icu'), Js('Idas'), Js('Iddas'), Js('Idder'), Js('Ider'), Js('Ides'), Js('Idibal'), Js('Idir'), Js('Idmi'), Js('Idras'), Js('Idren'), Js('Idus'), Js('Iesdan'), Js('Iffou'), Js('Iffu'), Js('Ifni'), Js('Ifrek'), Js('Ifren'), Js('Ifri'), Js('Ifrou'), Js('Ifru'), Js('Ifruy'), Js('Ifser'), Js('Iften'), Js('Ifthen'), Js('Ifui'), Js('Ifwin'), Js('Igan'), Js('Igas'), Js('Igdal'), Js('Iggas'), Js('Ighis'), Js('Ighlaf'), Js('Ighlas'), Js('Igider'), Js('Igig'), Js('Iglen'), Js('Igli'), Js('Igmasen'), Js('Igmaz'), Js('Igmi'), Js('Ignim'), Js('Iguc'), Js('Iguig'), Js('Iher'), Js('Ijja'), Js('Ijju'), Js('Iken'), Js('Ikis'), Js('Ikken'), Js('Ikkis'), Js('Ikku'), Js('Ikles'), Js('Iksin'), Js('Ilalsan'), Js('Ilasen'), Js('Ilatig'), Js('Ilayetmas'), Js('Ilaytmas'), Js('Iles'), Js('Iletan'), Js('Ilila'), Js('Ilisen'), Js('Iliten'), Js('Iliz'), Js('Illil'), Js('Ilmen'), Js('Ilyas'), Js('Ilyes'), Js('Imar'), Js('Imilten'), Js('Imlul'), Js('Immas'), Js('Immeghar'), Js('Immel'), Js('Imrouch'), Js('Imruc'), Js('Imsen'), Js('Imsugar'), Js('Inarus'), Js('Indjen'), Js('Ingadh'), Js('Ingas'), Js('Ingras'), Js('Inguas'), Js('Inifel'), Js('Intasen'), Js('Ioues'), Js('Irat'), Js('Irate'), Js('Iraten'), Js('Irathen'), Js('Irenyan'), Js('Irgasen'), Js('Irgen'), Js('Irges'), Js('Irhad'), Js('Irjen'), Js('Irnas'), Js('Irnaten'), Js('Irnuhan'), Js('Irris'), Js('Irru'), Js('Irsas'), Js('Isam'), Js('Isan'), Js('Isdur'), Js('Isef'), Js('Isgaden'), Js('Isi'), Js('Isid'), Js('Isiguar'), Js('Iskel'), Js('Islasen'), Js('Isli'), Js('Isliten'), Js('Isragin'), Js('Isri'), Js('Issid'), Js('Isu'), Js('Isuda'), Js('Isugh'), Js('Isuhet'), Js('Isul'), Js('Isula'), Js('Itbir'), Js('Ithimbal'), Js('Ithri'), Js('Ithvir'), Js('Itisen'), Js('Itmasen'), Js('Itri'), Js('Itueft'), Js('Iufas'), Js('Iunam'), Js('Iwes'), Js('Ixfensen'), Js('Ixzi'), Js('Iylul'), Js('Izîl'), Js('Izar'), Js('Izdârasen'), Js('Izdeg'), Js('Izdyten'), Js('Izelta'), Js('Izem'), Js('Izemrasen'), Js('Izerdan'), Js('Izim'), Js('Izmerten'), Js('Izri'), Js('Izul'), Js('Izzou'), Js('Izzoul'), Js('Izzu'), Js('Izzul'), Js('Jeggi'), Js('Jenad'), Js('Jennad'), Js('Jerin'), Js('Jesna'), Js('Jeta'), Js('Jildun'), Js('Jilwa'), Js('Juba'), Js('Jugurtha'), Js('Jugurthen'), Js('Kaouar'), Js('Kaousen'), Js('Karakala'), Js('Kawar'), Js('Kawsen'), Js('Keffou'), Js('Keffu'), Js('Kenna'), Js('Koumaz'), Js('Kumaz'), Js('LGawda'), Js('Lyes'), Js('Maday'), Js('Madghan'), Js('Madghis'), Js('Madhil'), Js('Madidu'), Js('Madikum'), Js('Madin'), Js('Madjer'), Js('Madjkis'), Js('Madyen'), Js('Maggen'), Js('Magher'), Js('Maghus'), Js('Magsen'), Js('Mahha'), Js('Maius'), Js('Majen'), Js('Majer'), Js('Makoud'), Js('Makrin'), Js('Maksen'), Js('Makud'), Js('Makurgund'), Js('Makus'), Js('Malu'), Js('Mangelat'), Js('Maouel'), Js('Maoues'), Js('Maoui'), Js('Maqrin'), Js('Maqurtam'), Js('Marasen'), Js('Maray'), Js('Mardenic'), Js('Marin'), Js('Maris'), Js('Marksen'), Js('Marous'), Js('Marru'), Js('Marus'), Js('Masal'), Js('Masala'), Js('Masar'), Js('Masel'), Js('Masen'), Js('Masensen'), Js('Masezel'), Js('Masgaba'), Js('Masgawa'), Js('Masiden'), Js('Masidiqa'), Js('Masil'), Js('Masin'), Js('Masinas'), Js('Masinisan'), Js('Masinissa'), Js('Masiranis'), Js('Masiwa'), Js('Masiwan'), Js('Masmud'), Js('Masmul'), Js('Masnaf'), Js('Masnag'), Js('Masnsen'), Js('Mass'), Js('Massala'), Js('Massan'), Js('Massin'), Js('Massinissa'), Js('Massmoul'), Js('Massyl'), Js('Mastan'), Js('Mastanabal'), Js('Mastaw'), Js('Masthalul'), Js('Masthan'), Js('Mastias'), Js('Mastilus'), Js('Mastina'), Js('Masugrada'), Js('Masuna'), Js('Matenan'), Js('Mathu'), Js('Mathun'), Js('Matif'), Js('Matilam'), Js('Matzul'), Js('Mawel'), Js('Mawes'), Js('Mawi'), Js('Maydul'), Js('Mayen'), Js('Maysar'), Js('Mayyu'), Js('Mayzar'), Js('Mazdal'), Js('Mazer'), Js('Maziba'), Js('Mazifa'), Js('Mazigh'), Js('Mazipa'), Js('Mazit'), Js('Mazitula'), Js('Maziz'), Js('Mazuka'), Js('Meddour'), Js('Meddur'), Js('Meder'), Js('Medghasen'), Js('Medri'), Js('Medur'), Js('Megar'), Js('Meggen'), Js('Meghraw'), Js('Mehena'), Js('Mejdan'), Js('Mejqan'), Js('Mekra'), Js('Melag'), Js('Melal'), Js('Meld'), Js('Melkem'), Js('Mellal'), Js('Melloul'), Js('Mellul'), Js('Melwan'), Js('Menac'), Js('Menad'), Js('Menan'), Js('Mendas'), Js('Mendil'), Js('Mengelet'), Js('Menis'), Js('Menna'), Js('Mennad'), Js('Meqran'), Js('Merad'), Js('Meri'), Js('Merin'), Js('Mernis'), Js('Mernisa'), Js('Merwel'), Js('Merwul'), Js('Mesfaw'), Js('Meslagh'), Js('Meslata'), Js('Mesli'), Js('Mesrata'), Js('Mesray'), Js('Mestawa'), Js('Metus'), Js('Meuzer'), Js('Mezgeld'), Js('Mezian'), Js('Meztata'), Js('Mezura'), Js('Mezwar'), Js('Mezyan'), Js('Midrar'), Js('Migin'), Js('Mihemi'), Js('Mihi'), Js('Miknasa'), Js('Mikyusa'), Js('Mimum'), Js('Mindas'), Js('Mira'), Js('Misagen'), Js('Misagenes'), Js('Misibsen'), Js('Misifsen'), Js('Misunia'), Js('Mizri'), Js('Mizuar'), Js('Mizwar'), Js('Mliles'), Js('Mualat'), Js('Muda'), Js('Mula'), Js('Munatas'), Js('Muqran'), Js('Muthunbal'), Js('Muttun'), Js('Saden'), Js('Sisangh'), Js('Syphax'), Js('Tacfin'), Js('Takfarinas'), Js('Tanan'), Js('Tariq'), Js('Tasfin'), Js('Tiqfarin'), Js('Udad'), Js('Ugwistan'), Js('Uksintas'), Js('Usaden'), Js('Usem'), Js('Usus'), Js('Wimmiden'), Js('Winaruz'), Js('Winifsan'), Js('Winitran'), Js('Winsen'), Js('Winul'), Js('Wiwul'), Js('Wiwurgh'), Js('Yaba'), Js('Yabdas'), Js('Yadisgan'), Js('Yadras'), Js('Yafelman'), Js('Yafren'), Js('Yafu'), Js('Yaghmurasen'), Js('Yaghut'), Js('Yaksan'), Js('Yaktin'), Js('Yala'), Js('Yaleddes'), Js('Yam'), Js('Yanat'), Js('Yani'), Js('Yaru'), Js('Yasul'), Js('Yattuy'), Js('Yawus'), Js('Yazid'), Js('Yedder'), Js('Yeften'), Js('Yehlem'), Js('Yellel'), Js('Yemdu'), Js('Yemel'), Js('Yemlud'), Js('Yemlul'), Js('Yemsal'), Js('Yendu'), Js('Yeni'), Js('Yensal'), Js('Yerma'), Js('Yeru'), Js('Yidaw'), Js('Yidir'), Js('Yidthir'), Js('Yifiw'), Js('Yifrin'), Js('Yifruy'), Js('Yifsas'), Js('Yighis'), Js('Yiliyen'), Js('Yilyen'), Js('Yinay'), Js('Yinis'), Js('Yisisan'), Js('Yizdig'), Js('Yub'), Js('Yuba'), Js('Yudas'), Js('Yufan'), Js('Yufayyur'), Js('Yufitran'), Js('Yufitri'), Js('Yufran'), Js('Yuften'), Js('Yufthen'), Js('Yuger'), Js('Yugerten'), Js('Yughurten'), Js('Yughurtha'), Js('Yughurthen'), Js('Yugrazal'), Js('Yukus'), Js('Yukyan'), Js('Yula'), Js('Yulmes'), Js('Yuman'), Js('Yumas'), Js('Yunan'), Js('Yunas'), Js('Yunes'), Js('Yunus'), Js('Yur'), Js('Yurgasel'), Js('Yurman'), Js('Yursen'), Js('Yutaf'), Js('Ziri')]))
    var.put('nm2', Js([Js('Adjan'), Js('Aduda'), Js('Afou'), Js('Afu'), Js('Aggou'), Js('Aldjya'), Js('Amanan'), Js('Amanecer'), Js('Amenna'), Js('Amtziri'), Js('Anazra'), Js('Anella'), Js('Anida'), Js('Anisa'), Js('Anitan'), Js('Anya'), Js('Arrida'), Js('Arzeghnet'), Js('Asa'), Js('Asia'), Js('Asifa'), Js('Asigna'), Js('Auzia'), Js('Avedda'), Js('Awina'), Js('Awlima'), Js('Awrigha'), Js('Aya'), Js('Azel'), Js('Badida'), Js('Bagduda'), Js('Bahac'), Js('Bahha'), Js('Bahta'), Js('Bahtuta'), Js('Bakka'), Js('Bakra'), Js('Bamu'), Js('Banu'), Js('Basil'), Js('Bati'), Js('Batti'), Js('Battusa'), Js('Batul'), Js('Baya'), Js('Bbiya'), Js('Beghnat'), Js('Bejja'), Js('Bella'), Js('Benat'), Js('Bennina'), Js('Bergar'), Js('Berri'), Js('Berza'), Js('Bessa'), Js('Beszza'), Js('Bghnat'), Js('Bibya'), Js('Bittu'), Js('Brika'), Js('Buredyma'), Js('Buyan'), Js('Bysra'), Js('Cama'), Js('Cefa'), Js('Cettu'), Js('Chama'), Js('Chila'), Js('Cicma'), Js('Cila'), Js('Cilmuma'), Js('Cuca'), Js('Cucana'), Js('Dalila'), Js('Damya'), Js('Danna'), Js('Darbala'), Js('Dasenti'), Js('Dasin'), Js('Dasine'), Js('Dassa'), Js('Dassin'), Js('Dawn'), Js('Daya'), Js('Debira'), Js('Delenda'), Js('Delina'), Js('Dhoha'), Js('Diana'), Js('Dihinna'), Js('Dihya'), Js('Dila'), Js('Dimmida'), Js('Dimya'), Js('Djura'), Js('Dorisa'), Js('Drifa'), Js('Dudja'), Js('Duga'), Js('Fabia'), Js('Fadina'), Js('Fafa'), Js('Faghisa'), Js('Fariza'), Js('Fasa'), Js('Feddada'), Js('Fella'), Js('Feriel'), Js('Ferrudja'), Js('Fettuch'), Js('Filadelfa'), Js('Fina'), Js('Flysa'), Js('Foras'), Js('Frara'), Js('Fuda'), Js('Gadda'), Js('Gava'), Js('Gawa'), Js('Gaya'), Js('Gayet'), Js('Geldasen'), Js('Geldasent'), Js('Gemala'), Js('Ghadda'), Js('Ghamima'), Js('Ghella'), Js('Ghennou'), Js('Ghennu'), Js('Ghida'), Js('Ghighda'), Js('Ghnima'), Js('Giva'), Js('Gourara'), Js('Gouraya'), Js('Grica'), Js('Grisa'), Js('Grisha'), Js('Guedduda'), Js('Guellala'), Js('Guema'), Js('Gulusa'), Js('Guraya'), Js('Gwejda'), Js('Gwejdthi'), Js("H'edda"), Js('Habbu'), Js('Hadda'), Js('Hallu'), Js('Hannou'), Js('Hannu'), Js('Hatita'), Js('Hayda'), Js('Haylana'), Js('Haysu'), Js('Hazza'), Js('Hbiya'), Js('Hbuba'), Js('Hdiza'), Js('Heddou'), Js('Heddu'), Js('Hedduga'), Js('Hedduz'), Js('Heka'), Js('Hella'), Js('Hemma'), Js('Hemmusa'), Js('Hennu'), Js('Hennuba'), Js('Hennuz'), Js('Herri'), Js('Herru'), Js('Hetta'), Js('Hezzu'), Js('Hibba'), Js('Hmija'), Js('Hnata'), Js('Hsiba'), Js('Huda'), Js('Ifsan'), Js('Ihemma'), Js('Ijja'), Js('Ijju'), Js('Ikkou'), Js('Ikku'), Js('Illi'), Js('Ilma'), Js('Inas'), Js('Indi'), Js('Inina'), Js('Isfra'), Js('Iszza'), Js('Iszzu'), Js('Itran'), Js('Itri'), Js('Ittû'), Js('Ittou'), Js('Ittuba'), Js('Ittuna'), Js('Iza'), Js('Izelta'), Js('Izya'), Js('Izza'), Js('Jasmin'), Js('Jdira'), Js('Jeddjiga'), Js('Jella'), Js('Kahina'), Js('Kanimana'), Js('Kassu'), Js('Kejjou'), Js('Kella'), Js('Kellou'), Js('Kellu'), Js('Kemicha'), Js('Kenna'), Js('Kenwa'), Js('Keslala'), Js('Kettou'), Js('Kettu'), Js('Kinsa'), Js('Kisa'), Js('Ksou'), Js('Ksu'), Js('Kulla'), Js('Kwella'), Js('Kweller'), Js('Laddu'), Js('Lahna'), Js('Lalla'), Js('Laysa'), Js('Lebeda'), Js('Lemta'), Js('Lhiva'), Js('Lila'), Js('Lilia'), Js('Ljida'), Js('Lmiara'), Js('Louiza'), Js('Loula'), Js('Louna'), Js('Loundja'), Js('Lula'), Js('Lumsi'), Js('Luna'), Js('Lundja'), Js('Lunja'), Js('Lwiza'), Js('Lyaqut'), Js('Macina'), Js('Maciva'), Js('Mada'), Js('Madel'), Js('Madila'), Js('Magara'), Js('Magiva'), Js('Maira'), Js("Malh'a"), Js('Malida'), Js('Malika'), Js('Maliza'), Js('Mamma'), Js('Mammas'), Js('Mannet'), Js('Maria'), Js('Markounda'), Js('Markunda'), Js('Marniza'), Js('Maryama'), Js('Masa'), Js('Masana'), Js('Masilah'), Js('Masilya'), Js('Masiva'), Js('Massa'), Js('Massila'), Js('Massilya'), Js('Matugez'), Js('Mazika'), Js('Mazzi'), Js('Medousa'), Js('Megdila'), Js('Megduda'), Js('Meghighda'), Js('Meghnisa'), Js('Melilla'), Js('Mella'), Js('Mellala'), Js('Mellisa'), Js('Mellula'), Js('Melluya'), Js('Meluna'), Js('Meluza'), Js('Menna'), Js('Mennoune'), Js('Mennun'), Js('Menza'), Js('Meriem'), Js('Merkida'), Js('Mermusa'), Js('Mesraya'), Js('Messuna'), Js('Metila'), Js('Metira'), Js('Metuza'), Js('Mezifa'), Js('Mighisa'), Js('Milda'), Js('Milla'), Js('Mimouna'), Js('Mimuna'), Js('Mimunt'), Js('Mina'), Js('Mira'), Js('Mirina'), Js('Mlila'), Js('Mnahou'), Js('Mnahu'), Js('Mouli'), Js('Mririda'), Js('Muda'), Js('Muli'), Js('Muna'), Js('MuniMouni'), Js('MuniMunia'), Js('Munia'), Js('Muzaya'), Js('Myasa'), Js('Myriam'), Js('Nadia'), Js('Nanna'), Js('Nefza'), Js('Nora'), Js('Nounja'), Js('Nuja'), Js('Numa'), Js('Nundina'), Js('Nundja'), Js('Nunja'), Js('Nura'), Js('Nuva'), Js('Onesa'), Js('Ouba'), Js('Oudda'), Js('Ouna'), Js('Ouzza'), Js('Qayda'), Js('Qejju'), Js('Qezzu'), Js('Qura'), Js('Raisa'), Js('Randja'), Js('Rate'), Js('Reghisa'), Js('Reqima'), Js('Riga'), Js('Romana'), Js('Rqiyya'), Js('Ruza'), Js('Rziqa'), Js('Sabu'), Js('Sadra'), Js('Salsa'), Js('Sama'), Js('Satna'), Js('Sedrata'), Js('Sedura'), Js('Sefuya'), Js('Segguma'), Js('Sekkura'), Js('Selina'), Js('Setti'), Js('Sifa'), Js('Siga'), Js('Silina'), Js('Silya'), Js('Silyuna'), Js('Siman'), Js('Sinim'), Js('Siniman'), Js('Skikda'), Js('Skura'), Js('Slima'), Js('Sula'), Js('Sura'), Js('Susa'), Js('Susaa'), Js('Syna'), Js('Syra'), Js('Szidhant'), Js('Taballout'), Js('Taballutt'), Js('Tabaynutt'), Js('Tabayount'), Js('Tabayt'), Js('Tabbayt'), Js('Tabuhayt'), Js('Tacelvat'), Js('Tacemayt'), Js('Tachnout'), Js('Tacia'), Js('Tacnut'), Js('Tadêfi'), Js('Tadda'), Js('Taderfit'), Js('Tadla'), Js('Tadmut'), Js('Tafalkayt'), Js('Tafat'), Js('Tafenda'), Js('Taferrujt'), Js('Taffugt'), Js('Tafira'), Js('Tafna'), Js('Tafrara'), Js('Tafsut'), Js('Tafukt'), Js('Tafza'), Js('Tagafayt'), Js('Tagama'), Js('Taganint'), Js('Taghbalout'), Js('Taghbalut'), Js('Taghit'), Js('Tagoura'), Js('Tagrert'), Js('Tagura'), Js('Tagwerramt'), Js('Tagwilalt'), Js('Tagwillult'), Js('Tagwizult'), Js('Taheyyâtt'), Js('Tahouska'), Js('Tahu'), Js('Tahuska'), Js('Tajeddigt'), Js('Tajedjigt'), Js('Takama'), Js('Takawit'), Js('Takensust'), Js('Takfa'), Js('Taklit'), Js('Taknarit'), Js('Takouba'), Js('Taksimt'), Js('Takuka'), Js('Tala'), Js('Talalit'), Js('Taliza'), Js('Taljat'), Js('Talsa'), Js('Talut'), Js('Talwa'), Js('Talwit'), Js('Tama'), Js('Tamada'), Js('Tamalut'), Js('Tamanart'), Js('Tamanga'), Js('Tamaynut'), Js('Tamayourt'), Js('Tamayurt'), Js('Tamayyurt'), Js('Tamazight'), Js('Tamazuzt'), Js('Tamazzalt'), Js('Tameddourt'), Js('Tameddurt'), Js('Tamella'), Js('Tamellalt'), Js('Tamemt'), Js('Tamenna'), Js('Tament'), Js('Tamenzut'), Js('Tameqrant'), Js('Tamesmûtt'), Js('Tamezyant'), Js('Tamilla'), Js('Tamimt'), Js('Tamimunt'), Js('Taminda'), Js('Tamment'), Js('Tamnayt'), Js('Tamou'), Js('Tamrust'), Js('Tamrut'), Js('Tamseggint'), Js('Tamsoult'), Js('Tamsult'), Js('Tamu'), Js('Tamunt'), Js('Tamyourt'), Js('Tamyurt'), Js('Tanamart'), Js('Tanazârt'), Js('Tanebdatt'), Js('Tanefzawit'), Js('Tanemghurt'), Js('Tanest'), Js('Tanga'), Js('Tanifa'), Js('Tanilla'), Js('Taninna'), Js('Tanirt'), Js('Tanit'), Js('Tannar'), Js('Tannes'), Js('Tannirt'), Js('Tansaw'), Js('Taoua'), Js('Taouala'), Js('Taouri'), Js('Taqnart'), Js('Tara'), Js('Tarast'), Js('Tarenza'), Js('Tariwelt'), Js('Tarounga'), Js('Tarunga'), Js('Tarza'), Js('Tasa'), Js('Tasafut'), Js('Tasekkourt'), Js('Tasekkurt'), Js('Tasra'), Js('Tata'), Js('Tatam'), Js('Tatas'), Js('Tatbirt'), Js('Tati'), Js('Tawa'), Js('Tawala'), Js('Taweckint'), Js('Tawenza'), Js('Tawizet'), Js('Tawnat'), Js('Tawri'), Js('Tawzalt'), Js('Taya'), Js('Taylalt'), Js('Tayma'), Js('Tayri'), Js('Tayttutt'), Js('Tayyurt'), Js('Tazêllayt'), Js('Tazdayt'), Js('Tazenkêt'), Js('Tazenkwêt'), Js('Tazerwalt'), Js('Tazibba'), Js('Tazikit'), Js('Tazirit'), Js('Tazoula'), Js('Tazrurt'), Js('Tazrzît'), Js('Tazrzit'), Js('Tazula'), Js('Tazwart'), Js('Tecwwa'), Js('Tedus'), Js('Telgoumas'), Js('Telgumas'), Js('Telil'), Js('Tella'), Js('Temlud'), Js('Teriel'), Js('Tersheddat'), Js('Tfit'), Js('Tfoulla'), Js('Tfulla'), Js('Thablalt'), Js('Thadfi'), Js('Thadmuth'), Js('Thafat'), Js('Thafrara'), Js('Thafrirth'), Js('Thafsilt'), Js('Thaladza'), Js('Thalsa'), Js('Thamazuzt'), Js('Thamelle'), Js('Thamemt'), Js('Thamrusth'), Js('Thanaya'), Js('Thannina'), Js('Thasa'), Js('Thasnutt'), Js('Thasrifa'), Js('Thati'), Js('Thawant'), Js('Thawles'), Js('Thayda'), Js('Thazert'), Js('Themsal'), Js('Thengadh'), Js('Therna'), Js('Thersum'), Js('Theslas'), Js('Thidaw'), Js('Thidir'), Js('Thifa'), Js('Thifawth'), Js('Thifrar'), Js('Thifruy'), Js('Thighlan'), Js('Thighlas'), Js('Thigis'), Js('Thigwmi'), Js('Thikisa'), Js('Thikwinas'), Js('Thilelli'), Js('Thimsal'), Js('Thinezwa'), Js('Thinifsan'), Js('Thinmal'), Js('Thinufa'), Js('Thinuzal'), Js('Thinzerth'), Js('Thirnis'), Js('Thisent'), Js('Thisisn'), Js('Thiska'), Js('Thislas'), Js('Thislith'), Js('Thithvirth'), Js('Thiyefsan'), Js('Thiynay'), Js('Thiyya'), Js('Thizemth'), Js('Thiziri'), Js('Thuda'), Js('Thudjin'), Js('Thufran'), Js('Thula'), Js('Thumas'), Js('Thumer'), Js('Thunsa'), Js('Thurda'), Js('Thureghth'), Js('Thurnan'), Js('Thusa'), Js('Tichi'), Js('Tidar'), Js('Tidda'), Js('Tidghas'), Js('Tidir'), Js('Tidmi'), Js('Tidnas'), Js('Tifa'), Js('Tifagour'), Js('Tifagur'), Js('Tifawt'), Js('Tifayour'), Js('Tifayur'), Js('Tifirellest'), Js('Tifna'), Js('Tifsa'), Js('Tiga'), Js('Tiggi'), Js('Tigmi'), Js('Tigzi'), Js('Tihusay'), Js('Tikinas'), Js('Tilelli'), Js('Tililoua'), Js('Tililwa'), Js('Tilla'), Js('Tilleli'), Js('Tima'), Js('Timan'), Js('Timellet'), Js('Timla'), Js('Timmi'), Js('Timya'), Js('Tin'), Js('Tin Hinan'), Js('Tina'), Js('Tinamer'), Js('Tindaya'), Js('Tinef'), Js('Tinezwa'), Js('Tinga'), Js('Tingh'), Js('Tinghan'), Js('Tinhinan'), Js('Tinifsan'), Js('Tinitran'), Js('Tinounzar'), Js('Tinsin'), Js('Tintadêfi'), Js('Tintafoukt'), Js('Tintafukt'), Js('Tintayri'), Js('Tintfsut'), Js('Tintifawin'), Js('Tintlelli'), Js('Tintziri'), Js('Tinunzar'), Js('Tinwurgh'), Js('Tinyour'), Js('Tinyur'), Js('Tinza'), Js('Tinzert'), Js('Tiriya'), Js('Tisent'), Js('Tisila'), Js('Tiska'), Js('Tiski'), Js('Tislanzar'), Js('Tislas'), Js('Tislit'), Js('Tistina'), Js('Titem'), Js('Titma'), Js('Titrit'), Js('Tiwul'), Js('Tizdig'), Js('Tizemt'), Js('Tizenga'), Js('Tiziri'), Js('Tizma'), Js('Tizoua'), Js('Tizwa'), Js('Tlafulki'), Js('Tlaten'), Js('Tlatig'), Js('Tlayt'), Js('Tlaytmas'), Js('Toucha'), Js('Touda'), Js('Toudert'), Js('Toufayour'), Js('Toufitri'), Js('Toufrint'), Js('Tougga'), Js('Tougna'), Js('Touka'), Js('Toukfa'), Js('Toukyist'), Js('Toula'), Js('Toumert'), Js('Tounarouz'), Js('Touncha'), Js('Triya'), Js('Tseriel'), Js('Tsul'), Js('Tuca'), Js('Tucka'), Js('Tuda'), Js('Tudatt'), Js('Tudert'), Js('Tufayyur'), Js('Tufinet'), Js('Tufitran'), Js('Tufitri'), Js('Tufrint'), Js('Tuftafukt'), Js('Tuftent'), Js('Tuftifawt'), Js('Tufulla'), Js('Tugertent'), Js('Tugga'), Js('Tugna'), Js('Tuka'), Js('Tukyist'), Js('Tula'), Js('Tumadir'), Js('Tumart'), Js('Tumas'), Js('Tumert'), Js('Tunaruz'), Js('Tunca'), Js('Tureght'), Js('Tzeddig'), Js('Tzil'), Js('Tzila'), Js('Uba'), Js('Udda'), Js('Ultafa'), Js('Ultasila'), Js('Uminet'), Js('Una'), Js('Unifa'), Js('Urika'), Js('Urtaghir'), Js('Urtedus'), Js('Usa'), Js('Usila'), Js('Uudda'), Js('Uza'), Js('Uzia'), Js('Uzna'), Js('Uzza'), Js('Uzzah'), Js('Watila'), Js('Wedira'), Js('WenzOenza'), Js('Wesina'), Js('Wezna'), Js('Wigelden'), Js('Wiza'), Js('Wnisa'), Js('Wrina'), Js('Xelludja'), Js('Xuda'), Js('Yamina'), Js('Yamma'), Js('Yarra'), Js('Yasmin'), Js('Yellana'), Js('Yettou'), Js('Yettu'), Js('Yezzi'), Js('Yilda'), Js('Zahra'), Js('Zamra'), Js('Zana'), Js('Zara'), Js('Zawgha'), Js('Zediga'), Js('Zefra'), Js('Zeggula'), Js('Zegna'), Js('Zegura'), Js('Zelgoum'), Js('Zelgum'), Js('Zennou'), Js('Zennu'), Js('Zennuba'), Js('Zergha'), Js('Zibba'), Js('Zidant'), Js('Zila'), Js('Zilgoum'), Js('Zilgum'), Js('Zineb'), Js('Zira'), Js('Znina'), Js('Zouara'), Js('Zunagha'), Js('Zunja'), Js('Zwara'), Js('Zwina'), Js('Zwira')]))
    var.put('nm3', Js([Js('Abad'), Js('Abbas'), Js('Abbasi'), Js('Abdalla'), Js('Abdallah'), Js('Abdella'), Js('Abdelnour'), Js('Abdelrahman'), Js('Abdi'), Js('Abdo'), Js('Abdoo'), Js('Abdou'), Js('Abdul'), Js('Abdulla'), Js('Abdullah'), Js('Abed'), Js('Abid'), Js('Abood'), Js('Aboud'), Js('Abraham'), Js('Abu'), Js('Adel'), Js('Afzal'), Js('Agha'), Js('Ahmad'), Js('Ahmadi'), Js('Ahmed'), Js('Ahsan'), Js('Akbar'), Js('Akbari'), Js('Akel'), Js('Akhtar'), Js('Akhter'), Js('Akram'), Js('Alam'), Js('Ali'), Js('Allam'), Js('Allee'), Js('Alli'), Js('Ally'), Js('Aly'), Js('Aman'), Js('Amara'), Js('Amber'), Js('Ameen'), Js('Amen'), Js('Amer'), Js('Amin'), Js('Amini'), Js('Amir'), Js('Amiri'), Js('Ammar'), Js('Ansari'), Js('Anwar'), Js('Arafat'), Js('Arif'), Js('Arshad'), Js('Asad'), Js('Ashraf'), Js('Aslam'), Js('Asmar'), Js('Assad'), Js('Assaf'), Js('Atallah'), Js('Attar'), Js('Awan'), Js('Aydin'), Js('Ayoob'), Js('Ayoub'), Js('Ayub'), Js('Azad'), Js('Azam'), Js('Azer'), Js('Azimi'), Js('Aziz'), Js('Azizi'), Js('Azzam'), Js('Azzi'), Js('Bacchus'), Js('Baccus'), Js('Bacho'), Js('Baddour'), Js('Badie'), Js('Badour'), Js('Bagheri'), Js('Bahri'), Js('Baig'), Js('Baksh'), Js('Baluch'), Js('Bangura'), Js('Barakat'), Js('Bari'), Js('Basa'), Js('Basha'), Js('Bashara'), Js('Basher'), Js('Bashir'), Js('Baten'), Js('Begum'), Js('Ben'), Js('Beshara'), Js('Bey'), Js('Beydoun'), Js('Bilal'), Js('Bina'), Js('Burki'), Js('Can'), Js('Chahine'), Js('Dada'), Js('Dajani'), Js('Dallal'), Js('Daoud'), Js('Dar'), Js('Darwish'), Js('Dawood'), Js('Demian'), Js('Dia'), Js('Diab'), Js('Dib'), Js('Din'), Js('Doud'), Js('Ebrahim'), Js('Ebrahimi'), Js('Edris'), Js('Eid'), Js('Elamin'), Js('Elbaz'), Js('El-Sayed'), Js('Emami'), Js('Fadel'), Js('Fahmy'), Js('Fahs'), Js('Farag'), Js('Farah'), Js('Faraj'), Js('Fares'), Js('Farha'), Js('Farhat'), Js('Farid'), Js('Faris'), Js('Farman'), Js('Farooq'), Js('Farooqui'), Js('Farra'), Js('Farrah'), Js('Farran'), Js('Fawaz'), Js('Fayad'), Js('Firman'), Js('Gaber'), Js('Gad'), Js('Galla'), Js('Ghaffari'), Js('Ghanem'), Js('Ghani'), Js('Ghattas'), Js('Ghazal'), Js('Ghazi'), Js('Greiss'), Js('Guler'), Js('Habeeb'), Js('Habib'), Js('Habibi'), Js('Hadi'), Js('Hafeez'), Js('Hai'), Js('Haidar'), Js('Haider'), Js('Hakeem'), Js('Hakim'), Js('Halaby'), Js('Halim'), Js('Hallal'), Js('Hamad'), Js('Hamady'), Js('Hamdan'), Js('Hamed'), Js('Hameed'), Js('Hamid'), Js('Hamidi'), Js('Hammad'), Js('Hammoud'), Js('Hana'), Js('Hanif'), Js('Hannan'), Js('Haq'), Js('Haque'), Js('Hares'), Js('Hariri'), Js('Harron'), Js('Harroun'), Js('Hasan'), Js('Hasen'), Js('Hashem'), Js('Hashemi'), Js('Hashim'), Js('Hashmi'), Js('Hassan'), Js('Hassen'), Js('Hatem'), Js('Hoda'), Js('Hoque'), Js('Hosein'), Js('Hossain'), Js('Hosseini'), Js('Huda'), Js('Huq'), Js('Husain'), Js('Hussain'), Js('Hussein'), Js('Ibrahim'), Js('Idris'), Js('Imam'), Js('Iman'), Js('Iqbal'), Js('Irani'), Js('Ishak'), Js('Ishmael'), Js('Islam'), Js('Ismael'), Js('Ismail'), Js('Jabara'), Js('Jabbar'), Js('Jabbour'), Js('Jaber'), Js('Jabour'), Js('Jafari'), Js('Jaffer'), Js('Jafri'), Js('Jalali'), Js('Jalil'), Js('Jama'), Js('Jamail'), Js('Jamal'), Js('Jamil'), Js('Jan'), Js('Javed'), Js('Javid'), Js('Kaba'), Js('Kaber'), Js('Kabir'), Js('Kader'), Js('Kaiser'), Js('Kaleel'), Js('Kalil'), Js('Kamal'), Js('Kamali'), Js('Kamara'), Js('Kamel'), Js('Kanan'), Js('Karam'), Js('Karim'), Js('Karimi'), Js('Kassem'), Js('Kazemi'), Js('Kazi'), Js('Kazmi'), Js('Khalaf'), Js('Khalid'), Js('Khalifa'), Js('Khalil'), Js('Khalili'), Js('Khan'), Js('Khatib'), Js('Khawaja'), Js('Koroma'), Js('Laham'), Js('Latif'), Js('Lodi'), Js('Lone'), Js('Madani'), Js('Mady'), Js('Mahdavi'), Js('Mahdi'), Js('Mahfouz'), Js('Mahmood'), Js('Mahmoud'), Js('Mahmud'), Js('Majeed'), Js('Majid'), Js('Malak'), Js('Malek'), Js('Malik'), Js('Mannan'), Js('Mansoor'), Js('Mansour'), Js('Mansouri'), Js('Mansur'), Js('Maroun'), Js('Masih'), Js('Masood'), Js('Masri'), Js('Massoud'), Js('Matar'), Js('Matin'), Js('Mattar'), Js('Meer'), Js('Meskin'), Js('Miah'), Js('Mian'), Js('Mina'), Js('Minhas'), Js('Mir'), Js('Mirza'), Js('Mitri'), Js('Moghaddam'), Js('Mohamad'), Js('Mohamed'), Js('Mohammad'), Js('Mohammadi'), Js('Mohammed'), Js('Mohiuddin'), Js('Molla'), Js('Momin'), Js('Mona'), Js('Morad'), Js('Moradi'), Js('Mostafa'), Js('Mourad'), Js('Mousa'), Js('Moussa'), Js('Moustafa'), Js('Mowad'), Js('Muhammad'), Js('Muhammed'), Js('Munir'), Js('Murad'), Js('Musa'), Js('Mussa'), Js('Mustafa'), Js('Naderi'), Js('Nagi'), Js('Naim'), Js('Naqvi'), Js('Nasir'), Js('Nasr'), Js('Nasrallah'), Js('Nasser'), Js('Nassif'), Js('Nawaz'), Js('Nazar'), Js('Nazir'), Js('Neman'), Js('Niazi'), Js('Noor'), Js('Noorani'), Js('Noori'), Js('Nour'), Js('Nouri'), Js('Obeid'), Js('Odeh'), Js('Omar'), Js('Omer'), Js('Othman'), Js('Ozer'), Js('Parsa'), Js('Pasha'), Js('Pashia'), Js('Pirani'), Js('Popal'), Js('Pour'), Js('Qadir'), Js('Qasim'), Js('Qazi'), Js('Quadri'), Js('Raad'), Js('Rabbani'), Js('Rad'), Js('Radi'), Js('Radwan'), Js('Rafiq'), Js('Rahaim'), Js('Rahaman'), Js('Rahim'), Js('Rahimi'), Js('Rahman'), Js('Rahmani'), Js('Rais'), Js('Ramadan'), Js('Ramin'), Js('Rashed'), Js('Rasheed'), Js('Rashid'), Js('Rassi'), Js('Rasul'), Js('Rauf'), Js('Rayes'), Js('Rehman'), Js('Rehmann'), Js('Reza'), Js('Riaz'), Js('Rizk'), Js('Saab'), Js('Saad'), Js('Saade'), Js('Saadeh'), Js('Saah'), Js('Saba'), Js('Saber'), Js('Sabet'), Js('Sabir'), Js('Sadek'), Js('Sader'), Js('Sadiq'), Js('Sadri'), Js('Saeed'), Js('Safar'), Js('Safi'), Js('Sahli'), Js('Saidi'), Js('Sala'), Js('Salaam'), Js('Saladin'), Js('Salah'), Js('Salahuddin'), Js('Salam'), Js('Salama'), Js('Salame'), Js('Salameh'), Js('Saleem'), Js('Saleh'), Js('Salehi'), Js('Salek'), Js('Salem'), Js('Salih'), Js('Salik'), Js('Salim'), Js('Salloum'), Js('Salman'), Js('Samaan'), Js('Samad'), Js('Samara'), Js('Sami'), Js('Samra'), Js('Sani'), Js('Sarah'), Js('Sarwar'), Js('Sattar'), Js('Satter'), Js('Sawaya'), Js('Sayed'), Js('Selim'), Js('Semaan'), Js('Sesay'), Js('Shaban'), Js('Shabazz'), Js('Shad'), Js('Shaer'), Js('Shafi'), Js('Shah'), Js('Shahan'), Js('Shaheed'), Js('Shaheen'), Js('Shahid'), Js('Shahidi'), Js('Shahin'), Js('Shaikh'), Js('Shaker'), Js('Shakir'), Js('Shakoor'), Js('Sham'), Js('Shams'), Js('Sharaf'), Js('Shareef'), Js('Sharif'), Js('Shariff'), Js('Sharifi'), Js('Shehadeh'), Js('Shehata'), Js('Sheikh'), Js('Siddiqi'), Js('Siddique'), Js('Siddiqui'), Js('Sinai'), Js('Soliman'), Js('Soltani'), Js('Srour'), Js('Sulaiman'), Js('Suleiman'), Js('Sultan'), Js('Sultana'), Js('Syed'), Js('Sylla'), Js('Tabatabai'), Js('Tabet'), Js('Taha'), Js('Taheri'), Js('Tahir'), Js('Tamer'), Js('Tariq'), Js('Tawil'), Js('Toure'), Js('Turay'), Js('Uddin'), Js('Ullah'), Js('Usman'), Js('Vaziri'), Js('Vohra'), Js('Wahab'), Js('Wahba'), Js('Waheed'), Js('Wakim'), Js('Wali'), Js('Yacoub'), Js('Yamin'), Js('Yasin'), Js('Yassin'), Js('Younan'), Js('Younes'), Js('Younis'), Js('Yousef'), Js('Yousif'), Js('Youssef'), Js('Yousuf'), Js('Yusuf'), Js('Zadeh'), Js('Zafar'), Js('Zaher'), Js('Zahra'), Js('Zaidi'), Js('Zakaria'), Js('Zaki'), Js('Zaman'), Js('Zamani'), Js('Zia')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
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
amazighNames = var.to_python()