__all__ = ['nicknames']

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
var.put('nm1', Js([Js('Ace'), Js('Admiral'), Js('Aggy'), Js('Angel'), Js('Animal'), Js('Answer'), Js('Aqua'), Js('Arrow'), Js('Artsy'), Js('Assassin'), Js('Babe'), Js('Baby'), Js('Bad Boy'), Js('Baldy'), Js('Bambam'), Js('Barber'), Js('Bash'), Js('Basher'), Js('Beans'), Js('Bear'), Js('Beard'), Js('Beast'), Js('Beau'), Js('Beauty'), Js('Belle'), Js('Berry'), Js('Big Boy'), Js('Big Dog'), Js('Bigby'), Js('Biggie'), Js('Bigshot'), Js('Bing'), Js('Bingo'), Js('Bird'), Js('Birds'), Js('Bitsy'), Js('Black Magic'), Js('Black Widow'), Js('Blackjack'), Js('Blade'), Js('Blessed'), Js('Blondie'), Js('Blossom'), Js('Blue'), Js('Blush'), Js('Bo'), Js('Bobo'), Js('Bones'), Js('Boogie'), Js('Boomer'), Js('Boots'), Js('Braveheart'), Js('Brick'), Js('Brow'), Js('Buck'), Js('Bucket'), Js('Bud'), Js('Buddy'), Js('Bugs'), Js('Bull'), Js('Bulldog'), Js('Bullet'), Js('Bullseye'), Js('Bunny'), Js('Buster'), Js('Butch'), Js('Butcher'), Js('Butterfly'), Js('Buzz'), Js('Camille'), Js('Candy'), Js('Cannonball'), Js('Captain'), Js('Chappie'), Js('Charisma'), Js('Cheery'), Js('Chef'), Js('Chief'), Js('Chip'), Js('Chipper'), Js('Chuck'), Js('Cloud'), Js('Cobra'), Js('Comet'), Js('Coocoo'), Js('Cookie'), Js('Coyote'), Js('Crash'), Js('Creed'), Js('Creep'), Js('Crow'), Js('Cryo'), Js('Crystal'), Js('Cuddles'), Js('Curles'), Js('Cutie'), Js('Cyclone'), Js('Cyclops'), Js('Daddy'), Js('Dagger'), Js('Dandy'), Js('Dapper'), Js('Daring'), Js('Darlin'), Js('Darling'), Js('Dash'), Js('Dawg'), Js('Daydream'), Js('Dazzle'), Js('Dealer'), Js('Deedee'), Js('Delight'), Js('Demon'), Js('Devil'), Js('Diamond'), Js('Dice'), Js('Digger'), Js('Dimple'), Js('Dino'), Js('Dizzy'), Js('Doc'), Js('Dodo'), Js('Dog'), Js('Doggie'), Js('Double'), Js('Double Trouble'), Js('Dragon'), Js('Dream'), Js('Ducky'), Js('Duke'), Js('Dumdum'), Js('Dummy'), Js('Dusty'), Js('Dutch'), Js('Dynamite'), Js('Eagle'), Js('Fancy'), Js('Feathers'), Js('Fire'), Js('Fish'), Js('Flame'), Js('Flash'), Js('Flip'), Js('Flutters'), Js('Fortuna'), Js('Fox'), Js('Freak'), Js('Frosty'), Js('Fury'), Js('Fuzz'), Js('Fuzzy'), Js('Gator'), Js('Gem'), Js('Genie'), Js('Genius'), Js('Gentle'), Js('Gibbs'), Js('Gibby'), Js('Gigi'), Js('Gilly'), Js('Ginger'), Js('Glide'), Js('Gonzo'), Js('Goose'), Js('Grace'), Js('Grim'), Js('Groovy'), Js('Grouch'), Js('Growl'), Js('Guns'), Js('Gus'), Js('Hammer'), Js('Handsome'), Js('Happy'), Js('Hawk'), Js('Hawkeye'), Js('Hog'), Js('Honesty'), Js('Honey'), Js('Hooks'), Js('Horse'), Js('Hound'), Js('Hurricane'), Js('Ice'), Js('Icicle'), Js('Indie'), Js('Iron'), Js('Izzy'), Js('Jackal'), Js('Jacket'), Js('Jackhammer'), Js('Jade'), Js('Jazzy'), Js('Jelly'), Js('Jewel'), Js('Joker'), Js('Jolly'), Js('Jumbo'), Js('Jumper'), Js('Kiki'), Js('Killer'), Js('Kindle'), Js('King'), Js('Knight'), Js('Landslide'), Js('Lightning'), Js('Lion'), Js('Lioness'), Js('Little'), Js('Lock'), Js('Loco'), Js('Lucky'), Js('Mac'), Js('Machine'), Js('Mad'), Js('Mad Dog'), Js('Magic'), Js('Magica'), Js('Magician'), Js('Major'), Js('Mamba'), Js('Mania'), Js('Maniac'), Js('Marvel'), Js('Mayor'), Js('Mellow'), Js('Memo'), Js('Merry'), Js('Micro'), Js('Miracle'), Js('Missile'), Js('Mistletoe'), Js('Mitzi'), Js('Monk'), Js('Moose'), Js('Mouse'), Js('Mugs'), Js('Mugsy'), Js('Mule'), Js('Mutt'), Js('Navigator'), Js('Nimble'), Js('Old Buck'), Js('Oracle'), Js('Ox'), Js('Peanut'), Js('Penny'), Js('Petit'), Js('Pig'), Js('Piggy'), Js('Pipi'), Js('Pitch'), Js('Pogo'), Js('Poncho'), Js('Pops'), Js('Porky'), Js('Pretzel'), Js('Prince'), Js('Princess'), Js('Pug'), Js('Pugs'), Js('Punch'), Js('Pyro'), Js('Queen Bee'), Js('Queenie'), Js('Rags'), Js('Reaper'), Js('Rebel'), Js('Red'), Js('Rip'), Js('Ripper'), Js('Robin'), Js('Rock'), Js('Rogue'), Js('Rose'), Js('Rouge'), Js('Ruby'), Js('Ruin'), Js('Rusty'), Js('Sage'), Js('Sailor'), Js('Sandy'), Js('Sassy'), Js('Scoop'), Js('Scruffy'), Js('Serpent'), Js('Shade'), Js('Shadow'), Js('Shark'), Js('Sheep'), Js('Shorty'), Js('Shrimp'), Js('Shy'), Js('Silence'), Js('Silly'), Js('Silver'), Js('Sizzle'), Js('Sketch'), Js('Skin'), Js('Skinny'), Js('Skip'), Js('Skipper'), Js('Skippy'), Js('Slash'), Js('Slayer'), Js('Slick'), Js('Slide'), Js('Slim'), Js('Small'), Js('Smash'), Js('Smasher'), Js('Smiley'), Js('Smitty'), Js('Smoothie'), Js('Snake'), Js('Snowflake'), Js('Spark'), Js('Sparkle'), Js('Sparky'), Js('Sparrow'), Js('Special'), Js('Speed'), Js('Spider'), Js('Spike'), Js('Spud'), Js('Spuds'), Js('Starfall'), Js('Steel'), Js('Sticks'), Js('Stone'), Js('Storm'), Js('Stout'), Js('Stretch'), Js('Stuffy'), Js('Sugar'), Js('T-Bone'), Js('Tank'), Js('Terminator'), Js('Thief'), Js('Thunder'), Js('Tiger'), Js('Tigress'), Js('Tiny'), Js('Titch'), Js('Toon'), Js('Torch'), Js('Trey'), Js('Tricky'), Js('Trouble'), Js('Tug'), Js('Turk'), Js('Twinkle'), Js('Twinkle Toes'), Js('Twitch'), Js('Uncle'), Js('Undertaker'), Js('Vanilla'), Js('Viper'), Js('Vulture'), Js('Wheels'), Js('Whopper'), Js('Wiggles'), Js('Wild'), Js('Wildy'), Js('Wiz'), Js('Wonder'), Js('Worm'), Js('Yank'), Js('Zen'), Js('Zero'), Js('Ziggy')]))
pass
pass


# Add lib to the module scope
nicknames = var.to_python()