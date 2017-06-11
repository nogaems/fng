__all__ = ['oasisNames']

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
    var.put('nm1', Js([Js('Abyssal'), Js('Airy'), Js('Amber'), Js('Ancient'), Js('Angelic'), Js('Arcane'), Js('Arctic'), Js('Aromatic'), Js('Aurora'), Js('Awoken'), Js('Azure'), Js('Beryl'), Js('Blossom'), Js('Blossoming'), Js('Blue Moon'), Js('Blushing'), Js('Boiling'), Js('Bold'), Js('Brilliant'), Js('Bronze'), Js('Bubbling'), Js('Carmine'), Js('Cerulean'), Js('Changing'), Js('Chasm'), Js('Chittering'), Js('Chuckling'), Js('Claret'), Js('Cleansing'), Js('Coiling'), Js('Convex'), Js('Crane'), Js('Crawling'), Js('Crescent'), Js('Croaking'), Js('Curiosity'), Js('Curious'), Js('Dahlia'), Js('Dancing'), Js('Dark'), Js('Daydream'), Js('Demilune'), Js('Discovery'), Js('Divine'), Js('Eastern'), Js('Ebony'), Js('Electric'), Js('Empty'), Js('Enchanted'), Js('Enchanting'), Js('Enigma'), Js('Enlightened'), Js('Enlightenment'), Js('Evergreen'), Js('False'), Js('Firefly'), Js('Flickering'), Js('Foggy'), Js('Forbidden'), Js('Forsaken'), Js('Fragrant'), Js('Frozen'), Js('Geiser'), Js('Glass'), Js('Gleaming'), Js('Glistening'), Js('Glowing'), Js('Golden'), Js('Grand'), Js('Great'), Js('Halcyon'), Js('Half'), Js('Harmony'), Js('Hollow'), Js('Holy'), Js('Hotspring'), Js('Infinite'), Js('Infinity'), Js('Ivory'), Js('Jade'), Js('Laughing'), Js('Lava'), Js('Little'), Js('Living'), Js('Lone'), Js('Lonely'), Js('Lost'), Js('Luminous'), Js('Lunar'), Js('Lune'), Js('Lurking'), Js('Lustrious'), Js('Lustrous'), Js('Magma'), Js('Majestic'), Js('Malachite'), Js('Mammoth'), Js('Maroon'), Js('Meditating'), Js('Meditation'), Js('Merry'), Js('Mountain'), Js('Mumbling'), Js('Mystery'), Js('Nightmare'), Js('Northern'), Js('Observing'), Js('Oracle'), Js('Ornate'), Js('Petal'), Js('Phantom'), Js('Pinnacle'), Js('Pioneer'), Js('Prime'), Js('Radiant'), Js('Raging'), Js('Repose'), Js('Resting'), Js('Roaring'), Js('Royal'), Js('Rumbling'), Js('Running'), Js('Rustling'), Js('Saffron'), Js('Sanguine'), Js('Sapphire'), Js('Savage'), Js('Scarlet'), Js('Scented'), Js('Serene'), Js('Serenity'), Js('Serpent'), Js('Shade'), Js('Shadow'), Js('Shady'), Js('Shallow'), Js('Shimmering'), Js('Shivering'), Js('Shrouded'), Js('Sickle'), Js('Silent'), Js('Silver'), Js('Skyfall'), Js('Sleeping'), Js('Sleepy'), Js('Smoldering'), Js('Sneaking'), Js('Snoring'), Js('Solitude'), Js('Soothing'), Js('Southern'), Js('Sparkling'), Js('Starfall'), Js('Sweet'), Js('Swirling'), Js('Tamed'), Js('Tempered'), Js('Tempest'), Js('Timeless'), Js('Tranquil'), Js('Tranquility'), Js('Triumph'), Js('Twin'), Js('Veiled'), Js('Velvet'), Js('Verdigris'), Js('Vertex'), Js('Vibrant'), Js('Vine'), Js('Violet'), Js('Viridian'), Js('Volcano'), Js('Vortex'), Js('Waking'), Js('Wandering'), Js('Watching'), Js('Weeping'), Js('Western'), Js('Whisper'), Js('Whispering'), Js('Whistle'), Js('Whistling'), Js('Wicked'), Js('Wilted'), Js('Windy'), Js('Wish'), Js('Wishing'), Js('Youth')]))
    var.put('nm2', Js([Js('Oasis'), Js('Spring'), Js('Fountain'), Js('Oasis'), Js('Oasis'), Js('Oasis'), Js('Oasis'), Js('Oasis'), Js('Oasis'), Js('Oasis')]))
    var.put('nm3', Js([Js('Afternoons'), Js('Ancestors'), Js('Angels'), Js('Animals'), Js('Arcane'), Js('Auras'), Js('Autumn'), Js('Ballance'), Js('Change'), Js('Clouds'), Js('Crimson'), Js('Crossroads'), Js('Curiosity'), Js('Daydreams'), Js('Desire'), Js('Destiny'), Js('Discovery'), Js('Dreams'), Js('Fall'), Js('Fortune'), Js('Gardens'), Js('Glass'), Js('Gold'), Js('Guidance'), Js('Harmony'), Js('Hope'), Js('Ice'), Js('Infinity'), Js('Iron'), Js('Jade'), Js('Jewels'), Js('Knowledge'), Js('Life'), Js('Light'), Js('Lights'), Js('Love'), Js('Luck'), Js('Magic'), Js('Meditation'), Js('Melodies'), Js('Memories'), Js('Metal'), Js('Music'), Js('Observation'), Js('Ornaments'), Js('Passages'), Js('Peace'), Js('Pleasure'), Js('Pleasures'), Js('Power'), Js('Prosperity'), Js('Purity'), Js('Rain'), Js('Rhythms'), Js('Riddles'), Js('Roses'), Js('Sanctity'), Js('Sanctuaries'), Js('Sapphire'), Js('Scents'), Js('Serenity'), Js('Serpents'), Js('Shadows'), Js('Shrines'), Js('Silk'), Js('Silver'), Js('Smiles'), Js('Solitude'), Js('Song'), Js('Spirits'), Js('Spring'), Js('Steam'), Js('Summer'), Js('Thought'), Js('Thoughts'), Js('Thrills'), Js('Time'), Js('Tranquility'), Js('Treasures'), Js('Voices'), Js('Voyages'), Js('Waves'), Js('Whispers'), Js('Wind'), Js('Winter'), Js('Wishes'), Js('Youth'), Js('the Aurora'), Js('the Celestial'), Js('the Clouds'), Js('the Divine'), Js('the Garden'), Js('the Light'), Js('the Moon'), Js('the Night'), Js('the Senses'), Js('the Sky'), Js('the Stars'), Js('the Sun'), Js('the Temple')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm2').get(var.get('rnd2')))+Js(' of '))+var.get('nm3').get(var.get('rnd'))))
                var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
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
oasisNames = var.to_python()