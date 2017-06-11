__all__ = ['basilisksNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'check'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('nm5').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd3'))):
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
            if (var.get('i')<Js(5.0)):
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                #for JS loop
                var.put('j', Js(0.0))
                while (var.get('j')<var.get('check').get('length')):
                    try:
                        while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                    finally:
                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            else:
                if (var.get('i')<Js(9.0)):
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
                        #for JS loop
                        var.put('j', Js(0.0))
                        while (var.get('j')<var.get('check').get('length')):
                            try:
                                while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
                            finally:
                                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                    else:
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                        #for JS loop
                        var.put('j', Js(0.0))
                        while (var.get('j')<var.get('check').get('length')):
                            try:
                                while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                            finally:
                                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                else:
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
                    #for JS loop
                    var.put('j', Js(0.0))
                    while (var.get('j')<var.get('check').get('length')):
                        try:
                            while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
                        finally:
                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('ch'), Js('h'), Js('j'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('th'), Js('x'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('u'), Js('aa'), Js('au'), Js('ei'), Js('ou'), Js('ua')]))
var.put('nm3', Js([Js('c'), Js('g'), Js('j'), Js('k'), Js('n'), Js('q'), Js('s'), Js('x'), Js('z'), Js('c'), Js('g'), Js('j'), Js('k'), Js('n'), Js('q'), Js('s'), Js('x'), Js('z'), Js('c'), Js('cc'), Js('ch'), Js('cs'), Js('cr'), Js('hs'), Js('hg'), Js('hx'), Js('hn'), Js('g'), Js('gg'), Js('gr'), Js('gy'), Js('gsh'), Js('j'), Js('k'), Js('kh'), Js('ksh'), Js('ks'), Js('kz'), Js('kr'), Js('n'), Js('ns'), Js('nsh'), Js('nz'), Js('nq'), Js('q'), Js('qh'), Js('s'), Js('sh'), Js('sz'), Js('x'), Js('z'), Js('zh')]))
var.put('nm4', Js([Js('c'), Js('g'), Js('j'), Js('k'), Js('n'), Js('q'), Js('s'), Js('x'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('h'), Js('q'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('x'), Js('z')]))
var.put('check', Js([Js('anal'), Js('anus'), Js('arse'), Js('ass'), Js('balls'), Js('bastard'), Js('biatch'), Js('bigot'), Js('bitch'), Js('bollock'), Js('bollok'), Js('boner'), Js('boob'), Js('bugger'), Js('bum'), Js('butt'), Js('clitoris'), Js('cock'), Js('coon'), Js('crap'), Js('cunt'), Js('damn'), Js('dick'), Js('dildo'), Js('dyke'), Js('fag'), Js('feck'), Js('felching'), Js('fellate'), Js('fellatio'), Js('flange'), Js('fuck'), Js('gay'), Js('lust'), Js('goddamn'), Js('homo'), Js('jackass'), Js('jerk'), Js('jizz'), Js('knobend'), Js('labia'), Js('muff'), Js('nigga'), Js('nigger'), Js('niggers'), Js('penis'), Js('piss'), Js('poop'), Js('prick'), Js('pube'), Js('pussy'), Js('queer'), Js('scrotum'), Js('sex'), Js('shit'), Js('slut'), Js('smegma'), Js('spunk'), Js('tit'), Js('tosser'), Js('turd'), Js('twat'), Js('vagina'), Js('wank'), Js('whore'), Js('wtf')]))
pass
pass


# Add lib to the module scope
basilisksNames = var.to_python()