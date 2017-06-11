__all__ = ['hideoutNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd2')),var.get('nm4').get(var.get('rnd3'))):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (((var.get('nm3').get(var.get('rnd2'))+var.get('nm4').get(var.get('rnd3')))+Js(' '))+var.get('nm2').get(var.get('rnd'))))
            else:
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd2')))+Js(' '))+var.get('nm2').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abyss'), Js('Adorned'), Js('Aeon'), Js('Amber'), Js('Ancient'), Js('Angelic'), Js('Animus'), Js('Arachnid'), Js('Arc'), Js('Arcane'), Js('Arch'), Js('Arctic'), Js('Argent'), Js('Armada'), Js('Ash'), Js('Ashen'), Js('Aspect'), Js('Aura'), Js('Aurora'), Js('Autumn'), Js('Avian'), Js('Azure'), Js('Barrage'), Js('Basilisk'), Js('Bastion'), Js('Blackout'), Js('Blind'), Js('Blitz'), Js('Blue Moon'), Js('Brass'), Js('Bristle'), Js('Broken'), Js('Brotherhood'), Js('Bulwark'), Js('Canine'), Js('Cardinal'), Js('Cerulean'), Js('Cinder'), Js('Cloak'), Js('Clover'), Js('Cobalt'), Js('Concave'), Js('Convex'), Js('Copper'), Js('Core'), Js('Corona'), Js('Covert'), Js('Creed'), Js('Crescent'), Js('Crimson'), Js('Crooked'), Js('Crown'), Js('Dark'), Js('Dawn'), Js('Defiance'), Js('Defiant'), Js('Demilune'), Js('Diablo'), Js('Diligence'), Js('Dirge'), Js('Division'), Js('Dragon'), Js('Dread'), Js('Duplicity'), Js('Dusk'), Js('Ebon'), Js('Echo'), Js('Eclipse'), Js('Elysium'), Js('Enigma'), Js('Eos'), Js('Epiphany'), Js('Epoch'), Js('Eternity'), Js('Eventide'), Js('Exalted'), Js('Exile'), Js('Falcon'), Js('Feather'), Js('Fel'), Js('Feline'), Js('Fickle'), Js('Fire'), Js('Flame'), Js('Flower'), Js('Fog'), Js('Frayed'), Js('Fury'), Js('Glass'), Js('Globe'), Js('Glum'), Js('Golden'), Js('Grand'), Js('Granite'), Js('Grave'), Js('Grim'), Js('Hallowed'), Js('Halo'), Js('Harmony'), Js('Hellion'), Js('Hollow'), Js('Infinity'), Js('Iron'), Js('Ironclad'), Js('Ivory'), Js('Jade'), Js('Jagged'), Js('Jewel'), Js('Juggernaut'), Js('Karma'), Js('Keen'), Js('Livid'), Js('Low'), Js('Luna'), Js('Lune'), Js('Meridian'), Js('Miracle'), Js('Mirage'), Js('Misty'), Js('Molten'), Js('Monolith'), Js('Murk'), Js('Mute'), Js('Mystery'), Js('Needle'), Js('Nemo'), Js('Nether'), Js('Night'), Js('Nightfall'), Js('Nightmare'), Js('Odyssey'), Js('Opulent'), Js('Outcast'), Js('Outlandish'), Js('Parapet'), Js('Penumbra'), Js('Phoenix'), Js('Pilgrim'), Js('Pinnacle'), Js('Prime'), Js('Quill'), Js('Quiver'), Js('Rabbit'), Js('Reaper'), Js('Renegade'), Js('Requiem'), Js('Retribution'), Js('Rotten'), Js('Runaway'), Js('Rune'), Js('Sabre'), Js('Salvation'), Js('Sanguine'), Js('Sapphire'), Js('Scale'), Js('Scaly'), Js('Scarlet'), Js('Serpent'), Js('Shadow'), Js('Shroud'), Js('Sickle'), Js('Silent'), Js('Silver'), Js('Sisterhood'), Js('Snowflake'), Js('Solar'), Js('Starfall'), Js('Stark'), Js('Starlight'), Js('Storm'), Js('Sub'), Js('Syncope'), Js('Syndicate'), Js('Talon'), Js('Tempest'), Js('Thorn'), Js('Thunder'), Js('Titan'), Js('Tramp'), Js('Tribute'), Js('Trident'), Js('Trinity'), Js('Triumph'), Js('Twilight'), Js('Twin'), Js('Vagabond'), Js('Vagrant'), Js('Valhalla'), Js('Vanguard'), Js('Veil'), Js('Velvet'), Js('Visage'), Js('Vortex'), Js('Warden'), Js('Watcher'), Js('Wicked'), Js('Wild'), Js('Winter'), Js('Wrath'), Js('Zephyr'), Js('Zodiac')]))
var.put('nm2', Js([Js('Base'), Js('Burrow'), Js('Cave'), Js('Cover'), Js('Covert'), Js('Den'), Js('Escape'), Js('Garrison'), Js('Harbor'), Js('Haunt'), Js('Hideaway'), Js('Hideout'), Js('Lair'), Js('Nest'), Js('Retreat'), Js('Sanctuary'), Js('Sanctum')]))
var.put('nm3', Js([Js('amber'), Js('arch'), Js('ash'), Js('ashen'), Js('bitter'), Js('black'), Js('blood'), Js('boulder'), Js('chaos'), Js('cinder'), Js('clear'), Js('cloud'), Js('cold'), Js('crest'), Js('crimson'), Js('deep'), Js('dragon'), Js('dream'), Js('dusk'), Js('ember'), Js('fire'), Js('flame'), Js('fore'), Js('free'), Js('frost'), Js('grand'), Js('grass'), Js('hallow'), Js('high'), Js('iron'), Js('jade'), Js('jugger'), Js('keen'), Js('light'), Js('lone'), Js('long'), Js('lunar'), Js('moon'), Js('mourn'), Js('nether'), Js('nettle'), Js('night'), Js('noble'), Js('path'), Js('pride'), Js('proud'), Js('rune'), Js('saur'), Js('shadow'), Js('silent'), Js('silver'), Js('skull'), Js('sky'), Js('solar'), Js('spire'), Js('spirit'), Js('star'), Js('stone'), Js('storm'), Js('sun'), Js('swift'), Js('tall'), Js('thunder'), Js('trail'), Js('van '), Js('whisper'), Js('white'), Js('wild'), Js('wolf')]))
var.put('nm4', Js([Js('bane'), Js('bark'), Js('blade'), Js('bloom'), Js('bond'), Js('born'), Js('brace'), Js('bramble'), Js('claw'), Js('crest'), Js('fall'), Js('flame'), Js('force'), Js('forge'), Js('guard'), Js('hand'), Js('heart'), Js('horn'), Js('howl'), Js('keep'), Js('keeper'), Js('lance'), Js('land'), Js('light'), Js('lock'), Js('mane'), Js('mantle'), Js('maul'), Js('might'), Js('ridge'), Js('run'), Js('shield'), Js('spell'), Js('spire'), Js('stand'), Js('star'), Js('stone'), Js('storm'), Js('strike'), Js('sword'), Js('sworn'), Js('tail'), Js('thorn'), Js('tide'), Js('tooth'), Js('vale'), Js('ward'), Js('watch'), Js('whisper'), Js('wing'), Js('word'), Js('work')]))
pass
pass


# Add lib to the module scope
hideoutNames = var.to_python()