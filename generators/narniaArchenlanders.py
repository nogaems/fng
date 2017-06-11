__all__ = ['narniaArchenlanders']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3'))))
                else:
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm10').get(var.get('rnd3'))))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd3'))))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(3.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    if (var.get('rnd3')<Js(3.0)):
                        var.put('rnd3', (var.get('rnd3')+Js(3.0)))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
                else:
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('tr')]))
var.put('nm2', Js([Js('a'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('l'), Js('ll'), Js('lv'), Js('m'), Js('n'), Js('t'), Js('r'), Js('rr')]))
var.put('nm4', Js([Js('e'), Js('i')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('l'), Js('m'), Js('n'), Js('r')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t')]))
var.put('nm7', Js([Js('a'), Js('i'), Js('a'), Js('i'), Js('a'), Js('i'), Js('e'), Js('e'), Js('o')]))
var.put('nm8', Js([Js('d'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t')]))
var.put('nm9', Js([Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v')]))
var.put('nm10', Js([Js('ln'), Js('m'), Js('mn'), Js('n'), Js('nn'), Js('ph'), Js('rn'), Js('s'), Js('sh'), Js('t'), Js('th')]))
pass
pass


# Add lib to the module scope
narniaArchenlanders = var.to_python()