__all__ = ['languageNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('name', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('name', ((var.get('nm2').get(var.get('rnd2'))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        if (var.get('rnd2')>Js(19.0)):
                            while (var.get('rnd4')>Js(19.0)):
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        if (var.get('rnd3')>Js(80.0)):
                            while (var.get('rnd5')>Js(80.0)):
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('name', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6'))))
                    else:
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        if (var.get('rnd2')>Js(19.0)):
                            while (var.get('rnd4')>Js(19.0)):
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        if (var.get('rnd3')>Js(80.0)):
                            while (var.get('rnd5')>Js(80.0)):
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('name', ((((var.get('nm2').get(var.get('rnd2'))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('bh'), Js('bl'), Js('br'), Js('ch'), Js('cl'), Js('cr'), Js('cy'), Js('dh'), Js('dr'), Js('fh'), Js('fl'), Js('fr'), Js('gh'), Js('gn'), Js('gl'), Js('gr'), Js('kh'), Js('kl'), Js('kn'), Js('kr'), Js('mh'), Js('my'), Js('nh'), Js('ph'), Js('pl'), Js('pr'), Js('pn'), Js('rh'), Js('sc'), Js('sh'), Js('sl'), Js('sm'), Js('sn'), Js('sp'), Js('sr'), Js('st'), Js('str'), Js('th'), Js('tr'), Js('ty'), Js('vh'), Js('wh'), Js('zh')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('ae'), Js('ao'), Js('ai'), Js('au'), Js('ea'), Js('eo'), Js('ei'), Js('eu'), Js('oa'), Js('oe'), Js('oi'), Js('ou'), Js('ia'), Js('ie'), Js('io'), Js('iu'), Js('ua'), Js('ue'), Js('uo'), Js('ui'), Js('aa'), Js('ee'), Js('oo'), Js('uu')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('bb'), Js('cc'), Js('dd'), Js('ff'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt'), Js('ww'), Js('zz'), Js('cb'), Js('lb'), Js('nb'), Js('bd'), Js('zb'), Js('cd'), Js('gd'), Js('ld'), Js('md'), Js('nd'), Js('sd'), Js('rd'), Js('zd'), Js('lf'), Js('mf'), Js('nf'), Js('sf'), Js('tf'), Js('lg'), Js('mg'), Js('ng'), Js('rg'), Js('sg'), Js('zg'), Js('yg'), Js('ck'), Js('lk'), Js('mk'), Js('str'), Js('nk'), Js('sk'), Js('tk'), Js('zk'), Js('fl'), Js('gl'), Js('kl'), Js('pl'), Js('sl'), Js('tl'), Js('dm'), Js('fm'), Js('gm'), Js('km'), Js('lm'), Js('nm'), Js('sm'), Js('tm'), Js('xm'), Js('zm'), Js('yn'), Js('dn'), Js('fn'), Js('gn'), Js('kn'), Js('mn'), Js('pn'), Js('sn'), Js('tn'), Js('xn'), Js('zn'), Js('np'), Js('sp'), Js('tp'), Js('xp'), Js('fr'), Js('gr'), Js('kr'), Js('pr'), Js('tr'), Js('gs'), Js('ks'), Js('ls'), Js('ms'), Js('ns'), Js('ps'), Js('ts'), Js('xs'), Js('ct'), Js('kt'), Js('lt'), Js('mt'), Js('nt'), Js('pt'), Js('rt'), Js('st'), Js('xt'), Js('yt')]))
var.put('nm4', Js([Js('abi'), Js('ada'), Js('ali'), Js('an'), Js('esh'), Js('ash'), Js('ani'), Js('ano'), Js('arhi'), Js('ari'), Js('aric'), Js('arin'), Js('asy'), Js('athi'), Js('ati'), Js('ean'), Js('ekhi'), Js('eno'), Js('eesh'), Js('ese'), Js('esh'), Js('ethi'), Js('eti'), Js('ian'), Js('ic'), Js('ili'), Js('in'), Js('ina'), Js('ish'), Js('iya'), Js('oshi'), Js('oni'), Js('osa'), Js('uin'), Js('un'), Js('uni'), Js('uri')]))
pass
pass


# Add lib to the module scope
languageNames = var.to_python()