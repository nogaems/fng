__all__ = ['ogreNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4'))))
            else:
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('Bl'), Js('Br'), Js('D'), Js('Dr'), Js('G'), Js('Gl'), Js('Gr'), Js('K'), Js('Kl'), Js('Kr'), Js('M'), Js('N'), Js('T'), Js('Tr'), Js('V'), Js('Vr'), Js('W'), Js('X'), Js('Y'), Js('Z'), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('e'), Js('i'), Js('u'), Js('o'), Js('a')]))
var.put('nm3', Js([Js('b'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('g'), Js('k'), Js('rug'), Js('rog'), Js('rag'), Js('ruk'), Js('rok'), Js('kag'), Js('rth'), Js('rub'), Js('rob'), Js('rig'), Js('kohr'), Js('kuhr'), Js('kor'), Js('kur'), Js('ret'), Js('rut'), Js('rot'), Js('kug'), Js('kog'), Js('kig'), Js('keg'), Js('reg'), Js('rek'), Js('rg'), Js('rk'), Js('zar'), Js('zug'), Js('zor'), Js('zag'), Js('zig'), Js('zir'), Js('zur'), Js('nk'), Js('gut'), Js('grut'), Js('grot'), Js('gruk'), Js('grok'), Js('rok'), Js('ruk'), Js('rag'), Js('gark'), Js('gork'), Js('gurk'), Js('kur'), Js('kurk'), Js('kurg'), Js('kor'), Js('kork'), Js('korg'), Js('zog'), Js('zug'), Js('zig'), Js('zrog'), Js('zrug')]))
pass
pass


# Add lib to the module scope
ogreNames = var.to_python()