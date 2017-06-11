__all__ = ['beachNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd1')))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+Js(' '))+var.get('nm2').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abysmal'), Js('Albatross'), Js('Alligator'), Js('Almond'), Js('Amazon'), Js('Apple Blossom'), Js('Arctic'), Js('Bamboo'), Js('Barracuda'), Js('Barren'), Js('Birds of Paradise'), Js('Black'), Js('Black Boulder'), Js('Black Coral'), Js('Black Rock'), Js('Blackrock'), Js("Blindman's"), Js('Blue'), Js('Boulder'), Js('Breakwater'), Js('Brilliant'), Js('Bronze'), Js('Buccaneer'), Js('Calm'), Js('Calmest'), Js('Cannon'), Js('Cannonball'), Js('Capricorn'), Js('Champion'), Js('Charmed'), Js('Cheerless'), Js('Cherry'), Js('Cherry Blossom'), Js('Cobalt'), Js('Cocoa'), Js('Coconut'), Js('Cold'), Js('Cold Water'), Js('Coral'), Js('Crescent'), Js('Crescent Moon'), Js('Crocodile'), Js('Crystal'), Js('Cursed'), Js('Dancing'), Js('Dark'), Js('Darkest'), Js('Dead'), Js('Depraved'), Js('Desert'), Js('Deserted'), Js('Diamond'), Js('Distant'), Js('Dolphin'), Js('Dragon'), Js('Dragonfly'), Js('Dragontooth'), Js('Dread'), Js('Dreaded'), Js('Driftwood'), Js('Eagle'), Js('Eastern'), Js('Emerald'), Js('Empty'), Js('Enchanted'), Js('Equator'), Js('Ethereal'), Js('Fire'), Js("Fisherman's"), Js('Flamingo'), Js('Flat'), Js('Floral'), Js('Flowing'), Js('Fluorescent'), Js('Foaming'), Js('Forbidden'), Js('Frothy'), Js('Frozen'), Js('Giant'), Js('Gleaming'), Js('Glistening'), Js('Gold'), Js('Golden'), Js('Golden Sands'), Js('Grave'), Js('Gray'), Js('Green'), Js('Harmonious'), Js('Harmony'), Js('Hermite Crab'), Js('Honey Comb'), Js('Hope'), Js('Hot Water'), Js('Hummingbird'), Js('Hungry'), Js('Hurricane'), Js('Infernal'), Js('Infinite'), Js('Invisible'), Js('Isolated'), Js('Jade'), Js('Jericho'), Js('Jeronimo'), Js('Laughing'), Js('Lifeless'), Js('Lighthouse'), Js('Lime'), Js('Living'), Js('Lobster'), Js('Lonely'), Js('Long'), Js('Lotus'), Js('Lucent'), Js('Majestic'), Js('Manatee'), Js('Manta'), Js('Manta Ray'), Js('Mermaid'), Js('Mesmerizing'), Js('Midnight'), Js('Mighty'), Js('Mirror'), Js('Mirrored'), Js('Misty'), Js('Moaning'), Js('Monkey'), Js('Moving'), Js('Mudcrab'), Js('Mystery'), Js('Mystique'), Js('Neptune'), Js('New'), Js('New Hope'), Js('New Spring'), Js('Northern'), Js('Oak'), Js('Ocean City'), Js('Oceanview'), Js('Orange'), Js('Orchid'), Js('Oyster'), Js('Oyster Pearl'), Js('Palm'), Js('Palm Tree'), Js('Paradise'), Js('Peaceful'), Js('Pearl'), Js('Pebble'), Js('Pelican'), Js('Perfumed'), Js('Pirate'), Js('Pirate Grove'), Js('Pirate Ship'), Js("Pirate's"), Js('Pleasant'), Js('Poseidon'), Js('Pristine'), Js('Quiet'), Js('Raging'), Js('Rainbow'), Js('Raincloud'), Js('Rainy'), Js('Red'), Js('Reflecting'), Js('Relaxing'), Js('Restless'), Js('Rocky'), Js('Rolling'), Js('Rough'), Js('Rushing'), Js('Salty'), Js('Sandbar'), Js('Sandcrab'), Js('Sandfoot'), Js('Sandollar'), Js('Sandy'), Js('Sandy Cliffs'), Js('Sanguine'), Js('Sapphire'), Js('Savage'), Js('Seacliffs'), Js('Seagull'), Js('Seashell'), Js('Serene'), Js('Shaded'), Js('Shadow'), Js('Shady'), Js('Shark'), Js('Sharktooth'), Js('Shimmering'), Js('Shipwreck'), Js('Shrimp'), Js('Silent'), Js('Silver'), Js('Sleeping'), Js('Soundless'), Js('Southern'), Js('Sparkling'), Js('Starfish'), Js('Sterile'), Js('Stingray'), Js('Stormy'), Js('Sundown'), Js('Sunken'), Js('Sunken Ship'), Js('Sunken Wreck'), Js('Sunny'), Js('Sunrise'), Js('Sunset'), Js('Sunshine'), Js('Surf City'), Js('Surfer'), Js('Teal'), Js('Tinted'), Js('Tortoise'), Js('Tortuga'), Js('Tranquil'), Js('Treasure'), Js('Trinity'), Js('Tropic'), Js('Troubled'), Js('Turbulent'), Js('Turquoise'), Js('Turtle'), Js('Unknown'), Js('Unstable'), Js('Vast'), Js('Victoria'), Js('Violent'), Js('Western'), Js('Whale'), Js('Whispering'), Js('White'), Js('White Boulder'), Js('White Coral'), Js('White Rock'), Js('Wild'), Js('Willow'), Js('Windy'), Js('Wondering'), Js('Wrinkled'), Js('Yearning')]))
var.put('nm2', Js([Js('Bank'), Js('Beach'), Js('Coast'), Js('Coastline'), Js('Edge'), Js('Margin'), Js('Beach'), Js('Coast'), Js('Sands'), Js('Strand'), Js('Shore'), Js('Point'), Js('Oceanfront'), Js('Sands'), Js('Cove'), Js('Bay'), Js('Paradise'), Js('Seafront'), Js('Shore'), Js('Strand')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm7', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
beachNames = var.to_python()