__all__ = ['zabrakNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('A'), Js('O'), Js('E'), Js('U'), Js('B'), Js('Br'), Js('Bl'), Js('D'), Js('Dr'), Js('G'), Js('Gr'), Js('H'), Js('K'), Js('Kr'), Js('Kl'), Js('M'), Js('N'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('St'), Js('T'), Js('V'), Js('Vr'), Js('X')]))
var.put('nm2', Js([Js('a'), Js('o'), Js('u'), Js('e')]))
var.put('nm3', Js([Js('ra'), Js('ro'), Js('ru'), Js('rga'), Js('rgo'), Js('rgu'), Js('rge'), Js('ba'), Js('bo'), Js('bu'), Js('bra'), Js('bru'), Js('bro'), Js('da'), Js('do'), Js('du'), Js('dra'), Js('dru'), Js('dro'), Js('ga'), Js('go'), Js('gu'), Js('gro'), Js('gra'), Js('gru'), Js('ka'), Js('ko'), Js('ku'), Js('ke'), Js('kra'), Js('kro'), Js('kru'), Js('ma'), Js('mo'), Js('mu'), Js('na'), Js('no'), Js('nu'), Js('pa'), Js('po'), Js('pu'), Js('pra'), Js('pro'), Js('pru'), Js('qa'), Js('qo'), Js('qu'), Js('sa'), Js('so'), Js('su'), Js('sra'), Js('sro'), Js('sru'), Js('sta'), Js('sto'), Js('stu'), Js('ta'), Js('to'), Js('tu'), Js('tra'), Js('tro'), Js('tru'), Js('va'), Js('vo'), Js('vu'), Js('vra'), Js('vro'), Js('vru'), Js('xa'), Js('xo'), Js('xu')]))
var.put('nm4', Js([Js('d'), Js('g'), Js('k'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('x'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm5', Js([Js('a'), Js('o'), Js('u'), Js('e'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('A'), Js('O'), Js('E'), Js('B'), Js('Bl'), Js('D'), Js('G'), Js('H'), Js('K'), Js('Kl'), Js('L'), Js('M'), Js('N'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('St'), Js('T'), Js('V'), Js('Vr'), Js('X'), Js('W')]))
var.put('nm7', Js([Js('ba'), Js('be'), Js('bi'), Js('bo'), Js('bra'), Js('bre'), Js('bri'), Js('bro'), Js('da'), Js('de'), Js('di'), Js('do'), Js('dra'), Js('dre'), Js('dri'), Js('dro'), Js('ga'), Js('ge'), Js('gi'), Js('go'), Js('gra'), Js('gre'), Js('gri'), Js('gro'), Js('ka'), Js('ke'), Js('ki'), Js('ko'), Js('kra'), Js('kre'), Js('kri'), Js('kro'), Js('ma'), Js('me'), Js('mi'), Js('mo'), Js('na'), Js('ne'), Js('ni'), Js('no'), Js('pa'), Js('pe'), Js('pi'), Js('po'), Js('pra'), Js('pre'), Js('pri'), Js('pro'), Js('qa'), Js('qe'), Js('qi'), Js('qo'), Js('ra'), Js('re'), Js('rga'), Js('rge'), Js('rgi'), Js('rgo'), Js('ri'), Js('ro'), Js('sa'), Js('se'), Js('si'), Js('so'), Js('sra'), Js('sre'), Js('sri'), Js('sro'), Js('sta'), Js('ste'), Js('sti'), Js('sto'), Js('ta'), Js('te'), Js('ti'), Js('to'), Js('tra'), Js('tre'), Js('tri'), Js('tro'), Js('va'), Js('ve'), Js('vi'), Js('vo'), Js('vra'), Js('vre'), Js('vri'), Js('vro'), Js('xa'), Js('xe'), Js('xi'), Js('xo')]))
var.put('nm8', Js([Js('a'), Js('o'), Js('u'), Js('e'), Js('i'), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
zabrakNames = var.to_python()