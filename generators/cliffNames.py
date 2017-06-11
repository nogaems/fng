__all__ = ['cliffNames']

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
    var.registers(['names4', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7', 'result'])
    var.put('names1', Js([Js('Adamantine'), Js('Albatross'), Js('Ancient'), Js('Angry'), Js('Arctic'), Js('Arid'), Js('Bare'), Js('Basalt'), Js('Basanite'), Js('Bellowing'), Js('Black'), Js('Black Cavern'), Js('Blackrock'), Js('Blazing'), Js('Broken'), Js('Broken Ship'), Js('Bronze'), Js('Burning'), Js('Calm'), Js('Clay'), Js('Claystone'), Js('Clouded'), Js('Collapsing'), Js('Colossal'), Js('Cracking'), Js('Crumbling'), Js('Crushing'), Js('Cursed'), Js('Cyclone'), Js('Dark'), Js('Dead'), Js('Desolate'), Js('Diamond'), Js('Distant'), Js('Eagle'), Js('Eastern'), Js('Ebon'), Js('Empty'), Js('Enchanted'), Js('Eroded'), Js('Ever Reaching'), Js('Fabled'), Js('Faraway'), Js('Feared'), Js('Fearsome'), Js('Fishermen'), Js('Flower'), Js('Forbidden'), Js('Foxtail'), Js('Fractured'), Js('Frightening'), Js('Frozen'), Js('Giant'), Js('Gloomy'), Js('Golden'), Js('Granite'), Js('Gray'), Js('Grim'), Js('Growling'), Js('Guardian'), Js('Haunted'), Js('Hidden'), Js('Hidden Gold'), Js('Hollow'), Js('Hooded'), Js('Hopeless'), Js('Howling'), Js('Hungry'), Js('Hurricane'), Js('Ice-Crowned'), Js('Iced'), Js('Icy'), Js('Infernal'), Js('Iron'), Js('Ironbeak'), Js('Ivory'), Js('Jagged'), Js('Killer Whale'), Js('Laughing'), Js('Lifeless'), Js('Limestone'), Js('Lobster'), Js('Lonely'), Js('Mammoth'), Js('Marble'), Js('Mermaid'), Js('Mighty'), Js('Mirrored'), Js('Misty'), Js('Moaning'), Js('Moonlit'), Js('Mountain Goat'), Js('Mumbling'), Js('Murky'), Js('Musselbay'), Js('Mysterious'), Js('Narrow'), Js('Neverending'), Js('Northern'), Js('Obsidian'), Js('Oyster'), Js('Peaceful'), Js('Penguin'), Js('Petal'), Js('Pinetree'), Js('Plain'), Js('Pristine'), Js('Quiet'), Js('Rabbit Ear'), Js('Raging'), Js('Ravenclaw'), Js('Red'), Js('Restless'), Js('Roaring'), Js('Rock Lobster'), Js('Rocky'), Js('Rugged'), Js('Sacred'), Js('Sad'), Js('Salmon'), Js('Sandstone'), Js('Sandy'), Js('Savage'), Js('Scarlet'), Js('Scented'), Js('Screaming'), Js('Screeching'), Js('Sea Gull'), Js('Seal'), Js('Serpent'), Js('Severed'), Js('Shadowed'), Js('Shattered'), Js('Shattering'), Js('Shimmering'), Js('Sighing'), Js('Silent'), Js('Silver'), Js('Silver Cavern'), Js('Silverrock'), Js('Slippery'), Js('Slumbering'), Js('Snaketail'), Js('Snowy'), Js('Soft'), Js('Southern'), Js('Sterile'), Js('Stonetalon'), Js('Storm'), Js('Stormy'), Js('Sunken Ship'), Js('Tempest'), Js('Thunder'), Js('Thundering'), Js('Thunderrock'), Js('Thunderstorm'), Js('Titan'), Js('Tradepost'), Js('Treachorous'), Js('Violent'), Js('Voiceless'), Js('Volcanic'), Js('Wailing'), Js('Warthog'), Js('Western'), Js('Whimpering'), Js('Whining'), Js('Whirlwind'), Js('Whispering'), Js('Whisperwind'), Js('White'), Js('White Feather'), Js('Wild'), Js('Windless'), Js('Windy')]))
    var.put('names2', Js([Js('Cliff'), Js('Cliffs'), Js('Fjord'), Js('Fjords'), Js('Wall'), Js('Crag'), Js('Bluff'), Js('Bluffs'), Js('Ravine'), Js('Crevice'), Js('Gorge'), Js('Chasm'), Js('Canyon'), Js('Abyss'), Js('Gulch')]))
    var.put('names3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('names4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
    var.put('names5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('names6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
    var.put('names7', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', (((Js('The ')+var.get('names1').get(var.get('rnd')))+Js(' '))+var.get('names2').get(var.get('rnd2'))))
                var.get('result').callprop('push', var.get('names'))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('names', ((((var.get('names3').get(var.get('rnd'))+var.get('names4').get(var.get('rnd2')))+var.get('names7').get(var.get('rnd3')))+Js(' '))+var.get('names2').get(var.get('rnd4'))))
                    var.get('result').callprop('push', var.get('names'))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('names', ((((((var.get('names3').get(var.get('rnd'))+var.get('names4').get(var.get('rnd2')))+var.get('names5').get(var.get('rnd3')))+var.get('names6').get(var.get('rnd4')))+var.get('names7').get(var.get('rnd5')))+Js(' '))+var.get('names2').get(var.get('rnd6'))))
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
cliffNames = var.to_python()