__all__ = ['pegasusNames']

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
var.put('nm1', Js([Js('Abde'), Js('Aby'), Js('Aca'), Js('Ache'), Js('Achi'), Js('Acta'), Js('Ade'), Js('Adme'), Js('Adra'), Js('Ae'), Js('Aea'), Js('Aeto'), Js('Agame'), Js('Aja'), Js('Ale'), Js('Amy'), Js('Ando'), Js('Anta'), Js('Ante'), Js('Apo'), Js('Arca'), Js('Arce'), Js('Arche'), Js('Argo'), Js('Arse'), Js('Arte'), Js('Asca'), Js('Atha'), Js('Atla'), Js('Baccu'), Js('Bazy'), Js('Bry'), Js('Cae'), Js('Cali'), Js('Capa'), Js('Casea'), Js('Cepha'), Js('Cory'), Js('Cyra'), Js('Dae'), Js('Dama'), Js('Damia'), Js('Damio'), Js('Daria'), Js('Dario'), Js('Deme'), Js('Demo'), Js('Dio'), Js('Dora'), Js('Dra'), Js('Era'), Js('Ere'), Js('Este'), Js('Eury'), Js('Fe'), Js('Gae'), Js('Gela'), Js('Hae'), Js('Helio'), Js('Hera'), Js('Hero'), Js('Ia'), Js('Ico'), Js('Ja'), Js('Ko'), Js('Koru'), Js('Kra'), Js('Kyri'), Js('La'), Js('Laiu'), Js('Lea'), Js('Leo'), Js('Leoni'), Js('Lo'), Js('Lu'), Js('Mela'), Js('Mida'), Js('Myro'), Js('Nau'), Js('Ne'), Js('Obe'), Js('Obia'), Js('Ocea'), Js('Pano'), Js('Pelia'), Js('Phanta'), Js('Phy'), Js('Pria'), Js('Pyra'), Js('Ra'), Js('Rho'), Js('Saba'), Js('Sote'), Js('Ste'), Js('Tara'), Js('Tela'), Js('Tha'), Js('Thano'), Js('Thau'), Js('The'), Js('Thye'), Js('Ti'), Js('Tiva'), Js('Tri'), Js('Ty'), Js('Tyro'), Js('Vasi'), Js('Xa'), Js('Ze'), Js('Zeno'), Js('Zo')]))
var.put('nm2', Js([Js('carus'), Js('celos'), Js('chus'), Js('clus'), Js('cnaeon'), Js('cos'), Js('dalus'), Js('dareus'), Js('das'), Js('demus'), Js('des'), Js('don'), Js('dras'), Js('dros'), Js('jax'), Js('kon'), Js('lan'), Js('laus'), Js('leimon'), Js('lemus'), Js('leon'), Js('les'), Js('lios'), Js('lius'), Js('lix'), Js('lles'), Js('llos'), Js('lops'), Js('los'), Js('lpheus'), Js('lphos'), Js('maeus'), Js('mas'), Js('medes'), Js('meon'), Js('mion'), Js('mnon'), Js('mon'), Js('morus'), Js('naeon'), Js('nder'), Js('ndras'), Js('neus'), Js('nidas'), Js('nios'), Js('nis'), Js('nius'), Js('nnos'), Js('nous'), Js('peros'), Js('pheus'), Js('phon'), Js('phos'), Js('phyr'), Js('pios'), Js('pius'), Js('rdanus'), Js('reus'), Js('rgos'), Js('rgus'), Js('rian'), Js('ridon'), Js('rios'), Js('ritus'), Js('rnus'), Js('ron'), Js('ros'), Js('rtus'), Js('rus'), Js('ses'), Js('seus'), Js('sidas'), Js('sios'), Js('sius'), Js('smus'), Js('ssus'), Js('stheus'), Js('sthus'), Js('stolos'), Js('stos'), Js('stus'), Js('teon'), Js('teus'), Js('thes'), Js('thon'), Js('tone'), Js('tos'), Js('trios'), Js('trius'), Js('tros'), Js('tus'), Js('xio'), Js('xus')]))
var.put('nm3', Js([Js('Aca'), Js('Ada'), Js('Ade'), Js('Ado'), Js('Aga'), Js('Agne'), Js('Ai'), Js('Ala'), Js('Aldo'), Js('Ale'), Js('Ali'), Js('Aly'), Js('Ana'), Js('Ane'), Js('Aphro'), Js('Apo'), Js('Are'), Js('Ari'), Js('Athe'), Js('Axe'), Js('Ba'), Js('Bella'), Js('Ca'), Js('Cala'), Js('Casca'), Js('Cassa'), Js('Cha'), Js('Che'), Js('Co'), Js('Cyna'), Js('Da'), Js('Dama'), Js('Deni'), Js('Dia'), Js('Dio'), Js('Dy'), Js('Ebo'), Js('Eire'), Js('Ele'), Js('Elea'), Js('Eli'), Js('Eu'), Js('Eudo'), Js('Euphe'), Js('Eva'), Js('Fae'), Js('Fe'), Js('Gela'), Js('Ha'), Js('Hele'), Js('Hya'), Js('Hypa'), Js('Ido'), Js('Io'), Js('Iri'), Js('Isa'), Js('Ja'), Js('Ka'), Js('Kare'), Js('Kari'), Js('Katha'), Js('Ko'), Js('Ky'), Js('La'), Js('Lari'), Js('Lea'), Js('Leo'), Js('Li'), Js('Liva'), Js('Mae'), Js('Mari'), Js('Me'), Js('Melai'), Js('Meli'), Js('Mine'), Js('Nai'), Js('Nare'), Js('Ne'), Js('Neo'), Js('No'), Js('Obe'), Js('Ode'), Js('Oly'), Js('Ophe'), Js('Ophi'), Js('Pene'), Js('Perse'), Js('Phe'), Js('Phy'), Js('Rai'), Js('Re'), Js('Sa'), Js('Sele'), Js('Sire'), Js('Ste'), Js('Ta'), Js('Tere'), Js('Tha'), Js('The'), Js('Tia'), Js('Tima'), Js('Tita'), Js('Tre'), Js('Vane'), Js('Xe'), Js('Yale'), Js('Yola'), Js('Za'), Js('Zani'), Js('Ze'), Js('Zera')]))
var.put('nm4', Js([Js('cia'), Js('da'), Js('dia'), Js('dite'), Js('dora'), Js('la'), Js('lanie'), Js('lena'), Js('leta'), Js('lia'), Js('lina'), Js('lla'), Js('llia'), Js('lline'), Js('lona'), Js('mara'), Js('meda'), Js('mena'), Js('mia'), Js('misia'), Js('mona'), Js('mone'), Js('na'), Js('ndia'), Js('ndra'), Js('neta'), Js('nia'), Js('nie'), Js('nne'), Js('nor'), Js('nora'), Js('ntha'), Js('nthe'), Js('nthea'), Js('phelia'), Js('phine'), Js('phira'), Js('phne'), Js('phone'), Js('ra'), Js('rena'), Js('rene'), Js('resa'), Js('rine'), Js('rise'), Js('rissa'), Js('rria'), Js('sia'), Js('sima'), Js('sine'), Js('ssa'), Js('tasia'), Js('teia'), Js('tha'), Js('thea'), Js('thia'), Js('thy'), Js('tia'), Js('tine'), Js('tria'), Js('vana'), Js('xis')]))
pass
pass


# Add lib to the module scope
pegasusNames = var.to_python()