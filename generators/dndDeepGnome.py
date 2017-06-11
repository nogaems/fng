__all__ = ['dndDeepGnome']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nameFem', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nameMas', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameFem_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
    if (var.get('i')<Js(5.0)):
        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
        if ((var.get('rnd')<Js(5.0)) and (var.get('rnd5')<Js(7.0))):
            while (var.get('rnd5')<Js(7.0)):
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
        while (PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm12').get(var.get('rnd5')))):
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
        var.put('nMs', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5'))))
    else:
        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
        while (PyJsStrictEq(var.get('nm10').get(var.get('rnd5')),var.get('nm8').get(var.get('rnd3'))) or PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd')))):
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
        var.put('nMs', (((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd6'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameFem_.func_name = 'nameFem'
var.put('nameFem', PyJsHoisted_nameFem_)
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
    while (PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd5')))):
        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
    var.put('nMs', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
    var.get('testSwear')(var.get('nMs'))
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
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
            var.put('nSr', (var.get('nm13').get(var.get('rnd'))+var.get('nm14').get(var.get('rnd2'))))
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
var.put('nm1', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('fr'), Js('g'), Js('gh'), Js('gr'), Js('k'), Js('kh'), Js('kr'), Js('sch'), Js('schn'), Js('sn'), Js('sh'), Js('t'), Js('th'), Js('w'), Js('z'), Js('zh')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ie'), Js('ee'), Js('ai'), Js('aa'), Js('ei')]))
var.put('nm3', Js([Js('ck'), Js('ckt'), Js('ckh'), Js('cn'), Js('dg'), Js('dl'), Js('ddl'), Js('dm'), Js('g'), Js('gg'), Js('gn'), Js('gl'), Js('ggl'), Js('kt'), Js('kth'), Js('kl'), Js('kn'), Js('lsch'), Js('lw'), Js('lth'), Js('lk'), Js('lkr'), Js('ltr'), Js('ll'), Js('ld'), Js('ldr'), Js('nth'), Js('nt'), Js('nd'), Js('ndr'), Js('ntr'), Js('rbl'), Js('rthm'), Js('rt'), Js('rdr'), Js('t'), Js('tt'), Js('tl'), Js('ttl'), Js('tr'), Js('thr'), Js('th')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('u')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('ck'), Js('d'), Js('g'), Js('l'), Js('ll'), Js('ld'), Js('n'), Js('nd'), Js('nk'), Js('r'), Js('rs'), Js('t')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('fr'), Js('gh'), Js('gr'), Js('h'), Js('k'), Js('kh'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('sn'), Js('sch'), Js('schn'), Js('t'), Js('th'), Js('y'), Js('w'), Js('z')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('u')]))
var.put('nm8', Js([Js('ckn'), Js('d'), Js('dl'), Js('dd'), Js('g'), Js('gg'), Js('gd'), Js('gn'), Js('gh'), Js('l'), Js('ll'), Js('lg'), Js('lm'), Js('lv'), Js('ls'), Js('lsch'), Js('lsh'), Js('m'), Js('mk'), Js('mg'), Js('n'), Js('nn'), Js('nt'), Js('ny'), Js('ng'), Js('nk'), Js('rb'), Js('rg'), Js('rl'), Js('rsh'), Js('rv'), Js('rt'), Js('rth'), Js('rs'), Js('s'), Js('ss'), Js('sh'), Js('sn'), Js('sk'), Js('sg'), Js('sl'), Js('th'), Js('t'), Js('tr'), Js('thr'), Js('v'), Js('vr'), Js('vy'), Js('z')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('ee'), Js('ie'), Js('ei'), Js('ai'), Js('ia')]))
var.put('nm10', Js([Js('d'), Js('dd'), Js('l'), Js('ll'), Js('ld'), Js('ln'), Js('lk'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('ry'), Js('rt'), Js('sh'), Js('sch')]))
var.put('nm11', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('i'), Js('a'), Js('i')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('dd'), Js('h'), Js('l'), Js('ll'), Js('n'), Js('nn'), Js('s'), Js('ss')]))
var.put('nm13', Js([Js('adamant'), Js('agate'), Js('alabaster'), Js('alloy'), Js('amethyst'), Js('basalt'), Js('bedrock'), Js('block'), Js('boulder'), Js('brass'), Js('brick'), Js('bronze'), Js('clay'), Js('cobalt'), Js('cobble'), Js('copper'), Js('crag'), Js('crystal'), Js('deposit'), Js('diamond'), Js('dirt'), Js('dust'), Js('emerald'), Js('flint'), Js('fossil'), Js('garnet'), Js('gem'), Js('geo'), Js('geode'), Js('gold'), Js('granite'), Js('gravel'), Js('grime'), Js('ground'), Js('ingot'), Js('iron'), Js('jade'), Js('jewel'), Js('joint'), Js('lapis'), Js('lazuli'), Js('lead'), Js('lime'), Js('lodge'), Js('lump'), Js('marble'), Js('mason'), Js('metal'), Js('mill'), Js('mineral'), Js('mold'), Js('nickel'), Js('nugget'), Js('obsidian'), Js('onyx'), Js('opal'), Js('ore'), Js('pebble'), Js('pellet'), Js('peridot'), Js('pit'), Js('quartz'), Js('rock'), Js('rough'), Js('rubble'), Js('ruby'), Js('sand'), Js('sapphire'), Js('scrap'), Js('seam'), Js('shelf'), Js('silver'), Js('slab'), Js('slate'), Js('smelt'), Js('soil'), Js('spinel'), Js('steel'), Js('stone'), Js('stony'), Js('sturdy'), Js('terra'), Js('tile'), Js('tin'), Js('topaz'), Js('turf'), Js('wedge'), Js('wire'), Js('zinc'), Js('zircon')]))
var.put('nm14', Js([Js('back'), Js('basher'), Js('bender'), Js('biter'), Js('bleacher'), Js('bone'), Js('bones'), Js('brander'), Js('breaker'), Js('bringer'), Js('browser'), Js('brusher'), Js('carrier'), Js('carver'), Js('catcher'), Js('checker'), Js('cheek'), Js('chest'), Js('chewer'), Js('chin'), Js('chiseler'), Js('cleaner'), Js('cleanser'), Js('collector'), Js('counter'), Js('crusher'), Js('cutter'), Js('designer'), Js('digger'), Js('duster'), Js('ear'), Js('eye'), Js('eyes'), Js('face'), Js('feet'), Js('finder'), Js('finger'), Js('fingers'), Js('fist'), Js('foot'), Js('forger'), Js('gatherer'), Js('gazer'), Js('getter'), Js('grasper'), Js('grinder'), Js('hand'), Js('head'), Js('heart'), Js('hewer'), Js('holder'), Js('knuckle'), Js('leg'), Js('legs'), Js('lifter'), Js('loader'), Js('maker'), Js('marker'), Js('mask'), Js('melter'), Js('mender'), Js('merger'), Js('molder'), Js('moulder'), Js('mug'), Js('neck'), Js('nose'), Js('packer'), Js('presser'), Js('pusher'), Js('rater'), Js('recorder'), Js('rinser'), Js('saver'), Js('scanner'), Js('scratcher'), Js('sealer'), Js('searcher'), Js('seeker'), Js('seizer'), Js('senser'), Js('shaper'), Js('shoveler'), Js('skin'), Js('smasher'), Js('smelter'), Js('snatcher'), Js('sniffer'), Js('sorter'), Js('splitter'), Js('stamper'), Js('stasher'), Js('stocker'), Js('surveyor'), Js('sweeper'), Js('switcher'), Js('teeth'), Js('temperer'), Js('tooth'), Js('trader'), Js('twirler'), Js('twister'), Js('vein'), Js('viewer'), Js('warper'), Js('watcher')]))
pass
pass
pass
pass


# Add lib to the module scope
dndDeepGnome = var.to_python()