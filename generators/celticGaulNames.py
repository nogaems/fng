__all__ = ['celticGaulNames']

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
    var.registers(['nm1', 'nm2', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Acedillus'), Js('Acedilu'), Js('Adbitus'), Js('Adcanaunos'), Js('Adcomaros'), Js('Adebugi'), Js('Adebugius'), Js('Adgennus'), Js('Adgenus'), Js('Adginnius'), Js('Adiatorix'), Js('Adiatumarus'), Js('Adietuanus'), Js('Adietumarus'), Js('Admatius'), Js('Adnamati'), Js('Adnamatius'), Js('Adnamatus'), Js('Adretilis'), Js('Adrotus'), Js('Advorix'), Js('Aesarius'), Js('Agedilicus'), Js('Agedilio'), Js('Agedilios'), Js('Agedilli'), Js('Agedillus'), Js('Agedovirus'), Js('Agisilius'), Js('Agisillus'), Js('Aicovindo'), Js('Aisus'), Js('Albic'), Js('Albius'), Js('Albus'), Js('Alebece'), Js('Allecnus'), Js('Allinus'), Js('Allobroxus'), Js('Allovico'), Js('Alluci'), Js('Allucius'), Js('Alpius'), Js('Alpus'), Js('Ambadus'), Js('Ambaxius'), Js('Ambilli'), Js('Ambillus'), Js('Ambilo'), Js('Ambilos'), Js('Ambimogidus'), Js('Ambisauus'), Js('Ambisavus'), Js('Ambudsuilus'), Js('Andangi'), Js('Andecarius'), Js('Andecarus'), Js('Andegalli'), Js('Andegasi'), Js('Andegasus'), Js('Andereseni'), Js('Andergi'), Js('Andergos'), Js('Andolatius'), Js('Andosion'), Js('Andosten'), Js('Andosteni'), Js('Andosteno'), Js('Andoston'), Js('Andreine'), Js('Anducor'), Js('Annamatus'), Js('Annamoris'), Js('Annamus'), Js('Antedrigus'), Js('Anteremius'), Js('Areobindus'), Js('Arimanus'), Js('Ateano'), Js('Atecilus'), Js('Atecurus'), Js('Ategnutis'), Js('Atepatus'), Js('Atepiccus'), Js('Ateponirus'), Js('Ateponius'), Js('Ateponus'), Js('Ateratos'), Js('Atesios'), Js('Atesmertus'), Js('Atesos'), Js('Atessatis'), Js('Atesso'), Js('Atestas'), Js('Ateuritus'), Js('Atgite'), Js('Atolisus'), Js('Atporix'), Js('Atrectius'), Js('Atrectus'), Js('Atregtius'), Js('Atrextus'), Js('Atrixtos'), Js('Attectius'), Js('Atuirus'), Js('Atusonius'), Js('Audatus'), Js('Audeti'), Js('Audoenus'), Js('Audoti'), Js('Aventinius'), Js('Aventinus'), Js('Balaesus'), Js('Balatonux'), Js('Balorix'), Js('Banni'), Js('Bannio'), Js('Banu'), Js('Banui'), Js('Banuillus'), Js('Banuo'), Js('Banuus'), Js('Bellognatus'), Js('Bilicedo'), Js('Biliureto'), Js('Billiccissioni'), Js('Billicedo'), Js('Birucatus'), Js('Bocontius'), Js('Bodenia'), Js('Bodocenos'), Js('Bodocenus'), Js('Boduogenus'), Js('Bogionius'), Js('Borili'), Js('Borillus'), Js('Boritus'), Js('Borso'), Js('Borsus'), Js('Boruonicus'), Js('Borvonicus'), Js('Boudillus'), Js('Bravecci'), Js('Brigomaglos'), Js('Britomartis'), Js('Britomartus'), Js('Brocchus'), Js('Broccius'), Js('Broccus'), Js('Bussumarius'), Js('Bussumarus'), Js('Busturo'), Js('Butiro'), Js('Buturo'), Js('Cabriabantos'), Js('Cabrus'), Js('Caccuso'), Js('Cacurio'), Js('Cacurius'), Js('Cambo'), Js('Cambulus'), Js('Cambus'), Js('Camerianus'), Js('Camerinus'), Js('Camulatucus'), Js('Camulixus'), Js('Camulorigi'), Js('Caracco'), Js('Caracus'), Js('Caraddounius'), Js('Caraddounus'), Js('Caramantius'), Js('Carantacus'), Js('Carantillo'), Js('Caranto'), Js('Carantorius'), Js('Carasius'), Js('Carathounus'), Js('Caratillus'), Js('Caratodius'), Js('Cariaus'), Js('Carigo'), Js('Carigus'), Js('Carino'), Js('Carisianus'), Js('Caritosus'), Js('Carix'), Js('Caromarus'), Js('Carominius'), Js('Carucenus'), Js('Carugenus'), Js('Carulirus'), Js('Cassicius'), Js('Cassicus'), Js('Cassitalus'), Js('Cassutus'), Js('Castonius'), Js('Catabar'), Js('Catacius'), Js('Catacus'), Js('Catamandus'), Js('Catamanus'), Js('Catavignus'), Js('Caterto'), Js('Cathirix'), Js('Caticorix'), Js('Catinius'), Js('Catlus'), Js('Catonianus'), Js('Catotigirni'), Js('Catoualos'), Js('Cattabbot'), Js('Cattabus'), Js('Cattabuttas'), Js('Cattaus'), Js('Cattedius'), Js('Cattulus'), Js('Cattuvir'), Js('Cattuvvir'), Js('Catuen'), Js('Catuenus'), Js('Caturicus'), Js('Caturo'), Js('Catusius'), Js('Caurius'), Js('Caurus'), Js('Cenalus'), Js('Cenicus'), Js('Cenno'), Js('Ceno'), Js('Cenocantus'), Js('Centugeni'), Js('Centus'), Js('Cicedu'), Js('Cimarius'), Js('Cimarus'), Js('Cinge'), Js('Cinges'), Js('Cingessus'), Js('Cingetoutus'), Js('Cingius'), Js('Cintio'), Js('Cinto'), Js('Cintu'), Js('Cintugenus'), Js('Cintumarus'), Js('Cintusminius'), Js('Coaeddus'), Js('Cobledulitauus'), Js('Cobledulitavus'), Js('Coimagni'), Js('Colomagni'), Js('Comanus'), Js('Comatullus'), Js('Combaromarus'), Js('Comnertus'), Js('Conbertius'), Js('Conbertus'), Js('Conconnetodumnus'), Js('Condarillus'), Js('Condercus'), Js('Coneddus'), Js('Congenno'), Js('Congonetiacus'), Js('Congonnetiacus'), Js('Conteddius'), Js('Contesilo'), Js('Contessilo'), Js('Contoutos'), Js('Convictolitavis'), Js('Corbagni'), Js('Corio'), Js('Cornutos'), Js('Coro'), Js('Corobus'), Js('Coteus'), Js('Cotilius'), Js('Cotillus'), Js('Cotilus'), Js('Cotis'), Js('Cotius'), Js('Cottalus'), Js('Cottilus'), Js('Cottio'), Js('Cottius'), Js('Cotto'), Js('Cottro'), Js('Cottus'), Js('Cotus'), Js('Cotusus'), Js('Couertomotul'), Js('Covertomotul'), Js('Covirius'), Js('Covirus'), Js('Criciro'), Js('Criciru'), Js('Cricirus'), Js('Crigiru'), Js('Cunegni'), Js('Cunigni'), Js('Cunovicodu'), Js('Curcagni'), Js('Curcagnus'), Js('Dacotoutus'), Js('Dagillus'), Js('Dagobius'), Js('Dagomarus'), Js('Dalagni'), Js('Dannonus'), Js('Dano'), Js('Dattovir'), Js('Deoratus'), Js('Dercillos'), Js('Dercillus'), Js('Deuus'), Js('Devus'), Js('Diddignatus'), Js('Diocaitus'), Js('Diorix'), Js('Diuicatus'), Js('Divicatus'), Js('Divos'), Js('Dobagni'), Js('Doninas'), Js('Donnadu'), Js('Donnedo'), Js('Donnius'), Js('Donnotaurus'), Js('Donnus'), Js('Dovagni'), Js('Drutalus'), Js('Dubnotalus'), Js('Dubnovellaun'), Js('Dubnovellaunos'), Js('Dumnobellaunus'), Js('Dumnovellaunos'), Js('Ebicatos'), Js('Ebredus'), Js('Eburianus'), Js('Eburio'), Js('Eburius'), Js('Eburo'), Js('Elusco'), Js('Elusconos'), Js('Endouellicus'), Js('Endovellicus'), Js('Epacus'), Js('Epasius'), Js('Epatus'), Js('Epetinus'), Js('Epo'), Js('Epomedius'), Js('Epos'), Js('Epotsiorouidus'), Js('Epotsorouidus'), Js('Eppo'), Js('Eqqegni'), Js('Ercaviccas'), Js('Escengolatis'), Js('Escincos'), Js('Esumagius'), Js('Excingillius'), Js('Excingomarus'), Js('Excingullus'), Js('Exscincious'), Js('Exsomnus'), Js('Gabrius'), Js('Gabrus'), Js('Gedilli'), Js('Genetlus'), Js('Genillus'), Js('Gennalo'), Js('Girgani'), Js('Gnatusius'), Js('Grimiggni'), Js('Haesus'), Js('Iantasio'), Js('Iantinus'), Js('Iantumalius'), Js('Iantumar'), Js('Iantumarus'), Js('Iatinius'), Js('Iccalus'), Js('Iccinus'), Js('Iccnus'), Js('Icomius'), Js('Ientinus'), Js('Ientius'), Js('Iliatus'), Js('Illiomarus'), Js('Indercillus'), Js('Iotobito'), Js('Isarnouallanos'), Js('Itavus'), Js('Itosius'), Js('Itotagi'), Js('Lanianus'), Js('Laniogaius'), Js('Latauis'), Js('Leucamulo'), Js('Licno'), Js('Licnos'), Js('Licnus'), Js('Litauus'), Js('Litavis'), Js('Litgenes'), Js('Litgenus'), Js('Litigius'), Js('Litugenius'), Js('Lituriri'), Js('Losagni'), Js('Lucterius'), Js('Lugetus'), Js('Lugius'), Js('Lugurix'), Js('Macareus'), Js('Macarius'), Js('Maccarus'), Js('Maccis'), Js('Magiacos'), Js('Maglagni'), Js('Magurio'), Js('Magurius'), Js('Mailagni'), Js('Malucnus'), Js('Mando'), Js('Maritalus'), Js('Martalos'), Js('Martilinus'), Js('Martoualus'), Js('Meddignatius'), Js('Meddugnatus'), Js('Megaravico'), Js('Melmandus'), Js('Mertoualus'), Js('Mesillus'), Js('Messillus'), Js('Metilius'), Js('Metillius'), Js('Miletumarus'), Js('Moddagni'), Js('Nantonos'), Js('Nertomaros'), Js('Netacari'), Js('Nisigni'), Js('Oclicno'), Js('Oclicnos'), Js('Ollocnus'), Js('Ollognus'), Js('Onalisus'), Js('Oppianicnos'), Js('Perrius'), Js('Perrus'), Js('Peruincus'), Js('Perus'), Js('Qasigni'), Js('Qenilocgni'), Js('Regenos'), Js('Regenus'), Js('Regininus'), Js('Reginius'), Js('Reginus'), Js('Remico'), Js('Remicus'), Js('Reovalis'), Js('Reticius'), Js('Reticus'), Js('Retomarus'), Js('Rextugeos'), Js('Rigalis'), Js('Ripcicnus'), Js('Ritogenus'), Js('Rittuvvecc'), Js('Rituvvecas'), Js('Rovicus'), Js('Sacrovir'), Js('Sacrovirus'), Js('Sagillius'), Js('Sagillus'), Js('Samaconius'), Js('Samalus'), Js('Samio'), Js('Samis'), Js('Samius'), Js('Sammio'), Js('Sammo'), Js('Sammus'), Js('Samo'), Js('Samocenus'), Js('Samocinus'), Js('Samogenus'), Js('Samognatius'), Js('Samus'), Js('Sancotalus'), Js('Sanicios'), Js('Scilagni'), Js('Segolatius'), Js('Segomaros'), Js('Senecio'), Js('Senecius'), Js('Senocarus'), Js('Senovir'), Js('Senucaris'), Js('Silanus'), Js('Smertulitanus'), Js('Sollouico'), Js('Sollovico'), Js('Suadinus'), Js('Suadugenus'), Js('Suadutto'), Js('Suratus'), Js('Talagni'), Js('Talavus'), Js('Talis'), Js('Talius'), Js('Tallius'), Js('Tallus'), Js('Tallutius'), Js('Talotius'), Js('Talussanus'), Js('Talutius'), Js('Tanco'), Js('Tanotalos'), Js('Tarbunus'), Js('Taruiacus'), Js('Tascius'), Js('Tascus'), Js('Tasgetios'), Js('Tasgetius'), Js('Tauratis'), Js('Tauri'), Js('Taurio'), Js('Taurocutius'), Js('Taurou'), Js('Teutagonus'), Js('Teuto'), Js('Teutomalius'), Js('Teutomus'), Js('Totavali'), Js('Toutio'), Js('Touto'), Js('Toutobocio'), Js('Toutobocios'), Js('Toutos'), Js('Toutus'), Js('Trenacatus'), Js('Trenaccatlo'), Js('Triti'), Js('Trito'), Js('Tritos'), Js('Tritus'), Js('Trogimarus'), Js('Trouceteius'), Js('Tuticanius'), Js('Tuticanus'), Js('Ulcagni'), Js('Ulccagni'), Js('Urogenonertus'), Js('Valatonius'), Js('Valis'), Js('Vallio'), Js('Vallius'), Js('Vallo'), Js('Vallus'), Js('Vebro'), Js('Vebru'), Js('Vecatus'), Js('Vecconius'), Js('Vecius'), Js('Vectimarius'), Js('Vectimarus'), Js('Vecto'), Js('Velagenius'), Js('Velagenus'), Js('Velenius'), Js('Velitas'), Js('Velitius'), Js('Vello'), Js('Velugni'), Js('Velugnius'), Js('Vendagni'), Js('Vendogni'), Js('Venecarus'), Js('Venedius'), Js('Venextos'), Js('Venicarus'), Js('Venixamus'), Js('Venixxamus'), Js('Vennenus'), Js('Vennonius'), Js('Venucius'), Js('Vepotalus'), Js('Veqreq'), Js('Vercatus'), Js('Vercombogio'), Js('Vercombogious'), Js('Vercombogus'), Js('Versicnos'), Js('Versignos'), Js('Verter'), Js('Verto'), Js('Vertos'), Js('Vertros'), Js('Veruecco'), Js('Veruico'), Js('Veugnus'), Js('Vicatus'), Js('Vicixtillus'), Js('Victi'), Js('Viction'), Js('Vindedo'), Js('Vindicatus'), Js('Vinicarus'), Js('Vinovaleius'), Js('Viranus'), Js('Virato'), Js('Viratus'), Js('Viri'), Js('Viriacius'), Js('Viriaicus'), Js('Virianto'), Js('Viriatis'), Js('Viriatius'), Js('Virici'), Js('Virico'), Js('Viriodacus'), Js('Virisimi'), Js('Virlus'), Js('Virocantus'), Js('Vironianus'), Js('Virotalus'), Js('Virotutus'), Js('Vitousurix'), Js('Vlatcani'), Js('Vlatos'), Js('Vlatucni'), Js('Vlatucnos'), Js('Vlatugni'), Js('Vocagni'), Js('Vocarantus'), Js('Vocorix'), Js('Vogitoutus'), Js('Voltodaga'), Js('Vopiscus'), Js('Voretouirius'), Js('Voretoviros'), Js('Vosegus'), Js('Vridolanos'), Js('Vrittakos')]))
    var.put('nm2', Js([Js('Abrezta'), Js('Acca'), Js('Acisillia'), Js('Adbugiouna'), Js('Adbugissa'), Js('Adginna'), Js('Adgonna'), Js('Adiania'), Js('Adianta'), Js('Admata'), Js('Adnama'), Js('Adnamata'), Js('Adnamatia'), Js('Adnamita'), Js('Adnamu'), Js('Adreticia'), Js('Aduorix'), Js('Advorix'), Js('Aesica'), Js('Aesiua'), Js('Agedia'), Js('Agisiaca'), Js('Agisilia'), Js('Agisilla'), Js('Aisa'), Js('Albina'), Js('Albisia'), Js('Albucia'), Js('Aleasiumara'), Js('Alla'), Js('Alleicea'), Js('Alleticia'), Js('Allia'), Js('Allouira'), Js('Allusa'), Js('Alpina'), Js('Alpinia'), Js('Alpinula'), Js('Alteurita'), Js('Ambada'), Js('Andaitia'), Js('Andarta'), Js('Andebrocirix'), Js('Andeca'), Js('Anderca'), Js('Anderica'), Js('Anderina'), Js('Anderitia'), Js('Andilia'), Js('Andoca'), Js('Andueia'), Js('Anduenna'), Js('Annama'), Js('Ariola'), Js('Arrotala'), Js('Arsulana'), Js('Atebodua'), Js('Atectorigiana'), Js('Ategenta'), Js('Ategnissa'), Js('Atepa'), Js('Atepu'), Js('Atessatia'), Js('Atestatia'), Js('Atestia'), Js('Ateurita'), Js('Atigenta'), Js('Atioxta'), Js('Atreba'), Js('Atrebia'), Js('Attisaga'), Js('Atturita'), Js('Auamacimaria'), Js('Audata'), Js('Audenta'), Js('Auentina'), Js('Aulricmara'), Js('Aventina'), Js('Avitianomara'), Js('Balatonaua'), Js('Ballatulla'), Js('Banna'), Js('Bannua'), Js('Banona'), Js('Betudaca'), Js('Bileseton'), Js('Bilisa'), Js('Billia'), Js('Bimottia'), Js('Bitudaga'), Js('Bora'), Js('Borissa'), Js('Boudenna'), Js('Boudilla'), Js('Boudinna'), Js('Brocchia'), Js('Brogimara'), Js('Buscilla'), Js('Bussia'), Js('Bussugnata'), Js('Cabrilla'), Js('Cabura'), Js('Caburena'), Js('Caccosa'), Js('Cacossa'), Js('Cacudia'), Js('Cambaria'), Js('Cambosa'), Js('Camelognata'), Js('Camolatia'), Js('Camoulatia'), Js('Camula'), Js('Camulata'), Js('Camulatia'), Js('Camuledu'), Js('Camulia'), Js('Camulilia'), Js('Camullia'), Js('Cantexta'), Js('Caraddouna'), Js('Caranta'), Js('Carantana'), Js('Carantia'), Js('Carantiana'), Js('Carantila'), Js('Carantilla'), Js('Carantina'), Js('Carantodia'), Js('Carantusa'), Js('Carata'), Js('Caratila'), Js('Caratilla'), Js('Caratulla'), Js('Careia'), Js('Carenta'), Js('Caretosa'), Js('Caria'), Js('Carina'), Js('Carisia'), Js('Carissa'), Js('Carosa'), Js('Carosia'), Js('Carrotala'), Js('Cartulla'), Js('Caruca'), Js('Caruiliena'), Js('Caruonia'), Js('Cassa'), Js('Cassia'), Js('Cassibodua'), Js('Cassicia'), Js('Cassimara'), Js('Cassiola'), Js('Casticia'), Js('Castina'), Js('Cata'), Js('Catalia'), Js('Catia'), Js('Catica'), Js('Catilia'), Js('Catilla'), Js('Catiola'), Js('Catnea'), Js('Catronia'), Js('Catta'), Js('Cattara'), Js('Cattea'), Js('Cattia'), Js('Cattira'), Js('Cattulla'), Js('Cattuviqqa'), Js('Catuallauna'), Js('Catucia'), Js('Catulla'), Js('Catullia'), Js('Caturica'), Js('Caturigia'), Js('Caturisa'), Js('Cauaria'), Js('Caura'), Js('Cauru'), Js('Cavaria'), Js('Cenia'), Js('Ceniuria'), Js('Cenos'), Js('Censonia'), Js('Centa'), Js('Centogenea'), Js('Centusmia'), Js('Cigemma'), Js('Cincia'), Js('Cincissa'), Js('Cingetissa'), Js('Cinia'), Js('Cintucra'), Js('Cintugena'), Js('Cintusma'), Js('Cintusmina'), Js('Cintussa'), Js('Cintussia'), Js('Cloutina'), Js('Clutamilla'), Js('Cobiatia'), Js('Coblanuo'), Js('Coblucia'), Js('Cobnerta'), Js('Cobromara'), Js('Cobronia'), Js('Cobruna'), Js('Comacia'), Js('Comatia'), Js('Comatimara'), Js('Comatulla'), Js('Combara'), Js('Comerta'), Js('Comiomara'), Js('Condexua'), Js('Congenetia'), Js('Congenncia'), Js('Consuadullia'), Js('Contessia'), Js('Corasia'), Js('Corobilla'), Js('Corrodu'), Js('Cotina'), Js('Cotira'), Js('Cotta'), Js('Cottia'), Js('Cottina'), Js('Cottira'), Js('Cottula'), Js('Cotu'), Js('Cotuconi'), Js('Cotulia'), Js('Counerta'), Js('Cricconia'), Js('Cubria'), Js('Cunacena'), Js('Dagania'), Js('Dania'), Js('Danissa'), Js('Dannia'), Js('Dannumaa'), Js('Danotala'), Js('Danu'), Js('Deiotariana'), Js('Derceia'), Js('Deuila'), Js('Deuillia'), Js('Deuognata'), Js('Devignata'), Js('Diona'), Js('Diorata'), Js('Diougenia'), Js('Diuilla'), Js('Diuuogna'), Js('Diuvogna'), Js('Diveca'), Js('Divogenia'), Js('Donilla'), Js('Donisia'), Js('Dubna'), Js('Dubnia'), Js('Dumnana'), Js('Dumnia'), Js('Eburia'), Js('Eburila'), Js('Eliomara'), Js('Elovissa'), Js('Elvissa'), Js('Emogenia'), Js('Epa'), Js('Epetina'), Js('Epia'), Js('Epilla'), Js('Epillia'), Js('Epiu'), Js('Eppa'), Js('Eppacta'), Js('Eppaxtia'), Js('Eppia'), Js('Epponina'), Js('Etiona'), Js('Etolugnia'), Js('Exapia'), Js('Excinga'), Js('Excingilla'), Js('Exobna'), Js('Exomna'), Js('Exouna'), Js('Fimmilene'), Js('Friagabi'), Js('Gabra'), Js('Genaca'), Js('Genetodia'), Js('Genna'), Js('Genobia'), Js('Genucia'), Js('Gnata'), Js('Gnatia'), Js('Gnatilla'), Js('Iantulla'), Js('Iantumara'), Js('Iatta'), Js('Iattossa'), Js('Ibliomaria'), Js('Iccia'), Js('Ilateuta'), Js('Inatura'), Js('Inderca'), Js('Indercilea'), Js('Isosae'), Js('Itta'), Js('Kareia'), Js('Karina'), Js('Lanpendia'), Js('Larma'), Js('Leuca'), Js('Leucena'), Js('Leucimara'), Js('Leucona'), Js('Leuconia'), Js('Litania'), Js('Litogena'), Js('Littiossa'), Js('Litu'), Js('Litua'), Js('Litucca'), Js('Lituccia'), Js('Litugena'), Js('Litullina'), Js('Loucita'), Js('Loucitta'), Js('Lugiola'), Js('Luppa'), Js('Macaria'), Js('Maccira'), Js('Maccirra'), Js('Magunia'), Js('Magunna'), Js('Magusatia'), Js('Mandelana'), Js('Manduilla'), Js('Manduissa'), Js('Marilla'), Js('Martidia'), Js('Martilia'), Js('Martiria'), Js('Martna'), Js('Mata'), Js('Mataura'), Js('Materiona'), Js('Matia'), Js('Maticia'), Js('Matidia'), Js('Matina'), Js('Matona'), Js('Matonia'), Js('Matta'), Js('Mattia'), Js('Mattosa'), Js('Mattua'), Js('Matua'), Js('Matucenia'), Js('Matucia'), Js('Matugena'), Js('Matugenia'), Js('Matullina'), Js('Matuna'), Js('Medilotamica'), Js('Medlotama'), Js('Meducena'), Js('Melicia'), Js('Meliginna'), Js('Messilia'), Js('Messilla'), Js('Metela'), Js('Metilia'), Js('Moria'), Js('Moriena'), Js('Mottu'), Js('Motuca'), Js('Motuidiaca'), Js('Nama'), Js('Namia'), Js('Namidia'), Js('Namiola'), Js('Namma'), Js('Nammia'), Js('Nammota'), Js('Namu'), Js('Namusa'), Js('Namuta'), Js('Nantia'), Js('Nantiorix'), Js('Nemetocena'), Js('Nemetogena'), Js('Nerta'), Js('Nertilla'), Js('Nertomaria'), Js('Netelia'), Js('Nitiogenna'), Js('Ollia'), Js('Olliadu'), Js('Olluna'), Js('Olugnia'), Js('Orbia'), Js('Orbiana'), Js('Orbissa'), Js('Origena'), Js('Oxidubna'), Js('Pera'), Js('Perra'), Js('Peruia'), Js('Perula'), Js('Rega'), Js('Regallia'), Js('Regina'), Js('Reginia'), Js('Regula'), Js('Rematia'), Js('Resia'), Js('Ressatu'), Js('Ressilla'), Js('Ressona'), Js('Resta'), Js('Restia'), Js('Reticiana'), Js('Rextugeniana'), Js('Riceina'), Js('Ricina'), Js('Ricua'), Js('Riguiru'), Js('Rikua'), Js('Ritomara'), Js('Ritulla'), Js('Ritumara'), Js('Rituscia'), Js('Rotama'), Js('Rotania'), Js('Sagila'), Js('Sagillia'), Js('Sama'), Js('Samacia'), Js('Samaxa'), Js('Samia'), Js('Samianta'), Js('Samicantu'), Js('Samicia'), Js('Saminia'), Js('Samma'), Js('Sammia'), Js('Sammiola'), Js('Sammola'), Js('Sammulla'), Js('Samuda'), Js('Sattomata'), Js('Sedata'), Js('Sedatia'), Js('Sedecennis'), Js('Sedia'), Js('Sedida'), Js('Segla'), Js('Segolia'), Js('Segusiaua'), Js('Senila'), Js('Senilla'), Js('Sennaucia'), Js('Senocenna'), Js('Senodona'), Js('Senodonna'), Js('Sila'), Js('Solimara'), Js('Suadugena'), Js('Suaduilla'), Js('Suadulla'), Js('Suagria'), Js('Suausia'), Js('Sucaria'), Js('Sueta'), Js('Sumaria'), Js('Sumela'), Js('Sumelia'), Js('Sumenu'), Js('Talauia'), Js('Talavica'), Js('Taliounia'), Js('Talisia'), Js('Talissa'), Js('Taluppa'), Js('Talussa'), Js('Tancina'), Js('Tancorix'), Js('Tascilla'), Js('Tasgilia'), Js('Tasgilla'), Js('Tauria'), Js('Taurica'), Js('Taurilla'), Js('Taurina'), Js('Teolugnia'), Js('Teuta'), Js('Teutalu'), Js('Teutana'), Js('Trita'), Js('Tritia'), Js('Trocina'), Js('Troucetissa'), Js('Troucisa'), Js('Troucissa'), Js('Valagenta'), Js('Valeia'), Js('Valicinia'), Js('Vallia'), Js('Vandania'), Js('Vebromara'), Js('Vebronara'), Js('Vebrumma'), Js('Veca'), Js('Vecticia'), Js('Vectinia'), Js('Velacena'), Js('Velacosta'), Js('Veleda'), Js('Velitia'), Js('Vellibia'), Js('Vena'), Js('Venaesia'), Js('Venia'), Js('Veniala'), Js('Venica'), Js('Venicia'), Js('Veniena'), Js('Venimara'), Js('Veninia'), Js('Venisama'), Js('Veniuallia'), Js('Venivallia'), Js('Venixama'), Js('Venixema'), Js('Venixiema'), Js('Venna'), Js('Vennonia'), Js('Venulanta'), Js('Venuleia'), Js('Verbronara'), Js('Verica'), Js('Verodumna'), Js('Vertia'), Js('Verucia'), Js('Vicana'), Js('Viccu'), Js('Viccus'), Js('Victisarana'), Js('Victulliena'), Js('Vindaina'), Js('Vindama'), Js('Vindauscia'), Js('Vindilla'), Js('Vindoinissa'), Js('Vindu'), Js('Viniuallia'), Js('Viralira'), Js('Viratia'), Js('Viriana'), Js('Viriata'), Js('Viricia'), Js('Viriciu'), Js('Viriola'), Js('Viriondaga'), Js('Virodu'), Js('Virotouta'), Js('Visurix'), Js('Vlattia'), Js('Vlattu'), Js('Vlatuna'), Js('Vocara'), Js('Vocontia'), Js('Volatia'), Js('Vritea'), Js('Vrittia'), Js('Vrogenia')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', var.get('nm2').get(var.get('rnd')))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('names', var.get('nm1').get(var.get('rnd')))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
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
celticGaulNames = var.to_python()