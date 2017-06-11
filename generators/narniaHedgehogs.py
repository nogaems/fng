__all__ = ['narniaHedgehogs']

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
    var.put('nm1', Js([Js('addle'), Js('aidle'), Js('babble'), Js('baffle'), Js('bashle'), Js('bindle'), Js('boggle'), Js('bondle'), Js('breezle'), Js('buffle'), Js('burple'), Js('burrow'), Js('bustle'), Js('chatle'), Js('chipple'), Js('chopple'), Js('climble'), Js('comble'), Js('crackle'), Js('craddle'), Js('cuddle'), Js('dabble'), Js('dangle'), Js('dartle'), Js('dazzle'), Js('diggle'), Js('dipple'), Js('doffle'), Js('draggle'), Js('dribble'), Js('dripple'), Js('droople'), Js('dropple'), Js('dubble'), Js('dustle'), Js('feedle'), Js('fibble'), Js('fiddle'), Js('fittle'), Js('flapple'), Js('fumble'), Js('giggle'), Js('gobble'), Js('goggle'), Js('grabble'), Js('grapple'), Js('grasple'), Js('gripple'), Js('grumple'), Js('hobble'), Js('hoggle'), Js('hopple'), Js('huddle'), Js('huggle'), Js('hustle'), Js('jabble'), Js('jangle'), Js('juggle'), Js('knittle'), Js('lisple'), Js('lurkle'), Js('meddle'), Js('meeple'), Js('muggle'), Js('nibble'), Js('paddle'), Js('peekle'), Js('pickle'), Js('plopple'), Js('popple'), Js('proddle'), Js('puffle'), Js('ramble'), Js('riddle'), Js('ripple'), Js('rumble'), Js('rustle'), Js('scramble'), Js('scribble'), Js('scrubble'), Js('smirkle'), Js('sniffle'), Js('snuggle'), Js('startle'), Js('stumble'), Js('swattle'), Js('tapple'), Js('thumble'), Js('tickle'), Js('tipple'), Js('toddle'), Js('topple'), Js('tripple'), Js('waddle'), Js('waggle'), Js('wiggle'), Js('wriggle')]))
    pass
    var.put('nm2', Js([Js('badge'), Js('bag'), Js('bags'), Js('band'), Js('bat'), Js('bead'), Js('bell'), Js('belt'), Js('bet'), Js('bit'), Js('book'), Js('boot'), Js('boots'), Js('bottle'), Js('box'), Js('bun'), Js('butt'), Js('cakes'), Js('cap'), Js('caps'), Js('cart'), Js('cheek'), Js('cheeks'), Js('chin'), Js('chip'), Js('comb'), Js('cord'), Js('cork'), Js('crate'), Js('crib'), Js('dig'), Js('dish'), Js('dock'), Js('dot'), Js('drop'), Js('drum'), Js('feet'), Js('fog'), Js('fold'), Js('foot'), Js('gap'), Js('gear'), Js('gift'), Js('grab'), Js('grip'), Js('hand'), Js('hat'), Js('hold'), Js('hook'), Js('host'), Js('jam'), Js('jar'), Js('keep'), Js('key'), Js('knot'), Js('lab'), Js('lock'), Js('log'), Js('luck'), Js('mess'), Js('mud'), Js('need'), Js('needle'), Js('nose'), Js('note'), Js('pack'), Js('page'), Js('pin'), Js('pir'), Js('pit'), Js('pivk'), Js('plan'), Js('play'), Js('pop'), Js('pot'), Js('quill'), Js('rod'), Js('roll'), Js('root'), Js('rub'), Js('sack'), Js('share'), Js('ship'), Js('shop'), Js('slip'), Js('split'), Js('spot'), Js('stamp'), Js('step'), Js('stick'), Js('stock'), Js('store'), Js('strip'), Js('stuff'), Js('thread'), Js('tip'), Js('top'), Js('tub'), Js('vest'), Js('wit')]))
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
narniaHedgehogs = var.to_python()