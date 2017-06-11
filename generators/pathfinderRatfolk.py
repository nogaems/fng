__all__ = ['pathfinderRatfolk']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd5')<Js(8.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(7.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('cr'), Js('ch'), Js('d'), Js('dr'), Js('dj'), Js('g'), Js('gr'), Js('gn'), Js('gl'), Js('j'), Js('k'), Js('kr'), Js('kv'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('skr'), Js('sc'), Js('scr'), Js('sk'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('z'), Js('zr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i')]))
var.put('nm3', Js([Js('cc'), Js('cd'), Js('cr'), Js('gg'), Js('gr'), Js('gk'), Js('gv'), Js('gd'), Js('kk'), Js('kr'), Js('kv'), Js('kz'), Js('m'), Js('mm'), Js('md'), Js('mk'), Js('mv'), Js('mz'), Js('n'), Js('nn'), Js('nd'), Js('nv'), Js('nk'), Js('ng'), Js('nz'), Js('rr'), Js('r'), Js('rk'), Js('rv'), Js('rz'), Js('rc'), Js('rg'), Js('rd'), Js('vv'), Js('v'), Js('vd'), Js('vk'), Js('vz')]))
var.put('nm4', Js([Js('c'), Js('g'), Js('c'), Js('g'), Js('hl'), Js('hz'), Js('hk'), Js('hn'), Js('hc'), Js('k'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('z'), Js('k'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('z')]))
var.put('nm5', Js([Js('b'), Js('bh'), Js('c'), Js('ch'), Js('dh'), Js('f'), Js('fr'), Js('fh'), Js('gh'), Js('j'), Js('k'), Js('m'), Js('n'), Js('nh'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('vh'), Js('z'), Js('zh')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('e'), Js('e'), Js('e'), Js('i'), Js('i'), Js('i')]))
var.put('nm7', Js([Js('b'), Js('bb'), Js('c'), Js('cc'), Js('f'), Js('ff'), Js('g'), Js('gg'), Js('j'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('p'), Js('pp'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('tt'), Js('z'), Js('zz')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('f'), Js('hm'), Js('hl'), Js('ks'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('tch'), Js('x')]))
pass
pass


# Add lib to the module scope
pathfinderRatfolk = var.to_python()