__all__ = ['batarianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                def PyJs_LONG_0_(var=var):
                    return (((((((((((var.get('nm2').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd12')))+Js(' '))+var.get('nm3').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd8')))+var.get('nm6').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd10')))+var.get('nm8').get(var.get('rnd11')))
                var.put('names', PyJs_LONG_0_())
            else:
                def PyJs_LONG_1_(var=var):
                    return (((((((((((var.get('nm2').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+Js(' '))+var.get('nm3').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd8')))+var.get('nm6').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd10')))+var.get('nm8').get(var.get('rnd11')))
                var.put('names', PyJs_LONG_1_())
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('c'), Js('cr'), Js('d'), Js('dh'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('gh'), Js('k'), Js('kh'), Js('kr'), Js('p'), Js('pr'), Js('r'), Js('s')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('a'), Js('o')]))
var.put('nm5', Js([Js('chi'), Js('chia'), Js('cress'), Js('fin'), Js('fine'), Js('kia'), Js('kira'), Js('kis'), Js('lea'), Js('leya'), Js('lile'), Js('lla'), Js('lle'), Js('lya'), Js('men'), Js('mis'), Js('misa'), Js('mye'), Js('neya'), Js('nim'), Js('nin'), Js('nine'), Js('nis'), Js('nith'), Js('nna'), Js('nne'), Js('nya'), Js('phe'), Js('phi'), Js('pril'), Js('pris'), Js('rish'), Js('rith'), Js('sin'), Js('sina'), Js('the'), Js('tia'), Js('tin'), Js('vile'), Js('zis')]))
var.put('nm6', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('k'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s')]))
var.put('nm7', Js([Js("'"), Js('')]))
var.put('nm8', Js([Js('ba'), Js('b'), Js('bar'), Js('can'), Js('char'), Js('dah'), Js('drak'), Js('dor'), Js('gan'), Js('goh'), Js('gar'), Js('han'), Js('hal'), Js('h'), Js('kan'), Js('kk'), Js('lak'), Js('lok'), Js('lor'), Js('mak'), Js('mon'), Js('nak'), Js('nrek'), Js('prak'), Js('pos'), Js('rah'), Js('ral'), Js('rk'), Js('roh'), Js('rok'), Js('ros'), Js('rr'), Js('ss'), Js('star'), Js('th'), Js('tor'), Js('van'), Js('vran'), Js('war'), Js('wen')]))
var.put('nm9', Js([Js('cor'), Js('gan'), Js('gar'), Js('grom'), Js('ko'), Js('kon'), Js('lem'), Js('lo'), Js('m'), Js('mak'), Js('mo'), Js('n'), Js('nk'), Js('no'), Js('po'), Js('por'), Js('prak'), Js('rag'), Js('rak'), Js('rek'), Js('rem'), Js('rk'), Js('rlak'), Js('rn'), Js('rok'), Js('ros'), Js('rvan'), Js('sk'), Js('srak'), Js('svan'), Js('svin'), Js('th'), Js('than'), Js('thar'), Js('thor'), Js('tin'), Js('to'), Js('tok'), Js('tor'), Js('y')]))
pass
pass


# Add lib to the module scope
batarianNames = var.to_python()