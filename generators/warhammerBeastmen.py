__all__ = ['warhammerBeastmen']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                while PyJsStrictEq(var.get('nm5').get(var.get('rnd')),var.get('nm6').get(var.get('rnd2'))):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', (var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('k'), Js('kn'), Js('kh'), Js('m'), Js('n'), Js('t'), Js('th'), Js('v'), Js('z'), Js('zh')]))
var.put('nm2', Js([Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('e'), Js('i'), Js('e'), Js('i'), Js('au'), Js('ao'), Js('aa'), Js('oo')]))
var.put('nm3', Js([Js('cr'), Js('cn'), Js('cc'), Js('cv'), Js('cth'), Js('g'), Js('gh'), Js('gth'), Js('gd'), Js('gdh'), Js('k'), Js('kh'), Js('kz'), Js('kk'), Js('kr'), Js('kt'), Js('kth'), Js('l'), Js('lg'), Js('lgh'), Js('lgr'), Js('ltr'), Js('lc'), Js('n'), Js('ng'), Js('nk'), Js('nc'), Js('r'), Js('rr'), Js('rz'), Js('rg'), Js('rk'), Js('rkr'), Js('rgh'), Js('rth'), Js('zr'), Js('zg'), Js('zc'), Js('zk'), Js('zz')]))
var.put('nm4', Js([Js('c'), Js('g'), Js('k'), Js('r'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('amber'), Js('ashen'), Js('battle'), Js('bitter'), Js('black'), Js('blazing'), Js('bleeding'), Js('blood'), Js('bright'), Js('bristle'), Js('broad'), Js('brown'), Js('chaos'), Js('cinder'), Js('dark'), Js('dawn'), Js('dead'), Js('death'), Js('ember'), Js('fallen'), Js('fiery'), Js('fire'), Js('flame'), Js('frozen'), Js('giant'), Js('gloom'), Js('gore'), Js('grand'), Js('gray'), Js('great'), Js('grim'), Js('grizzly'), Js('heavy'), Js('hell'), Js('iron'), Js('keen'), Js('lightning'), Js('lone'), Js('metal'), Js('molten'), Js('moon'), Js('morning'), Js('moss'), Js('mountain'), Js('nether'), Js('night'), Js('onyx'), Js('plain'), Js('proud'), Js('pyre'), Js('rage'), Js('rapid'), Js('rough'), Js('rumble'), Js('serpent'), Js('shadow'), Js('sharp'), Js('shatter'), Js('silent'), Js('silver'), Js('slug'), Js('solid'), Js('spring'), Js('star'), Js('steel'), Js('stern'), Js('stone'), Js('storm'), Js('strong'), Js('swift'), Js('thunder'), Js('wild')]))
var.put('nm6', Js([Js('arm'), Js('bane'), Js('belly'), Js('belt'), Js('braid'), Js('breath'), Js('brow'), Js('chest'), Js('chin'), Js('claw'), Js('coat'), Js('crest'), Js('eye'), Js('eyes'), Js('fang'), Js('fangs'), Js('feet'), Js('finger'), Js('fingers'), Js('fist'), Js('foot'), Js('gaze'), Js('grip'), Js('gut'), Js('hair'), Js('hand'), Js('hands'), Js('head'), Js('heart'), Js('hide'), Js('jaw'), Js('mane'), Js('manes'), Js('mantle'), Js('maw'), Js('mouth'), Js('paw'), Js('pelt'), Js('ridge'), Js('scar'), Js('shoulder'), Js('shoulders'), Js('snout'), Js('spine'), Js('tail'), Js('teeth'), Js('toe'), Js('toes'), Js('tongue'), Js('tooth'), Js('wound')]))
pass
pass


# Add lib to the module scope
warhammerBeastmen = var.to_python()