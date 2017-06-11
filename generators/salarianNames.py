__all__ = ['salarianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1'])
@Js
def PyJsHoisted_nameGen_(gender, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'gender':gender}, var)
    var.registers(['names7', 'tp', 'result', 'gender'])
    var.put('tp', var.get('gender'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names7', Js([Js('')]))
    else:
        var.put('names7', Js([Js('a'), Js('e'), Js('o'), Js('i')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            while PyJsStrictEq(var.get('rnd5'),Js('')):
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
            var.put('names', (((((((((var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1')))+var.get('names3').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd3')))+var.get('names5').get(var.get('rnd4')))+Js(' '))+var.get('names1').get(var.get('rnd5')))+var.get('names2').get(var.get('rnd6')))+var.get('names6').get(var.get('rnd7')))+var.get('names7').get(var.get('rnd8'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js(''), Js(''), Js(''), Js('')]))
var.put('names2', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('ae')]))
var.put('names3', Js([Js('r'), Js(''), Js('')]))
var.put('names4', Js([Js('b'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('st'), Js('t'), Js('w')]))
var.put('names5', Js([Js('af'), Js('al'), Js('all'), Js('an'), Js('ann'), Js('ant'), Js('ar'), Js('arf'), Js('arp'), Js('art'), Js('arth'), Js('aw'), Js('ern'), Js('ik'), Js('in'), Js('ip'), Js('irn'), Js('ok'), Js('ol'), Js('oln'), Js('on'), Js('op'), Js('orm'), Js('ort'), Js('orth'), Js('ow'), Js('um')]))
var.put('names6', Js([Js('bam'), Js('ban'), Js('ben'), Js('dril'), Js('drok'), Js('he'), Js('ja'), Js('ji'), Js('ks'), Js('lan'), Js('lban'), Js('lben'), Js('lis'), Js('lji'), Js('lon'), Js('lorn'), Js('ls'), Js('lu'), Js('lus'), Js('lzik'), Js('mal'), Js('min'), Js('mnor'), Js('mor'), Js('nik'), Js('nis'), Js('nmorn'), Js('nok'), Js('pon'), Js('raji'), Js('ral'), Js('ralan'), Js('ran'), Js('rban'), Js('rix'), Js('rji'), Js('rlan'), Js('ss'), Js('u'), Js('wan'), Js('x'), Js('yor'), Js('zal'), Js('zen'), Js('zik'), Js('zom'), Js('zon'), Js('zor'), Js('zu'), Js('zz')]))
pass
pass


# Add lib to the module scope
salarianNames = var.to_python()