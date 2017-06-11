__all__ = ['homestuckNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm0', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm0').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if (var.get('rnd2')>Js(29.0)):
                    while (var.get('rnd4')>Js(29.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if ((var.get('rnd2')<Js(30.0)) and (var.get('rnd4')<Js(30.0))):
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('namesf', ((((var.get('nm0').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
                else:
                    var.put('namesf', (((var.get('nm0').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    if (var.get('rnd2')>Js(29.0)):
                        while (var.get('rnd4')>Js(29.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    if ((var.get('rnd2')<Js(30.0)) and (var.get('rnd4')<Js(30.0))):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('namesf', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
                    else:
                        var.put('namesf', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4'))))
                else:
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    if (var.get('rnd2')>Js(29.0)):
                        if (var.get('rnd4')>Js(29.0)):
                            var.put('namesf', ((var.get('nm2').get(var.get('rnd2'))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4'))))
                        else:
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('namesf', (((var.get('nm2').get(var.get('rnd2'))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
                    else:
                        if (var.get('rnd4')>Js(29.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('namesf', (((var.get('nm2').get(var.get('rnd2'))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
                        else:
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('namesf', ((((var.get('nm2').get(var.get('rnd2'))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm3').get(var.get('rnd6'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if (var.get('rnd2')>Js(29.0)):
                    if (var.get('rnd4')>Js(29.0)):
                        var.put('names', ((((var.get('namesf')+Js(' '))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4'))))
                    else:
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', (((((var.get('namesf')+Js(' '))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
                else:
                    if (var.get('rnd4')>Js(29.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', (((((var.get('namesf')+Js(' '))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
                    else:
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', ((((((var.get('namesf')+Js(' '))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm3').get(var.get('rnd6'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm0').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    if (var.get('rnd2')>Js(29.0)):
                        while (var.get('rnd4')>Js(29.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    if ((var.get('rnd2')<Js(30.0)) and (var.get('rnd4')<Js(30.0))):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((var.get('namesf')+Js(' '))+var.get('nm0').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
                    else:
                        var.put('names', (((((var.get('namesf')+Js(' '))+var.get('nm0').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    if (var.get('rnd2')>Js(29.0)):
                        while (var.get('rnd4')>Js(29.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    if ((var.get('rnd2')<Js(30.0)) and (var.get('rnd4')<Js(30.0))):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((var.get('namesf')+Js(' '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
                    else:
                        var.put('names', (((((var.get('namesf')+Js(' '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm0', Js([Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('p'), Js('s'), Js('t'), Js('v'), Js('x'), Js('z')]))
var.put('nm1', Js([Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('gh'), Js('kh'), Js('kr'), Js('rh'), Js('ph'), Js('pr'), Js('sk'), Js('st'), Js('tr'), Js('vr'), Js('xh'), Js('zh')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('ai'), Js('ea'), Js('ee'), Js('eu'), Js('ei'), Js('ia'), Js('ie'), Js('io')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm4', Js([Js('dc'), Js('dj'), Js('dn'), Js('dr'), Js('dv'), Js('dy'), Js('dz'), Js('fg'), Js('fk'), Js('fr'), Js('ft'), Js('fz'), Js('gg'), Js('gh'), Js('gn'), Js('gr'), Js('gt'), Js('gz'), Js('kh'), Js('kk'), Js('kn'), Js('kr'), Js('ks'), Js('kt'), Js('kz'), Js('ld'), Js('lg'), Js('lk'), Js('ll'), Js('lm'), Js('ln'), Js('lr'), Js('lv'), Js('ly'), Js('mk'), Js('mm'), Js('mr'), Js('mv'), Js('mz'), Js('nc'), Js('nd'), Js('ng'), Js('nk'), Js('nl'), Js('nn'), Js('nr'), Js('nt'), Js('nv'), Js('ny'), Js('nz'), Js('qq'), Js('qr'), Js('qt'), Js('rc'), Js('rg'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rr'), Js('rt'), Js('rv'), Js('rx'), Js('rz'), Js('sc'), Js('sh'), Js('sk'), Js('sl'), Js('sm'), Js('sn'), Js('sp'), Js('sr'), Js('ss'), Js('st'), Js('sy'), Js('th'), Js('tr'), Js('vl'), Js('vr'), Js('zl'), Js('zr'), Js('zz')]))
var.put('nm5', Js([Js('d'), Js('f'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y'), Js('z')]))
var.put('nm6', Js([Js('h'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
homestuckNames = var.to_python()