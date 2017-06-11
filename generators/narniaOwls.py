__all__ = ['narniaOwls']

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
    var.put('nm1', Js([Js('arch'), Js('band'), Js('beam'), Js('bell'), Js('bend'), Js('bleak'), Js('bold'), Js('brash'), Js('brass'), Js('cave'), Js('cloud'), Js('clue'), Js('cold'), Js('cream'), Js('dark'), Js('dawn'), Js('dim'), Js('dirt'), Js('dive'), Js('draft'), Js('dusk'), Js('dust'), Js('edge'), Js('fan'), Js('flame'), Js('flight'), Js('flock'), Js('flow'), Js('fluke'), Js('fog'), Js('force'), Js('frost'), Js('ghost'), Js('gift'), Js('glass'), Js('glim'), Js('glint'), Js('gloom'), Js('glow'), Js('glum'), Js('gold'), Js('grace'), Js('grand'), Js('great'), Js('grim'), Js('hex'), Js('high'), Js('hook'), Js('ice'), Js('ink'), Js('iron'), Js('light'), Js('lock'), Js('lone'), Js('long'), Js('loud'), Js('lush'), Js('mad'), Js('mass'), Js('mist'), Js('moon'), Js('mud'), Js('murk'), Js('night'), Js('pale'), Js('perk'), Js('phantom'), Js('phase'), Js('plume'), Js('plump'), Js('prime'), Js('quick'), Js('quill'), Js('rain'), Js('rash'), Js('shade'), Js('shadow'), Js('silk'), Js('silver'), Js('sky'), Js('slim'), Js('smoke'), Js('soot'), Js('spirit'), Js('spite'), Js('spot'), Js('star'), Js('steel'), Js('storm'), Js('stout'), Js('sun'), Js('thick'), Js('thorn'), Js('thrift'), Js('thunder'), Js('tranquil'), Js('trim'), Js('veil'), Js('vex'), Js('wild'), Js('woe')]))
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
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('beak'), Js('belly'), Js('bill'), Js('breast'), Js('claw'), Js('crest'), Js('crown'), Js('eye'), Js('eyes'), Js('feather'), Js('head'), Js('mantle'), Js('plume'), Js('tail'), Js('talon'), Js('wing'), Js('wings')]))
pass
pass


# Add lib to the module scope
narniaOwls = var.to_python()