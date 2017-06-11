__all__ = ['northAmericanTowns']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(12.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
                else:
                    if (var.get('i')<Js(9.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', (var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('names', (var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Al'), Js('Ala'), Js('Alber'), Js('Am'), Js('Anti'), Js('Ar'), Js('Arbor'), Js('Arn'), Js('As'), Js('Atha'), Js('Ati'), Js('Avon'), Js('Bal'), Js('Ban'), Js('Bark'), Js('Barr'), Js('Bas'), Js('Battle'), Js('Bay'), Js('Beacon'), Js('Beau'), Js('Beaver'), Js('Bed'), Js('Bell'), Js('Belle'), Js('Ben'), Js('Bent'), Js('Ber'), Js('Beres'), Js('Berthier'), Js('Bien'), Js('Big'), Js('Bir'), Js('Black'), Js('Blain'), Js('Bois'), Js('Bona'), Js('Bord'), Js('Boucher'), Js('Brace'), Js('Breden'), Js('Bri'), Js('Bridge'), Js('Brigh'), Js('Bro'), Js('Broad'), Js('Bros'), Js('Brown'), Js('Bruder'), Js('Buch'), Js('Bur'), Js('Burs'), Js('Cal'), Js('Cale'), Js('Camp'), Js('Can'), Js('Cano'), Js('Car'), Js('Cara'), Js('Carbo'), Js('Card'), Js('Carig'), Js('Carle'), Js('Carn'), Js('Cart'), Js('Cas'), Js('Cau'), Js('Causa'), Js('Cha'), Js('Cham'), Js('Chan'), Js('Chi'), Js('Chibou'), Js('Church'), Js('Clare'), Js('Claren'), Js('Cler'), Js('Co'), Js('Coal'), Js('Coati'), Js('Coch'), Js('Col'), Js('Coli'), Js('Com'), Js('Con'), Js('Cor'), Js('Corn'), Js('Coro'), Js('Cottle'), Js('Cowan'), Js('Cres'), Js('Cross'), Js('Cud'), Js('Dal'), Js('Dan'), Js('Davel'), Js('Day'), Js('Del'), Js('Delis'), Js('Delor'), Js('Dig'), Js('Dis'), Js('Do'), Js('Dol'), Js('Donna'), Js('Dor'), Js('Dray'), Js('Drum'), Js('Dun'), Js('Dupar'), Js('East'), Js('Eato'), Js('Eck'), Js('El'), Js('Ellis'), Js('Em'), Js('Emer'), Js('Engle'), Js('Ester'), Js('Fair'), Js('Fal'), Js('Farn'), Js('Fer'), Js('Flat'), Js('Flem'), Js('For'), Js('Fran'), Js('Gal'), Js('Gallan'), Js('Gam'), Js('Gan'), Js('Gana'), Js('Gar'), Js('Gati'), Js('Gaul'), Js('Gib'), Js('Gil'), Js('Glad'), Js('Glen'), Js('Glover'), Js('Go'), Js('Gode'), Js('Gol'), Js('Grace'), Js('Gran'), Js('Grand'), Js('Gravel'), Js('Graven'), Js('Green'), Js('Gren'), Js('Gret'), Js('Grim'), Js('Hal'), Js('Ham'), Js('Hamp'), Js('Han'), Js('Har'), Js('Hart'), Js('Hep'), Js('Hermi'), Js('Hf'), Js('Hin'), Js('Holy'), Js('Hud'), Js('Hum'), Js('Hunt'), Js('Inger'), Js('Innis'), Js('Iro'), Js('Irri'), Js('Itu'), Js('Jol'), Js('Kam'), Js('Kapus'), Js('Kear'), Js('Keel'), Js('Kerro'), Js('Kinder'), Js('Kings'), Js('Kini'), Js('Kip'), Js('Kirk'), Js('La'), Js('Lam'), Js('Lama'), Js('Lang'), Js('Lani'), Js('Lash'), Js('Latch'), Js('Laval'), Js('Le'), Js('Lea'), Js('Lem'), Js('Lin'), Js('Locke'), Js('Lour'), Js('Lum'), Js('Lunen'), Js('Luse'), Js('Maca'), Js('Mag'), Js('Maho'), Js('Malar'), Js('Man'), Js('Mani'), Js('Mara'), Js('Mata'), Js('Meli'), Js('Mid'), Js('Mida'), Js('Middle'), Js('Mil'), Js('Mill'), Js('Miller'), Js('Mini'), Js('Minne'), Js('Mont'), Js('Moo'), Js('Morin'), Js('Mul'), Js('Mun'), Js('Mus'), Js('Nai'), Js('Nan'), Js('Nee'), Js('Neu'), Js('Nia'), Js('Nico'), Js('Nipa'), Js('Niver'), Js('Noko'), Js('Nor'), Js('Oak'), Js('Oge'), Js('Oko'), Js('Ono'), Js('Oro'), Js('Oso'), Js('Otter'), Js('Out'), Js('Ox'), Js('Pac'), Js('Par'), Js('Para'), Js('Parr'), Js('Pas'), Js('Pel'), Js('Pen'), Js('Pene'), Js('Peta'), Js('Petro'), Js('Pic'), Js('Pil'), Js('Pin'), Js('Pla'), Js('Plym'), Js('Pohe'), Js('Pon'), Js('Pono'), Js('Port'), Js('Pres'), Js('Pro'), Js('Ra'), Js('Rad'), Js('Ray'), Js('Reid'), Js('Repen'), Js('Rim'), Js('Rimou'), Js('River'), Js('Rob'), Js('Ros'), Js('Rose'), Js('Ross'), Js('Rothe'), Js('Sag'), Js('Sal'), Js('San'), Js('Sau'), Js('Sava'), Js('Sedge'), Js('Senne'), Js('Shau'), Js('Shaw'), Js('She'), Js('Shel'), Js('Shell'), Js('Sher'), Js('Ship'), Js('Sin'), Js('Smi'), Js('Spring'), Js('Stan'), Js('Stel'), Js('Stet'), Js('Stone'), Js('Stough'), Js('Strat'), Js('Summer'), Js('Sun'), Js('Tecum'), Js('Temis'), Js('Ter'), Js('Terre'), Js('Terren'), Js('Thes'), Js('Thessa'), Js('Thet'), Js('Thur'), Js('Till'), Js('Tray'), Js('Tre'), Js('Tren'), Js('Tri'), Js('Tro'), Js('Tur'), Js('Twil'), Js('Val'), Js('Varen'), Js('Vaux'), Js('Vegre'), Js('Ver'), Js('Vir'), Js('Von'), Js('Vot'), Js('Wa'), Js('Wade'), Js('Waka'), Js('Wal'), Js('Wape'), Js('War'), Js('Wasa'), Js('Whit'), Js('White'), Js('Wil'), Js('Wind'), Js('Winter'), Js('Wit'), Js('Wolf'), Js('Wood'), Js('Wyn'), Js('Yar')]))
