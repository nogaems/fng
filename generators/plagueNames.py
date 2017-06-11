__all__ = ['plagueNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Aberration'), Js('Abnormality'), Js('Alpha'), Js('Ancient'), Js('Annihilation'), Js('Anomaly'), Js('Apex'), Js('Aquatic'), Js('Austere'), Js('Bare'), Js('Barren'), Js('Berserker'), Js('Bitter'), Js('Black'), Js('Bleak'), Js('Blind'), Js('Blinding'), Js('Burning'), Js('Chaos'), Js('Chronic'), Js('Crazed'), Js('Creeping'), Js('Crippling'), Js('Crusty'), Js('Curtains'), Js('Dawn'), Js('Deadline'), Js('Dehydration'), Js('Delirium'), Js('Deluge'), Js('Delusion'), Js('Demise'), Js('Desperate'), Js('Desperation'), Js('Deviation'), Js('Dire'), Js('Doom'), Js('Dread'), Js('Dusk'), Js('Ebon'), Js('End'), Js('Ending'), Js('Extinction'), Js('Extreme'), Js('Extremist'), Js('Feral'), Js('Fierce'), Js('Finale'), Js('Forlorn'), Js('Fragment'), Js('Frenzy'), Js('Frozen'), Js('Fuming'), Js('Funereal'), Js('Fury'), Js('Futile'), Js('Global'), Js('Gloom'), Js('God'), Js('Grave'), Js('Great'), Js('Grievous'), Js('Grim'), Js('Grisly'), Js('Horrid'), Js('Howling'), Js('Hysteria'), Js('Illusion'), Js('Immortal'), Js('Inferior'), Js('Inhuman'), Js('Insanity'), Js('Invincible'), Js('Ire'), Js('Iron'), Js('Ivory'), Js('K.O.'), Js('Last'), Js('Laughing'), Js('Limbo'), Js('Lingering'), Js('Lost'), Js('Lunacy'), Js('Lunar'), Js('Lurking'), Js('Mad'), Js('Malevolent'), Js('Mania'), Js('Maniac'), Js('Massacre'), Js('Merciless'), Js('Molten'), Js('Morose'), Js('Mortal'), Js('Necrosis'), Js('Necrotic'), Js('Neglect'), Js('Neglected'), Js('Neurosis'), Js('Nightmare'), Js('Oblivion'), Js('Obsidian'), Js('Omega'), Js('Onyx'), Js('Original'), Js('Paragon'), Js('Particle'), Js('Phantom'), Js('Pinnacle'), Js('Prime'), Js('Primeval'), Js('Primitive'), Js('Primordial'), Js('Rabid'), Js('Radical'), Js('Reaper'), Js('Recurring'), Js('Relentless'), Js('Repose'), Js('Returning'), Js('Ruthless'), Js('Sadistic'), Js('Savage'), Js('Scalding'), Js('Second'), Js('Shadow'), Js('Silence'), Js('Silent'), Js('Singularity'), Js('Sleeper'), Js('Sleeping'), Js('Smothering'), Js('Solar'), Js('Spasm'), Js('Stark'), Js('Storm'), Js('Stubborn'), Js('Superior'), Js('Tearing'), Js('Terminal'), Js('Terminus'), Js('Terror'), Js('Third'), Js('Titan'), Js('Tomb'), Js('Torture'), Js('Turbulent'), Js('Twilight'), Js('Uncontrollable'), Js('Underestimated'), Js('Unseen'), Js('Veiled'), Js('Vertex'), Js('Violent'), Js('Void'), Js('Vortex'), Js('White'), Js('Wild'), Js('Wildlife'), Js('World'), Js('Wretched'), Js('Zombie')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('Affliction'), Js('Contagion'), Js('Death'), Js('Epidemic'), Js('Infestation'), Js('Outbreak'), Js('Pandemic'), Js('Plague'), Js('Scourge')]))
pass
pass


# Add lib to the module scope
plagueNames = var.to_python()