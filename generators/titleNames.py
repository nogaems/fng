__all__ = ['titleNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' of '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm3').get(var.get('rnd'))+Js(' of '))+var.get('nm4').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((var.get('nm5').get(var.get('rnd'))+Js(' of '))+var.get('nm6').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Queen'), Js('Matriarch'), Js('Mother'), Js('Father'), Js('Admiral'), Js('Baron'), Js('Blessed'), Js('Caesar'), Js('Captain'), Js('Cardinal'), Js('Chairman'), Js('Chief'), Js('Chieftain'), Js('Commander'), Js('Corporal'), Js('Count'), Js('Defender'), Js('Divine'), Js('Dom'), Js('Duke'), Js('Earl'), Js('Elder'), Js('Eminence'), Js('Emperor'), Js('Exarch'), Js('General'), Js('Governor'), Js('Grand Master'), Js('Guardian'), Js('Headman'), Js('Herald'), Js('Imperator'), Js('King'), Js('Lord'), Js('Master'), Js('Palatine'), Js('Paragon'), Js('Patriarch'), Js('Pharaoh'), Js('President'), Js('Prime'), Js('Prince'), Js('Protector'), Js('Ruler'), Js('Shogun'), Js('Sultan')]))
var.put('nm2', Js([Js('Arrows'), Js('Ash'), Js('Blue'), Js('Bones'), Js('Conviction'), Js('Damned'), Js('Darkness'), Js('Dawn'), Js('Death'), Js('Demons'), Js('Dragons'), Js('Dreams'), Js('Dusk'), Js('Dwarves'), Js('Elves'), Js('Faith'), Js('Fear'), Js('Fire'), Js('Fools'), Js('Fortitude'), Js('Gold'), Js('Green'), Js('Heaven'), Js('Hell'), Js('Ice'), Js('Iron'), Js('Justice'), Js('Kingdoms'), Js('Life'), Js('Light'), Js('Men'), Js('Nations'), Js('Nature'), Js('New Kingdom'), Js('Night'), Js('Nightmares'), Js('the Old Kingdom'), Js('Orcs'), Js('Order'), Js('Peace'), Js('Purity'), Js('Realms'), Js('Red'), Js('Sand'), Js('Ships'), Js('Silver'), Js('Skulls'), Js('Snow'), Js('Steel'), Js('Swords'), Js('Thieves'), Js('Unity'), Js('Universe'), Js('Virtue'), Js('War'), Js('Watch'), Js('Water'), Js('the Dead'), Js('the Desert'), Js('the Dominion'), Js('the Earth'), Js('the East'), Js('the Fields'), Js('the Fleet'), Js('the Forests'), Js('the Future'), Js('the Gods'), Js('the Lakes'), Js('the Lands'), Js('the Living'), Js('the Marsh'), Js('the Millenium'), Js('the Moon'), Js('the Mountains'), Js('the New Age'), Js('the North'), Js('the Ocean'), Js('the People'), Js('the Plains'), Js('the Reach'), Js('the Realm'), Js('the Rivers'), Js('the Seas'), Js('the Skies'), Js('the Small'), Js('the South'), Js('the Stars'), Js('the Sun'), Js('the Titans'), Js('the Undead'), Js('the Vale'), Js('the Valleys'), Js('the West'), Js('the Wild'), Js('the Winds'), Js('the Wise'), Js('the World')]))
var.put('nm3', Js([Js('Administrator'), Js('Assistant'), Js('Baron'), Js('Captain'), Js('Chairman'), Js('Chief'), Js('Consul'), Js('Curator'), Js('Delegate'), Js('Director'), Js('Earl'), Js('Exarch'), Js('Governor'), Js('Head'), Js('Headman'), Js('Lady'), Js('Liaison'), Js('Lord'), Js('Master'), Js('Matriarch'), Js('Minister'), Js('Noble'), Js('Official'), Js('Overlord'), Js('Patriarch'), Js('Prime'), Js('Professor'), Js('Secretary'), Js('Sir'), Js('Tribune')]))
var.put('nm4', Js([Js('Affairs'), Js('Agents'), Js('Agriculture'), Js('Alliances'), Js('Armor'), Js('Aviation'), Js('Borders'), Js('Bows'), Js('City Planning'), Js('Coin'), Js('Commerce'), Js('Communication'), Js('Control'), Js('Culture'), Js('Death'), Js('Defense'), Js('Development'), Js('Education'), Js('Emissaries'), Js('Employment'), Js('Energy'), Js('Farming'), Js('Finance'), Js('Fish'), Js('Food'), Js('Forestry'), Js('Gold'), Js('Guards'), Js('Health'), Js('Hope'), Js('Housing'), Js('Immigration'), Js('Industry'), Js('Information'), Js('Iron'), Js('Justice'), Js('Labour'), Js('Law'), Js('Magic'), Js('Medicine'), Js('Merchants'), Js('Mining'), Js('Money'), Js('Natural Resources'), Js('Peace'), Js('Planning'), Js('Poison'), Js('Protection'), Js('Relations'), Js('Resources'), Js('Revenue'), Js('Science'), Js('Scouts'), Js('Secrets'), Js('Security'), Js('Shields'), Js('Ships'), Js('Silver'), Js('Slaves'), Js('Spies'), Js('Sports'), Js('Steel'), Js('Strategy'), Js('Swords'), Js('Tactics'), Js('Technology'), Js('Tourism'), Js('Toxins'), Js('Trade'), Js('Transport'), Js('Treasure'), Js('Vigor'), Js('Virtue'), Js('War'), Js('Warfare'), Js('Water'), Js('Weapons'), Js('Well-Being'), Js('the Future'), Js('the Marine')]))
var.put('nm5', Js([Js('Priestess'), Js('High Priestess'), Js('Abbot'), Js('Angelic'), Js('Apostle'), Js('Archbishop'), Js('Archdeacon'), Js('Archpriest'), Js('Bishop'), Js('Cardinal'), Js('Chancellor'), Js('Chaplain'), Js('Cleric'), Js('Counselor'), Js('Deacon'), Js('Divine'), Js('Doctor'), Js('Elder'), Js('Exalted'), Js('Father'), Js('Guru'), Js('High Priest'), Js('Imam'), Js('Lama'), Js('Mage'), Js('Magi'), Js('Matriarch'), Js('Minister'), Js('Missionary'), Js('Monk'), Js('Mother'), Js('Novice'), Js('Nun'), Js('Paladin'), Js('Pastor'), Js('Patriarch'), Js('Preacher'), Js('Priest'), Js('Rabbi'), Js('Reverend'), Js('Sage'), Js('Saint'), Js('Seer'), Js('Sensei'), Js('Shaman'), Js('Templar'), Js('Warlock'), Js('Witch')]))
var.put('nm6', Js([Js('Birth'), Js('Bliss'), Js('Blood'), Js('Bones'), Js('Darkness'), Js('Death'), Js('Devotion'), Js('Divinity'), Js('Dreams'), Js('Eternity'), Js('Faith'), Js('Freedom'), Js('Genesis'), Js('Gold'), Js('Gracy'), Js('Healing'), Js('Life'), Js('Light'), Js('Mercy'), Js('Misery'), Js('Nature'), Js('Nightmares'), Js('Peace'), Js('Pestinence'), Js('Piety'), Js('Pure Hearts'), Js('Purity'), Js('Rebirth'), Js('Sanctity'), Js('Shadow'), Js('Silence'), Js('Silver'), Js('Solitude'), Js('Spirits'), Js('Time'), Js('Virtue'), Js('Worship'), Js('the Arcane'), Js('the Blue'), Js('the Dead'), Js('the Earth'), Js('the East'), Js('the Flame'), Js('the Gardens'), Js('the King'), Js('the Light'), Js('the Living'), Js('the Moon'), Js('the Night'), Js('the North'), Js('the Phoenix'), Js('the Realm'), Js('the Red'), Js('the Sands'), Js('the Sea'), Js('the South'), Js('the Stars'), Js('the Sun'), Js('the Undead'), Js('the Undying'), Js('the Veil'), Js('the Voice'), Js('the Void'), Js('the West'), Js('the White'), Js('the World')]))
pass
pass


# Add lib to the module scope
titleNames = var.to_python()