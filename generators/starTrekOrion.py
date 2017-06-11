__all__ = ['starTrekOrion']

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
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd7'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('D'), Js('G'), Js('H'), Js('J'), Js('L'), Js('M'), Js('N'), Js('Ng'), Js('R'), Js('T'), Js('Th'), Js('V')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('e'), Js('o'), Js('a'), Js('ai'), Js('ou'), Js('aa'), Js('a'), Js('e'), Js('i'), Js('o')]))
var.put('nm3', Js([Js('g'), Js('gg'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('r'), Js('rr'), Js('sr'), Js('ss'), Js('t'), Js('tt'), Js('yc'), Js('z'), Js('zz')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm5', Js([Js('d'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('rc'), Js('v'), Js('z'), Js('')]))
var.put('nm6', Js([Js('D'), Js('G'), Js('H'), Js('J'), Js('L'), Js('M'), Js('N'), Js('S'), Js('Sh'), Js('T'), Js('Th'), Js('V'), Js('Zh')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('ee'), Js('ai'), Js('ay'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i')]))
var.put('nm8', Js([Js('d'), Js('dd'), Js('g'), Js('gg'), Js('hn'), Js('l'), Js('ll'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('rt'), Js('s'), Js('ss'), Js('sh'), Js('shk'), Js('v'), Js('vn'), Js('vv')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('ou')]))
var.put('nm10', Js([Js('r'), Js('s'), Js('sh'), Js('ss'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm11', Js([Js('hn'), Js('l'), Js('ll'), Js('n'), Js('nn'), Js('s'), Js('ss'), Js('sh'), Js('v')]))
pass
pass


# Add lib to the module scope
starTrekOrion = var.to_python()