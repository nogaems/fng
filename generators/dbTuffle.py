__all__ = ['dbTuffle']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'result'])
    var.put('nm1', Js([Js('Amba'), Js('Ango'), Js('Anno'), Js('Appri'), Js('Apri'), Js('Ara'), Js('Atemo'), Js('Azara'), Js('Babacoco'), Js('Baco'), Js('Bacu'), Js('Bananan'), Js('Banna'), Js('Barella'), Js('Blica'), Js('Boloma'), Js('Buljam'), Js('Buram'), Js('Butan'), Js('Cala'), Js('Callama'), Js('Canta'), Js('Cawwes'), Js('Cerola'), Js('Cerole'), Js('Chari'), Js('Charrie'), Js('Chayo'), Js('Cheelai'), Js('Cheri'), Js('Chuello'), Js('Cito'), Js('Clemmen'), Js('Cocon'), Js('Connu'), Js('Conut'), Js('Cote'), Js('Cotejo'), Js('Craba'), Js('Cranbe'), Js('Cupari'), Js('Curi'), Js('Dila'), Js('Dillagra'), Js('Dirra'), Js('Drian'), Js('Durin'), Js('Elon'), Js('Embli'), Js('Feeg'), Js('Firkaf'), Js('Firri'), Js('Fousa'), Js('Frui'), Js('Galis'), Js('Gallia'), Js('Ganlon'), Js('Gava'), Js('Gojee'), Js('Goma'), Js('Grana'), Js('Granadi'), Js('Grapis'), Js('Guara'), Js('Guav'), Js('Guavis'), Js('Guavvan'), Js('Gunun'), Js('Jambully'), Js('Jubbish'), Js('Jubeju'), Js('Jubu'), Js('Juju'), Js('Kaffi'), Js('Larel'), Js('Limbi'), Js('Limo'), Js('Lonme'), Js('Loquish'), Js('Loupe'), Js('Maboro'), Js('Maray'), Js('Marin'), Js('Marind'), Js('Meelo'), Js('Meelon'), Js('Melain'), Js('Mello'), Js('Melo'), Js('Melopo'), Js('Menti'), Js('Merron'), Js('Monga'), Js('Monlee'), Js('Moring'), Js('Moya'), Js('Moyaa'), Js('Moyate'), Js('Nabana'), Js('Nadila'), Js('Nadilgra'), Js('Nadira'), Js('Netche'), Js('Nona'), Js('Nonaan'), Js('Papaw'), Js('Papayata'), Js('Pari'), Js('Pawpa'), Js('Paya'), Js('Payapa'), Js('Payata'), Js('Pearish'), Js('Peejee'), Js('Pegra'), Js('Peqi'), Js('Per'), Js('Persim'), Js('Pilly'), Js('Pimmello'), Js('Pitay'), Js('Pote'), Js('Potesa'), Js('Pricot'), Js('Pulum'), Js('Pulume'), Js('Pumme'), Js('Qincee'), Js('Quatum'), Js('Quipe'), Js('Quira'), Js('Raime'), Js('Ranagua'), Js('Rangee'), Js('Ranji'), Js('Raza'), Js('Razza'), Js('Riandu'), Js('Rime'), Js('Rola'), Js('Rongan'), Js('Roupe'), Js('Ruity'), Js('Rybe'), Js('Simper'), Js('Talou'), Js('Taloup'), Js('Tama'), Js('Tang'), Js('Tara'), Js('Tarato'), Js('Tareen'), Js('Tarine'), Js('Taya'), Js('Tayapi'), Js('Tecojo'), Js('Temoya'), Js('Tohui'), Js('Vagua'), Js('Vaqua'), Js('Wesha'), Js('Wiki'), Js('Woran'), Js('Yapa'), Js('Yote'), Js('Zara')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
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
dbTuffle = var.to_python()