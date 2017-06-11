__all__ = ['swDurosNames']

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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('namelast', ((var.get('nm7').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm9').get(var.get('rnd8'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('namelast', ((((var.get('nm7').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd10')))+var.get('nm9').get(var.get('rnd8'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(3.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
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
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ei'), Js('aa'), Js('ai'), Js('oo')]))
var.put('nm3', Js([Js('d'), Js('dw'), Js('hw'), Js('l'), Js('lz'), Js('ls'), Js('ld'), Js('lw'), Js('m'), Js('ms'), Js('mz'), Js('n'), Js('ns'), Js('nz'), Js('nss'), Js('nt'), Js('rw'), Js('z'), Js('d'), Js('l'), Js('m'), Js('n'), Js('z')]))
var.put('nm4', Js([Js('d'), Js('l'), Js('m'), Js('n'), Js('r')]))
var.put('nm5', Js([Js('ch'), Js('d'), Js('f'), Js('h'), Js('j'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('z')]))
var.put('nm6', Js([Js('ch'), Js('d'), Js('dw'), Js('h'), Js('hl'), Js('hn'), Js('hm'), Js('m'), Js('mm'), Js('mn'), Js('md'), Js('ms'), Js('n'), Js('nd'), Js('nl'), Js('nw'), Js('ns'), Js('nt'), Js('nn'), Js('rl'), Js('sl'), Js('d'), Js('h'), Js('m'), Js('n'), Js('l'), Js('ll')]))
var.put('nm7', Js([Js('b'), Js('d'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('s'), Js('st'), Js('t'), Js('tr'), Js('v'), Js('zh')]))
var.put('nm8', Js([Js('b'), Js('bb'), Js('c'), Js('ch'), Js('ggl'), Js('gw'), Js('gl'), Js('gn'), Js('gg'), Js('g'), Js('h'), Js('kt'), Js('ll'), Js('lm'), Js('lw'), Js('md'), Js('m'), Js('mp'), Js('nw'), Js('nd'), Js('nt'), Js('ns'), Js('n'), Js('rd'), Js('rl'), Js('rr'), Js('z')]))
var.put('nm9', Js([Js(''), Js('d'), Js('g'), Js('ks'), Js('l'), Js('lt'), Js('m'), Js('n'), Js('s')]))
pass
pass


# Add lib to the module scope
swDurosNames = var.to_python()