var.put('nm2', Js([Js('balt'), Js('bel'), Js('berg'), Js('berry'), Js('biens'), Js('bo'), Js('boia'), Js('bonear'), Js('borg'), Js('bour'), Js('bourg'), Js('briand'), Js('bridge'), Js('burg'), Js('burns'), Js('bury'), Js('by'), Js('cam'), Js('cana'), Js('carres'), Js('chill'), Js('cier'), Js('cola'), Js('coln'), Js('cona'), Js('cook'), Js('couche'), Js('cour'), Js('croft'), Js('dale'), Js('dare'), Js('deen'), Js('den'), Js('der'), Js('des'), Js('diac'), Js('don'), Js('dosa'), Js('dows'), Js('duff'), Js('durn'), Js('fail'), Js('fait'), Js('fell'), Js('field'), Js('fil'), Js('ford'), Js('forte'), Js('gamau'), Js('gami'), Js('gan'), Js('gar'), Js('geo'), Js('gonie'), Js('gough'), Js('grave'), Js('guay'), Js('gue'), Js('gueuil'), Js('gus'), Js('ham'), Js('hazy'), Js('head'), Js('heim'), Js('heller'), Js('her'), Js('holm'), Js('hurst'), Js('jour'), Js('kasing'), Js('lam'), Js('lams'), Js('lan'), Js('land'), Js('lants'), Js('leche'), Js('let'), Js('ley'), Js('liers'), Js('lin'), Js('line'), Js('linet'), Js('ling'), Js('lis'), Js('lisle'), Js('lita'), Js('lodge'), Js('mack'), Js('magne'), Js('man'), Js('mar'), Js('meda'), Js('meny'), Js('mer'), Js('mere'), Js('meuse'), Js('ming'), Js('miota'), Js('mis'), Js('mont'), Js('more'), Js('na'), Js('nach'), Js('nan'), Js('near'), Js('neau'), Js('ney'), Js('nia'), Js('nigan'), Js('ning'), Js('nola'), Js('noque'), Js('nora'), Js('par'), Js('pawa'), Js('pids'), Js('pond'), Js('port'), Js('quet'), Js('raine'), Js('ram'), Js('rane'), Js('rath'), Js('ree'), Js('rial'), Js('rich'), Js('rior'), Js('ris'), Js('rock'), Js('ronto'), Js('rood'), Js('rose'), Js('roy'), Js('sack'), Js('sano'), Js('sard'), Js('say'), Js('sby'), Js('sevain'), Js('shall'), Js('shaw'), Js('side'), Js('soll'), Js('somin'), Js('son'), Js('sonee'), Js('sons'), Js('stall'), Js('stead'), Js('stino'), Js('ston'), Js('stone'), Js('tague'), Js('tane'), Js('tara'), Js('tawa'), Js('terel'), Js('terre'), Js('thon'), Js('to'), Js('tois'), Js('ton'), Js('tona'), Js('tonas'), Js('tos'), Js('tou'), Js('town'), Js('trie'), Js('val'), Js('ver'), Js('view'), Js('ville'), Js('vista'), Js('vons'), Js('waki'), Js('wall'), Js('wick'), Js('win'), Js('wood'), Js('worth')]))
var.put('nm3', Js([Js('Aappi'), Js('Aappilat'), Js('Aas'), Js('Akun'), Js('Alluit'), Js('Ammas'), Js('Ar'), Js('Atam'), Js('Eqalu'), Js('Eqalugaar'), Js('Havig'), Js('Hiura'), Js('Hiurapa'), Js('Igali'), Js('Iginniar'), Js('Ika'), Js('Ikera'), Js('Ili'), Js('Ilima'), Js('Illor'), Js('Ilu'), Js('Ilulis'), Js('Iser'), Js('Itil'), Js('Itto'), Js('Ittoqqor'), Js('Kangaa'), Js('Kangaat'), Js('Kanger'), Js('Kangersuat'), Js('Kangi'), Js('Kangilinn'), Js('Kapi'), Js('Kapisil'), Js('Kitsi'), Js('Kitsisuar'), Js('Kullor'), Js('Kulu'), Js('Kuum'), Js('Manii'), Js('Maniit'), Js('Naa'), Js('Nanor'), Js('Napa'), Js('Nar'), Js('Narsar'), Js('Nia'), Js('Niaqor'), Js('Nutaar'), Js('Nuugaat'), Js('Nuus'), Js('Oqaat'), Js('Paa'), Js('Qa'), Js('Qaa'), Js('Qaar'), Js('Qaqor'), Js('Qasi'), Js('Qasigian'), Js('Qasigiann'), Js('Qassi'), Js('Qassiar'), Js('Qeqer'), Js('Qeqertar'), Js('Saar'), Js('Saat'), Js('Saq'), Js('Sar'), Js('Sarfann'), Js('Savi'), Js('Savissi'), Js('Si'), Js('Sio'), Js('Siora'), Js('Siorapa'), Js('Sisi'), Js('Tasii'), Js('Tasiu'), Js('Uper'), Js('Uperna'), Js('Uumma'), Js('Uumman')]))
var.put('nm4', Js([Js('dal'), Js('fik'), Js('gaamiut'), Js('gaarsuit'), Js('guit'), Js('hivik'), Js('jaat'), Js('laq'), Js('lattoq'), Js('leq'), Js('lik'), Js('liku'), Js('linnguit'), Js('loq'), Js('luitsup'), Js('luk'), Js('lussuaq'), Js('manaq'), Js('mannaq'), Js('miit'), Js('mijit'), Js('mik'), Js('miut'), Js('naaq'), Js('naarsuk'), Js('naq'), Js('navik'), Js('nes'), Js('niarfik'), Js('paluk'), Js('palul'), Js('qaq'), Js('qornat'), Js('qortoq'), Js('rapaluk'), Js('rasak'), Js('saarsuk'), Js('sak'), Js('saq'), Js('sat'), Js('siaat'), Js('siaq'), Js('siarsuk'), Js('sillit'), Js('simiut'), Js('sivik'), Js('soq'), Js('suaq'), Js('suarsuit'), Js('suatsiaat'), Js('suatsiaq'), Js('suit'), Js('suk'), Js('sup'), Js('sut'), Js('talik'), Js('taq'), Js('tat'), Js('thal'), Js('toormiit'), Js('toq'), Js('tu'), Js('tut'), Js('vik')]))
var.put('nm5', Js([Js('Aca'), Js('Acam'), Js('Agua'), Js('Allen'), Js('Almo'), Js('Alta'), Js('Amo'), Js('Apat'), Js('Apo'), Js('Ati'), Js('Atiza'), Js('Atli'), Js('Beni'), Js('Buena'), Js('Ca'), Js('Caje'), Js('Cam'), Js('Can'), Js('Car'), Js('Cauh'), Js('Cela'), Js('Cen'), Js('Chal'), Js('Che'), Js('Chetu'), Js('Chi'), Js('Chico'), Js('Chil'), Js('Chila'), Js('Chilpan'), Js('Chimal'), Js('Co'), Js('Coa'), Js('Coatza'), Js('Coli'), Js('Comal'), Js('Comi'), Js('Cordo'), Js('Corre'), Js('Coso'), Js('Cosolea'), Js('Cuauh'), Js('Cuautit'), Js('Cuer'), Js('Cuerna'), Js('Culia'), Js('Cun'), Js('Cundua'), Js('Deli'), Js('Dolo'), Js('Du'), Js('Dura'), Js('Eca'), Js('Ecate'), Js('Ense'), Js('Fres'), Js('Gar'), Js('Gua'), Js('Guada'), Js('Guadala'), Js('Guana'), Js('Guasa'), Js('Guay'), Js('Hida'), Js('Hidal'), Js('Hue'), Js('Huehue'), Js('Hui'), Js('Huiman'), Js('Huix'), Js('Igua'), Js('Ira'), Js('Irapua'), Js('Ixta'), Js('Ixtapa'), Js('Ixtla'), Js('Jiu'), Js('Jiute'), Js('Jua'), Js('Ler'), Js('Macus'), Js('Made'), Js('Man'), Js('Manza'), Js('Mar'), Js('Mata'), Js('Maza'), Js('Meri'), Js('Mete'), Js('Mina'), Js('Mira'), Js('Mon'), Js('More'), Js('Naca'), Js('Nau'), Js('Naucal'), Js('Navo'), Js('Neza'), Js('Nezahual'), Js('Noga'), Js('Oaxa'), Js('Obre'), Js('Oco'), Js('Ori'), Js('Oriza'), Js('Pachu'), Js('Palen'), Js('Papan'), Js('Pen'), Js('Penja'), Js('Pue'), Js('Quere'), Js('Rey'), Js('Sal'), Js('Sala'), Js('Si'), Js('Sole'), Js('Soli'), Js('Tan'), Js('Tanto'), Js('Tapa'), Js('Teca'), Js('Teco'), Js('Tehua'), Js('Tema'), Js('Temix'), Js('Tepa'), Js('Tepex'), Js('Tex'), Js('Ti'), Js('Tijua'), Js('Tkaque'), Js('Tolu'), Js('Tona'), Js('Tor'), Js('Tul'), Js('Tulan'), Js('Urua'), Js('Vera'), Js('Villa'), Js('Xala'), Js('Zaca'), Js('Zamo'), Js('Zapo'), Js('Zihua'), Js('Zina'), Js('Zita'), Js('Zum')]))
var.put('nm6', Js([Js('baro'), Js('calco'), Js('cali'), Js('calpan'), Js('camac'), Js('can'), Js('caque'), Js('cate'), Js('chuca'), Js('chula'), Js('cingo'), Js('clova'), Js('co'), Js('coalcos'), Js('coco'), Js('coman'), Js('coyotl'), Js('cruz'), Js('cuaro'), Js('cun'), Js('daca'), Js('dalgo'), Js('denas'), Js('doba'), Js('dora'), Js('duacan'), Js('gales'), Js('gidora'), Js('guillo'), Js('hua'), Js('huacan'), Js('huahua'), Js('jamo'), Js('jara'), Js('joa'), Js('juana'), Js('juato'), Js('juca'), Js('lajara'), Js('lao'), Js('lapa'), Js('lato'), Js('laya'), Js('lende'), Js('lia'), Js('licias'), Js('lientes'), Js('lima'), Js('loapan'), Js('lon'), Js('loya'), Js('lucan'), Js('lupe'), Js('mal'), Js('man'), Js('manca'), Js('mas'), Js('mira'), Js('mora'), Js('moros'), Js('mosa'), Js('nada'), Js('nala'), Js('nas'), Js('navaca'), Js('nillo'), Js('nito'), Js('nosa'), Js('pache'), Js('paluca'), Js('pan'), Js('pango'), Js('pantla'), Js('paque'), Js('peche'), Js('pico'), Js('popan'), Js('puato'), Js('pulco'), Js('ques'), Js('quilucan'), Js('ramar'), Js('range'), Js('reon'), Js('rida'), Js('ridad'), Js('save'), Js('sillo'), Js('singo'), Js('tanejo'), Js('taro'), Js('tecas'), Js('temoc'), Js('tepec'), Js('titlan'), Js('tla'), Js('toca'), Js('toyuca'), Js('tro'), Js('tumal'), Js('yuca'), Js('zanillo'), Js('zapan'), Js('zava'), Js('zingan'), Js('zoc')]))
var.put('nm7', Js([Js('Ab'), Js('Al'), Js('Aller'), Js('Ames'), Js('An'), Js('Apple'), Js('Arling'), Js('As'), Js('Ash'), Js('Attle'), Js('Autumn'), Js('Bain'), Js('Bal'), Js('Bar'), Js('Barn'), Js('Barring'), Js('Bax'), Js('Bed'), Js('Bedding'), Js('Ber'), Js('Berk'), Js('Bever'), Js('Bex'), Js('Birming'), Js('Bloom'), Js('Blooms'), Js('Blythe'), Js('Bol'), Js('Booth'), Js('Bos'), Js('Box'), Js('Brad'), Js('Brent'), Js('Bridge'), Js('Brigh'), Js('Bright'), Js('Brim'), Js('Bris'), Js('Brom'), Js('Brook'), Js('Bucking'), Js('Bux'), Js('Cam'), Js('Can'), Js('Canter'), Js('Carl'), Js('Chat'), Js('Chats'), Js('Chel'), Js('Chelms'), Js('Ches'), Js('Chester'), Js('Chil'), Js('Clif'), Js('Cliff'), Js('Clin'), Js('Coal'), Js('Col'), Js('Cole'), Js('Con'), Js('Corn'), Js('Coven'), Js('Croy'), Js('Cumber'), Js('Dan'), Js('Dar'), Js('Dart'), Js('De'), Js('Dead'), Js('Ded'), Js('Del'), Js('Der'), Js('Do'), Js('Dor'), Js('Dun'), Js('Dur'), Js('Effing'), Js('Elling'), Js('Elm'), Js('Ems'), Js('En'), Js('Ep'), Js('Es'), Js('Ever'), Js('Ex'), Js('Fair'), Js('Fal'), Js('Fall'), Js('Farm'), Js('Farming'), Js('Ford'), Js('Framing'), Js('Free'), Js('Glas'), Js('Glou'), Js('Graf'), Js('Gran'), Js('Grand'), Js('Grave'), Js('Green'), Js('Gro'), Js('Guil'), Js('Had'), Js('Hali'), Js('Ham'), Js('Hamp'), Js('Har'), Js('Harp'), Js('Hart'), Js('Has'), Js('Hast'), Js('Hat'), Js('Haver'), Js('Heb'), Js('Here'), Js('Hil'), Js('Hill'), Js('Hills'), Js('Hing'), Js('Hors'), Js('Hul'), Js('Hunt'), Js('Hunting'), Js('Isling'), Js('Kensing'), Js('Killing'), Js('Kings'), Js('Kir'), Js('Lan'), Js('Leaming'), Js('Lee'), Js('Lei'), Js('Leo'), Js('Liming'), Js('Litch'), Js('Liver'), Js('Lon'), Js('Maid'), Js('Mal'), Js('Man'), Js('Mans'), Js('Mar'), Js('Marl'), Js('May'), Js('Men'), Js('Mens'), Js('Meri'), Js('Middle'), Js('Middles'), Js('Mil'), Js('Mill'), Js('Monk'), Js('New'), Js('Newing'), Js('Nor'), Js('North'), Js('Not'), Js('Notting'), Js('Oak'), Js('Ox'), Js('Plai'), Js('Plain'), Js('Ply'), Js('Port'), Js('Ports'), Js('Pres'), Js('Put'), Js('Read'), Js('Rich'), Js('Ridge'), Js('Ring'), Js('River'), Js('Ro'), Js('Roch'), Js('Rock'), Js('Rocking'), Js('Rom'), Js('Row'), Js('Rox'), Js('Rug'), Js('Rut'), Js('Salis'), Js('San'), Js('Sand'), Js('Scar'), Js('Scars'), Js('Shef'), Js('Shrew'), Js('Shrews'), Js('Smith'), Js('Smiths'), Js('Somer'), Js('South'), Js('Spring'), Js('Staf'), Js('Stam'), Js('Stock'), Js('Stoke'), Js('Stone'), Js('Straf'), Js('Strat'), Js('Sud'), Js('Suf'), Js('Summer'), Js('Sunder'), Js('Sur'), Js('Sus'), Js('Sut'), Js('Tam'), Js('Taun'), Js('Temple'), Js('Tis'), Js('Tiver'), Js('Tol'), Js('Tor'), Js('Torring'), Js('Tun'), Js('Ven'), Js('Vent'), Js('Wake'), Js('Wal'), Js('Wall'), Js('Walling'), Js('Wals'), Js('War'), Js('Ware'), Js('Water'), Js('Way'), Js('Welling'), Js('Wes'), Js('West'), Js('Wey'), Js('Whit'), Js('White'), Js('Wick'), Js('Wil'), Js('Willing'), Js('Win'), Js('Wind'), Js('Winder'), Js('Winter'), Js('Wood'), Js('Wor'), Js('Wrent'), Js('Yar'), Js('York')]))
var.put('nm8', Js([Js('boro'), Js('borough'), Js('bridge'), Js('bron'), Js('brook'), Js('burn'), Js('bury'), Js('by'), Js('caster'), Js('castle'), Js('cester'), Js('chester'), Js('coln'), Js('cord'), Js('dale'), Js('de'), Js('den'), Js('ding'), Js('don'), Js('dover'), Js('down'), Js('dwell'), Js('fair'), Js('field'), Js('folk'), Js('ford'), Js('gate'), Js('ham'), Js('hampton'), Js('hampton'), Js('hill'), Js('hurst'), Js('isle'), Js('lem'), Js('ley'), Js('low'), Js('ly'), Js('mark'), Js('mere'), Js('minster'), Js('mond'), Js('more'), Js('mouth'), Js('net'), Js('ney'), Js('pon'), Js('pool'), Js('port'), Js('rey'), Js('riden'), Js('ry'), Js('sea'), Js('send'), Js('set'), Js('shire'), Js('son'), Js('sor'), Js('stable'), Js('stead'), Js('ster'), Js('stone'), Js('swell'), Js('ter'), Js('tham'), Js('ton'), Js('try'), Js('vern'), Js('ville'), Js('wall'), Js('ware'), Js('water'), Js('way'), Js('we'), Js('well'), Js('wich'), Js('wick'), Js('win'), Js('wood'), Js('worth')]))
pass
pass


# Add lib to the module scope
northAmericanTowns = var.to_python()