__all__ = ['starTrekRigelians']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd7'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd7'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('C'), Js('Ch'), Js('D'), Js('G'), Js('Gr'), Js('K'), Js('Kr'), Js('M'), Js('Pr'), Js('R'), Js('Sr'), Js('Sch'), Js('T'), Js('V'), Js('Vr'), Js('W'), Js('Z')]))
var.put('nm2', Js([Js('a'), Js('ae'), Js('ei'), Js('i'), Js('o'), Js('ou'), Js('u'), Js('a'), Js('u'), Js('a'), Js('u'), Js('o'), Js('ii'), Js('ea'), Js('oo'), Js('aa'), Js('a'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('b'), Js('ch'), Js('d'), Js('g'), Js('d'), Js('g'), Js('gr'), Js('k'), Js('l'), Js('m'), Js('n'), Js('t'), Js('v'), Js('w'), Js('k'), Js('l'), Js('m'), Js('n'), Js('t'), Js('v'), Js('w'), Js('xt'), Js('y'), Js('z'), Js('y'), Js('z'), Js('zy')]))
var.put('nm4', Js([Js('d'), Js('k'), Js('l'), Js('lr'), Js('n'), Js('p'), Js('r'), Js('t'), Js('v'), Js(''), Js('')]))
var.put('nm5', Js([Js('B'), Js('C'), Js('H'), Js('J'), Js('K'), Js('Kh'), Js('R'), Js('S'), Js('Sh'), Js('X'), Js('Y'), Js('Z'), Js('Zh')]))
var.put('nm6', Js([Js('a'), Js('ae'), Js('ei'), Js('i'), Js('o'), Js('ou'), Js('u'), Js('a'), Js('u'), Js('a'), Js('u'), Js('o'), Js('ii'), Js('ea'), Js('oo'), Js('aa'), Js('oi'), Js('ee')]))
var.put('nm7', Js([Js('c'), Js('ch'), Js('gg'), Js('gr'), Js('l'), Js('ll'), Js('ln'), Js('ngy'), Js('ng'), Js('n'), Js('m'), Js('s'), Js('st'), Js('sh'), Js('shw'), Js('v'), Js('ys'), Js('w'), Js('wr'), Js('c'), Js('g'), Js('l'), Js('s'), Js('v'), Js('w'), Js('c'), Js('g'), Js('l'), Js('s'), Js('v'), Js('w'), Js('n'), Js('n'), Js('m'), Js('m')]))
var.put('nm8', Js([Js('d'), Js('l'), Js('n'), Js('m'), Js('s'), Js('x'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
starTrekRigelians = var.to_python()