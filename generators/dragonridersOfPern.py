__all__ = ['dragonridersOfPern']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6', 'check'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                    #for JS loop
                    var.put('j', Js(0.0))
                    while (var.get('j')<var.get('check').get('length')):
                        try:
                            while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                                var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                        finally:
                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5'))))
                    #for JS loop
                    var.put('j', Js(0.0))
                    while (var.get('j')<var.get('check').get('length')):
                        try:
                            while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                                var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5'))))
                        finally:
                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    if (var.get('i')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        if (var.get('i')<Js(3.0)):
                            var.put('names', ((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5'))))
                            #for JS loop
                            var.put('j', Js(0.0))
                            while (var.get('j')<var.get('check').get('length')):
                                try:
                                    while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                                        var.put('names', ((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5'))))
                                finally:
                                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                        else:
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                            var.put('names', ((((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd7')))+var.get('nm12').get(var.get('rnd5'))))
                            #for JS loop
                            var.put('j', Js(0.0))
                            while (var.get('j')<var.get('check').get('length')):
                                try:
                                    while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                                        var.put('names', ((((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd7')))+var.get('nm12').get(var.get('rnd5'))))
                                finally:
                                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((var.get('nm13').get(var.get('rnd'))+var.get('nm14').get(var.get('rnd2')))+var.get('nm15').get(var.get('rnd3')))+var.get('nm14').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5'))))
                            #for JS loop
                            var.put('j', Js(0.0))
                            while (var.get('j')<var.get('check').get('length')):
                                try:
                                    while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                                        var.put('names', ((((var.get('nm13').get(var.get('rnd'))+var.get('nm14').get(var.get('rnd2')))+var.get('nm15').get(var.get('rnd3')))+var.get('nm14').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5'))))
                                finally:
                                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                        else:
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                            var.put('names', ((((((var.get('nm13').get(var.get('rnd'))+var.get('nm14').get(var.get('rnd2')))+var.get('nm15').get(var.get('rnd3')))+var.get('nm14').get(var.get('rnd4')))+var.get('nm15').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd7')))+var.get('nm12').get(var.get('rnd5'))))
                            #for JS loop
                            var.put('j', Js(0.0))
                            while (var.get('j')<var.get('check').get('length')):
                                try:
                                    while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                                        var.put('names', ((((((var.get('nm13').get(var.get('rnd'))+var.get('nm14').get(var.get('rnd2')))+var.get('nm15').get(var.get('rnd3')))+var.get('nm14').get(var.get('rnd4')))+var.get('nm15').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd7')))+var.get('nm12').get(var.get('rnd5'))))
                                finally:
                                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(3.0)):
                        while (var.get('rnd')<Js(4.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        while (var.get('rnd5')<Js(4.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
                        #for JS loop
                        var.put('j', Js(0.0))
                        while (var.get('j')<var.get('check').get('length')):
                            try:
                                while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
                            finally:
                                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                    else:
                        if (var.get('i')<Js(7.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                            #for JS loop
                            var.put('j', Js(0.0))
                            while (var.get('j')<var.get('check').get('length')):
                                try:
                                    while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                                finally:
                                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                        else:
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5'))))
                            #for JS loop
                            var.put('j', Js(0.0))
                            while (var.get('j')<var.get('check').get('length')):
                                try:
                                    while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5'))))
                                finally:
                                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('y'), Js('y'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('ee'), Js('au'), Js('ai'), Js('ie'), Js('ea'), Js('io')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('b'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('g'), Js('k'), Js('l'), Js('ld'), Js('ll'), Js('lr'), Js('lt'), Js('m'), Js('n'), Js('nc'), Js('nd'), Js('ng'), Js('ngr'), Js('nn'), Js('nr'), Js('ns'), Js('nt'), Js('p'), Js('r'), Js('rbr'), Js('rm'), Js('rn'), Js('rr'), Js('rsh'), Js('rt'), Js('sg'), Js('shm'), Js('ss'), Js('sr'), Js('st'), Js('t'), Js('th'), Js('v'), Js('x')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('l'), Js('l'), Js('l'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('n'), Js('n'), Js('n'), Js('n'), Js('nt'), Js('r'), Js('rg'), Js('rl'), Js('s'), Js('sh'), Js('st'), Js('t'), Js('x')]))
var.put('nm5', Js([Js('b'), Js('br'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('w'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('io'), Js('ia'), Js('ai'), Js('ea')]))
var.put('nm7', Js([Js('c'), Js('d'), Js('dn'), Js('k'), Js('kk'), Js('kl'), Js('l'), Js('l'), Js('l'), Js('l'), Js('lk'), Js('ll'), Js('ll'), Js('ll'), Js('lm'), Js('ln'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('r'), Js('rdr'), Js('rn'), Js('rr'), Js('s'), Js('ss'), Js('sn'), Js('sl'), Js('t'), Js('tr'), Js('v'), Js('y'), Js('z'), Js('c'), Js('d'), Js('k'), Js('l'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y'), Js('z'), Js('kk'), Js('ll'), Js('ll'), Js('mm'), Js('nn'), Js('rr'), Js('ss')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('n'), Js('m')]))
var.put('nm9', Js([Js('b'), Js('br'), Js('c'), Js('ch'), Js('cr'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('p'), Js('r'), Js('s'), Js('sp'), Js('t'), Js('v'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('ai'), Js('io')]))
var.put('nm11', Js([Js('dr'), Js('g'), Js('gr'), Js('gl'), Js('k'), Js('l'), Js('lz'), Js('ld'), Js('m'), Js('n'), Js('nd'), Js('r'), Js('r'), Js('r'), Js('r'), Js('rr'), Js('rm'), Js('rn'), Js('rt'), Js('ss'), Js('sr'), Js('y'), Js('z'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('y'), Js('z')]))
var.put('nm12', Js([Js('lth'), Js('nth'), Js('rth'), Js('th')]))
var.put('nm13', Js([Js('b'), Js('br'), Js('ch'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('t'), Js('w'), Js('z')]))
var.put('nm14', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm15', Js([Js('d'), Js('d'), Js('l'), Js('l'), Js('l'), Js('l'), Js('ll'), Js('lm'), Js('ln'), Js('ls'), Js('m'), Js('m'), Js('n'), Js('n'), Js('nl'), Js('nr'), Js('nm'), Js('r'), Js('r'), Js('r'), Js('rl'), Js('r'), Js('s'), Js('s'), Js('yl'), Js('yr'), Js('yn')]))
var.put('check', Js([Js('anal'), Js('anus'), Js('arse'), Js('ass'), Js('balls'), Js('bastard'), Js('biatch'), Js('bigot'), Js('bitch'), Js('bollock'), Js('bollok'), Js('boner'), Js('boob'), Js('bugger'), Js('bum'), Js('butt'), Js('clitoris'), Js('cock'), Js('coon'), Js('crap'), Js('cunt'), Js('damn'), Js('dick'), Js('dildo'), Js('dyke'), Js('fag'), Js('feck'), Js('felching'), Js('fellate'), Js('fellatio'), Js('flange'), Js('fuck'), Js('gay'), Js('lust'), Js('goddamn'), Js('homo'), Js('jackass'), Js('jerk'), Js('jizz'), Js('knobend'), Js('labia'), Js('muff'), Js('nigga'), Js('nigger'), Js('penis'), Js('piss'), Js('poop'), Js('prick'), Js('pube'), Js('pussy'), Js('queer'), Js('scrotum'), Js('sex'), Js('shit'), Js('slut'), Js('smegma'), Js('spunk'), Js('tit'), Js('tosser'), Js('turd'), Js('twat'), Js('vagina'), Js('wank'), Js('whore'), Js('wtf')]))
pass
pass


# Add lib to the module scope
dragonridersOfPern = var.to_python()