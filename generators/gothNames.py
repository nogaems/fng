__all__ = ['gothNames']

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
    var.put('nm1', Js([Js('Ablabius'), Js('Achila'), Js('Agila'), Js('Agiwulf'), Js('Agriwulf'), Js('Aidoingus'), Js('Aithanarid'), Js('Alaric'), Js('Alatheus'), Js('Alaviv'), Js('Alica'), Js('Aligern'), Js('Alla'), Js('Amal'), Js('Amalaric'), Js('Ammius'), Js('Anagastes'), Js('Andagis'), Js('Anianus'), Js('Ansila'), Js('Ansis'), Js('Aoric'), Js('Apahida'), Js('Ardabur'), Js('Ardaric'), Js('Argaith'), Js('Ariaric'), Js('Arimir'), Js('Arius'), Js('Arnegliscus'), Js('Arvandus'), Js('Asbad'), Js('Aspar'), Js('Ataulf'), Js('Ataulph'), Js('Athalaric'), Js('Athanagild'), Js('Athanaric'), Js('Atharid'), Js('Athaulf'), Js('Babai'), Js('Badua'), Js('Baduila'), Js('Baza'), Js('Berig'), Js('Berimud'), Js('Berimund'), Js('Bessa'), Js('Bessas'), Js('Bessi'), Js('Beuca'), Js('Beucad'), Js('Bigelis'), Js('Bilimer'), Js('Borani'), Js('Braga'), Js('Brandila'), Js('Candac'), Js('Cannabas'), Js('Cannabaudes'), Js('Cethegus'), Js('Chindasuinth'), Js('Cniva'), Js('Cnivida'), Js('Colias'), Js('Crocus'), Js('Cunigast'), Js('Cunimund'), Js('Cyrila'), Js('Dubius'), Js('Duda'), Js('Ebermud'), Js('Eberwolf'), Js('Ebrimud'), Js('Edica'), Js('Eraric'), Js('Eriulf'), Js('Ermanaric'), Js('Ermelandus'), Js('Ervig'), Js('Euric'), Js('Eutharic'), Js('Farnobius'), Js('Fastida'), Js('Feletheus'), Js('Feva'), Js('Filimer'), Js('Flaccitheus'), Js('Fravitta'), Js('Fredegar'), Js('Fretela'), Js('Frideric'), Js('Fridigern'), Js('Frigeridus'), Js('Frithila'), Js('Fritigern'), Js('Gadaric'), Js('Gainas'), Js('Gaiseric'), Js('Galindo'), Js('Galindus'), Js('Gaut'), Js('Gauterit'), Js('Geberic'), Js('Gelimer'), Js('Gento'), Js('Gerung'), Js('Gesalec'), Js('Gesimund'), Js('Getica'), Js('Goar'), Js('Goddas'), Js('Godegisel'), Js('Godigisclus'), Js('Goiaricus'), Js('Gouththas'), Js('Gundehar'), Js('Gundiok'), Js('Gundobad'), Js('Gunteric'), Js('Gunthigis'), Js('Gutthikas'), Js('Hadubrand'), Js('Heldebald'), Js('Heldefredus'), Js('Heribrand'), Js('Hermangild'), Js('Hermenigild'), Js('Herminafrid'), Js('Hernegliscus'), Js('Hildebad'), Js('Hildebrand'), Js('Hilderic'), Js('Hilderith'), Js('Himnerith'), Js('Hisarna'), Js('Hulmul'), Js('Huml'), Js('Huneric'), Js('Hunigild'), Js('Hunimund'), Js('Hunulf'), Js('Hunumund'), Js('Ibba'), Js('Ildebad'), Js('Inna'), Js('Irnfried'), Js('Jordanes'), Js('Lagariman'), Js('Lampridius'), Js('Leovigild'), Js('Leuvibild'), Js('Livila'), Js('Marcomir'), Js('Modaharius'), Js('Modares'), Js('Munderic'), Js('Mundo'), Js('Namatius'), Js('Naulabates'), Js('Nidada'), Js('Niketas'), Js('Odoin'), Js('Odotheus'), Js('Odovacar'), Js('Ostrogotha'), Js('Osuin'), Js('Ovida'), Js('Patza'), Js('Radagaisus'), Js('Rausimod'), Js('Recared'), Js('Reccared'), Js('Recceswinth'), Js('Rechiar'), Js('Rechimund'), Js('Recitach'), Js('Rekitach'), Js('Remismund'), Js('Respa'), Js('Retemeris'), Js('Rhima'), Js('Ricimer'), Js('Rictiovarus'), Js('Rikiar'), Js('Roderic'), Js('Rodolf'), Js('Roduulf'), Js('Rudesind'), Js('Saba'), Js('Sadagares'), Js('Safrax'), Js('Salla'), Js('Sangiban'), Js('Sansalas'), Js('Saphrax'), Js('Sarus'), Js('Segeric'), Js('Selenas'), Js('Shapur'), Js('Sidimund'), Js('Sigeric'), Js('Sigesar'), Js('Sigibald'), Js('Sigismund'), Js('Sigisvult'), Js('Sindila'), Js('Sisbert'), Js('Sisebut'), Js('Sisenand'), Js('Soas'), Js('Suatrius'), Js('Sueridus'), Js('Sunericus'), Js('Sunnia'), Js('Tanais'), Js('Tanca'), Js('Teias'), Js('Teja'), Js('Tharuaro'), Js('Thela'), Js('Theodahad'), Js('Theodehad'), Js('Theodemer'), Js('Theoderic'), Js('Theoderid'), Js('Theodoric'), Js('Theodulf'), Js('Theudegisel'), Js('Theudegisklos'), Js('Theudis'), Js('Thidrek'), Js('Thiudimir'), Js('Thorismud'), Js('Thorismund'), Js('Thrasamund'), Js('Thrasaric'), Js('Thraustila'), Js('Totila'), Js('Tribigild'), Js('Tufa'), Js('Tuluin'), Js('Ulfilas'), Js('Unigild'), Js('Unila'), Js('Unimund'), Js('Uraias'), Js('Valamer'), Js('Valamir'), Js('Valaravans'), Js('Valia'), Js('Vandalarius'), Js('Vandil'), Js('Veduco'), Js('Vetericus'), Js('Vetranio'), Js('Videric'), Js('Vidigoia'), Js('Vidimir'), Js('Viliaris'), Js('Vinitharius'), Js('Visimar'), Js('Vithimiris'), Js('Vithmiris'), Js('Vitigis'), Js('Vittamar'), Js('Vultuulf'), Js('Wala'), Js('Walahmar'), Js('Wallia'), Js('Wamba'), Js('Wella'), Js('Winguric'), Js('Witige'), Js('Wittigis'), Js('Wittiza')]))
    var.put('nm2', Js([Js('Aalissa'), Js('Adosinda'), Js('Aleyda'), Js('Algonda'), Js('Alisa-Sophie'), Js('Alwina'), Js('Amala'), Js('Amalafrida'), Js('Amalasontha'), Js('Amalasuintha'), Js('Amalasuntha'), Js('Amalaswinth'), Js('Amalaswintha'), Js('Amalberga'), Js('Amalberta'), Js('Amalburga'), Js('Amalda'), Js('Amalfrida'), Js('Amalfrieda'), Js('Amalfriede'), Js('Amalgard'), Js('Amalgunda'), Js('Amalgundis'), Js('Amalina'), Js('Amalindis'), Js('Amalwara'), Js('Amelie'), Js('Amelina'), Js('Anouk'), Js('Areagne'), Js('Arika'), Js('Attala'), Js('Avagisa'), Js('Avina'), Js('Bjarka'), Js('Brenhilda'), Js('Brunhilda'), Js('Brunichild'), Js('Brunihild'), Js('Buffy'), Js('Chlodoswintha'), Js('Chlotsuintha'), Js('DÃ¶rthe-Julia'), Js('Elianor'), Js('Elisaweta'), Js('Elja'), Js('Emalia'), Js('Emelia'), Js('Ereleuva'), Js('Erelieva'), Js('Feenja'), Js('Fredegonda'), Js('Gaatha'), Js('Gailavira'), Js('Gailesvintha'), Js('Garsendis'), Js('Geleswintha'), Js('Geloyra'), Js('Gelvira'), Js('Giso'), Js('Glismoda'), Js('Goisvintha'), Js('Gosvintha'), Js('Gudeliva'), Js('Heidrun-Gabriela'), Js('Helchen'), Js('Hermangild'), Js('Hermesind'), Js('Heva'), Js('Hilduara'), Js('Hunila'), Js('Jeanne-Alice'), Js('Kaethe'), Js('Kriemhild'), Js('Limiteti'), Js('Lioba'), Js('Liuva'), Js('Lorelei'), Js('Lucienne'), Js('Malasintha'), Js('Matasuntha'), Js('Matasvintha'), Js('Megan-Laureen'), Js('Melisanda'), Js('Melisande'), Js('Melisenda'), Js('Melle'), Js('Melusine'), Js('Mia-Selina'), Js('Mira'), Js('Monia'), Js('Narin'), Js('Oonagh'), Js('Ostrogotho'), Js('Radegond'), Js('Radegonda'), Js('Rasha'), Js('Rautgundis'), Js('Richildis'), Js('Riciberga'), Js('Seda'), Js('Sunigilda'), Js('Sunilda'), Js('Talida'), Js('Teja'), Js('Theodananda'), Js('Thiudigotho'), Js('Vadamerca'), Js('Valdamerca'), Js('Wilgefortis')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
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
gothNames = var.to_python()