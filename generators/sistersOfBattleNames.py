__all__ = ['sistersOfBattleNames']

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
var.put('nm1', Js([Js('Agn'), Js('Al'), Js('Alic'), Js('Am'), Js('An'), Js('Ar'), Js('Arab'), Js('Asp'), Js('Bell'), Js('Bren'), Js('Brig'), Js('Bris'), Js('Cel'), Js('Celest'), Js('Chr'), Js('Chris'), Js('Chrism'), Js('Dec'), Js('Diss'), Js('Dor'), Js('Dyl'), Js('Ell'), Js('Ephr'), Js('Ess'), Js('Est'), Js('Gal'), Js('Gell'), Js('Gin'), Js('Gwyn'), Js('Hann'), Js('Hel'), Js('Hen'), Js('Hild'), Js('Imm'), Js('Immac'), Js('Ion'), Js('Ish'), Js('Jen'), Js('Jess'), Js('Josm'), Js('Jul'), Js('Kat'), Js('Kath'), Js('Kess'), Js('Kyl'), Js('Let'), Js('Leth'), Js('Luc'), Js('Lyn'), Js('Mesh'), Js('Min'), Js('Mir'), Js('Mor'), Js('Og'), Js('Ol'), Js('Oliv'), Js('Osh'), Js('Pal'), Js('Palm'), Js('Phan'), Js('Prax'), Js('Res'), Js('Rhian'), Js('Rhiann'), Js('Rienn'), Js('Sab'), Js('Sabr'), Js('Sar'), Js('Sel'), Js('Seph'), Js('Silv'), Js('Syl'), Js('Venn'), Js('Ver'), Js('Viss'), Js('Vyl')]))
var.put('nm2', Js([Js('a'), Js('ael'), Js('ais'), Js('ana'), Js('ane'), Js('anon'), Js('ata'), Js('atea'), Js('arya'), Js('ahla'), Js('e'), Js('ea'), Js('edes'), Js('ella'), Js('ena'), Js('enta'), Js('erina'), Js('erine'), Js('es'), Js('enya'), Js('i'), Js('ia'), Js('iael'), Js('iah'), Js('icia'), Js('ien'), Js('ima'), Js('ina'), Js('ine'), Js('ira'), Js('iro'), Js('isma'), Js('itta'), Js('ity'), Js('iya'), Js('on'), Js('one'), Js('osha'), Js('oya'), Js('olis'), Js('oia'), Js('onya'), Js('olla'), Js('o'), Js('oris'), Js('ora'), Js('ulata'), Js('uya'), Js('une'), Js('uah'), Js('una')]))
pass
pass


# Add lib to the module scope
sistersOfBattleNames = var.to_python()