__all__ = ['lands']

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
            if (var.get('i')<Js(5.0)):
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Haunted'), Js('Naked'), Js('Angry'), Js('Arctic'), Js('Arid'), Js('Bare'), Js('Barren'), Js('Black'), Js('Bleak'), Js('Boiling'), Js('Bone-Dry'), Js('Burned'), Js('Burning'), Js('Calm'), Js('Calmest'), Js('Charmed'), Js('Cunning'), Js('Cursed'), Js('Dangerous'), Js('Dark'), Js('Darkest'), Js('Dead'), Js('Decayed'), Js('Decaying'), Js('Dehydrated'), Js('Depraved'), Js('Deserted'), Js('Desolate'), Js('Desolated'), Js('Distant'), Js('Dread'), Js('Dreaded'), Js('Dreadful'), Js('Dreary'), Js('Dry'), Js('Eastern'), Js('Empty'), Js('Enchanted'), Js('Ethereal'), Js('Ever Reaching'), Js('Everlasting'), Js('Feared'), Js('Fearsome'), Js('Fiery'), Js('Flat'), Js('Forbidden'), Js('Forbidding'), Js('Frightening'), Js('Frozen'), Js('Grave'), Js('Grim'), Js('Hellish'), Js('Homeless'), Js('Hopeless'), Js('Hot'), Js('Hungry'), Js('Infernal'), Js('Infinite'), Js('Isolated'), Js('Killing'), Js('Laughing'), Js('Lifeless'), Js('Light'), Js('Lightest'), Js('Lonely'), Js('Malevolent'), Js('Malicious'), Js('Mighty'), Js('Mirrored'), Js('Misty'), Js('Moaning'), Js('Monotonous'), Js('Motionless'), Js('Mysterious'), Js('Narrow'), Js('Neverending'), Js('Northern'), Js('Open'), Js('Painful'), Js('Parched'), Js('Perfumed'), Js('Quiet'), Js('Raging'), Js('Red'), Js('Restless'), Js('Rocky'), Js('Sad'), Js('Sandy'), Js('Sanguine'), Js('Savage'), Js('Scorching'), Js('Scorched'), Js('Shadowed'), Js('Silent'), Js('Sly'), Js('Soundless'), Js('Southern'), Js('Sterile'), Js('Thundering'), Js('Treacherous'), Js('Twisting'), Js('Uncanny'), Js('Uninteresting'), Js('Uninviting'), Js('Unknown'), Js('Unresting'), Js('Unwelcoming'), Js('Vast'), Js('Violent'), Js('Voiceless'), Js('Waterless'), Js('Western'), Js('Whispering'), Js('White'), Js('Windy'), Js('Withered'), Js('Yelling'), Js('Yellow')]))
var.put('nm2', Js([Js('Badlands'), Js('Barrens'), Js('Borderlands'), Js('Desert'), Js('Expanse'), Js('Fields'), Js('Grasslands'), Js('Hinterland'), Js('Prairie'), Js('Savanna'), Js('Steppes'), Js('Tundra'), Js('Wasteland'), Js('Wastes'), Js('Wilderness'), Js('Wilds'), Js('Emptyness'), Js('Frontier'), Js('Flatlands')]))
pass
pass


# Add lib to the module scope
lands = var.to_python()