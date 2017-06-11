__all__ = ['unsulliedNames']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', ((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Ash'), Js('Awful'), Js('Bad'), Js('Black'), Js('Blue'), Js('Bottom'), Js('Broken'), Js('Brown'), Js('Cheap'), Js('Dirt'), Js('Dirty'), Js('Down'), Js('Drab'), Js('Dreck'), Js('Dust'), Js('Feeble'), Js('Filthy'), Js('Foul'), Js('Fragile'), Js('Frail'), Js('Garbage'), Js('Grease'), Js('Grey'), Js('Grim'), Js('Grime'), Js('Grisly'), Js('Gross'), Js('Grotesque'), Js('Hideous'), Js('Horrid'), Js('Ill'), Js('Inferior'), Js('Infirm'), Js('Junk'), Js('Lesser'), Js('Little'), Js('Lousy'), Js('Low'), Js('Meager'), Js('Measly'), Js('Mediocre'), Js('Menial'), Js('Messy'), Js('Minor'), Js('Monstrous'), Js('Muck'), Js('Mud'), Js('Murky'), Js('Nasty'), Js('Paltry'), Js('Peon'), Js('Pesky'), Js('Poor'), Js('Puny'), Js('Raunchy'), Js('Red'), Js('Repulsive'), Js('Revolting'), Js('Sad'), Js('Scant'), Js('Scrap'), Js('Shame'), Js('Shoddy'), Js('Sick'), Js('Slag'), Js('Slimey'), Js('Slop'), Js('Smut'), Js('Soil'), Js('Soot'), Js('Stink'), Js('Tiny'), Js('Trash'), Js('Trashy'), Js('Trivial'), Js('Ugly'), Js('Vile'), Js('Waste'), Js('Worthless'), Js('Wracked'), Js('Wretched')]))
var.put('names2', Js([Js('Ant'), Js('Beetle'), Js('Bug'), Js('Crawler'), Js('Creep'), Js('Creeper'), Js('Cricket'), Js('Curse'), Js('Dog'), Js('Flea'), Js('Fly'), Js('Frog'), Js('Grub'), Js('Insect'), Js('Larva'), Js('Leech'), Js('Maggot'), Js('Mite'), Js('Mole'), Js('Mongrel'), Js('Moth'), Js('Mouse'), Js('Mule'), Js('Mutt'), Js('Nit'), Js('Parasite'), Js('Pest'), Js('Pig'), Js('Rabbit'), Js('Rat'), Js('Roach'), Js('Rodent'), Js('Scrub'), Js('Shrimp'), Js('Snail'), Js('Spider'), Js('Squirmer'), Js('Termite'), Js('Tick'), Js('Toad'), Js('Vermin'), Js('Weasel'), Js('Weevil'), Js('Whelp'), Js('Worm'), Js('Wriggler'), Js('Runt'), Js('Slug'), Js('Oaf'), Js('Prawn'), Js('Louse'), Js('Skunk')]))
pass
pass


# Add lib to the module scope
unsulliedNames = var.to_python()