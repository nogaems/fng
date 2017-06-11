__all__ = ['byzantineNames']

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
    var.registers(['nm1', 'nm4', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Ablabius'), Js('Abundanitus'), Js('Agnellus'), Js('Alexius'), Js('Alypius'), Js('Ambrosius'), Js('Ammonianus'), Js('Anastasius'), Js('Ancius'), Js('Andronicus'), Js('Anicius'), Js('Annibalianus'), Js('Anthemius'), Js('Apollinare'), Js('Apollonius'), Js('Arethas'), Js('Armenius'), Js('Armentarius'), Js('Athanasius'), Js('Aurelius'), Js('Auxentius'), Js('Auxitius'), Js('Avienus'), Js('Bacchus'), Js('Bardas'), Js('Basil'), Js('Basilides'), Js('Basiliscus'), Js('Basilius'), Js('Beatus'), Js('Belisarius'), Js('Bonifatius'), Js('Calixtus'), Js('Callinicus'), Js('Carinus'), Js('Castinus'), Js('Cephalas'), Js('Cerinthus'), Js('Cerularius'), Js('Chrysaphius'), Js('Clemens'), Js('Constantianus'), Js('Constantine'), Js('Constantinianus'), Js('Constantinus'), Js('Constantius'), Js('Critobulus'), Js('Cyril'), Js('Dalmatius'), Js('David'), Js('Decentius'), Js('Delmatius'), Js('Demetrius'), Js('Dioscorus'), Js('Domianus'), Js('Domnicus'), Js('Domninus'), Js('Donus'), Js('Dulcitius'), Js('Enomius'), Js('Epiphanius'), Js('Eulalius'), Js('Eusebius'), Js('Eustachius'), Js('Eustathius'), Js('Euthymius'), Js('Eutropius'), Js('Evaristus'), Js('Evgrius'), Js('Faustus'), Js('Florentinus'), Js('Florentius'), Js('Florian'), Js('Florus'), Js('Francio'), Js('Fructosus'), Js('Fulgentius'), Js('Gallienus'), Js('Gemistos'), Js('Georgios'), Js('Georgius'), Js('Germanus'), Js('Gratian'), Js('Gregorius'), Js('Harmatius'), Js('Heracleonas'), Js('Heraclius'), Js('Hilarianus'), Js('Hilarius'), Js('Hippolytus'), Js('Honoratus'), Js('Honorius'), Js('Iamblichus'), Js('Ianuarius'), Js('Innocentius'), Js('Iovinus'), Js('Iovivus'), Js('Isaac'), Js('Isidorus'), Js('Joannes'), Js('John'), Js('Justinian'), Js('Justinianus'), Js('Lactanius'), Js('Laonicus'), Js('Latinius'), Js('Leo'), Js('Leontinus'), Js('Leontius'), Js('Libanius'), Js('Liberius'), Js('Lucas'), Js('Lukas'), Js('Macedonius'), Js('Magnentius'), Js('Manuel'), Js('Marcian'), Js('Martinianus'), Js('Martyrius'), Js('Maurentius'), Js('Maurianus'), Js('Maurice'), Js('Mauricius'), Js('Maurinus'), Js('Maurus'), Js('Maxentius'), Js('Maximianus'), Js('Maximin'), Js('Maximinus'), Js('Maximus'), Js('Mercurius'), Js('Michael'), Js('Mundus'), Js('Narses'), Js('Nepotian'), Js('Nestorius'), Js('Nicephorus'), Js('Nicetas'), Js('Nonnosus'), Js('Nonnus'), Js('Olympiodorus'), Js('Opilio'), Js('Palladius'), Js('Paternus'), Js('Patricius'), Js('Paulus'), Js('Pegarius'), Js('Petronas'), Js('Petrus'), Js('Phillipicus'), Js('Photius'), Js('Praesentinus'), Js('Praetextatus'), Js('Principius'), Js('Priscian'), Js('Priscianus'), Js('Priscillian'), Js('Probus'), Js('Proclus'), Js('Procopius'), Js('Prudentius'), Js('Psellus'), Js('Quintus'), Js('Regino'), Js('Romanus'), Js('Sabbatius'), Js('Satyrus'), Js('Sebastianus'), Js('Sergius'), Js('Simplicius'), Js('Suda'), Js('Synesius'), Js('Theodoretos'), Js('Theodosius'), Js('Theophanes'), Js('Theophilus'), Js('Trascallisseus'), Js('Tribonianus'), Js('Tribunas'), Js('Urbicus'), Js('Valens'), Js('Venantius'), Js('Venerandus'), Js('Vetranis'), Js('Viator'), Js('Victorinus'), Js('Vigilius'), Js('Vincentius'), Js('Virus'), Js('Vitalianus'), Js('Vitalius'), Js('Volusian'), Js('Zeno'), Js('Zephyrinus')]))
    var.put('nm2', Js([Js('Adeodata'), Js('Adula'), Js('Aelia'), Js('Aemiliana'), Js('Aetheria'), Js('Aetia'), Js('Agnella'), Js('Agnes'), Js('Alexandria'), Js('Anastasia'), Js('Anna'), Js('Anthemia'), Js('Anthusa'), Js('Antipatra'), Js('Antonina'), Js('Anzoy'), Js('Appa'), Js('Arabia'), Js('Aretha'), Js('Arethusa'), Js('Argentea'), Js('Armentaria'), Js('Athanasia'), Js('Athenaïs'), Js('Athenais'), Js('Augustina'), Js('Aurelia'), Js('Aureliana'), Js('Basilia'), Js('Basina'), Js('Baudegundis'), Js('Bobila'), Js('Bore'), Js('Calixta'), Js('Callinia'), Js('Campana'), Js('Candida'), Js('Casia'), Js('Casiane'), Js('Catella'), Js('Cervella'), Js('Cesarea'), Js('Charito'), Js('Clementina'), Js('Columba'), Js('Comito'), Js('Consolantia'), Js('Constantia'), Js('Constantina'), Js('Costantia'), Js('Cyra'), Js('Damiane'), Js('Delmatia'), Js('Demetria'), Js('Destasia'), Js('Didyma'), Js('Domentzia'), Js('Dominica'), Js('Domnica'), Js('Domnola'), Js('Eirene'), Js('Epiphania'), Js('Eudocia'), Js('Eudoxia'), Js('Eugenia'), Js('Eulalia'), Js('Euphemia'), Js('Euphrasia'), Js('Eusebia'), Js('Evantia'), Js('Fausta'), Js('Firmina'), Js('Flavia'), Js('Flora'), Js('Gabrielia'), Js('Galla'), Js('Georgia'), Js('Germana'), Js('Gordia'), Js('Gordiana'), Js('Gregoria'), Js('Helena'), Js('Herena'), Js('Hesychia'), Js('Honorata'), Js('Honoria'), Js('Ianuaria'), Js('Ionna'), Js('Ionnia'), Js('Ionnina'), Js('Irene'), Js('Italica'), Js('Iulia'), Js('Iuliana'), Js('Iustina'), Js('Justina'), Js('Labinia'), Js('Leocadia'), Js('Leontia'), Js('Libania'), Js('Lucia'), Js('Lucilla'), Js('Macedonia'), Js('Marcellina'), Js('Marcia'), Js('Maria'), Js('Martha'), Js('Martina'), Js('Masticana'), Js('Maximina'), Js('Megaris'), Js('Megethia'), Js('Melissa'), Js('Minervina'), Js('Minicea'), Js('Nereida'), Js('Nicasia'), Js('Nonna'), Js('Olympia'), Js('Olympiodora'), Js('Palatina'), Js('Passara'), Js('Pateria'), Js('Patricia'), Js('Paula'), Js('Paulina'), Js('Pericleia'), Js('Petronella'), Js('Petronia'), Js('Placidia'), Js('Placidina'), Js('Pompeiana'), Js('Popilia'), Js('Praeiecta'), Js('Prisca'), Js('Priscilla'), Js('Proba'), Js('Probina'), Js('Proseria'), Js('Prudentia'), Js('Pulcheria'), Js('Rhoda'), Js('Rhode'), Js('Rustica'), Js('Rusticana'), Js('Salvianella'), Js('Serena'), Js('Sergia'), Js('Sidonia'), Js('Silvia'), Js('Sophia'), Js('Sophie'), Js('Stephanous'), Js('Syagria'), Js('Synesia'), Js('Tetradia'), Js('Theocharista'), Js('Theodora'), Js('Theodoracis'), Js('Theodosia'), Js('Theognosia'), Js('Theophania'), Js('Theophilia'), Js('Theosebeia'), Js('Therosia'), Js('Valeria'), Js('Valeriana'), Js('Veneranda'), Js('Verina'), Js('Vesta'), Js('Victorina'), Js('Vigilantia'), Js('Vigilia'), Js('Vincentia'), Js('Vitula'), Js('Viviana'), Js('Xanthippe'), Js('Zena'), Js('Zoë')]))
    var.put('nm3', Js([Js('Acominatus'), Js('Acropolita'), Js('Akropolites'), Js('Angelus'), Js('Attaliates'), Js('Bardanes'), Js('Bardas'), Js('Botaniates'), Js('Caerularius'), Js('Cantacuzene'), Js('Chalcocondyles'), Js('Comnenus'), Js('Constantinus'), Js('Diogenus'), Js('Ducas'), Js('Glycas'), Js('Gregoras'), Js('Ingerinus'), Js('Kerularios'), Js('Kurkuas'), Js('Lascaris'), Js('Lecapenas'), Js('Lucaenus'), Js('Macrembolitissus'), Js('Maniakes'), Js('Melodus'), Js('Ooryphas'), Js('Palaeologus'), Js('Palamas'), Js('Philoponus'), Js('Phocus'), Js('Phrantzes'), Js('Sphrantzes'), Js('Planudes'), Js('Prodromus'), Js('Psellus'), Js('Ptochoprodromus'), Js('Rhangabe'), Js('Rhagabe'), Js('Staurakius'), Js('Stauricius'), Js('Stratioticus'), Js('Vatatzes'), Js('Ypsilanti'), Js('Zimisces'), Js('Tzimiskes'), Js('Zonaras')]))
    var.put('nm4', Js([Js('Acominata'), Js('Acropolite'), Js('Angela'), Js('Attaliate'), Js('Bardane'), Js('Barda'), Js('Botaniate'), Js('Caerularia'), Js('Cantacuzene'), Js('Chalcocondyle'), Js('Comnena'), Js('Constantina'), Js('Diogene'), Js('Duca'), Js('Glyca'), Js('Gregora'), Js('Ingerina'), Js('Kerularia'), Js('Kurkua'), Js('Lascari'), Js('Lecapena'), Js('Lucapena'), Js('Macrembolitissa'), Js('Maniake'), Js('Meloda'), Js('Oorypha'), Js('Palaeologa'), Js('Palama'), Js('Philopona'), Js('Phoca'), Js('Phrantze'), Js('Sphrantze'), Js('Planuda'), Js('Prodroma'), Js('Psella'), Js('Ptochoprodroma'), Js('Rhangabe'), Js('Staurakia'), Js('Stratiotica'), Js('Vatatze'), Js('Ypsilantis'), Js('Zimisce'), Js('Tzimiske'), Js('Zonara')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm4').callprop('splice', var.get('rnd2'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
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
byzantineNames = var.to_python()