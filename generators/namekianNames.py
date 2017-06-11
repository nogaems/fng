__all__ = ['namekianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('names', var.get('names1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Abut'), Js('Accordi'), Js('Alsetto'), Js('Amisen'), Js('Andoli'), Js('Andolin'), Js('Armon'), Js('Armoni'), Js('Armonic'), Js('Arp'), Js('Astropo'), Js('Axopho'), Js('Azoo'), Js('Balalai'), Js('Banji'), Js('Banjo'), Js('Barito'), Js('Baritone'), Js('Base'), Js('Bass'), Js('Bassoo'), Js('Bassoon'), Js('Batu'), Js('Carina'), Js('Cello'), Js('Clarin'), Js('Cordi'), Js('Cordio'), Js('Cordion'), Js('Didger'), Js('Didgeri'), Js('Dolin'), Js('Eleluku'), Js('Escar'), Js('Escargo'), Js('Fiddel'), Js('Fiddle'), Js('Fidel'), Js('Flute'), Js('Gastro'), Js('Gastropo'), Js('Geridoo'), Js('Guitar'), Js('Guitara'), Js('Guls'), Js('Guytar'), Js('Harmo'), Js('Harmon'), Js('Harp'), Js('Horn'), Js('Horne'), Js('Iolin'), Js('Iren'), Js('Istle'), Js('Itar'), Js('Kazoo'), Js('Keyta'), Js('Keytar'), Js('Kotai'), Js('Kulele'), Js('Lalaika'), Js('Larinet'), Js('Lians'), Js('Lire'), Js('Lophone'), Js('Lug'), Js('Lusc'), Js('Lute'), Js('Lyre'), Js('Mando'), Js('Mandolin'), Js('Mollus'), Js('Mollusc'), Js('Murd'), Js('Neris'), Js('Oboe'), Js('Oboo'), Js('Ocari'), Js('Ocarin'), Js('Okiat'), Js('Ollusc'), Js('Oozak'), Js('Oragan'), Js('Organ'), Js('Organa'), Js('Orn'), Js('Piani'), Js('Picco'), Js('Piyano'), Js('Prano'), Js('Ratis'), Js('Riangle'), Js('Rombon'), Js('Rombone'), Js('Rumpet'), Js('Saxo'), Js('Saxofo'), Js('Scargo'), Js('Scargot'), Js('Senshami'), Js('Shami'), Js('Sirren'), Js('Sitar'), Js('Snai'), Js('Snayle'), Js('Sopra'), Js('Sopran'), Js('Sulug'), Js('Taiko'), Js('Tooba'), Js('Triango'), Js('Trombo'), Js('Trombon'), Js('Tropod'), Js('Trump'), Js('Trumpe'), Js('Tuba'), Js('Ukule'), Js('Ukulel'), Js('Ukulele'), Js('Viol'), Js('Violin'), Js('Vuvu'), Js('Vuzela'), Js('Whist'), Js('Xophone'), Js('Xylo'), Js('Xylofo'), Js('Zooka')]))
pass
pass


# Add lib to the module scope
namekianNames = var.to_python()