__all__ = ['batNames']

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
var.put('nm1', Js([Js('Ace'), Js('Acrobat'), Js('Ajax'), Js('Angel'), Js('Apollo'), Js('Archangel'), Js('Artemis'), Js('Ash'), Js('Azar'), Js('Azral'), Js('Baltazar'), Js('Bandit'), Js('Bane'), Js('Basil'), Js('BatPitt'), Js('Batista'), Js('Batley'), Js('Baxter'), Js('Beaker'), Js('Bigglesworth'), Js('Bitz'), Js('Blackjack'), Js('Blade'), Js('Blaze'), Js('Blitz'), Js('Bloodwing'), Js('Blues'), Js('Booboo'), Js('Bruce'), Js('Brutus'), Js('Bubba'), Js('Bubbles'), Js('Bullet'), Js('Buster'), Js('Butch'), Js('Buttons'), Js('Chaos'), Js('Char'), Js('Chocula'), Js('Cole'), Js('Comet'), Js('Cookie'), Js('Count'), Js('Cupcake'), Js('Darkess'), Js('Darth'), Js('Dexter'), Js('Diablo'), Js('Dimitri'), Js('Ding'), Js('Dodge'), Js('Dodger'), Js('Doom'), Js('Drac'), Js('Dracula'), Js('Draculon'), Js('Drake'), Js('Echo'), Js('Equinox'), Js('Fangs'), Js('Flapper'), Js('Flappy'), Js('Flaps'), Js('Flash'), Js('Flicker'), Js('Fuzz'), Js('Gambat'), Js('Gargle'), Js('Gargles'), Js('Gargoyle'), Js('Gavalon'), Js('Ghost'), Js('Gizmo'), Js('Glider'), Js('Gloom'), Js('Glyde'), Js('Golbat'), Js('Gouge'), Js('Grey'), Js('Guano'), Js('Hannibal'), Js('Hawke'), Js('Hunter'), Js('Hyperion'), Js('Impaler'), Js('Jet'), Js('Kane'), Js('Khan'), Js('Kindle'), Js('Lecter'), Js('Lockjaw'), Js('Lucifer'), Js('Marble'), Js('Matrix'), Js('Merlin'), Js('Midas'), Js('Midnight'), Js('Mirage'), Js('Monty'), Js('Moon'), Js('Mothra'), Js('Muse'), Js('Nerf'), Js('Nibbles'), Js('Nightmare'), Js('Nightwing'), Js('Nugget'), Js('Nukem'), Js('Nyx'), Js('Onyx'), Js('Orion'), Js('Ozzy'), Js('Patch'), Js('Patches'), Js('Pebbles'), Js('Phantom'), Js('Pickle'), Js('Psych'), Js('Quickfang'), Js('Quilla'), Js('Rabies'), Js('Rainbow'), Js('Rascal'), Js('Remus'), Js('Render'), Js('Rhonin'), Js('Ripmaw'), Js('Rocky'), Js('Rufus'), Js('Sabath'), Js('Sawyer'), Js('Screech'), Js('Screechy'), Js('Shade'), Js('Shadow'), Js('Shreek'), Js('Shrike'), Js('Slate'), Js('Slithe'), Js('Snuffle'), Js('Sonar'), Js('Sonny'), Js('Spectre'), Js('Spitfire'), Js('Spudnik'), Js('Spuds'), Js('Swoops'), Js('Thunder'), Js('Tiberius'), Js('Titan'), Js('Twinkle'), Js('Umber'), Js('Vamp'), Js('Vlad'), Js('Vladimir'), Js('Vulkan'), Js('Wayne'), Js('Wiggles'), Js('Wingnut'), Js('Xanadu'), Js('Zion')]))
var.put('nm2', Js([Js('Abby'), Js('Aerial'), Js('Aine'), Js('Alexia'), Js('Alexis'), Js('Amber'), Js('Angel'), Js('Angie'), Js('Apple'), Js('Ash'), Js('Atilla'), Js('Aura'), Js('Aurora'), Js('Azraelle'), Js('Azure'), Js('Azurys'), Js('Babes'), Js('Bandetta'), Js('Batsy'), Js('Batty'), Js('Beauty'), Js('Biscuit'), Js('Blaze'), Js('Breeze'), Js('Bubble'), Js('Bubbles'), Js('Buttercup'), Js('Buttons'), Js('Calypso'), Js('Cerulean'), Js('Chuckles'), Js('Cinderella'), Js('Cinnamon'), Js('Clementine'), Js('Cleo'), Js('Cookie'), Js('Cosmo'), Js('Cuddles'), Js('Cupcake'), Js('Dakota'), Js('Daphne'), Js('Dawn'), Js('Dawne'), Js('Dawnstar'), Js('Dot'), Js('Draculette'), Js('Ebony'), Js('Echo'), Js('Eclipse'), Js('Ember'), Js('Enigma'), Js('Equina'), Js('Equinox'), Js('Fang'), Js('Fangie'), Js('Faune'), Js('Fierra'), Js('Fizzle'), Js('Flappy'), Js('Fluffy'), Js('Flutters'), Js('Gadget'), Js('Gargles'), Js('Giggles'), Js('Grace'), Js('Guani'), Js('Harmony'), Js('Haze'), Js('Hazel'), Js('Honey'), Js('Huntress'), Js('Iggy'), Js('Illumina'), Js('Indigo'), Js('Iris'), Js('Ivory'), Js('Ivy'), Js('Jinx'), Js('Jynx'), Js('Lady'), Js('Liberty'), Js('Lucy'), Js('Lullaby'), Js('Luna'), Js('Mable'), Js('Marbles'), Js('Maya'), Js('Melody'), Js('Mirage'), Js('Mittens'), Js('Moonbeam'), Js('Moone'), Js('Moonlight'), Js('Morning'), Js('Morticia'), Js('Myst'), Js('Mystique'), Js('Nibbles'), Js('Nighte'), Js('Noodles'), Js('Nova'), Js('Nugget'), Js('Oracle'), Js('Peaches'), Js('Pebbles'), Js('Pepper'), Js('Phoenix'), Js('Pickle'), Js('Pickles'), Js('Plume'), Js('Precious'), Js('Princess'), Js('Psyche'), Js('Raine'), Js('Raven'), Js('Rebel'), Js('Rhyme'), Js('Rogue'), Js('Ruth'), Js('Sade'), Js('Sage'), Js('Scarlett'), Js('Shade'), Js('Shadow'), Js('Shay'), Js('Shine'), Js('Siren'), Js('Skye'), Js('Skylar'), Js('Snuffles'), Js('Sona'), Js('Sora'), Js('Star'), Js('Stardust'), Js('Starlight'), Js('Sugar'), Js('Tinkerbell'), Js('Trixie'), Js('Trixy'), Js('Twilight'), Js('Twinkle'), Js('Twinkles'), Js('Vanity'), Js('Velvet'), Js('Violet'), Js('Vixen'), Js('Wiggles'), Js('Xena')]))
pass
pass


# Add lib to the module scope
batNames = var.to_python()