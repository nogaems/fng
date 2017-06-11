__all__ = ['narniaCentaurs']

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
    var.put('nm1', Js([Js('agile'), Js('arch'), Js('bitter'), Js('blank'), Js('bold'), Js('brass'), Js('brave'), Js('broken'), Js('charge'), Js('cloud'), Js('cold'), Js('copper'), Js('copse'), Js('court'), Js('crown'), Js('dark'), Js('deep'), Js('den'), Js('diamond'), Js('dim'), Js('dirt'), Js('dream'), Js('drum'), Js('dual'), Js('dust'), Js('earth'), Js('earthen'), Js('even'), Js('fire'), Js('flame'), Js('fluke'), Js('fog'), Js('free'), Js('frost'), Js('ghost'), Js('glass'), Js('glen'), Js('gold'), Js('good'), Js('grand'), Js('great'), Js('grey'), Js('grim'), Js('grove'), Js('half'), Js('heart'), Js('ice'), Js('ink'), Js('iron'), Js('kind'), Js('light'), Js('lightning'), Js('lone'), Js('long'), Js('loud'), Js('lunar'), Js('mad'), Js('mask'), Js('meadow'), Js('might'), Js('mind'), Js('mist'), Js('moon'), Js('mud'), Js('night'), Js('phase'), Js('prime'), Js('proud'), Js('quiver'), Js('rain'), Js('rich'), Js('river'), Js('roon'), Js('rough'), Js('rush'), Js('shadow'), Js('silk'), Js('silver'), Js('single'), Js('sky'), Js('slim'), Js('smoke'), Js('snow'), Js('solar'), Js('spark'), Js('star'), Js('stark'), Js('stone'), Js('sun'), Js('swift'), Js('tall'), Js('temper'), Js('thunder'), Js('wind'), Js('wise'), Js('wood'), Js('world'), Js('young')]))
    var.put('nm2', Js([Js('arm'), Js('back'), Js('band'), Js('bolt'), Js('chance'), Js('charge'), Js('chest'), Js('clap'), Js('cloud'), Js('clover'), Js('coil'), Js('crest'), Js('crown'), Js('dance'), Js('dream'), Js('drum'), Js('edge'), Js('fire'), Js('flame'), Js('grace'), Js('grip'), Js('heart'), Js('hoof'), Js('horn'), Js('hunt'), Js('light'), Js('lock'), Js('mane'), Js('mask'), Js('might'), Js('mind'), Js('mist'), Js('pride'), Js('reach'), Js('rest'), Js('ridge'), Js('root'), Js('run'), Js('runner'), Js('shine'), Js('star'), Js('stone'), Js('storm'), Js('tale'), Js('trail'), Js('veil'), Js('web'), Js('wish'), Js('wit'), Js('worth')]))
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
narniaCentaurs = var.to_python()