__all__ = ['lichNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            if (var.get('i')<Js(6.0)):
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            else:
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if ((var.get('rnd2')>Js(50.0)) or (var.get('rnd4')>Js(50.0))):
                    while (var.get('rnd6')>Js(50.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('br'), Js('bz'), Js('c'), Js('ch'), Js('cr'), Js('cz'), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gh'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('kr'), Js('m'), Js('mh'), Js('n'), Js('nh'), Js('p'), Js('pr'), Js('ps'), Js('ph'), Js('q'), Js('qh'), Js('qr'), Js('r'), Js('rh'), Js('s'), Js('sc'), Js('sh'), Js('sk'), Js('sq'), Js('sr'), Js('st'), Js('str'), Js('sz'), Js('t'), Js('th'), Js('tr'), Js('ts'), Js('tz'), Js('v'), Js('vh'), Js('vr'), Js('x'), Js('xh'), Js('z'), Js('zh')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('y'), Js('y'), Js('y'), Js('au'), Js('aa'), Js('ae'), Js('ai'), Js('ea'), Js('ee'), Js('ia'), Js('oo'), Js('ou'), Js('ua')]))
var.put('nm3', Js([Js('b'), Js('br'), Js("b'gh"), Js('bz'), Js('c'), Js('cq'), Js('cr'), Js('ch'), Js('cd'), Js('cn'), Js('cm'), Js('cz'), Js("c'z"), Js("c'n"), Js("c'm"), Js("c'dh"), Js('d'), Js('dd'), Js('dh'), Js('dr'), Js('dz'), Js("d'z"), Js("d'gh"), Js('g'), Js('gg'), Js('gh'), Js('gd'), Js("g'd"), Js('gn'), Js('gm'), Js('gr'), Js("g'sh"), Js('gv'), Js("g'v"), Js('gz'), Js("g'z"), Js('j'), Js('k'), Js('kd'), Js('kh'), Js('kk'), Js('kn'), Js('kr'), Js('kt'), Js('kv'), Js('kz'), Js("k'z"), Js("k'n"), Js("k'm"), Js("k'sh"), Js("k'v"), Js('l'), Js('ld'), Js('lg'), Js('lk'), Js('lq'), Js('lz'), Js('lx'), Js("l'z"), Js("l'x"), Js("l'q"), Js("l'kh"), Js('md'), Js("m'g"), Js("m'gh"), Js('mk'), Js("m'q"), Js('mz'), Js("m'z"), Js('nc'), Js('nd'), Js('ng'), Js("n'g"), Js("n'gh"), Js('nk'), Js('nq'), Js("n'q"), Js('nz'), Js('q'), Js("q'd"), Js("q'g"), Js('qn'), Js("q'r"), Js("q'z"), Js('r'), Js('rr'), Js('rc'), Js('rd'), Js('rg'), Js('rgh'), Js('rk'), Js('rq'), Js('rz'), Js("r'z"), Js("r'g"), Js("r'gh"), Js("r'q"), Js('s'), Js('sz'), Js('sc'), Js('sg'), Js('sk'), Js("s'q"), Js("s'z"), Js('st'), Js("s't"), Js('t'), Js('th'), Js('tr'), Js("t'g"), Js("th'g"), Js("t'z"), Js("t'q"), Js('x'), Js('xh'), Js("x'r"), Js("x'z"), Js('xz'), Js('z'), Js('zz'), Js('zc'), Js('zd'), Js('zg'), Js("z'q"), Js("z'g"), Js("z'dh"), Js('zh')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('n'), Js('q'), Js('r'), Js('gh'), Js('gn'), Js('gr')]))
var.put('nm5', Js([Js(''), Js(''), Js('c'), Js('d'), Js('dh'), Js('g'), Js('k'), Js('l'), Js('n'), Js('q'), Js('r'), Js('s'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
lichNames = var.to_python()