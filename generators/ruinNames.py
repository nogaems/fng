__all__ = ['ruinNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' of '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm3').get(var.get('rnd')))+Js(' '))+var.get('nm1').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Borough'), Js('City'), Js('Cove'), Js('Farms'), Js('Fields'), Js('Forest'), Js('Harbor'), Js('Island'), Js('Isle'), Js('Labyrinth'), Js('Lands'), Js('Mountain'), Js('Outpost'), Js('Reef'), Js('River'), Js('Shore'), Js('Temple'), Js('Town'), Js('Vault'), Js('Village')]))
var.put('nm2', Js([Js('Ash'), Js('Ashes'), Js('Blight'), Js('Bones'), Js('Chaos'), Js('Charcoal'), Js('Coal'), Js('Collapse'), Js('Corrosion'), Js('Cracks'), Js('Crimson'), Js('Crumbles'), Js('Darkness'), Js('Death'), Js('Debris'), Js('Decay'), Js('Desertion'), Js('Desolation'), Js('Despair'), Js('Dishonor'), Js('Doom'), Js('Dread'), Js('Dreams'), Js('Destruction'), Js('Dusk'), Js('Emptiness'), Js('Ends'), Js('Exiles'), Js('Extinction'), Js('Fire'), Js('Fog'), Js('Fragments'), Js('Ghosts'), Js('Gloom'), Js('Graves'), Js('Hauntings'), Js('Ice'), Js('Illusions'), Js('Isolation'), Js('Mist'), Js('Mold'), Js('Molten Rock'), Js('Myths'), Js('Necrosis'), Js('Nightfall'), Js('Nightmares'), Js('Oblivion'), Js('Obsidian'), Js('Onyx'), Js('Phantoms'), Js('Pieces'), Js('Plants'), Js('Remains'), Js('Remnants'), Js('Residue'), Js('Rot'), Js('Rubble'), Js('Ruination'), Js('Ruins'), Js('Rust'), Js('Screams'), Js('Shadows'), Js('Shambles'), Js('Shrubs'), Js('Silence'), Js('Silver'), Js('Skeletons'), Js('Skulls'), Js('Slate'), Js('Sleep'), Js('Smoke'), Js('Solitude'), Js('Soot'), Js('Spirits'), Js('Stone'), Js('Twilight'), Js('Undoing'), Js('Vibrations'), Js('Waste'), Js('Water'), Js('Whispers'), Js('Wind'), Js('Wreckages'), Js('the Abandoned'), Js('the Abyss'), Js('the Broken'), Js('the Curse'), Js('the Damned'), Js('the Fallen'), Js('the Forgotten'), Js('the Forsaken'), Js('the Infernal'), Js('the Inferno'), Js('the Lost'), Js('the Night'), Js('the Perished'), Js('the Scourge'), Js('the Unknown'), Js('the Vanquished'), Js('the Void')]))
var.put('nm3', Js([Js('Abandoned'), Js('Abyss'), Js('Agony'), Js('Ashen'), Js('Bare'), Js('Barren'), Js('Bleak'), Js('Blight'), Js('Bone'), Js('Broken'), Js('Burning'), Js('Chaos'), Js('Charcoal'), Js('Coal'), Js('Cobalt'), Js('Collapsed'), Js('Corroded'), Js('Cracking'), Js('Crimson'), Js('Crumbled'), Js('Crumbling'), Js('Cursed'), Js('Damned'), Js('Dark'), Js('Dcayed'), Js('Dead'), Js('Debris'), Js('Decaying'), Js('Deserted'), Js('Desolated'), Js('Desolation'), Js('Despair'), Js('Destroyed'), Js('Destruction'), Js('Dismissed'), Js('Doom'), Js('Dread'), Js('Emptied'), Js('Empty'), Js('End'), Js('Ender'), Js('Erased'), Js('Ethereal'), Js('Exile'), Js('Exiled'), Js('Extinct'), Js('Fallen'), Js('Fire'), Js('Foggy'), Js('Forgotten'), Js('Forsaken'), Js('Fragmented'), Js('Frozen'), Js('Ghost'), Js('Gloom'), Js('Grave'), Js('Haunted'), Js('Ice'), Js('Illusion'), Js('Infernal'), Js('Inferno'), Js('Isolated'), Js('Isolation'), Js('Lifeless'), Js('Lonely'), Js('Lost'), Js('Mist'), Js('Molded'), Js('Molten'), Js('Motionless'), Js('Murky'), Js('Mythic'), Js('Nameless'), Js('Necrotic'), Js('Neglected'), Js('Night'), Js('Nightmare'), Js('Nullified'), Js('Obliterated'), Js('Oblivion'), Js('Obsidian'), Js('Onyx'), Js('Overgrown'), Js('Perished'), Js('Petrified'), Js('Phantom'), Js('Remnant'), Js('Residue'), Js('Rotting'), Js('Rubble'), Js('Ruin'), Js('Ruined'), Js('Rusted'), Js('Savage'), Js('Scorching'), Js('Scourge'), Js('Scream'), Js('Screaming'), Js('Shadow'), Js('Shamble'), Js('Shrub'), Js('Silent'), Js('Silver'), Js('Skeleton'), Js('Skull'), Js('Slate'), Js('Sleeping'), Js('Sleepy'), Js('Smoke'), Js('Solitude'), Js('Soot'), Js('Spirit'), Js('Stone'), Js('Twilight'), Js('Uncanny'), Js('Undone'), Js('Unknown'), Js('Vanquished'), Js('Vibrating'), Js('Void'), Js('Waste'), Js('Wasted'), Js('Weeping'), Js('Whisper'), Js('Whispering'), Js('Windy'), Js('Wreckage')]))
pass
pass


# Add lib to the module scope
ruinNames = var.to_python()