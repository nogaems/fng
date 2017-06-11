__all__ = ['naviNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nmEnd', 'nmCl', 'nm7', 'nm9', 'nm10', 'nm13', 'nm2', 'nm15', 'nm6'])
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
            var.put('names', Js(''))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('gEnd', Js("'ite"))
            else:
                var.put('gEnd', Js("'itan"))
            var.put('rndFn', ((var.get('Math').callprop('random')*Js(2.0))|(Js(0.0)+Js(2.0))))
            var.put('rndCn', ((var.get('Math').callprop('random')*Js(2.0))|(Js(0.0)+Js(2.0))))
            var.put('rndSn', ((var.get('Math').callprop('random')*Js(2.0))|(Js(0.0)+Js(2.0))))
            #for JS loop
            var.put('j', Js(0.0))
            while (var.get('j')<var.get('rndFn')):
                try:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    if (var.get('rnd')<Js(5.0)):
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nmCl').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nmCl').get(var.get('rnd2')),var.get('nm1').get(var.get('rnd'))):
                            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nmCl').get('length'))|Js(0.0)))
                    else:
                        var.put('rnd2', Js(0.0))
                    var.put('rndEnd', ((var.get('Math').callprop('random')*Js(3.0))|Js(0.0)))
                    var.put('rndDv', ((var.get('Math').callprop('random')*Js(4.0))|Js(0.0)))
                    if PyJsStrictEq(var.get('rndEnd'),Js(1.0)):
                        var.put('nm2a', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey')]))
                        var.put('nmEnd', Js([Js('k'), Js('kx'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('p'), Js('px'), Js('r'), Js('t'), Js('tx')]))
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nmEnd').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nmEnd').get(var.get('rnd4')),var.get('nm1').get(var.get('rnd'))):
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nmEnd').get('length'))|Js(0.0)))
                    else:
                        if PyJsStrictEq(var.get('nm1').get(var.get('rnd')),Js('')):
                            var.put('nm2a', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey')]))
                        else:
                            var.put('nm2a', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey'), Js('rr'), Js('ll')]))
                        var.put('nmEnd', Js([Js('')]))
                        var.put('rnd4', Js(0.0))
                    if PyJsStrictEq(var.get('rndDv'),Js(1.0)):
                        var.put('nm2', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey')]))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    else:
                        var.put('nm2', Js([Js('')]))
                        var.put('rnd5', Js(0.0))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm2a').get('length'))|Js(0.0)))
                    var.put('names', (((((var.get('names')+var.get('nm1').get(var.get('rnd')))+var.get('nmCl').get(var.get('rnd2')))+var.get('nm2a').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nmEnd').get(var.get('rnd4'))))
                finally:
                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            var.put('names', (var.get('names')+Js(' te ')))
            #for JS loop
            var.put('k', Js(0.0))
            while (var.get('k')<var.get('rndCn')):
                try:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    if (var.get('rnd')<Js(5.0)):
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nmCl').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nmCl').get(var.get('rnd2')),var.get('nm1').get(var.get('rnd'))):
                            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nmCl').get('length'))|Js(0.0)))
                    else:
                        var.put('rnd2', Js(0.0))
                    var.put('rndEnd', ((var.get('Math').callprop('random')*Js(3.0))|Js(0.0)))
                    var.put('rndDv', ((var.get('Math').callprop('random')*Js(4.0))|Js(0.0)))
                    if PyJsStrictEq(var.get('rndEnd'),Js(1.0)):
                        var.put('nm2a', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey')]))
                        var.put('nmEnd', Js([Js('k'), Js('kx'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('p'), Js('px'), Js('r'), Js('t'), Js('tx')]))
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nmEnd').get('length'))|Js(0.0)))
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nmEnd').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nmEnd').get(var.get('rnd4')),var.get('nm1').get(var.get('rnd'))):
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nmEnd').get('length'))|Js(0.0)))
                    else:
                        if PyJsStrictEq(var.get('nm1').get(var.get('rnd')),Js('')):
                            var.put('nm2a', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey')]))
                        else:
                            var.put('nm2a', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey'), Js('rr'), Js('ll')]))
                        var.put('nmEnd', Js([Js('')]))
                        var.put('rnd4', Js(0.0))
                    if PyJsStrictEq(var.get('rndDv'),Js(1.0)):
                        var.put('nm2', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey')]))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    else:
                        var.put('nm2', Js([Js('')]))
                        var.put('rnd5', Js(0.0))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm2a').get('length'))|Js(0.0)))
                    var.put('names', (((((var.get('names')+var.get('nm1').get(var.get('rnd')))+var.get('nmCl').get(var.get('rnd2')))+var.get('nm2a').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nmEnd').get(var.get('rnd4'))))
                finally:
                        (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
            var.put('names', (var.get('names')+Js(' ')))
            #for JS loop
            var.put('h', Js(0.0))
            while (var.get('h')<var.get('rndSn')):
                try:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    if (var.get('rnd')<Js(5.0)):
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nmCl').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nmCl').get(var.get('rnd2')),var.get('nm1').get(var.get('rnd'))):
                            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nmCl').get('length'))|Js(0.0)))
                    else:
                        var.put('rnd2', Js(0.0))
                    var.put('rndEnd', ((var.get('Math').callprop('random')*Js(3.0))|Js(0.0)))
                    var.put('rndDv', ((var.get('Math').callprop('random')*Js(4.0))|Js(0.0)))
                    if PyJsStrictEq(var.get('rndEnd'),Js(1.0)):
                        var.put('nm2a', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey')]))
                        var.put('nmEnd', Js([Js('k'), Js('kx'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('p'), Js('px'), Js('r'), Js('t'), Js('tx')]))
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nmEnd').get('length'))|Js(0.0)))
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nmEnd').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nmEnd').get(var.get('rnd4')),var.get('nm1').get(var.get('rnd'))):
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nmEnd').get('length'))|Js(0.0)))
                    else:
                        if PyJsStrictEq(var.get('nm1').get(var.get('rnd')),Js('')):
                            var.put('nm2a', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey')]))
                        else:
                            var.put('nm2a', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey'), Js('rr'), Js('ll')]))
                        var.put('nmEnd', Js([Js('')]))
                        var.put('rnd4', Js(0.0))
                    if PyJsStrictEq(var.get('rndDv'),Js(1.0)):
                        var.put('nm2', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey')]))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    else:
                        var.put('nm2', Js([Js('')]))
                        var.put('rnd5', Js(0.0))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm2a').get('length'))|Js(0.0)))
                    var.put('names', (((((var.get('names')+var.get('nm1').get(var.get('rnd')))+var.get('nmCl').get(var.get('rnd2')))+var.get('nm2a').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nmEnd').get(var.get('rnd4'))))
                finally:
                        (var.put('h',Js(var.get('h').to_number())+Js(1))-Js(1))
            var.put('names', (var.get('names')+var.get('gEnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('f'), Js('s'), Js('ts'), Js('f'), Js('s'), Js('h'), Js('k'), Js('h'), Js('k'), Js('kx'), Js('l'), Js('m'), Js('n'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('p'), Js('p'), Js('px'), Js('r'), Js('t'), Js('r'), Js('t'), Js('tx'), Js('v'), Js('w'), Js('y'), Js('z'), Js('v'), Js('w'), Js('y'), Js('z'), Js("'"), Js("'"), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), None, Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey')]))
var.put('nm3', Js([Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), None, Js('a'), Js('ä'), Js('e'), Js('i'), Js('ì'), Js('o'), Js('u'), Js('aw'), Js('ay'), Js('ew'), Js('ey'), Js('rr'), Js('ll')]))
var.put('nmEnd', Js([Js('k'), Js('k'), Js('kx'), Js('l'), Js('m'), Js('n'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('p'), Js('p'), Js('px'), Js('r'), Js('t'), Js('r'), Js('t'), Js('tx')]))
var.put('nmCl', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('p'), Js('t'), Js('k'), Js('p'), Js('t'), Js('k'), Js('px'), Js('tx'), Js('kx'), Js('m'), Js('n'), Js('m'), Js('n'), Js('ng'), Js('r'), Js('l'), Js('w'), Js('y'), Js('r'), Js('l'), Js('w'), Js('y')]))
var.put('nm5', Js([]))
var.put('nm6', Js([]))
var.put('nm7', Js([]))
var.put('nm8', Js([]))
var.put('nm9', Js([]))
var.put('nm10', Js([]))
var.put('nm11', Js([]))
var.put('nm12', Js([]))
var.put('nm13', Js([]))
var.put('nm14', Js([]))
var.put('nm15', Js([]))
pass
pass


# Add lib to the module scope
naviNames = var.to_python()