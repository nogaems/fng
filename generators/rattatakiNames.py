__all__ = ['rattatakiNames']

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
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('names', (((((var.get('nm6').get(var.get('rnd6'))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd5'))))
            else:
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd8')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('au'), Js('ei'), Js('ou'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('b'), Js('br'), Js('bz'), Js('bj'), Js('c'), Js('cz'), Js('ch'), Js('d'), Js('dj'), Js('dz'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kz'), Js('kr'), Js('p'), Js('pr'), Js('pj'), Js('pz'), Js('q'), Js('r'), Js('sj'), Js('st'), Js('sr'), Js('t'), Js('ts'), Js('tr'), Js('v'), Js('wr'), Js('x'), Js('xj'), Js('xr'), Js('yj'), Js('yr'), Js('ys'), Js('yz'), Js('z'), Js('zr')]))
var.put('nm3', Js([Js('i'), Js('a'), Js('o'), Js('e'), Js('u')]))
var.put('nm4', Js([Js('c'), Js('ch'), Js('dj'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('m'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z')]))
var.put('nm5', Js([Js('c'), Js('ch'), Js('dj'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('m'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('au'), Js('ei'), Js('ou'), Js('ay'), Js('ey'), Js('oy'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm7', Js([Js('b'), Js('br'), Js('bj'), Js('c'), Js('cz'), Js('ch'), Js('d'), Js('dj'), Js('dz'), Js('g'), Js('h'), Js('j'), Js('k'), Js('kz'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pj'), Js('q'), Js('r'), Js('s'), Js('sj'), Js('st'), Js('sr'), Js('t'), Js('ts'), Js('tr'), Js('v'), Js('w'), Js('wr'), Js('x'), Js('xj'), Js('xr'), Js('y'), Js('yj'), Js('yr'), Js('ys'), Js('yz'), Js('z'), Js('zr')]))
var.put('nm8', Js([Js('i'), Js('a'), Js('o'), Js('e'), Js('u'), Js('ie'), Js('ai'), Js('ey'), Js('ay')]))
pass
pass


# Add lib to the module scope
rattatakiNames = var.to_python()