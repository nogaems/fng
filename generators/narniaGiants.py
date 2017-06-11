__all__ = ['narniaGiants']

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
    var.put('nm1', Js([Js('anger'), Js('band'), Js('basin'), Js('bitter'), Js('bother'), Js('boulder'), Js('bramble'), Js('bubble'), Js('bumble'), Js('butter'), Js('button'), Js('cannon'), Js('cattle'), Js('cloud'), Js('cobble'), Js('common'), Js('copper'), Js('crumble'), Js('dabble'), Js('dimple'), Js('double'), Js('garden'), Js('good'), Js('grand'), Js('ground'), Js('long'), Js('lumber'), Js('marble'), Js('middle'), Js('moon'), Js('mud'), Js('mumble'), Js('night'), Js('nimble'), Js('pebble'), Js('plane'), Js('pocket'), Js('powder'), Js('puddle'), Js('ramble'), Js('range'), Js('rich'), Js('riddle'), Js('river'), Js('rock'), Js('rumble'), Js('scratch'), Js('shadow'), Js('shock'), Js('silver'), Js('simple'), Js('slumber'), Js('spark'), Js('stone'), Js('storm'), Js('struggle'), Js('tackle'), Js('thunder'), Js('trouble'), Js('tumble'), Js('weather'), Js('whistle'), Js('wild'), Js('wobble'), Js('wonder')]))
    var.put('nm2', Js([Js('back'), Js('balance'), Js('basin'), Js('bead'), Js('berry'), Js('block'), Js('bottom'), Js('boulder'), Js('branch'), Js('breath'), Js('bubble'), Js('buffer'), Js('buffin'), Js('button'), Js('chin'), Js('cloud'), Js('coat'), Js('cover'), Js('crown'), Js('cushion'), Js('dance'), Js('dock'), Js('drag'), Js('dream'), Js('drum'), Js('feature'), Js('foot'), Js('force'), Js('friend'), Js('grace'), Js('growth'), Js('guard'), Js('guide'), Js('habit'), Js('hand'), Js('heart'), Js('hide'), Js('kin'), Js('kind'), Js('knot'), Js('link'), Js('loaf'), Js('lock'), Js('lumber'), Js('marble'), Js('march'), Js('mask'), Js('might'), Js('mind'), Js('mountain'), Js('move'), Js('noise'), Js('paint'), Js('patch'), Js('plate'), Js('plot'), Js('point'), Js('pound'), Js('pride'), Js('rest'), Js('rhythm'), Js('ride'), Js('roll'), Js('root'), Js('run'), Js('rush'), Js('scratch'), Js('shift'), Js('shine'), Js('shock'), Js('shot'), Js('slumber'), Js('spark'), Js('spell'), Js('stand'), Js('storm'), Js('stream'), Js('string'), Js('swing'), Js('thunder'), Js('tool'), Js('tremor'), Js('tune'), Js('wave'), Js('weather'), Js('wind'), Js('wire'), Js('zephyr'), Js('zone')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            if PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm2').get(var.get('rnd2'))):
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
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
narniaGiants = var.to_python()