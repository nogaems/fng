__all__ = ['cityNames']

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
    var.registers(['names4', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7', 'result'])
    var.put('names1', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('names2', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('pr'), Js('qr'), Js('sr'), Js('tr'), Js('vr'), Js('wr'), Js('yr'), Js('zr'), Js('str'), Js('bl'), Js('cl'), Js('fl'), Js('gl'), Js('kl'), Js('pl'), Js('sl'), Js('vl'), Js('yl'), Js('zl'), Js('ch'), Js('kh'), Js('ph'), Js('sh'), Js('yh'), Js('zh')]))
    var.put('names3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ai'), Js('ao'), Js('au'), Js('aa'), Js('ee'), Js('ea'), Js('ei'), Js('eo'), Js('eu'), Js('ia'), Js('ie'), Js('io'), Js('iu'), Js('oa'), Js('oe'), Js('oi'), Js('oo'), Js('ou'), Js('ua'), Js('ue'), Js('ui'), Js('uo'), Js('uu'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
    var.put('names4', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('pr'), Js('tr'), Js('vr'), Js('wr'), Js('zr'), Js('st'), Js('bl'), Js('cl'), Js('fl'), Js('gl'), Js('kl'), Js('pl'), Js('sl'), Js('vl'), Js('zl'), Js('ch'), Js('kh'), Js('ph'), Js('sh'), Js('zh')]))
    var.put('names5', Js([Js('c'), Js('d'), Js('f'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('x'), Js('y'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('names6', Js([Js('aco'), Js('ada'), Js('adena'), Js('ago'), Js('agos'), Js('aka'), Js('ale'), Js('alo'), Js('am'), Js('anbu'), Js('ance'), Js('and'), Js('ando'), Js('ane'), Js('ans'), Js('anta'), Js('arc'), Js('ard'), Js('ares'), Js('ario'), Js('ark'), Js('aso'), Js('athe'), Js('eah'), Js('edo'), Js('ego'), Js('eigh'), Js('eim'), Js('eka'), Js('eles'), Js('eley'), Js('ence'), Js('ens'), Js('ento'), Js('erton'), Js('ery'), Js('esa'), Js('ester'), Js('ey'), Js('ia'), Js('ico'), Js('ido'), Js('ila'), Js('ille'), Js('in'), Js('inas'), Js('ine'), Js('ing'), Js('irie'), Js('ison'), Js('ita'), Js('ock'), Js('odon'), Js('oit'), Js('ok'), Js('olis'), Js('olk'), Js('oln'), Js('ona'), Js('oni'), Js('onio'), Js('ont'), Js('ora'), Js('ord'), Js('ore'), Js('oria'), Js('ork'), Js('osa'), Js('ose'), Js('ouis'), Js('ouver'), Js('ul'), Js('urg'), Js('urgh'), Js('ury')]))
    var.put('names7', Js([Js('bert'), Js('bridge'), Js('burg'), Js('burgh'), Js('burn'), Js('bury'), Js('bus'), Js('by'), Js('caster'), Js('cester'), Js('chester'), Js('dale'), Js('dence'), Js('diff'), Js('ding'), Js('don'), Js('fast'), Js('field'), Js('ford'), Js('gan'), Js('gas'), Js('gate'), Js('gend'), Js('ginia'), Js('gow'), Js('ham'), Js('hull'), Js('land'), Js('las'), Js('ledo'), Js('lens'), Js('ling'), Js('mery'), Js('mond'), Js('mont'), Js('more'), Js('mouth'), Js('nard'), Js('phia'), Js('phis'), Js('polis'), Js('pool'), Js('port'), Js('pus'), Js('ridge'), Js('rith'), Js('ron'), Js('rora'), Js('ross'), Js('rough'), Js('sa'), Js('sall'), Js('sas'), Js('sea'), Js('set'), Js('sey'), Js('shire'), Js('son'), Js('stead'), Js('stin'), Js('ta'), Js('tin'), Js('tol'), Js('ton'), Js('vale'), Js('ver'), Js('ville'), Js('vine'), Js('ving'), Js('well'), Js('wood')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1')))+var.get('names3').get(var.get('rnd2')))+var.get('names5').get(var.get('rnd3')))+var.get('names7').get(var.get('rnd4'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('names', ((((var.get('names3').get(var.get('rnd2'))+var.get('names4').get(var.get('rnd3')))+var.get('names3').get(var.get('rnd4')))+var.get('names5').get(var.get('rnd5')))+var.get('names7').get(var.get('rnd6'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                        var.put('names', ((var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1')))+var.get('names6').get(var.get('rnd2'))))
                    else:
                        var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                        var.put('names', ((((var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1')))+var.get('names3').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd3')))+var.get('names6').get(var.get('rnd4'))))
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
cityNames = var.to_python()