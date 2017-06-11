__all__ = ['helicopterNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aegis'), Js('Aello'), Js('Aethon'), Js('Albatross'), Js('Alicanto'), Js('Alicorn'), Js('Ambrosia'), Js('Amrita'), Js('Angel'), Js('Aphrodite'), Js('Apollo'), Js('Apostle'), Js('Ara'), Js('Argo'), Js('Aria'), Js('Arondight'), Js('Artemis'), Js('Arthur'), Js('Ascalon'), Js('Ash'), Js('Astra'), Js('Aura'), Js('Aurora'), Js('Avalanche'), Js('Avalerion'), Js('Avalon'), Js('Azoth'), Js('Bandit'), Js('Barbarian'), Js('Beast'), Js('Behemoth'), Js('Big Bird'), Js('Blaze'), Js('Blizzard'), Js('Boomer'), Js('Brawl'), Js('Broxa'), Js('Bumblebee'), Js('Bustard'), Js('Cinder'), Js('Cockatrice'), Js('Condor'), Js('Cormorant'), Js('Cosmos'), Js('Crane'), Js('Creature'), Js('Critter'), Js('Cryobird'), Js('Cupid'), Js('Cyclone'), Js('Cyclops'), Js('Demon'), Js('Devil Bird'), Js('Diablo'), Js('Dustdevil'), Js('Dynamite'), Js('Eagle'), Js('Echo'), Js('Effigy'), Js('Ellida'), Js('Enigma'), Js('Ether'), Js('Ethereal'), Js('Excalibur'), Js('Exile'), Js('Falcon'), Js('Feather'), Js('Fiend'), Js('Firebird'), Js('Flamingo'), Js('Flash'), Js('Fluke'), Js('Fray'), Js('Frenzy'), Js('Frigatebird'), Js('Fury'), Js('Gale'), Js('Gargoyle'), Js('Ghost'), Js('Glory'), Js('Glutton'), Js('Goliath'), Js('Gram'), Js('Griffin'), Js('Growler'), Js('Guerrilla'), Js('Gungnir'), Js('Gust'), Js('Hades'), Js('Harpy'), Js('Hawk'), Js('Hawker'), Js('Helix'), Js('Herald'), Js('Heretic'), Js('Hippogriff'), Js('Hornet'), Js('Hover Dove'), Js('Hoverbird'), Js('Howler'), Js('Hummingbird'), Js('Hunter'), Js('Huntress'), Js('Huricane'), Js('Husk'), Js('Hussle'), Js('Hydra'), Js('Illume'), Js('Inferno'), Js('Javelin'), Js('Juvenile'), Js('Kindle'), Js('Kingfisher'), Js('Kookaburra'), Js('Lark'), Js('Leviathan'), Js('Lightning Bird'), Js('Loki'), Js('Lumina'), Js('Lyrebird'), Js('Mammoth'), Js('Medusa'), Js('Miracle'), Js('Mithril'), Js('Mjolnir'), Js('Monsoon'), Js('Mother Hen'), Js('Naglfar'), Js('Nebula'), Js('Nightingale'), Js('Nova'), Js('Nurse'), Js('Omen'), Js('Oracle'), Js('Orb'), Js('Ozone'), Js('Pamola'), Js('Pandora'), Js('Paradox'), Js('Parakeet'), Js('Pelican'), Js('Phantom'), Js('Phoenix'), Js('Poseidon'), Js('Pterodactyl'), Js('Pterosaur'), Js('Pyre'), Js('Pyrobird'), Js('Quail'), Js('Quarrel'), Js('Queen Bee'), Js('Rebel'), Js('Rebound'), Js('Renegade'), Js('Riot'), Js('Roc'), Js('Rumbler'), Js('Sanddevil'), Js('Seahawk'), Js('Silver'), Js('Siren'), Js('Sliver'), Js('Snake'), Js('Spot'), Js('Spotlight'), Js('Squall'), Js('Stalker'), Js('Stallion'), Js('Stark'), Js('Stork'), Js('Storm'), Js('Strife'), Js('Striker'), Js('Swan'), Js('Swift'), Js('Swiftstrike'), Js('Talaria'), Js('Tempest'), Js('Teratorn'), Js('Terrorbird'), Js('Thor'), Js('Thunder Bird'), Js('Thunderbolt'), Js('Tigress'), Js('Tinder'), Js('Trumpet'), Js('Tucan'), Js('Typhoon'), Js('Varmint'), Js('Veil'), Js('Vermillion'), Js('Vimana'), Js('Void'), Js('Volley'), Js('Vulture'), Js('Warbler'), Js('Wasp'), Js('Zephyr'), Js('Zeus'), Js('Zion')]))
pass
pass


# Add lib to the module scope
helicopterNames = var.to_python()