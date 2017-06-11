__all__ = ['pirateCrews']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names4', 'names2', 'nameGen', 'names3'])
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
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', (((Js('The ')+var.get('names1').get(var.get('rnd')))+Js(' '))+var.get('names2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('names', (((Js('The ')+var.get('names2').get(var.get('rnd')))+Js(' of the '))+var.get('names3').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('names', (Js('The ')+var.get('names4').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Albatross'), Js('Berserker'), Js('Black Bandana'), Js('Black Crow'), Js('Black Parrot'), Js('Black Rose'), Js('Black Skull'), Js('Black Snake'), Js('Black Tooth'), Js('Black Tooth Grin'), Js('Blackbeard'), Js('Bloodsail'), Js('Blue Whale'), Js('Bone Dry'), Js('Brass Knuckle'), Js('Broken Heart'), Js('Bullseye'), Js('Catamaran'), Js('Chaos'), Js('Crazy Eyed'), Js('Crossbone'), Js('Cutlass'), Js('Cyclone'), Js('Daydream'), Js('Dead'), Js('Defiant'), Js('Dread'), Js('Drifting'), Js('Driftwood'), Js('East Sea'), Js('Filibuster'), Js('Filthy Frigate'), Js('Forsaken'), Js('Full Sail'), Js('Giant Turtle'), Js('Golden Grin'), Js('Golden Tooth'), Js('Goldtooth'), Js('Hydra'), Js('Jolly'), Js('Keel Haul'), Js('Kraken'), Js('Land Shark'), Js('Lost'), Js('Lost Rum'), Js('Mad Man'), Js('Maelstrom'), Js('Maroon'), Js('Masked'), Js('Mermaid'), Js('Merpeople'), Js('Mirage'), Js('Neptune'), Js('Nightmare'), Js('North Sea'), Js('Octo'), Js('Octopus'), Js('One Eyed'), Js('One Legged'), Js('Painted'), Js('Pegleg'), Js('Phantom'), Js('Poseidon'), Js('Rat Grin'), Js('Rattail'), Js('Red Bandana'), Js('Red Hair'), Js('Red Rose'), Js('Rickety'), Js('River'), Js('Rusty'), Js('Sanguine'), Js('Scarlet'), Js('Sea Lurker'), Js('Sea Serpent'), Js('Sea Siren'), Js('Seagull'), Js('Seashell'), Js('Serpent'), Js('Seven Sails'), Js('Seven Seas'), Js('Shadow'), Js('Sharkfin'), Js('Sharktooth'), Js('Silent Whisper'), Js('Silver Crow'), Js('Smiling'), Js('South Sea'), Js('Specter'), Js('Talking Parrot'), Js('Tankard'), Js('Tooth Grin'), Js('Undead'), Js('Vortex'), Js('West Sea'), Js('Whirlpool'), Js('White Shark'), Js('Whitebeard'), Js('Black Squid'), Js('White Squid'), Js('Silver Hydra'), Js('Laviathan'), Js('Silver Wave'), Js('Golden Cannon'), Js('Silver Cannon'), Js('Hollow'), Js('Gilded')]))
var.put('names2', Js([Js('Pirates'), Js('Raiders'), Js('Buccaneers'), Js('Corsairs'), Js('Rovers'), Js('Pillagers'), Js('Plunderers'), Js('Pirates'), Js('Bandits'), Js('Buccaneers')]))
var.put('names3', Js([Js('Black Diamond'), Js('Black Fog'), Js('Black Hydra'), Js('Black Lagoon'), Js('Black Sea'), Js('Black Skull'), Js('Black Squid'), Js('Black Turtle'), Js('Bloodied Flag'), Js('Blue Lagoon'), Js('Blue Moon'), Js('Blue Whale'), Js('Broken Harbor'), Js('Broken Islands'), Js('Coin'), Js('Crossbones'), Js('Curse'), Js('Cursed Doubloon'), Js('Dark Waters'), Js('Dead Sea'), Js('Depths'), Js('East'), Js('East Coast'), Js('Eternal Raid'), Js('Flintlock'), Js('Fog'), Js('Forsaken Captain'), Js('Frozen North'), Js('Frozen Ocean'), Js('Frozen Sea'), Js('Gilded Cannon'), Js('Golden Banner'), Js('Golden Cannonball'), Js('Golden Cutlass'), Js('Golden Mermaid'), Js('Great Lake'), Js('Hidden Cove'), Js('Hidden Monster'), Js('High Seas'), Js('Hollow'), Js('Horizon'), Js('Infernal Depths'), Js('Inner Sea'), Js('Leviathan'), Js('Lost Kraken'), Js('Lost Mermaid'), Js('Lost Ocean'), Js('Lost Shores'), Js('Lost Treasure'), Js('Lurker in the Depths'), Js('Maelstrom'), Js('Monster Shark'), Js('Nether'), Js('New Horizon'), Js('New World'), Js('North'), Js('North Sea'), Js('Open Seas'), Js('Plague'), Js('Plank'), Js('Promised Lands'), Js('Promised Treasure'), Js('Rum'), Js('Sanguine Flag'), Js('Scarlet Flag'), Js('Sea Serpent'), Js('Sea Wolf'), Js('Seven Sails'), Js('Seven Seas'), Js('Seven Shores'), Js('Shade'), Js('Shallows'), Js('Shores'), Js('Silent Bay'), Js('Silent Sea'), Js('Silver Cannon'), Js('Silver Cove'), Js('Silver Eye'), Js('Silver Moon'), Js('Silver Serpent'), Js('Silver Sword'), Js('Silver Wave'), Js("Siren's Call"), Js("Siren's Song"), Js('South'), Js('South Sea'), Js('Squid'), Js('Sword'), Js('Tempest'), Js('Thunder'), Js('Thunderstorm'), Js('Tide'), Js('Void'), Js('Vortex'), Js('West'), Js('West Coast'), Js('Wicked Seas'), Js('Unleashed Kraken'), Js('Eternal Curse'), Js('Stolen Years')]))
var.put('names4', Js([Js('Barnicles'), Js('Black Bandana Buccaneers'), Js('Black Bandanas'), Js('Black Sails'), Js('Black Skulls'), Js('Black Tooth Grins'), Js('Blackbeards'), Js('Bloody Bandits'), Js('Broken Bandits'), Js('Broken bones'), Js('Cannon Balls'), Js('Cannonball Bandits'), Js('Crazy Eyes'), Js('Cutlasses'), Js('Dividers'), Js('Drifters'), Js('Driftwood Divers'), Js('Eternal Smiles'), Js('Filibusters'), Js('Fishguts'), Js('Flintlocks'), Js('Floaters'), Js('Golden Guns'), Js('Grand Cannoneers'), Js("High 'n Dry"), Js('Hired Guns'), Js('Hired Swords'), Js('Hydras'), Js('Keel Haulers'), Js('Landlocked'), Js('Lost Souls'), Js('Mad Marauders'), Js('Nautical Navigators'), Js('Ocean Shadows'), Js('Ocean Wanderers'), Js('Odd Jobs'), Js('Peg Legs'), Js('Peglegs'), Js('Pelicans'), Js('Pieces of Eight'), Js('Plagued Pillagers'), Js('Plank Walkers'), Js('Plunderers and Pillagers'), Js('Rattails'), Js('Red Raiders'), Js('Red Sails'), Js('Red Scarfs'), Js('Rusty Rustlers'), Js('Salty Dogs'), Js('Salty Swabbers'), Js('Sea Angels'), Js('Sea Devils'), Js('Sea Dogs'), Js('Sea Foxes'), Js('Sea Monsters'), Js('Sea Sharks'), Js('Sea Terrors'), Js('Sea Wolves'), Js('Seagulls'), Js('Shellbacks'), Js('Silver Eyes'), Js('Silver Sailors'), Js('Silver Swords'), Js("Siren's Song"), Js('Sirens'), Js('Skull and Crossbones'), Js('Sons of the Sea'), Js('South Sea Sailors'), Js('Squids'), Js('Stray Dogs'), Js('Talking Parrots'), Js('Thirsty Thieves'), Js('Thunder Waves'), Js('Water Walkers'), Js('Wild Windjammers')]))
pass
pass


# Add lib to the module scope
pirateCrews = var.to_python()