__all__ = ['amazonNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('bl'), Js('br'), Js('c'), Js('chr'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gl'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kl'), Js('kr'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('ps'), Js('pr'), Js('r'), Js('rh'), Js('s'), Js('sm'), Js('sc'), Js('t'), Js('th'), Js('v'), Js('x'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ou'), Js('ei'), Js('oe'), Js('ao'), Js('io'), Js('eo'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('c'), Js('d'), Js('k'), Js('l'), Js('m'), Js('r'), Js('s'), Js('t'), Js('x'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('k'), Js('l'), Js('m'), Js('r'), Js('s'), Js('t'), Js('x'), Js('nd'), Js('nt'), Js('lk'), Js('lc'), Js('ll'), Js('ndr'), Js('br'), Js('st'), Js('ch'), Js('br'), Js('cl'), Js('ph'), Js('rm'), Js('pp'), Js('pt'), Js('rp'), Js('nth'), Js('th'), Js('rg'), Js('thr'), Js('dm'), Js('lth'), Js('lc'), Js('chr'), Js('phn'), Js('dr'), Js('mn'), Js('rr'), Js('rrh')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('adia'), Js('ameia'), Js('anta'), Js('asca'), Js('cabe'), Js('ce'), Js('cleia'), Js('cyone'), Js('cyra'), Js('da'), Js('dae'), Js('dia'), Js('dice'), Js('dora'), Js('enice'), Js('esia'), Js('estra'), Js('estris'), Js('gea'), Js('gone'), Js('haedra'), Js('hyia'), Js('ippe'), Js('isbe'), Js('ises'), Js('leia'), Js('lene'), Js('lete'), Js('liope'), Js('lipe'), Js('lyte'), Js('mache'), Js('meia'), Js('nache'), Js('nara'), Js('neira'), Js('nestra'), Js('nia'), Js('nippe'), Js('noe'), Js('nousa'), Js('ope'), Js('padia'), Js('pedo'), Js('peia'), Js('pesia'), Js('phale'), Js('pyle'), Js('pyte'), Js('rera'), Js('reto'), Js('roe'), Js('scyra'), Js('ses'), Js('sippe'), Js('sose'), Js('tane'), Js('thippe'), Js('thoe'), Js('thya'), Js('thye'), Js('thyia'), Js('ybe'), Js('yche'), Js('yle'), Js('yme'), Js('yne'), Js('yope'), Js('yrbe'), Js('ytie')]))
pass
pass


# Add lib to the module scope
amazonNames = var.to_python()