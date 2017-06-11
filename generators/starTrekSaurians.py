__all__ = ['starTrekSaurians']

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
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    if (var.get('rnd2')>Js(4.0)):
                        while (var.get('rnd4')>Js(4.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm8').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    if (var.get('rnd2')>Js(4.0)):
                        while (var.get('rnd4')>Js(4.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    if ((var.get('rnd2')>Js(4.0)) or (var.get('rnd4')>Js(4.0))):
                        while (var.get('rnd6')>Js(4.0)):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm8').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5')))+var.get('nm8').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd7'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd6'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js('d'), Js('g'), Js('j'), Js('k'), Js('kr'), Js('m'), Js('n'), Js('pl'), Js('r'), Js('st'), Js('t'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('g'), Js('gz'), Js('ggt'), Js('j'), Js('k'), Js('kz'), Js('kr'), Js('km'), Js('l'), Js('m'), Js('mz'), Js('nz'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('rk'), Js('rd'), Js('t'), Js('tg'), Js('tk'), Js('zk'), Js('zr'), Js('zg'), Js('z'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('z'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('z')]))
var.put('nm4', Js([Js('c'), Js('chv'), Js('g'), Js('gt'), Js('k'), Js('n'), Js('s'), Js('ss'), Js('t'), Js('tt'), Js('z')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('ii'), Js(''), Js('')]))
var.put('nm6', Js([Js('g'), Js('gz'), Js('ggt'), Js('j'), Js('k'), Js('kz'), Js('kr'), Js('km'), Js('l'), Js('m'), Js('mz'), Js('nz'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('rk'), Js('rd'), Js('t'), Js('tg'), Js('tk'), Js('zk'), Js('zr'), Js('zg'), Js('z'), Js('c'), Js('chv'), Js('g'), Js('gt'), Js('k'), Js('n'), Js('s'), Js('ss'), Js('t'), Js('tt'), Js('z')]))
var.put('nm7', Js([Js(''), Js(''), Js('c'), Js('g'), Js('gl'), Js('h'), Js('j'), Js('k'), Js('l'), Js('n'), Js('m'), Js('r'), Js('s'), Js('sh'), Js('y')]))
var.put('nm8', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('ie'), Js('uo'), Js('ai'), Js('uu'), Js('oo'), Js('ae'), Js('uoa')]))
var.put('nm9', Js([Js('gr'), Js('gg'), Js('g'), Js('gt'), Js('h'), Js('l'), Js('m'), Js('n'), Js('nn'), Js('q'), Js('qq'), Js('r'), Js('rr'), Js('sh'), Js('s'), Js('ss'), Js('t'), Js('tt'), Js('v'), Js('y'), Js('z')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('g'), Js('m'), Js('n'), Js('s')]))
pass
pass


# Add lib to the module scope
starTrekSaurians = var.to_python()