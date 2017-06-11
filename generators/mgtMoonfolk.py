__all__ = ['mgtMoonfolk']

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
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', ((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+Js(', '))+var.get('nm7').get(var.get('rnd9'))))
                    else:
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(', '))+var.get('nm7').get(var.get('rnd9'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    while PyJsStrictEq(var.get('nm8').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    if (var.get('i')<Js(8.0)):
                        var.put('names', (((((((var.get('nm8').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+Js(' '))+var.get('nm7').get(var.get('rnd9'))))
                    else:
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        while PyJsStrictEq(var.get('nm3').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd7'))):
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', (((((((((var.get('nm8').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd8')))+Js(' '))+var.get('nm7').get(var.get('rnd9'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm3').get(var.get('rnd5'))):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+Js(', '))+var.get('nm7').get(var.get('rnd9'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    while PyJsStrictEq(var.get('nm8').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    if (var.get('i')<Js(8.0)):
                        var.put('names', (((((((var.get('nm8').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+Js(' '))+var.get('nm7').get(var.get('rnd9'))))
                    else:
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        while PyJsStrictEq(var.get('nm3').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd7'))):
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', (((((((((var.get('nm8').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd8')))+Js(' '))+var.get('nm7').get(var.get('rnd9'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('d'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('e'), Js('o'), Js('u'), Js('e'), Js('o'), Js('u'), Js('a'), Js('i')]))
var.put('nm3', Js([Js('b'), Js('d'), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('t'), Js('z')]))
var.put('nm4', Js([Js('e'), Js('a'), Js('o'), Js('e'), Js('a'), Js('o'), Js('e'), Js('a'), Js('o'), Js('e'), Js('a'), Js('o'), Js('i'), Js('i'), Js('u')]))
var.put('nm5', Js([Js('b'), Js('d'), Js('f'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y'), Js('z')]))
var.put('nm6', Js([Js('b'), Js('d'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('y'), Js('z')]))
var.put('nm7', Js([Js('Ambassador'), Js('Ascendant'), Js('Breezecaller'), Js('Cerberus'), Js('Cloud-Conjurer'), Js('Floodbringer'), Js('Cloudchaser'), Js('Cloudguard'), Js('Cloudkeeper'), Js('Cloudskater'), Js('Cloudwatcher'), Js('Conjurer'), Js('Conservator'), Js('Consul'), Js('Custodian'), Js('Defender'), Js('Delegate'), Js('Diplomat'), Js('Diviner'), Js('Emissary'), Js('Enchanter'), Js('Envoy'), Js('Guard'), Js('Guardian'), Js('Gustcaller'), Js('Illusionist'), Js('Keeper'), Js('Legate'), Js('Mage'), Js('Messenger'), Js('Mindsweeper'), Js('Mirror-Mage'), Js('Overseer'), Js('Prophet'), Js('Protector'), Js('Raincaller'), Js('Rainchaser'), Js('Rainmaker'), Js('Rainshaper'), Js('Sage'), Js('Savant'), Js('Sear'), Js('Seer'), Js('Sentinel'), Js('Sentry'), Js('Shepherd'), Js('Soothsayer'), Js('Sorcerer'), Js('Spellbinder'), Js('Vicar'), Js('Ward'), Js('Warden'), Js('Watch'), Js('Windcaller')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z')]))
pass
pass


# Add lib to the module scope
mgtMoonfolk = var.to_python()