__all__ = ['legendaryCreatures']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['result', 'type'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd7b', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd8', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                var.put('rnd9', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                if (var.get('i')<Js(3.0)):
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd8')))+var.get('nm7').get(var.get('rnd7b')))+var.get('nm9').get(var.get('rnd9'))))
                else:
                    var.put('nmRep', ((var.get('Math').callprop('random')*var.get('nm1').get(var.get('rnd')).get('length'))|Js(0.0)))
                    def PyJs_LONG_0_(var=var):
                        return ((((PyJsStrictEq(var.get('nm1').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('a')) or PyJsStrictEq(var.get('nm1').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('e'))) or PyJsStrictEq(var.get('nm1').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('i'))) or PyJsStrictEq(var.get('nm1').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('o'))) or PyJsStrictEq(var.get('nm1').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('u')))
                    if (PyJs_LONG_0_() or PyJsStrictEq(var.get('nm1').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('y'))):
                        var.put('nmRepl', var.get('nm3').get(((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0))))
                    else:
                        var.put('nmRepl', var.get('nm4').get(((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0))))
                    var.put('nmR', ((var.get('nm1').get(var.get('rnd')).callprop('substr', Js(0.0), var.get('nmRep'))+var.get('nmRepl'))+var.get('nm1').get(var.get('rnd')).callprop('substr', (var.get('nmRep')+Js(1.0)))))
                    var.put('names', (((var.get('nmR')+var.get('nm8').get(var.get('rnd8')))+var.get('nm7').get(var.get('rnd7b')))+var.get('nm9').get(var.get('rnd9'))))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                if (var.get('i')<Js(8.0)):
                    var.put('names', ((var.get('nm6').get(var.get('rnd6'))+var.get('nm7').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd'))))
                else:
                    var.put('nmRep', ((var.get('Math').callprop('random')*var.get('nm2').get(var.get('rnd')).get('length'))|Js(0.0)))
                    def PyJs_LONG_1_(var=var):
                        return ((((PyJsStrictEq(var.get('nm2').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('a')) or PyJsStrictEq(var.get('nm2').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('e'))) or PyJsStrictEq(var.get('nm2').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('i'))) or PyJsStrictEq(var.get('nm2').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('o'))) or PyJsStrictEq(var.get('nm2').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('u')))
                    if (PyJs_LONG_1_() or PyJsStrictEq(var.get('nm2').get(var.get('rnd')).callprop('charAt', var.get('nmRep')),Js('y'))):
                        var.put('nmRepl', var.get('nm3').get(((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0))))
                    else:
                        var.put('nmRepl', var.get('nm4').get(((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0))))
                    var.put('nmR', ((var.get('nm2').get(var.get('rnd')).callprop('substr', Js(0.0), var.get('nmRep'))+var.get('nmRepl'))+var.get('nm1').get(var.get('rnd')).callprop('substr', (var.get('nmRep')+Js(1.0)))))
                    var.put('names', ((var.get('nm6').get(var.get('rnd6'))+var.get('nm7').get(var.get('rnd7')))+var.get('nmR')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aklo'), Js('Alec'), Js('Ama'), Js('Anu'), Js('Ara'), Js('Arach'), Js('Ase'), Js('Asu'), Js('Ban'), Js('Basi'), Js('Behe'), Js('Bi'), Js('Bun'), Js('Ca'), Js('Cal'), Js('Cala'), Js('Chi'), Js('Chu'), Js('Cro'), Js('Cy'), Js('Dha'), Js('Dham'), Js('Dra'), Js('Du'), Js('Dulla'), Js('Gol'), Js('Gor'), Js('Gri'), Js('Grif'), Js('Hai'), Js('Har'), Js('Hell'), Js('Hi'), Js('Hiba'), Js('Hy'), Js('Incu'), Js('Ja'), Js('Jac'), Js('Jacka'), Js('Kel'), Js('La'), Js('Lam'), Js('Lama'), Js('Lin'), Js('Man'), Js('Manti'), Js('Me'), Js('Medu'), Js('Melu'), Js('Mi'), Js('Mino'), Js('Ouro'), Js('Pa'), Js('Pabi'), Js('Pabil'), Js('Pe'), Js('Pega'), Js('Pery'), Js('Phoe'), Js('Sa'), Js('Sel'), Js('Si'), Js('Sil'), Js('Sile'), Js('Su'), Js('Succu'), Js('Tara'), Js('Taras'), Js('Un'), Js('Uni'), Js('Va'), Js('Vam'), Js('Vana'), Js('Wol'), Js('Wolper'), Js('Wy'), Js('Ye'), Js('Zla'), Js('Zlato')]))
var.put('nm2', Js([Js('berus'), Js('bis'), Js('boros'), Js('bra'), Js('bus'), Js('cabra'), Js('camp'), Js('clops'), Js('core'), Js('corn'), Js('cotta'), Js('dine'), Js('dorm'), Js('dra'), Js('drius'), Js('dusa'), Js('fin'), Js('ger'), Js('gon'), Js('griff'), Js('han'), Js('horn'), Js('ket'), Js('kie'), Js('leni'), Js('lenus'), Js('lez'), Js('lisk'), Js('lope'), Js('lops'), Js('mera'), Js('moth'), Js('nara'), Js('ne'), Js('ni'), Js('nix'), Js('nost'), Js('nus'), Js('pad'), Js('pie'), Js('pir'), Js('pire'), Js('py'), Js('que'), Js('quix'), Js('ren'), Js('rion'), Js('rog'), Js('rok'), Js('ron'), Js('ros'), Js('sag'), Js('sena'), Js('shee'), Js('sine'), Js('ssu'), Js('su'), Js('sura'), Js('sus'), Js('taur'), Js('tinger'), Js('ton'), Js('torog'), Js('trice'), Js('tryon'), Js('tyr'), Js('vern'), Js('yip'), Js('zum')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('y'), Js('z')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('br'), Js('ch'), Js('cr'), Js('dh'), Js('dr'), Js('fr'), Js('gn'), Js('gr'), Js('kn'), Js('kr'), Js('kh'), Js('ph'), Js('sc'), Js('sh'), Js('sk'), Js('st'), Js('str'), Js('th'), Js('tr'), Js('vr'), Js('wr')]))
var.put('nm7', Js([Js('a'), Js('a'), Js('a'), Js('a'), Js('aa'), Js('ai'), Js('ao'), Js('au'), Js('e'), Js('e'), Js('e'), Js('e'), Js('ea'), Js('ee'), Js('ei'), Js('eo'), Js('i'), Js('i'), Js('i'), Js('i'), Js('ia'), Js('ie'), Js('io'), Js('o'), Js('o'), Js('o'), Js('o'), Js('oa'), Js('oo'), Js('ou'), Js('u'), Js('u'), Js('u'), Js('ua'), Js('ue')]))
var.put('nm8', Js([Js('b'), Js('br'), Js('c'), Js('cc'), Js('ch'), Js('chn'), Js('cl'), Js('d'), Js('dr'), Js('ff'), Js('g'), Js('h'), Js('kl'), Js('l'), Js('lk'), Js('ll'), Js('lp'), Js('ls'), Js('m'), Js('mp'), Js('n'), Js('nd'), Js('ng'), Js('nsh'), Js('nt'), Js('p'), Js('pp'), Js('q'), Js('r'), Js('rb'), Js('rg'), Js('rp'), Js('s'), Js('sh'), Js('sq'), Js('ss'), Js('t'), Js('tr'), Js('tt'), Js('v'), Js('y'), Js('z')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('ff'), Js('g'), Js('k'), Js('m'), Js('mp'), Js('n'), Js('nd'), Js('nx'), Js('p'), Js('ps'), Js('r'), Js('rm'), Js('rn'), Js('s'), Js('sk'), Js('st'), Js('t'), Js('th'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
legendaryCreatures = var.to_python()