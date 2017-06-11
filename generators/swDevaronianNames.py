__all__ = ['swDevaronianNames']

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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('namelast', ((var.get('nm8').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd8'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('namelast', ((((var.get('nm8').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm9').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd10')))+var.get('nm10').get(var.get('rnd8'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(4.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd4b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd3b')))+var.get('nm2').get(var.get('rnd4b')))+var.get('nm7').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd5')<Js(5.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd3b')))+var.get('nm2').get(var.get('rnd4b')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('c'), Js('cr'), Js('ch'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ue'), Js('ao'), Js('ei'), Js('aa')]))
var.put('nm3', Js([Js('c'), Js('ch'), Js('g'), Js('gh'), Js('gr'), Js('k'), Js('kr'), Js('kh'), Js('kl'), Js('l'), Js('ll'), Js('lm'), Js('m'), Js('mr'), Js('mm'), Js('md'), Js('n'), Js('nd'), Js('r'), Js('rt'), Js('ss'), Js('vr'), Js('v')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('cx'), Js('hk'), Js('hr'), Js('k'), Js('kh'), Js('lc'), Js('lt'), Js('n'), Js('r'), Js('rc'), Js('rh'), Js('s'), Js('ss'), Js('t'), Js('th'), Js('x')]))
var.put('nm5', Js([Js('b'), Js('br'), Js('bh'), Js('c'), Js('ch'), Js('cr'), Js('g'), Js('gh'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('t'), Js('th'), Js('v')]))
var.put('nm6', Js([Js('bh'), Js('ch'), Js('dh'), Js('g'), Js('gh'), Js('gn'), Js('h'), Js('hn'), Js('hs'), Js('l'), Js('ll'), Js('ln'), Js('lm'), Js('m'), Js('mm'), Js('mn'), Js('n'), Js('nn'), Js('nch'), Js('r'), Js('rh'), Js('s'), Js('ss'), Js('v')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('th'), Js('y')]))
var.put('nm8', Js([Js('br'), Js('c'), Js('ch'), Js('dr'), Js("d'r"), Js("d'v"), Js('dh'), Js('g'), Js('gr'), Js("g'v"), Js('h'), Js('j'), Js('m'), Js("n'v"), Js('n'), Js('r'), Js('t'), Js("t'v"), Js("t'r"), Js('v')]))
var.put('nm9', Js([Js('d'), Js('dd'), Js('gr'), Js('gn'), Js('k'), Js('kr'), Js('kl'), Js('l'), Js('lg'), Js('ln'), Js('ll'), Js('lr'), Js('m'), Js('mm'), Js('mr'), Js('mn'), Js('n'), Js('nn'), Js('nd'), Js('nh'), Js('r'), Js('rh'), Js('rg'), Js('s'), Js('sn'), Js('ss'), Js('x'), Js('v'), Js('z')]))
var.put('nm10', Js([Js('c'), Js('ct'), Js('g'), Js('hrk'), Js('hk'), Js('k'), Js('kt'), Js('l'), Js('n'), Js('ndt'), Js('nd'), Js('nt'), Js('q'), Js('r'), Js('rt'), Js('rk'), Js('s'), Js('sk'), Js('st'), Js('v'), Js('w'), Js('z')]))
pass
pass


# Add lib to the module scope
swDevaronianNames = var.to_python()