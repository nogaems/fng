__all__ = ['pathfinderAasimar']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
            var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd16', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('nameLast', ((((((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm10').get(var.get('rnd14')))+var.get('nm11').get(var.get('rnd15')))+var.get('nm10').get(var.get('rnd16')))+var.get('nm12').get(var.get('rnd12'))))
            else:
                var.put('nameLast', ((((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm10').get(var.get('rnd14')))+var.get('nm12').get(var.get('rnd12'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(7.0)):
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('cr'), Js('d'), Js('gr'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('s'), Js('t'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ai'), Js('au'), Js('ie'), Js('ia'), Js('ea')]))
var.put('nm3', Js([Js('b'), Js('b'), Js('d'), Js('d'), Js('dr'), Js('g'), Js('g'), Js('gr'), Js('gn'), Js('k'), Js('k'), Js('kw'), Js('kr'), Js('l'), Js('l'), Js('lw'), Js('lr'), Js('lm'), Js('ln'), Js('lg'), Js('lt'), Js('m'), Js('m'), Js('mr'), Js('ml'), Js('mw'), Js('n'), Js('n'), Js('nr'), Js('nl'), Js('ng'), Js('nv'), Js('nw'), Js('r'), Js('r'), Js('rl'), Js('rw'), Js('rg'), Js('rn'), Js('t'), Js('t')]))
var.put('nm4', Js([Js('l'), Js('m'), Js('n'), Js('n'), Js('n'), Js('nt'), Js('r')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('dr'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('r'), Js('rh'), Js('v'), Js('vh'), Js('w')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('oe'), Js('ou'), Js('ua'), Js('ea'), Js('ia')]))
var.put('nm7', Js([Js('d'), Js('d'), Js('dr'), Js('dy'), Js('gr'), Js('j'), Js('j'), Js('l'), Js('l'), Js('ll'), Js('lt'), Js('ld'), Js('lm'), Js('ln'), Js('ldr'), Js('ls'), Js('m'), Js('m'), Js('mr'), Js('mk'), Js('ml'), Js('n'), Js('n'), Js('ndr'), Js('nd'), Js('nk'), Js('ng'), Js('nd'), Js('ny'), Js('nm'), Js('p'), Js('p'), Js('pr'), Js('r'), Js('r'), Js('rk'), Js('rl'), Js('s'), Js('s'), Js('v'), Js('v'), Js('y'), Js('y'), Js('z'), Js('z')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('n'), Js('r')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('dr'), Js('h'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm11', Js([Js('b'), Js('d'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('kr'), Js('km'), Js('l'), Js('ll'), Js('lr'), Js('ls'), Js('lg'), Js('ldr'), Js('lm'), Js('lw'), Js('m'), Js('mr'), Js('ml'), Js('n'), Js('nm'), Js('ng'), Js('nv'), Js('nk'), Js('p'), Js('pr'), Js('r'), Js('rl'), Js('rg'), Js('rv'), Js('rw'), Js('s'), Js('v'), Js('z')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js('l'), Js('m'), Js('n'), Js('r')]))
pass
pass


# Add lib to the module scope
pathfinderAasimar = var.to_python()