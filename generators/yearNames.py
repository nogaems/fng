__all__ = ['yearNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(2.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                def PyJs_LONG_0_(var=var):
                    return ((((((((((((Js('Year: ')+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+Js(', Month: '))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+Js(', Day: '))+var.get('nm3').get(var.get('rnd8')))+var.get('nm4').get(var.get('rnd9')))+var.get('nm7').get(var.get('rnd10')))
                var.put('names', PyJs_LONG_0_())
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', (((((((Js('Month: ')+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+Js(', Year of the '))+var.get('nm8').get(var.get('rnd8'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd3b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd5b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd6b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd7b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd3c', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4c', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd5c', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd6c', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd7c', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        if (var.get('rnd5')>Js(6.0)):
                            while PyJsStrictEq(var.get('rnd6'),Js(0.0)):
                                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        if (var.get('rnd5b')>Js(6.0)):
                            while PyJsStrictEq(var.get('rnd6b'),Js(0.0)):
                                var.put('rnd6b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        if (var.get('rnd5c')>Js(6.0)):
                            while PyJsStrictEq(var.get('rnd6c'),Js(0.0)):
                                var.put('rnd6c', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        def PyJs_LONG_1_(var=var):
                            return (((((((((((Js('Year: ')+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+Js(', Month: '))+var.get('nm3').get(var.get('rnd3b')))+var.get('nm4').get(var.get('rnd4b')))+var.get('nm5').get(var.get('rnd5b')))+var.get('nm6').get(var.get('rnd6b')))+var.get('nm7').get(var.get('rnd7b')))
                        var.put('names', ((((((PyJs_LONG_1_()+Js(', Day: '))+var.get('nm3').get(var.get('rnd3c')))+var.get('nm4').get(var.get('rnd4c')))+var.get('nm5').get(var.get('rnd5c')))+var.get('nm6').get(var.get('rnd6c')))+var.get('nm7').get(var.get('rnd7c'))))
                    else:
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('names', (((Js('Month of ')+var.get('nm9').get(var.get('rnd9')))+Js(', Year of the '))+var.get('nm8').get(var.get('rnd8'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('U'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z')]))
var.put('nm2', Js([Js('0'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z')]))
var.put('nm6', Js([Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('cus'), Js('cius'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hn'), Js('hm'), Js('hl'), Js('k'), Js('kius'), Js('kix'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sis'), Js('sius'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('xis'), Js('xius'), Js('z'), Js('zis')]))
var.put('nm8', Js([Js('Aardvark'), Js('Albatross'), Js('Alligator'), Js('Alpaca'), Js('Ant'), Js('Antelope'), Js('Ape'), Js('Armadillo'), Js('Baboon'), Js('Badger'), Js('Bandicoot'), Js('Barracuda'), Js('Basilisk'), Js('Bat'), Js('Bear'), Js('Beaver'), Js('Beetle'), Js('Bighorn'), Js('Bird'), Js('Bison'), Js('Boa'), Js('Boar'), Js('Bobcat'), Js('Bongo'), Js('Buffalo'), Js('Bull'), Js('Butterfly'), Js('Caiman'), Js('Camel'), Js('Canary'), Js('Cat'), Js('Caterpillar'), Js('Catfish'), Js('Centipede'), Js('Chameleon'), Js('Cheetah'), Js('Chicken'), Js('Chimpanzee'), Js('Cockroach'), Js('Cow'), Js('Coyote'), Js('Crab'), Js('Crane'), Js('Crocodile'), Js('Crow'), Js('Deer'), Js('Dingo'), Js('Dog'), Js('Dolphin'), Js('Donkey'), Js('Dragon'), Js('Dragonfly'), Js('Duck'), Js('Eagle'), Js('Elephant'), Js('Elk'), Js('Emu'), Js('Falcon'), Js('Ferret'), Js('Fish'), Js('Flamingo'), Js('Fly'), Js('Fox'), Js('Frog'), Js('Gazelle'), Js('Gecko'), Js('Goat'), Js('Goose'), Js('Gopher'), Js('Gorilla'), Js('Grasshopper'), Js('Guinea Pig'), Js('Hamster'), Js('Hare'), Js('Hedgehog'), Js('Hippopotamus'), Js('Hog'), Js('Hornet'), Js('Horse'), Js('Hound'), Js('Human'), Js('Hummingbird'), Js('Hyena'), Js('Ibis'), Js('Iguana'), Js('Insect'), Js('Jackal'), Js('Jaguar'), Js('Jellyfish'), Js('Kangaroo'), Js('Kingfisher'), Js('Kiwi'), Js('Koala'), Js('Ladybird'), Js('Lamb'), Js('Lemming'), Js('Lemur'), Js('Leopard'), Js('Lion'), Js('Lizard'), Js('Llama'), Js('Lobster'), Js('Lynx'), Js('Macaw'), Js('Magpie'), Js('Manatee'), Js('Mantis'), Js('Meerkat'), Js('Mole'), Js('Mongoose'), Js('Monkey'), Js('Moose'), Js('Moth'), Js('Mouse'), Js('Mule'), Js('Nightingale'), Js('Ocelot'), Js('Octopus'), Js('Orangutan'), Js('Orca'), Js('Ostrich'), Js('Otter'), Js('Owl'), Js('Ox'), Js('Oyster'), Js('Panda'), Js('Panther'), Js('Parrot'), Js('Peacock'), Js('Pelican'), Js('Penguin'), Js('Pheasant'), Js('Pig'), Js('Piranha'), Js('Platypus'), Js('Porcupine'), Js('Prawn'), Js('Quail'), Js('Rabbit'), Js('Raccoon'), Js('Rat'), Js('Raven'), Js('Rhinoceros'), Js('Salamander'), Js('Scorpion'), Js('Seahorse'), Js('Seal'), Js('Shark'), Js('Sheep'), Js('Shrimp'), Js('Skunk'), Js('Sloth'), Js('Snail'), Js('Snake'), Js('Sparrow'), Js('Spider'), Js('Squid'), Js('Squirrel'), Js('Starfish'), Js('Stork'), Js('Swan'), Js('Termite'), Js('Tiger'), Js('Toad'), Js('Tortoise'), Js('Toucan'), Js('Turkey'), Js('Turtle'), Js('Vulture'), Js('Warthog'), Js('Wasp'), Js('Weasel'), Js('Whale'), Js('Wolf'), Js('Wolverine'), Js('Wombat'), Js('Woodchuck'), Js('Woodpecker'), Js('Yak'), Js('Zebra')]))
var.put('nm9', Js([Js('Accomplishments'), Js('Agony'), Js('Amusement'), Js('Ancestors'), Js('Ancients'), Js('Anguish'), Js('Animals'), Js('Anticipation'), Js('Ashes'), Js('Beasts'), Js('Beginnings'), Js('Beliefs'), Js('Birth'), Js('Blessings'), Js('Blight'), Js('Bliss'), Js('Blood'), Js('Bloodlust'), Js('Brotherhood'), Js('Burdens'), Js('Celebration'), Js('Ceremonies'), Js('Champions'), Js('Chaos'), Js('Charm'), Js('Cheers'), Js('Children'), Js('Comfort'), Js('Construction'), Js('Corruption'), Js('Cruelty'), Js('Cunning'), Js('Darkness'), Js('Dawn'), Js('Death'), Js('Decay'), Js('Deception'), Js('Defeat'), Js('Delight'), Js('Delusions'), Js('Desires'), Js('Despair'), Js('Destruction'), Js('Dismay'), Js('Dreams'), Js('Drinking'), Js('Earth'), Js('Echoes'), Js('Ecstasy'), Js('Education'), Js('Elation'), Js('Ends'), Js('Establishing'), Js('Eternity'), Js('Euphoria'), Js('Executions'), Js('Expansion'), Js('Failure'), Js('Families'), Js('Fathers'), Js('Feasts'), Js('Festivals'), Js('Fire'), Js('Fools'), Js('Fortune'), Js('Frost'), Js('Fury'), Js('Giants'), Js('Gifts'), Js('Glee'), Js('Glory'), Js('Grace'), Js('Growth'), Js('Happiness'), Js('Harvest'), Js('Hate'), Js('Hatred'), Js('Heroes'), Js('History'), Js('Honor'), Js('Hope'), Js('Horrors'), Js('Humor'), Js('Illumination'), Js('Immortality'), Js('Insanity'), Js('Joy'), Js('Judgement'), Js('Justice'), Js('Laughter'), Js('Legacies'), Js('Life'), Js('Light'), Js('Loss'), Js('Luxury'), Js('Magic'), Js('Memorials'), Js('Memories'), Js('Mercy'), Js('Misery'), Js('Moonlight'), Js('Mothers'), Js('Mountains'), Js('Mourning'), Js('Mystery'), Js('Nightmares'), Js('Nights'), Js('Oblivion'), Js('Origins'), Js('Pain'), Js('Paradise'), Js('Parents'), Js('Parties'), Js('Peace'), Js('Perdition'), Js('Phantoms'), Js('Plagues'), Js('Pleasure'), Js('Poverty'), Js('Power'), Js('Preparation'), Js('Pride'), Js('Prosperity'), Js('Protection'), Js('Putrefaction'), Js('Rapture'), Js('Reckoning'), Js('Redemption'), Js('Regrets'), Js('Rejoice'), Js('Remembrance'), Js('Rest'), Js('Riches'), Js('Riddles'), Js('Safety'), Js('Sanctuary'), Js('Secrecy'), Js('Secrets'), Js('Shadows'), Js('Silence'), Js('Slaughter'), Js('Snow'), Js('Sorrow'), Js('Souls'), Js('Stars'), Js('Storms'), Js('Struggles'), Js('Suffering'), Js('Summoning'), Js('Sunlight'), Js('Terror'), Js('Thunder'), Js('Titans'), Js('Torment'), Js('Training'), Js('Trials'), Js('Triumphs'), Js('Truth'), Js('Vengeance'), Js('Victory'), Js('Visions'), Js('Voices'), Js('Void'), Js('War'), Js('Water'), Js('Wealth'), Js('Whispers'), Js('Widows'), Js('Wind'), Js('Winds'), Js('Wizardry'), Js('Woe'), Js('Wonder'), Js('Work'), Js('Wraiths')]))
pass
pass


# Add lib to the module scope
yearNames = var.to_python()