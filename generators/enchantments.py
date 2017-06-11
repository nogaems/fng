__all__ = ['enchantments']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if (var.get('i')<Js(3.0)):
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' of '))+var.get('nm3').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((var.get('nm2').get(var.get('rnd3'))+Js('  '))+var.get('nm1').get(var.get('rnd')))+Js(' of '))+var.get('nm3').get(var.get('rnd2'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    while (var.get('rnd2')<Js(55.0)):
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    while (var.get('rnd3')<Js(5.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+Js(' of '))+var.get('nm2').get(var.get('rnd3')))+Js('  '))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aspect'), Js('Attunement'), Js('Aura'), Js('Blessing'), Js('Bond'), Js('Boon'), Js('Brand'), Js('Breath'), Js('Chant'), Js('Charge'), Js('Core'), Js('Crest'), Js('Crux'), Js('Curse'), Js('Emblem'), Js('Enchantment'), Js('Favor'), Js('Gift'), Js('Grace'), Js('Hymn'), Js('Infusion'), Js('Mantra'), Js('Mark'), Js('Miracle'), Js('Oath'), Js('Order'), Js('Pledge'), Js('Seal'), Js('Secrets'), Js('Seed'), Js('Spark'), Js('Symbol'), Js('Token'), Js('Tribute'), Js('Vow'), Js('Whisper'), Js('Word')]))
var.put('nm2', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('Advanced'), Js('Bolstered'), Js('Brilliant'), Js('Colossal'), Js('Elite'), Js('Enhanced'), Js('Eternal'), Js('Exceptional'), Js('Faultless'), Js('Fortified'), Js('Glorious'), Js('Grand'), Js('Greater'), Js('Immortal'), Js('Impeccable'), Js('Increased'), Js('Lesser'), Js('Light'), Js('Major'), Js('Mighty'), Js('Minor'), Js('Mortal'), Js('Mystic'), Js('Mythic'), Js('Potent'), Js('Prime'), Js('Reinforced'), Js('Renewed'), Js('Strengthened'), Js('Superior'), Js('Supreme'), Js('Titanic'), Js('Toughened'), Js('Vampiric'), Js('Vicious')]))
var.put('nm3', Js([Js('the Archer'), Js('the Armageddon'), Js('the Bear'), Js('the Beast'), Js('the Berserker'), Js('the Boar'), Js('the Cataclysm'), Js('the Crane'), Js('the Crescent Moon'), Js('the Crusader'), Js('the Day'), Js('the Dragonborn'), Js('the Eagle'), Js('the Eclipse'), Js('the End'), Js('the Enigma'), Js('the Fox'), Js('the Full Moon'), Js('the Gargoyle'), Js('the Gladiator'), Js('the Hunter'), Js('the Isles'), Js('the King'), Js('the Knight'), Js('the Light'), Js('the Lion'), Js('the Mage'), Js('the Moon'), Js('the Mountain'), Js('the Night'), Js('the Oracle'), Js('the Phoenix'), Js('the Prince'), Js('the Princess'), Js('the Prisoner'), Js('the Prodigy'), Js('the Prophecy'), Js('the Prophet'), Js('the Queen'), Js('the Rising Sun'), Js('the River'), Js('the Scourge'), Js('the Seer'), Js('the Serpent'), Js('the Setting Sun'), Js('the Steward'), Js('the Sun'), Js('the Swamp'), Js('the Tiger'), Js('the Void'), Js('the Volcano'), Js('the Ward'), Js('the Warrior'), Js('the Whale'), Js('the Wolf'), Js('Absorption'), Js('Accuracy'), Js('Adaptability'), Js('Adventure'), Js('Affliction'), Js('Agility'), Js('Air'), Js('Amnesia'), Js('Angel Wings'), Js('Anger'), Js('Anguish'), Js('Animalistic Cunning'), Js('Annihilation'), Js('Anxiety'), Js('Magic'), Js('Power'), Js('Archery'), Js('Armor'), Js('Ashes'), Js('Assassination'), Js('Assassins'), Js('Assaults'), Js('Attack'), Js('Attunement'), Js('Auras'), Js('Awareness'), Js('Balance'), Js('Barriers'), Js('Battle'), Js('Beginnings'), Js('Binding'), Js('Blades'), Js('Blast Protection'), Js('Blasting'), Js('Blindness'), Js('Bliss'), Js('Blood'), Js('Bloodshed'), Js('Boulderfists'), Js('Bravery'), Js('Brawn'), Js('Brilliance'), Js('Calamities'), Js('Calmness'), Js('Camouflage'), Js('Caring'), Js('Carnage'), Js('Cat Eyes'), Js('Cataclysms'), Js('Catastrophes'), Js('Chains'), Js('Charisma'), Js('Chills'), Js('Clarity'), Js('Cloud Walking'), Js('Combat'), Js('Conjurations'), Js('Conjuring'), Js('Constitution'), Js('Conviction'), Js('Convulsion'), Js('Courage'), Js('Cover'), Js('Creation'), Js('Crushing'), Js('Crystal Barriers'), Js('Crystal Clarity'), Js('Cunning'), Js('Dancing Blades'), Js('Danger'), Js('Dangers'), Js('Dark Magic'), Js('Dark Powers'), Js('Darkness'), Js('Dawn'), Js('Defense'), Js('Defiance'), Js('Deflection'), Js('Delight'), Js('Delirium'), Js('Demolition'), Js('Demonic Eyes'), Js('Demonic Wings'), Js('Demons'), Js('Depressions'), Js('Despair'), Js('Destruction'), Js('Determination'), Js('Devotion'), Js('Dexterity'), Js('Diplomacies'), Js('Disbelief'), Js('Discipline'), Js('Diseases'), Js('Disgust'), Js('Dishonor'), Js('Dismay'), Js('Distress'), Js('Dodging'), Js('Dominance'), Js('Domination'), Js('Doom'), Js('Doubt'), Js('Dread'), Js('Dreams'), Js('Duels'), Js('Dusk'), Js('Elimination'), Js('Enchanting'), Js('Enchantments'), Js('Ends'), Js('Endurance'), Js('Executions'), Js('Expertise'), Js('Explosions'), Js('Extinction'), Js('Faith'), Js('Fear'), Js('Feather Falling'), Js('Finesse'), Js('Fire'), Js('Focus'), Js('Fog'), Js('Force'), Js('Foresight'), Js('Forging'), Js('Fortitude'), Js('Fortune'), Js('Fright'), Js('Frost'), Js('Fury'), Js('Ghostly Essences'), Js('Ghosts'), Js('Glee'), Js('Gloom'), Js('Glory'), Js('Gluttony'), Js('Grace'), Js('Greed'), Js('Grief'), Js('Guardians'), Js('Guards'), Js('Happiness'), Js('Harm'), Js('Haste'), Js('Hate'), Js('Hatred'), Js('Havoc'), Js('Healing'), Js('Health'), Js('Health Absorption'), Js('Heaven'), Js('Hell'), Js('Hellfire'), Js('Higher Spirits'), Js('Honor'), Js('Horror'), Js('Horrors'), Js('Hostility'), Js('Hot Tempers'), Js('Hunger'), Js('Hurricanes'), Js('Ice'), Js('Icewalking'), Js('Illusions'), Js('Incantations'), Js('Infinity'), Js('Insight'), Js('Intellect'), Js('Invisibility'), Js('Judgment'), Js('Killing'), Js('Kings'), Js('Laughter'), Js('Lava'), Js('Lavawalking'), Js('Life'), Js('Lifemending'), Js('Lifestealing'), Js('Light'), Js('Lightning'), Js('Limbo'), Js('Loot'), Js('Loss'), Js('Lost Souls'), Js('Love'), Js('Luck'), Js('Magic'), Js('Magic Barriers'), Js('Magical Defenses'), Js('Magma'), Js('Mana'), Js('Mana Restoration'), Js('Massacres'), Js('Mastery'), Js('Mending'), Js('Might'), Js('Miracles'), Js('Misery'), Js('Misfortune'), Js('Mist'), Js('Moonlight'), Js('Multistrike'), Js('Murder'), Js('Mutation'), Js('Mysteries'), Js('Nature'), Js('Neglect'), Js('Nightmares'), Js('Oblivion'), Js('Pain'), Js('Panic'), Js('Paradise'), Js('Parry'), Js('Patience'), Js('Peace'), Js('Pessimism'), Js('Phantoms'), Js('Phoenix Ashes'), Js('Pickpocketing'), Js('Piercing'), Js('Pleasure'), Js('Poise'), Js('Poison'), Js('Poison Resist'), Js('Potency'), Js('Potions'), Js('Power'), Js('Praise'), Js('Prayers'), Js('Precision'), Js('Preservation'), Js('Prestige'), Js('Prophecies'), Js('Protection'), Js('Recoil'), Js('Regeneration'), Js('Reincarnation'), Js('Relics'), Js('Relief'), Js('Renewal'), Js('Resilience'), Js('Respect'), Js('Restoration'), Js('Revenge'), Js('Ruins'), Js('Runes'), Js('Salvation'), Js('Sanity'), Js('Shadow Resist'), Js('Shadows'), Js('Shock'), Js('Sight'), Js('Silence'), Js('Awareness'), Js('Slaughter'), Js('Slaying'), Js('Smite'), Js('Smiting'), Js('Sneaking'), Js('Solitude'), Js('Sorcery'), Js('Soulmending'), Js('Souls'), Js('Soulstealing'), Js('Speed'), Js('Spellpower'), Js('Spells'), Js('Spirits'), Js('Spite'), Js('Stability'), Js('Stamina'), Js('Stealth'), Js('Stone'), Js('Storms'), Js('Strength'), Js('Striking'), Js('Subtlety'), Js('Success'), Js('Suffering'), Js('Summoning'), Js('Sunfire'), Js('Sunlight'), Js('Swiftness'), Js('Swordbreaking'), Js('Tears'), Js('Tenacity'), Js('Terror'), Js('Terrors'), Js('Thieves'), Js('Thorns'), Js('Thunder'), Js('Titanic Bravery'), Js('Torment'), Js('Torture'), Js('Treasures'), Js('Tributes'), Js('Trickery'), Js('Triumph'), Js('Trouble'), Js('Trust'), Js('Twilight'), Js('Understanding'), Js('Undoing'), Js('Unending Attacks'), Js('Unseen Dangers'), Js('Valiance'), Js('Valor'), Js('Vengeance'), Js('Venom'), Js('Versatility'), Js('Vigor'), Js('Visibility'), Js('Vitality'), Js('Voodoo'), Js('War'), Js('Water Walking'), Js('Weakness'), Js('Wealth'), Js('Wind'), Js('Windwalking'), Js('Wisdom'), Js('Witchcraft'), Js('Woe'), Js('Wonders'), Js('Worship')]))
pass
pass


# Add lib to the module scope
enchantments = var.to_python()