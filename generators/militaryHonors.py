__all__ = ['militaryHonors']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'nm2', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Adamant'), Js("Angel's"), Js('Angelic'), Js('Blessed'), Js('Brass'), Js('Brave'), Js('Bright'), Js('Cooperative'), Js('Courageous'), Js("Crown's"), Js('Dependable'), Js('Dependent'), Js('Devoted'), Js('Diamond'), Js('Diligent'), Js('Distinguished'), Js('Divine'), Js('Dutiful'), Js('Earnest'), Js('Elated'), Js('Emerald'), Js('Eternal'), Js('Ethereal'), Js('Exalted'), Js('Fearless'), Js('Flawless'), Js('Fragile'), Js('Gilded'), Js('Glorious'), Js('Golden'), Js('Grateful'), Js('Grieving'), Js('Hallowed'), Js('Heavenly'), Js('Honorable'), Js('Honored'), Js('Infinite'), Js('Ivory'), Js('Jade'), Js('Loyal'), Js('Majestic'), Js('Marbled'), Js('Merciful'), Js('Mighty'), Js('Radiant'), Js('Resonant'), Js('Royal'), Js('Ruby'), Js('Sapphire'), Js('Serene'), Js('Silent'), Js('Silver'), Js('Tranquil'), Js('United'), Js('Velvet'), Js('Venerated'), Js('Vibrant'), Js('Victorious'), Js('Vigilant'), Js('Winged')]))
    var.put('nm2', Js([Js('Air Force'), Js('Army'), Js('Bravery'), Js('Clarity'), Js('Conduct'), Js('Corps'), Js('Defense'), Js('Efficiency'), Js('Excellence'), Js('Flying'), Js('Freedom'), Js('Gallantry'), Js('Independence'), Js('Liberation'), Js('Liberty'), Js('Loyalty'), Js('Marine'), Js('Marksmanship'), Js('Merit'), Js('Navy'), Js('Peace'), Js('Regiment'), Js('Service'), Js('Services'), Js('Soldier'), Js('Special Operations'), Js('Virtue'), Js('Volunteer'), Js('Volunteering')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            if (var.get('i')<Js(4.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
                    var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
                    var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                    var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm3', Js([Js('Commendation'), Js('Crescent'), Js('Cross'), Js('Decoration'), Js('Heart'), Js('Laurel'), Js('Medal'), Js('Medallion'), Js('Order'), Js('Ribbon'), Js('Sigil'), Js('Star')]))
pass
pass


# Add lib to the module scope
militaryHonors = var.to_python()