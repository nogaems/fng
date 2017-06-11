__all__ = ['pathfinderOread']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', (((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('g'), Js('j'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('y')]))
var.put('nm3', Js([Js('d'), Js('dd'), Js('f'), Js('fd'), Js('ft'), Js('hd'), Js('hn'), Js('hv'), Js('l'), Js('ll'), Js('ln'), Js('lm'), Js('ld'), Js('lv'), Js('lt'), Js('lth'), Js('lm'), Js('m'), Js('md'), Js('mt'), Js('mh'), Js('mv'), Js('n'), Js('nd'), Js('nt'), Js('nv'), Js('nh'), Js('nn'), Js('nm'), Js('nh'), Js('nr'), Js('r'), Js('rt'), Js('rh'), Js('rn'), Js('rm'), Js('rl'), Js('rv'), Js('rr'), Js('rd'), Js('th'), Js('tr'), Js('thr'), Js('v'), Js('vh'), Js('vr')]))
var.put('nm4', Js([Js(''), Js('m'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('d'), Js('dh'), Js('gh'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('w')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('e')]))
var.put('nm7', Js([Js('c'), Js('ch'), Js('d'), Js('dh'), Js('f'), Js('ff'), Js('fh'), Js('fth'), Js('h'), Js('hn'), Js('hv'), Js('hl'), Js('hs'), Js('l'), Js('lh'), Js('ln'), Js('lm'), Js('ls'), Js('lsh'), Js('m'), Js('mn'), Js('mm'), Js('mh'), Js('my'), Js('n'), Js('nn'), Js('nh'), Js('ny'), Js('ns'), Js('nth'), Js('nf'), Js('r'), Js('ry'), Js('rh'), Js('rs'), Js('rsh'), Js('rth'), Js('s'), Js('sh'), Js('sth'), Js('sht'), Js('sn'), Js('sm'), Js('sy'), Js('sl'), Js('t'), Js('th'), Js('ty'), Js('thy'), Js('y')]))
pass
pass


# Add lib to the module scope
pathfinderOread = var.to_python()