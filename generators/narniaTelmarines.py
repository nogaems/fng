__all__ = ['narniaTelmarines']

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
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                if (var.get('i')<Js(6.0)):
                    var.put('names', (((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4'))))
                else:
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('rnd8', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', (((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd8')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd4'))))
                    else:
                        var.put('names', (((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd8')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4'))))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                while (PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd5'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd')))):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                if (var.get('i')<Js(4.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                    else:
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('gl'), Js('gr'), Js('m'), Js('n'), Js('r'), Js('rh'), Js('s'), Js('sc')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('cn'), Js('ct'), Js('g'), Js('gt'), Js('gr'), Js('gn'), Js('l'), Js('lp'), Js('lv'), Js('lt'), Js('nd'), Js('nn'), Js('nv'), Js('p'), Js('r'), Js('rg'), Js('rl'), Js('rs'), Js('rt'), Js('sp'), Js('st'), Js('sn'), Js('thl'), Js('th'), Js('tr'), Js('tv'), Js('v'), Js('vr'), Js('vl'), Js('z')]))
var.put('nm4', Js([Js('g'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('s')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('d'), Js('m'), Js('n'), Js('r'), Js('rn'), Js('s'), Js('z')]))
var.put('nm6', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('h'), Js('l'), Js('m'), Js('n'), Js('pr'), Js('s'), Js('t'), Js('tr')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('u')]))
var.put('nm8', Js([Js('d'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('v'), Js('y'), Js('z')]))
var.put('nm9', Js([Js('dn'), Js('dl'), Js('fn'), Js('fl'), Js('ffl'), Js('gn'), Js('gl'), Js('gs'), Js('ll'), Js('ln'), Js('lm'), Js('ls'), Js('ml'), Js('mml'), Js('nl'), Js('nnl'), Js('ns'), Js('sm'), Js('sl'), Js('ssl'), Js('sn'), Js('zl'), Js('zn'), Js('zzl')]))
var.put('nm10', Js([Js('e'), Js('i'), Js('ia'), Js('ea'), Js('ei')]))
pass
pass


# Add lib to the module scope
narniaTelmarines = var.to_python()