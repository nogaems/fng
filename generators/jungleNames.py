__all__ = ['jungleNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
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
var.put('names1', Js([Js('Anaconda'), Js('Ancient'), Js('Angry'), Js('Baboon'), Js('Bellowing'), Js('Bird of Paradise'), Js('Black'), Js('Black Elephant'), Js('Black Panther'), Js('Black Rhino'), Js('Blazing'), Js('Bloodthirsty'), Js('Broken'), Js('Brutal'), Js('Burning'), Js('Bustling'), Js('Calm'), Js('Calming'), Js('Cougar'), Js('Crocodile'), Js('Cursed'), Js('Dancing Bird'), Js('Dark'), Js('Dead'), Js('Diamond'), Js('Distant'), Js('Eastern'), Js('Ebon'), Js('Elephant'), Js('Elephant Tusk'), Js('Emerald'), Js('Emperor'), Js('Empty'), Js('Enchanted'), Js('Ever Reaching'), Js('Expanding'), Js('Fabled'), Js('Faraway'), Js('Feared'), Js('Fearsome'), Js('Feral'), Js('Ferocious'), Js('Flower'), Js('Forbidden'), Js('Furious'), Js('Gentle'), Js('Giant'), Js('Gloomy'), Js('Golden'), Js('Greedy'), Js('Grim'), Js('Growing'), Js('Growling'), Js('Guardian'), Js('Haunted'), Js('Hidden'), Js('Hollow'), Js('Hopeless'), Js('Howling'), Js('Hungry'), Js('Infernal'), Js('Ivory'), Js('Laughing'), Js('Lemur'), Js('Lifeless'), Js('Lioness'), Js('Lionroar'), Js('Lonely'), Js('Lunar'), Js('Macaw'), Js('Mighty'), Js('Mirrored'), Js('Misty'), Js('Moaning'), Js('Moonlit'), Js('Moving'), Js('Mumbling'), Js('Mysterious'), Js('Narrow'), Js('Neverending'), Js('Northern'), Js('Ocelot'), Js('Orangutan'), Js('Peaceful'), Js('Plain'), Js('Playful'), Js('Predator'), Js('Preying'), Js('Primate'), Js('Primeval'), Js('Pristine'), Js('Pygmy'), Js('Quiet'), Js('Raging'), Js('Rainy'), Js('Red'), Js('Restless'), Js('Rising'), Js('Roaring'), Js('Royal Lion'), Js('Rugged'), Js('Sacred'), Js('Sad'), Js('Sanguine'), Js('Savage'), Js('Scarlet'), Js('Scented'), Js('Scrambling'), Js('Screaming'), Js('Serpent'), Js('Severed'), Js('Shadowed'), Js('Shimmering'), Js('Sighing'), Js('Silent'), Js('Silver'), Js('Silverback'), Js('Sleeping'), Js('Slumbering'), Js('Snaketail'), Js('Soft'), Js('Solar'), Js('Southern'), Js('Spider'), Js('Spider Monkey'), Js('Sterile'), Js('Storm'), Js('Stormy'), Js('Tempest'), Js('Thirsty'), Js('Thornbush'), Js('Thunder'), Js('Thundering'), Js('Thunderstorm'), Js('Tigerpaw'), Js('Tigress'), Js('Timeless'), Js('Titan'), Js('Toucan'), Js('Towering'), Js('Treachorous'), Js('Turbulent'), Js('Venomous'), Js('Vicious'), Js('Violent'), Js('Voiceless'), Js('Volcanic'), Js('Wailing'), Js('Waking'), Js('Watching'), Js('Western'), Js('Wet'), Js('Whimpering'), Js('Whining'), Js('Whispering'), Js('White'), Js('White Elephant'), Js('White Lion'), Js('White Parrot'), Js('White Tiger'), Js('Wild'), Js('Windless'), Js('Windy')]))
var.put('names2', Js([Js('Jungle'), Js('Rain Forest'), Js('Bush'), Js('Tropics'), Js('Gardens'), Js('Wilds'), Js('Wilderness'), Js('Wild'), Js('Jungles'), Js('Garden'), Js('Paradise')]))
var.put('names3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('names5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('names7', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
jungleNames = var.to_python()