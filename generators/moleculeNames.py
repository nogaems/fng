__all__ = ['moleculeNames']

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
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd8'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd8')))+var.get('nm4').get(var.get('rnd9')))+var.get('nm6').get(var.get('rnd10'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('deca'), Js('di'), Js('duo'), Js('hepta'), Js('hexa'), Js('hydra'), Js('hydro'), Js('hypo'), Js('iso'), Js('mono'), Js('octa'), Js('penta'), Js('tetra'), Js('tri')]))
var.put('nm2', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('c'), Js('ch'), Js('chl'), Js('chr'), Js('cl'), Js('d'), Js('f'), Js('fl'), Js('fr'), Js('g'), Js('gl'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('pl'), Js('pr'), Js('ps'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('sp'), Js('st'), Js('str'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('w'), Js('z')]))
var.put('nm4', Js([Js('b'), Js('bd'), Js('br'), Js('bsc'), Js('c'), Js('cc'), Js('cch'), Js('ch'), Js('chl'), Js('chr'), Js('cl'), Js('cr'), Js('ct'), Js('d'), Js('dr'), Js('dv'), Js('f'), Js('ff'), Js('fl'), Js('g'), Js('gl'), Js('gn'), Js('h'), Js('k'), Js('l'), Js('lb'), Js('lc'), Js('lch'), Js('ldr'), Js('lf'), Js('lg'), Js('ll'), Js('lp'), Js('lph'), Js('lpr'), Js('lt'), Js('m'), Js('mm'), Js('mn'), Js('mph'), Js('n'), Js('nc'), Js('nd'), Js('nh'), Js('nk'), Js('nn'), Js('ns'), Js('nt'), Js('nth'), Js('nthr'), Js('nz'), Js('p'), Js('ph'), Js('phth'), Js('pp'), Js('pr'), Js('ps'), Js('pt'), Js('pth'), Js('q'), Js('rb'), Js('rchl'), Js('rd'), Js('rf'), Js('rg'), Js('rh'), Js('rk'), Js('rl'), Js('rn'), Js('rph'), Js('rq'), Js('rr'), Js('rrh'), Js('rs'), Js('rt'), Js('rv'), Js('s'), Js('sc'), Js('sg'), Js('sp'), Js('sph'), Js('spl'), Js('ss'), Js('st'), Js('str'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ae'), Js('aa'), Js('ai'), Js('au'), Js('ea'), Js('ee'), Js('ei'), Js('eo'), Js('eu'), Js('ia'), Js('ie'), Js('io'), Js('iu'), Js('ua'), Js('ue'), Js('ui'), Js('ya'), Js('ye'), Js('yo')]))
var.put('nm6', Js([Js('aene'), Js('an'), Js('ane'), Js('ar'), Js('as'), Js('ase'), Js('asy'), Js('ate'), Js('eide'), Js('ein'), Js('eite'), Js('el'), Js('ene'), Js('er'), Js('ial'), Js('id'), Js('ide'), Js('iene'), Js('in'), Js('ine'), Js('iol'), Js('ite'), Js('ium'), Js('oate'), Js('ocin'), Js('ol'), Js('ole'), Js('on'), Js('one'), Js('or'), Js('ose'), Js('ox'), Js('oxin'), Js('uene'), Js('um'), Js('ur'), Js('ycin'), Js('yde'), Js('yl'), Js('yme'), Js('yn')]))
pass
pass


# Add lib to the module scope
moleculeNames = var.to_python()