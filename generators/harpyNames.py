__all__ = ['harpyNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
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
var.put('nm1', Js([Js('Aell'), Js('Aer'), Js('Air'), Js('Ar'), Js('Av'), Js('Bel'), Js('Ber'), Js('Caell'), Js('Cal'), Js('Cec'), Js('Cel'), Js('Crel'), Js('Cyl'), Js('Der'), Js('Des'), Js('Dhon'), Js('Dhyl'), Js('Dor'), Js('Dys'), Js('Faen'), Js('Fean'), Js('Fer'), Js('Flor'), Js('Glor'), Js('God'), Js('Gwyn'), Js('Gyl'), Js('Hell'), Js('Hem'), Js('Heph'), Js('Hyn'), Js('Hyst'), Js('Ial'), Js('Ier'), Js('Ill'), Js('Ion'), Js('Laer'), Js('Lin'), Js('Lor'), Js('Lyn'), Js('Lyph'), Js('Lys'), Js('Lyv'), Js('Maer'), Js('Men'), Js('Mes'), Js('Mor'), Js('Myn'), Js('Nel'), Js('Nell'), Js('Neph'), Js('Ner'), Js('Nor'), Js('Nyph'), Js('Nyr'), Js('Nys'), Js('Oc'), Js('Ocyp'), Js('Oll'), Js('Or'), Js('Orin'), Js('Pel'), Js('Per'), Js('Phel'), Js('Phlor'), Js('Phyn'), Js('Pod'), Js('Sav'), Js('Seph'), Js('Sol'), Js('Syl'), Js('Syr'), Js('Taer'), Js('Ten'), Js('Thel'), Js('Ther'), Js('Thyl'), Js('Tyl'), Js('Typh'), Js('Tyr'), Js('Tyv'), Js('Uem'), Js('Ur'), Js('Uv'), Js('Vael'), Js('Vel'), Js('Ver'), Js('Vol'), Js('Vyn'), Js('Xel'), Js('Xir'), Js('Xyl'), Js('Xyn'), Js('Yen'), Js('Yes'), Js('Yor'), Js('Zean'), Js('Zel'), Js('Zeph'), Js('Zer')]))
var.put('nm2', Js([Js('a'), Js('aene'), Js('aeno'), Js('alin'), Js('alis'), Js('alle'), Js('ane'), Js('aphe'), Js('aphine'), Js('ara'), Js('arge'), Js('aria'), Js('ase'), Js('asha'), Js('asis'), Js('ea'), Js('eano'), Js('eanor'), Js('efis'), Js('elle'), Js('ena'), Js('enne'), Js('eo'), Js('ephise'), Js('era'), Js('erin'), Js('eris'), Js('ete'), Js('ethe'), Js('evis'), Js('ia'), Js('ial'), Js('ialle'), Js('iana'), Js('iane'), Js('iara'), Js('ie'), Js('ielle'), Js('iene'), Js('inis'), Js('inore'), Js('iphis'), Js('iris'), Js('is'), Js('ise'), Js('o'), Js('oah'), Js('oe'), Js('oelle'), Js('oene'), Js('oinne'), Js('ola'), Js('one'), Js('onia'), Js('ophine'), Js('ophis'), Js('ora'), Js('orena'), Js('oris'), Js('oya'), Js('ya'), Js('yana'), Js('ylia'), Js('ylis'), Js('yne'), Js('ynea'), Js('ynne'), Js('ynore'), Js('yore'), Js('yphe'), Js('yre'), Js('yrea'), Js('yris'), Js('ys'), Js('yth')]))
pass
pass


# Add lib to the module scope
harpyNames = var.to_python()