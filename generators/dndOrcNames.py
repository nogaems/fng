__all__ = ['dndOrcNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameFem', 'nm4', 'nameGen', 'nm5', 'nm3', 'nameMas', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameFem_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
    var.put('nMs', ((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameFem_.func_name = 'nameFem'
var.put('nameFem', PyJsHoisted_nameFem_)
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
    var.put('nMs', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameMas_.func_name = 'nameMas'
var.put('nameMas', PyJsHoisted_nameMas_)
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
                var.get('nameFem')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameFem')()
            else:
                var.get('nameMas')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameMas')()
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ag'), Js('Agg'), Js('Ar'), Js('Arn'), Js('As'), Js('At'), Js('Atr'), Js('B'), Js('Bar'), Js('Bel'), Js('Bor'), Js('Br'), Js('Brak'), Js('C'), Js('Cr'), Js('D'), Js('Dor'), Js('Dr'), Js('Dur'), Js('G'), Js('Gal'), Js('Gan'), Js('Gar'), Js('Gna'), Js('Gor'), Js('Got'), Js('Gr'), Js('Gram'), Js('Grim'), Js('Grom'), Js('Grum'), Js('Gul'), Js('H'), Js('Hag'), Js('Han'), Js('Har'), Js('Hog'), Js('Hon'), Js('Hor'), Js('Hun'), Js('Hur'), Js('K'), Js('Kal'), Js('Kam'), Js('Kar'), Js('Kel'), Js('Kil'), Js('Kom'), Js('Kor'), Js('Kra'), Js('Kru'), Js('Kul'), Js('Kur'), Js('Lum'), Js('M'), Js('Mag'), Js('Mahl'), Js('Mak'), Js('Mal'), Js('Mar'), Js('Mog'), Js('Mok'), Js('Mor'), Js('Mug'), Js('Muk'), Js('Mura'), Js('N'), Js('Oggu'), Js('Ogu'), Js('Ok'), Js('Oll'), Js('Or'), Js('Rek'), Js('Ren'), Js('Ron'), Js('Rona'), Js('S'), Js('Sar'), Js('Sor'), Js('T'), Js('Tan'), Js('Th'), Js('Thar'), Js('Ther'), Js('Thr'), Js('Thur'), Js('Trak'), Js('Truk'), Js('Ug'), Js('Uk'), Js('Ukr'), Js('Ull'), Js('Ur'), Js('Urth'), Js('Urtr'), Js('Z'), Js('Za'), Js('Zar'), Js('Zas'), Js('Zav'), Js('Zev'), Js('Zor'), Js('Zur'), Js('Zus')]))
var.put('nm2', Js([Js('a'), Js('a'), Js('a'), Js('o'), Js('o'), Js('e'), Js('i'), Js('u'), Js('u'), Js('u')]))
var.put('nm3', Js([Js('bak'), Js('bar'), Js('bark'), Js('bash'), Js('bur'), Js('burk'), Js('d'), Js('dak'), Js('dall'), Js('dar'), Js('dark'), Js('dash'), Js('dim'), Js('dur'), Js('durk'), Js('g'), Js('gak'), Js('gall'), Js('gar'), Js('gark'), Js('gash'), Js('glar'), Js('gul'), Js('gur'), Js('m'), Js('mak'), Js('mar'), Js('marsh'), Js('mash'), Js('mir'), Js('mur'), Js('n'), Js('nar'), Js('nars'), Js('nur'), Js('rak'), Js('rall'), Js('rash'), Js('rim'), Js('rimm'), Js('rk'), Js('rsh'), Js('rth'), Js('ruk'), Js('sk'), Js('tar'), Js('tir'), Js('tur'), Js('z'), Js('zall'), Js('zar'), Js('zur')]))
var.put('nm4', Js([Js('Al'), Js('Ar'), Js('Br'), Js('Ek'), Js('El'), Js('Fal'), Js('Fel'), Js('Fol'), Js('Ful'), Js('G'), Js('Gaj'), Js('Gar'), Js('Gij'), Js('Gor'), Js('Gr'), Js('Gry'), Js('Gyn'), Js('Hur'), Js('K'), Js('Kar'), Js('Kat'), Js('Ker'), Js('Ket'), Js('Kir'), Js('Kot'), Js('Kur'), Js('Kut'), Js('Lag'), Js('M'), Js('Mer'), Js('Mir'), Js('Mor'), Js('N'), Js('Ol'), Js('Oot'), Js('Puy'), Js('R'), Js('Rah'), Js('Rahk'), Js('Ras'), Js('Rash'), Js('Raw'), Js('Roh'), Js('Rohk'), Js('S'), Js('Sam'), Js('San'), Js('Sem'), Js('Sen'), Js('Sh'), Js('Shay'), Js('Sin'), Js('Sum'), Js('Sun'), Js('Tam'), Js('Tem'), Js('Tu'), Js('Tum'), Js('Ub'), Js('Um'), Js('Ur'), Js('Van'), Js('Zan'), Js('Zen'), Js('Zon'), Js('Zun')]))
var.put('nm5', Js([Js('a'), Js('a'), Js('o'), Js('o'), Js('e'), Js('i'), Js('i'), Js('u')]))
var.put('nm6', Js([Js('d'), Js('da'), Js('dar'), Js('dur'), Js('g'), Js('gar'), Js('gh'), Js('gri'), Js('gu'), Js('sh'), Js('sha'), Js('shi'), Js('gum'), Js('gume'), Js('gur'), Js('ki'), Js('mar'), Js('mi'), Js('mira'), Js('me'), Js('mur'), Js('ne'), Js('ner'), Js('nir'), Js('nar'), Js('nchu'), Js('ni'), Js('nur'), Js('ral'), Js('rel'), Js('ri'), Js('rook'), Js('ti'), Js('tah'), Js('tir'), Js('tar'), Js('tur'), Js('war'), Js('z'), Js('zar'), Js('zara'), Js('zi'), Js('zur'), Js('zura'), Js('zira')]))
pass
pass
pass
pass


# Add lib to the module scope
dndOrcNames = var.to_python()