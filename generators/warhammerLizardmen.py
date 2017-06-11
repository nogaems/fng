__all__ = ['warhammerLizardmen']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm', 'nm3', 'nm2'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(3.0)):
                if (var.get('rnd')<Js(5.0)):
                    while (var.get('rnd5')<Js(3.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('-'))+var.get('nm').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('names', ((((((((var.get('nm').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd5')))+Js('-'))+var.get('nm').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd8'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm', Js([Js('c'), Js('cr'), Js('ch'), Js('g'), Js('h'), Js('kr'), Js('m'), Js('n'), Js('q'), Js('qr'), Js('t'), Js('tl'), Js('x'), Js('xlt'), Js('y'), Js('z')]))
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('cr'), Js('ch'), Js('g'), Js('h'), Js('kr'), Js('m'), Js('n'), Js('q'), Js('qr'), Js('t'), Js('tl'), Js('x'), Js('xlt'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('oa'), Js('aui'), Js("a'u"), Js("o'e"), Js("o'a"), Js("u'a"), Js("a'e"), Js("e'a")]))
var.put('nm3', Js([Js('c'), Js('cc'), Js('ch'), Js('cht'), Js('chtl'), Js('cn'), Js('ct'), Js('ctl'), Js('d'), Js('h'), Js('hc'), Js('hg'), Js('hp'), Js('ht'), Js('htl'), Js('htz'), Js('k'), Js('kt'), Js('l'), Js('lch'), Js('lh'), Js('ll'), Js('lm'), Js('ln'), Js('lp'), Js('lt'), Js('lx'), Js('m'), Js('n'), Js('nd'), Js('nh'), Js('nq'), Js('nt'), Js('ntl'), Js('p'), Js('q'), Js('r'), Js('szc'), Js('t'), Js('tl'), Js('tt'), Js('tz'), Js('tzc'), Js('tzp'), Js('tzt'), Js('x'), Js('xc'), Js('xch'), Js('xt'), Js('xtl'), Js('xy'), Js('y'), Js('z'), Js('zc'), Js('zd'), Js('zq'), Js('ztl')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('cl'), Js('k'), Js('l'), Js('n'), Js('p'), Js('r'), Js('tl'), Js('x')]))
var.put('nm5', Js([Js('c'), Js('ch'), Js('cl'), Js('k'), Js('l'), Js('n'), Js('p'), Js('r'), Js('tl'), Js('x')]))
pass
pass


# Add lib to the module scope
warhammerLizardmen = var.to_python()