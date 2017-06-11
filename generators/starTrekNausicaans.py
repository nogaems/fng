__all__ = ['starTrekNausicaans']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
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
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('rnd2')<Js(5.0)):
                    while (var.get('rnd4')<Js(5.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js('b'), Js('ch'), Js('d'), Js('dg'), Js('gh'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kl'), Js('lh'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('st'), Js('t'), Js('th'), Js('tl'), Js('tr'), Js('v'), Js('x'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('ae'), Js('ee'), Js('ei'), Js('ou'), Js('uu'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('bz'), Js('ch'), Js('d'), Js('g'), Js('ggr'), Js('gv'), Js('h'), Js('j'), Js('jh'), Js('l'), Js('lth'), Js('lrsh'), Js('k'), Js('kz'), Js('kkz'), Js('ktz'), Js('m'), Js('mmk'), Js('n'), Js('p'), Js('r'), Js('rt'), Js('rg'), Js('rc'), Js('sh'), Js('th'), Js('t'), Js('tz'), Js('v'), Js('y'), Js('yk'), Js('z'), Js('zj'), Js('zzg'), Js('d'), Js('g'), Js('h'), Js('j'), Js('l'), Js('k'), Js('m'), Js('n'), Js('p'), Js('r'), Js('t'), Js('v'), Js('y'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js('c'), Js('chk'), Js('rdz'), Js('g'), Js('jz'), Js('k'), Js('m'), Js('n'), Js('ng'), Js('p'), Js('r'), Js('rr'), Js('rrg'), Js('sh'), Js('t'), Js('th'), Js('tz'), Js('tkz'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('c'), Js('chk'), Js('rdz'), Js('g'), Js('jz'), Js('k'), Js('m'), Js('n'), Js('ng'), Js('p'), Js('r'), Js('rr'), Js('rrg'), Js('sh'), Js('t'), Js('th'), Js('tz'), Js('tkz'), Js('x'), Js('z')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
pass
pass


# Add lib to the module scope
starTrekNausicaans = var.to_python()