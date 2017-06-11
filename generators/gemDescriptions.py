__all__ = ['gemDescriptions']

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
    var.registers(['nm1', 'rnd15', 'rnd11', 'rnd8', 'name', 'nm3', 'rnd14', 'name3', 'nm2', 'rnd2', 'br', 'name2', 'name4', 'rnd5', 'nm5', 'rnd4', 'rnd7', 'result', 'nm6', 'rnd6', 'rnd13', 'nm4', 'rnd3', 'nm8', 'name5', 'rnd16', 'rnd10', 'rnd9', 'rnd12', 'rnd1'])
    var.put('nm1', Js([Js('Agate'), Js('Agate Geode'), Js('Alexandrite'), Js('Almandine Garnet'), Js('Amazonite'), Js('Amethyst'), Js('Ametrine'), Js('Ammolite'), Js('Andalusite'), Js('Apatite'), Js('Aquamarine'), Js('Aventurine'), Js('Axinite'), Js('Beryl'), Js('Bloodstone'), Js('Boulder Opal'), Js('Calcite'), Js('Carnelian'), Js('Cassiterite'), Js('Charoite'), Js('Chrome Diopside'), Js('Citrine'), Js('Clinohumite'), Js('Diamond'), Js('Emerald'), Js('Enstatite'), Js('Fire Agate'), Js('Fire Opal'), Js('Fluorite'), Js('Hematite'), Js('Hiddenite'), Js('Howlite'), Js('Iolite'), Js('Jasper'), Js('Kyanite'), Js('Lapis Lazuli'), Js('Malachite'), Js('Mali Garnet'), Js('Melanite'), Js('Moldavite'), Js('Moonstone'), Js('Morganite'), Js('Moss Opal'), Js('Nuummite'), Js('Obsidian'), Js('Onyx'), Js('Opal'), Js('Peridot'), Js('Prehnite'), Js('Pyrope Garnet'), Js('Quartz'), Js('Rainbow Moonstone'), Js('Rainbow Pyrite'), Js('Rhodochrosite'), Js('Rhodolite Garnet'), Js('Rhodonite'), Js('Rose Quartz'), Js('Ruby'), Js('Sapphire'), Js('Scapolite'), Js('Seraphinite'), Js('Serpentine'), Js('Snowflake Obsidian'), Js('Sodalite'), Js('Sphalerite'), Js('Sphene'), Js('Spinel'), Js('Star Diopside'), Js('Star Garnet'), Js('Star Ruby'), Js('Star Sapphire'), Js('Sugilite'), Js('Sunstone'), Js('Tanzanite'), Js("Tiger's Eye"), Js('Topaz'), Js('Tourmaline'), Js('Turquoise'), Js('Verdite'), Js('Zircon')]))
    var.put('nm2', Js([Js('an antique cushion'), Js('a baguette'), Js('a brilliant'), Js('a briolette'), Js('a cabochon'), Js('a cushion'), Js('an emerald'), Js('a heart'), Js('a kite'), Js('a marquise'), Js('an octagon'), Js('an oval'), Js('a pear'), Js('a princess'), Js('a radiant'), Js('a round'), Js('a royal'), Js('a square'), Js('a triangle'), Js('a trillion')]))
    var.put('nm3', Js([Js('bean'), Js('blueberry'), Js('fig'), Js('fist'), Js('grape'), Js('hazelnut'), Js('kumquat'), Js('lemon'), Js('lentil'), Js('lime'), Js('pea'), Js('peanut'), Js('strawberry'), Js('walnut')]))
    var.put('nm4', Js([Js('average'), Js('decent'), Js('excellent'), Js('fair'), Js('fairly decent'), Js('fairly poor'), Js('fairly rough'), Js('fine'), Js('great'), Js('inferior'), Js('magnificent'), Js('mediocre'), Js('near flawless'), Js('outstanding'), Js('poor'), Js('premium'), Js('presentable'), Js('pristine'), Js('reasonable'), Js('rough'), Js('rugged'), Js('superb'), Js('supreme'), Js('terrific')]))
    var.put('nm5', Js([Js('barely sought after'), Js('decently popular'), Js('fairly popular'), Js('in average demand'), Js('in decent demand'), Js('in fairly high demand'), Js('in low demand'), Js('in very high demand'), Js('not that popular'), Js('not very sought after'), Js('often ignored'), Js('often in high demand'), Js('often quite popular'), Js('quite unpopular'), Js('rarely sought after')]))
    var.put('nm6', Js([Js('an incredibly common'), Js('a very common'), Js('a fairly common'), Js('a fairly uncommon'), Js('a quite uncommon'), Js('a very uncommon'), Js('a fairly rare'), Js('a quite rare'), Js('a very rare'), Js('an incredibly rare')]))
    var.put('nm8', Js([Js('defensive weapon'), Js('offensive weapon'), Js('defensive spell focus'), Js('offensive spell focus'), Js('beneficial spell focus'), Js('offensive weapon enhancement'), Js('defensive weapon enhancement'), Js('defensive spell focus enhancement'), Js('offensive spell focus enhancement'), Js('beneficial spell focus enhancement'), Js('defensive artifact'), Js('offensive artifact'), Js('defensive artifact enhancement'), Js('offensive artifact enhancement'), Js('defensive jewelry'), Js('offensive jewelry'), Js('defensive jewelry enhancement'), Js('offensive jewelry enhancement')]))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    var.put('rnd16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    var.put('name', ((((((((((((Js('This ')+var.get('nm1').get(var.get('rnd1')))+Js(' with '))+var.get('nm2').get(var.get('rnd2')))+Js(' cut and the size of a '))+var.get('nm3').get(var.get('rnd3')))+Js(' is in '))+var.get('nm4').get(var.get('rnd4')))+Js(' condition. These gems are '))+var.get('nm5').get(var.get('rnd5')))+Js(", but they're "))+var.get('nm6').get(var.get('rnd6')))+Js(' gemstone species.')))
    var.put('name2', ((((Js("It's said these gems contain ")+var.get('nm7').get(var.get('rnd7')))+Js(' properties which make for a great '))+var.get('nm8').get(var.get('rnd8')))+Js('.')))
    var.put('name3', Js('-----------------------------------------------------------------------------------------------------------------------------'))
    var.put('name4', ((((((((((((Js('This ')+var.get('nm1').get(var.get('rnd9')))+Js(' with '))+var.get('nm2').get(var.get('rnd10')))+Js(' cut and the size of a '))+var.get('nm3').get(var.get('rnd11')))+Js(' is in '))+var.get('nm4').get(var.get('rnd12')))+Js(' condition. These gems are '))+var.get('nm5').get(var.get('rnd13')))+Js(", but they're "))+var.get('nm6').get(var.get('rnd14')))+Js(' gemstone species.')))
    var.put('name5', ((((Js("It's said these gems contain ")+var.get('nm7').get(var.get('rnd15')))+Js(' properties which make for a great '))+var.get('nm8').get(var.get('rnd16')))+Js('.')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(6.0)):
        try:
            pass
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
gemDescriptions = var.to_python()