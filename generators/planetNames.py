__all__ = ['planetNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                            var.put('names', ((((var.get('nm3').get(var.get('rnd3'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                        else:
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('names', ((((((var.get('nm3').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+Js(' '))+var.get('nm7').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('i'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('pr'), Js('str'), Js('tr'), Js('bl'), Js('cl'), Js('fl'), Js('gl'), Js('pl'), Js('sl'), Js('sc'), Js('sk'), Js('sm'), Js('sn'), Js('sp'), Js('st'), Js('sw'), Js('ch'), Js('sh'), Js('th'), Js('wh')]))
var.put('nm4', Js([Js('ae'), Js('ai'), Js('ao'), Js('au'), Js('a'), Js('ay'), Js('ea'), Js('ei'), Js('eo'), Js('eu'), Js('e'), Js('ey'), Js('ua'), Js('ue'), Js('ui'), Js('uo'), Js('u'), Js('uy'), Js('ia'), Js('ie'), Js('iu'), Js('io'), Js('iy'), Js('oa'), Js('oe'), Js('ou'), Js('oi'), Js('o'), Js('oy')]))
var.put('nm5', Js([Js('turn'), Js('ter'), Js('nus'), Js('rus'), Js('tania'), Js('hiri'), Js('hines'), Js('gawa'), Js('nides'), Js('carro'), Js('rilia'), Js('stea'), Js('lia'), Js('lea'), Js('ria'), Js('nov'), Js('phus'), Js('mia'), Js('nerth'), Js('wei'), Js('ruta'), Js('tov'), Js('zuno'), Js('vis'), Js('lara'), Js('nia'), Js('liv'), Js('tera'), Js('gantu'), Js('yama'), Js('tune'), Js('ter'), Js('nus'), Js('cury'), Js('bos'), Js('pra'), Js('thea'), Js('nope'), Js('tis'), Js('clite')]))
var.put('nm6', Js([Js('una'), Js('ion'), Js('iea'), Js('iri'), Js('illes'), Js('ides'), Js('agua'), Js('olla'), Js('inda'), Js('eshan'), Js('oria'), Js('ilia'), Js('erth'), Js('arth'), Js('orth'), Js('oth'), Js('illon'), Js('ichi'), Js('ov'), Js('arvis'), Js('ara'), Js('ars'), Js('yke'), Js('yria'), Js('onoe'), Js('ippe'), Js('osie'), Js('one'), Js('ore'), Js('ade'), Js('adus'), Js('urn'), Js('ypso'), Js('ora'), Js('iuq'), Js('orix'), Js('apus'), Js('ion'), Js('eon'), Js('eron'), Js('ao'), Js('omia')]))
var.put('nm7', Js([Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('U'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z'), Js('0'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9'), Js('0'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
planetNames = var.to_python()