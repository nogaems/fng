__all__ = ['zeldaGoronNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(4.0)):
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd4'))))
            else:
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd4'))))
                if (var.get('i')>Js(7.0)):
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('D'), Js('G'), Js('K'), Js('M'), Js('N'), Js('R'), Js('T')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bl'), Js('d'), Js('dr'), Js('dl'), Js('g'), Js('gr'), Js('gl'), Js('gg'), Js('g'), Js('gr'), Js('gl'), Js('gg'), Js('g'), Js('gr'), Js('gl'), Js('gg'), Js('g'), Js('gr'), Js('gl'), Js('gg'), Js('l'), Js('lg'), Js('lb'), Js('ld'), Js('m'), Js('mr'), Js('md'), Js('mb'), Js('n'), Js('nd'), Js('nl'), Js('nb'), Js('ng'), Js('r'), Js('rb'), Js('rg'), Js('rd'), Js('rk'), Js('rm'), Js('rtr'), Js('t'), Js('z'), Js('kb'), Js('kl'), Js('km'), Js('kn'), Js('kd'), Js('b'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('z'), Js('b'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('z'), Js('b'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('z'), Js('b'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('z'), Js('b'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('k'), Js('g'), Js('ck'), Js('gs'), Js('m'), Js('n'), Js('s')]))
pass
pass


# Add lib to the module scope
zeldaGoronNames = var.to_python()