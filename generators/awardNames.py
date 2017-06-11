__all__ = ['awardNames']

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
    var.registers(['nm1', 'nm2', 'nm3', 'result'])
    var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('Acclaimed'), Js('Adept'), Js('Arcane'), Js('Artistic'), Js('Aurora'), Js('Austere'), Js('Bold'), Js('Brass'), Js('Bravery'), Js('Bright'), Js('Brilliant'), Js('Candid'), Js("Children's"), Js('Clever'), Js('Comfort'), Js('Complexity'), Js('Confusion'), Js('Convention'), Js('Crafty'), Js('Creation'), Js('Creative'), Js('Critic'), Js("Critics'"), Js('Crystal'), Js('Dapper'), Js('Defiant'), Js('Diamond'), Js('Discovery'), Js('Discretion'), Js('Dual'), Js('Duality'), Js('Earnesty'), Js('Education'), Js('Elegance'), Js('Elegant'), Js('Elementary'), Js('Enchanted'), Js('Enlightened'), Js('Ethic'), Js('Exalted'), Js('Excellence'), Js('Experience'), Js('Expert'), Js('Expertise'), Js('Fantasy'), Js('Fashion'), Js('Flawless'), Js('Fragrant'), Js('Free'), Js('Future'), Js('Gentle'), Js('Golden'), Js('Graceful'), Js('Gracious'), Js('Grand'), Js('Guardian'), Js('Handy'), Js('Harmony'), Js('Health'), Js('Healthy'), Js('Honest'), Js('Honesty'), Js('Honor'), Js('Honored'), Js('Humane'), Js('Humanity'), Js('Humble'), Js('Imagination'), Js('Impossible'), Js('Incredible'), Js('Independent'), Js('Infinity'), Js('Informed'), Js('Innocence'), Js('Intelligence'), Js('Intelligent'), Js('International'), Js('Intrepid'), Js('Jade'), Js('Jubilant'), Js('Knowledge'), Js('Life'), Js('Light'), Js('Literary'), Js('Logic'), Js('Loyalty'), Js('Luminous'), Js('Luna'), Js('Lunar'), Js('Magic'), Js('Majestic'), Js('Majesty'), Js('Medicine'), Js('Melody'), Js('Merry'), Js('Miniature'), Js('Motion'), Js('Mysterious'), Js('Mystery'), Js('National'), Js('Natural'), Js('Nature'), Js('Neo'), Js('New'), Js('Novel'), Js('Novice'), Js('Passion'), Js('Peace'), Js("People's"), Js('Pointless'), Js('Possibility'), Js('Power'), Js('Perseverance'), Js('Prime'), Js("Public's"), Js('Regal'), Js('Ruby'), Js('Sanity'), Js('Sapphire'), Js('Science'), Js('Short'), Js('Silk'), Js('Silver'), Js('Solar'), Js('Soul'), Js('Stellar'), Js('Style'), Js('Stylish'), Js('Superior'), Js('Sympathy'), Js('Teen'), Js('Terror'), Js('Truth'), Js('Twin'), Js('Unity'), Js('Unsung'), Js('Velvet'), Js('Vigilant'), Js('Virtuous'), Js('Warped'), Js('Wisdom'), Js('Wise'), Js('Young')]))
    var.put('nm2', Js([Js('Act'), Js('Actor'), Js('Performance'), Js('Performer'), Js('Answer'), Js('Art'), Js('Atom'), Js('Badge'), Js('Balloon'), Js('Band'), Js('Bear'), Js('Bell'), Js('Bird'), Js('Book'), Js('Camera'), Js('Canvas'), Js('Chance'), Js('Change'), Js('Cherry'), Js('Choice'), Js('Clover'), Js('Comet'), Js('Cord'), Js('Creator'), Js('Crown'), Js('Curtain'), Js('Cushion'), Js('Dance'), Js('Design'), Js('Droplet'), Js('Eagle'), Js('Education'), Js('Engine'), Js('Example'), Js('Eye'), Js('Fan'), Js('Feather'), Js('Film'), Js('Fingerprint'), Js('Flame'), Js('Flower'), Js('Footprint'), Js('Globe'), Js('Glove'), Js('Halo'), Js('Hammer'), Js('Heart'), Js('Hero'), Js('Horse'), Js('Image'), Js('Impulse'), Js('Instrument'), Js('Invention'), Js('Iris'), Js('Jewel'), Js('Ladybug'), Js('Laugh'), Js('Leaf'), Js('Lion'), Js('Locket'), Js('Machine'), Js('Mark'), Js('Mask'), Js('Melody'), Js('Monkey'), Js('Moon'), Js('Mouse'), Js('Music'), Js('Owl'), Js('Palm'), Js('Performance'), Js('Press'), Js('Print'), Js('Pulse'), Js('Question'), Js('Question Mark'), Js('Quill'), Js('Quiver'), Js('Record'), Js('Ribbon'), Js('Smile'), Js('Snail'), Js('Song'), Js('Spade'), Js('Star'), Js('Sun'), Js('Taste'), Js('Theory'), Js('Throne'), Js('Tune'), Js('Veil'), Js('Wand'), Js('Wing')]))
    var.put('nm3', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('Accolade'), Js('Award'), Js('Award'), Js('Award'), Js('Award'), Js('Award'), Js('Award'), Js('Award'), Js('Award'), Js('Award'), Js('Award'), Js('Grant'), Js('Hall of Fame'), Js('Hall of Fame Award'), Js('Prize'), Js('Prize for Quality'), Js('Quality Award'), Js('Trophy'), Js('of the Year')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq(var.get('nm1').get(var.get('rnd')),Js('')):
                while (var.get('rnd3')<Js(5.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('names', (((((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
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
awardNames = var.to_python()