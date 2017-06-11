__all__ = ['kroganNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names5', 'names2', 'nameGen', 'names3'])
@Js
def PyJsHoisted_nameGen_(gender, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'gender':gender}, var)
    var.registers(['names4', 'tp', 'result', 'gender'])
    var.put('tp', var.get('gender'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names4', Js([Js('')]))
    else:
        var.put('names4', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('a')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
            var.put('names', (((((((var.get('names1').get(var.get('rnd4'))+var.get('names2').get(var.get('rnd5')))+var.get('names5').get(var.get('rnd6')))+Js(' '))+var.get('names1').get(var.get('rnd0')))+var.get('names2').get(var.get('rnd1')))+var.get('names3').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('B'), Js('Br'), Js('C'), Js('Cr'), Js('Ch'), Js('D'), Js('Dr'), Js('F'), Js('G'), Js('Gr'), Js('H'), Js('J'), Js('K'), Js('Kh'), Js('Kr'), Js('M'), Js('N'), Js('P'), Js('Pr'), Js('Q'), Js('Qr'), Js('R'), Js('S'), Js('Sr'), Js('Str'), Js('T'), Js('Tr'), Js('V'), Js('Vr'), Js('W'), Js('Wr'), Js('Zr')]))
var.put('names2', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('a'), Js('u')]))
var.put('names3', Js([Js('rr'), Js('x'), Js('nd'), Js('nk'), Js('yas'), Js('rm'), Js('rn'), Js('rk'), Js('tack'), Js('rg'), Js('g'), Js('gg'), Js('sk'), Js('zk'), Js('nd'), Js('d'), Js('rd'), Js('xx'), Js('yak'), Js('yax'), Js('rak'), Js('nak'), Js('kar'), Js('kor'), Js('lak'), Js('gor'), Js('gar'), Js('gas'), Js('r')]))
var.put('names5', Js([Js('ash'), Js('bakur'), Js('brakir'), Js('dark'), Js('drak'), Js('drax'), Js('dtar'), Js('k'), Js('kador'), Js('karor'), Js('kirum'), Js('kmar'), Js('kmor'), Js('krax'), Js('ksan'), Js('ksar'), Js('kson'), Js('ksor'), Js('l'), Js('lot'), Js('mar'), Js('nar'), Js('ndok'), Js('ntor'), Js('rax'), Js('rbok'), Js('rbon'), Js('rdak'), Js('rdan'), Js('rdok'), Js('rdon'), Js('rgal'), Js('rgon'), Js('rkan'), Js('rloc'), Js('rlok'), Js('rsan'), Js('rtak'), Js('tarog'), Js('tarok'), Js('tarum'), Js('tarun'), Js('tatog'), Js('tilak'), Js('vanor'), Js('varog'), Js('vrak'), Js('x'), Js('yrdok'), Js('yrloc')]))
pass
pass


# Add lib to the module scope
kroganNames = var.to_python()