__all__ = ['bansheeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm2', 'result'])
    var.put('nm1', Js([Js('Abandoned'), Js('Aching'), Js('Agony'), Js('Anguish'), Js('Anguished'), Js('Bawling'), Js('Bitter'), Js('Blaring'), Js('Blind'), Js('Bloodied'), Js('Bloody'), Js('Broken'), Js('Burning'), Js('Cackling'), Js('Craven'), Js('Crazed'), Js('Crying'), Js('Dark'), Js('Deafening'), Js('Depraved'), Js('Deranged'), Js('Dire'), Js('Distressed'), Js('Drained'), Js('Dread'), Js('Dreadful'), Js('Enraged'), Js('Evanescent'), Js('Faded'), Js('Fading'), Js('Flustered'), Js('Forsaken'), Js('Frail'), Js('Grave'), Js('Grieving'), Js('Grievous'), Js('Grim'), Js('Haunted'), Js('Haunting'), Js('Heartrending'), Js('Heartsick'), Js('Hollow'), Js('Hopeless'), Js('Howling'), Js('Humming'), Js('Hurt'), Js('Hysterical'), Js('Ivory'), Js('Lamenting'), Js('Lone'), Js('Lonely'), Js('Lost'), Js('Mad'), Js('Maniacal'), Js('Manic'), Js('Mewling'), Js('Miserable'), Js('Misery'), Js('Moaning'), Js('Mournful'), Js('Mourning'), Js('Praying'), Js('Ringing'), Js('Roaming'), Js('Screaming'), Js('Screeching'), Js('Searching'), Js('Seeking'), Js('Shadowy'), Js('Shady'), Js('Shrieking'), Js('Silver'), Js('Sinister'), Js('Skeletal'), Js('Skinny'), Js('Slivery'), Js('Sniveling'), Js('Sobbing'), Js('Sorrowing'), Js('Sorrowing'), Js('Spiteful'), Js('Tearful'), Js('Torment'), Js('Tormented'), Js('Tortured'), Js('Vengeful'), Js('Vexed'), Js('Vicious'), Js('Wailing'), Js('Wandering'), Js('Warped'), Js('Waving'), Js('Weeping'), Js('Whimpering'), Js('Whining'), Js('Wicked'), Js('Woeful'), Js('Worn'), Js('Wretched'), Js('Yammering'), Js('Yelling'), Js('Yelping')]))
    var.put('nm2', Js([Js('Apparition'), Js('Banshee'), Js('Bride'), Js('Bridesmaid'), Js('Dame'), Js('Damsel'), Js('Daughter'), Js('Gal'), Js('Girl'), Js('Lady'), Js('Maid'), Js('Maiden'), Js('Matriarch'), Js('Matron'), Js('Mother'), Js('Nurse'), Js('Priestess'), Js('Soul'), Js('Specter'), Js('Spirit'), Js('Widow'), Js('Woman'), Js('Wraith'), Js('Angel'), Js('Lover'), Js('Fiancee'), Js('Child'), Js('Youth'), Js('Aunt')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
bansheeNames = var.to_python()