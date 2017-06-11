__all__ = ['hydraNames']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(4.0)):
                if (var.get('rnd')<Js(5.0)):
                    while (var.get('rnd5')<Js(7.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd7'))):
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd7'))):
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm3').get(var.get('rnd7'))):
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('g'), Js('gh'), Js('j'), Js('jh'), Js('k'), Js('kh'), Js('kr'), Js('m'), Js('mr'), Js('mg'), Js('n'), Js('ng'), Js('nr'), Js('tr'), Js('v'), Js('z'), Js('zh'), Js('zr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ou'), Js('ua'), Js('ia'), Js('ai'), Js('ae')]))
var.put('nm3', Js([Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z'), Js('g'), Js('h'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z'), Js('g'), Js('gg'), Js('k'), Js('kk'), Js('ll'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('r'), Js('ss'), Js('v'), Js('z'), Js('zz'), Js('ch'), Js('g'), Js('gz'), Js('gr'), Js('gn'), Js('gg'), Js('h'), Js('hj'), Js('hsh'), Js('hz'), Js('k'), Js('kk'), Js('kh'), Js('ll'), Js('m'), Js('mm'), Js('mz'), Js('n'), Js('ng'), Js('nn'), Js('nz'), Js('nk'), Js('ngr'), Js('r'), Js('rd'), Js('rg'), Js('rz'), Js('sh'), Js('ss'), Js('shg'), Js('shk'), Js('sk'), Js('ssh'), Js('ssk'), Js('sz'), Js('v'), Js('vh'), Js('z'), Js('zr'), Js('zsh'), Js('zg'), Js('zk'), Js('zz')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('hs'), Js('hz'), Js('j'), Js('n'), Js('s'), Js('sh'), Js('z')]))
var.put('nm5', Js([Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z'), Js('g'), Js('gg'), Js('k'), Js('kk'), Js('ll'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('r'), Js('ss'), Js('v'), Js('z'), Js('zz')]))
pass
pass


# Add lib to the module scope
hydraNames = var.to_python()