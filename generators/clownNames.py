__all__ = ['clownNames']

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
    var.put('nm1', Js([Js('Ah Choo'), Js('Alfie'), Js('Antsy'), Js('Augustus'), Js('Baggy'), Js('Bam Bam'), Js('Bashful'), Js('Bee'), Js('Beebee'), Js('Berry'), Js('Bim Bam'), Js('Bimbo'), Js('Bingo'), Js('Binky'), Js('Blinky'), Js('Blossom'), Js('Bobo'), Js('Bonbon'), Js('Bongo'), Js('Bonzo'), Js('Booboo'), Js('Boom Boom'), Js('Boxy'), Js('Bozo'), Js('Britches'), Js('Bronco'), Js('Bucket'), Js('Buddy'), Js('Buffo'), Js('Buffoon'), Js('Buster'), Js('Buttercup'), Js('Buttons'), Js('Candy'), Js('Casey'), Js('Charlie'), Js('Cheeky'), Js('Cheery'), Js('Chester'), Js('Choco'), Js('Choochoo'), Js('Chubby'), Js('Chuckles'), Js('Clarabell'), Js('Clueless'), Js('Clumsy'), Js('Coocoo'), Js('Cookie'), Js('Cornflake'), Js('Crafty'), Js('Cupcake'), Js('Curly'), Js('Daffy'), Js('Daisy'), Js('Dazzle'), Js('Dazzler'), Js('Digger'), Js('Dimdim'), Js('Dimple'), Js('Dimples'), Js('Dinky'), Js('Ditso'), Js('Doodles'), Js('Duckie'), Js('Dumbo'), Js('Dumpling'), Js('Dumpty'), Js('Dusty'), Js('Echo'), Js('Feathers'), Js('Floppy'), Js('Flopsy'), Js('Flower'), Js('Fluffy'), Js('Flutter'), Js('Freckles'), Js('Frosty'), Js('Giggle'), Js('Giggles'), Js('Gogo'), Js('Goofy'), Js('Googles'), Js('Happy'), Js('Harpo'), Js('Humpty'), Js('Jazzy'), Js('Jester'), Js('Jimbo'), Js('Jingles'), Js('Joey'), Js('Jojo'), Js('Joy'), Js('Jumbo'), Js('Junior'), Js('Kicker'), Js('Knicknack'), Js('Koko'), Js('Lala'), Js('Loko'), Js('Lollypop'), Js('Loof'), Js('Loofy'), Js('Loopy'), Js('Lucky'), Js('Lulu'), Js('Luna'), Js('Marble'), Js('Marbles'), Js('Mickey'), Js('Miko'), Js('Milo'), Js('Minstrel'), Js('Mittens'), Js('Molly'), Js('Monkey'), Js('Nanners'), Js('Noodles'), Js('Oddball'), Js('Pancake'), Js('Patch'), Js('Patches'), Js('Pickles'), Js('Pockets'), Js('Pogo'), Js('Poodles'), Js('Popsy'), Js('Puddles'), Js('Pumpkin'), Js('Raffles'), Js('Riddles'), Js('Ruffles'), Js('Scooter'), Js('Scruffy'), Js('Shaggy'), Js('Shorty'), Js('Skippy'), Js('Skittles'), Js('Smiley'), Js('Snickers'), Js('Snoots'), Js('Snuggles'), Js('Soots'), Js('Sparkle'), Js('Sparkles'), Js('Sparks'), Js('Sparky'), Js('Squeaks'), Js('Squigley'), Js('Squishy'), Js('Sugar'), Js('Sunshine'), Js('Tatters'), Js('Tickle'), Js('Tickles'), Js('Tiny'), Js('Toodles'), Js('Tootsy'), Js('Topsy'), Js('Trixy'), Js('Tubby'), Js('Twinkles'), Js('Velvet'), Js('Waldo'), Js('Wally'), Js('Whistle'), Js('Wiggles'), Js('Witty'), Js('Yoyo'), Js('Zeppy'), Js('Zippy')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('names', var.get('nm1').get(var.get('rnd')))
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
clownNames = var.to_python()