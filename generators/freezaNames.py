__all__ = ['freezaNames']

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
            if (var.get('i')<Js(4.0)):
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
var.put('names1', Js([Js('Arcti'), Js('Arctic'), Js('Arctico'), Js('Chill'), Js('Chilla'), Js('Chilley'), Js('Chills'), Js('Colde'), Js('Coled'), Js('Coola'), Js('Coolio'), Js('Forost'), Js('Freez'), Js('Freeze'), Js('Fridge'), Js('Fridged'), Js('Frigi'), Js('Frigid'), Js('Frosbyte'), Js('Fross'), Js('Frost'), Js('Frostbite'), Js('Froza'), Js('Froze'), Js('Frozen'), Js('Hail'), Js('Hale'), Js('Ice'), Js('Icecube'), Js('Icequ'), Js('Iceqube'), Js('Icey'), Js('Icicle'), Js('Kold'), Js('Kool'), Js('Nippy'), Js('Pola'), Js('Polara'), Js('Polaro'), Js('Qube'), Js('Rime'), Js('Ryme'), Js('Sano'), Js('Sanow'), Js('Shiver'), Js('Shivera'), Js('Shivero'), Js('Snow'), Js('Wintera'), Js('Wintrey'), Js('Yce'), Js('Ycicle')]))
var.put('names2', Js([Js('Andarin'), Js('Appel'), Js('Appine'), Js('Apple'), Js('Aprico'), Js('Apricot'), Js('Avoca'), Js('Avocado'), Js('Bana'), Js('Banan'), Js('Berry'), Js('Blueber'), Js('Cantalou'), Js('Cantaloupe'), Js('Cheely'), Js('Cherr'), Js('Cherry'), Js('Citro'), Js('Citron'), Js('Citrone'), Js('Coconu'), Js('Coconut'), Js('Conut'), Js('Cranber'), Js('Cranberry'), Js('Crant'), Js('Curran'), Js('Currant'), Js('Darin'), Js('Doorian'), Js('Duria'), Js('Durian'), Js('Emil'), Js('Fig'), Js('Figg'), Js('Gerine'), Js('Gomang'), Js('Goose'), Js('Gooseber'), Js('Gooseberry'), Js('Granate'), Js('Grape'), Js('Grapefru'), Js('Grapefruit'), Js('Grapefrute'), Js('Graype'), Js('Guav'), Js('Guava'), Js('Iwik'), Js('Kinpum'), Js('Kiwi'), Js('Kokonut'), Js('Kuava'), Js('Kumqua'), Js('Kumquad'), Js('Kumquat'), Js('Lamone'), Js('Lemon'), Js('Lemone'), Js('Lime'), Js('Lych'), Js('Lychee'), Js('Lyme'), Js('Mandar'), Js('Mandarin'), Js('Mango'), Js('Mato'), Js('Mellon'), Js('Melo'), Js('Melon'), Js('Melone'), Js('Nectari'), Js('Nectarine'), Js('Nilla'), Js('Nolem'), Js('Nomel'), Js('Notric'), Js('Odacova'), Js('Ognam'), Js('Orange'), Js('Orango'), Js('Otamot'), Js('Pallum'), Js('Papaw'), Js('Papay'), Js('Papaya'), Js('Pawpaw'), Js('Paya'), Js('Peach'), Js('Peache'), Js('Pear'), Js('Peare'), Js('Peech'), Js('Peere'), Js('Pine'), Js('Pineap'), Js('Pineapple'), Js('Plum'), Js('Pomegra'), Js('Pomegranate'), Js('Pomel'), Js('Pomelo'), Js('Pricot'), Js('Pump'), Js('Pumpki'), Js('Pumpkin'), Js('Qiwi'), Js('Quiwi'), Js('Rango'), Js('Rasber'), Js('Raspberry'), Js('Rasperry'), Js('Rhubar'), Js('Rhubarb'), Js('Rubar'), Js('Strawber'), Js('Strawberry'), Js('Taloupe'), Js('Tanger'), Js('Tangeri'), Js('Tangerine'), Js('Tarine'), Js('Toma'), Js('Tomato'), Js('Vanilla'), Js('Vocado')]))
pass
pass


# Add lib to the module scope
freezaNames = var.to_python()