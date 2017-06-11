__all__ = ['warhammerDwarfs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            while PyJsStrictEq(var.get('nm9').get(var.get('rnd')),var.get('nm10').get(var.get('rnd2'))):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('nameL', (var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameL')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameL')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameL')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('br'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('kh'), Js('kr'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sr'), Js('str'), Js('th'), Js('tr'), Js('thr'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ai'), Js('oa'), Js('ao')]))
var.put('nm3', Js([Js('d'), Js('g'), Js('k'), Js('l'), Js('r'), Js('th'), Js('d'), Js('g'), Js('k'), Js('l'), Js('r'), Js('th'), Js('br'), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gr'), Js('gh'), Js('gn'), Js('gm'), Js('gz'), Js('gd'), Js('k'), Js('kr'), Js('l'), Js('lb'), Js('ld'), Js('lg'), Js('lgr'), Js('ldr'), Js('nd'), Js('ng'), Js('nr'), Js('ndr'), Js('ngr'), Js('r'), Js('rd'), Js('rdr'), Js('rg'), Js('rt'), Js('rbr'), Js('rb'), Js('rgr'), Js('th'), Js('tr'), Js('thr')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('gg'), Js('k'), Js('m'), Js('mm'), Js('n'), Js('r'), Js('rd'), Js('t')]))
var.put('nm5', Js([Js('b'), Js('bh'), Js('c'), Js('d'), Js('dr'), Js('g'), Js('gh'), Js('h'), Js('m'), Js('n'), Js('s'), Js('sk'), Js('sc'), Js('t'), Js('th'), Js('v'), Js('z'), Js('zh')]))
var.put('nm6', Js([Js('e'), Js('i'), Js('u'), Js('e'), Js('i'), Js('u'), Js('e'), Js('i'), Js('u'), Js('e'), Js('i'), Js('u'), Js('a'), Js('a'), Js('o'), Js('o')]))
var.put('nm7', Js([Js('br'), Js('dr'), Js('dg'), Js('dw'), Js('dd'), Js('ff'), Js('fr'), Js('gr'), Js('gw'), Js('gn'), Js('gm'), Js('gf'), Js('gv'), Js('kk'), Js('kh'), Js('kr'), Js('kv'), Js('lg'), Js('lgr'), Js('lv'), Js('ng'), Js('ngr'), Js('ngw'), Js('nd'), Js('ndw'), Js('ndr'), Js('rg'), Js('rgr'), Js('rgw'), Js('rw'), Js('rz'), Js('sg'), Js('sgr'), Js('sv'), Js('th'), Js('tr'), Js('tv'), Js('thr'), Js('vr')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('h'), Js('m'), Js('n'), Js('t')]))
var.put('nm9', Js([Js('amber'), Js('autumn'), Js('battle'), Js('bear'), Js('bitter'), Js('black'), Js('blunt'), Js('boulder'), Js('brane'), Js('bright'), Js('brittle'), Js('broad'), Js('broken'), Js('bronze'), Js('brown'), Js('cask'), Js('cinder'), Js('cliff'), Js('coal'), Js('cold'), Js('common'), Js('copper'), Js('crag'), Js('deep'), Js('distant'), Js('ember'), Js('far'), Js('fiery'), Js('fire'), Js('flame'), Js('flat'), Js('flint'), Js('forge'), Js('full'), Js('fuse'), Js('gold'), Js('golden'), Js('grand'), Js('granite'), Js('gray'), Js('great'), Js('grim'), Js('grudge'), Js('grumble'), Js('hammer'), Js('hill'), Js('ingot'), Js('iron'), Js('keen'), Js('keg'), Js('krag'), Js('lead'), Js('light'), Js('magma'), Js('merry'), Js('metal'), Js('mild'), Js('mirth'), Js('mithril'), Js('mountain'), Js('noble'), Js('onyx'), Js('plain'), Js('proud'), Js('regal'), Js('rich'), Js('rock'), Js('rough'), Js('rumble'), Js('shatter'), Js('silver'), Js('slender'), Js('solid'), Js('steel'), Js('stone'), Js('storm'), Js('stout'), Js('strong'), Js('thunder'), Js('true')]))
var.put('nm10', Js([Js('arm'), Js('armor'), Js('armour'), Js('axe'), Js('back'), Js('basher'), Js('beam'), Js('beard'), Js('bearer'), Js('belly'), Js('belt'), Js('bender'), Js('bluff'), Js('bone'), Js('bough'), Js('brace'), Js('branch'), Js('brand'), Js('breaker'), Js('brew'), Js('brewer'), Js('bringer'), Js('brow'), Js('buckle'), Js('buster'), Js('chaser'), Js('chest'), Js('chin'), Js('cloak'), Js('crag'), Js('crest'), Js('digger'), Js('dreamer'), Js('feet'), Js('finger'), Js('fire'), Js('fist'), Js('fists'), Js('flame'), Js('foot'), Js('force'), Js('forge'), Js('forged'), Js('fury'), Js('grip'), Js('grog'), Js('guard'), Js('gut'), Js('hammer'), Js('hand'), Js('hank'), Js('head'), Js('heart'), Js('helm'), Js('keeper'), Js('maker'), Js('mantle'), Js('mark'), Js('master'), Js('might'), Js('more'), Js('punch'), Js('rage'), Js('seeker'), Js('shaper'), Js('shield'), Js('shoulder'), Js('shout'), Js('strength'), Js('strider'), Js('striker'), Js('surge'), Js('sworn'), Js('thane'), Js('walker'), Js('ward')]))
pass
pass


# Add lib to the module scope
warhammerDwarfs = var.to_python()