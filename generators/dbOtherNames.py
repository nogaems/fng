__all__ = ['dbOtherNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('names', var.get('names1').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', var.get('names2').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Lala'), Js('Abra'), Js('Ala'), Js('Alaka'), Js('Bim'), Js('Braca'), Js('Bracada'), Js('Cada'), Js('Cadabra'), Js('Dabra'), Js('Eppe'), Js('Flam'), Js('Flim'), Js('Gobble'), Js('Gobbledee'), Js('Gook'), Js('Hello'), Js('Hillo'), Js('Hocu'), Js('Hocus'), Js('Hollo'), Js('Hum'), Js('Jumbo'), Js('Kakke'), Js('Kazam'), Js('Laka'), Js('Mani'), Js('Mumbo'), Js('Ocus'), Js('Om'), Js('Padme'), Js('Peppe'), Js('Pocu'), Js('Pocus'), Js('Pow'), Js('Presto'), Js('Sala'), Js('Same'), Js('Sesa'), Js('Sesame'), Js('Shazam'), Js('Sim'), Js('Wow'), Js('Zam'), Js('Zik'), Js('Zizzi'), Js('Zuzzy')]))
var.put('names2', Js([Js('Aioli'), Js('Anise'), Js('Basil'), Js('Bay'), Js('Celery'), Js('Chili'), Js('Chutney'), Js('Cilantro'), Js('Cinnamon'), Js('Clove'), Js('Coriander'), Js('Cream'), Js('Cumin'), Js('Dashi'), Js('Dressing'), Js('Fennel'), Js('Guacamole'), Js('Jasmine'), Js('Juniper'), Js('Ketchup'), Js('Lemon'), Js('Lime'), Js('Mace'), Js('Marmite'), Js('Mash'), Js('Mayo'), Js('Mint'), Js('Miso'), Js('Naise'), Js('Nutmeg'), Js('Oil'), Js('Onion'), Js('Oregano'), Js('Paprika'), Js('Parsley'), Js('Pepper'), Js('Peppermint'), Js('Pesto'), Js('Piccalilli'), Js('Pickle'), Js('Ponzu'), Js('Radish'), Js('Relish'), Js('Rice'), Js('Riyaki'), Js('Rosemary'), Js('Safe'), Js('Saffron'), Js('Salsa'), Js('Sambal'), Js('Sauce'), Js('Sesame'), Js('Shichimi'), Js('Sichuan'), Js('Soy'), Js('Syrup'), Js('Tarragon'), Js('Tartar'), Js('Teriya'), Js('Teriyaki'), Js('Thyme'), Js('Turmeric'), Js('Tzatziki'), Js('Vanilla'), Js('Wasabi')]))
pass
pass


# Add lib to the module scope
dbOtherNames = var.to_python()