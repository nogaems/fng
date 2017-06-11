__all__ = ['gameStudio']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
            if (var.get('i')<Js(3.0)):
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd1'))+Js(' '))+var.get('names2').get(var.get('rnd2')))+Js(' '))+var.get('names7').get(var.get('rnd'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('names', ((((var.get('names1').get(var.get('rnd1'))+Js(' '))+var.get('names3').get(var.get('rnd2')))+Js(' '))+var.get('names7').get(var.get('rnd'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                        var.put('names', (((var.get('names4').get(var.get('rnd1'))+var.get('names5').get(var.get('rnd2')))+Js(' '))+var.get('names7').get(var.get('rnd'))))
                    else:
                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                        var.put('names', ((var.get('names6').get(var.get('rnd1'))+Js(' '))+var.get('names7').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Acid'), Js('Active'), Js('Adorable'), Js('Aggressive'), Js('Agile'), Js('Alarming'), Js('Amazing'), Js('Amusing'), Js('Ancient'), Js('Angelic'), Js('Angry'), Js('Antique'), Js('Arctic'), Js('Awesome'), Js('Baby'), Js('Bad'), Js('Big'), Js('Big Bad'), Js('Black'), Js('Black and White'), Js('Blind'), Js('Bold'), Js('Brave'), Js('Bright'), Js('Broken'), Js('Bronze'), Js('Buzy'), Js('Calm'), Js('Classic'), Js('Clever'), Js('Clumsy'), Js('Confused'), Js('Crazy'), Js('Creative'), Js('Cute'), Js('Dapper'), Js('Dark'), Js('Deadly'), Js('Dear'), Js('Defiant'), Js('Digital'), Js('Dirty'), Js('Dizzy'), Js('Dopey'), Js('Eager'), Js('Elegant'), Js('Evil'), Js('Exalted'), Js('Excited'), Js('Exotic'), Js('Fake'), Js('False'), Js('Fancy'), Js('Fast'), Js('Feisty'), Js('Filthy'), Js('Fluffy'), Js('Foolish'), Js('Forsaken'), Js('Free'), Js('Fuzzy'), Js('Gentle'), Js('Glass'), Js('Gloomy'), Js('Golden'), Js('Good'), Js('Gray'), Js('Green'), Js('Grumpy'), Js('Hairy'), Js('Happy'), Js('Hidden'), Js('Hollow'), Js('Honest'), Js('Hungry'), Js('Infamous'), Js('Intelligent'), Js('Intrepid'), Js('Jade'), Js('Jolly'), Js('Kind'), Js('Light'), Js('Liquid'), Js('Little'), Js('Lonely'), Js('Lost'), Js('Lucky'), Js('Mad'), Js('Massive'), Js('Mellow'), Js('Merry'), Js('Misty'), Js('Naughty'), Js('Nervous'), Js('Nice'), Js('Nifty'), Js('Night'), Js('Numb'), Js('Obvious'), Js('Odd'), Js('Old'), Js('Orange'), Js('Original'), Js('Peaceful'), Js('Plump'), Js('Pretty'), Js('Proud'), Js('Quick'), Js('Rare'), Js('Red'), Js('Royal'), Js('Rude'), Js('Rusty'), Js('Scary'), Js('Shadow'), Js('Shady'), Js('Silent'), Js('Silly'), Js('Silver'), Js('Smart'), Js('Snappy'), Js('Steel'), Js('Strange'), Js('Sunny'), Js('Sweet'), Js('Tiny'), Js('Twin'), Js('Ugly'), Js('Urban'), Js('Vicious'), Js('Violet'), Js('Virtual'), Js('Weird'), Js('Wild'), Js('Wise'), Js('Young')]))
var.put('names2', Js([Js('Albatross'), Js('Alligator'), Js('Ant'), Js('Ape'), Js('Armadillo'), Js('Bandicoot'), Js('Barnacle'), Js('Barracuda'), Js('Basilisk'), Js('Bat'), Js('Bear'), Js('Beaver'), Js('Beetle'), Js('Bird'), Js('Bison'), Js('Boa'), Js('Boar'), Js('Bull'), Js('Bulldog'), Js('Bunny'), Js('Butterfly'), Js('Calf'), Js('Camel'), Js('Canary'), Js('Cat'), Js('Caterpillar'), Js('Chicken'), Js('Cobra'), Js('Cougar'), Js('Cow'), Js('Coyote'), Js('Crab'), Js('Crane'), Js('Crow'), Js('Deer'), Js('Dingo'), Js('Dino'), Js('Dinosaur'), Js('Dog'), Js('Dolphin'), Js('Donkey'), Js('Dove'), Js('Dragon'), Js('Duck'), Js('Eagle'), Js('Elephant'), Js('Falcon'), Js('Fish'), Js('Fly'), Js('Fox'), Js('Frog'), Js('Gecko'), Js('Giraffe'), Js('Goat'), Js('Gopher'), Js('Gorilla'), Js('Hamster'), Js('Hare'), Js('Hippo'), Js('Horse'), Js('Hyena'), Js('Ibis'), Js('Jellyfish'), Js('Kitten'), Js('Kiwi'), Js('Lamb'), Js('Lemur'), Js('Leopard'), Js('Lion'), Js('Lizard'), Js('Llama'), Js('Lobster'), Js('Manta'), Js('Mantis'), Js('Moose'), Js('Mouse'), Js('Newt'), Js('Otter'), Js('Owl'), Js('Ox'), Js('Panda'), Js('Panther'), Js('Pelican'), Js('Penguin'), Js('Pig'), Js('Pigeon'), Js('Piranha'), Js('Pony'), Js('Poodle'), Js('Prawn'), Js('Pug'), Js('Puppy'), Js('Rabbit'), Js('Raccoon'), Js('Rat'), Js('Raven'), Js('Ray'), Js('Rhino'), Js('Rooster'), Js('Scorpion'), Js('Seahorse'), Js('Seal'), Js('Shark'), Js('Sheep'), Js('Shrimp'), Js('Sloth'), Js('Snail'), Js('Snake'), Js('Spider'), Js('Squid'), Js('Squirrel'), Js('Starfish'), Js('Stork'), Js('Swan'), Js('Tiger'), Js('Toad'), Js('Tortoise'), Js('Turtle'), Js('Vulture'), Js('Walrus'), Js('Wasp'), Js('Weasel'), Js('Whale'), Js('Wolf'), Js('Yak'), Js('Zebra')]))
var.put('names3', Js([Js('Alien'), Js('Amulet'), Js('Android'), Js('Angel'), Js('Apple'), Js('Assassin'), Js('Banana'), Js('Bandit'), Js('Banshee'), Js('Beast'), Js('Bigfoot'), Js('Blossom'), Js('Bow'), Js('Boy'), Js('Candle'), Js('Castle'), Js('Cave'), Js('Centaur'), Js('Champion'), Js('Chest'), Js('Citadel'), Js('Clock'), Js('Companion'), Js('Crown'), Js('Crystal'), Js('Cup'), Js('Cyborg'), Js('Cyclops'), Js('Demon'), Js('Devil'), Js('Diamond'), Js('Door'), Js('Dwarf'), Js('Elf'), Js('Emperor'), Js('Enigma'), Js('Eyes'), Js('Face'), Js('Fairy'), Js('Fire'), Js('Flag'), Js('Flower'), Js('Forest'), Js('Fortress'), Js('Friend'), Js('Fungus'), Js('Ghost'), Js('Ghoul'), Js('Giant'), Js('Girl'), Js('Gnome'), Js('Goblin'), Js('Golem'), Js('Gryphon'), Js('Guardian'), Js('Halfling'), Js('Helmet'), Js('Imp'), Js('King'), Js('Kiwi'), Js('Knight'), Js('Lake'), Js('Lantern'), Js('Light'), Js('Lighthouse'), Js('Mage'), Js('Man'), Js('Manor'), Js('Mansion'), Js('Melon'), Js('Mermaid'), Js('Merman'), Js('Mirror'), Js('Monster'), Js('Mountain'), Js('Mushroom'), Js('Nation'), Js('Necklace'), Js('Nymph'), Js('Ogre'), Js('Orc'), Js('Palace'), Js('Paladin'), Js('Peanut'), Js('Pear'), Js('Petal'), Js('Phantom'), Js('Phoenix'), Js('Pirate'), Js('Pixy'), Js('Potato'), Js('Queen'), Js('Ring'), Js('River'), Js('Road'), Js('Robot'), Js('Satyr'), Js('Shadow'), Js('Shield'), Js('Sidekick'), Js('Siren'), Js('Skeleton'), Js('Slime'), Js('Spaceship'), Js('Spear'), Js('Spectre'), Js('Spire'), Js('Statue'), Js('Stranger'), Js('Sword'), Js('Thief'), Js('Tiara'), Js('Tower'), Js('Treasure'), Js('Tree'), Js('Trinket'), Js('Troll'), Js('Vampire'), Js('Viking'), Js('Walnut'), Js('Watch'), Js('Water'), Js('Werewolf'), Js('Windmill'), Js('Wisp'), Js('Witch'), Js('Wizard'), Js('Woman'), Js('Wraith'), Js('Yeti')]))
var.put('names4', Js([Js('angel'), Js('astral'), Js('auto'), Js('autumn'), Js('bio'), Js('chrono'), Js('cyber'), Js('dead'), Js('demon'), Js('feral'), Js('fire'), Js('free'), Js('frost'), Js('frozen'), Js('ghost'), Js('half'), Js('info'), Js('inter'), Js('intro'), Js('jade'), Js('lightning'), Js('liquid'), Js('lunar'), Js('mega'), Js('micro'), Js('mist'), Js('moon'), Js('nether'), Js('phantom'), Js('real'), Js('reflex'), Js('silver'), Js('snow'), Js('solar'), Js('star'), Js('stray'), Js('sub'), Js('summer'), Js('sun'), Js('super'), Js('thunder'), Js('trick'), Js('winter')]))
var.put('names5', Js([Js('berg'), Js('blast'), Js('blossom'), Js('bolt'), Js('bullet'), Js('byte'), Js('cloud'), Js('control'), Js('domain'), Js('door'), Js('dream'), Js('fire'), Js('flux'), Js('fly'), Js('fun'), Js('ice'), Js('jam'), Js('lab'), Js('less'), Js('line'), Js('ly'), Js('petal'), Js('pixel'), Js('play'), Js('punch'), Js('rain'), Js('realm'), Js('soft'), Js('sphere'), Js('storm'), Js('tale'), Js('trap'), Js('ware'), Js('water'), Js('web'), Js('wire'), Js('world'), Js('zone')]))
var.put('names6', Js([Js('Afterlife'), Js('Amnesia'), Js('Anomaly'), Js('Asteroid'), Js('Blessing'), Js('Bullettime'), Js('Cataclysm'), Js('Century'), Js('Cherry Blossom'), Js('Clairvoyant'), Js('Climax'), Js('Cloudburst'), Js('Comet'), Js('Crown'), Js('Cyclone'), Js('Deluge'), Js('Destiny'), Js('Downpour'), Js('Dumb Luck'), Js('Dynamic'), Js('Enigma'), Js('Enterprise'), Js('Eternity'), Js('Exile'), Js('Extinction'), Js('Falling Star'), Js('Fate'), Js('Fierce'), Js('Fluke'), Js('Flytrap'), Js('Fortune'), Js('Hellfire'), Js('Heretic'), Js('Honor'), Js('Hurricane'), Js('Idol'), Js('Immortal'), Js('Immortality'), Js('Insomnia'), Js('Insurgent'), Js('Isolation'), Js('Karma'), Js('Limbo'), Js('Locomotion'), Js('Lonely'), Js('Maximum'), Js('Mental'), Js('Meteoroid'), Js('Millenium'), Js('Miracle'), Js('Mithril'), Js('Monsoon'), Js('Motion'), Js('Mystery'), Js('Mystic'), Js('Nirvana'), Js('Oblivion'), Js('Occult'), Js('Outcast'), Js('Paradox'), Js('Phenomenon'), Js('Pinnacle'), Js('Prodigy'), Js('Psychic'), Js('Radical'), Js('Rebel'), Js('Refugee'), Js('Relentless'), Js('Renegade'), Js('Revelation'), Js('Reverse'), Js('Rogue'), Js('Rose Petal'), Js('Ruthless'), Js('Sensation'), Js('Serendipity'), Js('Shooting Star'), Js('Skyward'), Js('Solarflare'), Js('Stardust'), Js('Summit'), Js('Supreme'), Js('Surprise'), Js('Thunder'), Js('Thunderstorm'), Js('Tidal Wave'), Js('Time Traveler'), Js('Tomorrow'), Js('Tragedy'), Js('Trinket'), Js('Typhoon'), Js('Typical'), Js('Ultimate'), Js('Underground'), Js('Untouchable'), Js('Vagabond'), Js('Vault'), Js('Vigor'), Js('Void'), Js('Zion')]))
var.put('names7', Js([Js('Games'), Js('Entertainment'), Js('Studios'), Js('Interactive'), Js('Game Studios'), Js('Media'), Js('Productions'), Js('Arts')]))
pass
pass


# Add lib to the module scope
gameStudio = var.to_python()