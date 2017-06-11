__all__ = ['postSocietyNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen', 'names3'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', ((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd1'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('names', (Js('The ')+var.get('names3').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Abandoned'), Js('Aberration'), Js('Abnormality'), Js('Abomination'), Js('Acid'), Js('Acidic'), Js('Acrid'), Js('Amnesia'), Js('Anomaly'), Js('Armageddon'), Js('Asylum'), Js('Babylon'), Js('Black Ashes'), Js('Black Dust'), Js('Black Earth'), Js('Black Moon'), Js('Black Rain'), Js('Black Sun'), Js('Blessed'), Js('Burning World'), Js('Cataclysm'), Js('Chaos'), Js('Cockroach'), Js('Decimation'), Js('Desolate'), Js('Deviant'), Js('Dominance'), Js('Eclipse'), Js('Ember'), Js('Enigma'), Js('Eternal'), Js('Eternal Darkness'), Js('Eternal Eclipse'), Js('Eternal Fire'), Js('Eternal Void'), Js('Evolution'), Js('Extinction'), Js('Fallen Star'), Js('Fallout'), Js('False Prophet'), Js('Forsaken'), Js('Found Fortune'), Js('Gifts of Mutation'), Js('Godless'), Js('Honor'), Js('Honorbound'), Js('Human Expiration'), Js('Human Extinction'), Js('Human Hunter'), Js('Isolation'), Js('Law Abiding'), Js('Lawless'), Js('Legion'), Js('Limbo'), Js('Lost Soul'), Js('Martial Law'), Js('Metamorphosis'), Js('Miracle'), Js('Misery'), Js('Monster'), Js('Monster Hunter'), Js('Mutant'), Js('Mutant Hunter'), Js('Myriad'), Js('Neo-Human'), Js('New Friends'), Js('New God'), Js('New Haven'), Js('New Hope'), Js('New Law'), Js('New Monster'), Js('New Moon'), Js('New Prophet'), Js('New Start'), Js('New Sun'), Js('New Supremacy'), Js('New World'), Js('No Legacy'), Js('Nuclear'), Js('Oath'), Js('Oblivion'), Js('Old Ruins'), Js('Orphan'), Js('Our Legacy'), Js('Outcast'), Js('Paragon'), Js('Phoenix'), Js('Prodigy'), Js('Rebirth'), Js('Red Moon'), Js('Red Sun'), Js('Reincarnation'), Js('Resurrection'), Js('Revelation'), Js('Risen Ashes'), Js('Sanctuary'), Js('Survivor'), Js('Total Eclipse'), Js('Traitor'), Js('Warhead')]))
var.put('names2', Js([Js('Alliance'), Js('Association'), Js('Brotherhood'), Js('Clan'), Js('Coalition'), Js('Confederacy'), Js('Cooperative'), Js('Federation'), Js('Gang'), Js('League'), Js('Order'), Js('Republic'), Js('Syndicate'), Js('Tribe'), Js('Nation'), Js('Union')]))
var.put('names3', Js([Js('Abandoned'), Js('Aberrations'), Js('Abnormalities'), Js('Invincible'), Js('Abominations'), Js('Anomalies'), Js('Armageddons'), Js('Asylum'), Js('Babylonians'), Js('Black Ashes'), Js('Blessed'), Js('Chosen Ones'), Js('Cleansed'), Js('Cockroaches'), Js('Dead'), Js('Defiance'), Js('Deviants'), Js('Droplets'), Js('Enigmas'), Js('Eternals'), Js('Evolved'), Js('Expired'), Js('Extinct'), Js('Fallen'), Js('Flock'), Js('Forsaken'), Js('Freaks'), Js('Giants'), Js('Gifted'), Js('Godless'), Js('Hermits'), Js('Hidden'), Js('Homeless'), Js('Honorbound'), Js('Honorless'), Js('Horned Ones'), Js('Immune'), Js('Impure'), Js('Infected'), Js('Invisible'), Js('Law'), Js('Lawless'), Js('Legion'), Js('Living'), Js('Lost Ones'), Js('Lost Souls'), Js('Miracles'), Js('Monsters'), Js('Mutants'), Js('Myriad'), Js('Neo-Human'), Js('New Friends'), Js('New Humans'), Js('New Monsters'), Js('Newmans'), Js('Orphans'), Js('Outcasts'), Js('Paragons'), Js('Phantoms'), Js('Phoenixes'), Js('Prodigies'), Js('Pure'), Js('Purified'), Js('Rats'), Js('Reincarnated'), Js('Resurrected'), Js('Risen'), Js('Roaches'), Js('Salvation'), Js('Shadows'), Js('Stalkers'), Js('Survivors'), Js('Tails'), Js('Tormented'), Js('Vanished'), Js('Walkers'), Js('Warheads'), Js('White Ashes')]))
pass
pass


# Add lib to the module scope
postSocietyNames = var.to_python()