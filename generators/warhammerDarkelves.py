__all__ = ['warhammerDarkelves']

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
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameL')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameL')))
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
var.put('nm1', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('t'), Js('v')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ou'), Js('au')]))
var.put('nm3', Js([Js('c'), Js('cc'), Js('cr'), Js('ch'), Js('g'), Js('gh'), Js('gr'), Js('gn'), Js('k'), Js('kh'), Js('kr'), Js('kk'), Js('kz'), Js('l'), Js('ll'), Js('lk'), Js('lc'), Js('lg'), Js('n'), Js('nn'), Js('nk'), Js('r'), Js('rv'), Js('rk'), Js('rc'), Js('rg'), Js('rz'), Js('rl'), Js('tr'), Js('th'), Js('vr'), Js('v'), Js('c'), Js('g'), Js('k'), Js('l'), Js('n'), Js('r'), Js('v'), Js('c'), Js('g'), Js('k'), Js('l'), Js('n'), Js('r'), Js('v'), Js('c'), Js('g'), Js('k'), Js('l'), Js('n'), Js('r'), Js('v')]))
var.put('nm4', Js([Js('c'), Js('k'), Js('l'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th')]))
var.put('nm5', Js([Js('c'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('th'), Js('v')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o')]))
var.put('nm7', Js([Js('b'), Js('bh'), Js('c'), Js('ch'), Js('gh'), Js('gg'), Js('h'), Js('hh'), Js('kh'), Js('l'), Js('ll'), Js('lr'), Js('ln'), Js('lv'), Js('r'), Js('rr'), Js('rt'), Js('rl'), Js('rs'), Js('rn'), Js('rv'), Js('s'), Js('ss'), Js('sh'), Js('t'), Js('tt'), Js('th'), Js('v'), Js('vh'), Js('b'), Js('c'), Js('h'), Js('l'), Js('r'), Js('s'), Js('t'), Js('v'), Js('kh'), Js('b'), Js('c'), Js('h'), Js('l'), Js('r'), Js('s'), Js('t'), Js('v'), Js('kh')]))
var.put('nm8', Js([Js('h'), Js('n'), Js('l'), Js('sh'), Js('s'), Js('th'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm9', Js([Js('amber'), Js('ash'), Js('battle'), Js('blood'), Js('cinder'), Js('dark'), Js('dawn'), Js('dead'), Js('death'), Js('doom'), Js('dread'), Js('dusk'), Js('dust'), Js('ember'), Js('fall'), Js('fallen'), Js('fell'), Js('fire'), Js('flame'), Js('gloom'), Js('grim'), Js('haze'), Js('hell'), Js('nether'), Js('night'), Js('pyre'), Js('rage'), Js('rain'), Js('shade'), Js('shadow'), Js('silent'), Js('skull'), Js('steel'), Js('storm'), Js('thunder'), Js('void'), Js('war'), Js('wild')]))
var.put('nm10', Js([Js('arm'), Js('arrow'), Js('axe'), Js('bane'), Js('basher'), Js('binder'), Js('blade'), Js('blaze'), Js('bleeder'), Js('blight'), Js('breaker'), Js('bringer'), Js('caller'), Js('cleaver'), Js('crusher'), Js('cutter'), Js('eye'), Js('eyes'), Js('fall'), Js('fury'), Js('grip'), Js('hand'), Js('heart'), Js('hunter'), Js('mantle'), Js('maul'), Js('might'), Js('more'), Js('reaper'), Js('reaver'), Js('rider'), Js('ripper'), Js('runner'), Js('scar'), Js('seeker'), Js('shade'), Js('shadow'), Js('shard'), Js('slayer'), Js('sorrow'), Js('stalker'), Js('stride'), Js('strike'), Js('striker'), Js('surge'), Js('taker')]))
pass
pass


# Add lib to the module scope
warhammerDarkelves = var.to_python()