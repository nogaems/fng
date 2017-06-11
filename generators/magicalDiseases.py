__all__ = ['magicalDiseases']

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
    var.registers(['nm1', 'nm2', 'result'])
    var.put('nm1', Js([Js('Aether'), Js('Aethereal'), Js('Alacadabra'), Js('Angelic'), Js('Arcane'), Js('Astral'), Js('Aura'), Js('Banishing'), Js('Banshee'), Js('Basilisk'), Js('Bog'), Js('Celestial'), Js('Centaur'), Js('Chakra'), Js('Changeling'), Js('Chaos'), Js('Charm'), Js('Charmed'), Js('Chimera'), Js('Cipher'), Js('Clairvoyance'), Js('Clairvoyant'), Js('Conjuring'), Js('Coven'), Js('Crystal'), Js('Demon'), Js('Diabolical'), Js('Divine'), Js('Djinni'), Js('Dowsing'), Js('Dragon'), Js('Dryad'), Js('Echo'), Js('Ecto'), Js('Ectoplasm'), Js('Eerie'), Js('Elemental'), Js('Enchanted'), Js('Enigma'), Js('Ethereal'), Js('Evocation'), Js('Fairy'), Js('Familiar'), Js('Fire'), Js('Flashing'), Js('Flux'), Js('Flying'), Js('Fortune'), Js("Giant's"), Js('Glamour'), Js('Goblin'), Js('Griffin'), Js('Grimoire'), Js('Harpy'), Js('Haunted'), Js('Hellion'), Js('Hex'), Js('Hexing'), Js('Hocuspocus'), Js('Horror'), Js('Hypnosis'), Js('Hypnotic'), Js('Illusion'), Js('Infernal'), Js('Invisible'), Js('Juju'), Js('Kelpie'), Js('Lamia'), Js('Levitation'), Js('Lich'), Js('Lucifer'), Js("Magician's"), Js('Magnetic'), Js('Malediction'), Js('Menace'), Js('Miracle'), Js('Mojo'), Js('Morphing'), Js('Mutant'), Js('Mystic'), Js('Nether'), Js('Ogre'), Js('Omen'), Js('Oracle'), Js('Ouija'), Js('Pandora'), Js('Paragon'), Js('Paranormal'), Js('Pendulum'), Js('Pentacle'), Js('Phantom'), Js('Phoenix'), Js('Pixie'), Js('Prophecy'), Js('Prowess'), Js('Psi'), Js('Psionic'), Js('Psychic'), Js('Pyro'), Js('Qi'), Js('Rune'), Js('Scale'), Js('Scrying'), Js('Seance'), Js('Shade'), Js('Shadow'), Js('Sigil'), Js('Siren'), Js('Skeleton'), Js('Sorcerous'), Js('Specter'), Js('Spectral'), Js('Spirit'), Js('Tantra'), Js('Titan'), Js('Totem'), Js('Totemic'), Js('Transmutation'), Js('Treant'), Js('Troll'), Js('Undine'), Js('Vampire'), Js('Vanishing'), Js('Void'), Js('Voodoo'), Js('Warlock'), Js('Wendigo'), Js('Werewolf'), Js('Witcher'), Js("Witches'"), Js('Wither'), Js('Wizard'), Js('Wyvern'), Js('Zombie')]))
    var.put('nm2', Js([Js('Ache'), Js('Aches'), Js('Affliction'), Js('Amnesia'), Js('Anemia'), Js('Blight'), Js('Blindness'), Js('Blisters'), Js('Blood'), Js('Breakdown'), Js('Burn'), Js('Chills'), Js('Cold'), Js('Cough'), Js('Cramps'), Js('Curse'), Js('Death'), Js('Decay'), Js('Delirium'), Js('Delusion'), Js('Dementia'), Js('Disease'), Js('Disorder'), Js('Doom'), Js('Drip'), Js('Fatigue'), Js('Fever'), Js('Flu'), Js('Gut'), Js('Haze'), Js('Infection'), Js('Insanity'), Js('Limb'), Js('Madness'), Js('Malady'), Js('Mark'), Js('Plague'), Js('Pox'), Js('Puffs'), Js('Rage'), Js('Rash'), Js('Rot'), Js('Shakes'), Js('Sickness'), Js('Sores'), Js('Spasm'), Js('Spasms'), Js('Syndrome'), Js('Thirst'), Js('Vapors'), Js('Virus'), Js('Warts')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
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
magicalDiseases = var.to_python()