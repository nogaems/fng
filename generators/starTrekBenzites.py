__all__ = ['starTrekBenzites']

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
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
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
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('j'), Js('k'), Js('m'), Js('p'), Js('q'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o')]))
var.put('nm3', Js([Js('b'), Js('d'), Js('r'), Js('rr'), Js('dd'), Js('zz'), Js('rb'), Js('rd'), Js('rg'), Js('rj'), Js('rk'), Js('rq'), Js('rt'), Js('rh'), Js('rl'), Js('rs'), Js('rv'), Js('nd'), Js('ng'), Js('nd'), Js('nr'), Js('nt'), Js('nv'), Js('dg'), Js('zd'), Js('zg'), Js('zr')]))
var.put('nm4', Js([Js('ck'), Js('n'), Js('k'), Js('d'), Js('r'), Js('z'), Js('t'), Js('g')]))
var.put('nm5', Js([Js('ar'), Js('or'), Js('ur'), Js('an'), Js('on'), Js('un'), Js('at'), Js('ot'), Js('ut'), Js('az'), Js('oz'), Js('uz'), Js('ab'), Js('ob'), Js('ub'), Js('ad'), Js('od'), Js('ud'), Js('ak'), Js('ok'), Js('uk'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('j'), Js('k'), Js('m'), Js('p'), Js('q'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm7', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('p'), Js('q'), Js('r'), Js('t'), Js('v'), Js('x'), Js('y'), Js('z'), Js('cc'), Js('dd'), Js('gg'), Js('kk'), Js('pp'), Js('qq'), Js('rr'), Js('tt'), Js('vv'), Js('xx'), Js('zz')]))
var.put('nm8', Js([Js('n'), Js('x'), Js('q'), Js('s'), Js('th'), Js('g'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm9', Js([Js('in'), Js('en'), Js('iq'), Js('eq'), Js('ix'), Js('ex'), Js('eth'), Js('ith'), Js('ez'), Js('iz'), Js('ey'), Js('iy')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
starTrekBenzites = var.to_python()