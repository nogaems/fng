__all__ = ['rankNames']

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
var.put('nm1', Js([Js('Adept'), Js('Adjunct'), Js('Administrator'), Js('Admiral'), Js('Advisor'), Js('Alpha'), Js('Alpha Chieftain'), Js('Alpha King'), Js('Ambassador'), Js('Apostle'), Js('Apprentice'), Js('Archbishop'), Js('Archduke'), Js('Archjusticar'), Js('Archmage'), Js('Archpaladin'), Js('Archpriest'), Js('Archsage'), Js('Archseer'), Js('Archsentinel'), Js('Archwarrior'), Js('Assistant'), Js('Attendant'), Js('Baron'), Js('Beta'), Js('Bishop'), Js('Blessed'), Js('Caesar'), Js('Chairman'), Js('Chamberlain'), Js('Chancellor'), Js('Chaplain'), Js('Chief'), Js('Chieftain'), Js('Cleric'), Js('Clerk'), Js('Congressman'), Js('Consort'), Js('Consul'), Js('Council Chief'), Js('Council Member'), Js('Councillor'), Js('Count'), Js('Demonlord'), Js('Dictator'), Js('Director'), Js('Disciple'), Js('Divine'), Js('Dom'), Js('Dragonlord'), Js('Duke'), Js('Earl'), Js('Elder'), Js('Emperor'), Js('Ensign'), Js('Exarch'), Js('Executive'), Js('Executor'), Js('Father'), Js('First Secretary'), Js('Foreman'), Js('General'), Js('Governer'), Js('Grand Admiral'), Js('Grand Vizier'), Js('Hand of the King'), Js('Head of State'), Js('Herald'), Js('High Baron'), Js('High Chairman'), Js('High Chancellor'), Js('High Chief'), Js('High Cleric'), Js('High Councillor'), Js('High Duke'), Js('High Earl'), Js('High Emperor'), Js('High Father'), Js('High General'), Js('High Governor'), Js('High Justicar'), Js('High King'), Js('High Mage'), Js('High Magister'), Js('High Marshal'), Js('High Minister'), Js('High Paladin'), Js('High Priest'), Js('High Prince'), Js('High Prophet'), Js('High Regent'), Js('High Sage'), Js('High Saint'), Js('High Secretary'), Js('High Seer'), Js('High Senator'), Js('High Sentinel'), Js('High Shaman'), Js('High Strategos'), Js('High Templar'), Js('Imperator'), Js('Inquisitor'), Js('Junior Adept'), Js('Junior Apprentice'), Js('Justicar'), Js('King'), Js("King's Advisor"), Js("King's Guard"), Js("King's Knight"), Js('Knight'), Js('Knight Commander'), Js('Librarian'), Js('Lord'), Js('Lord Commander'), Js('Lord General'), Js('Mage'), Js('Magister'), Js('Marshal'), Js('Master'), Js('Master Chief'), Js('Master Father'), Js('Mayor'), Js('Mentor'), Js('Mercenary'), Js('Minister'), Js('Neophyte'), Js('Overlord'), Js('Paladin'), Js('Palatine'), Js('Patriarch'), Js('Patroon'), Js('Pharaoh'), Js('Pilgrim'), Js('President'), Js('Prime'), Js('Prime Chief'), Js('Prime General'), Js('Prime Justicar'), Js('Prime Minister'), Js('Prime Paladin'), Js('Prime Patriarch'), Js('Prime Secretary'), Js('Prime Sentinel'), Js('Prime Templar'), Js('Prince'), Js('Professor'), Js('Prophet'), Js('Protector'), Js('Purifier'), Js('Ranger'), Js('Ranger Commander'), Js('Regent'), Js('Rogue'), Js('Royal Administrator'), Js('Royal Advisor'), Js('Royal Ambassador'), Js('Royal Chamberlain'), Js('Royal Consort'), Js('Royal Consul'), Js('Royal Councillor'), Js('Royal Executor'), Js('Royal Inquisitor'), Js('Royal Justicar'), Js('Royal Knight'), Js('Royal Mentor'), Js('Royal Mercenary'), Js('Royal Paladin'), Js('Royal Professor'), Js('Royal Sage'), Js('Royal Saint'), Js('Royal Scholar'), Js('Royal Secretary'), Js('Royal Sentinel'), Js('Royal Spokesman'), Js('Royal Strategos'), Js('Royal Templar'), Js('Royal Vizier'), Js('Sage'), Js('Saint'), Js('Scholar'), Js('Secretary'), Js('Seer'), Js('Sellsword'), Js('Senator'), Js('Sentinel'), Js('Shaman'), Js('Shogun'), Js('Specialist'), Js('Spokesman'), Js('Squire'), Js('Strategos'), Js('Sultan'), Js('Supervisor'), Js('Templar'), Js('Trainee'), Js('Vizier'), Js('Warchief'), Js('Warlord'), Js('Warmaster'), Js('Warrior'), Js('Zealot')]))
pass
pass


# Add lib to the module scope
rankNames = var.to_python()