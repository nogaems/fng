__all__ = ['candyNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Angels'), Js('Angelwings'), Js('Animazings'), Js('Appies'), Js('Baboons'), Js('Baboos'), Js('Bakies'), Js('Banananice'), Js('Banonza'), Js('Banonzas'), Js('Banzais'), Js('Barbarians'), Js('Beaks'), Js('Beardies'), Js('Bingbongs'), Js('Bitbites'), Js('Bits'), Js('Bitterbutter'), Js('Blasters'), Js('Blossoms'), Js('Blues'), Js('Bomboons'), Js('Booboos'), Js('Boombun'), Js('Booters'), Js('Braids'), Js('Brattles'), Js('Brittles'), Js('Buggles'), Js('Bumbles'), Js('Bundles'), Js('Bunnies'), Js('Butterflies'), Js('Buzzers'), Js('Caramellows'), Js('Cerealice'), Js('Cheddies'), Js('Cheekies'), Js('Cheeries'), Js('Cheeselocks'), Js('Cheezies'), Js('Chestnutters'), Js('Chewies'), Js('Chippies'), Js('Chocakes'), Js('Chococanes'), Js('Chuckles'), Js('Chunkies'), Js('Cocoons'), Js('Cocos'), Js('Coils'), Js('Comets'), Js('Coolies'), Js('Coyoties'), Js('Crackles'), Js('Crawlies'), Js('Creamies'), Js('Crescents'), Js('Crispies'), Js('Crumblers'), Js('Crumblies'), Js('Crunchers'), Js('Crusties'), Js('Cubies'), Js('Cupids'), Js('Custart'), Js('Damias'), Js('Delicies'), Js('Dewies'), Js('Diggies'), Js('Dimdums'), Js('Doodles'), Js('Doofies'), Js("Doughno's"), Js('Dragons'), Js('Drivers'), Js('Droplets'), Js('Dubbles'), Js('Dubloons'), Js('Dumdums'), Js('Fairy Rings'), Js('Fancakes'), Js('Fanties'), Js('Fiddlesticks'), Js('Fidge'), Js('Fidgies'), Js('Figles'), Js('Flakies'), Js('Flappers'), Js('Fluxies'), Js('Fortunes'), Js('Frazzles'), Js('Fruities'), Js('Fusers'), Js('Galaxies'), Js('Gingies'), Js('Gnomies'), Js('Gobbles'), Js('Goldies'), Js('Gooeys'), Js('Goofies'), Js('Googlies'), Js('Growlies'), Js('Grumbles'), Js('Gumbies'), Js('Gumbles'), Js('Haggles'), Js('Halos'), Js('Heartstones'), Js('Hoots'), Js('Howlers'), Js('Huckles'), Js('Huffles'), Js('Humhums'), Js('Hushies'), Js('Jabbers'), Js('Jazzles'), Js('Jesters'), Js('Jice'), Js('Jimbles'), Js('Jingles'), Js('Jokers'), Js('Jumpers'), Js('Khandi'), Js('Lasers'), Js('Lemones'), Js('Loopies'), Js('Lumpies'), Js('Lunas'), Js('Luscies'), Js('Magmas'), Js('Marbles'), Js('Marvels'), Js('Mellows'), Js('Melties'), Js('Mergies'), Js('Merries'), Js('Milkies'), Js('Miracles'), Js('Mockers'), Js('Moomoos'), Js('Muffles'), Js('Mumbles'), Js('Mummies'), Js('Munchers'), Js('Munties'), Js('Nacheeze'), Js('Neptunes'), Js('Nudgefudge'), Js('Nutters'), Js('Oaties'), Js('Partles'), Js('Pastels'), Js('Pasties'), Js('Pawpaws'), Js('Petals'), Js('Picolocos'), Js('Picos'), Js('Piglets'), Js('Pinkies'), Js('Pippops'), Js('Pizzaz'), Js('Poofs'), Js('Pretties'), Js('Prickles'), Js('Puds'), Js('Puffles'), Js('Puffs'), Js('Pulpies'), Js('Pummels'), Js('Pumples'), Js('Raffits'), Js('Raffles'), Js('Rainbows'), Js('Rascals'), Js('Rebels'), Js('Ribbles'), Js('Rickets'), Js('Rifrafs'), Js('Riglies'), Js('Rimbas'), Js('Riots'), Js('Ripples'), Js('Roars'), Js('Rolers'), Js('Roley Poley'), Js('Rollies'), Js('Rompers'), Js('Rubies'), Js('Rumbles'), Js('Rumbuns'), Js('Salties'), Js('Samsams'), Js('Samsos'), Js('Sapphires'), Js('Shakies'), Js('Shazams'), Js('Shinies'), Js('Shorties'), Js('Slapples'), Js('Sluicies'), Js('Smashers'), Js('Smoots'), Js('Snappers'), Js('Snipsnaps'), Js('Snowballs'), Js('Snowflakes'), Js('Sparklers'), Js('Speakers'), Js('Spikes'), Js('Sponges'), Js('Spoofs'), Js('Squirmies'), Js('Stampers'), Js('Stripies'), Js('Sugies'), Js('Sunies'), Js('Sweeties'), Js('Swirvels'), Js('Tackles'), Js('Tea-ser'), Js('Teasers'), Js('Tempies'), Js('Thrillers'), Js('Tiftofs'), Js('Timbles'), Js('Timtums'), Js('Trailers'), Js('Troofles'), Js('Twiglies'), Js('Twinkles'), Js('Twisters'), Js('Twitters'), Js('Vampies'), Js('Waggles'), Js('Wallops'), Js('Whippers'), Js('Whippersnappers'), Js('Whoopees'), Js('Wibbles'), Js('Wiggles'), Js('Wisecrackers'), Js('Witties'), Js('Wizards'), Js('Wonkies'), Js('Wrilies'), Js('Wrinklies'), Js('Yahoos'), Js('Yumyums'), Js('Zigzags'), Js('Zoots')]))
pass
pass


# Add lib to the module scope
candyNames = var.to_python()