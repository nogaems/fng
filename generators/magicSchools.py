__all__ = ['magicSchools']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('names', (((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names4').get(var.get('rnd4')))+var.get('names5').get(var.get('rnd5')))+var.get('names6').get(var.get('rnd6'))))
            else:
                var.put('names', (((((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names4').get(var.get('rnd4')))+var.get('names5').get(var.get('rnd5')))+var.get('names6').get(var.get('rnd6')))+Js(', '))+var.get('names7').get(var.get('rnd7'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names2', Js([Js('b'), Js('d'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('b'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('br'), Js('dr'), Js('gr'), Js('kr'), Js('pr'), Js('str'), Js('tr'), Js('bl'), Js('cl'), Js('fl'), Js('gl'), Js('kl'), Js('pl'), Js('sl')]))
var.put('names3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ea'), Js('ou'), Js('au'), Js('a'), Js('e'), Js('o')]))
var.put('names4', Js([Js('d'), Js('f'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('x')]))
var.put('names5', Js([Js('w'), Js('n'), Js('s'), Js('m'), Js('r'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names6', Js([Js('any'), Js('arry'), Js('arth'), Js('arths'), Js('arts'), Js('elts'), Js('erra'), Js('erry'), Js('erth'), Js('eth'), Js('iams'), Js('ia'), Js('iara'), Js('ine'), Js('inns'), Js('iths'), Js('iton'), Js('ity'), Js('onia'), Js('ons'), Js('ora'), Js('ore'), Js('orth'), Js('orths'), Js('ose'), Js('yce')]))
var.put('names7', Js([Js('Academy of Sorcery'), Js('Academy of Spells'), Js('Academy of Magics'), Js('Academy of Witchcraft'), Js('Academy of Wizardry'), Js('Academy of the Arcane'), Js('Institute of Magics'), Js('Institute of Wizardy'), Js('Institute of the Arcane'), Js('School of Magics'), Js('School of Sorcery'), Js('School of Witchcraft'), Js('School of Wizardry'), Js('School of Wizards'), Js('School of the Arcane')]))
pass
pass


# Add lib to the module scope
magicSchools = var.to_python()