__all__ = ['beorningNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ag'), Js('Aln'), Js('Aran'), Js('Arn'), Js('Bald'), Js('Beorn'), Js('Beran'), Js('Borg'), Js('Both'), Js('Dag'), Js('Darn'), Js('Dreng'), Js('Dug'), Js('Eld'), Js('Erad'), Js('Eran'), Js('Ern'), Js('Fer'), Js('Forn'), Js('Frid'), Js('Froth'), Js('Gal'), Js('Glum'), Js('Gluth'), Js('Grim'), Js('Har'), Js('Hart'), Js('Heim'), Js('Hroth'), Js('Ig'), Js('Ingel'), Js('Is'), Js('Iw'), Js('Jal'), Js('Jar'), Js('Jarn'), Js('Jorn'), Js('Log'), Js('Lor'), Js('Lyd'), Js('Lyth'), Js('Mag'), Js('Mar'), Js('Morn'), Js('Moth'), Js('Nard'), Js('Ned'), Js('Nef'), Js('Nor'), Js('Old'), Js('Ord'), Js('Ot'), Js('Oth'), Js('Rand'), Js('Rath'), Js('Ric'), Js('Rod'), Js('Sig'), Js('Skal'), Js('Skol'), Js('Stig'), Js('Tar'), Js('Theod'), Js('Thor'), Js('Throt'), Js('Val'), Js('Vald'), Js('Vig'), Js('Vul'), Js('Wal'), Js('Wald'), Js('Wid'), Js('Wul')]))
var.put('nm2', Js([Js('ald'), Js('angar'), Js('ard'), Js('aric'), Js('bald'), Js('beorn'), Js('bert'), Js('bold'), Js('brand'), Js('dar'), Js('dhor'), Js('dam'), Js('dan'), Js('fald'), Js('fara'), Js('fast'), Js('forn'), Js('gár'), Js('geir'), Js('gils'), Js('grim'), Js('hame'), Js('har'), Js('helm'), Js('here'), Js('kald'), Js('kar'), Js('karl'), Js('kin'), Js('mód'), Js('mar'), Js('mark'), Js('moth'), Js('mund'), Js('ohd'), Js('ond'), Js('or'), Js('oric'), Js('rand'), Js('rath'), Js('rek'), Js('ric'), Js('sel'), Js('sorn'), Js('stin'), Js('styr'), Js('tar'), Js('taric'), Js('thorn'), Js('torn'), Js('var'), Js('vat'), Js('vir'), Js('vith'), Js('wald'), Js('war'), Js('wine'), Js('wulf')]))
var.put('nm3', Js([Js('Aer'), Js('Amal'), Js('Arin'), Js('Ava'), Js('Beorn'), Js('Bera'), Js('Beran'), Js('Birn'), Js('Bog'), Js('Bruni'), Js('Din'), Js('Dis'), Js('Dom'), Js('Dyr'), Js('Eir'), Js('Esil'), Js('Eth'), Js('Ey'), Js('Fast'), Js('Faye'), Js('Feor'), Js('Fyn'), Js('Gail'), Js('Gel'), Js('Gerth'), Js('Gis'), Js('Grim'), Js('Gud'), Js('Hall'), Js('Har'), Js('Hild'), Js('Hrim'), Js('Huld'), Js('Hun'), Js('Ilin'), Js('Ingi'), Js('Ior'), Js('Is'), Js('Jen'), Js('Jern'), Js('Jil'), Js('Jor'), Js('Kat'), Js('Kath'), Js('Kay'), Js('Kyn'), Js('Leot'), Js('Lif'), Js('Lin'), Js('Lyn'), Js('Maer'), Js('Mag'), Js('Mar'), Js('Mel'), Js('Nel'), Js('Nor'), Js('Nyr'), Js('Od'), Js('Ol'), Js('Ovi'), Js('Ovin'), Js('Raen'), Js('Ran'), Js('Rhon'), Js('Ril'), Js('Sal'), Js('Sig'), Js('Sol'), Js('Svan'), Js('Ul'), Js('Ulin'), Js('Ulvin'), Js('Una'), Js('Vel'), Js('Ven'), Js('Vil'), Js('Vyl'), Js('Waen'), Js('Wen'), Js('Win'), Js('Wyl')]))
var.put('nm4', Js([Js('a'), Js('aen'), Js('aeya'), Js('anda'), Js('ara'), Js('ava'), Js('aya'), Js('bi'), Js('bina'), Js('bwyn'), Js('byn'), Js('da'), Js('dira'), Js('dis'), Js('dora'), Js('eith'), Js('elde'), Js('ena'), Js('era'), Js('eva'), Js('ewyn'), Js('fast'), Js('firth'), Js('frida'), Js('fyn'), Js('garth'), Js('gifu'), Js('ginny'), Js('gun'), Js('helda'), Js('hena'), Js('hera'), Js('hild'), Js('la'), Js('laug'), Js('lin'), Js('loth'), Js('nida'), Js('nis'), Js('nwyn'), Js('ny'), Js('olin'), Js('ora'), Js('otta'), Js('owyn'), Js('rin'), Js('risa'), Js('rlin'), Js('run'), Js('thrith'), Js('tina'), Js('tira'), Js('tyn'), Js('vera'), Js('vild'), Js('vor'), Js('vyn'), Js('wed'), Js('wild'), Js('winne'), Js('wyn')]))
pass
pass


# Add lib to the module scope
beorningNames = var.to_python()