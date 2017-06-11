__all__ = ['dndDrowNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nmMFf', 'nmFRl', 'nmS', 'nmSFf', 'nameFem', 'nameGen', 'nmFFf', 'nmFFl', 'nmSRf', 'nmMRl', 'nmF', 'nmMRf', 'nmSFl', 'nmMFl', 'nmFRf', 'nmSRl', 'nameSur', 'nameMas', 'nmM'])
@Js
def PyJsHoisted_nameSur_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    if (var.get('i')<Js(4.0)):
        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmSRf').get('length'))))
        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmSRl').get('length'))))
        var.put('nSr', (var.get('nmSRf').get(var.get('rnd3'))+var.get('nmSRl').get(var.get('rnd4'))))
        var.get('testSwear')(var.get('nSr'))
    else:
        if (var.get('i')<Js(8.0)):
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmSFf').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmSFl').get('length'))))
            var.put('nSr', (var.get('nmSFf').get(var.get('rnd3'))+var.get('nmSFl').get(var.get('rnd4'))))
            var.get('testSwear')(var.get('nSr'))
        else:
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmS').get('length'))))
            var.put('nSr', var.get('nmS').get(var.get('rnd3')))
PyJsHoisted_nameSur_.func_name = 'nameSur'
var.put('nameSur', PyJsHoisted_nameSur_)
@Js
def PyJsHoisted_nameFem_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    if (var.get('i')<Js(4.0)):
        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmFRf').get('length'))))
        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmFRl').get('length'))))
        var.put('nMs', (var.get('nmFRf').get(var.get('rnd'))+var.get('nmFRl').get(var.get('rnd2'))))
        var.get('testSwear')(var.get('nMs'))
    else:
        if (var.get('i')<Js(8.0)):
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmFFf').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmFFl').get('length'))))
            var.put('nMs', (var.get('nmFFf').get(var.get('rnd'))+var.get('nmFFl').get(var.get('rnd2'))))
            var.get('testSwear')(var.get('nMs'))
        else:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmF').get('length'))))
            var.put('nMs', var.get('nmF').get(var.get('rnd')))
PyJsHoisted_nameFem_.func_name = 'nameFem'
var.put('nameFem', PyJsHoisted_nameFem_)
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    if (var.get('i')<Js(4.0)):
        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmMRf').get('length'))))
        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmMRl').get('length'))))
        var.put('nMs', (var.get('nmMRf').get(var.get('rnd'))+var.get('nmMRl').get(var.get('rnd2'))))
        var.get('testSwear')(var.get('nMs'))
    else:
        if (var.get('i')<Js(8.0)):
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmMFf').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmMFl').get('length'))))
            var.put('nMs', (var.get('nmMFf').get(var.get('rnd'))+var.get('nmMFl').get(var.get('rnd2'))))
            var.get('testSwear')(var.get('nMs'))
        else:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmM').get('length'))))
            var.put('nMs', var.get('nmM').get(var.get('rnd')))
