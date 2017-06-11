__all__ = ['themeParkNames']

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
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((var.get('nm3').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Angel'), Js('Animal'), Js('Aqua'), Js('Arcane'), Js('Astral'), Js('Astro'), Js('Aura'), Js('Beach'), Js('Beast'), Js('Carny'), Js('Cartoon'), Js('Child'), Js('Clown'), Js('Comic'), Js('Creep'), Js('Critter'), Js('Crypt'), Js('Demon'), Js('Dino'), Js('Doll'), Js('Dragon'), Js('Dread'), Js('Dream'), Js('Elf'), Js('Ember'), Js('Epic'), Js('Eterni'), Js('Ever'), Js('Expo'), Js('Fable'), Js('Fairy'), Js('Feral'), Js('Festi'), Js('Film'), Js('Fire'), Js('Forest'), Js('Freak'), Js('Fright'), Js('Fun'), Js('Game'), Js('Ghost'), Js('Giant'), Js('Groovy'), Js('Happy'), Js('Hell'), Js('Hero'), Js('Horror'), Js('Ice'), Js('Jungle'), Js('Kids'), Js('Luna'), Js('Lunar'), Js('Magic'), Js('Marina'), Js('Maze'), Js('Mega'), Js('Mini'), Js('Miracle'), Js('Mirror'), Js('Monster'), Js('Movie'), Js('Mutant'), Js('Never'), Js('Night'), Js('Ocean'), Js('Paradox'), Js('Phantom'), Js('Play'), Js('Quest'), Js('Rain'), Js('Rainbow'), Js('River'), Js('Robot'), Js('Saga'), Js('Sand'), Js('Scream'), Js('Secret'), Js('Shadow'), Js('Shock'), Js('Sky'), Js('Snow'), Js('Solar'), Js('Space'), Js('Speed'), Js('Spirit'), Js('Splash'), Js('Star'), Js('Stellar'), Js('Storm'), Js('Story'), Js('Summer'), Js('Sun'), Js('Super'), Js('Terra'), Js('Terror'), Js('Thrill'), Js('Titan'), Js('Toy'), Js('Undead'), Js('Vision'), Js('Warp'), Js('Water'), Js('Winter'), Js('Witch'), Js('Wizard'), Js('Wonder'), Js('Zombie'), Js('Zoo')]))
var.put('nm2', Js([Js('land'), Js('world'), Js('zone'), Js('park'), Js('town'), Js('fair'), Js('realm'), Js('ville'), Js('land'), Js('park'), Js('ventures')]))
var.put('nm3', Js([Js('Adventure'), Js('Amazing'), Js('Amazon'), Js('Angel'), Js('Animal'), Js('Animation'), Js('Anime'), Js('Aqua'), Js('Arcane'), Js('Astral'), Js('Beach'), Js('Beast'), Js('Bird'), Js('Candy'), Js('Cartoon'), Js('Castle'), Js('Child'), Js('Chocolate'), Js('Clown'), Js('Comic'), Js('Creep'), Js('Critter'), Js('Crypt'), Js('Crystal'), Js('Demon'), Js('Dino'), Js('Dinosaur'), Js('Discovery'), Js('Doll'), Js('Dragon'), Js('Dread'), Js('Dream'), Js('Elf'), Js('Ember'), Js('Enchanted'), Js('Epic'), Js('Fable'), Js('Fairy'), Js('Fairy Tale'), Js('Family'), Js('Fantasy'), Js('Feral'), Js('Festival'), Js('Film'), Js('Fire'), Js('Forest'), Js('Freak'), Js('Fright'), Js('Fun'), Js('Galaxy'), Js('Game'), Js('Ghost'), Js('Giant'), Js('Happy'), Js('Hell'), Js('Hero'), Js('Horror'), Js('Ice'), Js('Jungle'), Js('Kids'), Js("King's"), Js('Knight'), Js('Legend'), Js('Luna'), Js('Lunar'), Js('Magic'), Js('Magic Forest'), Js('Marina'), Js('Marine'), Js('Maze'), Js('Mega'), Js('Midnight'), Js('Mini'), Js('Miniature'), Js('Miracle'), Js('Mirror'), Js('Monster'), Js('Movie'), Js('Mutant'), Js('Mystery'), Js('Mystic'), Js('Mythic'), Js('Nature'), Js('Night'), Js('Nightmare'), Js('Oasis'), Js('Ocean'), Js('Panorama'), Js('Paradox'), Js('Parody'), Js('Phantom'), Js('Phoenix'), Js('Pirate'), Js('Play'), Js('Power'), Js('Quest'), Js('Rain'), Js('Rainbow'), Js('River'), Js('Robot'), Js('Saga'), Js('Sand'), Js("Santa's"), Js('Science'), Js('Scream'), Js('Secret'), Js('Serpent'), Js('Shadow'), Js('Shock'), Js('Sky'), Js('Snow'), Js('Solar'), Js('Space'), Js('Speed'), Js('Spirit'), Js('Splash'), Js('Star'), Js('Storebook'), Js('Storm'), Js('Story'), Js('Summer'), Js('Sun'), Js('Super'), Js('Surprise'), Js('Terror'), Js('Thrill'), Js('Titan'), Js('Toy'), Js('Trampoline'), Js('Transilvanian'), Js('Undead'), Js('Underwater'), Js('Universe'), Js('Vampire'), Js('Vision'), Js('Warp'), Js('Water'), Js('Werewolf'), Js('Wild Water'), Js('Wild West'), Js('Wildlife'), Js('Winter'), Js('Witch'), Js('Wizard'), Js('Wonder'), Js('Zombie'), Js('Zoo')]))
var.put('nm4', Js([Js('World'), Js('Land'), Js('Zone'), Js('Park'), Js('Town'), Js('Village'), Js('Realm'), Js('Fair'), Js('Island'), Js('Fun Park'), Js('Fun World'), Js('Kingdom'), Js('Dome'), Js('Paradise'), Js('Experience')]))
pass
pass


# Add lib to the module scope
themeParkNames = var.to_python()