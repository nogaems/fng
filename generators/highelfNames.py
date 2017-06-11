__all__ = ['highelfNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['names1', 'names2', 'tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names1', Js([Js('Ael'), Js('Aem'), Js('Aer'), Js('Aern'), Js('Aest'), Js('Ag'), Js('Aghn'), Js('Ail'), Js('Aiy'), Js('Alis'), Js('Am'), Js('Amay'), Js('Aoib'), Js('Awen'), Js('Brian'), Js('Brig'), Js('Cael'), Js('Caen'), Js('Cainn'), Js('Ceall'), Js('Cear'), Js('Chey'), Js('Daer'), Js('Deir'), Js('Don'), Js('Eab'), Js('Ead'), Js('Eil'), Js('Eist'), Js('Eor'), Js('Eten'), Js('Faen'), Js('Fen'), Js('Fin'), Js('Finn'), Js('Gael'), Js('Gel'), Js('Hat'), Js('Kim'), Js('Kol'), Js('Laen'), Js('Leen'), Js('Lenm'), Js('Maed'), Js('Maen'), Js('Maer'), Js('Maev'), Js('Mag'), Js('Mair'), Js('Med'), Js('Mig'), Js('Moir'), Js('Mor'), Js('Muir'), Js('Naem'), Js('Nam'), Js('Nual'), Js('On'), Js('Onid'), Js('Orl'), Js('Ros'), Js('Saen'), Js('Shan'), Js('Sib'), Js('Sor'), Js('Taer'), Js('Tak'), Js('Ter'), Js('Wak'), Js('Wik'), Js('Yok')]))
        var.put('names2', Js([Js('aela'), Js('aelah'), Js('aena'), Js('aene'), Js('aenon'), Js('aid'), Js('aigen'), Js('aimh'), Js('aine'), Js('aith'), Js('ala'), Js('alae'), Js('alasa'), Js('ane'), Js('angwa'), Js('ania'), Js('anne'), Js('anon'), Js('aoin'), Js('aoine'), Js('athla'), Js('auma'), Js('awa'), Js('eal'), Js('eala'), Js('eamhna'), Js('eann'), Js('ear'), Js('earca'), Js('eekoni'), Js('een'), Js('eine'), Js('eis'), Js('enda'), Js('enia'), Js('enna'), Js('iav'), Js('ighid'), Js('ilahi'), Js('ilin'), Js('ine'), Js('inita'), Js('inka'), Js('inn'), Js('iona'), Js('ionn'), Js('irin'), Js('irne'), Js('is'), Js('ise'), Js('ish'), Js('ita'), Js('odhna'), Js('oise'), Js('oma'), Js('ona'), Js('oni'), Js('onora'), Js('ose'), Js('ovi'), Js('uala'), Js('uanee'), Js('ulah'), Js('unia'), Js('uoia')]))
    else:
        var.put('names1', Js([Js('Adh'), Js('Ag'), Js('Ahm'), Js('Ail'), Js('Ain'), Js('An'), Js('Aodh'), Js('Apen'), Js('Ar'), Js('Bair'), Js('Baol'), Js('Bean'), Js('Beol'), Js('Cadh'), Js('Cail'), Js('Caim'), Js('Caol'), Js('Ceall'), Js('Cean'), Js('Cher'), Js('Cill'), Js('Col'), Js('Con'), Js('Dak'), Js('Deam'), Js('Dels'), Js('Din'), Js('Each'), Js('Eam'), Js('Ear'), Js('Earn'), Js('Eimh'), Js('Eir'), Js('Eirn'), Js('Eog'), Js('Fael'), Js('Fear'), Js('Fer'), Js('Fin'), Js('Finn'), Js('Greag'), Js('Hahn'), Js('Hint'), Js('Hon'), Js('Kel'), Js('Lans'), Js('Maed'), Js('Mael'), Js('Maodh'), Js('Maoil'), Js('Mis'), Js('Mok'), Js('Muat'), Js('Muir'), Js('Niadh'), Js('Ohan'), Js('PAid'), Js('Pead'), Js('Raem'), Js('Saem'), Js('Seam'), Js('Sen'), Js('Taim'), Js('Tas'), Js('Tok'), Js('Wak'), Js('Wan'), Js('Yis'), Js('Yum')]))
        var.put('names2', Js([Js('amh'), Js('in'), Js('onn'), Js('ear'), Js('ach'), Js('aire'), Js('ithir'), Js('ileas'), Js('os'), Js('amcha'), Js('uan'), Js('oine'), Js('ionn'), Js('alach'), Js('eart'), Js('ainn'), Js('aon'), Js('easal'), Js('eall'), Js('adh'), Js('air'), Js('eidigh'), Js('obhar'), Js('uil'), Js('ionan'), Js('uimin'), Js('eaglan'), Js('ang'), Js('ead'), Js('eal'), Js('aidh'), Js('earn'), Js('onn'), Js('anan'), Js('ainin'), Js('iarn'), Js('ainm'), Js('iachna'), Js('ias'), Js('asan'), Js('uaire'), Js('erian'), Js('airian'), Js('ainn'), Js('aoilin'), Js('ios'), Js('each'), Js('eamas'), Js('eanan'), Js('amh'), Js('anu'), Js('ando'), Js('imon'), Js('oki'), Js('eyo'), Js('unta'), Js('oda'), Js('otah'), Js('osan'), Js('emin'), Js('abaoo'), Js('omemah'), Js('ahome'), Js('aneo'), Js('on'), Js('otah'), Js('oton'), Js('ehew'), Js('aska'), Js('enam'), Js('iye'), Js('achme'), Js('opka'), Js('etu'), Js('ahton')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', (var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2'))))
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
highelfNames = var.to_python()