__all__ = ['kingdomNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('names', (((((var.get('names1').get(var.get('rnd'))+var.get('names3').get(var.get('rnd2')))+var.get('names2').get(var.get('rnd3')))+var.get('names5').get(var.get('rnd4')))+Js(' '))+var.get('names6').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                if (var.get('rnd')<Js(5.0)):
                    while (var.get('rnd3')<Js(6.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                if (var.get('rnd3')<Js(6.0)):
                    while (var.get('rnd5')<Js(6.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('names', (((((((var.get('names1').get(var.get('rnd'))+var.get('names3').get(var.get('rnd2')))+var.get('names2').get(var.get('rnd3')))+var.get('names4').get(var.get('rnd4')))+var.get('names2').get(var.get('rnd5')))+var.get('names5').get(var.get('rnd6')))+Js(' '))+var.get('names6').get(var.get('rnd7'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('ae'), Js('ea'), Js('ai'), Js('au'), Js('ou'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names2', Js([Js('ae'), Js('eo'), Js('ea'), Js('ai'), Js('ui'), Js('ou'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('names3', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('pr'), Js('tr'), Js('vr'), Js('wr'), Js('st'), Js('sl'), Js('ch'), Js('sh'), Js('ph'), Js('kh'), Js('th')]))
var.put('names4', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('bb'), Js('cc'), Js('dd'), Js('ff'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt'), Js('zz'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('pr'), Js('sr'), Js('tr'), Js('zr'), Js('st'), Js('sl'), Js('ch'), Js('sh'), Js('ph'), Js('kh'), Js('th')]))
var.put('names5', Js([Js('ba'), Js('bet'), Js('bia'), Js('borg'), Js('burg'), Js('ca'), Js('caea'), Js('can'), Js('cia'), Js('curia'), Js('dal'), Js('del'), Js('dia'), Js('dian'), Js('do'), Js('dor'), Js('dora'), Js('dour'), Js('galla'), Js('gary'), Js('gia'), Js('gon'), Js('han'), Js('kar'), Js('kha'), Js('kya'), Js('les'), Js('lia'), Js('lon'), Js('lan'), Js('lum'), Js('lux'), Js('lyra'), Js('mid'), Js('mor'), Js('more'), Js('nad'), Js('nait'), Js('nao'), Js('nate'), Js('nada'), Js('neian'), Js('nem'), Js('nia'), Js('nid'), Js('niel'), Js('ning'), Js('ntis'), Js('nyth'), Js('pan'), Js('phate'), Js('pia'), Js('pis'), Js('ra'), Js('ral'), Js('rean'), Js('rene'), Js('renth'), Js('ria'), Js('rian'), Js('rid'), Js('rin'), Js('ris'), Js('rith'), Js('rus'), Js('ryn'), Js('sal'), Js('san'), Js('sea'), Js('seon'), Js('sha'), Js('sian'), Js('site'), Js('sta'), Js('ston'), Js('teron'), Js('terra'), Js('tha'), Js('thage'), Js('then'), Js('thia'), Js('tia'), Js('tis'), Js('tish'), Js('ton'), Js('topia'), Js('tor'), Js('tus'), Js('valon'), Js('varia'), Js('vell'), Js('ven'), Js('via'), Js('viel'), Js('wen'), Js('weth'), Js('wyth'), Js('ya'), Js('zar'), Js('zia')]))
var.put('names6', Js([Js('Kingdom'), Js('Empire'), Js('Dynasty')]))
pass
pass


# Add lib to the module scope
kingdomNames = var.to_python()