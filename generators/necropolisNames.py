__all__ = ['necropolisNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['result', 'type'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('nm5').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd3'))):
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
            if (var.get('i')<Js(3.0)):
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    while (PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm5').get(var.get('rnd5'))) or PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3')))):
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd8', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(8.0)):
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd8')))+Js(' '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                    else:
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm1').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd8'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('g'), Js('j'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('ph'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('u'), Js('u'), Js('u'), Js('o'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('u'), Js('u'), Js('u'), Js('o'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('u'), Js('u'), Js('u'), Js('o'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('u'), Js('u'), Js('u'), Js('o'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('u'), Js('u'), Js('u'), Js('o'), Js('o'), Js('au'), Js('ou'), Js('uu'), Js('oo'), Js('aa'), Js('ao'), Js('ai')]))
var.put('nm3', Js([Js('br'), Js('ch'), Js('cr'), Js('d'), Js('dr'), Js('g'), Js('gg'), Js('ggr'), Js('gr'), Js('gz'), Js('k'), Js('kk'), Js('kkr'), Js('kkz'), Js('kr'), Js('l'), Js('lg'), Js('lgh'), Js('lk'), Js('lr'), Js('lt'), Js('lz'), Js('mk'), Js('mkh'), Js('nk'), Js('nkh'), Js('nr'), Js('nz'), Js('r'), Js('rk'), Js('rkh'), Js('rq'), Js('rrg'), Js('rrk'), Js('sh'), Js('shr'), Js('shz'), Js('sz'), Js('xn'), Js('xr'), Js('xx'), Js('xxr'), Js('z'), Js('zz')]))
var.put('nm4', Js([Js('d'), Js('dd'), Js('dr'), Js('g'), Js('gg'), Js('gn'), Js('gr'), Js('hm'), Js('hn'), Js('hr'), Js('hz'), Js('k'), Js('kk'), Js('kn'), Js('kr'), Js('kv'), Js('kx'), Js('kz'), Js('lg'), Js('lz'), Js('m'), Js('mh'), Js('mm'), Js('n'), Js('nd'), Js('ng'), Js('nn'), Js('r'), Js('rh'), Js('rl'), Js('rm'), Js('rn'), Js('rr'), Js('s'), Js('sh'), Js('shz'), Js('ss'), Js('sz'), Js('z'), Js('zh'), Js('zk'), Js('zq'), Js('zz')]))
var.put('nm5', Js([Js('d'), Js('k'), Js('r'), Js('s'), Js('ss'), Js('th'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
necropolisNames = var.to_python()