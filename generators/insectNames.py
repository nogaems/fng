__all__ = ['insectNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Alpha'), Js('Apollo'), Js('Aragog'), Js('Ash'), Js('Ashes'), Js('Asterix'), Js('Aztec'), Js('Bandit'), Js('Beta'), Js('Biggelsworth'), Js('Bilbo'), Js('Blade'), Js('Blitz'), Js('Booker'), Js('Boomer'), Js('Boots'), Js('Brutus'), Js('Buddy'), Js('Bugs'), Js('Butch'), Js('Buttons'), Js('Casper'), Js('Celeb'), Js('Chewbacca'), Js('Chewy'), Js('Chinook'), Js('Chuck'), Js('Chuckles'), Js('Cinder'), Js('Cole'), Js('Comet'), Js('Cookie'), Js('Cosmo'), Js('Critter'), Js('Cuddles'), Js('Darcy'), Js('Dexter'), Js('Doc'), Js('Doodle'), Js('Dracula'), Js('Echo'), Js('Fangs'), Js('Flopsie'), Js('Frankenstein'), Js('Friskie'), Js('Fuzz'), Js('Fuzzy'), Js('Gadget'), Js('Gambit'), Js('Ghost'), Js('Godzilla'), Js('Goliath'), Js('Handsome'), Js('Hannibal'), Js('Hector'), Js('Hercules'), Js('Houdini'), Js('Hulk'), Js('Hunter'), Js('Icky'), Js('Ivan'), Js('Jaffa'), Js('Jiggles'), Js('Jitters'), Js('Junior'), Js('Lance'), Js('Lancelot'), Js('Loki'), Js('Lucifer'), Js('Magma'), Js('Marble'), Js('Midnight'), Js('Mittens'), Js('Muffin'), Js('Myst'), Js('Nacho'), Js('Nemesis'), Js('Nightmare'), Js('Noodle'), Js('Noodles'), Js('Nugget'), Js('Omega'), Js('Onyx'), Js('Orion'), Js('Ozzy'), Js('Patches'), Js('Peanut'), Js('Pepper'), Js('Phantom'), Js('Pickles'), Js('Poison'), Js('Poppers'), Js('Prometheus'), Js('Psyche'), Js('Psycho'), Js('Punky'), Js('Rambo'), Js('Rascal'), Js('Rebel'), Js('Rex'), Js('Rider'), Js('Rufus'), Js('Rusty'), Js('Salt'), Js('Scooter'), Js('Scratch'), Js('Scruff'), Js('Scruffy'), Js('Shade'), Js('Shadow'), Js('Sherlock'), Js('Skinner'), Js('Skipper'), Js('Slinky'), Js('Snickers'), Js('Snyder'), Js('Sox'), Js('Spike'), Js('Spinner'), Js('Squeaks'), Js('Stitches'), Js('Storm'), Js('Striker'), Js('Syd'), Js('Sylvester'), Js('Symore'), Js('Taboo'), Js('Tank'), Js('Thor'), Js('Thunder'), Js('Tinker'), Js('Titan'), Js('Trapper'), Js('Tremor'), Js('Truffle'), Js('Tyson'), Js('Venom'), Js('Webster'), Js('Whiskers'), Js('Whisper'), Js('Wolfgang'), Js('Xanadu'), Js('Xander'), Js('Ziggy')]))
var.put('nm2', Js([Js('Aggie'), Js('Akeeta'), Js('Alexei'), Js('Amber'), Js('Angel'), Js('Angi'), Js('Arachne'), Js('Arack'), Js('Aragi'), Js('Arania'), Js('Ash'), Js('Athena'), Js('Aura'), Js('Aurora'), Js('Babe'), Js('Beauty'), Js('Becky'), Js('Belle'), Js('Bitsy'), Js('Bizzie'), Js('Blossom'), Js('Breeze'), Js('Brizzie'), Js('Buffy'), Js('Bugsy'), Js('Bumble'), Js('Buttercup'), Js('Button'), Js('Buttons'), Js('Calico'), Js('Calypso'), Js('Candy'), Js('Carmen'), Js('Celeb'), Js('Charlotte'), Js('Charm'), Js('Cheeky'), Js('Chica'), Js('Cinders'), Js('Clarice'), Js('Cleo'), Js('Coco'), Js('Cookie'), Js('Coraline'), Js('Cotton'), Js('Crawline'), Js('Creepette'), Js('Crystal'), Js('Cuddles'), Js('Daisy'), Js('Dawn'), Js('Delilah'), Js('Dodger'), Js('Dot'), Js('Dotty'), Js('Ebony'), Js('Echo'), Js('Eek'), Js('Eep'), Js('Ember'), Js('Enigma'), Js('Fancy'), Js('Fangs'), Js('Flopsy'), Js('Fluffy'), Js('Freckles'), Js('Fuzzles'), Js('Gadget'), Js('Gertrude'), Js('Giggles'), Js('Gloria'), Js('Happy'), Js('Hugsie'), Js('Hyve'), Js('Incy'), Js('Indi'), Js('Iris'), Js('Itsy'), Js('Ivory'), Js('Jaffa'), Js('Jewel'), Js('Jiggly'), Js('Jinx'), Js('Jitters'), Js('Juicy'), Js('Jynx'), Js('Kisses'), Js('Klaxie'), Js('Lacy'), Js('Lady'), Js('Legs'), Js('Lucky'), Js('Lucy'), Js('Lulu'), Js('Midnight'), Js('Missy'), Js('Mittens'), Js('Morticia'), Js('Mothrine'), Js('Mystique'), Js('Pandora'), Js('Paws'), Js('Pebble'), Js('Pebbles'), Js('Phobia'), Js('Pickle'), Js('Pickles'), Js('Poison'), Js('Princess'), Js('Psyche'), Js('Queen'), Js('Raven'), Js('Rosebud'), Js('Rune'), Js('Scarlet'), Js('Scruffles'), Js('Serenity'), Js('Shade'), Js('Shelley'), Js('Shelob'), Js('Siri'), Js('Skitters'), Js('Skittles'), Js('Skreech'), Js('Snickers'), Js('Snuggle'), Js('Snuggles'), Js('Socks'), Js('Spindle'), Js('Spindles'), Js('Spindra'), Js('Squiggles'), Js('Squiggly'), Js('Squirmy'), Js('Stingy'), Js('Sugar'), Js('Sunshine'), Js('Tabitha'), Js('Tickle'), Js('Tickles'), Js('Tilly'), Js('Tinkerbelle'), Js('Toots'), Js('Twilight'), Js('Twitchy'), Js('Velvet'), Js('Venom'), Js('Violet'), Js('Waffle'), Js('Webzie'), Js('Xena'), Js('Ziggy')]))
pass
pass


# Add lib to the module scope
insectNames = var.to_python()