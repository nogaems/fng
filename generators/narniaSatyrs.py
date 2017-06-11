__all__ = ['narniaSatyrs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('nm1', Js([Js('Abder'), Js('Absyr'), Js('Abyd'), Js('Acast'), Js('Achat'), Js('Achel'), Js('Acher'), Js('Achil'), Js('Achl'), Js('Acris'), Js('Act'), Js('Adelph'), Js('Adm'), Js('Adon'), Js('Adr'), Js('Adras'), Js('Aeg'), Js('Aeol'), Js('Aggel'), Js('Alcin'), Js('Ald'), Js('Ambr'), Js('Amyc'), Js('Anast'), Js('Anat'), Js('Anc'), Js('And'), Js('Andr'), Js('Ant'), Js('Apost'), Js('Arc'), Js('Arg'), Js('Arist'), Js('Ars'), Js('Ast'), Js('Aster'), Js('Bacc'), Js('Bas'), Js('Bast'), Js('Bauc'), Js('Ceph'), Js('Cerb'), Js('Ces'), Js('Cet'), Js('Char'), Js('Cim'), Js('Cir'), Js('Corb'), Js('Cyr'), Js('Daem'), Js('Dam'), Js('Dar'), Js('Darr'), Js('Dem'), Js('Dim'), Js('Dion'), Js('Dor'), Js('Dun'), Js('Egid'), Js('Elefth'), Js('Eleuth'), Js('Endr'), Js('Eras'), Js('Ereb'), Js('Eum'), Js('Eur'), Js('Eust'), Js('Ev'), Js('Fan'), Js('Fed'), Js('Feodr'), Js('Gael'), Js('Gal'), Js('Gil'), Js('Gor'), Js('Greg'), Js('Haem'), Js('Hect'), Js('Hel'), Js('Ias'), Js('Ic'), Js('Idom'), Js('Ignat'), Js('Inach'), Js('Ivank'), Js('Jas'), Js('Kadm'), Js('Kir'), Js('Konst'), Js('Korud'), Js('Kost'), Js('Krat'), Js('Kyr'), Js('Lad'), Js('Lak'), Js('Land'), Js('Laz'), Js('Leand'), Js('Lich'), Js('Louk'), Js('Lox'), Js('Lyc'), Js('Maur'), Js('Ment'), Js('Mich'), Js('Myl'), Js('Nark'), Js('Nem'), Js('Nik'), Js('Nil'), Js('Nill'), Js('Ocn'), Js('Oen'), Js('Oenom'), Js('Or'), Js('Orthr'), Js('Pal'), Js('Panag'), Js('Par'), Js('Pell'), Js('Petr'), Js('Pil'), Js('Pirr'), Js('Preb'), Js('Prot'), Js('Rhod'), Js('Sav'), Js('Savv'), Js('Sim'), Js('Sot'), Js('Stam'), Js('Stavr'), Js('Stel'), Js('Sterg'), Js('Tak'), Js('Tal'), Js('Than'), Js('Thaum'), Js('Tim'), Js('Timm'), Js('Tit'), Js('Tod'), Js('Tol'), Js('Tox'), Js('Trit'), Js('Vas'), Js('Yan'), Js('Yann'), Js('Yor'), Js('Yrig'), Js('Zar'), Js('Zen'), Js('Zeph'), Js('Zolt')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('us'), Js('ius')]))
var.put('nm3', Js([Js('ia'), Js('a'), Js('ia')]))
pass
pass


# Add lib to the module scope
narniaSatyrs = var.to_python()