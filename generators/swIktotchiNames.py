__all__ = ['swIktotchiNames']

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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('namelast', ((((var.get('nm5').get(var.get('rnd6'))+var.get('nm6').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd9')))+var.get('nm6').get(var.get('rnd10')))+var.get('nm8').get(var.get('rnd8'))))
            else:
                var.put('namelast', ((var.get('nm5').get(var.get('rnd6'))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('h'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('ae'), Js('ie'), Js('ye'), Js('yi'), Js('ei')]))
var.put('nm3', Js([Js('d'), Js('dh'), Js('f'), Js('fl'), Js('fn'), Js('l'), Js('ll'), Js('ld'), Js('ln'), Js('lm'), Js('lr'), Js('lv'), Js('m'), Js('mm'), Js('md'), Js('mr'), Js('mn'), Js('mk'), Js('n'), Js('nn'), Js('nh'), Js('nk'), Js('ng'), Js('nv'), Js('nl'), Js('r'), Js('rr'), Js('rn'), Js('rl'), Js('rk'), Js('rd'), Js('s'), Js('sl'), Js('sh'), Js('shk')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js('j'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('th')]))
var.put('nm5', Js([Js('ch'), Js('d'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('t'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('ii')]))
var.put('nm7', Js([Js('d'), Js('f'), Js('h'), Js('j'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v'), Js('w'), Js('z')]))
var.put('nm8', Js([Js(''), Js(''), Js('l'), Js('mm'), Js('n'), Js('r'), Js('s')]))
pass
pass


# Add lib to the module scope
swIktotchiNames = var.to_python()