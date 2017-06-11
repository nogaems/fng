__all__ = ['allianceNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aegis'), Js('Aerospace'), Js('Air Space Independence'), Js('Allied'), Js('Amalgamation'), Js('Amity'), Js('Ancestral'), Js('Angelic'), Js('Anti-Terror'), Js('Arcane'), Js('Archangel'), Js('Archetype'), Js('Armament'), Js('Armistice'), Js('Ashed'), Js('Assembled'), Js('Assisted'), Js('Axis'), Js('Bastion'), Js('Blessed'), Js('Bulwark'), Js('Cardinal'), Js('Celestial'), Js('Central'), Js('Cerberus'), Js('Champion'), Js('Citadel'), Js('Commanding'), Js('Confederated'), Js('Confederation'), Js('Cooperation'), Js('Cosmic'), Js('Cosmos'), Js('Counter Terror'), Js('Crimson'), Js('Curator'), Js('Custodian'), Js('Custody'), Js('Defenders'), Js('Defending'), Js('Diplomatic'), Js('Divine'), Js('Domination'), Js('Dread'), Js('Dual'), Js('Earthen'), Js('Ebon'), Js('Empire'), Js('Environment Defense'), Js('Epitome'), Js('Equilibrium'), Js('Eternal'), Js('Faithful'), Js('First'), Js('First Aid'), Js('Fortification'), Js('Freedom'), Js('Fundamental'), Js('Galactic'), Js('Galactic Security'), Js('Galaxy Supervision'), Js('Galaxy Watch'), Js('Ghost'), Js('Global Authority'), Js('Global Combat'), Js('Global Economic'), Js('Global Financial'), Js('Global Food'), Js('Global Immunity'), Js('Global Industry'), Js('Global Inquisition'), Js('Global Insurance'), Js('Global Integrity'), Js('Global Intelligence'), Js('Global Jurisdiction'), Js('Global Justice'), Js('Global Prosperity'), Js('Global Protection'), Js('Global Sanctuary'), Js('Global Shield'), Js('Global Support'), Js('Global Surveillance'), Js('Global War'), Js('Global Watch'), Js('Global Welfare'), Js('Golden'), Js('Good Will'), Js('Grand'), Js('Guardian'), Js('Guardianship'), Js('Hallowed'), Js('Harmony'), Js('Harvest'), Js('Heavenly'), Js('Highborn'), Js('Holy'), Js('Immunity'), Js('Imperial'), Js('Independent'), Js('Industry'), Js('Inquisition'), Js('Integration'), Js('Integrity'), Js('Intercontinental Security'), Js('Interference'), Js('Intergalactic'), Js('International Security'), Js('Interstellar Administration'), Js('Interstellar Domination'), Js('Intimidation'), Js('Invulnerability'), Js('Ivory'), Js('Jewel'), Js('Kinship'), Js('Liberated'), Js('Little'), Js('Magistracy'), Js('Mutual Defense'), Js('Mutual Support'), Js('Mystic'), Js('Mythic'), Js('Nature'), Js('Nature Preservation'), Js('Next World'), Js('Noble'), Js('Nonaggression'), Js('Nuclear'), Js('Nuclear Protection'), Js('Obsidian'), Js('Occult'), Js('Onyx'), Js('Oracle'), Js('Pacifist'), Js('Paladin'), Js('Paragon'), Js('Paramount'), Js('Peace'), Js('Peacekeeper'), Js('Peacemonger'), Js('Phantom'), Js('Phoenix'), Js('Pious'), Js('Preservation'), Js('Prime'), Js('Primeval'), Js('Primordial'), Js('Prophecy'), Js('Protection'), Js('Quadruple'), Js('Radical'), Js('Rampart'), Js('Redemption'), Js('Regal'), Js('Reincarnation'), Js('Reinforcement'), Js('Resistance'), Js('Resurrection'), Js('Retribution'), Js('Revelation'), Js('Revitalization'), Js('Righteous'), Js('Royal'), Js('Sacred'), Js('Sacred World'), Js('Salvation'), Js('Sanctified'), Js('Sanctuary'), Js('Sanguine'), Js('Scientific Progress'), Js('Security'), Js('Self-Defense'), Js('Sentinel'), Js('Seraphic'), Js('Shepherd'), Js('Silver'), Js('Sovereign'), Js('Space Combat'), Js('Space Command'), Js('Stabilization'), Js('Steward'), Js('Strike Force'), Js('Supreme'), Js('Surveillance'), Js('Terror Defiance'), Js('Terror Opposition'), Js('Terror Response'), Js('Terror Supervision'), Js('Triple'), Js('Truce'), Js('Undivided'), Js('Unified'), Js('United'), Js('Unity'), Js('Utopian'), Js('Vigilante'), Js('Vortex'), Js('Watchdog'), Js('Wildlife Conservation'), Js('Wildlife Preservation'), Js('Wildlife Shelter'), Js('World Aid'), Js('World Authority'), Js('World Equilibrium'), Js('World Freedom'), Js('World Health'), Js('World Keeper'), Js('World Peace'), Js('World Preservation'), Js('World Provision'), Js('World Supervision'), Js('World Sustenance')]))
var.put('nm2', Js([Js('Alliance'), Js('Bond'), Js('Coalition'), Js('League'), Js('Nations'), Js('Treaty'), Js('Union'), Js('Federation'), Js('Confederation'), Js('Syndicate')]))
pass
pass


# Add lib to the module scope
allianceNames = var.to_python()