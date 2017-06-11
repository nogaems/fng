__all__ = ['nagaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(2.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((var.get('nm6').get(var.get('rnd2'))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(7.0)):
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4'))))
                else:
                    if (var.get('i')<Js(9.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd4'))))
                    else:
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd8')))+var.get('nm4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('d'), Js('dh'), Js('dhr'), Js('h'), Js('hr'), Js('j'), Js('jy'), Js('k'), Js('kh'), Js('kr'), Js('ksh'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('s'), Js('sr'), Js('t'), Js('v'), Js('vr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('a'), Js('a'), Js('a'), Js('i'), Js('i')]))
var.put('nm3', Js([Js('bh'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y'), Js('bh'), Js('d'), Js('dg'), Js('dh'), Js('dhy'), Js('dm'), Js('dr'), Js('g'), Js('h'), Js('hl'), Js('hy'), Js('j'), Js('k'), Js('kh'), Js('ksh'), Js('ky'), Js('l'), Js('lm'), Js('lw'), Js('m'), Js('mkh'), Js('mv'), Js('mvr'), Js('n'), Js('nd'), Js('ndh'), Js('ng'), Js('nj'), Js('nkh'), Js('nm'), Js('nshtr'), Js('nt'), Js('nth'), Js('p'), Js('pt'), Js('r'), Js('rd'), Js('rk'), Js('rm'), Js('rn'), Js('rt'), Js('ry'), Js('s'), Js('sh'), Js('shk'), Js('shm'), Js('shn'), Js('shp'), Js('shth'), Js('shtr'), Js('sr'), Js('st'), Js('sth'), Js('sw'), Js('t'), Js('th'), Js('tr'), Js('tt'), Js('ttr'), Js('ty'), Js('v'), Js('vy'), Js('y'), Js('yl')]))
var.put('nm4', Js([Js('a'), Js('a'), Js('a'), Js('a'), Js('a'), Js('a'), Js('a'), Js('a'), Js('a'), Js('i'), Js('u'), Js('as'), Js('at')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('cr'), Js('ch'), Js('d'), Js('h'), Js('k'), Js('kr'), Js('kh'), Js('l'), Js('r'), Js('s'), Js('s'), Js('s'), Js('sh'), Js('sz'), Js('sc'), Js('sy'), Js('sz'), Js('sh'), Js('t'), Js('th'), Js('x'), Js('y'), Js('z'), Js('zs'), Js('zh')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('aa'), Js('ai'), Js('ee'), Js('ei'), Js('ie')]))
var.put('nm7', Js([Js('c'), Js('d'), Js('dh'), Js('k'), Js('kh'), Js('l'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('x'), Js('xh'), Js('z'), Js('zh'), Js('c'), Js('d'), Js('k'), Js('l'), Js('r'), Js('s'), Js('t'), Js('x'), Js('z'), Js('c'), Js('d'), Js('k'), Js('l'), Js('r'), Js('s'), Js('t'), Js('x'), Js('z'), Js('s'), Js('s'), Js('sh'), Js('sh'), Js('cc'), Js('ch'), Js('ck'), Js('cs'), Js('csh'), Js('cz'), Js('dh'), Js('dj'), Js('kk'), Js('kh'), Js('ks'), Js('ksh'), Js('kz'), Js('ll'), Js('lh'), Js('lz'), Js('ls'), Js('rr'), Js('rc'), Js('rg'), Js('rh'), Js('rj'), Js('rs'), Js('rsh'), Js('rz'), Js('rsz'), Js('rt'), Js('rth'), Js('rc'), Js('rk'), Js('ss'), Js('sc'), Js('sh'), Js('sk'), Js('sz'), Js('sy'), Js('th'), Js('tr'), Js('ts'), Js('tz'), Js('tsh'), Js('xh'), Js('xs'), Js('xz'), Js('zh'), Js('zs'), Js('zz'), Js('zs')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('kh'), Js('l'), Js('r'), Js('s'), Js('sj'), Js('ss'), Js('sh'), Js('sz'), Js('t'), Js('th'), Js('x'), Js('z'), Js('zs')]))
pass
pass


# Add lib to the module scope
nagaNames = var.to_python()