PyJsHoisted_nameMas_.func_name = 'nameMas'
var.put('nameMas', PyJsHoisted_nameMas_)
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
            var.get('nameSur')()
            while PyJsStrictEq(var.get('nSr'),Js('')):
                var.get('nameSur')()
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.get('nameFem')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameFem')()
            else:
                var.get('nameMas')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameMas')()
            var.put('nMs', ((var.get('nMs')+Js(' '))+var.get('nSr')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nmF', Js([Js('Ahlysaaria'), Js('Akordia'), Js('Alaunirra'), Js('Alystin'), Js('Amalica'), Js('Angaste'), Js('Anluryn'), Js('Ardulace'), Js('Aunrae'), Js('Balaena'), Js('Baltana'), Js('Bautha'), Js('Belarbreena'), Js('Beszrima'), Js('Brigantyna'), Js('Briza'), Js('Brorna'), Js('Burryna'), Js('Byrtyn'), Js('Cazna'), Js('Chadra'), Js('Chadzina'), Js('Chalithra'), Js('Chandara'), Js('Chardalyn'), Js('Charinida'), Js('Charlindra'), Js('Chenzira'), Js('Chessintra'), Js('Dhaunae'), Js('Dilynrae'), Js('Drada'), Js('Drisinil'), Js('Eclavdra'), Js('Elerra'), Js('Elvanshalee'), Js('Elvraema'), Js('Erakasyne'), Js('Ereldra'), Js('Faeryl'), Js('Felyndiira'), Js('Felyndiira'), Js('Filfaere'), Js("G'eldriia"), Js('Gaussra'), Js('Ghilanna'), Js('Greyanna'), Js('Gurina'), Js('Haelra'), Js('Halisstra'), Js('Ilharess'), Js('Ilivarrra'), Js('Ilmra'), Js('Imrae'), Js('Jaelryn'), Js('Jezzara'), Js('Jhaelryna'), Js('Jhaelrynna'), Js('Jhalass'), Js('Jhangara'), Js('Jhanniss'), Js('Jhulae'), Js('Khaless'), Js('Kiaran'), Js('Laele'), Js('Laele'), Js('Larynda'), Js('LiNeerlay'), Js('Lledrith'), Js('Llolfaen'), Js('Lualyrr'), Js('Lythrana'), Js('Malice'), Js('Maya'), Js('Menzoberra'), Js("Mez'Barris"), Js('Micarlin'), Js("Miz'ri"), Js('Mizzrym'), Js('Myrymma'), Js('Narcelia'), Js('Nathrae'), Js('Nedylene'), Js('Nendra'), Js('Nizana'), Js('Nulliira'), Js('Olorae'), Js('Pellanistra'), Js('Phaere'), Js('Phyrra'), Js('Qilue'), Js('Quarra'), Js('Rauva'), Js('Rilrae'), Js('Sabrae'), Js('Saradreza'), Js('Sassandra'), Js('Schezalle'), Js('Shimyra'), Js('ShriNeerune'), Js('Shulvallriel'), Js('Shurdriira'), Js('Shurdriira'), Js('Shurraenil'), Js('Shyntlara'), Js('SiNafay'), Js('Sindyrrith'), Js('Solenzara'), Js('Ssapriina'), Js("T'risstree"), Js('Talabrina'), Js('Talice'), Js('Tallrene'), Js('Thalra'), Js('Thirza'), Js('Thraele'), Js('Triel'), Js('Ulitree'), Js('Ulviirala'), Js('Umrae'), Js('Urlryn'), Js('Urmelena'), Js('Vhondryl'), Js('Viconia'), Js('Vierna'), Js('Vornalla'), Js('Waerva'), Js('Wuyondra'), Js('Xalyth'), Js('Xullrae'), Js('Xune'), Js('Yasrena'), Js('Yvonnel'), Js("Z'ress"), Js('Zarra'), Js('Zebeyana'), Js('Zeerith'), Js('Zelpassa'), Js('Zendalure'), Js('Zesstra'), Js('Zilvra')]))
var.put('nmFRf', Js([Js('Akor'), Js('Alaun'), Js('Aly'), Js('Ang'), Js('Ardul'), Js('Aun'), Js('Bae'), Js('Bal'), Js('Belar'), Js('Briz'), Js('Bur'), Js('Chal'), Js('Char'), Js('Chess'), Js('Dhaun'), Js('Dil'), Js('Dirz'), Js('Dris'), Js('Eclav'), Js('Elvan'), Js('Elv'), Js('Erel'), Js('Ethe'), Js('Faer'), Js('Felyn'), Js('Filf'), Js('Gauss'), Js("G'eld"), Js('Ghuan'), Js('Gin'), Js('Grey'), Js('Hael'), Js('Hal'), Js('Houn'), Js('Iiv'), Js('Iim'), Js('Illiam'), Js('In'), Js('Ilph'), Js('Irae'), Js('In'), Js('Iym'), Js('Jan'), Js('Jhael'), Js('Jhul'), Js('Jys'), Js('Lael'), Js('Lar'), Js('LiNeer'), Js('Lird'), Js('Lua'), Js('Mal'), Js('May'), Js('Micar'), Js('Min'), Js('Mol'), Js('Myr'), Js('Nath'), Js('Ned'), Js('Nhil'), Js('Neer'), Js('Null'), Js('Olor'), Js('Pellan'), Js('Phaer'), Js('Phyr'), Js('Qualn'), Js('Quar'), Js('Quav'), Js('Qil'), Js('Rauv'), Js('Ril'), Js('Sbat'), Js('Sab'), Js("Shi'n"), Js('Shri'), Js('Shur'), Js('Shynt'), Js('Sin'), Js('Ssap'), Js('Susp'), Js('Talab'), Js('Tal'), Js('Triel'), Js("T'riss"), Js('Ulvir'), Js('Umrae'), Js('Vas'), Js('Vic'), Js('Vier'), Js('Vlon'), Js('Waer'), Js('Wuyon'), Js('Xull'), Js('Xun'), Js('Yas'), Js('Zar'), Js('Zebey'), Js('Zes'), Js('Zilv')]))
var.put('nmFRl', Js([Js('a'), Js('ace'), Js('ae'), Js('aer'), Js('afae'), Js('afay'), Js('ala'), Js('anna'), Js('arra'), Js('aste'), Js('avin'), Js('ayne'), Js('baste'), Js('breena'), Js('bryn'), Js('cice'), Js('cyrl'), Js('da'), Js('dia'), Js('diira'), Js('dra'), Js('driira'), Js('dril'), Js('e'), Js('eari'), Js('eyl'), Js('ffyn'), Js('fryn'), Js('iara'), Js('ice'), Js('idil'), Js('iira'), Js('inidia'), Js('inil'), Js('intra'), Js('isstra'), Js('ithra'), Js('jra'), Js('jss'), Js('kacha'), Js('kiira'), Js('lay'), Js('lara'), Js('lin'), Js('lochar'), Js('mice'), Js("mur'ss"), Js('na'), Js('nilee'), Js('niss'), Js('nitra'), Js('nolu'), Js('olin'), Js('onia'), Js('oyss'), Js('qualyn'), Js('quarra'), Js('quiri'), Js('ra'), Js('rae'), Js('raema'), Js('raena'), Js('riia'), Js('ril'), Js('riina'), Js('ryna'), Js('ryne'), Js('shalee'), Js('ssysn'), Js('stin'), Js('stra'), Js('tana'), Js('thara'), Js('thrae'), Js('tree'), Js('tyrr'), Js('ual'), Js('ue'), Js('uit'), Js('une'), Js('uque'), Js('urra'), Js('va'), Js('vayas'), Js('vyll'), Js('vyrae'), Js('wae'), Js('wiira'), Js('wyss'), Js('xae'), Js('xena'), Js('xyra'), Js('yl'), Js('ylene'), Js('ymma'), Js('ynda'), Js('ynrae'), Js('vrae'), Js('yrr'), Js('zyne')]))
var.put('nmFFf', Js([Js('Ahly'), Js('Akor'), Js('Alau'), Js('Aly'), Js('Ama'), Js('Anga'), Js('Anlu'), Js('Ardu'), Js('Aun'), Js('Ba'), Js('Bal'), Js('Bau'), Js('Belar'), Js('Bes'), Js('Bri'), Js('Brigan'), Js('Bror'), Js('Bur'), Js('Byr'), Js('Caz'), Js('Cha'), Js('Chad'), Js('Chali'), Js('Chan'), Js('Char'), Js('Chari'), Js('Chen'), Js('Ches'), Js('Dhau'), Js('Dilyn'), Js('Dra'), Js('Dri'), Js('Eclav'), Js('Eler'), Js('Elv'), Js('Elvan'), Js('Era'), Js('Erel'), Js('Fae'), Js('Felyn'), Js('Fil'), Js("G'el"), Js('Gaus'), Js('Ghi'), Js('Gre'), Js('Gu'), Js('Hael'), Js('Halis'), Js('Ilha'), Js('Ilivar'), Js('Ilm'), Js('Im'), Js('Jael'), Js('Jez'), Js('Jha'), Js('Jhael'), Js('Jhan'), Js('Jhu'), Js('Kha'), Js('Kia'), Js('La'), Js('Lae'), Js('Lle'), Js('Llol'), Js('Lua'), Js('Ly'), Js('Ma'), Js('Menzo'), Js("Mez'Bar"), Js('Micar'), Js('Miz'), Js("Miz'"), Js('Myrym'), Js('Na'), Js('Narce'), Js('Nedy'), Js('Nen'), Js('Ni'), Js('Nul'), Js('Olo'), Js('Pella'), Js('Phae'), Js('Phyr'), Js('Qi'), Js('Quar'), Js('Rau'), Js('Ril'), Js('Sab'), Js('Sara'), Js('Sas'), Js('Sche'), Js('Shi'), Js('Shulvall'), Js('Shur'), Js('Shyn'), Js('Sindyr'), Js('Solen'), Js('Ssap'), Js("T'ris"), Js('Ta'), Js('Tala'), Js('Tall'), Js('Thal'), Js('Thir'), Js('Thrae'), Js('Uli'), Js('Ulvii'), Js('Um'), Js('Url'), Js('Urme'), Js('Vhon'), Js('Vico'), Js('Vier'), Js('Vor'), Js('Waer'), Js('Wuyon'), Js('Xa'), Js('Xu'), Js('Xull'), Js('Yas'), Js('Yvon'), Js("Z'res"), Js('Zar'), Js('Zebe'), Js('Zee'), Js('Zel'), Js('Zenda'), Js('Zes'), Js('Zil')]))
var.put('nmFFl', Js([Js('berra'), Js('breena'), Js('brina'), Js('da'), Js('dalyn'), Js('dara'), Js('dia'), Js('diira'), Js('dra'), Js('dreza'), Js('driia'), Js('driira'), Js('drith'), Js('dryl'), Js('faen'), Js('faere'), Js('gara'), Js('ka'), Js('lace'), Js('lae'), Js('laena'), Js('lanna'), Js('lass'), Js('le'), Js('lena'), Js('lene'), Js('less'), Js('lia'), Js('lica'), Js('lice'), Js('liira'), Js('lin'), Js('lindra'), Js('lue'), Js('lure'), Js('lyrr'), Js('lyth'), Js('ma'), Js('myra'), Js('na'), Js('nae'), Js('nalla'), Js('ne'), Js('nel'), Js('nia'), Js('nida'), Js('nirra'), Js('niss'), Js('nistra'), Js('passa'), Js('ra'), Js('rae'), Js('raema'), Js('raenil'), Js('rala'), Js('ran'), Js('re'), Js('rena'), Js('rene'), Js('ress'), Js('ri'), Js('riel'), Js('riina'), Js('rina'), Js('ris'), Js('rith'), Js('ryl'), Js('ryn'), Js('ryna'), Js('rynda'), Js('rynna'), Js('saaria'), Js('sandra'), Js('shalee'), Js('sinil'), Js('sintra'), Js('sra'), Js('ste'), Js('stin'), Js('stra'), Js('stree'), Js('syne'), Js('tana'), Js('tha'), Js('thra'), Js('thrae'), Js('thrana'), Js('tlara'), Js('tree'), Js('tyn'), Js('tyna'), Js('va'), Js('vra'), Js('ya'), Js('yana'), Js('yanna'), Js('za'), Js('zalle'), Js('zana'), Js('zara'), Js('zina'), Js('zira'), Js('zrima'), Js('zrym')]))
var.put('nmM', Js([Js('Alton'), Js('Balok'), Js('Baragh'), Js('Belaern'), Js('Belgos'), Js('Bemril'), Js("Berg'inyon"), Js('Bhintel'), Js('Brorn'), Js('Bruherd'), Js('Caelkoth'), Js('Callimar'), Js('Chakos'), Js('Chaszmyr'), Js('Coranzen'), Js('Dantrag'), Js('Dhuunyl'), Js('Dinin'), Js('Dresmorlin'), Js('Dro'), Js('Duagloth'), Js('Durdyn'), Js('Elamshin'), Js('Elendar'), Js('Elkantar'), Js('Filraen'), Js('Ghaundan'), Js('Ghaundar'), Js('Guldor'), Js('Guldor'), Js('Gwylyss'), Js('Hadrogh'), Js("Hatch'net"), Js('Honemmeth'), Js('Houndaer'), Js('Ildan'), Js('Ilmryn'), Js('Ilphrin'), Js('Imbros'), Js('Irennan'), Js('Istolil'), Js('Istorvir'), Js('Iymril'), Js('Jaezred'), Js('Jalynfein'), Js('Jeggred'), Js('Jevan'), Js('Jhaamdath'), Js('Jhaldrym'), Js('Jivvin'), Js('Jyslin'), Js("K'yorl"), Js('Kalannar'), Js('Kethan'), Js('Kluthruel'), Js('Kophyn'), Js('Krenaste'), Js('Krondorl'), Js('Kyorlin'), Js('Lesaonar'), Js('Lirdnolu'), Js('Llaulmyn'), Js('Malaggar'), Js('Micarlin'), Js('Minolin'), Js('Molvayas'), Js('Morennel'), Js('Nadal'), Js('Nalfein'), Js('Narissorin'), Js('Narlros'), Js('Nilonim'), Js('Nimruil'), Js("Numrini'th"), Js('Nyloth'), Js('Nym'), Js('Omareth'), Js('Orgoloth'), Js('Ornaryn'), Js('Pharaun'), Js('Pharius'), Js('Quave'), Js('Quendar'), Js('Quenthel'), Js('Quevven'), Js('Ranaghar'), Js('Relonor'), Js('Riklaunim'), Js('Rinnill'), Js('Ristel'), Js('Ruathym'), Js('Ryld'), Js('Ryltar'), Js('Sabal'), Js('Selakiir'), Js('Seldszar'), Js('Seldszar'), Js('Sengo'), Js('Solaufein'), Js('Sorn'), Js('Syrdar'), Js('Szordrin'), Js('Szordrin'), Js('Taldinyon'), Js('Tarlyn'), Js('Tathlyn'), Js('Tazennin'), Js('Tebryn'), Js('Tolokoph'), Js('Torrellan'), Js('Trelgath'), Js('Tsabrak'), Js('Urlryn'), Js('Valas'), Js('Veldrin'), Js('Velkyn'), Js('Vhurdaer'), Js('Vhurindrar'), Js('Vielyn'), Js('Vlondril'), Js('Vorn'), Js('Vuzlyn'), Js('Welverin'), Js('Xarann'), Js('Xundus'), Js('Yazston'), Js('Yuimmar'), Js('Zaknafein'), Js('Zeerith'), Js('Zyn')]))
var.put('nmMRf', Js([Js('Adin'), Js('Alak'), Js('Alton'), Js('Amal'), Js('Ant'), Js('Bar'), Js('Bel'), Js('Berg'), Js('Bhin'), Js('Bruh'), Js('Cal'), Js('Chasz'), Js('Din'), Js('Dip'), Js('Div'), Js('Driz'), Js('Duag'), Js('Dur'), Js('Elaug'), Js('Elk'), Js('Erth'), Js('Fil'), Js('Gel'), Js('Go'), Js('Gul'), Js('Hatch'), Js('Hurz'), Js('Ilzt'), Js('Im'), Js('Ist'), Js('Izz'), Js('Jar'), Js('Kalan'), Js('Kel'), Js('Kren'), Js('Kron'), Js('Les'), Js('Llt'), Js('Lyme'), Js('Malag'), Js('Mas'), Js('Mer'), Js('Mourn'), Js('Nad'), Js('Nal'), Js('Nil'), Js('Nym'), Js('Omar'), Js('Orgoll'), Js('Phar'), Js('Phyx'), Js('Quev'), Js('Quil'), Js('Ran'), Js('Relon'), Js('Rhyl'), Js('Rik'), Js('Riz'), Js('Ryl'), Js('Ryld'), Js('Selds'), Js('Shar'), Js('Sol'), Js('Sorn'), Js('Spir'), Js('Ssz'), Js('Szin'), Js('Szor'), Js('Tar'), Js('Tath'), Js('Taz'), Js('Teb'), Js('Tluth'), Js('Tsab'), Js('Uhls'), Js('Url'), Js('Val'), Js('Vesz'), Js('Vorn'), Js('Vuz'), Js('Wehl'), Js('Welv'), Js('Wod'), Js('Wruz'), Js('Yaz'), Js('Zakn'), Js('Zek'), Js('Zsz')]))
var.put('nmMRl', Js([Js('afein'), Js('agh'), Js('aghar'), Js('al'), Js('antar'), Js('aonar'), Js('as'), Js('atar'), Js('atlab'), Js('aufein'), Js('aun'), Js('axle'), Js('d'), Js('daer'), Js('dan'), Js('dar'), Js('dax'), Js('diin'), Js('diirn'), Js('dor'), Js('dorl'), Js('driirn'), Js('drin'), Js('dyn'), Js('erd'), Js('erin'), Js('eth'), Js('fein'), Js('gloth'), Js('gos'), Js('hrae'), Js('hriir'), Js('hrys'), Js('ica'), Js('imar'), Js('in'), Js('inid'), Js('inyon'), Js('irahc'), Js('kah'), Js('launim'), Js('lyn'), Js('myr'), Js('nar'), Js('net'), Js('nozz'), Js('oj'), Js('olg'), Js('olil'), Js('olvir'), Js('omph'), Js('onim'), Js('or'), Js('orvir'), Js('oyn'), Js('raen'), Js('rak'), Js('ral'), Js('rar'), Js('ree'), Js('roos'), Js('ryn'), Js('rysn'), Js('tar'), Js('tel'), Js('ton'), Js('tran'), Js('trin'), Js('ven'), Js('vyr'), Js('yln'), Js('yraen'), Js('yrd'), Js('zaer'), Js('zar'), Js('zen'), Js('zt'), Js('zyr')]))
var.put('nmMFf', Js([Js('Al'), Js('Ba'), Js('Be'), Js('Bel'), Js('Bem'), Js("Berg'"), Js('Bhin'), Js('Bru'), Js('Cael'), Js('Cal'), Js('Cha'), Js('Chas'), Js('Coran'), Js('Dan'), Js('Dhuu'), Js('Di'), Js('Dres'), Js('Dro'), Js('Duag'), Js('Dur'), Js('El'), Js('Elam'), Js('Elen'), Js('Fil'), Js('Ghaun'), Js('Gul'), Js('Gwy'), Js('Had'), Js("Hatch'"), Js('Honem'), Js('Houn'), Js('Il'), Js('Ilm'), Js('Im'), Js('Iren'), Js('Isto'), Js('Istor'), Js('Iym'), Js('Jaez'), Js('Jalyn'), Js('Je'), Js('Jeg'), Js('Jhaam'), Js('Jhal'), Js('Jiv'), Js('Jys'), Js("K'yo"), Js('Kalan'), Js('Ke'), Js('Kluth'), Js('Ko'), Js('Kre'), Js('Kron'), Js('Kyor'), Js('Lesao'), Js('Lird'), Js('Llaul'), Js('Malag'), Js('Micar'), Js('Mino'), Js('Mol'), Js('Moren'), Js('Na'), Js('Nal'), Js('Naris'), Js('Narl'), Js('Nilo'), Js('Nim'), Js('Num'), Js('Ny'), Js('Nym'), Js('Oma'), Js('Orgo'), Js('Orna'), Js('Pha'), Js('Qua'), Js('Quen'), Js('Quev'), Js('Rana'), Js('Relo'), Js('Riklau'), Js('Rin'), Js('Ris'), Js('Rua'), Js('Ryl'), Js('Ryld'), Js('Sa'), Js('Sela'), Js('Seld'), Js('Sen'), Js('Solau'), Js('Syr'), Js('Szor'), Js('Tal'), Js('Tar'), Js('Tath'), Js('Tazen'), Js('Teb'), Js('Tolo'), Js('Torrel'), Js('Trel'), Js('Tsab'), Js('Url'), Js('Va'), Js('Vel'), Js('Vhu'), Js('Vhur'), Js('Vie'), Js('Vlon'), Js('Vuz'), Js('Wel'), Js('Xa'), Js('Xun'), Js('Yaz'), Js('Yuim'), Js('Zakna'), Js('Zee')]))
var.put('nmMFl', Js([Js('bal'), Js('bros'), Js('daer'), Js('dal'), Js('dan'), Js('dar'), Js('dath'), Js('dinyon'), Js('dor'), Js('dorl'), Js('drar'), Js('dril'), Js('drin'), Js('drym'), Js('dus'), Js('dyn'), Js('fein'), Js('gar'), Js('gath'), Js('ghar'), Js('go'), Js('gos'), Js('gred'), Js('herd'), Js('inyon'), Js('kantar'), Js('kiir'), Js('koph'), Js('kos'), Js('koth'), Js('kyn'), Js('laern'), Js('lan'), Js('las'), Js('lil'), Js('limar'), Js('lin'), Js('lok'), Js('loth'), Js('lyn'), Js('lyss'), Js('mar'), Js('meth'), Js('morlin'), Js('myn'), Js('nan'), Js('nar'), Js('naste'), Js('nel'), Js('net'), Js('nill'), Js('nim'), Js('nin'), Js('nolu'), Js('nor'), Js('nyl'), Js('phrin'), Js('phyn'), Js('raen'), Js('ragh'), Js('rak'), Js('rann'), Js('raun'), Js('red'), Js('reth'), Js('ril'), Js('rin'), Js("rini'th"), Js('rith'), Js('rius'), Js('rogh'), Js('ros'), Js('ruel'), Js('ruil'), Js('ryn'), Js('shin'), Js('sorin'), Js('ston'), Js('szar'), Js('tar'), Js('tel'), Js('than'), Js('thel'), Js('thym'), Js('ton'), Js('trag'), Js('van'), Js('vayas'), Js('ve'), Js('ven'), Js('verin'), Js('vin'), Js('vir'), Js('zen'), Js('zmyr')]))
var.put('nmS', Js([Js("A'Daragon"), Js('Abaeir'), Js('Abbylan'), Js('Argith'), Js('Baenre'), Js('Beltaulur'), Js('Blaerabban'), Js('Blundyth'), Js('Chaulssin'), Js('Coborel'), Js('Coloara'), Js('Cormrael'), Js("Daevion'lyr"), Js('Dalael'), Js('Dhalmass'), Js('Dhunnyl'), Js('Diliriy'), Js('Dinoryn'), Js('Dryaalis'), Js('Duskryn'), Js('Dyrr'), Js('Elpragh'), Js('Elpragh'), Js('Faertala'), Js('Filifar'), Js('Gallaer'), Js('Glannath'), Js('Glaurach'), Js('Helviiryn'), Js('Hune'), Js('Hunzrin'), Js('Hyluan'), Js('Icharyd'), Js('Ilaleztice'), Js('Illistyn'), Js('Illykur'), Js('Jhalavar'), Js('Jusztiirn'), Js('Keteeruae'), Js('Khalazza'), Js('Khalazza'), Js("Kront'tane"), Js('Lhalabar'), Js('Lueltar'), Js('Mizzrym'), Js('Mlezziir'), Js('Naerth'), Js('Nirinath'), Js('Olonrae'), Js('Omriwin'), Js('Philiom'), Js('Quavein'), Js('Rhomduil'), Js('Rrostarr'), Js('Seerear'), Js('Ssambra'), Js("T'orgh"), Js("T'sarran"), Js("Tanor'Thal"), Js('Telenna'), Js("Tlin'orzza"), Js('Tlintarn'), Js('Tuin'), Js('Uloavae'), Js('Vrammyr'), Js('Vrinn'), Js('Waeglossz'), Js('Xiltyn'), Js('Yauntyrr'), Js('Yauthlo'), Js("Yril'Lysaen"), Js('Zaphresz'), Js('Zauviir'), Js('Zolond')]))
var.put('nmSRf', Js([Js('Alean'), Js('Ale'), Js('Arab'), Js('Arken'), Js('Auvry'), Js('Baen'), Js('Barri'), Js('Cladd'), Js('Desp'), Js('De'), Js("Do'"), Js('Eils'), Js('Everh'), Js('Fre'), Js('Gode'), Js('Helvi'), Js('Hla'), Js("Hun'"), Js('Ken'), Js('Kil'), Js('Mae'), Js('Mel'), Js('My'), Js('Noqu'), Js('Orly'), Js('Ouss'), Js('Rilyn'), Js("Teken'"), Js('Tor'), Js('Zau')]))
var.put('nmSRl', Js([Js('afin'), Js('ana'), Js('ani'), Js('ar'), Js('arn'), Js('ate'), Js('ath'), Js('duis'), Js('ervs'), Js('ep'), Js('ett'), Js('ghym'), Js('iryn'), Js('lyl'), Js('mtor'), Js('ndar'), Js('neld'), Js('rae'), Js('rahel'), Js('rret'), Js('sek'), Js('th'), Js('tlar'), Js("t'tar"), Js('tyl'), Js('und'), Js('urden'), Js('val'), Js('viir'), Js('zynge')]))
var.put('nmSFf', Js([Js("A'Dar"), Js('Ab'), Js('Abb'), Js('Arg'), Js('Baenre'), Js('Belt'), Js('Blaer'), Js('Blund'), Js('Chaulss'), Js('Cob'), Js('Col'), Js('Cormr'), Js('D'), Js('Daev'), Js('Dal'), Js('Dhalm'), Js('Dhunn'), Js('Dil'), Js('Din'), Js('Dryaal'), Js('Duskr'), Js('Elpr'), Js('Faert'), Js('Fil'), Js('Gall'), Js('Glann'), Js('Glaur'), Js('H'), Js('Helv'), Js('Hunzr'), Js('Hyl'), Js('Ich'), Js('Ilal'), Js('Ill'), Js('Jhal'), Js('Juszt'), Js('Keteer'), Js('Khal'), Js("Kront't"), Js('Lhal'), Js('Luelt'), Js('Mizzr'), Js('Mlezz'), Js('N'), Js('Nir'), Js('Ol'), Js('Omr'), Js('Phil'), Js('Quav'), Js('Rhomd'), Js('Rrost'), Js('Seer'), Js('Ss'), Js('T'), Js("T'"), Js("T's"), Js("Tanor'Th"), Js('Tel'), Js("Tlin'"), Js('Tlint'), Js('Ul'), Js('Vr'), Js('Vramm'), Js('Waegl'), Js('Xilt'), Js('Yaunt'), Js("Yril'Lys"), Js('Zaphr'), Js('Zauv'), Js('Zol')]))
var.put('nmSFl', Js([Js('abar'), Js('abban'), Js('ach'), Js('aeir'), Js('ael'), Js('aen'), Js('aer'), Js('aerth'), Js('agh'), Js('agon'), Js('al'), Js('ala'), Js('ambra'), Js('ane'), Js('ar'), Js('arn'), Js('arr'), Js('arran'), Js('aryd'), Js('ass'), Js('ath'), Js('aulur'), Js('avar'), Js('azza'), Js('ear'), Js('ein'), Js('enna'), Js('esz'), Js('eztice'), Js('ifar'), Js('iir'), Js('iirn'), Js('iiryn'), Js('in'), Js('inath'), Js('inn'), Js('iom'), Js("ion'lyr"), Js('iriy'), Js('is'), Js('istyn'), Js('ith'), Js('iwin'), Js('oara'), Js('oavae'), Js('ond'), Js('onrae'), Js('orel'), Js('orgh'), Js('oryn'), Js('orzza'), Js('ossz'), Js('uae'), Js('uan'), Js('uil'), Js('uin'), Js('une'), Js('ykur'), Js('yl'), Js('ylan'), Js('ym'), Js('yn'), Js('yr'), Js('yrr'), Js('yth')]))
pass
pass
pass
pass
pass


# Add lib to the module scope
dndDrowNames = var.to_python()