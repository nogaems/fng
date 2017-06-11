__all__ = ['narniaCalmorenes']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                while (PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm11').get(var.get('rnd5')))):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                if (var.get('i')<Js(4.0)):
                    var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm8').get(var.get('rnd3'))):
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm11').get(var.get('rnd5'))))
                    else:
                        var.put('rnd8', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                        var.put('rnd9', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm10').get(var.get('rnd8'))):
                            var.put('rnd8', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                        var.put('names', ((((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd8')))+var.get('nm7').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd5'))))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                while (PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd5'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd')))):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('chl'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('dr'), Js('h'), Js('l'), Js('lg'), Js('lls'), Js('ld'), Js('lb'), Js('ldr'), Js('lbr'), Js('m'), Js('ml'), Js('nr'), Js('ng'), Js('nm'), Js('nsh'), Js('r'), Js('rph'), Js('rr'), Js('rd'), Js('rsh'), Js('rs'), Js('rb'), Js('shd'), Js('sd'), Js('sh'), Js('shb'), Js('sb'), Js('sht'), Js('x'), Js('zr'), Js('b'), Js('h'), Js('l'), Js('m'), Js('r'), Js('s')]))
var.put('nm4', Js([Js('b'), Js('d'), Js('l'), Js('ld'), Js('lb'), Js('m'), Js('mbr'), Js('mb'), Js('n'), Js('nd'), Js('ndr'), Js('nt'), Js('ntr'), Js('nth'), Js('rt'), Js('rd'), Js('rg'), Js('rth'), Js('sht'), Js('st'), Js('sh')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('h'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('t'), Js('th')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('v'), Js('z')]))
var.put('nm7', Js([Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('ee'), Js('ei'), Js('aa')]))
var.put('nm8', Js([Js('d'), Js('h'), Js('l'), Js('ln'), Js('lm'), Js('m'), Js('n'), Js('r'), Js('rd'), Js('s'), Js('v'), Js('z')]))
var.put('nm9', Js([Js('d'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('rd'), Js('sh'), Js('v'), Js('z')]))
var.put('nm10', Js([Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('v'), Js('w'), Js('y'), Js('z')]))
var.put('nm11', Js([Js('h'), Js('n'), Js('s'), Js('sh'), Js('th'), Js('h'), Js('n'), Js('s'), Js('sh'), Js('th'), Js('v'), Js('z')]))
pass
pass


# Add lib to the module scope
narniaCalmorenes = var.to_python()