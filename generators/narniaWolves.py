__all__ = ['narniaWolves']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
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
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
            if (var.get('rnd')<Js(3.0)):
                while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('a'), Js('a'), Js('a'), Js('e'), Js('e'), Js('i'), Js('i'), Js('o'), Js('o'), Js('u'), Js('u'), Js('u'), Js('au'), Js('ao'), Js('ou'), Js('ua')]))
var.put('nm3', Js([Js('br'), Js('cr'), Js('cl'), Js('cz'), Js('dr'), Js('gr'), Js('gn'), Js('gd'), Js('gdr'), Js('kn'), Js('kr'), Js('kl'), Js('kd'), Js('ld'), Js('ldr'), Js('lg'), Js('lgr'), Js('lk'), Js('mdr'), Js('mk'), Js('mr'), Js('ng'), Js('ngr'), Js('nd'), Js('ndr'), Js('nz'), Js('rb'), Js('rd'), Js('rv'), Js('rz'), Js('rg'), Js('sb'), Js('sk'), Js('sl'), Js('sm'), Js('zn'), Js('zr'), Js('zl')]))
var.put('nm4', Js([Js('a'), Js('i'), Js('a'), Js('i'), Js('a'), Js('i'), Js('e'), Js('o'), Js('u'), Js('u')]))
var.put('nm5', Js([Js(''), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('x')]))
pass
pass


# Add lib to the module scope
narniaWolves = var.to_python()