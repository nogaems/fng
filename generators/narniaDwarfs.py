__all__ = ['narniaDwarfs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                var.put('names', (((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4'))))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                if (var.get('rnd3')<Js(9.0)):
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js('e')))
                else:
                    var.put('lng', ((var.get('Math').callprop('random')*Js(2.0))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    if PyJsStrictEq(var.get('lng'),Js(0.0)):
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('br'), Js('cr'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('p'), Js('r'), Js('th'), Js('tr'), Js('thr')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('e'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('bl'), Js('bbl'), Js('ckl'), Js('dl'), Js('ddl'), Js('ffl'), Js('fl'), Js('gl'), Js('ggl'), Js('d'), Js('g'), Js('gg'), Js('k'), Js('l'), Js('ll'), Js('n'), Js('v'), Js('z'), Js('sn'), Js('gn'), Js('gd'), None, Js('d'), Js('g'), Js('gg'), Js('k'), Js('l'), Js('ll'), Js('n'), Js('v'), Js('z'), Js('sn'), Js('gn'), Js('gd'), Js('d'), Js('g'), Js('gg'), Js('k'), Js('l'), Js('ll'), Js('n'), Js('v'), Js('z'), Js('sn'), Js('gn'), Js('gd'), Js('dsh'), Js('lnd'), Js('lng'), Js('mdr'), Js('mgl'), Js('mpk'), Js('ndr'), Js('ngd'), Js('ngb'), Js('nkr'), Js('rgl'), Js('rnb'), Js('sdr'), Js('sgl')]))
var.put('nm4', Js([Js('br'), Js('bl'), Js('dr'), Js('dn'), Js('fn'), Js('fd'), Js('fl'), Js('ld'), Js('ln'), Js('lm'), Js('mb'), Js('md'), Js('ml'), Js('nl'), Js('nd'), Js('rb'), Js('rl'), Js('rbr'), Js('th')]))
var.put('nm5', Js([Js('d'), Js('g'), Js('k'), Js('lk'), Js('ld'), Js('n'), Js('nk'), Js('nks'), Js('t')]))
var.put('nm6', Js([Js('b'), Js('cl'), Js('d'), Js('f'), Js('fl'), Js('g'), Js('gl'), Js('m'), Js('n'), Js('w')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o')]))
var.put('nm8', Js([Js('bb'), Js('bl'), Js('ch'), Js('fl'), Js('fs'), Js('fn'), Js('fm'), Js('gs'), Js('ks'), Js('ln'), Js('ls'), Js('lp'), Js('ms'), Js('mn'), Js('nl'), Js('nt'), Js('ns'), Js('nf'), Js('pf'), Js('ps'), Js('sl'), Js('sn'), Js('sm')]))
var.put('nm9', Js([Js('ie'), Js('ey'), Js('ee'), Js('i'), Js('e'), Js('iy')]))
pass
pass


# Add lib to the module scope
narniaDwarfs = var.to_python()