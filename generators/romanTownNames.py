__all__ = ['romanTownNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aballava'), Js('Aballo'), Js('Aballum'), Js('Abbatis Villa'), Js('Abdera'), Js('Abellinum'), Js('Abrittus'), Js('Abritus'), Js('Abudiacum'), Js('Abula'), Js('Abusina'), Js('Acci'), Js('Acinipo'), Js('Acrae'), Js('Acyra'), Js('Ad Aesim'), Js('Ad Anisum'), Js('Ad Flexum'), Js('Ad Iuvense'), Js('Ad Martis'), Js('Ad Mauros'), Js('Ad Mediam'), Js('Ad Novas'), Js('Ad Pontes'), Js('Ad Statuas'), Js('Adana'), Js('Ader'), Js('Adraa'), Js('Adramyttium'), Js('Aecae'), Js('Aeclanum'), Js('Aelia Capitolina'), Js('Aelium Cetium'), Js('Aeminium'), Js('Aemona'), Js('Aenus'), Js('Aequinoctium'), Js('Aesernia'), Js('Aesica'), Js('Aesis'), Js('Agathe'), Js('Agedincum'), Js('Aginnum'), Js('Agrigentum'), Js('Agrippina'), Js('Agrippina Romanorum'), Js('Aguntum'), Js('Ala Nova'), Js('Alalia'), Js('Alba Fucens'), Js('Alba Longa'), Js('Alba Regia'), Js('Albaniana'), Js('Albanum'), Js('Albiga'), Js('Albintemelium'), Js('Almus'), Js('Altinum'), Js('Ambiani'), Js('Ambracia'), Js('Ameria'), Js('Amida'), Js('Amiternum'), Js('Ammaia'), Js('Ammurianum'), Js('Anavio'), Js('Anazarbus'), Js('Anchialus'), Js('Ancona'), Js('Anderida'), Js('Anhialo'), Js('Anicium'), Js('Anio'), Js('Antino?s'), Js('Antioch'), Js('Antipolis'), Js('Antium'), Js('Apamea'), Js('Aphrodisias'), Js('Apollonia'), Js('Apollonia Pontica'), Js('Apua'), Js('Apulum'), Js('Aqua Viva'), Js('Aquae Armenetiae'), Js('Aquae Arnemetiae'), Js('Aquae Cutiliae'), Js('Aquae Flaviae'), Js('Aquae Gratianae'), Js('Aquae Helveticae'), Js('Aquae Mattiacae'), Js('Aquae Mattiacorum'), Js('Aquae Originis'), Js('Aquae Pannonicae'), Js('Aquae Sextiae'), Js('Aquae Sulis'), Js('Aquileia'), Js('Aquilonia'), Js('Aquincum'), Js('Aquis Voconis'), Js('Aquisgranium'), Js('Aquitania'), Js('Arabona'), Js('Arausio'), Js('Arbeia'), Js('Arbor Felix'), Js('Arcadiopolis'), Js('Arcidava'), Js('Arconisium'), Js('Ardotalia'), Js('Arelape'), Js('Arelate'), Js('Argentoratum'), Js('Aricia'), Js('Ariminium'), Js('Ariminum'), Js('Armorica'), Js('Arpinum'), Js('Arrabona'), Js('Arretium'), Js('Arsinoe'), Js('Arverni'), Js('Ascalon'), Js('Asisium'), Js('Asturica'), Js('Asturica Augusta'), Js('Aternum'), Js('Athenae'), Js('Atrans'), Js('Atrebatum'), Js('Atuatuca Tungrorum'), Js('Augusta Argentorate'), Js('Augusta Emerita'), Js('Augusta Praetoria'), Js('Augusta Raurica'), Js('Augusta Suessionum'), Js('Augusta Taurinorum'), Js('Augusta Traiana'), Js('Augusta Trajana'), Js('Augusta Trebecorum'), Js('Augusta Treverorum'), Js('Augusta Trevirorum'), Js('Augusta Vangiorum'), Js('Augusta Vindelicorum'), Js('Augusta Viromanduorum'), Js('Augustadorum'), Js('Augustianis'), Js('Augustobona'), Js('Augustodunum'), Js('Augustodurum'), Js('Augustomagus'), Js('Augustonementum'), Js('Augustonemetum'), Js('Augustoritum'), Js('Aurelia'), Js('Aurelia Aquensi'), Js('Aurelianorum'), Js('Aurelianum'), Js('Autricum'), Js('Avaricum'), Js('Avenio'), Js('Avennio'), Js('Aventicum'), Js('Baeloe'), Js('Baeterrae'), Js('Baetulo'), Js('Bagacum'), Js('Bagradas'), Js('Baiae'), Js('Bannaventa'), Js('Barcino'), Js('Barduli'), Js('Barium'), Js('Basilea'), Js('Basilia'), Js('Basti'), Js('Batavis'), Js('Bauzanum'), Js('Bedriacum'), Js('Belgica'), Js('Belginum'), Js('Bellunum'), Js('Beneventum'), Js('Bergomum'), Js('Bergula'), Js('Beroe Augusta Trajana'), Js('Berytus'), Js('Berzobis'), Js('Besontio'), Js('Bethar'), Js('Bilachinium'), Js('Bilbilis'), Js('Bilbilis Italica'), Js('Bisanthe'), Js('Blariacum'), Js('Bobium Ebovium'), Js('Bona'), Js('Bonna'), Js('Bononia'), Js('Bononia Malata'), Js('Boreana'), Js('Bosona'), Js('Bostra'), Js('Bracara Augusta'), Js('Bremetennacum Veteranorum'), Js('Brigantium'), Js('Brigetio'), Js('Britannia'), Js('Brivas'), Js('Brixellum'), Js('Brixia'), Js('Brundisium'), Js('Budalia'), Js('Bulla Regia'), Js('Burdigala'), Js('Burrium'), Js('Butunti'), Js('Byblus'), Js('Byzantium'), Js('Caenophrurium'), Js('Caere'), Js('Caesaraugusta'), Js('Caesarea'), Js('Caesarea Maritima'), Js('Caesarea Mazaca'), Js('Caesarodunum'), Js('Caesaromagus'), Js('Caesena'), Js('Calagurris'), Js('Calagurris Iulia Nasica'), Js('Calcaria'), Js('Calceus Herculis'), Js('Caledonia'), Js('Callatis'), Js('Calleva Atrebatum'), Js('Camaracum'), Js('Camasiacum'), Js('Cambria'), Js('Camerinum'), Js('Campi Catalaunii'), Js('Campona'), Js('Campus vassorum'), Js('Camulodunum'), Js('Canatha'), Js('Cannabiaca'), Js('Cannae'), Js('Cantabrigia'), Js('Canusium'), Js('Canusum'), Js('Capena'), Js('Caprae'), Js('Capreae'), Js('Caprera'), Js('Capsa'), Js('Capua'), Js('Carales'), Js('Caralis'), Js('Caranusca'), Js('Carcaso'), Js('Carmo'), Js('Carmona'), Js('Carnotum'), Js('Carnuntum'), Js('Caromago'), Js('Carrhae'), Js('Carsioli'), Js('Carsulae'), Js('Carteia'), Js('Cartennae'), Js('Carthago'), Js('Carthago Nova'), Js('Cascantum'), Js('Casilinum'), Js('Casinum'), Js('Castellum Flevum'), Js('Castellum apud Confluentes'), Js('Castra Batava'), Js('Castra Batavorum'), Js('Castra Bonnensia'), Js('Castra Devana'), Js('Castra Martis'), Js('Castra Nicia'), Js('Castra Nova'), Js('Castra Regina'), Js('Castra Taurinorum'), Js('Castra Vetera'), Js('Castra ad Herculem'), Js('Castri locus'), Js('Castrum Deutonis'), Js('Castrum Octavianum'), Js('Castulo'), Js('Catania'), Js('Cataractonium'), Js('Cauca'), Js('Caudium'), Js('Caurium'), Js('Causennae'), Js('Celaenae'), Js('Celeia'), Js('Celsa'), Js('Cenabum'), Js('Cenabum Aureliani'), Js('Cenebelum'), Js('Centum Cellae'), Js('Centumcellai'), Js('Ceuniacum'), Js('Chalcedon'), Js('Chrysopolis'), Js('Chullu'), Js('Cibalae'), Js('Cidamus'), Js('Cillium'), Js('Cilurnum'), Js('Circesium'), Js('Cirpi'), Js('Cirta'), Js('Civitas Nerviorum'), Js('Civitas Sancti Romuli'), Js('Claudiopolis'), Js('Clausentum'), Js('Clotagenium'), Js('Clunia'), Js('Clupea'), Js('Clusium'), Js('Colonia Agrippina'), Js('Colonia Agrippina(e)'), Js('Colonia Agrippinensium'), Js('Colonia Antiocheia'), Js('Colonia Augusta Emerita'), Js('Colonia Baelo Claudia'), Js('Colonia Caecilia Metellinum'), Js('Colonia Caesar Augusta'), Js('Colonia Claudia Savaria'), Js('Colonia Flavia Scupi'), Js('Colonia Forum Segusiavorum'), Js('Colonia Iulia Equestris'), Js('Colonia Iulia Gemella Acci'), Js('Colonia Iulia Illici Augusta'), Js('Colonia Iulia Romula'), Js('Colonia Julia Carthago'), Js('Colonia Nemausa'), Js('Colonia Norba Caesarina'), Js('Colonia Patricia'), Js('Colonia Ulpia Traiana'), Js('Colonia Victrix Iulia Celsa'), Js('Colonia Victrix Iulia Lepida'), Js('Comagena'), Js('Complutum'), Js('Comum'), Js('Concangis'), Js('Concordia Sagittaria'), Js('Condate'), Js('Condate Redones'), Js('Condate Redonum'), Js('Condate Riedonum'), Js('Condatomagus'), Js('Conimbriga'), Js('Consentia'), Js('Constantia'), Js('Constantinopolis'), Js('Corcyra'), Js('Corduba'), Js('Corfinium'), Js('Coria'), Js('Coriallum'), Js('Corinium'), Js('Corinium Dobunnorum'), Js('Coriovallum'), Js('Corisopitum'), Js('Coristopitum'), Js('Cornelii'), Js('Corstopitum'), Js('Cortona'), Js('Cortoriacum'), Js('Corvinium'), Js('Cosa'), Js('Cremona'), Js('Croton'), Js('Crotona'), Js('Cuicul'), Js('Cularo'), Js('Cumae'), Js('Cunetio'), Js('Curia'), Js('Cydamae'), Js('Cyrene'), Js('Danaster'), Js('Danum'), Js('Danuvius'), Js('Darioritum'), Js('Decem Pagi'), Js('Derthona'), Js('Dertona'), Js('Dertosa'), Js('Derventio'), Js('Deva'), Js('Dianinum'), Js('Dierna'), Js('Dimale'), Js('Dimum'), Js('Diocletianopolis'), Js('Dionysopolis'), Js('Divio'), Js('Divodurum'), Js('Drepana'), Js('Drepanum'), Js('Drobeta'), Js('Drusus'), Js('Duacum'), Js('Dubris'), Js('Dumatha'), Js('Dunum'), Js('Duranius'), Js('Durnovaria'), Js('Durobrivae'), Js('Durocatalaunum'), Js('Durocobrivis'), Js('Durocornovium'), Js('Durocorotum'), Js('Durocortorum'), Js('Durocortorum Remorum'), Js('Durolipons'), Js('Durolitum'), Js('Durostorum'), Js('Durovernon'), Js('Durovernum'), Js('Durovernum Cantiacorum'), Js('Durovigutum'), Js('Dyrrachium'), Js('Dyrrhachium'), Js('Eboracum'), Js('Ebrus'), Js('Eburacum'), Js('Eburodunum'), Js('Ecnomus'), Js('Egara'), Js('Egnatia'), Js('Emerita'), Js('Emerita Augusta'), Js('Emesa'), Js('Emona'), Js('Emporiae'), Js('Epidamnus'), Js('Eporedia'), Js('Eryx'), Js('Evidensca'), Js('Fabiranum'), Js('Faesulae'), Js('Falerii Novi'), Js('Fanum Fortunae'), Js('Faventia'), Js('Favianis'), Js('Firmum'), Js('Flavia Solva'), Js('Florentia'), Js('Formiae'), Js('Forum Claudii Vallensium'), Js('Forum Hadriani'), Js('Forum Iulii'), Js('Forum Livii'), Js('Forum Lulii'), Js('Forum Popilii'), Js('Fulginiae'), Js('Fundi'), Js('Gades'), Js('Gandava'), Js('Gariannonum'), Js('Garrianonum'), Js('Garumna'), Js('Geminiacum'), Js('Genava'), Js('Geneva'), Js('Genua'), Js('Gerasa'), Js('Germania'), Js('Gerontium'), Js('Gerulata'), Js('Gesoriacum'), Js('Gigia'), Js('Glannaventa'), Js('Glevum'), Js('Glevum Colonia'), Js('Gorsium'), Js('Graccurris'), Js('Gratianopolis'), Js('Hadria'), Js('Hadrianopolis'), Js('Hadrianutherae'), Js('Hadrumetum'), Js('Haenna'), Js('Haga-Comitis'), Js('Hasta'), Js('Heliopolis'), Js('Heraclea'), Js('Heraclea Lyncestis'), Js('Herculaneum'), Js('Herculea'), Js('Herdonia'), Js('Hibernia'), Js('Hierosolyma'), Js('Hippo Diarrhytus'), Js('Hippo Regius'), Js('Hippo Zarytus'), Js('Hispalis'), Js('Hispellum'), Js('Histria'), Js('Hoius Vicus'), Js('Hortonium'), Js('Hydruntum'), Js('Iaurinum'), Js('Iberia'), Js('Iculisma'), Js('Iguvium'), Js('Ilerda'), Js('Illici'), Js('Iluro'), Js('Interamna Nahars'), Js('Interamnia Praetutiana'), Js('Intercisa'), Js('Ioviacum'), Js('Isara'), Js('Isca'), Js('Isca Augusta'), Js('Isca Dumnoniorum'), Js('Istropolis'), Js('Istrus'), Js('Isurium'), Js('Isurium Brigantum'), Js('Italica'), Js('Iuenna'), Js('Iulia Concordia'), Js('Iulia Traducta'), Js('Iulium Carnicum'), Js('Juliobona'), Js('Juliobriga'), Js('Juliomagus'), Js('Juvavum'), Js('Labacum'), Js('Labellum'), Js('Lactodorum'), Js('Lagentium'), Js('Lambaesis'), Js('Lanuvium'), Js('Lapurdum'), Js('Lascuta'), Js('Latopolis'), Js('Lauriacum'), Js('Lavatrae'), Js('Lederata'), Js('Legentium'), Js('Legio'), Js('Lemincum'), Js('Lemonum'), Js('Lentia'), Js('Lentie'), Js('Leptis Magna'), Js('Letocetum'), Js('Leucarum'), Js('Liberalitas Julia'), Js('Liburnum'), Js('Liger'), Js('Lihnidos'), Js('Lilybaeum'), Js('Limonum'), Js('Lincium'), Js('Lindinis'), Js('Lindum'), Js('Lindum Colonia'), Js('Liniacum'), Js('Londinium'), Js('Lousanna'), Js('Luca'), Js('Lucentum'), Js('Luceria'), Js('Lucus Augusti'), Js('Luentinum'), Js('Lugdunum'), Js('Lugdunum Batavorum'), Js('Lugio'), Js('Luguvalium'), Js('Luguvallum'), Js('Luna'), Js('Lupiae'), Js('Lusitania'), Js('Lusonum'), Js('Lussonium'), Js('Lutetia'), Js('Lutetia Parisiorum'), Js('Lutonium'), Js('Madauros'), Js('Magador'), Js('Malaca'), Js('Malata Bonenia'), Js('Mamucium'), Js('Mancunium'), Js('Manduessedum'), Js('Mantua'), Js('Marcianopolis'), Js('Maromago'), Js('Marsonia'), Js('Massilia'), Js('Matrica'), Js('Mattium'), Js('Mauriciacum'), Js('Mazaca'), Js('Mediolanum'), Js('Mediolanum Aulercorum'), Js('Mediolanum Santonum'), Js('Melitene'), Js('Melta'), Js('Messambria'), Js('Messana'), Js('Metapontum'), Js('Metellinum'), Js('Metheola'), Js('Metis'), Js('Mevania'), Js('Minturnae'), Js('Misenum'), Js('Moenum'), Js('Mogentianae'), Js('Mogontiacum'), Js('Moguntiacum'), Js('Mons Bellona'), Js('Montana'), Js('Moridunum'), Js('Mosa Trajectum'), Js('Municipium Augusta Bilbilis'), Js('Mursa'), Js('Mutina'), Js('Naissus'), Js('Napoca'), Js('Narbo'), Js('Narbo Martius'), Js('Navio'), Js('Neapolis'), Js('Nemausus'), Js('Nemetacum Atrebatum'), Js('Nepte'), Js('Nequinum'), Js('Neropolis'), Js('Nervia Glevensium'), Js('Neviodunum'), Js('Nevirnum'), Js('Nicaea'), Js('Nicopolis'), Js('Nidum'), Js('Nola'), Js('Nora'), Js('Norba'), Js('Noreia'), Js('Novae'), Js('Novaesium'), Js('Novaria'), Js('Noviodunum'), Js('Noviodunum Aeduorum'), Js('Noviomagus'), Js('Noviomagus Batavodurum'), Js('Noviomagus Cantiacorum'), Js('Noviomagus Reginorum'), Js('Novioritum'), Js('Novodunum'), Js('Numantia'), Js('Nursia'), Js('Obulco'), Js('Ocriculum'), Js('Octodurum'), Js('Octodurus'), Js('Odessus'), Js('Oea'), Js('Oenipons'), Js('Oenipontum'), Js('Olicana'), Js('Olisipo'), Js('Olmedum'), Js('Onuba'), Js('Opitergium'), Js('Oppidum Atuaticorum'), Js('Oppidum Batavorum'), Js('Oppidum Ubiorum'), Js('Orolaunum'), Js('Osca'), Js('Osset'), Js('Ossonoba'), Js('Ostia'), Js('Ostia Aterni'), Js('Ostium'), Js('Ovilava'), Js('Padus'), Js('Paestum'), Js('Palmyra'), Js('Panormus'), Js('Paraetonium'), Js('Parentium'), Js('Patavium'), Js('Pautalia'), Js('Pax Iulia'), Js('Perinthus'), Js('Perusia'), Js('Pharos'), Js('Philadelphia'), Js('Philippopolis'), Js('Pisa'), Js('Pisae'), Js('Pisaurum'), Js('Pistorium'), Js('Placentia'), Js('Podium Aniciense'), Js('Poetovio'), Js('Pola'), Js('Pollentia'), Js('Pompaelo'), Js('Pompeii'), Js('Pons Aelius'), Js('Pons Saravi'), Js('Pons aelii'), Js('Pontus Fractus'), Js('Populonium'), Js('Portus'), Js('Portus Adurni'), Js('Portus Cale'), Js('Portus Felix'), Js('Portus Itius'), Js('Portus Lemanis'), Js('Portus Magnus'), Js('Portus Namnetus'), Js('Portus Naonis'), Js('Posonium'), Js('Potaissa'), Js('Potentia'), Js('Praeneste'), Js('Praesidium'), Js('Praesidium Iulium'), Js('Praetorium'), Js('Praetorium Agrippinae'), Js('Praetorium Latobicorum'), Js('Ptolemais'), Js('Pumbedita'), Js('Puteoli'), Js('Quinque-Ecclesiis'), Js('Radasbona'), Js('Raetinium'), Js('Ragusa'), Js('Ragusa Ibla'), Js('Raphae'), Js('Ratae Corieltauvorum'), Js('Ratae Coritanorum'), Js('Ratea Colitanorum'), Js('Ratiara'), Js('Ravenna'), Js('Reginca'), Js('Regium Lepidi'), Js('Regium Lepidum'), Js('Regnum'), Js('Regulbium'), Js('Resapha'), Js('Rhaedestus'), Js('Rhegium'), Js('Rhegium Julium'), Js('Rhenus'), Js('Rhodanos'), Js('Ricciacum'), Js('Rigomagus'), Js('Risinium'), Js('Roma'), Js('Rothnacum'), Js('Rotomagus'), Js('Rusaddir'), Js('Rusicade'), Js('Rutupiae'), Js('Sabaria'), Js('Sabratha'), Js('Saena Julia'), Js('Saenna Julia'), Js('Saetabis'), Js('Saguntum'), Js('Saldae'), Js('Salduba'), Js('Salernum'), Js('Salinae'), Js('Salmantica'), Js('Salodurum'), Js('Salonae'), Js('Salva'), Js('Samarobriva'), Js('Samarobriva Ambianorum'), Js('Sarmizegethusa'), Js('Savaria'), Js('Savo'), Js('Savona'), Js('Scallabis'), Js('Scarbantia'), Js('Scupi'), Js('Scylacium'), Js('Segobriga'), Js('Segontium'), Js('Segovia'), Js('Segusio'), Js('Seleucia'), Js('Selymbria'), Js('Sempronium'), Js('Senones'), Js('Serdica'), Js('Sergiopolis'), Js('Sexaginta Prista'), Js('Sicca Veneria'), Js('Silvium'), Js('Simitthu'), Js('Singidunum'), Js('Sinope'), Js('Sinuessa'), Js('Sipontum'), Js('Sippar'), Js('Sirmium'), Js('Siscia'), Js('Sitifis'), Js('Solva'), Js('Sopianae'), Js('Sora'), Js('Sorviodunum'), Js('Sorviodurum'), Js('Sozopolis'), Js('Spalatum'), Js('Spoletium'), Js('Stabiae'), Js('Stirpiacum'), Js('Stobi'), Js('Storgozia'), Js('Suasa'), Js('Sucidava'), Js('Sufetula'), Js('Sulloniacis'), Js('Superiacum'), Js('Sutrium'), Js('Sybaris'), Js('Syene'), Js('Syracusae'), Js('Taginae'), Js('Taparura'), Js('Tarentum'), Js('Tarquinii'), Js('Tarracina'), Js('Tarraco'), Js('Tarvisium'), Js('Taurinum'), Js('Tauromenium'), Js('Teate Marrucinorum'), Js('Telo Martius'), Js('Tenedo'), Js('Tentyra'), Js('Tergeste'), Js('Tergestum'), Js('Teurnia'), Js('Thamugadi'), Js('Thermae Himerenses'), Js('Theveste'), Js('Thuburbo Maius'), Js('Thugga'), Js('Thysdrus'), Js('Tibur'), Js('Ticinum'), Js('Ticinum Papiae'), Js('Tifernum Tiberinum'), Js('Tigurum'), Js('Tingi'), Js('Tolbiacum'), Js('Toletum'), Js('Tolosa'), Js('Tomis'), Js('Tornacum'), Js('Traiectum Eriditum'), Js('Traiectum ad Mosam'), Js('Trajectum ad Rhenum'), Js('Trapezus'), Js('Trebizond'), Js('Tres Tabernae'), Js('Treviri'), Js('Tricciana'), Js('Tricensimae'), Js('Tridentum'), Js('Trimontium'), Js('Tripolis'), Js('Tripontium'), Js('Tropaeum Traiani'), Js('Tuder'), Js('Tullum Leucorum'), Js('Tupusuctu'), Js('Turiaso'), Js('Turiaso Silbis'), Js('Turicim'), Js('Turicum'), Js('Turnacum Nerviorum'), Js('Tusculum'), Js('Tyrus'), Js('Ugernum'), Js('Ulcisia Castra'), Js('Ulpia Novomagus'), Js('Umbracum'), Js('Urbinum Hortense'), Js('Urbinum Mataurense'), Js('Urbs Victrix Osca'), Js('Uria'), Js('Utina'), Js('Utinum'), Js('Vagniacea'), Js('Valcum'), Js('Valentia'), Js('Valentia Edetanorum'), Js('Valentianae'), Js('Varadinum'), Js('Vasio Vocontiorum'), Js('Vectis'), Js('Vedinum'), Js('Veii'), Js('Veldidena'), Js('Velia'), Js('Velitrae'), Js('Venetiae'), Js('Venta Belgarum'), Js('Venta Icenorum'), Js('Venta Silurum'), Js('Venusia'), Js('Veralamium'), Js('Vercellae'), Js('Vernementum'), Js('Verodunum'), Js('Verona'), Js('Verulamium'), Js('Vesuna'), Js('Vesunna'), Js('Vetera'), Js('Vetulonia'), Js('Vezeliacum'), Js('Vibo Valentia'), Js('Vicentia'), Js('Vicus Belginum'), Js('Vicus Elbii'), Js('Vicus Leodicus'), Js('Vienna'), Js('Vigiliae'), Js('Viglebanum'), Js('Vigueria'), Js('Viminiacum'), Js('Vindinium'), Js('Vindobona'), Js('Vindolanda'), Js('Vindomora'), Js('Vindonissa'), Js('Vinovia'), Js('Vinovium'), Js('Vipitenum'), Js('Viroconium'), Js('Viroconium Cornoviorum'), Js('Viroviacum'), Js('Virunum'), Js('Vitudurum'), Js('Vizeliacum'), Js('Volaterrae'), Js('Volsinii'), Js('Volsinii Novi'), Js('Volubilis'), Js('Vorgium'), Js('Vuenteka super fluvium Therma'), Js('Vulci'), Js('Xanthus'), Js('Zaitha'), Js('Zama Regia'), Js('Zela'), Js('Zeugma')]))
pass
pass


# Add lib to the module scope
romanTownNames = var.to_python()