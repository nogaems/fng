__all__ = ['filmStudio']

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
    var.registers(['names4', 'names6', 'names5', 'names8', 'names2', 'names3', 'names1', 'names7', 'result'])
    var.put('names1', Js([Js('Active'), Js('Adorable'), Js('Amazing'), Js('Amusing'), Js('Ancient'), Js('Angel'), Js('Angry'), Js('Awesome'), Js('Baby'), Js('Bad'), Js('Big'), Js('Big Bad'), Js('Black'), Js('Bold'), Js('Brave'), Js('Bright'), Js('Busy'), Js('Cinematic'), Js('Classic'), Js('Clever'), Js('Clumsy'), Js('Crazy'), Js('Creative'), Js('Curious'), Js('Cute'), Js('Dancing'), Js('Dapper'), Js('Dark'), Js('Dear'), Js('Dirty'), Js('Dopey'), Js('Dream'), Js('Dreaming'), Js('Eager'), Js('Eastern'), Js('Ecstatic'), Js('Elegant'), Js('Exalted'), Js('Excited'), Js('Exotic'), Js('Famous'), Js('Fancy'), Js('Fantasy'), Js('Fluffy'), Js('Free'), Js('Funny'), Js('Galactic'), Js('Gentle'), Js('Glass'), Js('Golden'), Js('Good'), Js('Green'), Js('Grumpy'), Js('Hairy'), Js('Happy'), Js('Imaginary'), Js('Infamous'), Js('Jade'), Js('Jolly'), Js('Joyful'), Js('Kind'), Js('Laughing'), Js('Legendary'), Js('Light'), Js('Little'), Js('Lost'), Js('Lucky'), Js('Lunar'), Js('Mad'), Js('Merry'), Js('Moving'), Js('Naughty'), Js('Night'), Js('Northern'), Js('Odd'), Js('Orange'), Js('Original'), Js('Playful'), Js('Playing'), Js('Proud'), Js('Quick'), Js('Rare'), Js('Red'), Js('Regal'), Js('Royal'), Js('Running'), Js('Silent'), Js('Silly'), Js('Silver'), Js('Sleeping'), Js('Smart'), Js('Smiling'), Js('Southern'), Js('Tiny'), Js('Twin'), Js('Virtual'), Js('Western'), Js('Wild'), Js('Working'), Js('Young')]))
    var.put('names2', Js([Js('Albatross'), Js('Alligator'), Js('Ant'), Js('Ape'), Js('Bandicoot'), Js('Barnacle'), Js('Barracuda'), Js('Bat'), Js('Bear'), Js('Beaver'), Js('Beetle'), Js('Bird'), Js('Bison'), Js('Boar'), Js('Bull'), Js('Bunny'), Js('Butterfly'), Js('Camel'), Js('Canary'), Js('Cat'), Js('Caterpillar'), Js('Chicken'), Js('Cobra'), Js('Cow'), Js('Coyote'), Js('Crab'), Js('Crane'), Js('Crow'), Js('Deer'), Js('Dingo'), Js('Dino'), Js('Dog'), Js('Donkey'), Js('Dove'), Js('Dragon'), Js('Duck'), Js('Eagle'), Js('Elephant'), Js('Falcon'), Js('Fish'), Js('Fly'), Js('Fox'), Js('Frog'), Js('Goat'), Js('Gopher'), Js('Gorilla'), Js('Hippo'), Js('Horse'), Js('Kitten'), Js('Kiwi'), Js('Lamb'), Js('Lemur'), Js('Leopard'), Js('Lion'), Js('Lizard'), Js('Llama'), Js('Lobster'), Js('Moose'), Js('Mouse'), Js('Otter'), Js('Owl'), Js('Ox'), Js('Panda'), Js('Panther'), Js('Pelican'), Js('Penguin'), Js('Pig'), Js('Pigeon'), Js('Pony'), Js('Prawn'), Js('Pug'), Js('Puppy'), Js('Rabbit'), Js('Raccoon'), Js('Rat'), Js('Raven'), Js('Rhino'), Js('Rooster'), Js('Seal'), Js('Shark'), Js('Sheep'), Js('Shrimp'), Js('Sloth'), Js('Snail'), Js('Snake'), Js('Spider'), Js('Squid'), Js('Squirrel'), Js('Stork'), Js('Swan'), Js('Tiger'), Js('Toad'), Js('Tortoise'), Js('Turtle'), Js('Walrus'), Js('Wasp'), Js('Whale'), Js('Wolf'), Js('Yak'), Js('Zebra')]))
    var.put('names3', Js([Js('Ancient'), Js('Angelic'), Js('Antique'), Js('Aquatic'), Js('Arctic'), Js('Artisan'), Js('Bad'), Js('Blessed'), Js('Blue'), Js('Bright'), Js('Bronze'), Js('Burning'), Js('Cinematic'), Js('Classic'), Js('Clockwork'), Js('Crystal'), Js('Curious'), Js('Dark'), Js('Diamond'), Js('Double'), Js('Eastern'), Js('Electric'), Js('Elegant'), Js('Emerald'), Js('Eternal'), Js('Evony'), Js('Exalted'), Js('Exotic'), Js('Fancy'), Js('Fantasy'), Js('Flaming'), Js('Floating'), Js('Flying'), Js('Frozen'), Js('Giant'), Js('Glass'), Js('Glowing'), Js('Golden'), Js('Granite'), Js('Greater'), Js('Green'), Js('Happy'), Js('Ice'), Js('Imaginary'), Js('Immortal'), Js('Infamous'), Js('Infinite'), Js('Ivory'), Js('Jade'), Js('Laughing'), Js('Legendary'), Js('Light'), Js('Little'), Js('Lonely'), Js('Lost'), Js('Lunar'), Js('Magma'), Js('Magnificent'), Js('Mammoth'), Js('Marble'), Js('Master'), Js('Miracle'), Js('Monochromatic'), Js('Moving'), Js('Night'), Js('Northern'), Js('Odd'), Js('Orange'), Js('Original'), Js('Perfect'), Js('Premium'), Js('Primal'), Js('Rare'), Js('Red'), Js('Regal'), Js('Remote'), Js('Rising'), Js('Royal'), Js('Ruby'), Js('Rusty'), Js('Sapphire'), Js('Shifting'), Js('Shining'), Js('Silent'), Js('Silver'), Js('Smiling'), Js('Smooth'), Js('Snow'), Js('Solar'), Js('Super'), Js('Surprise'), Js('Timeless'), Js('Tiny'), Js('Twin'), Js('Universal'), Js('Vibrant'), Js('Virtual'), Js('Western'), Js('Wild'), Js('Wonder')]))
    var.put('names4', Js([Js('Angel'), Js('Apple'), Js('Arena'), Js('Assistant'), Js('Avenue'), Js('Bandit'), Js('Blossom'), Js('Bond'), Js('Branch'), Js('Bridge'), Js('Brothers'), Js('Candle'), Js('Champion'), Js('Cloud'), Js('Companion'), Js('Cosmos'), Js('Crown'), Js('Dimension'), Js('Dream'), Js('Earth'), Js('Edge'), Js('Embassy'), Js('Empire'), Js('Enigma'), Js('Fantasy'), Js('Figurine'), Js('Fire'), Js('Flow'), Js('Flower'), Js('Gadget'), Js('Galaxy'), Js('Gate'), Js('Giant'), Js('Globe'), Js('Halo'), Js('Heart'), Js('Heaven'), Js('Knight'), Js('Lantern'), Js('Media'), Js('Mind'), Js('Ministry'), Js('Mirror'), Js('Monolith'), Js('Monument'), Js('Moon'), Js('Motion'), Js('Mountain'), Js('Nation'), Js('Nature'), Js('Obelisk'), Js('Orb'), Js('Paradise'), Js('Path'), Js('Petal'), Js('Pinnacle'), Js('Planet'), Js('Portal'), Js('Prism'), Js('Puzzle'), Js('Pyramid'), Js('Rainbow'), Js('Realm'), Js('Ring'), Js('River'), Js('Road'), Js('Robot'), Js('Sapling'), Js('Screen'), Js('Shrine'), Js('Signal'), Js('Sisters'), Js('Sky'), Js('Spire'), Js('Spirit'), Js('Sprite'), Js('Star'), Js('Statue'), Js('Summit'), Js('Sun'), Js('System'), Js('Temple'), Js('Tiara'), Js('Tower'), Js('Town'), Js('Toy'), Js('Tree'), Js('Trinket'), Js('Union'), Js('Universe'), Js('Utopia'), Js('Vault'), Js('Vertex'), Js('Village'), Js('Vortex'), Js('Wall'), Js('Water'), Js('Wings'), Js('Workshop'), Js('World')]))
    var.put('names5', Js([Js('Angel'), Js('Autumn'), Js('Bright'), Js('Chrono'), Js('Cine'), Js('Clock'), Js('Cloud'), Js('Digi'), Js('Film'), Js('Fire'), Js('Free'), Js('Frozen'), Js('Imagi'), Js('Imagine'), Js('Inter'), Js('Intro'), Js('Light'), Js('Lime'), Js('Liquid'), Js('Lunar'), Js('Mega'), Js('Micro'), Js('Mind'), Js('Moon'), Js('Motion'), Js('Movie'), Js('Nether'), Js('Photo'), Js('Pic'), Js('Pro'), Js('Puzzle'), Js('Road'), Js('Silver'), Js('Sky'), Js('Snow'), Js('Solar'), Js('Star'), Js('Summer'), Js('Sun'), Js('Thunder'), Js('Uni'), Js('Wing'), Js('Winter')]))
    var.put('names6', Js([Js('art'), Js('blossom'), Js('bolt'), Js('bunch'), Js('cloud'), Js('dream'), Js('film'), Js('fire'), Js('flix'), Js('flux'), Js('glass'), Js('graphs'), Js('less'), Js('light'), Js('line'), Js('magic'), Js('magine'), Js('mark'), Js('matic'), Js('motion'), Js('myth'), Js('pix'), Js('play'), Js('realm'), Js('saga'), Js('scope'), Js('screen'), Js('soft'), Js('sphere'), Js('storm'), Js('tainment'), Js('tale'), Js('topia'), Js('verse'), Js('wood'), Js('works'), Js('world'), Js('zone')]))
    var.put('names7', Js([Js('Ambience'), Js('Angel Wings'), Js('Anomaly'), Js('Aspect'), Js('Aura'), Js('Aurora'), Js('Azure'), Js('Bliss'), Js('Bullettime'), Js('Century'), Js('Clairvoyant'), Js('Climax'), Js('Crown'), Js('Cyclops'), Js('Destiny'), Js('Dreamland'), Js('Eclipse'), Js('Emerald'), Js('Enchanted'), Js('Enigma'), Js('Enterprise'), Js('Eternity'), Js('Eventide'), Js('Exile'), Js('Fable'), Js('Fantasy'), Js('Fluke'), Js('Fortune'), Js('Galaxy'), Js('Giant'), Js('Gold'), Js('Graphic'), Js('Harmony'), Js('Illusion'), Js('Imagination'), Js('Imagine'), Js('Immortal'), Js('Karma'), Js('Knight'), Js('Legend'), Js('Limbo'), Js('Limelight'), Js('Little Spirit'), Js('Locomotion'), Js('Lunar'), Js('Maximum'), Js('Midnight'), Js('Millenium'), Js('Miracle'), Js('Mithril'), Js('Moon'), Js('Motion'), Js('Mystery'), Js('Mystic'), Js('Mythic'), Js('Nirvana'), Js('Oblivion'), Js('Obscure'), Js('Oracle'), Js('Outcast'), Js('Paradox'), Js('Paragon'), Js('Perception'), Js('Phenomenon'), Js('Picture'), Js('Pinnacle'), Js('Platinum'), Js('Prodigy'), Js('Renegade'), Js('Reverse'), Js('Rising Star'), Js('Rogue'), Js('Ruby'), Js('Saga'), Js('Sapphire'), Js('Sensation'), Js('Silver'), Js('Silver Cloud'), Js('Solar'), Js('Stardust'), Js('Starlight'), Js('Summit'), Js('Sun'), Js('Supreme'), Js('Surprise'), Js('Thunder'), Js('Titan'), Js('Tomorrow'), Js('Transcend'), Js('Trinket'), Js('Twilight'), Js('Ultimate'), Js('Underground'), Js('Utopia'), Js('Vertigo'), Js('Vision'), Js('Vortex'), Js('Wild'), Js('Zion'), Js('Zodiac')]))
    var.put('names8', Js([Js('Entertainment'), Js('Film Company'), Js('Studio'), Js('Pictures'), Js('Productions'), Js('Cinema'), Js('Film'), Js('Filmworks'), Js('Studios'), Js('Film Productions'), Js('Films'), Js('Film Studios')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
            if (var.get('i')<Js(2.0)):
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd1'))+Js(' '))+var.get('names2').get(var.get('rnd2')))+Js(' '))+var.get('names8').get(var.get('rnd'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('names', ((((var.get('names3').get(var.get('rnd1'))+Js(' '))+var.get('names4').get(var.get('rnd2')))+Js(' '))+var.get('names8').get(var.get('rnd'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                        var.put('names', (((var.get('names5').get(var.get('rnd1'))+var.get('names6').get(var.get('rnd2')))+Js(' '))+var.get('names8').get(var.get('rnd'))))
                    else:
                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                        var.put('names', ((var.get('names7').get(var.get('rnd1'))+Js(' '))+var.get('names8').get(var.get('rnd'))))
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
filmStudio = var.to_python()