__all__ = ['pirateCoves']

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
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' of '))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ahoy'), Js('Anchor'), Js('Barnacle'), Js('Big Horn'), Js('Black Sand'), Js('Black Spot'), Js('Black Water'), Js("Blackbeard's"), Js('Blimey'), Js('Blood'), Js('Bloodmoon'), Js('Booty'), Js('Broken Tooth'), Js("Buccaneer's"), Js('Buried'), Js('Corsair'), Js('Covert'), Js('Crimson'), Js('Crocodile'), Js('Cross'), Js("Crow's Nest"), Js('Cutlass'), Js('Cyclone'), Js('Dagger Tooth'), Js('Danger'), Js("Davy Jones'"), Js('Dead Kraken'), Js("Dead Man's"), Js('Dead Men'), Js('Dead Whale'), Js('Death Curse'), Js('Debris'), Js('Demon'), Js("Devil's"), Js('Dry Rum'), Js('Dubloon'), Js('Execution'), Js('Freebooter'), Js('Full Moon'), Js('Gibbit'), Js('Gold'), Js('Golden Tooth'), Js('Grog'), Js('Gunpowder'), Js('Hazard'), Js('Hempen Halter'), Js('High Tide'), Js('Hornswaggle'), Js('Jagged Reef'), Js('Jolly Roger'), Js('Keelhaul'), Js('Killer Whale'), Js('Kraken'), Js('Landlubber'), Js('Last Words'), Js('Lost Treasure'), Js('Low Tide'), Js('Macaw'), Js('Marauder'), Js('Maroon'), Js('Mermaid'), Js('Monkey'), Js('Monsoon'), Js('Murder'), Js('Mutiny'), Js('Mystery'), Js('Nemo'), Js('No Tale'), Js('Occult'), Js('Old Salt'), Js('Parley'), Js('Parrot'), Js('Peril'), Js('Plunder'), Js('Privateer'), Js('Quartermaster'), Js('Rapier'), Js('Red Sand'), Js('Red Water'), Js('Rum'), Js('Rumrunner'), Js('Salty Sand'), Js('Sanguine'), Js('Scallywag'), Js('Scourge'), Js('Scurvy'), Js('Scuttle'), Js('Scuttlebutt'), Js('Sea Monster'), Js('Seadog'), Js('Seaweed'), Js('Shark'), Js('Shark Fin'), Js('Shipwreck'), Js('Shiver'), Js('Silver'), Js('Skeleton'), Js('Skull'), Js('Stormy'), Js('Sunken'), Js('Sunken Reef'), Js('Swashbuckler'), Js('Tempest'), Js('Thunder'), Js('Timber'), Js('Tortoise'), Js('Trophy'), Js('Turtle'), Js('Unnamed'), Js('Wreckage')]))
var.put('nm2', Js([Js('Anchorage'), Js('Atoll'), Js('Bay'), Js('Cave'), Js('Cavern'), Js('Cay'), Js('Cove'), Js('Enclave'), Js('Haven'), Js('Hideout'), Js('Island'), Js('Isle'), Js('Lagoon'), Js('Port'), Js('Reef'), Js('Refuge'), Js('Retreat'), Js('Sanctuary')]))
var.put('nm3', Js([Js('Anchors'), Js('Auras'), Js('Barnacles'), Js('Blackbeard'), Js('Blood'), Js('Booty'), Js('Broken Teeth'), Js('Buccaneers'), Js('Corsairs'), Js('Cries'), Js('Crimson'), Js('Crocodiles'), Js('Crosses'), Js("Crow's Nests"), Js('Danger'), Js("Davy Jones'"), Js('Dead Men'), Js('Dead Whales'), Js('Death'), Js('Debris'), Js('Demons'), Js('Destruction'), Js('Dry Rum'), Js('Dubloons'), Js('Executions'), Js('Freebooters'), Js('Gold'), Js('Grog'), Js('Gunpowder'), Js('Hazard'), Js('Hornswaggle'), Js('Hurricanes'), Js('Keelhaul'), Js('Killer Whales'), Js('Landlubbers'), Js('Last Words'), Js('Lost Treasure'), Js('Macaws'), Js('Marauders'), Js('Maroon'), Js('Mermaids'), Js('Monkeys'), Js('Monsters'), Js('Murder'), Js('Mutiny'), Js('Mystery'), Js('Nemo'), Js('No Return'), Js('No Tales'), Js('Old Salt'), Js('Parley'), Js('Parrots'), Js('Peril'), Js('Plunder'), Js('Privateers'), Js('Quartermasters'), Js('Rapiers'), Js('Rum'), Js('Rumrunners'), Js('Salty Sands'), Js('Sanguine'), Js('Scallywags'), Js('Scurvy'), Js('Scuttle'), Js('Scuttlebutt'), Js('Seadogs'), Js('Seaweed'), Js('Shark Fin'), Js('Sharks'), Js('Shipwrecks'), Js('Shivers'), Js('Silver'), Js('Skeletons'), Js('Skulls'), Js('Storms'), Js('Sunken Ships'), Js('Swashbucklers'), Js('Thunder'), Js('Timber'), Js('Turtles'), Js('Voices'), Js('Whispers'), Js('Wreckages'), Js('the Black Sand'), Js('the Black Spot'), Js('the Black Water'), Js('the Blood Moon'), Js('the Cyclone'), Js('the Dead Kraken'), Js('the Death Curse'), Js('the Devil'), Js('the Full Moon'), Js('the High Tide'), Js('the Jolly Roger'), Js('the Kraken'), Js('the Low Tide'), Js('the Monsoon'), Js('the Moon'), Js('the Occult'), Js('the Red Sand'), Js('the Red Water'), Js('the Scourge'), Js('the Sunken Fleet'), Js('the Tempest'), Js('the Tortoise'), Js('the Unknown'), Js('the Unnamed')]))
pass
pass


# Add lib to the module scope
pirateCoves = var.to_python()