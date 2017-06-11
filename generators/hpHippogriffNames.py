__all__ = ['hpHippogriffNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Agile'), Js('Beauty'), Js('Blitz'), Js('Breeze'), Js('Brisk'), Js('Buck'), Js('Charge'), Js('Class'), Js('Dart'), Js('Dash'), Js('Draft'), Js('Fleet'), Js('Flow'), Js('Flurry'), Js('Flux'), Js('Gale'), Js('Gentle'), Js('Glamor'), Js('Grace'), Js('Guard'), Js('Gust'), Js('Hale'), Js('Hate'), Js('Hurricane'), Js('Iron'), Js('Keen'), Js('Loud'), Js('Mellow'), Js('Nimble'), Js('Quick'), Js('Quiet'), Js('Rough'), Js('Rush'), Js('Sharp'), Js('Silk'), Js('Soft'), Js('Spirit'), Js('Spry'), Js('Stark'), Js('Steel'), Js('Storm'), Js('Stout'), Js('Strong'), Js('Surge'), Js('Swift'), Js('Tame'), Js('Tender'), Js('Thunder'), Js('Wild'), Js('Wind')]))
var.put('nm2', Js([Js('beak'), Js('bill'), Js('claw'), Js('colt'), Js('eye'), Js('feather'), Js('fluff'), Js('fringe'), Js('hoof'), Js('hook'), Js('mane'), Js('plume'), Js('quill'), Js('scream'), Js('screech'), Js('steed'), Js('tail'), Js('talon'), Js('tuft'), Js('wing')]))
pass
pass


# Add lib to the module scope
hpHippogriffNames = var.to_python()