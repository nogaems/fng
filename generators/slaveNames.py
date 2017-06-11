__all__ = ['slaveNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abnormality'), Js('Ache'), Js('Anguish'), Js('Anomaly'), Js('Ant'), Js('Barbarian'), Js('Bastard'), Js('Peon'), Js('Beast'), Js('Beetle'), Js('Birdbrain'), Js('Blemish'), Js('Blight'), Js('Blockhead'), Js('Boar'), Js('Bonehead'), Js('Boor'), Js('Bottomfeeder'), Js('Boy'), Js('Brute'), Js('Buffoon'), Js('Bug'), Js('Bum'), Js('Corruption'), Js('Crawler'), Js('Creep'), Js('Creeper'), Js('Cretin'), Js('Cricket'), Js('Crud'), Js('Crude'), Js('Curse'), Js('Defect'), Js('Defiled'), Js('Deformation'), Js('Degenerate'), Js('Demon'), Js('Deviant'), Js('Dirt'), Js('Disease'), Js('Disgrace'), Js('Dog'), Js('Dread'), Js('Dreck'), Js('Dunce'), Js('Dust'), Js('Dweller'), Js('Fiend'), Js('Filth'), Js('Flaw'), Js('Flea'), Js('Fly'), Js('Fool'), Js('Freak'), Js('Frog'), Js('Garbage'), Js('Girl'), Js('Gloom'), Js('Gnat'), Js('Gnome'), Js('Goblin'), Js('Greasy'), Js('Gremlin'), Js('Grime'), Js('Grotesque'), Js('Grub'), Js('Gunk'), Js('Halfwit'), Js('Hopeless'), Js('Horror'), Js('Hybrid'), Js('Ill-bred'), Js('Imp'), Js('Impure'), Js('Ingrate'), Js('Insect'), Js('Irregularity'), Js('Junk'), Js('Kobold'), Js('Larva'), Js('Leech'), Js('Lewd'), Js('Louse'), Js('Lowbred'), Js('Lowlife'), Js('Maggot'), Js('Malformed'), Js('Miscreant'), Js('Misery'), Js('Mistake'), Js('Mite'), Js('Mole'), Js('Mongrel'), Js('Monster'), Js('Moth'), Js('Mouse'), Js('Muck'), Js('Mud'), Js('Mug'), Js('Mule'), Js('Mutt'), Js('Nit'), Js('Oaf'), Js('Obscenity'), Js('Ogre'), Js('Parasite'), Js('Pervert'), Js('Pest'), Js('Pig'), Js('Plague'), Js('Pollution'), Js('Prawn'), Js('Primitive'), Js('Rabbit'), Js('Rags'), Js('Rascal'), Js('Rat'), Js('Roach'), Js('Rodent'), Js('Rubble'), Js('Runt'), Js('Savage'), Js('Scamp'), Js('Scrub'), Js('Scum'), Js('Shrimp'), Js('Simple-mind'), Js('Simpleton'), Js('Skunk'), Js('Sleaze'), Js('Slime'), Js('Slop'), Js('Slug'), Js('Smear'), Js('Smut'), Js('Snail'), Js('Snake'), Js('Snot'), Js('Sorrow'), Js('Spider'), Js('Squirmer'), Js('Stain'), Js('Stitch'), Js('Syndrome'), Js('Taint'), Js('Termite'), Js('Tick'), Js('Toad'), Js('Trash'), Js('Troll'), Js('Twerp'), Js('Unchaste'), Js('Uncivilized'), Js('Unclean'), Js('Uncouth'), Js('Unformed'), Js('Untaught'), Js('Vermin'), Js('Waste'), Js('Weakness'), Js('Weasel'), Js('Weevil'), Js('Whelp'), Js('Woe'), Js('Worm'), Js('Wretch'), Js('Wriggler')]))
var.put('nm2', Js([Js('Abomniable'), Js('Ash'), Js('Awful'), Js('Bad'), Js('Baseborn'), Js('Black'), Js('Bottom'), Js('Broken'), Js('Brown'), Js('Cheap'), Js('Dirt'), Js('Dirty'), Js('Disgusting'), Js('Dismal'), Js('Down'), Js('Drab'), Js('Dreck'), Js('Dust'), Js('Fecal'), Js('Feeble'), Js('Fetid'), Js('Filthy'), Js('Flimsy'), Js('Foul'), Js('Fragile'), Js('Frail'), Js('Garbage'), Js('Grease'), Js('Grim'), Js('Grime'), Js('Grisly'), Js('Gross'), Js('Grotesque'), Js('Hideous'), Js('Hollow'), Js('Horrid'), Js('Ill'), Js('Inept'), Js('Inferior'), Js('Infirm'), Js('Insignificant'), Js('Junk'), Js('Lesser'), Js('Limp'), Js('Little'), Js('Lousy'), Js('Low'), Js('Lowborn'), Js('Lowlife'), Js('Lowly'), Js('Meager'), Js('Measly'), Js('Mediocre'), Js('Menial'), Js('Messy'), Js('Minor'), Js('Miserable'), Js('Monstrous'), Js('Muck'), Js('Mud'), Js('Murky'), Js('Nasty'), Js('Noisome'), Js('Paltry'), Js('Pathetic'), Js('Pesky'), Js('Petty'), Js('Pitiful'), Js('Plague'), Js('Puny'), Js('Putrid'), Js('Rancid'), Js('Rank'), Js('Raunchy'), Js('Repulsive'), Js('Revolting'), Js('Rotten'), Js('Sad'), Js('Scant'), Js('Scrap'), Js('Senile'), Js('Shame'), Js('Shoddy'), Js('Sick'), Js('Slag'), Js('Sleazy'), Js('Slimey'), Js('Slop'), Js('Smut'), Js('Soil'), Js('Soot'), Js('Sour'), Js('Spoiled'), Js('Stink'), Js('Stinking'), Js('Tainted'), Js('Tiny'), Js('Trash'), Js('Trashy'), Js('Trifling'), Js('Trivial'), Js('Ugly'), Js('Useless'), Js('Vile'), Js('Waste'), Js('Wicked'), Js('Worthless'), Js('Wracked'), Js('Wretched')]))
var.put('nm3', Js([Js('Abnormality'), Js('Ache'), Js('Anomaly'), Js('Ant'), Js('Barbarian'), Js('Bastard'), Js('Beast'), Js('Beetle'), Js('Boar'), Js('Boor'), Js('Boy'), Js('Brute'), Js('Buffoon'), Js('Bug'), Js('Bum'), Js('Corruption'), Js('Crawler'), Js('Creep'), Js('Creeper'), Js('Cretin'), Js('Cricket'), Js('Crud'), Js('Crude'), Js('Curse'), Js('Demon'), Js('Deviant'), Js('Dog'), Js('Dunce'), Js('Dweller'), Js('Fiend'), Js('Flaw'), Js('Flea'), Js('Floom'), Js('Fly'), Js('Fool'), Js('Freak'), Js('Frog'), Js('Girl'), Js('Gnat'), Js('Gnome'), Js('Goblin'), Js('Gremlin'), Js('Halfwit'), Js('Hybrid'), Js('Imp'), Js('Ingrate'), Js('Insect'), Js('Kobold'), Js('Larva'), Js('Leech'), Js('Lewd'), Js('Louse'), Js('Lowlife'), Js('Maggot'), Js('Mistake'), Js('Mite'), Js('Mole'), Js('Mongrel'), Js('Monster'), Js('Moth'), Js('Mouse'), Js('Mug'), Js('Mule'), Js('Mutt'), Js('Nit'), Js('Oaf'), Js('Ogre'), Js('Parasite'), Js('Peon'), Js('Pervert'), Js('Pest'), Js('Pig'), Js('Prawn'), Js('Rat'), Js('Roach'), Js('Rodent'), Js('Runt'), Js('Savage'), Js('Scamp'), Js('Scrub'), Js('Scum'), Js('Shrimp'), Js('Skunk'), Js('Sleaze'), Js('Slime'), Js('Slug'), Js('Smut'), Js('Snail'), Js('Snake'), Js('Snot'), Js('Spider'), Js('Termite'), Js('Tick'), Js('Toad'), Js('Trash'), Js('Troll'), Js('Twerp'), Js('Vermin'), Js('Weasel'), Js('Weevil'), Js('Whelp'), Js('Worm')]))
pass
pass


# Add lib to the module scope
slaveNames = var.to_python()