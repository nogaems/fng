__all__ = ['landNames']

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
            if (var.get('i')<Js(2.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('names', ((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('names', ((var.get('nm2').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3'))))
                        else:
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('names', (((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm1').get(var.get('rnd3')))+Js('  '))+var.get('nm3').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('i'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('pr'), Js('str'), Js('tr'), Js('bl'), Js('cl'), Js('fl'), Js('gl'), Js('pl'), Js('sh'), Js('sc'), Js('sk'), Js('sm'), Js('sn'), Js('sp'), Js('st'), Js('sw'), Js('ch'), Js('sh'), Js('th'), Js('wh')]))
var.put('nm4', Js([Js('ae'), Js('ai'), Js('ao'), Js('au'), Js('a'), Js('ay'), Js('ea'), Js('ei'), Js('eo'), Js('eu'), Js('e'), Js('ey'), Js('ua'), Js('ue'), Js('ui'), Js('uo'), Js('u'), Js('uy'), Js('ia'), Js('ie'), Js('iu'), Js('io'), Js('iy'), Js('oa'), Js('oe'), Js('ou'), Js('oi'), Js('o'), Js('oy')]))
var.put('nm5', Js([Js('stan'), Js('dor'), Js('vania'), Js('nia'), Js('lor'), Js('cor'), Js('dal'), Js('bar'), Js('sal'), Js('ra'), Js('la'), Js('lia'), Js('jan'), Js('rus'), Js('ze'), Js('tan'), Js('wana'), Js('sil'), Js('so'), Js('na'), Js('le'), Js('bia'), Js('ca'), Js('ji'), Js('ce'), Js('ton'), Js('ssau'), Js('sau'), Js('sia'), Js('ca'), Js('ya'), Js('ye'), Js('yae'), Js('tho'), Js('stein'), Js('ria'), Js('nia'), Js('burg'), Js('nia'), Js('gro'), Js('que'), Js('gua'), Js('qua'), Js('rhiel'), Js('cia'), Js('les'), Js('dan'), Js('nga'), Js('land')]))
var.put('nm6', Js([Js('ia'), Js('a'), Js('en'), Js('ar'), Js('istan'), Js('aria'), Js('ington'), Js('ua'), Js('ijan'), Js('ain'), Js('ium'), Js('us'), Js('esh'), Js('os'), Js('ana'), Js('il'), Js('ad'), Js('or'), Js('ea'), Js('eau'), Js('ax'), Js('on'), Js('ana'), Js('ary'), Js('ya'), Js('ye'), Js('yae'), Js('ait'), Js('ein'), Js('urg'), Js('al'), Js('ines'), Js('ela')]))
pass
pass


# Add lib to the module scope
landNames = var.to_python()