__all__ = ['diabloSeraphim']

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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', (((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm8').get(var.get('rnd4'))))
                else:
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm8').get(var.get('rnd4'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4'))))
                else:
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('dr'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('th'), Js('v'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ai')]))
var.put('nm3', Js([Js('br'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('l'), Js('lt'), Js('ll'), Js('lg'), Js('lth'), Js('lz'), Js('m'), Js('mp'), Js('mph'), Js('mphr'), Js('mr'), Js('n'), Js('nd'), Js('nn'), Js('nny'), Js('nr'), Js('nl'), Js('ph'), Js('r'), Js('s'), Js('sr'), Js('st'), Js('th'), Js('z'), Js('zr')]))
var.put('nm4', Js([Js('al'), Js('ael'), Js('eon'), Js('iel'), Js('ial'), Js('il'), Js('el'), Js('ius'), Js('ion'), Js('on'), Js('os'), Js('ual'), Js('us')]))
var.put('nm5', Js([Js('c'), Js('dr'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('s'), Js('th'), Js('v')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ai'), Js('au')]))
var.put('nm7', Js([Js('br'), Js('c'), Js('dr'), Js('dy'), Js('f'), Js('g'), Js('gh'), Js('gl'), Js('hn'), Js('hr'), Js('l'), Js('ll'), Js('lth'), Js('ls'), Js('lz'), Js('ln'), Js('lm'), Js('lf'), Js('m'), Js('mr'), Js('ml'), Js('mn'), Js('mph'), Js('nl'), Js('ny'), Js('nph'), Js('nd'), Js('r'), Js('rd'), Js('s'), Js('sh'), Js('sr'), Js('th'), Js('z')]))
var.put('nm8', Js([Js('el'), Js('ael'), Js('il'), Js('on'), Js('uen'), Js('uel'), Js('eil'), Js('iel'), Js('is'), Js('ith'), Js('oelle'), Js('oenne'), Js('aelle')]))
pass
pass


# Add lib to the module scope
diabloSeraphim = var.to_python()