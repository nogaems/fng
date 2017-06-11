__all__ = ['faroeseNames']

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
    var.put('nm1', Js([Js('Ábal'), Js('Ábraham'), Js('Ábram'), Js('Ádam'), Js('Áki'), Js('Álvfinnur'), Js('Álvgeir'), Js('Álvheðin'), Js('Álvur'), Js('Ámundur'), Js('Ánanias'), Js('Ánias'), Js('Ápraham'), Js('Ápram'), Js('Árant'), Js('Ári'), Js('Árni'), Js('Áron'), Js('Ásar'), Js('Ásbergur'), Js('Ásbjørn'), Js('Ásbrandur'), Js('Ásfinnur'), Js('Ásgeir'), Js('Ásgrímur'), Js('Ási'), Js('Áskil'), Js('Áslakur'), Js('Ásleivur'), Js('Ásmóður'), Js('Ásmundur'), Js('Ássvein'), Js('Ásvaldur'), Js('Ásvarður'), Js('Ásvar'), Js('Ávaldur'), Js('Ægir'), Js('Ímundur'), Js('Ísakur'), Js('Ísleivur'), Js('Ísmal'), Js('Ívar'), Js('Óðin'), Js('Óla'), Js('Ólavur'), Js('Óli'), Js('Ólivar'), Js('Óttar'), Js('Øgmundur'), Js('Øgvaldur'), Js('Øksur'), Js('Ørnolvur'), Js('Ørvar'), Js('Ørvur'), Js('Øssur'), Js('Úlvar'), Js('Úlvheðin'), Js('Úlvur'), Js('Aðalgeir'), Js('Aðalstein'), Js('Absalon'), Js('Adolf'), Js('Adrian'), Js('Aggusteinus'), Js('Agnar'), Js('Aksal'), Js('Aksel'), Js('Albert'), Js('Albin'), Js('Aleks'), Js('Aleksandur'), Js('Alfred'), Js('Allan'), Js('Alvi'), Js('Amadeus'), Js('Amos'), Js('Andras'), Js('Andri'), Js('Andrias'), Js('Ansgar'), Js('Antines'), Js('Antinis'), Js('Anton'), Js('Ari'), Js('Arinbjørn'), Js('Arnór'), Js('Arnaldur'), Js('Arnar'), Js('Arnbjørn'), Js('Arndór'), Js('Arnfinnur'), Js('Arnfríður'), Js('Arngrímur'), Js('Arni'), Js('Arnleygur'), Js('Arnljótur'), Js('Arnoddur'), Js('Arnold'), Js('Arnstein'), Js('Arnsvein'), Js('Aron'), Js('Artan'), Js('Artur'), Js('Askur'), Js('Atli'), Js('August'), Js('Augustinus'), Js('Bárður'), Js('Báraldur'), Js('Bænadikt'), Js('Bóas'), Js('Bótolvur'), Js('Bødvar'), Js('Búgvi'), Js('Búi'), Js('Baldur'), Js('Baldvin'), Js('Baltasar'), Js('Baraldur'), Js('Bartal'), Js('Bastian'), Js('Beinar'), Js('Beini'), Js('Beinir'), Js('Benadikt'), Js('Benjamin'), Js('Bergar'), Js('Bergfinnur'), Js('Bergfríður'), Js('Bergleivur'), Js('Bergsvein'), Js('Bergtór'), Js('Bergur'), Js('Berint'), Js('Bernar'), Js('Bernhard'), Js('Bersi'), Js('Bessi'), Js('Betuel'), Js('Birgar'), Js('Birgir'), Js('Birni'), Js('Birtir'), Js('Bjørgúlvur'), Js('Bjørgfinnur'), Js('Bjørgheðin'), Js('Bjørgolvur'), Js('Bjørn'), Js('Bjarki'), Js('Bjarngrímur'), Js('Bjarnheðin'), Js('Bjarni'), Js('Bjarnvarður'), Js('Bjarti'), Js('Bjartmar'), Js('Bjartur'), Js('Blásius'), Js('Boas'), Js('Bogi'), Js('Borgar'), Js('Brúsi'), Js('Bragi'), Js('Brandar'), Js('Brandur'), Js('Bresti'), Js('Brestir'), Js('Brialdur'), Js('Brian'), Js('Broddi'), Js('Broddur'), Js('Brosi'), Js('Brynjar'), Js('Brynjolvur'), Js('Brynleivur'), Js('Bursi'), Js('Dánial'), Js('Dánjal'), Js('Dávið'), Js('Dávi'), Js('Dávid'), Js('Dávur'), Js('Díðrikur'), Js('Dagbjørn'), Js('Dagbjartur'), Js('Dagfinnur'), Js('Dagur'), Js('Dan'), Js('Danjal'), Js('Dann'), Js('Demmus'), Js('Dennis'), Js('Dion'), Js('Ditleivur'), Js('Djóni'), Js('Dunaldur'), Js('Ebbi'), Js('Edmundur'), Js('Edvard'), Js('Edvin'), Js('Egi'), Js('Egil'), Js('Egin'), Js('Eilívur'), Js('Einar'), Js('Eindri'), Js('Eiri'), Js('Eirikur'), Js('Eivindur'), Js('Eldbjørn'), Js('Eli'), Js('Elian'), Js('Elias'), Js('Eliesar'), Js('Elis'), Js('Ellindur'), Js('Elmar'), Js('Elvar'), Js('Emil'), Js('Enokur'), Js('Erhard'), Js('Erlendur'), Js('Erlingur'), Js('Ernst'), Js('Esbern'), Js('Esekiel'), Js('Eskil'), Js('Esmar'), Js('Esmundur'), Js('Evald'), Js('Eyðálvur'), Js('Eyðbjørn'), Js('Eyðbjartur'), Js('Eyðfinnur'), Js('Eyðgrímur'), Js('Eyði'), Js('Eyðleivur'), Js('Eyðmar'), Js('Eyðmundur'), Js('Eyðolvur'), Js('Eyðstein'), Js('Eyðsvein'), Js('Eyðtór'), Js('Eyðun'), Js('Eyðvarður'), Js('Fálgeir'), Js('Fabian'), Js('Filip'), Js('Filippus'), Js('Finnbjørn'), Js('Finnbogi'), Js('Finnfríði'), Js('Finngeir'), Js('Finnleivur'), Js('Finnur'), Js('Flæmingur'), Js('Flóki'), Js('Flóvin'), Js('Flemmingur'), Js('Flosi'), Js('Fríðálvur'), Js('Fríðbjørn'), Js('Fríðbjartur'), Js('Fríðfinnur'), Js('Fríði'), Js('Fríðmundur'), Js('Fríðolvur'), Js('Fríðrikur'), Js('Fríður'), Js('Frímann'), Js('Fróðar'), Js('Fróði'), Js('Frank'), Js('Frans'), Js('Fridleivur'), Js('Frits'), Js('Gíslar'), Js('Gísli'), Js('Gabrial'), Js('Gabriel'), Js('Gaprial'), Js('Garðar'), Js('Geir'), Js('Geirbjørn'), Js('Geirbrandur'), Js('Geirfinnur'), Js('Geiri'), Js('Geirmundur'), Js('Geirolvur'), Js('Geirur'), Js('Georg'), Js('Gestur'), Js('Geyti'), Js('Gilbert'), Js('Gilli'), Js('Gilstein'), Js('Gissur'), Js('Glúmur'), Js('Gormundur'), Js('Gormur'), Js('Grækaris'), Js('Grímolvur'), Js('Grímur'), Js('Greipur'), Js('Grettir'), Js('Grias'), Js('Gripur'), Js('Guðbjartur'), Js('Guðbrandur'), Js('Guðlakur'), Js('Gudfinnur'), Js('Gudjón'), Js('Gudleygur'), Js('Gudmar'), Js('Gudmundur'), Js('Gulakur'), Js('Gullbrandur'), Js('Gundur'), Js('Gunnálvur'), Js('Gunnar'), Js('Gunnbjørn'), Js('Gunni'), Js('Gunnleikur'), Js('Gunnleivur'), Js('Gunnleygur'), Js('Gunnolvur'), Js('Gunnstein'), Js('Gunnvaldur'), Js('Gustav'), Js('Gusti'), Js('Gutti'), Js('Guttormur'), Js('Gylvi'), Js('Hábarður'), Js('Hákun'), Js('Hálvdan'), Js('Hámundur'), Js('Hárikur'), Js('Hástein'), Js('Hávarður'), Js('Hávar'), Js('Hórður'), Js('Hóraldur'), Js('Hóri'), Js('Høgnar'), Js('Høgni'), Js('Hørður'), Js('Høskuldur'), Js('Húnbogi'), Js('Húni'), Js('Hagbarður'), Js('Halgir'), Js('Hallbergur'), Js('Hallbjørn'), Js('Halldór'), Js('Hallfríður'), Js('Hallgeir'), Js('Hallgrímur'), Js('Hallmar'), Js('Hallmundur'), Js('Hallormur'), Js('Hallstein'), Js('Hallur'), Js('Hallvarður'), Js('Hannes'), Js('Hannis'), Js('Hannus'), Js('Hans'), Js('Hanus'), Js('Haraldur'), Js('Havgrímur'), Js('Havliði'), Js('Havstein'), Js('Heðin'), Js('Heiðrikur'), Js('Heimir'), Js('Heindrikur'), Js('Heini'), Js('Heinrikur'), Js('Helgi'), Js('Hemingur'), Js('Hemmingur'), Js('Hendrikur'), Js('Henningur'), Js('Hensar'), Js('Herálvur'), Js('Herbert'), Js('Herbjørn'), Js('Herbjartur'), Js('Herbrandur'), Js('Herfinnur'), Js('Herfríður'), Js('Hergeir'), Js('Hergrímur'), Js('Heri'), Js('Herjolvur'), Js('Herleivur'), Js('Herleygur'), Js('Hermóður'), Js('Hermann'), Js('Hermundur'), Js('Herningur'), Js('Herolvur'), Js('Herstein'), Js('Hervarður'), Js('Hilbert'), Js('Hildar'), Js('Hildibjørn'), Js('Hildibjartur'), Js('Hildibrandur'), Js('Hilmar'), Js('Hjálmar'), Js('Hjørgrímur'), Js('Hjørleivur'), Js('Hjørmundur'), Js('Hjørtur'), Js('Hjalgrímur'), Js('Hjalmar'), Js('Hjalti'), Js('Hjarnar'), Js('Hjartvar'), Js('Holgar'), Js('Hugi'), Js('Hugin'), Js('Immanuel'), Js('Ingálvur'), Js('Ingi'), Js('Ingibjørn'), Js('Ingibjartur'), Js('Ingileivur'), Js('Ingimar'), Js('Ingimundur'), Js('Ingivaldur'), Js('Ingjaldur'), Js('Ingmar'), Js('Ingolvur'), Js('Ingvaldur'), Js('Ingvar'), Js('Ivan'), Js('Jákup'), Js('Játmundur'), Js('Jóal'), Js('Jóan'), Js('Jóanes'), Js('Jóanis'), Js('Jóannes'), Js('Jóannis'), Js('Jóas'), Js('Jóel'), Js('Jófríður'), Js('Jógvan'), Js('Jóhan'), Js('Jóhann'), Js('Jóhannes'), Js('Jóhannis'), Js('Jóhannus'), Js('Jón'), Js('Jónar'), Js('Jónas'), Js('Jónatan'), Js('Jónfinnur'), Js('Jónhard'), Js('Jónheðin'), Js('Jóni'), Js('Jónleivur'), Js('Jónstein'), Js('Jónsvein'), Js('Jósef'), Js('Jóstein'), Js('Jósup'), Js('Jósvein'), Js('Jøkil'), Js('Jøkul'), Js('Jørgun'), Js('Jørmundur'), Js('Jørundur'), Js('Júlian'), Js('Július'), Js('Júst'), Js('Jústi'), Js('Jústines'), Js('Jústinis'), Js('Jústinus'), Js('Jafet'), Js('Jallgrímur'), Js('Jan'), Js('Jann'), Js('Janus'), Js('Jarleivur'), Js('Jarmundur'), Js('Jason'), Js('Jaspur'), Js('Jatmundur'), Js('Jatvarður'), Js('Jenis'), Js('Jens'), Js('Jesar'), Js('Johan'), Js('John'), Js('Jonn'), Js('Josva'), Js('Julian'), Js('Julius'), Js('Justi'), Js('Kálvur'), Js('Kári'), Js('Kai'), Js('Kaleb'), Js('Karl'), Js('Karstin'), Js('Kartni'), Js('Kaspar'), Js('Ketil'), Js('Kjartan'), Js('Kláus'), Js('Klæmint'), Js('Knútur'), Js('Kolbein'), Js('Kolbjørn'), Js('Kolfinnur'), Js('Kolgrímur'), Js('Kolmundur'), Js('Konrad'), Js('Koraldur'), Js('Kornelius'), Js('Kornus'), Js('Kristafár'), Js('Kristian'), Js('Kristin'), Js('Kristjan'), Js('Kristleivur'), Js('Kristmar'), Js('Kristmundur'), Js('Kristoffur'), Js('Kristtór'), Js('Kristvar'), Js('Kurt'), Js('Kyrri'), Js('Lávus'), Js('Líggjas'), Js('Løðar'), Js('Lýðar'), Js('Lýður'), Js('Laars'), Js('Lars'), Js('Larvas'), Js('Lassi'), Js('Laurus'), Js('Lavars'), Js('Lavrans'), Js('Leiki'), Js('Leivur'), Js('Leo'), Js('Leon'), Js('Levi'), Js('Loðin'), Js('Loftur'), Js('Ludvík'), Js('Lukas'), Js('Lykkir'), Js('Máur'), Js('Mækir'), Js('Mórits'), Js('Mórus'), Js('Móses'), Js('Magnar'), Js('Magni'), Js('Magnus'), Js('Maks'), Js('Malvinus'), Js('Mannbjørn'), Js('Manni'), Js('Margeir'), Js('Marius'), Js('Marjus'), Js('Markus'), Js('Marnar'), Js('Marni'), Js('Martin'), Js('Mass'), Js('Mats'), Js('Mattas'), Js('Matteus'), Js('Mattias'), Js('Meinar'), Js('Meinhard'), Js('Melkir'), Js('Melkjor'), Js('Mikal'), Js('Mikkjal'), Js('Milan'), Js('Mortan'), Js('Nátan'), Js('Nói'), Js('Naddoddur'), Js('Napoleon'), Js('Narvi'), Js('Natanael'), Js('Nemus'), Js('Niels'), Js('Niklái'), Js('Niklas'), Js('Nikodemus'), Js('Nikolas'), Js('Nils'), Js('Njál'), Js('Njálur'), Js('Norðleivur'), Js('Oddbjørn'), Js('Oddfinnur'), Js('Oddfríður'), Js('Oddgeir'), Js('Oddleivur'), Js('Oddmar'), Js('Oddmundur'), Js('Oddur'), Js('Oddvaldur'), Js('Oddvar'), Js('Olgar'), Js('Olivur'), Js('Onundur'), Js('Ormar'), Js('Ormstein'), Js('Ormur'), Js('Orri'), Js('Oskar'), Js('Ottar'), Js('Otto'), Js('Ovi'), Js('Oygrímur'), Js('Oyleivur'), Js('Oymundur'), Js('Oyolvur'), Js('Oystein'), Js('Oyvindur'), Js('Pál'), Js('Páll'), Js('Pátrikur'), Js('Pætur'), Js('Pól'), Js('Palli'), Js('Pauli'), Js('Per'), Js('Petur'), Js('Poli'), Js('Poul'), Js('Ríkaldur'), Js('Ríkin'), Js('Róðbjartur'), Js('Róðolvur'), Js('Róaldur'), Js('Róar'), Js('Rógvi'), Js('Rói'), Js('Rókur'), Js('Róland'), Js('Rólant'), Js('Rólvur'), Js('Rómundur'), Js('Rósingur'), Js('Røgnvaldur'), Js('Rúnar'), Js('Rúni'), Js('Rúnolvur'), Js('Ragnar'), Js('Ragnvaldur'), Js('Randver'), Js('Rani'), Js('Rasmus'), Js('Ravnur'), Js('Regin'), Js('Reiðar'), Js('Reimar'), Js('Reinaldur'), Js('Reinar'), Js('Rikard'), Js('Robert'), Js('Rodleivur'), Js('Rodmar'), Js('Rodmundur'), Js('Ronni'), Js('Rubekur'), Js('Ruben'), Js('Sálamon'), Js('Sálomon'), Js('Sámal'), Js('Sámuel'), Js('Sámur'), Js('Sæbjørn'), Js('Sæfinnur'), Js('Sæmundur'), Js('Sævar'), Js('Símeon'), Js('Símun'), Js('Sívar'), Js('Sólbjørn'), Js('Sólbjartur'), Js('Sólfinnur'), Js('Sólmundur'), Js('Sølmundur'), Js('Sølvar'), Js('Sølvi'), Js('Sørin'), Js('Sørkvi'), Js('Sørli'), Js('Súni'), Js('Súnmundur'), Js('Sakarias'), Js('Sakaris'), Js('Sakir'), Js('Saksi'), Js('Salmundur'), Js('Samson'), Js('Sandur'), Js('Sebastian'), Js('Selmar'), Js('Servin'), Js('Set'), Js('Sevrin'), Js('Sigbjørn'), Js('Sigbjartur'), Js('Sigbrandur'), Js('Sigfús'), Js('Sigfríður'), Js('Sighvatur'), Js('Sigmar'), Js('Sigmundur'), Js('Signar'), Js('Signhard'), Js('Signheðin'), Js('Sigtór'), Js('Sigurð'), Js('Sigurd'), Js('Sigvaldur'), Js('Sigvar'), Js('Silas'), Js('Sirius'), Js('Sjúrði'), Js('Sjúrður'), Js('Skúvur'), Js('Skeggi'), Js('Skofti'), Js('Snæúlvur'), Js('Snæbjørn'), Js('Snævar'), Js('Sniolvur'), Js('Snorri'), Js('Sofus'), Js('Sonnhard'), Js('Sonni'), Js('Sproti'), Js('Stígur'), Js('Stefan'), Js('Steffan'), Js('Steinar'), Js('Steinbjørn'), Js('Steinfinnur'), Js('Steingrímur'), Js('Steinmundur'), Js('Steinoddur'), Js('Steinolvur'), Js('Steintór'), Js('Steinur'), Js('Summaldur'), Js('Summarliði'), Js('Suni'), Js('Sunnleivur'), Js('Sunnvar'), Js('Svávar'), Js('Sveinbjørn'), Js('Sveinungur'), Js('Sveinur'), Js('Svenningur'), Js('Sverri'), Js('Syftun'), Js('Tíðrikur'), Js('Tístram'), Js('Tóki'), Js('Tórálvur'), Js('Tórður'), Js('Tóraldur'), Js('Tórarin'), Js('Tórhallur'), Js('Tórheðin'), Js('Tóri'), Js('Tórir'), Js('Tóroddur'), Js('Tórolvur'), Js('Tórur'), Js('Tóti'), Js('Týrur'), Js('Teinar'), Js('Teitur'), Js('Teodor'), Js('Terji'), Js('Tjálvi'), Js('Tjóðolvur'), Js('Tobias'), Js('Tollakur'), Js('Tonni'), Js('Torbergur'), Js('Torbjørn'), Js('Torbrandur'), Js('Torfinnur'), Js('Torfríður'), Js('Torgeir'), Js('Torgestur'), Js('Torgrímur'), Js('Torkil'), Js('Torleivur'), Js('Torleygur'), Js('Tormóður'), Js('Tormann'), Js('Tormar'), Js('Tormundur'), Js('Torri'), Js('Torstein'), Js('Torvaldur'), Js('Tráin'), Js('Tróndur'), Js('Trøstur'), Js('Treysti'), Js('Tristan'), Js('Trygvi'), Js('Tummas'), Js('Tyrni'), Js('Tyrnir'), Js('Uggi'), Js('Uni'), Js('Unnar'), Js('Urbanus'), Js('Vígúlvur'), Js('Vígbaldur'), Js('Vígbrandur'), Js('Víggrímur'), Js('Vívil'), Js('Vónbjartur'), Js('Vøggur'), Js('Vølundur'), Js('Vagnar'), Js('Vagnur'), Js('Valbergur'), Js('Valbjørn'), Js('Valbrandur'), Js('Valdi'), Js('Valdimar'), Js('Vensil'), Js('Vermundur'), Js('Vernar'), Js('Vestar'), Js('Veturliði'), Js('Vigfús'), Js('Viggo'), Js('Viktor'), Js('Vilbergur'), Js('Vilhelm'), Js('Vilhjálmur'), Js('Viljam'), Js('Viljormur'), Js('Villi'), Js('Villiam'), Js('Vilmar'), Js('Vilmundur'), Js('Vinjar'), Js('Vinsi'), Js('Virgar'), Js('Vitus'), Js('Volmar'), Js('Yngvar'), Js('Yngvi')]))
    var.put('nm2', Js([Js('Ábria'), Js('Álvdis'), Js('Álvgerð'), Js('Álvheiður'), Js('Álvhild'), Js('Ánania'), Js('Árna'), Js('Ása'), Js('Ásbera'), Js('Ásbjørg'), Js('Ásdis'), Js('Ásfríð'), Js('Ásgerð'), Js('Áshild'), Js('Ásla'), Js('Ásleyg'), Js('Ásta'), Js('Ásthild'), Js('Ástrið'), Js('Ásvør'), Js('Æsa'), Js('Íðunn'), Js('Óluva'), Js('Úlvhild'), Js('Ýr'), Js('Aðalbjørg'), Js('Aðalborg'), Js('Aðalgunn'), Js('Aðalheiður'), Js('Aðallín'), Js('Abellóna'), Js('Agda'), Js('Agnas'), Js('Alberta'), Js('Albjørg'), Js('Alborg'), Js('Alda'), Js('Aldis'), Js('Aleksandra'), Js('Alfríð'), Js('Alisa'), Js('Alma'), Js('Alrún'), Js('Amalia'), Js('Amalja'), Js('Amanda'), Js('Andrea'), Js('Angela'), Js('Angelika'), Js('Anita'), Js('Anja'), Js('Anný'), Js('Anna'), Js('Annika'), Js('Antonia'), Js('Apollonia'), Js('Aranja'), Js('Arina'), Js('Armgarð'), Js('Arnóra'), Js('Arna'), Js('Arnbjørg'), Js('Arnborg'), Js('Arndis'), Js('Arnfríð'), Js('Arngerð'), Js('Arngunn'), Js('Arnheiður'), Js('Arnhild'), Js('Arnina'), Js('Arnleyg'), Js('Arnljót'), Js('Arnvør'), Js('Asta'), Js('Astrið'), Js('Ata'), Js('Augusta'), Js('Aura'), Js('Bára'), Js('Bænadikta'), Js('Bóthild'), Js('Børka'), Js('Barba'), Js('Barbara'), Js('Beata'), Js('Bedda'), Js('Beinta'), Js('Belinda'), Js('Benadikta'), Js('Benita'), Js('Bera'), Js('Bergdis'), Js('Bergfríð'), Js('Berghild'), Js('Bergitta'), Js('Bergljót'), Js('Bergný'), Js('Bergtóra'), Js('Bergunn'), Js('Berit'), Js('Berta'), Js('Bettý'), Js('Betta'), Js('Billa'), Js('Bina'), Js('Birgit'), Js('Birgitta'), Js('Birita'), Js('Birna'), Js('Birta'), Js('Bjølla'), Js('Bjørg'), Js('Bjørgfríð'), Js('Bjørghild'), Js('Bjørk'), Js('Bjørt'), Js('Bjalla'), Js('Bjarma'), Js('Bjarndis'), Js('Bjarnfríð'), Js('Bjarnhild'), Js('Bjarta'), Js('Borgfríð'), Js('Borghild'), Js('Borgný'), Js('Brá'), Js('Brita'), Js('Britt'), Js('Bryndis'), Js('Bryngerð'), Js('Brynhild'), Js('Brynja'), Js('Bylgja'), Js('Dís'), Js('Dóra'), Js('Døgg'), Js('Dagbjørg'), Js('Dagbjørt'), Js('Dagfríð'), Js('Dagmar'), Js('Dagný'), Js('Dagrún'), Js('Dagunn'), Js('Dania'), Js('Daniella'), Js('Danvør'), Js('Debora'), Js('Diana'), Js('Dina'), Js('Dinna'), Js('Dora'), Js('Doris'), Js('Dorotea'), Js('Dortea'), Js('Drós'), Js('Dropleyg'), Js('Durið'), Js('Durita'), Js('Duruta'), Js('Ebba'), Js('Edda'), Js('Edit'), Js('Edna'), Js('Eik'), Js('Eilin'), Js('Eina'), Js('Eir'), Js('Eirika'), Js('Eldbjørg'), Js('Eldrið'), Js('Eleonora'), Js('Elia'), Js('Elin'), Js('Elinbjørg'), Js('Elinborg'), Js('Elisa'), Js('Elisabet'), Js('Ella'), Js('Elma'), Js('Elna'), Js('Elsý'), Js('Elsa'), Js('Elsba'), Js('Elsbet'), Js('Elspa'), Js('Elsuba'), Js('Elsubet'), Js('Elvina'), Js('Elvira'), Js('Embla'), Js('Emilý'), Js('Emilia'), Js('Emma'), Js('Enna'), Js('Erika'), Js('Erla'), Js('Erna'), Js('Esta'), Js('Ester'), Js('Estrið'), Js('Estur'), Js('Eva'), Js('Eyð'), Js('Eyðbjørg'), Js('Eyðbjørt'), Js('Eyðdis'), Js('Eyðfríð'), Js('Eyðgerð'), Js('Eyðgunn'), Js('Eyðhild'), Js('Eyðleyg'), Js('Eyðrið'), Js('Eyðrun'), Js('Eyður'), Js('Eyðvør'), Js('Eydna'), Js('Fía'), Js('Fípa'), Js('Følva'), Js('Fanný'), Js('Felisia'), Js('Femja'), Js('Filippa'), Js('Finnbjørg'), Js('Finngerð'), Js('Finnleyg'), Js('Fjóla'), Js('Flykra'), Js('Fríða'), Js('Fríðbjørg'), Js('Fríðborg'), Js('Fríðgerð'), Js('Fríðhild'), Js('Fríðrún'), Js('Fríðrika'), Js('Fríðrun'), Js('Fríðunn'), Js('Fríðvør'), Js('Fróða'), Js('Friðgerð'), Js('Frida'), Js('Froya'), Js('Froydis'), Js('Froygerð'), Js('Gísleyg'), Js('Gabriella'), Js('Geira'), Js('Geirhild'), Js('Geirtrúð'), Js('Gerð'), Js('Gerda'), Js('Geythild'), Js('Giljanna'), Js('Gisleyg'), Js('Glæma'), Js('Glóa'), Js('Gloria'), Js('Gortra'), Js('Gróa'), Js('Greta'), Js('Grimhild'), Js('Guðbjørg'), Js('Guðrið'), Js('Guðrun'), Js('Gudbjørg'), Js('Gudfinna'), Js('Gudleyg'), Js('Gudný'), Js('Gudrun'), Js('Gudvør'), Js('Gullbjørg'), Js('Gullborg'), Js('Gunn'), Js('Gunna'), Js('Gunnbjørg'), Js('Gunnbrit'), Js('Gunnfríð'), Js('Gunngerð'), Js('Gunnhild'), Js('Gunnleyg'), Js('Gunnrið'), Js('Gunnvá'), Js('Gunnvør'), Js('Gurli'), Js('Gyða'), Js('Gylta'), Js('Húngerð'), Js('Húngunn'), Js('Halda'), Js('Halla'), Js('Hallbera'), Js('Hallbjørg'), Js('Halldóra'), Js('Halldis'), Js('Hallfríð'), Js('Hallgerð'), Js('Hallgunn'), Js('Hallvør'), Js('Hallveig'), Js('Hanna'), Js('Hansa'), Js('Hansina'), Js('Havdis'), Js('Havgerð'), Js('Heiða'), Js('Heiðdis'), Js('Heiðrún'), Js('Heiðrun'), Js('Heiðvík'), Js('Heiðvør'), Js('Heiðveig'), Js('Heidi'), Js('Heinina'), Js('Helena'), Js('Helga'), Js('Helma'), Js('Henný'), Js('Henrietta'), Js('Henrikka'), Js('Hera'), Js('Herbjørg'), Js('Herborg'), Js('Herdis'), Js('Herfríð'), Js('Hergerð'), Js('Hergunn'), Js('Herrið'), Js('Herta'), Js('Hervør'), Js('Hilda'), Js('Hildibjørg'), Js('Hildibjørt'), Js('Hildigarð'), Js('Hildigerð'), Js('Hildigunn'), Js('Hildur'), Js('Hilma'), Js('Hjørdis'), Js('Hjalma'), Js('Hjartvør'), Js('Hulda'), Js('Iðunn'), Js('Ida'), Js('Ina'), Js('Inga'), Js('Ingibjørg'), Js('Ingibjørt'), Js('Ingigerð'), Js('Ingilín'), Js('Ingileyg'), Js('Ingirið'), Js('Ingrún'), Js('Ingrið'), Js('Ingun'), Js('Ingunn'), Js('Ingvá'), Js('Ingvør'), Js('Inna'), Js('Irena'), Js('Iris'), Js('Irma'), Js('Isabella'), Js('Jóanna'), Js('Jódis'), Js('Jófríð'), Js('Jóhanna'), Js('Jóhild'), Js('Jóna'), Js('Jónbjørg'), Js('Jónfríð'), Js('Jóngerð'), Js('Jónhild'), Js('Jónleyg'), Js('Jónrið'), Js('Jónvá'), Js('Jónvár'), Js('Jónvør'), Js('Jónveig'), Js('Jórunn'), Js('Jóvør'), Js('Júlia'), Js('Jústa'), Js('Jútta'), Js('Jakoba'), Js('Jakobina'), Js('Jana'), Js('Janhild'), Js('Janita'), Js('Janna'), Js('Jansý'), Js('Jastrið'), Js('Jemima'), Js('Jenný'), Js('Jennhild'), Js('Jensa'), Js('Jensia'), Js('Jensina'), Js('Jetta'), Js('Jona'), Js('Jonna'), Js('Jonnhild'), Js('Josefina'), Js('Jovina'), Js('Judit'), Js('Julia'), Js('Julianna'), Js('Justa'), Js('Jutta'), Js('Kára'), Js('Kárunn'), Js('Kaia'), Js('Kamilla'), Js('Kamma'), Js('Karin'), Js('Karina'), Js('Karita'), Js('Karla'), Js('Karlina'), Js('Karolina'), Js('Kassandra'), Js('Katarina'), Js('Katja'), Js('Katla'), Js('Katrin'), Js('Katrina'), Js('Kirstin'), Js('Klára'), Js('Klara'), Js('Kolbrún'), Js('Kolfinna'), Js('Kornelia'), Js('Krista'), Js('Kristbjørg'), Js('Kristensa'), Js('Kristfríð'), Js('Kristhild'), Js('Kristianna'), Js('Kristin'), Js('Kristina'), Js('Kristinbjørg'), Js('Kristjanna'), Js('Kristrún'), Js('Kristrun'), Js('Kristvør'), Js('Lín'), Js('Lísbita'), Js('Lív'), Js('Lóa'), Js('Lý'), Js('Lýdia'), Js('Laila'), Js('Laura'), Js('Laurina'), Js('Lea'), Js('Lena'), Js('Leyvoy'), Js('Lilja'), Js('Lillý'), Js('Lina'), Js('Lind'), Js('Linda'), Js('Lisa'), Js('Lisabet'), Js('Lisbet'), Js('Liss'), Js('Liva'), Js('Lona'), Js('Lotta'), Js('Lovisa'), Js('Lula'), Js('Lusia'), Js('Málfríð'), Js('Magda'), Js('Magdalena'), Js('Magga'), Js('Magna'), Js('Magnhild'), Js('Maia'), Js('Maibrit'), Js('Maifríð'), Js('Maika'), Js('Maisól'), Js('Malan'), Js('Malena'), Js('Malfríð'), Js('Malja'), Js('Malla'), Js('Malvina'), Js('Marý'), Js('Margit'), Js('Margret'), Js('Margreta'), Js('Margunn'), Js('Marið'), Js('Maria'), Js('Marianna'), Js('Marin'), Js('Marit'), Js('Marita'), Js('Marja'), Js('Marjun'), Js('Marlena'), Js('Marna'), Js('Marnhild'), Js('Marta'), Js('Martina'), Js('Masa'), Js('Matilda'), Js('Matthild'), Js('Maud'), Js('Melania'), Js('Merrý'), Js('Metta'), Js('Mia'), Js('Mikala'), Js('Mildrið'), Js('Milja'), Js('Mina'), Js('Minna'), Js('Mira'), Js('Miriam'), Js('Mirja'), Js('Mirjam'), Js('Mona'), Js('Monika'), Js('Morið'), Js('Myrna'), Js('Nóra'), Js('Naina'), Js('Nanný'), Js('Nanna'), Js('Nansý'), Js('Naomi'), Js('Natalia'), Js('Natasja'), Js('Nikolina'), Js('Nina'), Js('Ninna'), Js('Nita'), Js('Nomi'), Js('Noomi'), Js('Norðbjørt'), Js('Nora'), Js('Norma'), Js('Oda'), Js('Oddbjørg'), Js('Oddfríð'), Js('Oddgerð'), Js('Oddleyg'), Js('Oddný'), Js('Oddrún'), Js('Oddvá'), Js('Oddvør'), Js('Oddveig'), Js('Olga'), Js('Olivia'), Js('Olivina'), Js('Oluffa'), Js('Oydis'), Js('Oygerð'), Js('Oygló'), Js('Oyleyg'), Js('Oyvør'), Js('Pálma'), Js('Píl'), Js('Póla'), Js('Pólina'), Js('Palma'), Js('Paula'), Js('Paulina'), Js('Pavla'), Js('Petra'), Js('Petrina'), Js('Poula'), Js('Poulina'), Js('Róða'), Js('Ró'), Js('Róa'), Js('Róhild'), Js('Rósa'), Js('Røskva'), Js('Rún'), Js('Rúna'), Js('Ragna'), Js('Ragnfríð'), Js('Ragnheiður'), Js('Ragnhild'), Js('Ragnvør'), Js('Rakul'), Js('Randarsól'), Js('Randfríð'), Js('Randið'), Js('Randi'), Js('Ranja'), Js('Rannfríð'), Js('Rannvá'), Js('Rannvør'), Js('Rannveig'), Js('Ravnhild'), Js('Rebekka'), Js('Reiðgunn'), Js('Reiðunn'), Js('Renata'), Js('Revna'), Js('Ria'), Js('Rikka'), Js('Rita'), Js('Ritva'), Js('Roda'), Js('Ronja'), Js('Royða'), Js('Rut'), Js('Rutt'), Js('Sára'), Js('Sæbjørg'), Js('Sædis'), Js('Sæfríð'), Js('Sæunn'), Js('Sól'), Js('Sólbirta'), Js('Sólbjørg'), Js('Sólbjørt'), Js('Sólborg'), Js('Sólbrá'), Js('Sólbrún'), Js('Sólbrit'), Js('Sóldís'), Js('Sóleyð'), Js('Sólfríð'), Js('Sólgerð'), Js('Sólja'), Js('Sólrið'), Js('Sólrun'), Js('Sólvá'), Js('Sólvør'), Js('Sólveig'), Js('Sølvá'), Js('Sølvør'), Js('Sølva'), Js('Súna'), Js('Súnbjørt'), Js('Súnfríð'), Js('Súnfríða'), Js('Súnhild'), Js('Súsanna'), Js('Salbjørg'), Js('Saldis'), Js('Salgerð'), Js('Salný'), Js('Saloma'), Js('Salvør'), Js('Sandra'), Js('Sanna'), Js('Saranja'), Js('Sarita'), Js('Selena'), Js('Selinda'), Js('Selma'), Js('Senita'), Js('Sesilia'), Js('Sigbjørg'), Js('Sigborg'), Js('Sigbrit'), Js('Sigfríð'), Js('Sigga'), Js('Signý'), Js('Signa'), Js('Signhild'), Js('Signild'), Js('Signuva'), Js('Sigrið'), Js('Sigrun'), Js('Sigurbjørg'), Js('Sigurgunn'), Js('Sigurleyg'), Js('Sigursól'), Js('Sigvør'), Js('Silja'), Js('Silrið'), Js('Silvia'), Js('Silvurlín'), Js('Simona'), Js('Sirið'), Js('Sissal'), Js('Siv'), Js('Smæra'), Js('Snæbjørg'), Js('Snæfríð'), Js('Snæleyg'), Js('Snjófríð'), Js('Sofía'), Js('Solveig'), Js('Sonja'), Js('Stefania'), Js('Steinbjarta'), Js('Steingerð'), Js('Steintóra'), Js('Steinunn'), Js('Steinvør'), Js('Stella'), Js('Stina'), Js('Suffía'), Js('Sunnbjørg'), Js('Sunnfríð'), Js('Sunnfríða'), Js('Sunnhild'), Js('Sunniva'), Js('Sunnleyg'), Js('Sunnrið'), Js('Sunnvá'), Js('Sunnvør'), Js('Sváva'), Js('Svanbjørg'), Js('Svanfríð'), Js('Svanhild'), Js('Svanleyg'), Js('Svanna'), Js('Sylvia'), Js('Tóna'), Js('Tóra'), Js('Tórhalla'), Js('Tórhild'), Js('Tórunn'), Js('Tóta'), Js('Tóva'), Js('Týra'), Js('Tabita'), Js('Talita'), Js('Tamara'), Js('Tanja'), Js('Tea'), Js('Teitrun'), Js('Tekla'), Js('Teresa'), Js('Tina'), Js('Tinna'), Js('Tita'), Js('Tjóðhild'), Js('Tomasia'), Js('Torbera'), Js('Torbjørg'), Js('Torbjørt'), Js('Torborg'), Js('Tordis'), Js('Torfinna'), Js('Torfríð'), Js('Torgerð'), Js('Torgunn'), Js('Torgunna'), Js('Torleyg'), Js('Torný'), Js('Torvør'), Js('Tova'), Js('Trina'), Js('Turið'), Js('Ulla'), Js('Una'), Js('Unn'), Js('Unna'), Js('Unnur'), Js('Urð'), Js('Urða'), Js('Vár'), Js('Várdis'), Js('Váreyð'), Js('Væna'), Js('Vígdis'), Js('Vón'), Js('Vónbjørt'), Js('Vagna'), Js('Valbjørg'), Js('Valborg'), Js('Valdis'), Js('Valgerð'), Js('Vera'), Js('Vióla'), Js('Vigdis'), Js('Viktoria'), Js('Vilbjørg'), Js('Vilbjørt'), Js('Vilborg'), Js('Vilgerð'), Js('Vinný'), Js('Vivia'), Js('Yngva'), Js('Yngvild'), Js('Yrsa'), Js('Yvonna')]))
    var.put('nm3', Js([Js('Ásgeirsdóttir'), Js('Ólavsson'), Js('Aagard'), Js('Anderssen'), Js('Andreasen'), Js('Andreassen'), Js('Arge'), Js('Arrheboe'), Js('Bærentsen'), Js('Bóndi'), Js('Børresen'), Js('Barthel'), Js('Bech'), Js('Blak'), Js('Bleken'), Js('Bogason'), Js('Boman'), Js('Brú'), Js('Brattaberg'), Js('Brestisson'), Js('Broberg'), Js('Bronck'), Js('Dahl'), Js('Dam'), Js('Danielsen'), Js('Danjalsson'), Js('Debes'), Js('Djurhuus'), Js('Effersøe'), Js('Eidesgaard'), Js('Evensen'), Js('Finsen'), Js('Ganting'), Js('Glerfoss'), Js('Gulbranson'), Js('Háberg'), Js('Hátun'), Js('Høgnesen'), Js('Højgaard'), Js('Hammershaimb'), Js('Hansdóttir'), Js('Hansen'), Js('Hanusardóttir'), Js('Haraldsen'), Js('Haugaard'), Js('Heinason'), Js('Heinesen'), Js('Helmsdal'), Js('Hentze'), Js('Holdremyr'), Js('Hoydal'), Js('Isaksen'), Js('Jákupsson'), Js('Jógvansson'), Js('Jóhansen'), Js('Jónsson'), Js('Jacobsen'), Js('Jakobsen'), Js('Jensen'), Js('Joensen'), Js('Johannesen'), Js('Johannessen'), Js('Johansen'), Js('Justinussen'), Js('Kallsberg'), Js('Kamban'), Js('Kampmann'), Js('Kielberg'), Js('Kjelnæs'), Js('Knudsen'), Js('Krogh'), Js('Kruse'), Js('Lützen'), Js('Lamhauge'), Js('Landt'), Js('Lassen'), Js('Lisberg'), Js('Long'), Js('Lyngbye'), Js('Magnussen'), Js('Matras'), Js('Mikines'), Js('Mikkelsen'), Js('Mohr'), Js('Mortensen'), Js('Nólsoy'), Js('Nansen'), Js('Niclasen'), Js('Nielsen'), Js('Nolsøe'), Js('Nysted'), Js('Olsen'), Js('Oskarsson'), Js('Ottarsdóttir'), Js('Páll'), Js('Pálsdóttir'), Js('Patursson'), Js('Petersen'), Js('Pløyen'), Js('Poulsen'), Js('Rólantsson'), Js('Rønne'), Js('Rønning'), Js('Rasmussen'), Js('Reginsson'), Js('Reinert'), Js('Reistrup'), Js('Restorff'), Js('Reyni'), Js('Rosenmeyer'), Js('Ryberg'), Js('Sørensen'), Js('Schrøter'), Js('Sigmundsdóttir'), Js('Sigurðsson'), Js('Simonsen'), Js('Skarði'), Js('Smith'), Js('Stórá'), Js('Svabo'), Js('Tórgarð'), Js('Taalle'), Js('Tausen'), Js('Thomsen'), Js('Torfasen'), Js('Vágadal'), Js('Vatnhamar'), Js('Viderø'), Js('Wich'), Js('Ziska')]))
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
faroeseNames = var.to_python()