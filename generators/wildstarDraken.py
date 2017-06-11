__all__ = ['wildstarDraken']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            while PyJsStrictEq(var.get('nm8').get(var.get('rnd6')),var.get('nm9').get(var.get('rnd7'))):
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('lname', (var.get('nm8').get(var.get('rnd6'))+var.get('nm9').get(var.get('rnd7'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(' '))+var.get('lname')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+Js(' '))+var.get('lname')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(7.0)):
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lname')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lname')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('ua'), Js('ia'), Js('uu')]))
var.put('nm3', Js([Js('c'), Js('cr'), Js('dr'), Js('g'), Js('gg'), Js('gr'), Js('gh'), Js('k'), Js('kr'), Js('kk'), Js('l'), Js('n'), Js('nk'), Js('ng'), Js('q'), Js('r'), Js('rr'), Js('rk'), Js('rg'), Js('rq'), Js('v'), Js('vr'), Js('vh'), Js('z'), Js('zg'), Js('c'), Js('g'), Js('k'), Js('l'), Js('n'), Js('q'), Js('r'), Js('v'), Js('z'), Js('c'), Js('g'), Js('k'), Js('l'), Js('n'), Js('q'), Js('r'), Js('v'), Js('z'), Js('c'), Js('g'), Js('k'), Js('l'), Js('n'), Js('q'), Js('r'), Js('v'), Js('z'), Js('c'), Js('g'), Js('k'), Js('l'), Js('n'), Js('q'), Js('r'), Js('v'), Js('z')]))
var.put('nm4', Js([Js('d'), Js('n'), Js('r'), Js('s'), Js('th'), Js('z')]))
var.put('nm5', Js([Js('c'), Js('g'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('ia'), Js('ee'), Js('ae'), Js('ie')]))
var.put('nm7', Js([Js('cc'), Js('g'), Js('gn'), Js('gr'), Js('k'), Js('kk'), Js('kr'), Js('kn'), Js('kz'), Js('kl'), Js('lk'), Js('lg'), Js('lr'), Js('lz'), Js('m'), Js('mz'), Js('mm'), Js('n'), Js('nn'), Js('nk'), Js('ng'), Js('nz'), Js('nr'), Js('r'), Js('rg'), Js('rk'), Js('rs'), Js('rv'), Js('s'), Js('sz'), Js('sr'), Js('sq'), Js('zz'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm8', Js([Js('amber'), Js('ash'), Js('axe'), Js('battle'), Js('beast'), Js('blaze'), Js('blood'), Js('burning'), Js('chaos'), Js('cinder'), Js('claw'), Js('cold'), Js('dark'), Js('dead'), Js('death'), Js('deep'), Js('doom'), Js('ember'), Js('far'), Js('fire'), Js('fist'), Js('flame'), Js('fury'), Js('fuse'), Js('glow'), Js('grand'), Js('hard'), Js('haze'), Js('heavy'), Js('hell'), Js('iron'), Js('keen'), Js('lone'), Js('mist'), Js('molten'), Js('moon'), Js('mountain'), Js('mourn'), Js('nether'), Js('night'), Js('pride'), Js('proud'), Js('pyre'), Js('rage'), Js('rough'), Js('rumble'), Js('shade'), Js('shadow'), Js('sharp'), Js('skull'), Js('spider'), Js('steel'), Js('still'), Js('storm'), Js('stout'), Js('strong'), Js('sun'), Js('swift'), Js('titan'), Js('true'), Js('wild'), Js('wolf'), Js('wrath')]))
var.put('nm9', Js([Js('bane'), Js('bash'), Js('basher'), Js('beam'), Js('blade'), Js('blaze'), Js('blight'), Js('bow'), Js('branch'), Js('brand'), Js('breaker'), Js('bringer'), Js('caller'), Js('claw'), Js('crusher'), Js('cut'), Js('cutter'), Js('fall'), Js('fang'), Js('fire'), Js('fist'), Js('flaw'), Js('flayer'), Js('force'), Js('forge'), Js('fury'), Js('gaze'), Js('gloom'), Js('glory'), Js('grip'), Js('guard'), Js('hammer'), Js('hell'), Js('horn'), Js('hunter'), Js('killer'), Js('lash'), Js('mane'), Js('mark'), Js('maul'), Js('maw'), Js('mourn'), Js('rage'), Js('reaper'), Js('reaver'), Js('ripper'), Js('roar'), Js('run'), Js('runner'), Js('scream'), Js('shade'), Js('shadow'), Js('shard'), Js('shot'), Js('slayer'), Js('snarl'), Js('soar'), Js('spear'), Js('spire'), Js('splitter'), Js('stalker'), Js('storm'), Js('strike'), Js('taker'), Js('talon'), Js('thorn'), Js('ward'), Js('weaver')]))
pass
pass


# Add lib to the module scope
wildstarDraken = var.to_python()