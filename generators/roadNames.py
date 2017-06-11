__all__ = ['roadNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd7')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Acorn'), Js('Adamantine'), Js('Ambush'), Js("Ancestor's"), Js('Ancient'), Js('Angry'), Js('Angry Giant'), Js('Apple Blossom'), Js('Appletree'), Js('Arching'), Js('Arid'), Js('Baker'), Js('Basilisk'), Js('Black'), Js('Black Brick'), Js('Black Castle'), Js('Black Forest'), Js('Black Palace'), Js('Black Sea'), Js('Blacksmith'), Js('Bleak'), Js('Blue'), Js('Blue Comet'), Js('Blueberry'), Js('Broken'), Js('Broken Altar'), Js('Broken Carriage'), Js('Broken Castle'), Js('Broken Ruins'), Js('Broken Tower'), Js('Bronze'), Js('Brown Bear'), Js('Burned'), Js('Burning'), Js('Burning Fire'), Js('Butcher'), Js('Butterfly'), Js('Calming'), Js('Caterpillar'), Js("Champion's"), Js('Charmed'), Js('Charming'), Js('Cherry Blossom'), Js('Chestnut'), Js('Cloud'), Js('Cloudfield'), Js('Coalmine'), Js('Cobalt'), Js('Cobweb'), Js("Conqueror's"), Js('Constellation'), Js('Coral'), Js("Crow's Nest"), Js('Crystal'), Js('Cursed'), Js('Dancing'), Js('Dark'), Js('Dead'), Js('Decaying'), Js('Deserted'), Js('Desolation'), Js('Diamond'), Js("Dragon's"), Js('Dragonfire'), Js('Dragontail'), Js('Dragontooth'), Js('Dreary'), Js("Eagle's Nest"), Js('Eastern'), Js('Elephant'), Js('Emerald'), Js('Enchanted'), Js('Ethereal'), Js('Ever Reaching'), Js('Everlasting'), Js('Fabled'), Js('Falcon'), Js('Falcon Claw'), Js('Fallen Champion'), Js('Fallen Giant'), Js('Fallen Knight'), Js('Fallen Oak'), Js('Fallen Phoenix'), Js('Fallen Soldier'), Js('Fallen Star'), Js('Faraway'), Js("Farmer's"), Js('Feared'), Js('Fiery'), Js('Filthy Pig'), Js('Firemaker'), Js('Five Mile'), Js('Fletcher'), Js('Flowing'), Js('Foaming'), Js('Forbidden'), Js('Frightening'), Js('Frozen'), Js('Frozen Lake'), Js('Frozen Mountain'), Js('Giant Leap'), Js('Glassy'), Js('Gleaming'), Js('Glistening'), Js('Golden'), Js('Gray'), Js('Grazing Cow'), Js('Green'), Js('Herbalist'), Js('Hidden'), Js('Hollow'), Js('Honeybee'), Js('Hungry'), Js("Hunter's"), Js('Hurricane'), Js('Infernal'), Js('Infinite'), Js('Invisible'), Js('Iron'), Js('Ironmine'), Js('Isolated'), Js('Isolation'), Js('Jade'), Js('Jagged'), Js('Killing'), Js("King's"), Js('Last Hope'), Js('Laughing'), Js('Lava Flow'), Js('Lifeless'), Js('Light'), Js('Lightning'), Js('Lion Roar'), Js('Living'), Js('Living Dead'), Js('Lonely'), Js('Lost Dragon'), Js('Lost Soul'), Js('Lurking Crows'), Js('Majestic'), Js('Maple Tree'), Js('Mapleleaf'), Js('Merchant'), Js('Miller'), Js('Mirrored'), Js('Misty'), Js('Moon'), Js('Moonlight'), Js('Moonrise'), Js('Moonset'), Js('Moonshine'), Js('Mountain'), Js('Mountain view'), Js('Murky Swamp'), Js('Mysterious'), Js('Mystery'), Js('Narrow'), Js('Northern'), Js('Oak Tree'), Js('Ocean view'), Js('Oceanside'), Js('Orchard'), Js('Overhanging'), Js('Owl'), Js('Pack Mule'), Js('Peach Blossom'), Js('Perfumed'), Js('Phoenix'), Js('Pickpocket'), Js('Pigmy'), Js("Queen's"), Js('Quiet'), Js('Rabbithole'), Js('Raging'), Js('Red'), Js('Red Brick'), Js('Red Comet'), Js('Restless'), Js('Riverside'), Js('Roaming Giant'), Js('Rosebush'), Js('Rugged'), Js('Salvation'), Js('Sanguine'), Js('Savage'), Js('Scarlet'), Js('Scorpion'), Js('Seashore'), Js('Seaside'), Js('Serene'), Js('Serpent'), Js('Shadow'), Js('Shadowed'), Js('Shadowy'), Js('Sharktooth'), Js('Sheep Herd'), Js('Shepherd'), Js('Shimmering'), Js('Shooting Star'), Js('Silent'), Js('Silent Hill'), Js('Silent Lake'), Js('Silent Mountain'), Js('Silver'), Js('Sleeping'), Js('Southern'), Js('Spidersilk'), Js('Starlight'), Js('Stepping Stone'), Js('Stingray'), Js('Strawberry'), Js('Sun'), Js('Sunlight'), Js('Sunray'), Js('Sunrise'), Js('Sunset'), Js('Sunshine'), Js('Tavern'), Js('Teal'), Js('Terraced'), Js('Thornbush'), Js('Thunder'), Js('Thundercloud'), Js('Thunderstorm'), Js('Tower'), Js("Trader's"), Js('Tranquil'), Js('Trepidation'), Js('Unknown'), Js('Violent'), Js('Volcano'), Js('Vulture'), Js('Walnut'), Js('Wandering Soul'), Js('Wandering Troll'), Js('Western'), Js('Whisper'), Js('Whisper Mountain'), Js('Whispering'), Js('White'), Js('White Castle'), Js('White Forest'), Js('White Palace'), Js('Wild'), Js('Willow Tree'), Js('Windy'), Js('Wolf Howl'), Js('Woodland'), Js('Yellow'), Js('Yellow Brick')]))
var.put('nm2', Js([Js('Avenue'), Js('Highway'), Js('Lane'), Js('Pass'), Js('Passage'), Js('Path'), Js('Pathway'), Js('Road'), Js('Route'), Js('Street'), Js('Track'), Js('Trail'), Js('Way'), Js('Alley'), Js('Walk')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm7', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
roadNames = var.to_python()