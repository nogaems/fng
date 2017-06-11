__all__ = ['brownieNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    while (var.get('rnd3')<Js(5.0)):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3'))))
                else:
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    while (PyJsStrictEq(var.get('nm7').get(var.get('rnd4')),var.get('nm5').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm7').get(var.get('rnd4')),var.get('nm8').get(var.get('rnd3')))):
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(8.0)):
                        var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm8').get(var.get('rnd3'))))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm7').get(var.get('rnd6')),var.get('nm7').get(var.get('rnd4'))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd3'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(4.0)):
                        while (var.get('rnd')<Js(3.0)):
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        while (var.get('rnd3')<Js(5.0)):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd3'))))
                    else:
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                        while (PyJsStrictEq(var.get('nm11').get(var.get('rnd4')),var.get('nm10').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm11').get(var.get('rnd4')),var.get('nm12').get(var.get('rnd3')))):
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+var.get('nm12').get(var.get('rnd3'))))
                        else:
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                            while PyJsStrictEq(var.get('nm11').get(var.get('rnd6')),var.get('nm11').get(var.get('rnd4'))):
                                var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                            var.put('names', ((((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd7')))+var.get('nm12').get(var.get('rnd3'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(4.0)):
                        while (var.get('rnd')<Js(5.0)):
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                        while (var.get('rnd3')<Js(5.0)):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3'))))
                    else:
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        while (PyJsStrictEq(var.get('nm3').get(var.get('rnd4')),var.get('nm1').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd4')),var.get('nm4').get(var.get('rnd3')))):
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd3'))))
                        else:
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                            while PyJsStrictEq(var.get('nm3').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd4'))):
                                var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('l'), Js('m'), Js('p'), Js('r'), Js('s'), Js('t')]))
var.put('nm2', Js([Js('a'), Js('a'), Js('a'), Js('a'), Js('a'), Js('aa'), Js('ai'), Js('ao'), Js('ea'), Js('ei'), Js('eo'), Js('i'), Js('i'), Js('ia'), Js('io'), Js('o'), Js('o'), Js('oi'), Js('u'), Js('u'), Js('ui')]))
var.put('nm3', Js([Js('b'), Js('bh'), Js('bhr'), Js('ch'), Js('d'), Js('dh'), Js('g'), Js('ghn'), Js('hl'), Js('l'), Js('ll'), Js('lmh'), Js('lp'), Js('lr'), Js('lt'), Js('m'), Js('mh'), Js('mhl'), Js('mhn'), Js('n'), Js('ng'), Js('ngh'), Js('nn'), Js('nnch'), Js('nngh'), Js('rd'), Js('rgh'), Js('rn'), Js('rt'), Js('s'), Js('sg'), Js('th')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('bh'), Js('c'), Js('ch'), Js('d'), Js('dh'), Js('g'), Js('gh'), Js('ll'), Js('m'), Js('mh'), Js('n'), Js('nn'), Js('r'), Js('s'), Js('th')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('fl'), Js('h'), Js('l'), Js('m'), Js('r'), Js('s'), Js('t')]))
var.put('nm6', Js([Js('a'), Js('a'), Js('a'), Js('a'), Js('ai'), Js('e'), Js('e'), Js('e'), Js('ea'), Js('ei'), Js('eo'), Js('eu'), Js('i'), Js('i'), Js('io'), Js('iu'), Js('o'), Js('o'), Js('oi'), Js('u')]))
var.put('nm7', Js([Js('b'), Js('bh'), Js('bl'), Js('dh'), Js('g'), Js('ghd'), Js('ghn'), Js('ghr'), Js('l'), Js('lr'), Js('m'), Js('mh'), Js('n'), Js('ng'), Js('ngh'), Js('nn'), Js('ns'), Js('r'), Js('rdr'), Js('rn'), Js('s'), Js('t'), Js('thr'), Js('tl'), Js('tr')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('dh'), Js('g'), Js('l'), Js('ld'), Js('ll'), Js('n'), Js('r'), Js('s')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('l'), Js('m'), Js('r'), Js('s'), Js('t')]))
var.put('nm10', Js([Js('a'), Js('a'), Js('a'), Js('a'), Js('ai'), Js('ea'), Js('ei'), Js('eo'), Js('i'), Js('i'), Js('ia'), Js('io'), Js('o'), Js('o'), Js('oi'), Js('u')]))
var.put('nm11', Js([Js('b'), Js('bh'), Js('d'), Js('dh'), Js('g'), Js('ghn'), Js('l'), Js('ll'), Js('lr'), Js('m'), Js('mh'), Js('n'), Js('ng'), Js('ngh'), Js('nn'), Js('rd'), Js('rn'), Js('s'), Js('t'), Js('tr')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('dh'), Js('g'), Js('gh'), Js('l'), Js('ll'), Js('m'), Js('mh'), Js('n'), Js('nn'), Js('r'), Js('s'), Js('th')]))
pass
pass


# Add lib to the module scope
brownieNames = var.to_python()