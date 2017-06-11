__all__ = ['starTrekBetazoids']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm14', 'nm17', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                    def PyJs_LONG_0_(var=var):
                        return (((((((((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5')))+Js(' '))+var.get('nm13').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd7')))+var.get('nm15').get(var.get('rnd8')))+var.get('nm16').get(var.get('rnd9')))+var.get('nm5').get(var.get('rnd10')))+var.get('nm17').get(var.get('rnd11')))
                    var.put('names', PyJs_LONG_0_())
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                    def PyJs_LONG_1_(var=var):
                        return (((((((((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5')))+var.get('nm10').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+Js(' '))+var.get('nm13').get(var.get('rnd8')))+var.get('nm14').get(var.get('rnd9')))+var.get('nm15').get(var.get('rnd10')))+var.get('nm17').get(var.get('rnd12')))
                    var.put('names', PyJs_LONG_1_())
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                    def PyJs_LONG_2_(var=var):
                        return var.put('names', ((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm13').get(var.get('rnd7')))+var.get('nm14').get(var.get('rnd8')))+var.get('nm15').get(var.get('rnd9')))+var.get('nm17').get(var.get('rnd11'))))
                    PyJs_LONG_2_()
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                    def PyJs_LONG_3_(var=var):
                        return var.put('names', ((((((((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(' '))+var.get('nm13').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd7')))+var.get('nm15').get(var.get('rnd8')))+var.get('nm16').get(var.get('rnd9')))+var.get('nm5').get(var.get('rnd10')))+var.get('nm17').get(var.get('rnd11'))))
                    PyJs_LONG_3_()
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ei'), Js('aa'), Js('oa')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('b'), Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('mr'), Js('nr'), Js('tr'), Js('sb'), Js('sd'), Js('sl'), Js('sm'), Js('sn'), Js('sr'), Js('str'), Js('ndr'), Js('nd'), Js('ng'), Js('nk'), Js('nl'), Js('nt'), Js('tt'), Js('rr'), Js('bb'), Js('dd'), Js('gg')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm6', Js([Js('m'), Js('n'), Js('s'), Js('d'), Js('h'), Js('l')]))
var.put('nm7', Js([Js('d'), Js('h'), Js('j'), Js('k'), Js('l'), Js('lw'), Js('m'), Js('n'), Js('st'), Js('t'), Js('r'), Js('rw'), Js('v')]))
var.put('nm8', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('ee'), Js('ia')]))
var.put('nm9', Js([Js('d'), Js('h'), Js('l'), Js('ll'), Js('nn'), Js('mm'), Js('n'), Js('m'), Js('rr'), Js('r'), Js('s'), Js('ss'), Js('str'), Js('v'), Js('vr'), Js('x'), Js('y')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o')]))
var.put('nm11', Js([Js('d'), Js('h'), Js('l'), Js('n'), Js('m'), Js('r'), Js('s'), Js('v'), Js('x'), Js('y')]))
var.put('nm12', Js([Js('t'), Js('h'), Js('w'), Js('n'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm13', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm14', Js([Js('b'), Js('d'), Js('g'), Js('h'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z'), Js('gr'), Js('dr'), Js('tr'), Js('br'), Js('ch')]))
var.put('nm15', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('oi'), Js('aa'), Js('ea'), Js('ai'), Js('ei')]))
var.put('nm16', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('lbr'), Js('m'), Js('n'), Js('r'), Js('s'), Js('str'), Js('t'), Js('v'), Js('x'), Js('z')]))
var.put('nm17', Js([Js('x'), Js('n'), Js('r'), Js('l'), Js('m'), Js('k'), Js('d'), Js('t'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
starTrekBetazoids = var.to_python()