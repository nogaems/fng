__all__ = ['metalNames']

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
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('i'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('pr'), Js('str'), Js('tr'), Js('bl'), Js('cl'), Js('fl'), Js('gl'), Js('pl'), Js('sl'), Js('sc'), Js('sk'), Js('sm'), Js('sn'), Js('sp'), Js('st'), Js('sw'), Js('ch'), Js('sh'), Js('th'), Js('wh'), Js('kr')]))
var.put('nm4', Js([Js('ae'), Js('ai'), Js('ao'), Js('au'), Js('a'), Js('ay'), Js('ea'), Js('ei'), Js('eo'), Js('eu'), Js('e'), Js('ey'), Js('ua'), Js('ue'), Js('ui'), Js('uo'), Js('u'), Js('uy'), Js('ia'), Js('ie'), Js('iu'), Js('io'), Js('iy'), Js('oa'), Js('oe'), Js('ou'), Js('oi'), Js('o'), Js('oy')]))
var.put('nm5', Js([Js('sium'), Js('cium'), Js('lium'), Js('rium'), Js('trium'), Js('tium'), Js('nese'), Js('nium'), Js('sten'), Js('nor'), Js('tine'), Js('ntine'), Js('rhil'), Js('thil'), Js('nyx'), Js('dian')]))
var.put('nm6', Js([Js('ium'), Js('ese'), Js('alt'), Js('um'), Js('ian'), Js('il'), Js('ine'), Js('yx'), Js('ite')]))
pass
pass


# Add lib to the module scope
metalNames = var.to_python()