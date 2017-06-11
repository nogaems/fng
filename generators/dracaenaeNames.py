__all__ = ['dracaenaeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nameMas', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
    while (PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd5')))):
        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
    if (var.get('i')<Js(6.0)):
        var.put('nMs', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
    else:
        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
        while (PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3'))) or PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm6').get(var.get('rnd5')))):
            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
        var.put('nMs', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd5'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameMas_.func_name = 'nameMas'
var.put('nameMas', PyJsHoisted_nameMas_)
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
            var.get('nameMas')()
            while PyJsStrictEq(var.get('nMs'),Js('')):
                var.get('nameMas')()
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gh'), Js('gr'), Js('l'), Js('ll'), Js('m'), Js('mn'), Js('n'), Js('p'), Js('ph'), Js('phr'), Js('s'), Js('sh'), Js('st'), Js('sth'), Js('sc'), Js('t'), Js('th'), Js('thr'), Js('v'), Js('z'), Js('zh')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('y'), Js('a'), Js('e'), Js('i'), Js('y'), Js('a'), Js('e'), Js('i'), Js('y'), Js('a'), Js('e'), Js('i'), Js('y'), Js('a'), Js('e'), Js('i'), Js('y'), Js('a'), Js('e'), Js('i'), Js('y'), Js('a'), Js('e'), Js('i'), Js('y'), Js('ui'), Js('oe'), Js('ia'), Js('ae'), Js('ea'), Js('eo'), Js('ie')]))
var.put('nm3', Js([Js('b'), Js('ch'), Js('d'), Js('dd'), Js('dh'), Js('dn'), Js('f'), Js('ff'), Js('fr'), Js('fl'), Js('l'), Js('ll'), Js('lm'), Js('ln'), Js('lr'), Js('m'), Js('mp'), Js('mb'), Js('ml'), Js('mn'), Js('mr'), Js('n'), Js('nt'), Js('nz'), Js('ns'), Js('nsh'), Js('p'), Js('ph'), Js('phr'), Js('phn'), Js('phl'), Js('r'), Js('rr'), Js('rl'), Js('rn'), Js('rm'), Js('s'), Js('ss'), Js('sh'), Js('shr'), Js('st'), Js('str'), Js('sth'), Js('t'), Js('th'), Js('tt'), Js('thr'), Js('tr'), Js('ts'), Js('v')]))
var.put('nm4', Js([Js('b'), Js('d'), Js('f'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('i'), Js('o')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('n'), Js('ph'), Js('s'), Js('s'), Js('sh'), Js('sh'), Js('th')]))
pass
pass
pass


# Add lib to the module scope
dracaenaeNames = var.to_python()