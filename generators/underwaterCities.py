__all__ = ['underwaterCities']

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
    var.registers(['nm1', 'nm2', 'result'])
    var.put('nm1', Js([Js('Aby'), Js('Abys'), Js('Ache'), Js('Acio'), Js('Aeg'), Js('Amphi'), Js('Anu'), Js('Aqu'), Js('Aqua'), Js('Aqui'), Js('Asha'), Js('Ashe'), Js('Atla'), Js('Azha'), Js('Azu'), Js('Beli'), Js('Bery'), Js('Boy'), Js('Bri'), Js('Cae'), Js('Caenu'), Js('Cala'), Js('Cata'), Js('Cla'), Js('Coa'), Js('Coara'), Js('Cora'), Js('Delph'), Js('Do'), Js('Ebi'), Js('Expa'), Js('Flu'), Js('Gey'), Js('Gla'), Js('Glaci'), Js('Hippo'), Js('Hy'), Js('Hyd'), Js('Jutu'), Js('Levi'), Js('Levia'), Js('Limu'), Js('Liqi'), Js('Liqu'), Js('Liqua'), Js('Liqui'), Js('Litto'), Js('Mari'), Js('Mer'), Js('Mimi'), Js('Nata'), Js('Nau'), Js('Nauti'), Js('Nava'), Js('Nep'), Js('Neph'), Js('Nept'), Js('Neptu'), Js('Nerei'), Js('Neri'), Js('Njo'), Js('Njor'), Js('Oce'), Js('Ocea'), Js('Osi'), Js('Paci'), Js('Palae'), Js('Pela'), Js('Pose'), Js('Posei'), Js('Pura'), Js('Puri'), Js('Rive'), Js('Sala'), Js('Sali'), Js('Saph'), Js('Saphi'), Js('Scy'), Js('Sequa'), Js('Si'), Js('Sire'), Js('Squa'), Js('Te'), Js('Tempe'), Js('Teth'), Js('Tha'), Js('Thala'), Js('Thau'), Js('The'), Js('Tri'), Js('Trite'), Js('Trito'), Js('Tsu'), Js('Tsuna'), Js('Ty'), Js('Typh'), Js('Va'), Js('Vapo'), Js('Voltu'), Js('Wata')]))
    var.put('nm2', Js([Js('cada'), Js('cadis'), Js('cia'), Js('cique'), Js('cis'), Js('dor'), Js('dore'), Js('gia'), Js('lean'), Js('lin'), Js('lina'), Js('lis'), Js('loch'), Js('lona'), Js('lor'), Js('lora'), Js('lore'), Js('lune'), Js('mari'), Js('mon'), Js('mond'), Js('na'), Js('nas'), Js('ne'), Js('nea'), Js('nia'), Js('nis'), Js('noch'), Js('pis'), Js('ra'), Js('rai'), Js('ran'), Js('rei'), Js('rem'), Js('ren'), Js('reth'), Js('rey'), Js('ri'), Js('ria'), Js('ril'), Js('rin'), Js('ris'), Js('rius'), Js('rus'), Js('sa'), Js('tas'), Js('tesh'), Js('thas'), Js('theas'), Js('this'), Js('thys'), Js('tia'), Js('tin'), Js('tis'), Js('ton'), Js('tria'), Js('via')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
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
underwaterCities = var.to_python()