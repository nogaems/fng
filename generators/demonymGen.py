__all__ = ['demonymGen']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'cust', 'dVowel', 'nm3', 'ranNames', 'nm2', 'nm6', 'vowel'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['csRan', 'dVowelLast', 'endingSplice', 'sran', 'vowelLast', 'endingNoSplice', 'cRan', 'cEndingSplice', 'cEndingNoSplice', 'endings', 'result', 'ran'])
    var.put('endings', Js([Js('n'), Js('an'), Js('ian'), Js('anian'), Js('nian'), Js('in'), Js('ine'), Js('ite'), Js('r'), Js('er'), Js('eno'), Js('ino'), Js('ish'), Js('ene'), Js('ensian'), Js('ard'), Js('ese'), Js('lese'), Js('vese'), Js('nese'), Js('i'), Js('ic'), Js('iot'), Js('iote'), Js('asque'), Js('gian'), Js('onian'), Js('vian')]))
    var.put('endingSplice', Js([Js('an'), Js('ian'), Js('anian'), Js('in'), Js('ine'), Js('ite'), Js('er'), Js('eno'), Js('ino'), Js('ish'), Js('ene'), Js('ensian'), Js('ard'), Js('ese'), Js('i'), Js('ic'), Js('iot'), Js('iote'), Js('asque'), Js('onian')]))
    var.put('endingNoSplice', Js([Js('nan'), Js('nian'), Js('nin'), Js('no'), Js('ne'), Js('nsian'), Js('lese'), Js('vese'), Js('nese'), Js('gian'), Js('vian'), Js('lian')]))
    var.put('cEndingSplice', Js([Js('an'), Js('ian'), Js('anian'), Js('in'), Js('ine'), Js('ite'), Js('er'), Js('eno'), Js('ino'), Js('ish'), Js('ene'), Js('ensian'), Js('ard'), Js('ese'), Js('i'), Js('ic'), Js('iot'), Js('iote'), Js('asque'), Js('onian')]))
    var.put('cEndingNoSplice', Js([Js('n'), Js('an'), Js('an'), Js('anian'), Js('nian'), Js('in'), Js('ine'), Js('ite'), Js('er'), Js('eno'), Js('ino'), Js('ish'), Js('ene'), Js('ensian'), Js('ard'), Js('ese'), Js('lese'), Js('vese'), Js('nese'), Js('i'), Js('ic'), Js('ot'), Js('ote'), Js('asque'), Js('gian'), Js('onian'), Js('vian')]))
    var.put('vowelLast', Js('no'))
    var.put('dVowelLast', Js('no'))
    var.put('result', Js([]))
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<Js(10.0)):
        try:
            if (var.get('j')<Js(2.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('cEndingSplice').get('length'))|Js(0.0)))
                var.get('ranNames').put(var.get('j'), (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('cEndingSplice').get(var.get('rnd5'))))
            else:
                if (var.get('j')<Js(4.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.get('ranNames').put(var.get('j'), (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
                else:
                    if (var.get('j')<Js(6.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                        var.get('ranNames').put(var.get('j'), ((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
                    else:
                        if (var.get('j')<Js(8.0)):
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                            var.get('ranNames').put(var.get('j'), ((var.get('nm2').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3'))))
                        else:
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('cEndingSplice').get('length'))|Js(0.0)))
                            var.get('ranNames').put(var.get('j'), (((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm1').get(var.get('rnd3')))+var.get('cEndingSplice').get(var.get('rnd4'))))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if var.get('$')(Js('#custName')).callprop('is', Js(':checked')):
                var.put('cust', var.get('$')(Js('.custName')).callprop('val'))
            else:
                var.put('cust', var.get('ranNames').get(var.get('i')))
            var.put('custLast', var.get('cust').callprop('slice', (-Js(1.0))))
            var.put('custLastTwo', var.get('cust').callprop('slice', (-Js(2.0))))
            #for JS loop
            var.put('j', Js(0.0))
            while (var.get('j')<var.get('vowel').get('length')):
                try:
                    if PyJsStrictEq(var.get('custLast'),var.get('vowel').get(var.get('j'))):
                        var.put('vowelLast', Js('yes'))
                        var.put('cEndingSplice', Js([Js('an'), Js('ian'), Js('anian'), Js('in'), Js('ine'), Js('ite'), Js('er'), Js('eno'), Js('ino'), Js('ish'), Js('ene'), Js('ensian'), Js('ard'), Js('ese'), Js('i'), Js('ic'), Js('iot'), Js('iote'), Js('asque'), Js('onian')]))
                        var.put('cEndingNoSplice', Js([Js('n'), Js('an'), Js('an'), Js('anian'), Js('nian'), Js('in'), Js('ine'), Js('ite'), Js('er'), Js('eno'), Js('ino'), Js('ish'), Js('ene'), Js('ensian'), Js('ard'), Js('ese'), Js('lese'), Js('vese'), Js('nese'), Js('i'), Js('ic'), Js('ot'), Js('ote'), Js('asque'), Js('gian'), Js('onian'), Js('vian')]))
                    else:
                        var.put('vowelLast', Js('no'))
                finally:
                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('k', Js(0.0))
            while (var.get('k')<var.get('dVowel').get('length')):
                try:
                    if PyJsStrictEq(var.get('custLastTwo'),var.get('dVowel').get(var.get('k'))):
                        var.put('dVowelLast', Js('yes'))
                        var.put('endingSplice', Js([Js('an'), Js('ian'), Js('anian'), Js('in'), Js('ine'), Js('ite'), Js('er'), Js('eno'), Js('ino'), Js('ish'), Js('ene'), Js('ensian'), Js('ard'), Js('ese'), Js('i'), Js('ic'), Js('iot'), Js('iote'), Js('asque'), Js('onian')]))
                        var.put('endingNoSplice', Js([Js('nan'), Js('nian'), Js('nin'), Js('no'), Js('ne'), Js('nsian'), Js('lese'), Js('vese'), Js('nese'), Js('gian'), Js('vian'), Js('lian')]))
                    else:
                        var.put('dVowelLast', Js('no'))
                finally:
                        (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
            var.put('cRan', ((var.get('Math').callprop('random')*var.get('cEndingNoSplice').get('length'))|Js(0.0)))
            var.put('ran', ((var.get('Math').callprop('random')*var.get('endingNoSplice').get('length'))|Js(0.0)))
            var.put('csRan', ((var.get('Math').callprop('random')*var.get('cEndingSplice').get('length'))|Js(0.0)))
            var.put('sran', ((var.get('Math').callprop('random')*var.get('endingSplice').get('length'))|Js(0.0)))
            if PyJsStrictEq(var.get('vowelLast'),Js('yes')):
                if (var.get('i')<Js(5.0)):
                    var.put('names', (var.get('cust').callprop('slice', Js(0.0), (-Js(1.0)))+var.get('endingSplice').get(var.get('sran'))))
                    var.get('endingSplice').callprop('splice', var.get('sran'), Js(1.0))
                else:
                    var.put('names', (var.get('cust').callprop('slice', Js(0.0), (-Js(1.0)))+var.get('endingNoSplice').get(var.get('ran'))))
                    var.get('endingNoSplice').callprop('splice', var.get('ran'), Js(1.0))
            else:
                if PyJsStrictEq(var.get('dVowelLast'),Js('yes')):
                    if (var.get('i')<Js(5.0)):
                        if (var.get('cust').get('length')<Js(5.0)):
                            var.put('names', (var.get('cust').callprop('slice', Js(0.0), (-Js(1.0)))+var.get('endingSplice').get(var.get('cran'))))
                            var.get('endingSplice').callprop('splice', var.get('sran'), Js(1.0))
                        else:
                            var.put('names', (var.get('cust').callprop('slice', Js(0.0), (-Js(2.0)))+var.get('cEndingSplice').get(var.get('csRan'))))
                            var.get('cEndingSplice').callprop('splice', var.get('csRan'), Js(1.0))
                    else:
                        if (var.get('cust').get('length')<Js(5.0)):
                            var.put('names', (var.get('cust').callprop('slice', Js(0.0), (-Js(1.0)))+var.get('endingSplice').get(var.get('cran'))))
                            var.get('endingSplice').callprop('splice', var.get('sran'), Js(1.0))
                        else:
                            var.put('names', (var.get('cust').callprop('slice', Js(0.0), (-Js(2.0)))+var.get('cEndingNoSplice').get(var.get('cRan'))))
                            var.get('cEndingNoSplice').callprop('splice', var.get('cRan'), Js(1.0))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('names', (var.get('cust')+var.get('endingSplice').get(var.get('sran'))))
                        var.get('endingSplice').callprop('splice', var.get('sran'), Js(1.0))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('names', (var.get('cust').callprop('slice', Js(0.0), (-Js(1.0)))+var.get('endingSplice').get(var.get('sran'))))
                            var.get('endingSplice').callprop('splice', var.get('sran'), Js(1.0))
                        else:
                            if (var.get('i')<Js(8.0)):
                                if (var.get('cust').get('length')<Js(5.0)):
                                    var.put('names', (var.get('cust').callprop('slice', Js(0.0), (-Js(1.0)))+var.get('endingSplice').get(var.get('sran'))))
                                    var.get('endingSplice').callprop('splice', var.get('sran'), Js(1.0))
                                else:
                                    var.put('names', (var.get('cust').callprop('slice', Js(0.0), (-Js(2.0)))+var.get('endingSplice').get(var.get('sran'))))
                                    var.get('endingSplice').callprop('splice', var.get('sran'), Js(1.0))
                            else:
                                if (var.get('cust').get('length')<Js(5.0)):
                                    var.put('names', (var.get('cust').callprop('slice', Js(0.0), (-Js(1.0)))+var.get('endingSplice').get(var.get('sran'))))
                                    var.get('endingSplice').callprop('splice', var.get('sran'), Js(1.0))
                                else:
                                    var.put('names', (var.get('cust').callprop('slice', Js(0.0), (-Js(3.0)))+var.get('endingSplice').get(var.get('sran'))))
                                    var.get('endingSplice').callprop('splice', var.get('sran'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('i'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('pr'), Js('str'), Js('tr'), Js('bl'), Js('cl'), Js('gl'), Js('pl'), Js('sl'), Js('sc'), Js('sk'), Js('sm'), Js('sn'), Js('sp'), Js('st'), Js('sw'), Js('ch'), Js('sh'), Js('th'), Js('wh')]))
var.put('nm4', Js([Js('ae'), Js('ai'), Js('ao'), Js('au'), Js('a'), Js('ay'), Js('ea'), Js('ei'), Js('eo'), Js('eu'), Js('e'), Js('ey'), Js('ua'), Js('ue'), Js('ui'), Js('uo'), Js('u'), Js('uy'), Js('ia'), Js('ie'), Js('iu'), Js('io'), Js('iy'), Js('oa'), Js('oe'), Js('ou'), Js('oi'), Js('o'), Js('oy')]))
var.put('nm5', Js([Js('stan'), Js('dor'), Js('vania'), Js('nia'), Js('lor'), Js('cor'), Js('dal'), Js('bar'), Js('sal'), Js('ra'), Js('la'), Js('lia'), Js('jan'), Js('rus'), Js('ze'), Js('tan'), Js('wana'), Js('sil'), Js('so'), Js('na'), Js('le'), Js('bia'), Js('ca'), Js('ji'), Js('ce'), Js('ton'), Js('ssau'), Js('sau'), Js('sia'), Js('ca'), Js('ya'), Js('ye'), Js('yae'), Js('tho'), Js('stein'), Js('ria'), Js('nia'), Js('burg'), Js('nia'), Js('gro'), Js('que'), Js('gua'), Js('qua'), Js('rhiel'), Js('cia'), Js('les'), Js('dan'), Js('nga')]))
var.put('nm6', Js([Js('ia'), Js('a'), Js('en'), Js('ar'), Js('istan'), Js('aria'), Js('ington'), Js('ua'), Js('ijan'), Js('ain'), Js('ium'), Js('us'), Js('esh'), Js('os'), Js('ana'), Js('il'), Js('ad'), Js('or'), Js('ea'), Js('eau'), Js('ax'), Js('on'), Js('ana'), Js('ary'), Js('ya'), Js('ye'), Js('yae'), Js('ait'), Js('ein'), Js('urg'), Js('al'), Js('ines'), Js('ela')]))
var.put('vowel', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('dVowel', Js([Js('aa'), Js('ae'), Js('ai'), Js('ao'), Js('ae'), Js('ea'), Js('ee'), Js('ei'), Js('eo'), Js('eu'), Js('ia'), Js('ie'), Js('ii'), Js('io'), Js('iu'), Js('oa'), Js('oe'), Js('oi'), Js('oo'), Js('ou'), Js('ua'), Js('ue'), Js('ui'), Js('uo'), Js('uu')]))
var.put('ranNames', Js([]))
var.put('cust', Js(''))
pass
pass


# Add lib to the module scope
demonymGen = var.to_python()