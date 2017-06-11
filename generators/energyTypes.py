__all__ = ['energyTypes']

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
var.put('nm1', Js([Js('Adrenaline'), Js('Ancestral Energy'), Js('Ancestral Spirit'), Js('Ancient Power'), Js('Angelic Power'), Js('Animus'), Js('Arcane'), Js('Arch Energy'), Js('Ardor'), Js('Artifacts'), Js('Aspect'), Js('Astral Power'), Js('Aura'), Js('Beastly Power'), Js('Blood'), Js('Blood Energy'), Js('Bloodlust'), Js('Carnal Energy'), Js('Celestial Energy'), Js('Chakra'), Js('Chaos Energy'), Js('Chi'), Js('Chrono Power'), Js('Corruption'), Js('Courage'), Js('Crystal Power'), Js('Death'), Js('Demonic Aura'), Js('Demonic Power'), Js('Devotion'), Js('Diabolic Energy'), Js('Divine Grace'), Js('Divinity'), Js('Draconic Power'), Js('Druidic Energy'), Js('Electricity'), Js('Elemental Energy'), Js('Elemental Power'), Js('Empyrean Power'), Js('Endurance'), Js('Energy'), Js('Essence'), Js('Excitement'), Js('Fealty'), Js('Fell Energy'), Js('Feral Energy'), Js('Fire'), Js('Fire Power'), Js('Flux'), Js('Focus'), Js('Fortitude'), Js('Fragment Power'), Js('Frenzy'), Js('Frost Power'), Js('Furor'), Js('Fury'), Js('Fusion Power'), Js('Ghost Energy'), Js('Glory'), Js('Godly Power'), Js('Grace'), Js('Grave Energy'), Js('Grim Energy'), Js('Guardian Spirit'), Js('Hallowed Energy'), Js('Heat'), Js('Heirlooms'), Js('Higher Power'), Js('Holy Might'), Js('Hunger'), Js('Immortal Power'), Js('Immunity'), Js('Impurity'), Js('Incorporeal Energy'), Js('Infinity Energy'), Js('Initiative'), Js('Innocence'), Js('Juice'), Js('Life Force'), Js('Lifeblood'), Js('Lifeforce'), Js('Love'), Js('Lunar Energy'), Js('Magnetism'), Js('Mana'), Js('Mastery'), Js('Memory'), Js('Metamorphosis'), Js('Might'), Js('Mindpower'), Js('Mojo'), Js('Momentum'), Js('Mutation'), Js('Mystery Power'), Js('Nether Energy'), Js('Occult Energy'), Js('Paragon Power'), Js('Phase Power'), Js('Plague Energy'), Js('Potency'), Js('Pressure'), Js('Primal Power'), Js('Prime Power'), Js('Primeval Power'), Js('Purity'), Js('Rage'), Js('Relic Energy'), Js('Resistance'), Js('Righteousness'), Js('Rush'), Js('Sacred Energy'), Js('Sacred Power'), Js('Satanic Power'), Js('Sanctity'), Js('Sanity'), Js('Savagery'), Js('Scraps'), Js('Seraphic Energy'), Js('Serpentine Power'), Js('Shadow Energy'), Js('Solar Energy'), Js('Soul Energy'), Js('Soul Pressure'), Js('Souls'), Js('Spirit'), Js('Spirit Energy'), Js('Spiritual Focus'), Js('Spiritual Power'), Js('Sprites'), Js('Stamina'), Js('Star Power'), Js('Starpower'), Js('Steam'), Js('Stellar Power'), Js('Stress'), Js('Strength'), Js('Stress'), Js('Surge'), Js('Synthesis'), Js('Terror'), Js('Thirst'), Js('Thunder'), Js('Timeless Power'), Js('Timelost Power'), Js('Token'), Js('Torment'), Js('Totemic Power'), Js('Transfiguration'), Js('Tribal Energy'), Js('Twisted Energy'), Js('Unholy Might'), Js('Ursine Power'), Js('Vigor'), Js('Virility'), Js('Virtue'), Js('Vitality'), Js('Void Energy'), Js('Warpower'), Js('Wicked Energy'), Js('Will'), Js('Willpower'), Js('Wrath'), Js('Yin Yang'), Js('Zeal'), Js('Zen')]))
pass
pass


# Add lib to the module scope
energyTypes = var.to_python()