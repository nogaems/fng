__all__ = ['nobleNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names8', 'names2', 'names3', 'names1', 'names7'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', (var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
                    var.put('names', (var.get('names7').get(var.get('rnd'))+var.get('names8').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    if (var.get('rnd2')>Js(4.0)):
                        while (var.get('rnd4')>Js(4.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('names', ((((var.get('names3').get(var.get('rnd'))+var.get('names4').get(var.get('rnd2')))+var.get('names5').get(var.get('rnd3')))+var.get('names4').get(var.get('rnd4')))+var.get('names6').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Ander'), Js('Arm'), Js('Arn'), Js('Bal'), Js('Batten'), Js('Beau'), Js('Beres'), Js('Black'), Js('Blan'), Js('Boat'), Js('Bott'), Js('Bran'), Js('Brew'), Js('Bridge'), Js('Brow'), Js('Buck'), Js('Cal'), Js('Camp'), Js('Car'), Js('Caul'), Js('Chal'), Js('Chap'), Js('Clay'), Js('Cole'), Js('Con'), Js('Cope'), Js('Coul'), Js('Coving'), Js('Craw'), Js('Cunning'), Js('Daven'), Js('Daw'), Js('Dris'), Js('Du'), Js('Ed'), Js('Eger'), Js('Est'), Js('Fair'), Js('Farn'), Js('Fiel'), Js('Fore'), Js('Fox'), Js('Frank'), Js('Free'), Js('Fuller'), Js('Gallo'), Js('Gardi'), Js('Garret'), Js('Glad'), Js('Gold'), Js('Good'), Js('Gran'), Js('Greg'), Js('Gren'), Js('Ham'), Js('Hamil'), Js('Har'), Js('Harring'), Js('Hart'), Js('Hen'), Js('Hol'), Js('Hop'), Js('How'), Js('Hub'), Js('Hum'), Js('Hutch'), Js('Jen'), Js('Ken'), Js('Knap'), Js('Lam'), Js('Lamb'), Js('Lan'), Js('Law'), Js('Le'), Js('Lind'), Js('Living'), Js('Mac'), Js('Man'), Js('Marsh'), Js('Mau'), Js('Max'), Js('May'), Js('Mea'), Js('Mer'), Js('Mon'), Js('Mont'), Js('Mor'), Js('More'), Js('Moris'), Js('Mul'), Js('Mur'), Js('Nel'), Js('Nichol'), Js('Nick'), Js('Nor'), Js('O'), Js('Os'), Js('Pad'), Js('Paken'), Js('Pal'), Js('Par'), Js('Part'), Js('Patter'), Js('Pau'), Js('Pear'), Js('Penning'), Js('Pet'), Js('Peter'), Js('Pett'), Js('Pick'), Js('Pit'), Js('Pitt'), Js('Port'), Js('Put'), Js('Rain'), Js('Ram'), Js('Ran'), Js('Rem'), Js('Rober'), Js('Robin'), Js('Rosen'), Js('Rot'), Js('Roths'), Js('Rott'), Js('Rut'), Js('Ruther'), Js('Rux'), Js('San'), Js('Saun'), Js('Saw'), Js('Sey'), Js('Shan'), Js('Shear'), Js('Shep'), Js('Shur'), Js('Sin'), Js('Skel'), Js('Skin'), Js('Small'), Js('Solo'), Js('Spen'), Js('Stan'), Js('Ste'), Js('Stone'), Js('Strat'), Js('Sul'), Js('Swee'), Js('Tal'), Js('Tay'), Js('Tho'), Js('Thorn'), Js('Tom'), Js('Town'), Js('Under'), Js('Valen'), Js('Wai'), Js('Wal'), Js('War'), Js('Wat'), Js('Wea'), Js('Web'), Js('Wer'), Js('Whit'), Js('Wil'), Js('Win'), Js('Woo'), Js('Wood'), Js('Wyn'), Js('Yeat')]))
var.put('names2', Js([Js('bard'), Js('barry'), Js('barth'), Js('bell'), Js('bert'), Js('borne'), Js('bot'), Js('bow'), Js('brand'), Js('brandt'), Js('brick'), Js('brook'), Js('burg'), Js('burn'), Js('card'), Js('caster'), Js('cher'), Js('child'), Js('clair'), Js('coll'), Js('comb'), Js('cox'), Js('cus'), Js('dal'), Js('dall'), Js('daway'), Js('del'), Js('dell'), Js('der'), Js('ders'), Js('ding'), Js('don'), Js('dows'), Js('drey'), Js('dwell'), Js('dwin'), Js('fax'), Js('field'), Js('ford'), Js('fort'), Js('gan'), Js('ger'), Js('gett'), Js('gomery'), Js('gor'), Js('hall'), Js('ham'), Js('herd'), Js('hold'), Js('hope'), Js('ker'), Js('kett'), Js('kins'), Js('lace'), Js('land'), Js('ledge'), Js('leigh'), Js('ler'), Js('less'), Js('lins'), Js('lor'), Js('lyn'), Js('maker'), Js('man'), Js('mann'), Js('mar'), Js('mas'), Js('mer'), Js('mers'), Js('mert'), Js('mier'), Js('mon'), Js('mond'), Js('mont'), Js('mour'), Js('nard'), Js('nedy'), Js('nell'), Js('nelly'), Js('ner'), Js('ney'), Js('ning'), Js('nings'), Js('non'), Js('nor'), Js('pard'), Js('perd'), Js('phens'), Js('phrey'), Js('port'), Js('rance'), Js('rant'), Js('rence'), Js('rene'), Js('rett'), Js('rice'), Js('ridge'), Js('rish'), Js('rough'), Js('row'), Js('ryett'), Js('say'), Js('sen'), Js('send'), Js('sey'), Js('sley'), Js('smith'), Js('son'), Js('ster'), Js('ston'), Js('stone'), Js('strong'), Js('sworth'), Js('ter'), Js('tero'), Js('ters'), Js('thall'), Js('tine'), Js('ton'), Js('van'), Js('ver'), Js('ville'), Js('vine'), Js('ward'), Js('wards'), Js('way'), Js('well'), Js('wen'), Js('wens'), Js('win'), Js('wood'), Js('yer')]))
var.put('names3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z'), Js('br'), Js('dr'), Js('fr'), Js('gr'), Js('pr'), Js('tr'), Js('st'), Js('fl'), Js('gl'), Js('bl'), Js('pl'), Js('ph'), Js('sh'), Js('sl'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('oo'), Js('ee'), Js('ea'), Js('ou'), Js('ai')]))
var.put('names5', Js([Js('bb'), Js('cc'), Js('dd'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('rr'), Js('ss'), Js('pp'), Js('bs'), Js('ck'), Js('ckl'), Js('dg'), Js('dk'), Js('dl'), Js('ds'), Js('dw'), Js('gl'), Js('lb'), Js('lbr'), Js('ld'), Js('ldw'), Js('lf'), Js('lm'), Js('lst'), Js('lt'), Js('lw'), Js('mb'), Js('mps'), Js('nc'), Js('nch'), Js('nd'), Js('ndr'), Js('ns'), Js('nsl'), Js('nt'), Js('nth'), Js('ntl'), Js('rb'), Js('rdn'), Js('rg'), Js('rk'), Js('rl'), Js('rn'), Js('rns'), Js('rp'), Js('rt'), Js('rv'), Js('sh'), Js('st'), Js('stm'), Js('tch'), Js('tl'), Js('tm'), Js('vs'), Js('wd'), Js('wf'), Js('wl'), Js('wn'), Js('wst'), Js('yd'), Js('yt')]))
var.put('names6', Js([Js('ch'), Js('gg'), Js('ggs'), Js('gs'), Js('k'), Js('l'), Js('ld'), Js('ll'), Js('m'), Js('mb'), Js('n'), Js('ng'), Js('ngs'), Js('ns'), Js('p'), Js('ph'), Js('r'), Js('rd'), Js('rn'), Js('rs'), Js('s'), Js('sh'), Js('ss'), Js('t'), Js('tt'), Js('w'), Js('wl'), Js('ws'), Js('y'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names7', Js([Js('Amber'), Js('Apple'), Js('Arm'), Js('August'), Js('Autumn'), Js('Bar'), Js('Bell'), Js('Black'), Js('Boat'), Js('Bow'), Js('Brew'), Js('Bride'), Js('Bridge'), Js('Bronze'), Js('Brown'), Js('Buck'), Js('Camp'), Js('Can'), Js('Chamber'), Js('Chap'), Js('Clay'), Js('Cliff'), Js('Cob'), Js('Cole'), Js('Coll'), Js('Copper'), Js('Cotton'), Js('Coving'), Js('Craw'), Js('Crow'), Js('Cunning'), Js('Dark'), Js('Daven'), Js('Daw'), Js('Down'), Js('Dye'), Js('Eagle'), Js('East'), Js('Feather'), Js('Fish'), Js('Fletch'), Js('Fore'), Js('Fox'), Js('Free'), Js('Fuller'), Js('Gallo'), Js('Gard'), Js('Gentle'), Js('Gil'), Js('Gill'), Js('God'), Js('Gold'), Js('Good'), Js('Grand'), Js('Green'), Js('Grim'), Js('Gross'), Js('Hart'), Js('Hawk'), Js('Hollo'), Js('Hunting'), Js('Kil'), Js('Knight'), Js('Law'), Js('Living'), Js('Loch'), Js('Lock'), Js('Love'), Js('Marsh'), Js('Merry'), Js('Mill'), Js('Moon'), Js('More'), Js('Moss'), Js('New'), Js('Night'), Js('North'), Js('Rain'), Js('Raven'), Js('Rich'), Js('Robin'), Js('Roth'), Js('Rott'), Js('Sea'), Js('Silver'), Js('Small'), Js('Solo'), Js('South'), Js('Spring'), Js('Stone'), Js('Summer'), Js('Sweet'), Js('Timber'), Js('Town'), Js('Under'), Js('Web'), Js('West'), Js('Whit'), Js('Winter'), Js('Wood')]))
var.put('names8', Js([Js('bard'), Js('beard'), Js('borne'), Js('bow'), Js('breed'), Js('bride'), Js('burn'), Js('colt'), Js('comb'), Js('dall'), Js('end'), Js('field'), Js('ford'), Js('gard'), Js('guard'), Js('hall'), Js('ham'), Js('head'), Js('hill'), Js('kind'), Js('land'), Js('ledge'), Js('less'), Js('ling'), Js('low'), Js('maker'), Js('man'), Js('mann'), Js('mere'), Js('mond'), Js('more'), Js('mour'), Js('port'), Js('rich'), Js('riddle'), Js('ridge'), Js('send'), Js('smith'), Js('son'), Js('star'), Js('stein'), Js('ster'), Js('strong'), Js('tomb'), Js('ton'), Js('tree'), Js('ward'), Js('water'), Js('way'), Js('well'), Js('win'), Js('wood')]))
pass
pass


# Add lib to the module scope
nobleNames = var.to_python()