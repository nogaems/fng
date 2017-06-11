__all__ = ['brewingCompanies']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Aegis'), Js('Aerie'), Js('Alabaster'), Js('Alchemist'), Js('Alesmith'), Js('Anchor'), Js('Angel Wing'), Js('Arcadia'), Js('Artisan'), Js('Audacity'), Js('Aurora'), Js('Avalanche'), Js('Barbarian'), Js('Barrage'), Js('Beard and Barrel'), Js('Bearded Barrel'), Js('Beaver Dam'), Js('Belly Hop'), Js('Bison'), Js('Black Diamond'), Js('Black Stallion'), Js('Black Swan'), Js('Black Widow'), Js('Blizzard'), Js('Blue Creek'), Js('Blueprint'), Js('Bootleg'), Js('Borealis'), Js("Bottom's Up"), Js('Boulder'), Js('Brass Cannon'), Js('Brickstone'), Js('Brimstone'), Js('Buffalo'), Js('Bull Horn'), Js('Cackling Hyena'), Js('Capital'), Js('Cascade'), Js('Catfish'), Js('Celestial'), Js('Cloud Nine'), Js('Cosmos'), Js('Crescent'), Js('Crossroad'), Js('Crystal'), Js('Dark Horse'), Js('Demon Horn'), Js('Diamond'), Js('Dominion'), Js('Dragon Scale'), Js('Dragonfire'), Js('Dragonmead'), Js('Eclipse'), Js('Elysium'), Js('Emerald'), Js('Empyrean'), Js('Epic'), Js('Epoch'), Js('Equinox'), Js('Estuary'), Js('Expedition'), Js('Feather Falling'), Js('Feral'), Js('Ferocious'), Js('Final Frontier'), Js('Final Swallow'), Js('Flying Compass'), Js('Flying Dutchman'), Js('Flying Fish'), Js('Flying Pig'), Js('Forge'), Js('Fountain'), Js('Full Moon'), Js('Glacier'), Js('Glass Bottom'), Js('Gold Rush'), Js('Goodlife'), Js('Gorilla'), Js('Grand Northern'), Js('Great Eastern'), Js('Griffin'), Js('Gritty'), Js('Guerilla'), Js('Hairy Turtle'), Js('Halo'), Js('Hare and Turtle'), Js('Hellhound'), Js('High Rise'), Js('Holy Cow'), Js("Hop 'o the Morning"), Js('Hop Dog'), Js('Hop Notch'), Js('Hop Story'), Js('Hop of the Hour'), Js('Hops and Robbers'), Js('Hourglass'), Js('Howling Wolf'), Js('Hurricane'), Js('Infinite'), Js('Infinity'), Js('Intrepid'), Js('Intrepid Journey'), Js('Journey'), Js('Labyrinth'), Js('Lakeside'), Js('Last Barrel'), Js('Last Glass'), Js('Last Whistle'), Js('Liquid Hero'), Js('Little Pint'), Js('Little River'), Js('Lone Tree'), Js('Lone Wolf'), Js('Long Oak'), Js('Mad Malts'), Js('Magnitude'), Js('Marble'), Js('Mason'), Js('Midnight'), Js('Midnight Meteor'), Js('Minotaur'), Js('Mirror Lake'), Js('Moustache'), Js('Mutual Friend'), Js('New Realm'), Js('Nirvana'), Js('Noble'), Js('Nordic'), Js('Norse'), Js('Nova'), Js('Obelisk'), Js('Obsidian'), Js('Oceanside'), Js('Omega'), Js('Omen'), Js('One Hop Stop'), Js('Onyx'), Js('Oracle'), Js('Over the Hop'), Js('Paradise'), Js('Paragon'), Js('Passage'), Js('Phoenix'), Js('Pinnacle'), Js('Pioneer'), Js('Praying Mantis'), Js('Prime Time'), Js('Props to Hops'), Js('Pyramid'), Js('Red Herring'), Js('Revolution'), Js('Rough Draft'), Js('Rough Sketch'), Js('Salty Dog'), Js('Sanctuary'), Js('Sanctum'), Js('Sapphire'), Js('Seafront'), Js('Side Project'), Js('Silver Tongue'), Js('Single Barrel'), Js('Smooth Sailing'), Js('Speakeasy'), Js('Starlight'), Js('Steamworks'), Js('Steel Beam'), Js('Stone'), Js('Strange'), Js('Stranger Tides'), Js('Summit'), Js('Sunshine'), Js('Sweetwater'), Js('Tall Tales'), Js('Thirsty'), Js('Thunder'), Js('Tidal Wave'), Js('Timeless'), Js('Tiptop Hop'), Js('Torrent'), Js('Tributary'), Js('Tricerahops'), Js('Trouble'), Js('Twin Barrel'), Js('Two Birds'), Js("Up's Bottom"), Js('Valiant'), Js('Valor'), Js('Vertex'), Js('Victory'), Js('Viking'), Js('Vintage'), Js('Voyage'), Js('Wanderlust'), Js('War Horse'), Js('Wheelbarrow'), Js('White Water'), Js('Wild Western'), Js('Wingman'), Js('Workhop'), Js('Zion')]))
    var.put('nm2', Js([Js('Brewing Company'), Js('Brewers'), Js('Brewing'), Js('Fermentary'), Js('Brewing Co.'), Js('Brewery'), Js('Aleworks'), Js('Craft Ales'), Js('Brewing Company'), Js('Brewers'), Js('Brewing'), Js('Brewing Co.'), Js('Brewery')]))
    var.put('nm3', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('The ')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('names', (((var.get('nm3').get(var.get('rnd3'))+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
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
brewingCompanies = var.to_python()