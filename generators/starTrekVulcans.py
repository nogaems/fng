__all__ = ['starTrekVulcans']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
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
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('names', ((var.get('nm5').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    if (var.get('rnd2')<Js(2.0)):
                        while (var.get('rnd4')<Js(2.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    if (var.get('rnd2')<Js(3.0)):
                        while (var.get('rnd4')<Js(3.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ch'), Js('D'), Js('F'), Js('H'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('P'), Js('S'), Js('Sk'), Js('Sp'), Js('St'), Js('Str'), Js('T'), Js("T'K"), Js('V'), Js("V'L"), Js('S'), Js('Sk'), Js('Sp'), Js('St'), Js('Str'), Js('S')]))
var.put('nm2', Js([Js('aa'), Js('ia'), Js('au'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y')]))
var.put('nm3', Js([Js('d'), Js('f'), Js('j'), Js('kk'), Js('l'), Js('ll'), Js('lk'), Js('lv'), Js('n'), Js('p'), Js('r'), Js('rr'), Js('s'), Js('str'), Js('ss'), Js('t'), Js('v')]))
var.put('nm4', Js([Js(''), Js(''), Js('c'), Js('ck'), Js('k'), Js('k'), Js('k'), Js('l'), Js('lk'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('rk'), Js('s'), Js('ss'), Js('t'), Js('tt'), Js('th'), Js('v')]))
var.put('nm5', Js([Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js("t's"), Js("t'r"), Js("t'h"), Js("t'l"), Js("t'm"), Js("t'p"), Js("t'pl"), Js("t'pr"), Js("t'sh"), Js("v'l"), Js('v')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js("t's"), Js("t'r"), Js("t'h"), Js("t'l"), Js("t'm"), Js("t'p"), Js("t'pl"), Js("t'pr"), Js("t'sh"), Js("v'l"), Js('v')]))
var.put('nm7', Js([Js('aa'), Js('ai'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm8', Js([Js('k'), Js('l'), Js('m'), Js('n'), Js('nv'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('v')]))
var.put('nm9', Js([Js(''), Js(''), Js('k'), Js('l'), Js('n'), Js('ng'), Js('r'), Js('s'), Js('th')]))
pass
pass


# Add lib to the module scope
starTrekVulcans = var.to_python()