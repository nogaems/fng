__all__ = ['narniaBadgers']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'nm2', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('acorn'), Js('almond'), Js('apple'), Js('barley'), Js('bean'), Js('beet'), Js('beetroot'), Js('berry'), Js('bloom'), Js('bulb'), Js('button'), Js('carrot'), Js('cherry'), Js('corn'), Js('cress'), Js('crop'), Js('earthnut'), Js('fig'), Js('fruit'), Js('fungi'), Js('fungus'), Js('gourd'), Js('grain'), Js('grape'), Js('honey'), Js('jalap'), Js('kernel'), Js('maize'), Js('melon'), Js('morel'), Js('mushroom'), Js('nectar'), Js('oat'), Js('okra'), Js('onion'), Js('orange'), Js('parsnip'), Js('peach'), Js('peanut'), Js('pear'), Js('pecan'), Js('peel'), Js('plum'), Js('plume'), Js('pod'), Js('poppet'), Js('potato'), Js('prune'), Js('pulp'), Js('pumpkin'), Js('radish'), Js('root'), Js('rye'), Js('salep'), Js('sapling'), Js('shoot'), Js('spice'), Js('sprout'), Js('spud'), Js('squash'), Js('stalk'), Js('sugar'), Js('sugarbeet'), Js('taro'), Js('tater'), Js('toadstool'), Js('tomato'), Js('truffle'), Js('tuber'), Js('turnip'), Js('vine'), Js('walnut'), Js('yam')]))
    var.put('nm2', Js([Js('baker'), Js('belcher'), Js('biter'), Js('boiler'), Js('bringer'), Js('browser'), Js('bundler'), Js('burper'), Js('burrower'), Js('catcher'), Js('chaser'), Js('chopper'), Js('collector'), Js('cooker'), Js('counter'), Js('devourer'), Js('digger'), Js('diner'), Js('diver'), Js('dreamer'), Js('drooler'), Js('dropper'), Js('dunker'), Js('feeder'), Js('feeler'), Js('finder'), Js('fryer'), Js('gatherer'), Js('groomer'), Js('grower'), Js('guard'), Js('helper'), Js('hider'), Js('hoarder'), Js('hogger'), Js('holder'), Js('hunter'), Js('keeper'), Js('lover'), Js('masher'), Js('picker'), Js('planter'), Js('plucker'), Js('reacher'), Js('remover'), Js('rester'), Js('robber'), Js('savorer'), Js('scooper'), Js('scourer'), Js('seeker'), Js('shaker'), Js('shuffler'), Js('snatcher'), Js('sniffer'), Js('snooper'), Js('spotter'), Js('stacker'), Js('stasher'), Js('stealer'), Js('stocker'), Js('taker'), Js('taster'), Js('tender'), Js('tracker'), Js('washer')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm2').get(var.get('rnd2'))):
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
narniaBadgers = var.to_python()