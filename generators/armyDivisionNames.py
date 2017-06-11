__all__ = ['armyDivisionNames']

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
            var.put('names', (var.get('nm1').get(var.get('rnd'))+Js(' Division')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Administrative'), Js('Advanced Weaponry'), Js('Aerial'), Js('Aeronautical'), Js('Air Assault'), Js('Air-Defense'), Js('Airborne'), Js('Aircraft'), Js('Airforce'), Js('Ammo Supply'), Js('Android'), Js('Angel'), Js('Animal'), Js('Antiaircraft'), Js('Aquatic'), Js('Archery'), Js('Armored'), Js('Artillery'), Js('Assault'), Js('Avian'), Js('Aviation'), Js('Ballistae'), Js('Banner'), Js('Barrage'), Js('Barricade'), Js('Battle Drum'), Js('Biological'), Js('Blitz'), Js('Blitzkrieg'), Js('Bombardment'), Js('Border'), Js('Bulwark'), Js('Camouflage'), Js('Cannon'), Js('Cartographing'), Js('Catapult'), Js('Catering'), Js('Cavalry'), Js('Challenger'), Js('Champion'), Js('Chaos'), Js('Charge'), Js('Chariot'), Js('Chemical'), Js('Chemical Defense'), Js('Chopper'), Js('Cleanup'), Js('Commando'), Js('Communications'), Js('Construction'), Js('Coordination'), Js('Correctional'), Js('Covert'), Js('Creature'), Js('Crossbow'), Js('Desert'), Js('Discipline'), Js('Domestic Communications'), Js('Domestication'), Js('Doom'), Js('Dragon'), Js('Education'), Js('Elephant'), Js('Emergency'), Js('Energy'), Js('Enforcement'), Js('Engineering'), Js('Eradication'), Js('Escort'), Js('Espionage'), Js('Ethereal'), Js('Extraction'), Js('Financial'), Js('Fire'), Js('First Response'), Js('Flamethrower'), Js('Flintlock'), Js('Forest'), Js('Galactic'), Js('Garrison'), Js('Ghost'), Js('Gladiator'), Js('Glory'), Js('Grenadier'), Js('Grunt'), Js('Guard'), Js('Guardian'), Js('Guerilla'), Js('Healer'), Js('Hidden'), Js('Honor'), Js('Hostage'), Js('Hunter'), Js('Imperial'), Js('Infantry'), Js('Information'), Js('Intergalactic'), Js('Internal Relations'), Js('International Relations'), Js('Interrogation'), Js('Invasion'), Js('Investigation'), Js('Jungle'), Js('Jurisdictional'), Js('Knight'), Js('Labor'), Js('Legal'), Js('Legionnaire'), Js('Legislative'), Js('Liberation'), Js('Light'), Js('Local Relations'), Js('Logistics'), Js('Lunar'), Js('Mage'), Js('Magic'), Js('Maintenance'), Js('Marine'), Js('Maritime'), Js('Martyr'), Js('Mastermind'), Js('Mechanical'), Js('Media'), Js('Medical'), Js('Mercenary'), Js('Mercurial'), Js('Mercy'), Js('Missile Defense'), Js('Mobile'), Js('Mortar'), Js('Mountain Division'), Js('Mounted'), Js('Nautical'), Js('Naval'), Js('Night'), Js('Nightmare'), Js('Nuclear'), Js('Nuclear Defense'), Js('Nutrition'), Js('Ocean'), Js('Offensive'), Js('Onslaught'), Js('Orbital'), Js('Orbital Defense'), Js('Overwatch'), Js('Paladin'), Js('Paratrooper'), Js('Pathfinder'), Js('Patrol'), Js('Peon'), Js('Phantom'), Js('Pirate'), Js('Plague'), Js('Preparation'), Js('Preservation'), Js('Prisoner'), Js('Private'), Js('Provision'), Js('Public Relations'), Js('Ranger'), Js('Reconnaisance'), Js('Reconstruction'), Js('Recovery'), Js('Recreation'), Js('Red Alert'), Js('Redemption'), Js('Regulation'), Js('Rehabilitation'), Js('Reinforcement'), Js('Relief'), Js('Rescue'), Js('Resistance'), Js('Restoration'), Js('Rifle'), Js('River'), Js('Robot'), Js('Rogue'), Js('Saddle'), Js('Salvage'), Js('Salvation'), Js('Sanction'), Js('Scouting'), Js('Sea'), Js('Security'), Js('Sentinel'), Js('Shadow'), Js('Shield'), Js('Shock'), Js('Siege'), Js('Signal'), Js('Skirmish'), Js('Slave'), Js('Slingshot'), Js('Sniper'), Js('Snow'), Js('Space'), Js('Spec Ops'), Js('Special Forces'), Js('Stabilisation'), Js('Stakeout'), Js('Stalker'), Js('Stealth'), Js('Storm'), Js('Stormtrooper'), Js('Strategy'), Js('Subaquatic'), Js('Submarine'), Js('Subterranean'), Js('Subterrestial'), Js('Suicide'), Js('Sunken'), Js('Supervision'), Js('Supply'), Js('Support'), Js('Surveillance'), Js('Survey'), Js('Surveyance'), Js('Sustenance'), Js('Tank'), Js('Telecommunications'), Js('Templar'), Js('Terror'), Js('Thunder'), Js('Torment'), Js('Torture'), Js('Training'), Js('Transport'), Js('Trauma'), Js('Trebuchet'), Js('Treetop'), Js('Trench'), Js('Tunneler'), Js('UAV'), Js('Undercover'), Js('Underground'), Js('Unmanned'), Js('Vanguard'), Js('Veteran'), Js('Veterinary'), Js('Victim Aid'), Js('Victory'), Js('Volunteer'), Js('War Dog'), Js('War Machine'), Js('Warband'), Js('Warhammer'), Js('Warmaster'), Js('Warrior'), Js('Weaponry'), Js('Winged')]))
pass
pass


# Add lib to the module scope
armyDivisionNames = var.to_python()