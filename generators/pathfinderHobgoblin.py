__all__ = ['pathfinderHobgoblin']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2'])
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
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(8.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('rnd')<Js(3.0)):
                    while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('kr'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('t'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('dr'), Js('gl'), Js('gr'), Js('gt'), Js('gh'), Js('kr'), Js('kt'), Js('kh'), Js('kl'), Js('l'), Js('lgr'), Js('lt'), Js('ld'), Js('ldr'), Js('lg'), Js('lb'), Js('lbr'), Js('ll'), Js('r'), Js('rg'), Js('rd'), Js('rt'), Js('rdr'), Js('rgr'), Js('rk'), Js('rl'), Js('th'), Js('tt'), Js('tr'), Js('thr'), Js('vl'), Js('vr'), Js('vt')]))
var.put('nm4', Js([Js(''), Js('d'), Js('g'), Js('k'), Js('m'), Js('n'), Js('ng'), Js('r'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('h'), Js('k'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm7', Js([Js('cl'), Js('cn'), Js('cm'), Js('cd'), Js('f'), Js('ff'), Js('fn'), Js('fm'), Js('fl'), Js('kl'), Js('kr'), Js('kn'), Js('km'), Js('kd'), Js('kt'), Js('ks'), Js('l'), Js('lz'), Js('ln'), Js('lm'), Js('ld'), Js('lg'), Js('m'), Js('mz'), Js('ms'), Js('mr'), Js('md'), Js('mg'), Js('mk'), Js('n'), Js('ns'), Js('nd'), Js('nr'), Js('ng'), Js('ns'), Js('nk'), Js('r'), Js('rm'), Js('rg'), Js('rn'), Js('rd'), Js('rk'), Js('s'), Js('sm'), Js('st'), Js('ss'), Js('sz'), Js('sm'), Js('sn'), Js('sd'), Js('sg'), Js('th'), Js('tr'), Js('tn'), Js('tz'), Js('ts'), Js('yd'), Js('yn'), Js('yg'), Js('yk'), Js('yr'), Js('yz')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('t')]))
pass
pass


# Add lib to the module scope
pathfinderHobgoblin = var.to_python()