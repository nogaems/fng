__all__ = ['ghostTownNames']

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
    var.put('nm1', Js([Js('ail'), Js('alder'), Js('amber'), Js('arach'), Js('ash'), Js('ashen'), Js('bane'), Js('bare'), Js('barren'), Js('bitter'), Js('black'), Js('bleak'), Js('bligh'), Js('blight'), Js('boon'), Js('brow'), Js('burn'), Js('cease'), Js('char'), Js('charring'), Js('ebon'), Js('onyx'), Js('cinder'), Js('clear'), Js('cold'), Js('crag'), Js('cri'), Js('crow'), Js('dark'), Js('dawn'), Js('death'), Js('deci'), Js('demo'), Js('dew'), Js('dia'), Js('diabo'), Js('dire'), Js('dread'), Js('dusk'), Js('dust'), Js('ember'), Js('fall'), Js('fallen'), Js('far'), Js('farrow'), Js('fes'), Js('fester'), Js('fire'), Js('flame'), Js('flaw'), Js('fog'), Js('fore'), Js('forge'), Js('forging'), Js('frost'), Js('full'), Js('gaze'), Js('ghos'), Js('gloom'), Js('glum'), Js('glumming'), Js('gore'), Js('gray'), Js('grim'), Js('grimming'), Js('hard'), Js('hazel'), Js('il'), Js('ill'), Js('kil'), Js('lo'), Js('lon'), Js('lone'), Js('low'), Js('mad'), Js('mali'), Js('mar'), Js('mause'), Js('maw'), Js('mise'), Js('mourn'), Js('mourning'), Js('mur'), Js('murk'), Js('nec'), Js('necro'), Js('nether'), Js('ni'), Js('nigh'), Js('night'), Js('pyre'), Js('reaper'), Js('reaver'), Js('ridge'), Js('rip'), Js('ripping'), Js('saur'), Js('scorch'), Js('ser'), Js('serpen'), Js('shadow'), Js('shar'), Js('shard'), Js('shel'), Js('shell'), Js('sla'), Js('slate'), Js('sly'), Js('spi'), Js('spine'), Js('talon'), Js('thorn'), Js('thorne'), Js('vile'), Js('vin'), Js('vine'), Js('wear'), Js('weep'), Js('weeping'), Js('wither'), Js('woe'), Js('wrath')]))
    var.put('nm2', Js([Js('borough'), Js('brook'), Js('brooke'), Js('burg'), Js('burgh'), Js('burn'), Js('bury'), Js('fall'), Js('ford'), Js('fort'), Js('gate'), Js('helm'), Js('mere'), Js('mire'), Js('moor'), Js('more'), Js('moure'), Js('mourn'), Js('rest'), Js('ridge'), Js('thorn'), Js('thorne'), Js('ton'), Js('town'), Js('ville')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm2').get(var.get('rnd2'))):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
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
ghostTownNames = var.to_python()