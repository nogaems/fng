__all__ = ['bugSpecies']

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
    var.registers(['nm1', 'nm2', 'result'])
    var.put('nm1', Js([Js('Abnormal'), Js('Abrasive'), Js('Absorbtion'), Js('Abstract'), Js('Acid'), Js('Acidic'), Js('Acoustic'), Js('Actor'), Js('Adapting'), Js('Aggressive'), Js('Anchor'), Js('Ancient'), Js('Angel'), Js('Angelic'), Js('Arctic'), Js('Arid'), Js('Aromatic'), Js('Assault'), Js('Attack'), Js('Audience'), Js('Bamboo'), Js('Barren'), Js('Basin'), Js('Basking'), Js('Battle'), Js('Bell'), Js('Berserker'), Js('Betrayal'), Js('Biting'), Js('Bitter'), Js('Black'), Js('Blade'), Js('Blind'), Js('Blood'), Js('Blossom'), Js('Blue'), Js('Bold'), Js('Bomber'), Js('Bone'), Js('Bony'), Js('Boulder'), Js('Brain'), Js('Brass'), Js('Bright'), Js('Brilliant'), Js('Bronze'), Js('Bubble'), Js('Bulb'), Js('Burrowing'), Js('Bush'), Js('Butter'), Js('Button'), Js('Cacti'), Js('Candid'), Js('Cannon'), Js('Cemetery'), Js('Champion'), Js('Chaos'), Js('Chimera'), Js('Cloud'), Js('Coast'), Js('Colossal'), Js('Community'), Js('Conquerer'), Js('Corrupting'), Js('Corruption'), Js('Creeping'), Js('Crimson'), Js('Crooked'), Js('Crown'), Js('Crypt'), Js('Curved'), Js('Dancing'), Js('Dark'), Js('Darling'), Js('Death'), Js('Deceit'), Js('Defender'), Js('Defiant'), Js('Defiler'), Js('Delivery'), Js('Demonic'), Js('Diamond'), Js('Diligent'), Js('Disguise'), Js('Draconian'), Js('Dragon'), Js('Dread'), Js('Dream'), Js('Drone'), Js('Drunk'), Js('Dueling'), Js('Ebon'), Js('Echo'), Js('Electric'), Js('Emerald'), Js('Emigrating'), Js('Emigration'), Js('Enchanted'), Js('Enchanting'), Js('Entangling'), Js('Ethereal'), Js('Evasive'), Js('Exalted'), Js('Exploring'), Js('Faded'), Js('Faint'), Js('Fake'), Js('False'), Js('Familiar'), Js('Fancy'), Js('Fire'), Js('Flamboyant'), Js('Flower'), Js('Fog'), Js('Forging'), Js('Fragrant'), Js('Frigid'), Js('Furry'), Js('Fuzzy'), Js('Garden'), Js('Gardening'), Js('Gatherer'), Js('Ghost'), Js('Giant'), Js('Gilded'), Js('Glass'), Js('Gliding'), Js('Gold'), Js('Golden'), Js('Grand'), Js('Grave'), Js('Great'), Js('Green'), Js('Grim'), Js('Grooming'), Js('Guardian'), Js('Gummy'), Js('Hairy'), Js('Hammer'), Js('Harvest'), Js('Harvester'), Js('Hill'), Js('Hissing'), Js('Hollow'), Js('Humming'), Js('Hypnotic'), Js('Ice'), Js('Infernal'), Js('Iron'), Js('Ivory'), Js('Jade'), Js('Jewel'), Js('Jolly'), Js('Juvenile'), Js('Lavish'), Js('Leather'), Js('Light'), Js('Lumber'), Js('Luminous'), Js('Macabre'), Js('Majestic'), Js('Mammoth'), Js('Marble'), Js('Marked'), Js('Masked'), Js('Milk'), Js('Minor'), Js('Monster'), Js('Monstrous'), Js('Mud'), Js('Mushy'), Js('Night'), Js('Nimble'), Js('Nocturnal'), Js('Noxious'), Js('Nursing'), Js('Oceanic'), Js('Ornate'), Js('Perfumed'), Js('Phoenix'), Js('Plump'), Js('Primal'), Js('Prime'), Js('Putrid'), Js('Radiant'), Js('Rainbow'), Js('Red'), Js('Regal'), Js('Rigid'), Js('Ring'), Js('Ringed'), Js('River'), Js('Rock'), Js('Royal'), Js('Rubble'), Js('Ruby'), Js('Ruin'), Js('Sanguine'), Js('Sapphire'), Js('Scaly'), Js('Scented'), Js('Servant'), Js('Shadow'), Js('Silk'), Js('Silky'), Js('Skeletal'), Js('Skeleton'), Js('Skinny'), Js('Smiling'), Js('Smoke'), Js('Sorrow'), Js('Spiked'), Js('Spiky'), Js('Spotted'), Js('Stone'), Js('Storm'), Js('Striped'), Js('Sugar'), Js('Thicket'), Js('Throne'), Js('Tomb'), Js('Tower'), Js('Tree'), Js('Tube'), Js('Umbrella'), Js('Vagabond'), Js('Velvet'), Js('Vibrant'), Js('Volatile'), Js('Volcano'), Js('Wandering'), Js('Wax'), Js('White'), Js('Wicked')]))
    var.put('nm2', Js([Js('Amphipod'), Js('Ant'), Js('Aphid'), Js('Arachnid'), Js('Bee'), Js('Beetle'), Js('Billbug'), Js('Borer'), Js('Bug'), Js('Bumblebee'), Js('Butterfly'), Js('Caterpillar'), Js('Centipede'), Js('Chigger'), Js('Cicada'), Js('Cockroach'), Js('Crawler'), Js('Cricket'), Js('Damselfly'), Js('Dragonfly'), Js('Earwig'), Js('Flatworm'), Js('Flea'), Js('Fly'), Js('Grasshopper'), Js('Grub'), Js('Hopper'), Js('Horntail'), Js('Katydid'), Js('Lacewing'), Js('Ladybird'), Js('Larva'), Js('Leech'), Js('Locust'), Js('Longhorn'), Js('Louse'), Js('Maggot'), Js('Mantid'), Js('Mantis'), Js('Mayfly'), Js('Millipede'), Js('Mite'), Js('Mosquito'), Js('Moth'), Js('Nepidae'), Js('Parasite'), Js('Peripatus'), Js('Pseudoscorpion'), Js('Psocid'), Js('Pupa'), Js('Scarab'), Js('Silverfish'), Js('Slater'), Js('Slug'), Js('Snail'), Js('Sowbug'), Js('Spider'), Js('Spittlebug'), Js('Springtail'), Js('Stick Insect'), Js('Stonefly'), Js('Termite'), Js('Thrip'), Js('Tick'), Js('Wasp'), Js('Weevil'), Js('Weta'), Js('Worm')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
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
bugSpecies = var.to_python()