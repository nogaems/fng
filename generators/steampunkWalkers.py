__all__ = ['steampunkWalkers']

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
    var.registers(['nm1', 'result'])
    var.put('nm1', Js([Js('Abomination'), Js('Achiever'), Js('Albatross'), Js('Ambition'), Js('Ant'), Js('Arachne'), Js('Arachnid'), Js('Atlas'), Js('Badger'), Js('Bear'), Js('Beast'), Js('Beetle'), Js('Behemoth'), Js('Beholder'), Js('Bender'), Js('Bigg'), Js('Black Bear'), Js('Boar'), Js('Booster'), Js('Bouncer'), Js('Bovine'), Js('Brass Knuckle'), Js('Brawler'), Js('Bruiser'), Js('Brute'), Js('Bull'), Js('Bumble Bee'), Js('Burrower'), Js('Butcher'), Js('Calf'), Js('Centaur'), Js('Challenger'), Js('Champion'), Js('Cleanser'), Js('Cockroach'), Js('Colossus'), Js('Commander'), Js('Companion'), Js('Courier'), Js('Crab'), Js('Crane'), Js('Crawler'), Js('Creator'), Js('Creature'), Js('Crustacean'), Js('Curator'), Js('Cyclops'), Js('Defender'), Js('Diagnosis'), Js('Digger'), Js('Dino'), Js('Dispatcher'), Js('Divebomb'), Js('Diver'), Js('Dodger'), Js('Donkey'), Js('Dozer'), Js('Drone'), Js('Eagle'), Js('Echo'), Js('Effigy'), Js('Elephant'), Js('Escort'), Js('Fairy'), Js('Fire Ant'), Js('Fireman'), Js('Forger'), Js('Frankenstein'), Js('Gargantua'), Js('Gargoyle'), Js('Gift'), Js('Godzilla'), Js('Goliath'), Js('Gorilla'), Js('Grizzly'), Js('Grunt'), Js('Guardian'), Js('Guide'), Js('Handyman'), Js('Harvester'), Js('Herald'), Js('Hercules'), Js('Hermit'), Js('Hornet'), Js('Hummingbird'), Js('Hypnotizer'), Js('Idol'), Js('Infernal'), Js('Insect'), Js('Inspector'), Js('Jack'), Js('Jack-Of-All-Trades'), Js('Jacket'), Js('Judge'), Js('Kraken'), Js('Leapfrog'), Js('Logger'), Js('Lumberjack'), Js('Lurker'), Js('Mammoth'), Js('Mare'), Js('Matriarch'), Js('Medic'), Js('Messenger'), Js('Minotaur'), Js('Model'), Js('Mole'), Js('Monkey'), Js('Mosquito'), Js('Muscle'), Js('Night Mare'), Js('Officer'), Js('Ogre'), Js('Operator'), Js('Ox'), Js('Passenger'), Js('Patriarch'), Js('Patriot'), Js('Pincer'), Js('Pioneer'), Js('Professor'), Js('Quaker'), Js('Rabbit'), Js('Rambler'), Js('Recruit'), Js('Rhino'), Js('Rig'), Js('Rigg'), Js('Roach'), Js('Robin'), Js('Rumbler'), Js('Scarab'), Js('Scarecrow'), Js('Scientist'), Js('Seahorse'), Js('Servant'), Js('Sheriff'), Js('Shoulder'), Js('Shrieker'), Js('Siren'), Js('Snail'), Js('Songbird'), Js('Spider'), Js('Sprite'), Js('Stallion'), Js('Stinger'), Js('Suit'), Js('Supporter'), Js('Surgeon'), Js('Thunder'), Js('Titan'), Js('Toddler'), Js('Vessel'), Js('Volunteer'), Js('Voyager'), Js('Walker'), Js('Wanderer'), Js('Whistler'), Js('Yak'), Js('Zealot')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('names', (Js('The ')+var.get('nm1').get(var.get('rnd'))))
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
steampunkWalkers = var.to_python()