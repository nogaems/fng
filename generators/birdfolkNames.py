__all__ = ['birdfolkNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    while (var.get('rnd3')<Js(5.0)):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm6').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3'))))
                else:
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(8.0)):
                        var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm10').get(var.get('rnd3'))))
                    else:
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm9').get(var.get('rnd4')),var.get('nm9').get(var.get('rnd6'))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd3'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(3.0)):
                        while (var.get('rnd')<Js(5.0)):
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        while (var.get('rnd3')<Js(5.0)):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm11').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+var.get('nm15').get(var.get('rnd3'))))
                    else:
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm15').get(var.get('rnd3'))))
                        else:
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                            while PyJsStrictEq(var.get('nm14').get(var.get('rnd4')),var.get('nm14').get(var.get('rnd6'))):
                                var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                            var.put('names', ((((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm14').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm15').get(var.get('rnd3'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(3.0)):
                        while (var.get('rnd')<Js(5.0)):
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                        while (var.get('rnd3')<Js(5.0)):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
                    else:
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd3'))))
                        else:
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                            while PyJsStrictEq(var.get('nm4').get(var.get('rnd4')),var.get('nm4').get(var.get('rnd6'))):
                                var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('c'), Js('cr'), Js('g'), Js('gr'), Js('k'), Js('kr'), Js('q'), Js('qr'), Js('r'), Js('sk'), Js('skr'), Js('sq'), Js('sqr'), Js('sc'), Js('z'), Js('zr')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('e'), Js('o'), Js('u'), Js('a'), Js('i'), Js('i'), Js('a'), Js('e'), Js('e'), Js('a'), Js('i'), Js('e'), Js('o'), Js('u'), Js('a'), Js('i'), Js('i'), Js('a'), Js('e'), Js('e'), Js('ai'), Js('ee'), Js('ia'), Js('ie'), Js('oo'), Js('ua')]))
var.put('nm3', Js([Js('ai'), Js('ee'), Js('ia'), Js('ie'), Js('oo'), Js('ua')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('cc'), Js('k'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('shr'), Js('t'), Js('y'), Js('w')]))
var.put('nm5', Js([Js(''), Js(''), Js('k'), Js('q'), Js('t'), Js('th'), Js('w'), Js('ww'), Js('wk')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('cr'), Js('g'), Js('gh'), Js('gr'), Js('k'), Js('kh'), Js('q'), Js('qh'), Js('r'), Js('rh'), Js('sq'), Js('sc'), Js('z'), Js('zr'), Js('zh')]))
var.put('nm7', Js([Js('a'), Js('i'), Js('e'), Js('o'), Js('u'), Js('a'), Js('i'), Js('i'), Js('a'), Js('e'), Js('e'), Js('a'), Js('i'), Js('e'), Js('o'), Js('u'), Js('a'), Js('i'), Js('i'), Js('a'), Js('e'), Js('e'), Js('ee'), Js('ea'), Js('ei'), Js('ia'), Js('ie'), Js('oo')]))
var.put('nm8', Js([Js('ee'), Js('ea'), Js('ei'), Js('ia'), Js('ie'), Js('oo')]))
var.put('nm9', Js([Js('b'), Js('bb'), Js('c'), Js('l'), Js('ll'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('sh'), Js('t'), Js('y'), Js('w')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('k'), Js('n'), Js('t'), Js('th'), Js('w'), Js('ww')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('cr'), Js('g'), Js('gh'), Js('gr'), Js('k'), Js('kr'), Js('kh'), Js('q'), Js('qr'), Js('qh'), Js('sk'), Js('r'), Js('rh'), Js('skr'), Js('sq'), Js('sqr'), Js('sc'), Js('z'), Js('zr'), Js('zh')]))
var.put('nm12', Js([Js('a'), Js('i'), Js('e'), Js('o'), Js('u'), Js('a'), Js('i'), Js('i'), Js('a'), Js('e'), Js('e'), Js('a'), Js('i'), Js('e'), Js('o'), Js('u'), Js('a'), Js('i'), Js('i'), Js('a'), Js('e'), Js('e'), Js('ai'), Js('ee'), Js('ea'), Js('ei'), Js('ia'), Js('ie'), Js('oo'), Js('ua')]))
var.put('nm13', Js([Js('ai'), Js('ee'), Js('ea'), Js('ei'), Js('ia'), Js('ie'), Js('oo'), Js('ua')]))
var.put('nm14', Js([Js('b'), Js('bb'), Js('c'), Js('cc'), Js('k'), Js('l'), Js('ll'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('sh'), Js('shr'), Js('t'), Js('y'), Js('w')]))
var.put('nm15', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('k'), Js('n'), Js('t'), Js('th'), Js('w'), Js('ww'), Js('wk')]))
pass
pass


# Add lib to the module scope
birdfolkNames = var.to_python()