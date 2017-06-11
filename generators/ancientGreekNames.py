__all__ = ['ancientGreekNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abantes'), Js('Abas'), Js('Abascantus'), Js('Abderos'), Js('Aberkios'), Js('Ablerus'), Js('Abreas'), Js('Abronychus'), Js('Abydos'), Js('Acaeus'), Js('Acamus'), Js('Acessamenus'), Js('Acestes'), Js('Aclepiades'), Js('Acrisias'), Js('Acrisius'), Js('Acroneos'), Js('Actor'), Js('Adeimanthos'), Js('Adelphius'), Js('Admetos'), Js('Adrastos'), Js('Adrastus'), Js('Adrestus'), Js('Aeaces'), Js('Aegaeon'), Js('Aegicoros'), Js('Aegisthes'), Js('Aegon'), Js('Aeimnestos'), Js('Aenesidemos'), Js('Aeolus'), Js('Aeropus'), Js('Aeschreas'), Js('Aesculapius'), Js('Aesepus'), Js('Aeson'), Js('Aesop'), Js('Aetes'), Js('Aethon'), Js('Aetion'), Js('Aetios'), Js('Aetolos'), Js('Agamedes'), Js('Agamemnon'), Js('Agapenor'), Js('Agapias'), Js('Agastrophos'), Js('Agathocles'), Js('Agathon'), Js('Agelaus'), Js('Agenor'), Js('Agesilaus'), Js('Agetos'), Js('Agis'), Js('Agrias'), Js('Aiantes'), Js('Aias'), Js('Aigeus'), Js('Airopos'), Js('Aischylos'), Js('Akadios'), Js('Akamas'), Js('Aktis'), Js('Aktor'), Js('Alastor'), Js('Alcaeos'), Js('Alcandros'), Js('Alcides'), Js('Alcimos'), Js('Alcinous'), Js('Alcmaion'), Js('Alcman'), Js('Alcon'), Js('Alector'), Js('Alektryon'), Js('Aleuas'), Js('Alexandros'), Js('Alexarchos'), Js('Alexias'), Js('Alexis'), Js('Alexon'), Js('Alkamenos'), Js('Alkestis'), Js('Alketas'), Js('Alkibiades'), Js('Alkides'), Js('Alkimachos'), Js('Alkiphron'), Js('Alkmaion'), Js('Aloeus'), Js('Alphaeus'), Js('Alpheos'), Js('Alphesiboeus'), Js('Alphios'), Js('Altes'), Js('Alypius'), Js('Amarinceus'), Js('Ameinias'), Js('Ameinokles'), Js('Amiantos'), Js('Amompharetos'), Js('Amopaon'), Js('Amphiaraos'), Js('Amphidamos'), Js('Amphimachos'), Js('Amphimnestus'), Js('Amphinomous'), Js('Amphion'), Js('Amphios'), Js('Amphitrion'), Js('Amyntas'), Js('Amyntor'), Js('Amyris'), Js('Amythaon'), Js('Anabesineos'), Js('Anacharsis'), Js('Anakletos'), Js('Anakreon'), Js('Anastasios'), Js('Anaxagoras'), Js('Anaxandridas'), Js('Anaxandrides'), Js('Anaxandros'), Js('Anaxarchos'), Js('Anaxilaus'), Js('Anaximander'), Js('Anaximenes'), Js('Anaxis'), Js('Anaxos'), Js('Anchialus'), Js('Anchimolios'), Js('Anchises'), Js('Ancus'), Js('Andokides'), Js('Andraemon'), Js('Andreas'), Js('Androbulos'), Js('Androcles'), Js('Androdamos'), Js('Androgeus'), Js('Aneristos'), Js('Aniketos'), Js('Anisodoros'), Js('Antaeus'), Js('Antagoras'), Js('Antemion'), Js('Antenor'), Js('Anthemion'), Js('Antichares'), Js('Antidoros'), Js('Antigenes'), Js('Antigonos'), Js('Antikles'), Js('Antilochus'), Js('Antinous'), Js('Antiochus'), Js('Antipatris'), Js('Antipatros'), Js('Antiphales'), Js('Antiphones'), Js('Antiphus'), Js('Antisthenes'), Js('Anytos'), Js('Anytus'), Js('Apelles'), Js('Apellicon'), Js('Aphidnos'), Js('Apisaon'), Js('Apollodoros'), Js('Apollophanes'), Js('Apollos'), Js('Aratus'), Js('Arcas'), Js('Arcesilaus'), Js('Archagoras'), Js('Archelaos'), Js('Archeptolemus'), Js('Archesilaus'), Js('Archestratidas'), Js('Archilochus'), Js('Archytas'), Js('Arcidamus'), Js('Arcturus'), Js('Areilycus'), Js('Areisius'), Js('Areithous'), Js('Argades'), Js('Argaeus'), Js('Argos'), Js('Aridolis'), Js('Arion'), Js('Ariphron'), Js('Aristaeus'), Js('Aristagoras'), Js('Aristaios'), Js('Aristandros'), Js('Aristarchos'), Js('Aristarchus'), Js('Aristides'), Js('Aristion'), Js('Aristippus'), Js('Aristoboulos'), Js('Aristobulus'), Js('Aristocles'), Js('Aristocypros'), Js('Aristodemos'), Js('Aristogeiton'), Js('Aristomachos'), Js('Ariston'), Js('Aristonous'), Js('Aristonymos'), Js('Aristophanes'), Js('Aristophantes'), Js('Aristos'), Js('Aristotles'), Js('Aristoxenus'), Js('Arrabaios'), Js('Arridaios'), Js('Arsenios'), Js('Artemas'), Js('Artemidoros'), Js('Artemios'), Js('Artemisthenes'), Js('Arybbas'), Js('Asasthenes'), Js('Ascalaphus'), Js('Ascanius'), Js('Aschines'), Js('Asius'), Js('Asklepios'), Js('Asonides'), Js('Asopodoros'), Js('Asopus'), Js('Asphalion'), Js('Assaraeus'), Js('Astacos'), Js('Aster'), Js('Asterion'), Js('Asteropaeus'), Js('Astrabacus'), Js('Astyanax'), Js('Athamas'), Js('Athenades'), Js('Athenaeus'), Js('Athenion'), Js('Athenodorus'), Js('Atiphates'), Js('Atreus'), Js('Atrometos'), Js('Attaginas'), Js('Attaginos'), Js('Attalos'), Js('Atymnius'), Js('Atys'), Js('Audax'), Js('Augias'), Js('Auletes'), Js('Autesion'), Js('Autodikos'), Js('Autolycus'), Js('Autolykos'), Js('Automedon'), Js('Autonous'), Js('Axylus'), Js('Azeus'), Js('Bacchides'), Js('Bacchios'), Js('Bacchylides'), Js('Bacenor'), Js('Bacis'), Js('Baerius'), Js('Balius'), Js('Barates'), Js('Bardas'), Js('Basileides'), Js('Basileios'), Js('Basilides'), Js('Bathyaes'), Js('Belos'), Js('Bendis'), Js('Bianor'), Js('Bias'), Js('Bion'), Js('Bisaltes'), Js('Biton'), Js('Blathyllos'), Js('Boethus'), Js('Borus'), Js('Boter'), Js('Briareus'), Js('Briarus'), Js('Brison'), Js('Brygos'), Js('Bucoli'), Js('Bulis'), Js('Burrhus'), Js('Butacidas'), Js('Cöon'), Js('Callimachus'), Js('Callimorphus'), Js('Carenos'), Js('Carneades'), Js('Carpophorus'), Js('Carpus'), Js('Casambus'), Js('Castor'), Js('Ceas'), Js('Cebriones'), Js('Celeas'), Js('Cephalos'), Js('Cepheus'), Js('Cephissos'), Js('Ceyx'), Js('Chabrias'), Js('Chaeremon'), Js('Chairophon'), Js('Chalcodon'), Js('Chalcon'), Js('Charax'), Js('Chares'), Js('Charidemos'), Js('Charilaus'), Js('Charillos'), Js('Charmides'), Js('Charon'), Js('Charopos'), Js('Cheiron'), Js('Chersis'), Js('Chileos'), Js('Chilon'), Js('Choerilos'), Js('Choeros'), Js('Chremes'), Js('Chremon'), Js('Chremonides'), Js('Chromis'), Js('Chromius'), Js('Chrysaor'), Js('Chryses'), Js('Chrysippos'), Js('Chrysogones'), Js('Chrysogonus'), Js('Chrysolorus'), Js('Cilix'), Js('Cineas'), Js('Cinyras'), Js('Cisses'), Js('Cisseus'), Js('Cleades'), Js('Cleandros'), Js('Cleathes'), Js('Cleisthenes'), Js('Cleobulus'), Js('Cleodaeos'), Js('Cleombrotos'), Js('Cleomenes'), Js('Cleon'), Js('Cleonicus'), Js('Cleonymus'), Js('Clinias'), Js('Clisthenes'), Js('Clonius'), Js('Clytius'), Js('Clytomedes'), Js('Cnoethos'), Js('Cobon'), Js('Codros'), Js('Coenus'), Js('Coeranus'), Js('Coes'), Js('Cois'), Js('Conon'), Js('Copreus'), Js('Cordylion'), Js('Coronos'), Js('Corydallos'), Js('Corydon'), Js('Crathis'), Js('Cratinus'), Js('Cratippus'), Js('Cretheus'), Js('Crethon'), Js('Cretines'), Js('Crios'), Js('Croesus'), Js('Cronos'), Js('Cteatus'), Js('Ctesippus'), Js('Cuphagoras'), Js('Cyberniskos'), Js('Cycnus'), Js('Cylon'), Js('Cynaegiros'), Js('Cyncus'), Js('Cyneas'), Js('Cyniscus'), Js('Cypselos'), Js('Cyrenios'), Js('Cytorissos'), Js('Dadaces'), Js('Daedalos'), Js('Daetor'), Js('Damasippus'), Js('Damasithymos'), Js('Damasos'), Js('Damastor'), Js('Damian'), Js('Damianos'), Js('Damiskos'), Js('Damoetas'), Js('Damon'), Js('Danaos'), Js('Danaus'), Js('Daphis'), Js('Daphnis'), Js('Dardanus'), Js('Dares'), Js('Davos'), Js('Deinias'), Js('Deinokrates'), Js('Deinomenes'), Js('Deiotones'), Js('Deiphobus'), Js('Deiphonous'), Js('Deipylus'), Js('Demades'), Js('Demaratos'), Js('Demarmenos'), Js('Demas'), Js('Demeas'), Js('Demetrios'), Js('Democedes'), Js('Democoön'), Js('Demodocus'), Js('Demokrates'), Js('Demoleon'), Js('Demonax'), Js('Demonous'), Js('Demophlos'), Js('Demosthenes'), Js('Deon'), Js('Derkylos'), Js('Deukalion'), Js('Dexicos'), Js('Dexios'), Js('Diactorides'), Js('Diadromes'), Js('Diadumenus'), Js('Diagoras'), Js('Dicaeus'), Js('Dieneces'), Js('Diocles'), Js('Diodoros'), Js('Diodorus'), Js('Diokles'), Js('Diomedes'), Js('Dionysios'), Js('Dionysophanes'), Js('Dionysos'), Js('Diophantus'), Js('Diores'), Js('Dioscuros'), Js('Diotrephes'), Js('Dismas'), Js('Dithyrambos'), Js('Dmetor'), Js('Dolon'), Js('Dolops'), Js('Doreios'), Js('Doreius'), Js('Dorian'), Js('Doriskos'), Js('Doros'), Js('Dorotheus'), Js('Doryssos'), Js('Dosithios'), Js('Drimylos'), Js('Dromeus'), Js('Dryas'), Js('Dryops'), Js('Ducetius'), Js('Duris'), Js('Dymas'), Js('Dymnos'), Js('Echëeus'), Js('Echekrates'), Js('Echelaos'), Js('Echemmon'), Js('Echemus'), Js('Echephron'), Js('Echepolus'), Js('Echestratos'), Js('Eetion'), Js('Eioneus'), Js('Eirenaios'), Js('Elasus'), Js('Elatos'), Js('Elatreus'), Js('Eleon'), Js('Elephenor'), Js('Elpenor'), Js('Elpides'), Js('Elpidius'), Js('Empedocles'), Js('Endios'), Js('Endymion'), Js('Engenes'), Js('Eniopus'), Js('Ennaeus'), Js('Ennomus'), Js('Ennychus'), Js('Enops'), Js('Eos'), Js('Epaenetus'), Js('Epaphos'), Js('Epaphroditus'), Js('Epeigeus'), Js('Epeius'), Js('Ephialtes'), Js('Epicurus'), Js('Epicydes'), Js('Epikrates'), Js('Epimenes'), Js('Epiphanes'), Js('Epistor'), Js('Epistrophos'), Js('Epitrophos'), Js('Epizelos'), Js('Erasistratus'), Js('Eratosthenes'), Js('Eratostheres'), Js('Erechtheus'), Js('Eretmenus'), Js('Ereuthalion'), Js('Erginus'), Js('Ergiyios'), Js('Erichthonius'), Js('Erxandros'), Js('Eryalus'), Js('Erysichton'), Js('Eryx'), Js('Eryximachos'), Js('Eteocles'), Js('Eteokles'), Js('Eteonous'), Js('Euaemon'), Js('Eualcidas'), Js('Euanthes'), Js('Euarestos'), Js('Eubalus'), Js('Eubulus'), Js('Eucarpus'), Js('Euchenor'), Js('Eucleides'), Js('Eudorus'), Js('Eudoxsus'), Js('Eudoxus'), Js('Euenius'), Js('Euenor'), Js('Euenus'), Js('Eugammon'), Js('Eugenios'), Js('Eugenius'), Js('Euhemenis'), Js('Euippus'), Js('Eukles'), Js('Eumaeus'), Js('Eumastas'), Js('Eumelus'), Js('Eumenes'), Js('Eumneus'), Js('Eumolpus'), Js('Euneas'), Js('Euonomos'), Js('Eupalinus'), Js('Euphenes'), Js('Euphorbos'), Js('Euphorion'), Js('Euphronios'), Js('Eupolos'), Js('Euripides'), Js('Euryanax'), Js('Eurybates'), Js('Eurybiades'), Js('Eurycliedes'), Js('Eurydamus'), Js('Eurydemon'), Js('Eurydemos'), Js('Euryhus'), Js('Eurykrates'), Js('Eurykratides'), Js('Euryleon'), Js('Eurylochos'), Js('Eurymachos'), Js('Euryphon'), Js('Eurypylos'), Js('Eurystenes'), Js('Eurysthenes'), Js('Eurystheus'), Js('Eurysthios'), Js('Eurythion'), Js('Eurytos'), Js('Eussorus'), Js('Euthydemos'), Js('Euthynos'), Js('Eutropios'), Js('Eutuches'), Js('Eutychides'), Js('Eutychus'), Js('Evaenetos'), Js('Evagoras'), Js('Evandros'), Js('Evanetus'), Js('Evelthon'), Js('Evenios'), Js('Evenus'), Js('Evios'), Js('Exaduis'), Js('Exekias'), Js('Faenus'), Js('Galenus'), Js('Gallus'), Js('Ganymedes'), Js('Gauanes'), Js('Geleon'), Js('Gelo'), Js('Gelon'), Js('Gennadios'), Js('Gerasimos'), Js('Giorgius'), Js('Glaukias'), Js('Glaukos'), Js('Glycon'), Js('Gnipho'), Js('Gordias'), Js('Gorgias'), Js('Gorgion'), Js('Gorgos'), Js('Gorgythion'), Js('Gregorius'), Js('Gryllus'), Js('Gurgos'), Js('Gylippos'), Js('Gyras'), Js('Gyrtias'), Js('Haemon'), Js('Hagias'), Js('Hagnon'), Js('Halisthertes'), Js('Halius'), Js('Harmatidas'), Js('Harmocydes'), Js('Harmodios'), Js('Harmon'), Js('Harpagos'), Js('Harpalion'), Js('Harpalos'), Js('Harpocras'), Js('Hecataeus'), Js('Hegesandros'), Js('Hegesistratos'), Js('Hegetoridas'), Js('Heirax'), Js('Heiron'), Js('Hektor'), Js('Helenos'), Js('Helgesippos'), Js('Helicaon'), Js('Heliodorus'), Js('Helios'), Js('Helle'), Js('Hephaestos'), Js('Herakleides'), Js('Herakleitos'), Js('Heraklides'), Js('Hermeias'), Js('Hermeros'), Js('Hermippos'), Js('Hermogenes'), Js('Hermolaos'), Js('Hermolycus'), Js('Hermon'), Js('Hermotimos'), Js('Hero'), Js('Herodes'), Js('Herodianus'), Js('Herodion'), Js('Heromenes'), Js('Hicetaon'), Js('Hiero'), Js('Hieronymus'), Js('Hipparchos'), Js('Hipparinos'), Js('Hippasus'), Js('Hippias'), Js('Hippocoön'), Js('Hippoklides'), Js('Hippokratides'), Js('Hippolytos'), Js('Hippomachos'), Js('Hippomenes'), Js('Hippon'), Js('Hipponax'), Js('Hipponicus'), Js('Hipponous'), Js('Hippotas'), Js('Hippothous'), Js('Hippotion'), Js('Hoiples'), Js('Homeros'), Js('Hyakinthos'), Js('Hylas'), Js('Hyllos'), Js('Hyllus'), Js('Hypatius'), Js('Hypeirochus'), Js('Hypenor'), Js('Hyperenor'), Js('Hyperion'), Js('Hypsenor'), Js('Hyrcanus'), Js('Hyrtacus'), Js('Hyrtius'), Js('Iakchos'), Js('Ialmenes'), Js('Iambulus'), Js('Iamus'), Js('Iasos'), Js('Iatragoras'), Js('Iatrokles'), Js('Ibanolis'), Js('Ibykos'), Js('Icarion'), Js('Icarius'), Js('Icarus'), Js('Idaeus'), Js('Idaios'), Js('Idas'), Js('Idomeneus'), Js('Ilioneus'), Js('Illyrius'), Js('Ilus'), Js('Imbrasus'), Js('Imbrius'), Js('Imbrus'), Js('Inachos'), Js('Inachus'), Js('Inaros'), Js('Iobates'), Js('Iolaos'), Js('Iollas'), Js('Ion'), Js('Iphiclus'), Js('Iphicrates'), Js('Iphikrates'), Js('Iphinous'), Js('Iphitos'), Js('Iphitus'), Js('Iros'), Js('Irus'), Js('Isagoras'), Js('Isandros'), Js('Ischenous'), Js('Isidor'), Js('Isidoros'), Js('Ision'), Js('Ismaros'), Js('Ismenios'), Js('Isocrates'), Js('Isodemos'), Js('Isokrates'), Js('Itheus'), Js('Itylus'), Js('Itys'), Js('Kadmos'), Js('Kaenas'), Js('Kaeneus'), Js('Kalchas'), Js('Kalesius'), Js('Kaletor'), Js('Kalliaros'), Js('Kallias'), Js('Kallikles'), Js('Kallikrates'), Js('Kallimachos'), Js('Kallinicus'), Js('Kallinos'), Js('Kallipides'), Js('Kallipos'), Js('Kallisthenes'), Js('Kallon'), Js('Kameirus'), Js('Kandaules'), Js('Kannadis'), Js('Kapaneus'), Js('Kapys'), Js('Karipos'), Js('Karopophores'), Js('Kasos'), Js('Kassandros'), Js('Kaunos'), Js('Kebalinos'), Js('Kebes'), Js('Kekrops'), Js('Keos'), Js('Kephalon'), Js('Kephalos'), Js('Kerameikos'), Js('Kerkyon'), Js('Keteus'), Js('Kimon'), Js('Kirphis'), Js('Kittos'), Js('Kleitos'), Js('Kleobis'), Js('Kleomenes'), Js('Koines'), Js('Koinos'), Js('Konon'), Js('Koragos'), Js('Korax'), Js('Kosmas'), Js('Krantor'), Js('Krateros'), Js('Kreon'), Js('Krinippos'), Js('Kristos'), Js('Kritias'), Js('Kritoboulos'), Js('Kritodemos'), Js('Kriton'), Js('Kroisos'), Js('Krokinos'), Js('Ktesiphon'), Js('Kyknos'), Js('Kynaegeiros'), Js('Kyrillos'), Js('Kyrios'), Js('Kyros'), Js('Labdacus'), Js('Labotas'), Js('Laertes'), Js('Lagos'), Js('Laios'), Js('Lamachos'), Js('Lampo'), Js('Lampon'), Js('Lampus'), Js('Lamus'), Js('Laodamas'), Js('Laodocus'), Js('Laogonus'), Js('Laomedon'), Js('Laphanes'), Js('Lasos'), Js('Lasthenes'), Js('Laureion'), Js('Leagros'), Js('Leandros'), Js('Learchos'), Js('Leicritus'), Js('Leitus'), Js('Lemnus'), Js('Leo'), Js('Leocedes'), Js('Leodes'), Js('Leon'), Js('Leonidas'), Js('Leonnatos'), Js('Leontiades'), Js('Leontis'), Js('Leoprepes'), Js('Leotychides'), Js('Lethos'), Js('Leucippus'), Js('Leukos'), Js('Lichas'), Js('Licymnios'), Js('Linus'), Js('Loxias'), Js('Lukos'), Js('Lycaon'), Js('Lycaretos'), Js('Lycidas'), Js('Lycomedes'), Js('Lycophon'), Js('Lycophron'), Js('Lycoris'), Js('Lycurgos'), Js('Lycus'), Js('Lydus'), Js('Lygdamis'), Js('Lykomedes'), Js('Lykon'), Js('Lynceus'), Js('Lysagoras'), Js('Lysandros'), Js('Lysanios'), Js('Lysias'), Js('Lysikles'), Js('Lysimachos'), Js('Lysippos'), Js('Lysippus'), Js('Lysis'), Js('Macar'), Js('Macarias'), Js('Machaon'), Js('Maeon'), Js('Maiandrios'), Js('Makarios'), Js('Maleos'), Js('Males'), Js('Mantes'), Js('Mantios'), Js('Marcion'), Js('Marnes'), Js('Maro'), Js('Maron'), Js('Marsyas'), Js('Mastor'), Js('Matullus'), Js('Mausolos'), Js('Mecistes'), Js('Mecistios'), Js('Medios'), Js('Medon'), Js('Medus'), Js('Megadates'), Js('Megakles'), Js('Megakreon'), Js('Megapenthes'), Js('Megareus'), Js('Megasthenes'), Js('Megathenes'), Js('Meges'), Js('Megistias'), Js('Meidias'), Js('Melampos'), Js('Melampus'), Js('Melanippos'), Js('Melanthios'), Js('Melanthos'), Js('Melas'), Js('Meleagros'), Js('Melegros'), Js('Meles'), Js('Meliboeus'), Js('Melicertes'), Js('Memnon'), Js('Menalcas'), Js('Menandros'), Js('Menares'), Js('Menekrates'), Js('Menelaos'), Js('Menestas'), Js('Menesthes'), Js('Menesthios'), Js('Menexinos'), Js('Menoeces'), Js('Menoitios'), Js('Mentes'), Js('Mentor'), Js('Meriones'), Js('Mermerus'), Js('Merops'), Js('Mesaulius'), Js('Mesthles'), Js('Methodios'), Js('Metiochus'), Js('Meton'), Js('Metrobius'), Js('Metron'), Js('Metrophanes'), Js('Meurius'), Js('Micythos'), Js('Midas'), Js('Midylos'), Js('Mikkos'), Js('Mikon'), Js('Milanion'), Js('Miltiades'), Js('Minos'), Js('Misenus'), Js('Mnasyllus'), Js('Mnesiphilos'), Js('Mnester'), Js('Mnesus'), Js('Moeris'), Js('Moliones'), Js('Molpagoras'), Js('Monoecus'), Js('Monomachus'), Js('Mopsius'), Js('Mopsus'), Js('Morsimus'), Js('Morys'), Js('Moschion'), Js('Mulius'), Js('Musaeus'), Js('Musaios'), Js('Mydon'), Js('Mygdon'), Js('Myrsinus'), Js('Myrto'), Js('Mys'), Js('Narkissos'), Js('Nastes'), Js('Naubolus'), Js('Naukles'), Js('Nausithous'), Js('Nauteus'), Js('Nearchos'), Js('Neleos'), Js('Nelpus'), Js('Neokles'), Js('Neoptolemos'), Js('Neritos'), Js('Nestor'), Js('Niarchos'), Js('Nicandros'), Js('Nicanor'), Js('Nicholas'), Js('Nicholaus'), Js('Nicias'), Js('Nicodromos'), Js('Nicolaus'), Js('Nicomachos'), Js('Nicon'), Js('Nikandros'), Js('Nikanor'), Js('Nikasios'), Js('Nikeratos'), Js('Nikias'), Js('Nikomachos'), Js('Nikomedes'), Js('Nilus'), Js('Nireus'), Js('Nisos'), Js('Noemon'), Js('Nomion'), Js('Nothon'), Js('Numa'), Js('Nyctinus'), Js('Nymphicus'), Js('Nymphodorus'), Js('Ocealus'), Js('Ochesius'), Js('Ochos'), Js('Ocytos'), Js('Odaenathus'), Js('Odius'), Js('Odysseus'), Js('Oeagnus'), Js('Oecleus'), Js('Oedipus'), Js('Oenemaus'), Js('Oeneus'), Js('Oenomaus'), Js('Oenopion'), Js('Oenops'), Js('Oicles'), Js('Oileas'), Js('Oliatos'), Js('Olus'), Js('Olympicus'), Js('Olympiodorus'), Js('Onamakritos'), Js('Onesilos'), Js('Onesimos'), Js('Onesiphorus'), Js('Onetas'), Js('Onetor'), Js('Onias'), Js('Onomastos'), Js('Ophelestes'), Js('Opites'), Js('Ops'), Js('Orcus'), Js('Orestes'), Js('Oresus'), Js('Orges'), Js('Oribasius'), Js('Orion'), Js('Orius'), Js('Oroites'), Js('Orpheus'), Js('Orsilochus'), Js('Orsiphantes'), Js('Orthaeus'), Js('Orythroneus'), Js('Otreus'), Js('Otrynteus'), Js('Otus'), Js('Paeëon'), Js('Paios'), Js('Palaechthon'), Js('Palaemon'), Js('Pallans'), Js('Pallas'), Js('Palmys'), Js('Pammon'), Js('Panaetios'), Js('Panaetius'), Js('Panares'), Js('Pandaros'), Js('Pandion'), Js('Panionos'), Js('Panites'), Js('Pankratios'), Js('Pantares'), Js('Panthous'), Js('Pantites'), Js('Paopeus'), Js('Paraebates'), Js('Paris'), Js('Parmenides'), Js('Parmenion'), Js('Parthenopaeus'), Js('Pasion'), Js('Pataicos'), Js('Patrobas'), Js('Patrobus'), Js('Patroclus'), Js('Patron'), Js('Pausanius'), Js('Pedaeus'), Js('Pedasus'), Js('Pedocles'), Js('Peirithous'), Js('Peiros'), Js('Peisandros'), Js('Peithon'), Js('Pelagon'), Js('Pelegon'), Js('Peleus'), Js('Pelias'), Js('Pelicles'), Js('Pelonus'), Js('Pelopidas'), Js('Peneleos'), Js('Peneus'), Js('Pentheus'), Js('Penthylos'), Js('Peolpidas'), Js('Perdikkas'), Js('Perdix'), Js('Periandros'), Js('Periclymenus'), Js('Perieeres'), Js('Perikles'), Js('Perimedes'), Js('Perimos'), Js('Periphas'), Js('Periphetes'), Js('Periscus'), Js('Peritas'), Js('Periumus'), Js('Peteos'), Js('Peukestes'), Js('Phaedo'), Js('Phaenippos'), Js('Phaeops'), Js('Phaestus'), Js('Phaidon'), Js('Phaidriades'), Js('Phalanthus'), Js('Phalces'), Js('Phalinos'), Js('Phanagoras'), Js('Phancis'), Js('Phanes'), Js('Phanias'), Js('Phantias'), Js('Pharnaces'), Js('Phausius'), Js('Phegeus'), Js('Pheidias'), Js('Pheidippides'), Js('Pheidon'), Js('Phemius'), Js('Phereclus'), Js('Pherecydes'), Js('Pheres'), Js('Pheronactus'), Js('Phidias'), Js('Phigaleios'), Js('Philagros'), Js('Philaon'), Js('Phileas'), Js('Philemon'), Js('Philetor'), Js('Philiskos'), Js('Philistos'), Js('Phillipos'), Js('Philocion'), Js('Philocrates'), Js('Philoctetes'), Js('Philocypros'), Js('Philoetius'), Js('Philogus'), Js('Philokles'), Js('Philokrates'), Js('Philolaos'), Js('Philologus'), Js('Philomen'), Js('Philomenes'), Js('Philometer'), Js('Philon'), Js('Philonikos'), Js('Philopoemon'), Js('Philostratos'), Js('Philostratus'), Js('Philotas'), Js('Philotectes'), Js('Philoxenos'), Js('Philpoemon'), Js('Phineus'), Js('Phintias'), Js('Phlaris'), Js('Phlegon'), Js('Phlios'), Js('Phoenix'), Js('Phoibus'), Js('Phoinix'), Js('Phoitios'), Js('Phokas'), Js('Phokion'), Js('Phorbas'), Js('Phorcys'), Js('Phormion'), Js('Phormos'), Js('Photius'), Js('Phrixus'), Js('Phrynichos'), Js('Phrynikos'), Js('Phrynon'), Js('Phylacus'), Js('Phylas'), Js('Pidytes'), Js('Pigres'), Js('Pinder'), Js('Pirithoos'), Js('Pisistratos'), Js('Pistias'), Js('Pittacos'), Js('Pittacus'), Js('Pittheus'), Js('Pixodarus'), Js('Plades'), Js('Pleistarchos'), Js('Pleistos'), Js('Plutarch'), Js('Podaeleirus'), Js('Podaleirus'), Js('Podalinus'), Js('Podarces'), Js('Podargos'), Js('Podaroes'), Js('Podes'), Js('Poeas'), Js('Poecas'), Js('Poimen'), Js('Polemion'), Js('Poliadas'), Js('Pollio'), Js('Polyas'), Js('Polybius'), Js('Polyctor'), Js('Polydectes'), Js('Polydeuces'), Js('Polydius'), Js('Polydoros'), Js('Polyeides'), Js('Polygonus'), Js('Polykleitos'), Js('Polykles'), Js('Polykritos'), Js('Polymedes'), Js('Polyneices'), Js('Polypemon'), Js('Polyperchon'), Js('Polyphemous'), Js('Polyphetes'), Js('Polyphontes'), Js('Polypoetes'), Js('Polyxeinus'), Js('Ponteus'), Js('Porphyrios'), Js('Porphyrius'), Js('Poseidon'), Js('Posides'), Js('Posidonios'), Js('Potamon'), Js('Pratinos'), Js('Praxilaus'), Js('Praxis'), Js('Praxiteles'), Js('Praxites'), Js('Prexinos'), Js('Priam'), Js('Prinetadas'), Js('Priskos'), Js('Procrustes'), Js('Proctus'), Js('Proetus'), Js('Prokles'), Js('Prokopios'), Js('Prokrustes'), Js('Proreus'), Js('Protagoras'), Js('Protesilaus'), Js('Prothoenor'), Js('Prothous'), Js('Protogenes'), Js('Protus'), Js('Proxenos'), Js('Prymneus'), Js('Prytanis'), Js('Ptolemaios'), Js('Ptolomaeus'), Js('Pylades'), Js('Pylaemenes'), Js('Pylaeus'), Js('Pylartes'), Js('Pylas'), Js('Pylenor'), Js('Pyris'), Js('Pyrrhus'), Js('Pythagoras'), Js('Pytheas'), Js('Pythes'), Js('Pythios'), Js('Pythogenes'), Js('Radamanthos'), Js('Rhadamanthos'), Js('Rhesus'), Js('Rhexenor'), Js('Ribes'), Js('Rizon'), Js('Sabas'), Js('Sabyllos'), Js('Salmoneus'), Js('Sarpedon'), Js('Satyros'), Js('Scaios'), Js('Scamandius'), Js('Scamandrius'), Js('Schedius'), Js('Scylax'), Js('Scyllias'), Js('Scythas'), Js('Sebastos'), Js('Seisames'), Js('Selagus'), Js('Seldomus'), Js('Selepos'), Js('Seleukos'), Js('Sicinnos'), Js('Siculus'), Js('Silanos'), Js('Silenos'), Js('Simmias'), Js('Simo'), Js('Simoisius'), Js('Simonides'), Js('Sinis'), Js('Sinon'), Js('Sippas'), Js('Siromos'), Js('Sisyphus'), Js('Skiron'), Js('Smindyrides'), Js('Smintheus'), Js('Socus'), Js('Sophanes'), Js('Sophokles'), Js('Soranus'), Js('Sosibios'), Js('Sosicles'), Js('Sosigines'), Js('Sosilus'), Js('Sosimenes'), Js('Sosipatros'), Js('Sosthenes'), Js('Sostias'), Js('Sostratos'), Js('Spertias'), Js('Speudon'), Js('Speusippos'), Js('Spinther'), Js('Spirodion'), Js('Stachys'), Js('Stentor'), Js('Stesagoras'), Js('Stesanor'), Js('Stesilaus'), Js('Sthenelaus'), Js('Sthenelus'), Js('Stichius'), Js('Stolos'), Js('Strabo'), Js('Strachys'), Js('Stratios'), Js('Straton'), Js('Strophantes'), Js('Strophius'), Js('Strymon'), Js('Syagros'), Js('Syennesis'), Js('Syloson'), Js('Synesius'), Js('Talaemenes'), Js('Talaos'), Js('Talaus'), Js('Talos'), Js('Talthybios'), Js('Tarchon'), Js('Taureas'), Js('Tebaeus'), Js('Tecton'), Js('Teiresias'), Js('Telamon'), Js('Telekles'), Js('Telemacho'), Js('Telemachos'), Js('Telemachus'), Js('Telephos'), Js('Telephus'), Js('Telesinus'), Js('Telesphorus'), Js('Telines'), Js('Tellias'), Js('Tellis'), Js('Telys'), Js('Temenos'), Js('Tenes'), Js('Tenthredon'), Js('Tereus'), Js('Terillos'), Js('Teucer'), Js('Teukros'), Js('Teutamos'), Js('Teuthranes'), Js('Teuthras'), Js('Thales'), Js('Thalpius'), Js('Thalysios'), Js('Tharybis'), Js('Thaulos'), Js('Thaumastus'), Js('Theagenes'), Js('Theages'), Js('Theas'), Js('Theasides'), Js('Themistius'), Js('Theoclymnius'), Js('Theocydes'), Js('Theodekles'), Js('Theodoros'), Js('Theodotus'), Js('Theognis'), Js('Theomestor'), Js('Theomestros'), Js('Theophanes'), Js('Theophrastos'), Js('Theophrastus'), Js('Theophylaktos'), Js('Theopompos'), Js('Theopompus'), Js('Theopropides'), Js('Theoros'), Js('Theos'), Js('Theramenes'), Js('Therapon'), Js('Theras'), Js('Thero'), Js('Theron'), Js('Thersandros'), Js('Therseandros'), Js('Thersilochus'), Js('Thersites'), Js('Thessalos'), Js('Thestor'), Js('Thettalos'), Js('Thoön'), Js('Thoas'), Js('Thon'), Js('Thorax'), Js('Thrasidaios'), Js('Thrasilaus'), Js('Thrasius'), Js('Thrasybulos'), Js('Thrasyllus'), Js('Thrasymedes'), Js('Threspotus'), Js('Thukydides'), Js('Thyestes'), Js('Thymoetes'), Js('Thymotes'), Js('Thyrsis'), Js('Thyrsos'), Js('Timagenidas'), Js('Timagoras'), Js('Timais'), Js('Timanthes'), Js('Timasion'), Js('Timasitheus'), Js('Timesithius'), Js('Timnes'), Js('Timoleon'), Js('Timon'), Js('Timonax'), Js('Timotheus'), Js('Timoxenos'), Js('Tiro'), Js('Tirynthius'), Js('Tisamenos'), Js('Tisandros'), Js('Tisias'), Js('Tithonius'), Js('Titormos'), Js('Tityrus'), Js('Tlepolemus'), Js('Tmolus'), Js('Trechus'), Js('Triopas'), Js('Triptolemus'), Js('Triton'), Js('Troezenus'), Js('Trophimus'), Js('Trophnus'), Js('Tros'), Js('Trypho'), Js('Turrianus'), Js('Tychaeus'), Js('Tydeides'), Js('Tydeus'), Js('Tymnes'), Js('Tyndareus'), Js('Tyndarios'), Js('Ucalegon'), Js('Vettias'), Js('Xanthippos'), Js('Xanthippus'), Js('Xanthos'), Js('Xenagoras'), Js('Xenokrates'), Js('Xenophanes'), Js('Xenophon'), Js('Xiphilinus'), Js('Xuthos'), Js('Xuthus'), Js('Zagreus'), Js('Zamolxis'), Js('Zenicetes'), Js('Zenodoros'), Js('Zephyrinus'), Js('Zethus'), Js('Zeuxidamos'), Js('Zeuxis'), Js('Zosimus')]))
var.put('nm2', Js([Js('Achaia'), Js('Achradina'), Js('Actaëe'), Js('Actë'), Js('Ada'), Js('Adeia'), Js('Aedon'), Js('Aegiolea'), Js('Aegle'), Js('Aerope'), Js('Aethre'), Js('Agamede'), Js('Aganippe'), Js('Agape'), Js('Agapia'), Js('Agarista'), Js('Agathé'), Js('Agathonice'), Js('Agave'), Js('Aglaia'), Js('Aglaurus'), Js('Aikaterine'), Js('Aithra'), Js('Aketa'), Js('Alcandre'), Js('Alcestis'), Js('Alcippe'), Js('Alcmene'), Js('Alcyone'), Js('Alemene'), Js('Alkmena'), Js('Althaea'), Js('Althaia'), Js('Althea'), Js('Amarhyllis'), Js('Amathea'), Js('Amatheia'), Js('Amphithoe'), Js('Amphitrite'), Js('Ampinomene'), Js('Amplias'), Js('Anais'), Js('Anastasia'), Js('Andromeda'), Js('Antehe'), Js('Anteia'), Js('Antheia'), Js('Anthousa'), Js('Anthusa'), Js('Anticleia'), Js('Antigone'), Js('Antiochis'), Js('Antiope'), Js('Anysia'), Js('Appollonia'), Js('Apseudes'), Js('Arete'), Js('Arethusa'), Js('Argeia'), Js('Ariadne'), Js('Arisbe'), Js('Aristonike'), Js('Aristophane'), Js('Arsinoe'), Js('Artemidora'), Js('Artemisia'), Js('Aspasia'), Js('Astera'), Js('Astyoche'), Js('Astyocheia'), Js('Atalanta'), Js('Atë'), Js('Athis'), Js('Auge'), Js('Augo'), Js('Autonoe'), Js('Auxesia'), Js('Axiothea'), Js('Barbara'), Js('Basiane'), Js('Baucis'), Js('Berenike'), Js('Bito'), Js('Briseis'), Js('Caenis'), Js('Caleope'), Js('Callianeira'), Js('Callianessa'), Js('Calliphana'), Js('Calypso'), Js('Canace'), Js('Castianiera'), Js('Charis'), Js('Chione'), Js('Chiore'), Js('Chloë'), Js('Chloris'), Js('Chryse'), Js('Chryseis'), Js('Chrysothemis'), Js('Cilissa'), Js('Cilla'), Js('Circe'), Js('Clio'), Js('Clymene'), Js('Clymere'), Js('Colubra'), Js('Corythia'), Js('Cratais'), Js('Creusa'), Js('Crisa'), Js('Ctimene'), Js('Cybele'), Js('Cydippe'), Js('Cymodoce'), Js('Cymothoe'), Js('Cyrene'), Js('Cythereia'), Js('Cytheris'), Js('Damaris'), Js('Damia'), Js('Danaë'), Js('Deianeira'), Js('Deineira'), Js('Deiphobe'), Js('Deipyle'), Js('Delias'), Js('Demetria'), Js('Demophile'), Js('Dexamene'), Js('Dianeme'), Js('Diomede'), Js('Dione'), Js('Dirce'), Js('Doris'), Js('Dorothea'), Js('Doto'), Js('Drosis'), Js('Dynamene'), Js('Egeria'), Js('Egina'), Js('Eidothee'), Js('Eileithyia'), Js('Elcmene'), Js('Electra'), Js('Elpir'), Js('Endeis'), Js('Enyo'), Js('Eos'), Js('Epicaste'), Js('Eriboea'), Js('Erigone'), Js('Eriopis'), Js('Eriphyle'), Js('Eris'), Js('Eucarpia'), Js('Eudokia'), Js('Eunice'), Js('Euodias'), Js('Euphro'), Js('Euphrosyne'), Js('Europa'), Js('Eurycleia'), Js('Eurydike'), Js('Eurynome'), Js('Evadne'), Js('Galatea'), Js('Glauce'), Js('Glyke'), Js('Gorgo'), Js('Gygaea'), Js('Haidee'), Js('Halie'), Js('Harmodias'), Js('Harmonia'), Js('Hecuba'), Js('Hekabe'), Js('Hekaline'), Js('Hekate'), Js('Helice'), Js('Helike'), Js('Heliodora'), Js('Hellanike'), Js('Helle'), Js('Hermine'), Js('Hermione'), Js('Hero'), Js('Herophile'), Js('Hesione'), Js('Hilaera'), Js('Hippodameia'), Js('Hippodamia'), Js('Hippolyta'), Js('Hypsipyle'), Js('Hyrmina'), Js('Iaera'), Js('Ianeira'), Js('Ianessa'), Js('Ianthe'), Js('Ino'), Js('Iola'), Js('Iolanthe'), Js('Iole'), Js('Iomene'), Js('Ione'), Js('Iphianassa'), Js('Iphigenia'), Js('Iphimedeia'), Js('Iphis'), Js('Iphitheme'), Js('Irene'), Js('Iris'), Js('Isadora'), Js('Ismene'), Js('Issa'), Js('Jocasta'), Js('Kallisto'), Js('Kallixeina'), Js('Kassandra'), Js('Katana'), Js('Katina'), Js('Kephissa'), Js('Kharmion'), Js('Khlöe'), Js('Khloris'), Js('Kleio'), Js('Kleopatra'), Js('Klymene'), Js('Klytemnestra'), Js('Koré'), Js('Koritto'), Js('Kydilla'), Js('Kynna'), Js('Kynthia'), Js('Kypris'), Js('Kyra'), Js('Labda'), Js('Lais'), Js('Lalage'), Js('Lampetie'), Js('Lampito'), Js('Lanike'), Js('Laodameia'), Js('Laodamia'), Js('Laodice'), Js('Laothoe'), Js('Lasthena'), Js('Latona'), Js('Leda'), Js('Lede'), Js('Leto'), Js('Leucothea'), Js('Leucothoë'), Js('Limnoreia'), Js('Lois'), Js('Lyra'), Js('Maeonia'), Js('Maera'), Js('Maia'), Js('Maiandria'), Js('Marpessa'), Js('Medea'), Js('Medesicaste'), Js('Megaera'), Js('Megara'), Js('Megare'), Js('Melanie'), Js('Melantho'), Js('Melissa'), Js('Melita'), Js('Melite'), Js('Menelaia'), Js('Merope'), Js('Metis'), Js('Metriche'), Js('Milo'), Js('Milto'), Js('Molpadia'), Js('Monima'), Js('Monime'), Js('Mykale'), Js('Myrine'), Js('Nausicaa'), Js('Neaera'), Js('Nemerte'), Js('Nephele'), Js('Nesaea'), Js('Nicopolis'), Js('Nikaia'), Js('Nikasepolis'), Js('Niko'), Js('Niobe'), Js('Nysa'), Js('Oenone'), Js('Oitane'), Js('Olympias'), Js('Omphale'), Js('Oreithuia'), Js('Oreithyia'), Js('Orithyia'), Js('Orthia'), Js('Otonia'), Js('Pales'), Js('Panope'), Js('Panora'), Js('Parthenia'), Js('Parthenope'), Js('Pasiphae'), Js('Pelopia'), Js('Penelope'), Js('Penthesilea'), Js('Percalus'), Js('Perialla'), Js('Periboea'), Js('Pero'), Js('Perse'), Js('Persephone'), Js('Persis'), Js('Pervica'), Js('Pervinca'), Js('Phaedra'), Js('Phaedre'), Js('Phaethusa'), Js('Phaia'), Js('Pherenike'), Js('Pherusa'), Js('Phigaleia'), Js('Philea'), Js('Philinna'), Js('Philomache'), Js('Philomela'), Js('Philona'), Js('Phoebe'), Js('Phryne'), Js('Phylace'), Js('Phylia'), Js('Phyllis'), Js('Phylo'), Js('Phylomedusa'), Js('Podarge'), Js('Polycaste'), Js('Polydamna'), Js('Polydora'), Js('Polymede'), Js('Polyxena'), Js('Procne'), Js('Procris'), Js('Prone'), Js('Proto'), Js('Protogonia'), Js('Psamathe'), Js('Psyche'), Js('Pylia'), Js('Pyrrha'), Js('Pythias'), Js('Raisa'), Js('Rhea'), Js('Rhene'), Js('Rhoda'), Js('Rhode'), Js('Rhodope'), Js('Roxane'), Js('Sappho'), Js('Scylla'), Js('Sebasteia'), Js('Semele'), Js('Sophia'), Js('Sotera'), Js('Speio'), Js('Stheneboea'), Js('Stratonice'), Js('Tecmessa'), Js('Telephassa'), Js('Thais'), Js('Thalassa'), Js('Thaleia'), Js('Theano'), Js('Thebe'), Js('Thelma'), Js('Themis'), Js('Theodotis'), Js('Theophane'), Js('Theophania'), Js('Theophano'), Js('Theresa'), Js('Thessala'), Js('Thessalonike'), Js('Thetis'), Js('Thisbe'), Js('Thoë'), Js('Thoösa'), Js('Thyia'), Js('Timandra'), Js('Timo'), Js('Tryphena'), Js('Tryphosa'), Js('Tyro'), Js('Xanthe'), Js('Xanthippe'), Js('Xantippe'), Js('Xene'), Js('Xenophile'), Js('Zenobia'), Js('Zita'), Js('Zoe')]))
pass
pass


# Add lib to the module scope
ancientGreekNames = var.to_python()