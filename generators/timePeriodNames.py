__all__ = ['timePeriodNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm3').get(var.get('rnd2')))+Js(' of '))+var.get('nm2').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Accord'), Js('Agency'), Js('Alchemy'), Js('Alliance'), Js('Ambitious'), Js('Anarchy'), Js('Ancestral'), Js('Android'), Js('Apocalypse'), Js('Arcane'), Js('Atomic'), Js('Aura'), Js('Aurora'), Js('Battle'), Js('Beauty'), Js('Bionic'), Js('Blissful'), Js('Bloodshed'), Js('Bloody'), Js('Blooming'), Js('Blossom'), Js('Carnage'), Js('Celestial'), Js('Civil'), Js('Clone'), Js('Collapsing'), Js('Collision'), Js('Colonial'), Js('Combat'), Js('Confusion'), Js('Conjured'), Js('Counterfeit'), Js('Covert'), Js('Crystal'), Js('Darkness'), Js('Deception'), Js('Delusion'), Js('Design'), Js('Destiny'), Js('Destruction'), Js('Diamond'), Js('Disabled'), Js('Discovery'), Js('Disinformation'), Js('Divine'), Js('Doom'), Js('Dread'), Js('Dream'), Js('Ecstasy'), Js('Electric'), Js('Elimination'), Js('Enlightened'), Js('Enmity'), Js('Eradication'), Js('Eternal'), Js('Euphoria'), Js('Evolution'), Js('Exalted'), Js('Exhausted'), Js('Exotic'), Js('Exploration'), Js('Extinction'), Js('Extraterrestrial'), Js('Extreme'), Js('Fable'), Js('Failure'), Js('False'), Js('Forgotten'), Js('Fright'), Js('Frozen'), Js('Fury'), Js('Fusion'), Js('Gadget'), Js('Glamor'), Js('Glass'), Js('Gleeful'), Js('Glory'), Js('Grandiose'), Js('Happy'), Js('Harmony'), Js('Havoc'), Js('Herculean'), Js('Hero'), Js('High'), Js('Holy'), Js('Honest'), Js('Horror'), Js('Idealist'), Js('Identity'), Js('Imagination'), Js('Infinity'), Js('Information'), Js('Intimidation'), Js('Invention'), Js('Isolation'), Js('Judgment'), Js('Karma'), Js('Limitless'), Js('Lost'), Js('Machine'), Js('Magic'), Js('Malignant'), Js('Martial'), Js('Massacre'), Js('Mechanical'), Js('Medical'), Js('Memorial'), Js('Metaphysical'), Js('Migration'), Js('Molten'), Js('Multicultural'), Js('Mutation'), Js('Mystery'), Js('Mystic'), Js('Mythical'), Js('Nationalistic'), Js('Nature'), Js('Noble'), Js('Nuclear'), Js('Nurture'), Js('Obliteration'), Js('Occult'), Js('Other'), Js('Panic'), Js('Paradise'), Js('Paragon'), Js('Paranormal'), Js('Peaceful'), Js('Perfection'), Js('Perversion'), Js('Phantom'), Js('Pinnacle'), Js('Plastic'), Js('Poison'), Js('Primal'), Js('Prime'), Js('Pristine'), Js('Private'), Js('Progress'), Js('Prophecy'), Js('Prophetic'), Js('Protection'), Js('Putrid'), Js('Radical'), Js('Rage'), Js('Rapture'), Js('Rebirth'), Js('Regal'), Js('Regression'), Js('Relic'), Js('Revelation'), Js('Revolution'), Js('Romantic'), Js('Ruin'), Js('Rune'), Js('Sacred'), Js('Scientific'), Js('Secrecy'), Js('Secret'), Js('Separation'), Js('Shadow'), Js('Shattered'), Js('Silent'), Js('Slaughter'), Js('Sleeping'), Js('Social'), Js('Solidarity'), Js('Solitude'), Js('Sorcery'), Js('Space'), Js('Spirit'), Js('Stealth'), Js('Strive'), Js('Struggle'), Js('Superhuman'), Js('Suppression'), Js('Supreme'), Js('Surrender'), Js('Synthetic'), Js('Tender'), Js('Terraforming'), Js('Territorial'), Js('Terror'), Js('Timeless'), Js('Titan'), Js('Toxic'), Js('Trepidation'), Js('Truce'), Js('Uncanny'), Js('Unity'), Js('Utopian'), Js('Venom'), Js('Visionary'), Js('Vitality'), Js('Voodoo'), Js('Warfare'), Js('Widget'), Js('Witchcraft'), Js('Wood'), Js('Wreckage'), Js('Youth')]))
var.put('nm2', Js([Js('Abundances'), Js('Advancement'), Js('Alterations'), Js('Amendments'), Js('Ancestors'), Js('Ancients'), Js('Annihilation'), Js('Ascension'), Js('Ashes'), Js('Attraction'), Js('Barbarians'), Js('Battle'), Js('Beauty'), Js('Bionics'), Js('Blessings'), Js('Blood'), Js('Bones'), Js('Brilliance'), Js('Brutes'), Js('Carnage'), Js('Change'), Js('Chaos'), Js('Clones'), Js('Combat'), Js('Confusion'), Js('Control'), Js('Correction'), Js('Creation'), Js('Cruelty'), Js('Cultivation'), Js('Darkness'), Js('Death'), Js('Deception'), Js('Deities'), Js('Demise'), Js('Destinies'), Js('Deterioration'), Js('Development'), Js('Disaster'), Js('Discipline'), Js('Discoveries'), Js('Divination'), Js('Divines'), Js('Doom'), Js('Downfalls'), Js('Dread'), Js('Dreams'), Js('Duplicates'), Js('Duplicity'), Js('Dust'), Js('Electricity'), Js('Enchantment'), Js('Enhancement'), Js('Enlightenment'), Js('Eradication'), Js('Euphoria'), Js('Evolution'), Js('Existence'), Js('Extinction'), Js('Failure'), Js('Fortune'), Js('Foundations'), Js('Fraudulence'), Js('Freedom'), Js('Fright'), Js('Frost'), Js('Fury'), Js('Gadgets'), Js('Ghosts'), Js('Glamor'), Js('Glass'), Js('Glory'), Js('Gods'), Js('Grandeur'), Js('Growth'), Js('Guidance'), Js('Guile'), Js('Harmony'), Js('Havoc'), Js('Health'), Js('Heroes'), Js('Honesty'), Js('Hypocrisy'), Js('Illusions'), Js('Immortality'), Js('Indifference'), Js('Indulgence'), Js('Injury'), Js('Insignificance'), Js('Intimidation'), Js('Inventions'), Js('Isolation'), Js('Karma'), Js('Kindness'), Js('Liberty'), Js('Life'), Js('Loss'), Js('Machines'), Js('Magic'), Js('Magnificence'), Js('Marvels'), Js('Massacres'), Js('Medicines'), Js('Might'), Js('Migration'), Js('Miracles'), Js('Misfortune'), Js('Mortality'), Js('Mutations'), Js('Mythics'), Js('Myths'), Js('Nature'), Js('Neglect'), Js('No Return'), Js('Nobility'), Js('Nothingness'), Js('Oblivion'), Js('Opulence'), Js('Originations'), Js('Origins'), Js('Oversight'), Js('Panic'), Js('Peace'), Js('Penance'), Js('Perdition'), Js('Perversion'), Js('Phantoms'), Js('Phenomenons'), Js('Plenty'), Js('Poison'), Js('Pretense'), Js('Progress'), Js('Prophecies'), Js('Protection'), Js('Punishment'), Js('Radicals'), Js('Rage'), Js('Raptures'), Js('Rebirth'), Js('Recovery'), Js('Reformation'), Js('Regeneration'), Js('Regulations'), Js('Release'), Js('Renovation'), Js('Repetition'), Js('Retribution'), Js('Revelations'), Js('Revisal'), Js('Revision'), Js('Revolutions'), Js('Romance'), Js('Rubble'), Js('Ruins'), Js('Sacrifice'), Js('Savagery'), Js('Scapegoats'), Js('Science'), Js('Secrecy'), Js('Secrets'), Js('Seduction'), Js('Silence'), Js('Sincerity'), Js('Slaughter'), Js('Solitude'), Js('Souls'), Js('Space'), Js('Spells'), Js('Spirits'), Js('Splendor'), Js('Spoils'), Js('Stagnation'), Js('Stealth'), Js('Storms'), Js('Strive'), Js('Struggle'), Js('Subjection'), Js('Success'), Js('Suffering'), Js('Suppression'), Js('Surprises'), Js('Temptation'), Js('Terror'), Js('Titans'), Js('Torture'), Js('Tragedy'), Js('Treachery'), Js('Trials'), Js('Trickery'), Js('Triumph'), Js('Trust'), Js('Turbulence'), Js('Turmoil'), Js('Unities'), Js('Utopia'), Js('Venom'), Js('Victims'), Js('Violence'), Js('Warfare'), Js('Waste'), Js('Whitewashing'), Js('Witchcraft'), Js('Wonder')]))
var.put('nm3', Js([Js('Age'), Js('Era'), Js('Aeon'), Js('Ages')]))
pass
pass


# Add lib to the module scope
timePeriodNames = var.to_python()