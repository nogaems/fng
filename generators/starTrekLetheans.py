__all__ = ['starTrekLetheans']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
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
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('rnd2')<Js(4.0)):
                    while (var.get('rnd4')<Js(4.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    while (var.get('rnd6')<Js(4.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if (var.get('rnd4')<Js(4.0)):
                    while (var.get('rnd6')<Js(4.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd7'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('rnd2')<Js(4.0)):
                    while (var.get('rnd4')<Js(4.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('z'), Js(''), Js('')]))
var.put('nm2', Js([Js('oi'), Js('ao'), Js('ui'), Js('ei'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('t'), Js('v'), Js('z'), Js('b'), Js('bb'), Js('bt'), Js('cz'), Js('c'), Js('d'), Js('dl'), Js('dz'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kz'), Js('kl'), Js('kr'), Js('l'), Js('lt'), Js('lv'), Js('m'), Js('nj'), Js('nb'), Js('n'), Js('nth'), Js('p'), Js('q'), Js('qr'), Js('r'), Js('rr'), Js('rrn'), Js('rn'), Js('t'), Js('tt'), Js('v'), Js('vv'), Js('z'), Js('zz'), Js('ztr'), Js('zm')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('k'), Js('m'), Js('nt'), Js('n'), Js('p'), Js('q'), Js('r'), Js('sz'), Js('t'), Js('v'), Js('z'), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
starTrekLetheans = var.to_python()