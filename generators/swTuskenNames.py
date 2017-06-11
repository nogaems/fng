__all__ = ['swTuskenNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm18', 'nm14', 'nm17', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
            if ((var.get('i')%Js(2.0))!=Js(0.0)):
                var.put('namelast', ((var.get('nm16').get(var.get('rnd7'))+var.get('nm17').get(var.get('rnd8')))+var.get('nm19').get(var.get('rnd10'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                var.put('namelast', ((((var.get('nm16').get(var.get('rnd7'))+var.get('nm17').get(var.get('rnd8')))+var.get('nm18').get(var.get('rnd11')))+var.get('nm17').get(var.get('rnd9')))+var.get('nm19').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm15').get(var.get('rnd4')))+Js(' '))+var.get('namelast')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('names', (((((var.get('nm12').get(var.get('rnd2'))+var.get('nm13').get(var.get('rnd3')))+var.get('nm14').get(var.get('rnd')))+var.get('nm13').get(var.get('rnd4')))+Js(' '))+var.get('namelast')))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    if (var.get('i')<Js(8.0)):
                        var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+Js("'"))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4'))))
                    else:
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('names', (((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+Js("'"))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+Js("'"))+var.get('nm10').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js("A'"), Js("Ch'"), Js("Gr'"), Js("H'"), Js("K'"), Js("Q'"), Js("R'"), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('B'), Js('C'), Js('Ch'), Js('D'), Js('G'), Js('K'), Js('Q'), Js('R'), Js('S'), Js('Sh'), Js('Sl'), Js('T'), Js('Th'), Js('Y'), Js('V'), Js('Z')]))
var.put('nm3', Js([Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('u'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('aa'), Js('ai'), Js('ee')]))
var.put('nm4', Js([Js('c'), Js('cr'), Js('g'), Js('gg'), Js('gd'), Js('gr'), Js('hr'), Js('hv'), Js('hm'), Js('k'), Js('kh'), Js('kd'), Js('kr'), Js('kv'), Js('km'), Js('kn'), Js('lm'), Js('lr'), Js('lh'), Js('lg'), Js('m'), Js('mr'), Js('mn'), Js('mg'), Js('md'), Js('mv'), Js('n'), Js('nn'), Js('nr'), Js('nv'), Js('q'), Js('qq'), Js('qh'), Js('r'), Js('rr'), Js('rt'), Js('rd'), Js('t'), Js('v'), Js('z'), Js('zh'), Js('zr'), Js('zd')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('g'), Js('gg'), Js('k'), Js('n'), Js('q'), Js('r'), Js('r'), Js('rk')]))
var.put('nm6', Js([Js('Gk'), Js('Gr'), Js('Gu'), Js('Gg'), Js('Kr'), Js('Kk'), Js('Ku'), Js('Kg'), Js('Or'), Js('Ok'), Js('Og'), Js('Rr'), Js('Rg'), Js('Rk'), Js('Ro'), Js('Ru'), Js('Ur'), Js('Ur'), Js('Ur')]))
var.put('nm7', Js([Js('k'), Js('h'), Js('r'), Js('g'), Js('rh'), Js('ur'), Js('or'), Js('orur'), Js('rrur'), Js('rror'), Js('rurr'), Js('orr'), Js('urr'), Js('rorr'), Js('rurr'), Js('orrur'), Js('ror'), Js('rur'), Js('urur')]))
var.put('nm8', Js([Js('or'), Js('ok'), Js('ro'), Js('ot'), Js('uk'), Js('rk'), Js('kr'), Js('kk'), Js('oa'), Js('ur'), Js('r'), Js('tl'), Js('ru')]))
var.put('nm9', Js([Js('r'), Js('rs'), Js('ruur'), Js('ur'), Js('rur'), Js('urr'), Js('rr'), Js('rt'), Js('urs'), Js('rurs'), Js('ruk')]))
var.put('nm10', Js([Js('ak'), Js('ar'), Js('rr'), Js('r'), Js('kt'), Js('rt'), Js('ku'), Js('ra'), Js('ro'), Js('ru')]))
var.put('nm11', Js([Js('k'), Js('r'), Js('hr'), Js('ur'), Js('t'), Js('ht'), Js('or'), Js('ar'), Js('ut'), Js('uk')]))
var.put('nm12', Js([Js('Ch'), Js('G'), Js('H'), Js('Kh'), Js('L'), Js('Q'), Js('R'), Js('Rh'), Js('Sh'), Js('T'), Js('Th'), Js('V'), Js('Y'), Js('Z')]))
var.put('nm13', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('e'), Js('e'), Js('e'), Js('ee'), Js('aa'), Js('ie'), Js('ei')]))
var.put('nm14', Js([Js('d'), Js('g'), Js('k'), Js('kk'), Js('kh'), Js('kt'), Js('kz'), Js('q'), Js('qt'), Js('qr'), Js('qz'), Js('rt'), Js('r'), Js('rr'), Js('rh'), Js('rt'), Js('x'), Js('xt'), Js('xr'), Js('z'), Js('zt'), Js('zr')]))
var.put('nm15', Js([Js('c'), Js('g'), Js('gh'), Js('k'), Js('n'), Js('m'), Js('rn'), Js('rm'), Js('rr'), Js('rg'), Js('rc'), Js('rh'), Js('rk')]))
var.put('nm16', Js([Js('cr'), Js('br'), Js('b'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('kr'), Js('l'), Js('q'), Js('qr'), Js('r'), Js('rh'), Js('s'), Js('sr'), Js('sh'), Js('t'), Js('tr'), Js('th'), Js('y'), Js('v'), Js('z'), Js('zr')]))
var.put('nm17', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o')]))
var.put('nm18', Js([Js('c'), Js('cr'), Js('g'), Js('gg'), Js('gd'), Js('gr'), Js('k'), Js('kh'), Js('kd'), Js('kr'), Js('kv'), Js('km'), Js('kn'), Js('n'), Js('nn'), Js('nr'), Js('nv'), Js('q'), Js('qq'), Js('qh'), Js('r'), Js('rr'), Js('rt'), Js('rd'), Js('t'), Js('v'), Js('z'), Js('zh'), Js('zr'), Js('zd')]))
var.put('nm19', Js([Js('c'), Js('ct'), Js('g'), Js('gg'), Js('k'), Js('kt'), Js('n'), Js('q'), Js('qt'), Js('r'), Js('rr'), Js('rk'), Js('rc'), Js('rg'), Js('rq'), Js('rt'), Js('rd'), Js('tt'), Js('t')]))
pass
pass


# Add lib to the module scope
swTuskenNames = var.to_python()