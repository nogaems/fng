__all__ = ['naturalDisasters']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', (((Js('The ')+var.get('names1').get(var.get('rnd')))+Js(' '))+var.get('names2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('200 minute'), Js('24 hour'), Js('50 minute'), Js('Abrupt'), Js('Almighty'), Js('Ambush'), Js('Annihilation'), Js('Blessed'), Js('Blight'), Js('Blocked'), Js('Boosted'), Js('Brief'), Js('Carnage'), Js('Cataclysmic'), Js('Cleansing'), Js('Collapsing'), Js('Corrupting'), Js('Crashing'), Js('Deception'), Js('Delayed'), Js('Demolition'), Js('Dire'), Js('Directed'), Js('Disrupted'), Js('Dormant'), Js('Double'), Js('Early Morning'), Js('Eclipse'), Js('Elimination'), Js('Endless'), Js('Eradication'), Js('Eternal'), Js('Evaded'), Js('Expiration'), Js('Exploding'), Js('Extermination'), Js('Extinction'), Js('Final'), Js('Gentle'), Js('Grave'), Js('Grim Reaper'), Js('Growing'), Js('Harmless'), Js('Idle'), Js('Intended'), Js('Interrupted'), Js('Last Minute'), Js('Lazy'), Js('Life-giving'), Js('Living'), Js('Man-made'), Js('Midnight'), Js('Midsummer'), Js('Midwinter'), Js('Mighty'), Js('Necrotic'), Js('Nightmare'), Js('Nonstop'), Js('Noxious'), Js('Obliteration'), Js('Overlooked'), Js('Persistent'), Js('Positive'), Js('Predicted'), Js('Rapid'), Js('Record'), Js('Released'), Js('Relentless'), Js('Seven Day'), Js('Shock'), Js('Shrouded'), Js('Silence'), Js('Sleeping'), Js('Sudden'), Js('Supported'), Js('Surreal'), Js('Swift'), Js('Tainted'), Js('Tainting'), Js('Tenacious'), Js('Tense'), Js('Thunder'), Js('Total Destruction'), Js('Toxic'), Js('Triple'), Js('Trivial'), Js('Twilight'), Js('Twin'), Js('Unbound'), Js('Unconstrained'), Js('Unforeseen'), Js('Unlimited'), Js('Unnatural'), Js('Unstoppable'), Js('Veiled'), Js('Vicious'), Js('Void'), Js('Weak'), Js('Wreckage'), Js('Wrecking')]))
var.put('names2', Js([Js('Hurricane'), Js('Flood'), Js('Tornado'), Js('Eruption'), Js('Avalanche'), Js('Drought'), Js('Hail Storm'), Js('Blizzard'), Js('Tsunami'), Js('Wildfire'), Js('Epidemic'), Js('Cyclone'), Js('Heat Wave'), Js('Solar Flare')]))
pass
pass


# Add lib to the module scope
naturalDisasters = var.to_python()