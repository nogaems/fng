__all__ = ['starTrekCaitians']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js("C'R"), Js("C'T"), Js("C'"), Js("C'M"), Js("C'N"), Js("C'Tr"), Js('Cr'), Js("Cr'"), Js('Cs'), Js("H'R"), Js("H'M"), Js("H'N"), Js("H'"), Js('Hr'), Js('Hs'), Js('Kr'), Js("K'R"), Js("K'M"), Js("K'N"), Js("K'Gr"), Js("K'Tr"), Js("M'Gr"), Js("M'M"), Js("M'N"), Js("M'R"), Js("M'T"), Js("M'Tr"), Js("M'"), Js('Mr'), Js("Mr'"), Js("P'R"), Js("P'M"), Js("P'N"), Js("P'Gr"), Js('Pr'), Js("P'T"), Js("R'M"), Js('Rr'), Js("R'R"), Js("R'N"), Js("R'T"), Js("R'Tr"), Js("S'T"), Js("S'Gr"), Js("S'M"), Js("S'N"), Js("S'R"), Js("Sh'"), Js('Sr'), Js('Sh'), Js("Sr'")]))
var.put('nm2', Js([Js('aal'), Js('aarra'), Js('aia'), Js('aiarr'), Js('ala'), Js('all'), Js('aow'), Js('ara'), Js('arash'), Js('arr'), Js('ash'), Js('asha'), Js('ashar'), Js('asi'), Js('au'), Js('earr'), Js('eia'), Js('elar'), Js('ell'), Js('elle'), Js('era'), Js('erah'), Js('eras'), Js('erl'), Js('erow'), Js('err'), Js('esint'), Js('esirr'), Js('ess'), Js('ia'), Js('iarr'), Js('ierr'), Js('iia'), Js('ill'), Js('ille'), Js('ira'), Js('iras'), Js('iri'), Js('irl'), Js('irr'), Js('isarr'), Js('ish'), Js('isil'), Js('iss'), Js('oa'), Js('oaw'), Js('oia'), Js('ol'), Js('oll'), Js('ora'), Js('orash'), Js('oren'), Js('ori'), Js('orish'), Js('orr'), Js('orri'), Js('osin'), Js('ow'), Js('uaw'), Js('ular'), Js('ulish'), Js('ull'), Js('uran'), Js('urin'), Js('uris'), Js('urr'), Js('urs'), Js('us'), Js('usar'), Js('uul'), Js('uur'), Js('uuras'), Js('uuri')]))
pass
pass


# Add lib to the module scope
starTrekCaitians = var.to_python()