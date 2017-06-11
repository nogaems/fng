__all__ = ['egyptianTowns']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['names1', 'names2', 'result', 'names3'])
    var.put('names1', Js([Js('Ab'), Js('Ac'), Js('Ak'), Js('Akh'), Js('Am'), Js('An'), Js('Ap'), Js('Ash'), Js('Av'), Js('Be'), Js('Beh'), Js('Behd'), Js('Bes'), Js('Cly'), Js('Clys'), Js('Cu'), Js('Cus'), Js('De'), Js('Deh'), Js('Des'), Js('Dja'), Js('Djan'), Js('Dje'), Js('Djed'), Js('Eb'), Js('Ed'), Js('Ek'), Js('Em'), Js('En'), Js('Fa'), Js('Far'), Js('Ge'), Js('Ges'), Js('He'), Js('Heb'), Js('Ke'), Js('Ker'), Js('Kha'), Js('Khas'), Js('Khe'), Js('Khem'), Js('Ki'), Js('Kis'), Js('Ku'), Js('Kus'), Js('Me'), Js('Med'), Js('Men'), Js('Na'), Js('Nap'), Js('Ne'), Js('Neb'), Js('Nek'), Js('Nekh'), Js('Nem'), Js('Qi'), Js('Qis'), Js('Qu'), Js('Qul'), Js('Sa'), Js('Sak'), Js('Se'), Js('Sep'), Js('Set'), Js('Sha'), Js('Shar'), Js('She'), Js('Shet'), Js('Ta'), Js('Tap'), Js('Tar'), Js('Tje'), Js('Tjeb'), Js('Tjen'), Js('Wa'), Js('Was'), Js('Za')]))
    var.put('names2', Js([Js('be'), Js('bu'), Js('by'), Js('ca'), Js('de'), Js('dje'), Js('dju'), Js('fu'), Js('kha'), Js('khe'), Js('ma'), Js('me'), Js('mu'), Js('ne'), Js('nei'), Js('no'), Js('nou'), Js('nu'), Js('pe'), Js('pi'), Js('po'), Js('re'), Js('ri'), Js('ru'), Js('sa'), Js('sai'), Js('se'), Js('si'), Js('so'), Js('sou'), Js('su'), Js('sy'), Js('ta'), Js('te'), Js('tu'), Js('va'), Js('zu')]))
    var.put('names3', Js([Js('benu'), Js('besheh'), Js('bu'), Js('det'), Js('djed'), Js('dju'), Js('dos'), Js('fu'), Js('hdet'), Js('henet'), Js('kha'), Js('khen'), Js('lzum'), Js('m'), Js('ma'), Js('mar'), Js('meru'), Js('mhat'), Js('mty'), Js('mu'), Js('munein'), Js('n'), Js('na'), Js('nein'), Js('nemhat'), Js('net'), Js('nis'), Js('nu'), Js('nutjer'), Js('pata'), Js('pet'), Js('pis'), Js('remu'), Js('ris'), Js('rma'), Js('rmeru'), Js('rna'), Js('ru'), Js('run'), Js('runa'), Js('s'), Js('sa'), Js('sai'), Js('set'), Js('sheh'), Js('sir'), Js('siris'), Js('sma'), Js('souk'), Js('sut'), Js('sy'), Js('ta'), Js('taten'), Js('ten'), Js('tennu'), Js('this'), Js('thus'), Js('tjer'), Js('tunis'), Js('ty'), Js('yut'), Js('zum'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
            var.put('names', ((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
egyptianTowns = var.to_python()