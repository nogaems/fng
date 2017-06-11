__all__ = ['outpostNames']

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
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('names', (((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+Js(' '))+var.get('names3').get(var.get('rnd3'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('names', ((var.get('names4').get(var.get('rnd'))+Js(' '))+var.get('names3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Amber'), Js('Anger'), Js('Anvil'), Js('Arrow'), Js('Autumn'), Js('Black'), Js('Blood'), Js('Bone'), Js('Boulder'), Js('Bracken'), Js('Bright'), Js('Broad'), Js('Bronze'), Js('Brown'), Js('Chill'), Js('Cold'), Js('Copper'), Js('Crystal'), Js('Dark'), Js('Dawn'), Js('Dead'), Js('Death'), Js('Dire'), Js('Dream'), Js('Dry'), Js('Dune'), Js('Dusk'), Js('Dust'), Js('East'), Js('Ebon'), Js('Ember'), Js('Ever'), Js('Far'), Js('Feather'), Js('Fel'), Js('Fire'), Js('Flame'), Js('Flint'), Js('Fog'), Js('Forgotten'), Js('Frost'), Js('Fuse'), Js('Ghost'), Js('Gold'), Js('Hammer'), Js('Heart'), Js('High'), Js('Honor'), Js('Iron'), Js('Living'), Js('Lost'), Js('Mad'), Js('Maple'), Js('Marsh'), Js('Moon'), Js('Moss'), Js('Murk'), Js('Musk'), Js('Narrow'), Js('North'), Js('Oak'), Js('Phantom'), Js('Plague'), Js('Pyre'), Js('Raven'), Js('Razor'), Js('River'), Js('Rubble'), Js('Sabre'), Js('Sand'), Js('Shade'), Js('Shadow'), Js('Shale'), Js('Shatter'), Js('Silver'), Js('Snow'), Js('Sorrow'), Js('South'), Js('Splinter'), Js('Spring'), Js('Star'), Js('Still'), Js('Stone'), Js('Summer'), Js('Sun'), Js('Swamp'), Js('Swift'), Js('Thunder'), Js('Timber'), Js('Twilight'), Js('Twin'), Js('Under'), Js('Up'), Js('Valor'), Js('West'), Js('Whisper'), Js('White'), Js('Wild'), Js('Winter'), Js('Wither')]))
var.put('names2', Js([Js('band'), Js('barks'), Js('blossom'), Js('branch'), Js('break'), Js('breeze'), Js('bridge'), Js('brook'), Js('claw'), Js('cloud'), Js('clutch'), Js('crest'), Js('cross'), Js('crown'), Js('deep'), Js('dew'), Js('drift'), Js('dust'), Js('fall'), Js('falls'), Js('fang'), Js('fen'), Js('field'), Js('fist'), Js('fold'), Js('foot'), Js('forge'), Js('front'), Js('fury'), Js('garde'), Js('gate'), Js('glen'), Js('grasp'), Js('grip'), Js('grove'), Js('guard'), Js('gulch'), Js('hand'), Js('hill'), Js('hold'), Js('holde'), Js('keep'), Js('lake'), Js('land'), Js('landing'), Js('leaf'), Js('light'), Js('lord'), Js('maw'), Js('mill'), Js('mines'), Js('mist'), Js('more'), Js('mount'), Js('mouth'), Js('pass'), Js('peak'), Js('pine'), Js('plume'), Js('point'), Js('prey'), Js('reach'), Js('ridge'), Js('rock'), Js('rune'), Js('runner'), Js('scream'), Js('sea'), Js('shear'), Js('shield'), Js('shire'), Js('shore'), Js('song'), Js('speaker'), Js('spear'), Js('spine'), Js('spire'), Js('springs'), Js('star'), Js('storm'), Js('stream'), Js('strider'), Js('summit'), Js('sword'), Js('talon'), Js('tomb'), Js('vale'), Js('vault'), Js('vein'), Js('wall'), Js('ward'), Js('watch'), Js('watcher'), Js('water'), Js('web'), Js('well'), Js('wharf'), Js('wind'), Js('wing'), Js('wood')]))
var.put('names3', Js([Js('Acropolis'), Js('Barracks'), Js('Barrier'), Js('Base'), Js('Bastille'), Js('Blockade'), Js('Bulwark'), Js('Camp'), Js('Castle'), Js('Citadel'), Js('Command'), Js('Depot'), Js('Encampment'), Js('Enclave'), Js('Fort'), Js('Fortification'), Js('Fortress'), Js('Front'), Js('Frontier'), Js('Garde'), Js('Garrison'), Js('Guard'), Js('Harbor'), Js('Harborage'), Js('Haven'), Js('Headquarters'), Js('Hideout'), Js('Hold'), Js('Outpost'), Js('Point'), Js('Post'), Js('Rampart'), Js('Redoubt'), Js('Refuge'), Js('Retreat'), Js('Sanctuary'), Js('Site'), Js('Stand'), Js('Station'), Js('Stockade'), Js('Stronghold'), Js('Terminal'), Js('Wall'), Js('Watch')]))
var.put('names4', Js([Js('Arid'), Js("Autumn's"), Js('Azure'), Js('Barren'), Js('Black Scar'), Js('Blood'), Js('Bone'), Js('Boulder'), Js('Burning'), Js('Canyon'), Js('Cinder'), Js('Crossroad'), Js('Crown'), Js('Crystal'), Js('Dawn'), Js('Dead'), Js('Death'), Js('Desolation'), Js('Dire'), Js('Doom'), Js("Dreamer's"), Js('Dusk'), Js('Dusty'), Js('Ebon'), Js('Echo'), Js('Eclipse'), Js('Eco-Dome'), Js('Ember'), Js('Eternal'), Js('Falcon'), Js('Final'), Js('First'), Js("Fool's Hope"), Js('Forest'), Js('Forsaken'), Js('Forward'), Js('Fury'), Js('Garden'), Js('Gloom'), Js('Hidden'), Js('Honor'), Js('Hunter'), Js('Iron'), Js('Lagoon'), Js('Lake'), Js("Light's"), Js('Marsh'), Js('Marshal'), Js('Mountain'), Js('Mountain-Foot'), Js('Night'), Js('Nightmare'), Js('Oasis'), Js('Obsidian'), Js('Ocean'), Js('Oracle'), Js('Phantom'), Js('Pinnacle'), Js('Raven'), Js('Razor'), Js('River'), Js('Sandy'), Js('Scarlet'), Js('Sea'), Js('Seabreeze'), Js('Second'), Js('Shadow'), Js('Skeleton'), Js('Sleeping'), Js('Solitude'), Js('Sorrow'), Js("Spring's"), Js('Starfall'), Js('Starlight'), Js('Storm'), Js("Summer's"), Js('Summit'), Js('Talon'), Js('Tempest'), Js('Terror'), Js('Third'), Js('Thunder'), Js('Thunderstorm'), Js('Timber'), Js('Triumph'), Js('Twilight'), Js('Twin'), Js('Valley'), Js('Valor'), Js('Vendetta'), Js('Vengeance'), Js('Venom'), Js('Victor'), Js('Vortex'), Js('Warden'), Js("Watcher's"), Js('Wild'), Js('Wildling'), Js("Winter's"), Js('Writhing')]))
pass
pass


# Add lib to the module scope
outpostNames = var.to_python()