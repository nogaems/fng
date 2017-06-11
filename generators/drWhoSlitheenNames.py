__all__ = ['drWhoSlitheenNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm18', 'nm14', 'nm17', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
            var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
            var.put('rnd16', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
            var.put('rnd17', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd18', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
            var.put('rnd19', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
            var.put('rnd20', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd21', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
            var.put('rnd22', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
            var.put('rnd23', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
            def PyJs_LONG_1_(var=var):
                def PyJs_LONG_0_(var=var):
                    return ((((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd8')))+var.get('nm8').get(var.get('rnd9')))+Js(' '))+var.get('nm9').get(var.get('rnd10')))
                return ((((((((((((PyJs_LONG_0_()+var.get('nm10').get(var.get('rnd11')))+var.get('nm11').get(var.get('rnd12')))+var.get('nm10').get(var.get('rnd13')))+var.get('nm12').get(var.get('rnd14')))+var.get('nm13').get(var.get('rnd15')))+Js('-'))+var.get('nm14').get(var.get('rnd16')))+var.get('nm10').get(var.get('rnd17')))+var.get('nm15').get(var.get('rnd18')))+Js(' '))+var.get('nm16').get(var.get('rnd19')))+var.get('nm10').get(var.get('rnd20')))
            var.put('names', (((PyJs_LONG_1_()+var.get('nm17').get(var.get('rnd21')))+var.get('nm18').get(var.get('rnd22')))+var.get('nm19').get(var.get('rnd23'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('Bl'), Js('Br'), Js('D'), Js('Dr'), Js('Gr'), Js('G'), Js('Gl'), Js('J'), Js('K'), Js('Kr'), Js('L'), Js('S'), Js('Sr'), Js('Sl'), Js('Tr'), Js('Tl')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('oo'), Js('aa')]))
var.put('nm3', Js([Js('cra'), Js('ckt'), Js('ckto'), Js('f'), Js('ft'), Js('ll'), Js('lm'), Js('ln'), Js('m'), Js('n'), Js('ne'), Js('p'), Js('rm'), Js('rn'), Js('rs'), Js('rst'), Js('st'), Js('s'), Js('ss'), Js('sp'), Js('x'), Js('xa')]))
var.put('nm4', Js([Js('B'), Js('D'), Js('F'), Js('G'), Js('K'), Js('L'), Js('M'), Js('N'), Js('R'), Js('T'), Js('V')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm6', Js([Js('d'), Js('f'), Js('g'), Js('gg'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('ng'), Js('nn'), Js('r'), Js('rr'), Js('rm'), Js('rn'), Js('s'), Js('ss'), Js('x'), Js('ze'), Js('z')]))
var.put('nm7', Js([Js('B'), Js('Bl'), Js('D'), Js('Dr'), Js('F'), Js('Fl'), Js('G'), Js('Gr'), Js('Gl'), Js('Kl'), Js('L'), Js('M'), Js('N'), Js('T')]))
var.put('nm8', Js([Js('bs'), Js('dd'), Js('gg'), Js('gs'), Js('ln'), Js('lm'), Js('ls'), Js('n'), Js('ng'), Js('rn'), Js('rm'), Js('rt'), Js('tch'), Js('sh'), Js('ze')]))
var.put('nm9', Js([Js('B'), Js('D'), Js('G'), Js('H'), Js('K'), Js('L'), Js('M'), Js('N'), Js('P'), Js('R'), Js('S'), Js('Sh')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm11', Js([Js('bb'), Js('bl'), Js('gl'), Js('gr'), Js('gg'), Js('kr'), Js('kl'), Js('kk'), Js('lm'), Js('ln'), Js('lr'), Js('ll'), Js('pp'), Js('pr'), Js('pl'), Js('rr'), Js('rl'), Js('ss'), Js('t'), Js('tl')]))
var.put('nm12', Js([Js('d'), Js('l'), Js('m'), Js('n'), Js('s'), Js('v')]))
var.put('nm13', Js([Js('eer'), Js('en'), Js('een')]))
var.put('nm14', Js([Js('B'), Js('Bl'), Js('D'), Js('G'), Js('Gl'), Js('Gr'), Js('Pl'), Js('P'), Js('Pr'), Js('R'), Js('S'), Js('Sl'), Js('T'), Js('Tr')]))
var.put('nm15', Js([Js('f'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('y')]))
var.put('nm16', Js([Js('B'), Js('Bl'), Js('C'), Js('Ch'), Js('F'), Js('Fl'), Js('Gl'), Js('G'), Js('H'), Js('K'), Js('L'), Js('M'), Js('N'), Js('P'), Js('R'), Js('Sl'), Js('S')]))
var.put('nm17', Js([Js('ck'), Js('dr'), Js('ff'), Js('g'), Js('gr'), Js('kk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('pp'), Js('rl'), Js('st'), Js('str'), Js('tt'), Js('th'), Js('v'), Js('z')]))
var.put('nm18', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('ar'), Js('er'), Js('et'), Js('ez'), Js('at'), Js('az'), Js('oz'), Js('el'), Js('al'), Js('es'), Js('as')]))
var.put('nm19', Js([Js('een'), Js('ene')]))
pass
pass


# Add lib to the module scope
drWhoSlitheenNames = var.to_python()