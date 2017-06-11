__all__ = ['hpDragonNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('names', (((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Algerian'), Js('American'), Js('Angolan'), Js('Antarctic'), Js('Argentinian'), Js('Armenian'), Js('Australian'), Js('Austrian'), Js('Bolivian'), Js('Brazilian'), Js('British'), Js('Bulgarian'), Js('Cambodian'), Js('Canadian'), Js('Chilean'), Js('Chinese'), Js('Croatian'), Js('Cuban'), Js('Danish'), Js('Egyptian'), Js('Finnish'), Js('French'), Js('German'), Js('Hungarian'), Js('Indian'), Js('Irish'), Js('Italian'), Js('Jamaican'), Js('Japanese'), Js('Mexican'), Js('Mongolian'), Js('Moroccan'), Js('Nepalese'), Js('Norwegian'), Js('Peruvian'), Js('Romanian'), Js('Russian'), Js('Slovenian'), Js('South-African'), Js('Spanish'), Js('Swedish'), Js('Thai'), Js('Turkish'), Js('Ukrainian'), Js('Vietnamese')]))
var.put('nm2', Js([Js('Barb'), Js('Blaze'), Js('Bristle'), Js('Dart'), Js('Demon'), Js('Ember'), Js('Fire'), Js('Flame'), Js('Foul'), Js('Fury'), Js('Giant'), Js('Glow'), Js('Horn'), Js('Iron'), Js('Jade'), Js('Long'), Js('Mammoth'), Js('Monster'), Js('Opal'), Js('Plate'), Js('Rage'), Js('Ridge'), Js('Ruby'), Js('Short'), Js('Smooth'), Js('Snake'), Js('Soft'), Js('Spark'), Js('Spike'), Js('Steel'), Js('Storm'), Js('Swift'), Js('Thin'), Js('Thorn'), Js('Thunder'), Js('Venom'), Js('Vile'), Js('Viper'), Js('Warp'), Js('Wide')]))
var.put('nm3', Js([Js('back'), Js('belly'), Js('bottom'), Js('claw'), Js('crown'), Js('dart'), Js('eye'), Js('fang'), Js('frame'), Js('gut'), Js('head'), Js('horn'), Js('muzzle'), Js('paw'), Js('rump'), Js('scale'), Js('skull'), Js('snout'), Js('spike'), Js('stub'), Js('tail'), Js('tooth'), Js('trunk'), Js('tusk'), Js('wing')]))
pass
pass


# Add lib to the module scope
hpDragonNames = var.to_python()