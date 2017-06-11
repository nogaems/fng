__all__ = ['jewelryNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm2', 'result'])
    var.put('nm1', Js([Js('Adored'), Js('Agate'), Js('Aged'), Js('Amber'), Js('Amethyst'), Js('Ancient'), Js('Angel'), Js('Angelic'), Js('Anonymous'), Js('Antique'), Js('Arctic'), Js('Austere'), Js('Azure'), Js('Blind'), Js('Blushing'), Js('Brave'), Js('Bright'), Js('Brilliant'), Js('Broken'), Js('Citrine'), Js('Colossal'), Js('Coral'), Js('Crisp'), Js('Crystal'), Js('Curly'), Js('Curvy'), Js('Darling'), Js('Dearest'), Js('Defiant'), Js('Devoted'), Js('Diamond'), Js('Diligent'), Js('Earnest'), Js('Elated'), Js('Elegant'), Js('Emerald'), Js('Enchanted'), Js('Enchanting'), Js('Enlightened'), Js('Exalted'), Js('Exotic'), Js('Faint'), Js('Fair'), Js('Feline'), Js('Flawless'), Js('Forsaken'), Js('Free'), Js('Frozen'), Js('Garnet'), Js('Gentle'), Js('Gifted'), Js('Glistening'), Js('Graceful'), Js('Gracious'), Js('Grand'), Js('Grateful'), Js('Handsome'), Js('Happy'), Js('Harmonious'), Js('Heaven'), Js('Heavenly'), Js('Hematite'), Js('Honest'), Js('Humble'), Js('Idle'), Js('Illustrious'), Js('Impossible'), Js('Infinite'), Js('Innocent'), Js('Jade'), Js('Jasper'), Js('Lavish'), Js('Lonely'), Js('Loyal'), Js('Luminous'), Js('Lunar'), Js('Lustrous'), Js('Majestic'), Js('Malachite'), Js('Mellow'), Js('Mysterious'), Js('Obsidian'), Js('Ocean'), Js('Onyx'), Js('Parallel'), Js('Peace'), Js('Peaceful'), Js('Pearl'), Js('Perfect'), Js('Pink'), Js('Playful'), Js('Precious'), Js('Pristine'), Js('Proud'), Js('Pure'), Js('Purity'), Js('Quiet'), Js('Royal'), Js('Ruby'), Js('Sapphire'), Js('Scented'), Js('Secret'), Js('Serene'), Js('Serpent'), Js('Serpentine'), Js('Shadow'), Js('Silent'), Js('Sinful'), Js('Solar'), Js('Spinel'), Js('Spotless'), Js('Stunning'), Js('Sweet'), Js('Tempting'), Js('Tender'), Js('Tinted'), Js('Unmounted'), Js('Velvet'), Js('Vibrant'), Js('Violet'), Js('Virtuous'), Js('Worthy'), Js('Zircon')]))
    var.put('nm2', Js([Js('Ambition'), Js('Aura'), Js('Balance'), Js('Bauble'), Js('Beauty'), Js('Belle'), Js('Blessing'), Js('Bliss'), Js('Blossom'), Js('Bond'), Js('Breath'), Js('Bubble'), Js('Charm'), Js('Class'), Js('Clover'), Js('Core'), Js('Crescent'), Js('Crest'), Js('Cross'), Js('Crux'), Js('Desire'), Js('Devotion'), Js('Dewdrop'), Js('Dream'), Js('Drop'), Js('Droplet'), Js('Eye'), Js('Fan'), Js('Favor'), Js('Flame'), Js('Flower'), Js('Focus'), Js('Force'), Js('Gift'), Js('Glamour'), Js('Globe'), Js('Grace'), Js('Heart'), Js('Hope'), Js('Hum'), Js('Hymn'), Js('Image'), Js('Leaf'), Js('Life'), Js('Light'), Js('Lily'), Js('Love'), Js('Lure'), Js('Mark'), Js('Memorial'), Js('Mind'), Js('Moon'), Js('Oath'), Js('Oculus'), Js('Orb'), Js('Palm'), Js('Panther'), Js('Passion'), Js('Petal'), Js('Pledge'), Js('Poem'), Js('Prayer'), Js('Promise'), Js('Prospect'), Js('Rainbow'), Js('Resolve'), Js('Riddle'), Js('Rock'), Js('Root'), Js('Scale'), Js('Seal'), Js('Shield'), Js('Song'), Js('Soul'), Js('Spark'), Js('Spiral'), Js('Spirit'), Js('Star'), Js('Stone'), Js('Sun'), Js('Swan'), Js('Tear'), Js('Teardrop'), Js('Tempest'), Js('Tribute'), Js('Trinket'), Js('Twin'), Js('Twins'), Js('Twirl'), Js('Twist'), Js('Valor'), Js('Vigor'), Js('Vision'), Js('Voice'), Js('Vow'), Js('Whisper'), Js('Will'), Js('Wing'), Js('Wings'), Js('Wish')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            else:
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
var.put('nm3', Js([Js('Tiara'), Js('Necklace'), Js('Amulet'), Js('Bracelet'), Js('Ornament'), Js('Pendant'), Js('Ring'), Js('Pin'), Js('Choker'), Js('Anklet'), Js('Brooch'), Js('Necklace'), Js('Amulet'), Js('Bracelet'), Js('Pendant'), Js('Ring')]))
pass
pass


# Add lib to the module scope
jewelryNames = var.to_python()