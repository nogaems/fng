__all__ = ['haloJiralhanaeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('rnd3')<Js(25.0)):
                while (var.get('rnd5')<Js(25.0)):
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('br'), Js('c'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('y'), Js('u'), Js('i'), Js('o')]))
var.put('nm3', Js([Js('bb'), Js('cc'), Js('ck'), Js('ct'), Js('dd'), Js('gt'), Js('kk'), Js('kt'), Js('ll'), Js('rb'), Js('rc'), Js('rd'), Js('rg'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rp'), Js('rr'), Js('rs'), Js('rt'), Js('rv'), Js('rz'), Js('ss'), Js('st'), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm4', Js([Js('bb'), Js('cc'), Js('ck'), Js('ct'), Js('dd'), Js('gt'), Js('kk'), Js('kt'), Js('ll'), Js('rb'), Js('rc'), Js('rd'), Js('rg'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rp'), Js('rr'), Js('rs'), Js('rt'), Js('rv'), Js('rz'), Js('ss'), Js('st'), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm5', Js([Js('us'), Js('um'), Js('eus'), Js('eum'), Js('ion'), Js('ius'), Js('is')]))
pass
pass


# Add lib to the module scope
haloJiralhanaeNames = var.to_python()