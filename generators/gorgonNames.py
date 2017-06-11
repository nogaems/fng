__all__ = ['gorgonNames']

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
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4'))))
                else:
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    if (var.get('rnd3')>Js(26.0)):
                        while (var.get('rnd5')>Js(26.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd4'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('ch'), Js('chr'), Js('d'), Js('h'), Js('k'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('sth'), Js('th'), Js('x'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('eia'), Js('ei'), Js('eu'), Js('ae'), Js('ya'), Js('ai'), Js('ia')]))
var.put('nm3', Js([Js('d'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('x'), Js('v'), Js('z'), Js('d'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('x'), Js('v'), Js('z'), Js('d'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('x'), Js('v'), Js('z'), Js('dn'), Js('dr'), Js('gg'), Js('gn'), Js('kt'), Js('lc'), Js('ld'), Js('mbr'), Js('nc'), Js('ndr'), Js('nt'), Js('nth'), Js('rd'), Js('rl'), Js('rr'), Js('sc'), Js('sd'), Js('sn'), Js('sp'), Js('st'), Js('str'), Js('th'), Js('tt')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('ea'), Js('ia'), Js('y')]))
var.put('nm5', Js([Js('aemon'), Js('aenon'), Js('aeon'), Js('aestus'), Js('aeus'), Js('agos'), Js('aios'), Js('anes'), Js('anos'), Js('antos'), Js('aon'), Js('arus'), Js('as'), Js('ates'), Js('atos'), Js('aumas'), Js('eas'), Js('eidon'), Js('er'), Js('erion'), Js('erus'), Js('es'), Js('etheus'), Js('etus'), Js('eus'), Js('ias'), Js('ibos'), Js('ion'), Js('ios'), Js('is'), Js('iton'), Js('ius'), Js('o'), Js('oeis'), Js('oeus'), Js('olus'), Js('on'), Js('onos'), Js('or'), Js('os'), Js('oteus'), Js('otos'), Js('otus'), Js('ous'), Js('us'), Js('yrus'), Js('ys'), Js('ytion')]))
pass
pass


# Add lib to the module scope
gorgonNames = var.to_python()