__all__ = ['bahmiNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['names1', 'names2', 'tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names1', Js([Js('Altan'), Js('Bat'), Js('Bayar'), Js('Bolor'), Js('Ene'), Js('Enkh'), Js('Erdene'), Js('Gan'), Js('Gerel'), Js('Hon'), Js('Khün'), Js('Khen'), Js('Khon'), Js('Mönkh'), Js('Medekh'), Js('Munkh'), Js('Muuno'), Js('Naran'), Js('Ner'), Js('Od'), Js('Ogt'), Js('Oyun'), Js('Oyuun'), Js('Saran'), Js('Sertuun'), Js('Solon'), Js('Ter'), Js('Uran')]))
        var.put('names2', Js([Js('bileg'), Js('bish'), Js('chimeg'), Js('güi'), Js('gerel'), Js('go'), Js('gorzol'), Js('gorzul'), Js('jargal'), Js('khoi'), Js('maa'), Js('tsatsral'), Js('tsetseg'), Js('tungalag'), Js('tuyaa'), Js('val'), Js('zorig')]))
    else:
        var.put('names1', Js([Js('Bat'), Js('Batu'), Js('Chin'), Js('Chuluun'), Js('Ene'), Js('Enkh'), Js('Gan'), Js('Khün'), Js('Khen'), Js('Mönkh'), Js('Medekh'), Js('Munoo'), Js('Naran'), Js('Ner'), Js('Ogt'), Js('Otgon'), Js('Sühk'), Js('Tömör'), Js('Ter'), Js('Yul')]))
        var.put('names2', Js([Js('baatar'), Js('bat'), Js('bataar'), Js('bayar'), Js('bish'), Js('bold'), Js('güi'), Js('gis'), Js('jargal'), Js('khan'), Js('khoi'), Js('saikhan'), Js('sukh'), Js('tulga'), Js('zorig')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', (var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
bahmiNames = var.to_python()