__all__ = ['apocalypseNames']

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
var.put('nm1', Js([Js('Armageddon'), Js('Bane of Mankind'), Js('The Catastrophic Experiment'), Js('The Cleansing Rains'), Js('Corruption of Mankind'), Js('Dawn of Destruction'), Js('Dawn of the Others'), Js('Dawn of the Walkers'), Js('Day of the Dead'), Js('Death of the Moon'), Js('Death of the Sun'), Js('Decimation of Mankind'), Js('Dusk of Mankind'), Js('End of the Living'), Js('Eternal Darkness'), Js('Fatal Impact'), Js('Final Hour'), Js('Final Impact'), Js('Frozen Hell'), Js('Garbage Day'), Js('Global Freezing'), Js('Global Warming'), Js('Judgement Day'), Js('Last Steps'), Js("Man's Greed"), Js("Mankind's Arrogance"), Js("Mankind's Betrayal"), Js("Mankind's Disgrace"), Js("Mankind's Expiration"), Js("Mankind's Ignorance"), Js("Nature's Vengeance"), Js('Our Expiration Date'), Js('Our Mutual Destruction'), Js('Our Wrong Choice'), Js('Rains of Death'), Js('Self-Assisted Damnation'), Js('Technological Destruction'), Js('Technological Expiration'), Js('Terminal Velocity'), Js('Terminus'), Js('The Annihilation'), Js('The Backfire'), Js('The Beginning'), Js('The Burning Rain'), Js('The Burning Skies'), Js('The Burning Winds'), Js('The Cataclysm'), Js('The Cleansing'), Js('The Collapse'), Js('The Collapse of Mankind'), Js('The Collision'), Js('The Combustion'), Js('The Conclusion'), Js('The Decimation'), Js('The Decimation of Mankind'), Js('The Departure'), Js('The Desolation of Mankind'), Js('The Detonation'), Js('The Disaster'), Js('The Drought'), Js('The Dry Rains'), Js('The End of Resources'), Js('The Erupting Earth'), Js('The Eternal Day'), Js('The Eternal Night'), Js('The Eternal Rains'), Js('The Eternal Storm'), Js('The Experiment'), Js('The Final Encounter'), Js('The First Encounter'), Js('The Flood'), Js('The Food Chain Collapse'), Js('The Immolation'), Js('The Invasion'), Js('The Killing Days'), Js('The Manifestation'), Js('The Meteor'), Js('The Nuclear Event'), Js('The Ozone Event'), Js('The Permafrost'), Js('The Phenomenon'), Js('The Purge'), Js('The Purification'), Js('The Putrefaction'), Js('The Rapture'), Js('The Revelation'), Js('The Rupture'), Js('The Sacrifice'), Js('The Severance'), Js('The Showdown'), Js('The Sterilization'), Js('The Sundering'), Js('The Tipping Point'), Js('The Visitors'), Js('The Wipe Out'), Js('Total Annihilation'), Js('Toxic Rain'), Js('Winds of Death'), Js('World War Final'), Js('Our Execution'), Js("Nature's Judgement"), Js('The Omega Event'), Js('The Cosmic Annihilation')]))
pass
pass


# Add lib to the module scope
apocalypseNames = var.to_python()