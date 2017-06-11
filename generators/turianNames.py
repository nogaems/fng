__all__ = ['turianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names3'])
@Js
def PyJsHoisted_nameGen_(gender, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'gender':gender}, var)
    var.registers(['names1', 'names2', 'tp', 'result', 'gender'])
    var.put('tp', var.get('gender'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names1', Js([Js('Agri'), Js('Am'), Js('Amu'), Js('Amul'), Js('Amuli'), Js('Ap'), Js('Ar'), Js('Arru'), Js('Au'), Js('Augu'), Js('Augus'), Js('Aul'), Js('Bri'), Js('Bru'), Js('Brut'), Js('Ca'), Js('Cae'), Js('Cael'), Js('Cai'), Js('Cam'), Js('Cami'), Js('Can'), Js('Cas'), Js('Cna'), Js('Cnae'), Js('Cos'), Js('De'), Js('Dec'), Js('Deci'), Js('Dru'), Js('Drus'), Js('Fa'), Js('Fau'), Js('Faus'), Js('Fla'), Js('Flavi'), Js('Ga'), Js('Gai'), Js('Gal'), Js('Galer'), Js('He'), Js('Her'), Js('Heri'), Js('Ho'), Js('Hos'), Js('Ju'), Js('Juli'), Js('Julian'), Js('Ka'), Js('Kae'), Js('Kaes'), Js('La'), Js('Lar'), Js('Lu'), Js('Luc'), Js('Luci'), Js('Ma'), Js('Mame'), Js('Mamer'), Js('Man'), Js('Mani'), Js('Mar'), Js('Marce'), Js('Max'), Js('Maxi'), Js('Met'), Js('No'), Js('Nu'), Js('Num'), Js('Nume'), Js('Octa'), Js('Octavi'), Js('Op'), Js('Opi'), Js('Oppi'), Js('Pa'), Js('Paul'), Js('Pla'), Js('Po'), Js('Posti'), Js('Postu'), Js('Pot'), Js('Poti'), Js('Pri'), Js('Prim'), Js('Pro'), Js('Proc'), Js('Procu'), Js('Pu'), Js('Publi'), Js('Qui'), Js('Quin'), Js('Se'), Js('Sec'), Js('Secu'), Js('Sep'), Js('Septi'), Js('Ser'), Js('Servi'), Js('Si'), Js('Sis'), Js('Spu'), Js('Te'), Js('Ter'), Js('Terti'), Js('Ti'), Js('Tibe'), Js('Tiber'), Js('Tiberi'), Js('Tu'), Js('Tul'), Js('Tull'), Js('Ve'), Js('Vel'), Js('Vi'), Js('Vibi'), Js('Vo'), Js('Vopi')]))
        var.put('names2', Js([Js('bius'), Js('bus'), Js('cus'), Js('eus'), Js('ius'), Js('lio'), Js('lius'), Js('lus'), Js('mius'), Js('mus'), Js('na'), Js('nus'), Js('pius'), Js('rius'), Js('runs'), Js('sius'), Js('so'), Js('ter'), Js('tis'), Js('tius'), Js('tus'), Js('us'), Js('vius'), Js('vus')]))
    else:
        var.put('names1', Js([Js('Abu'), Js('Ac'), Js('Aci'), Js('Aebu'), Js('Aedi'), Js('Aemi'), Js('Al'), Js('An'), Js('Anto'), Js('Avi'), Js('Bae'), Js('Ban'), Js('Barba'), Js('Betu'), Js('Bruc'), Js('Cae'), Js('Caeci'), Js('Cael'), Js('Caese'), Js('Caeso'), Js('Cali'), Js('Calve'), Js('Came'), Js('Cami'), Js('Cani'), Js('Cice'), Js('Clo'), Js('Comi'), Js('Conse'), Js('Decu'), Js('Desti'), Js('Dexi'), Js('Di'), Js('Duro'), Js('Epi'), Js('Equ'), Js('Fadi'), Js('Fla'), Js('Flo'), Js('Flori'), Js('Floro'), Js('Furi'), Js('Gabi'), Js('Gale'), Js('Gega'), Js('Gra'), Js('Here'), Js('Hermi'), Js('Hora'), Js('Ici'), Js('Ju'), Js('Juve'), Js('La'), Js('Lae'), Js('Libu'), Js('Livi'), Js('Luta'), Js('Mae'), Js('Mal'), Js('Mani'), Js('Mari'), Js('Maxi'), Js('Me'), Js('Mene'), Js('Meti'), Js('Milo'), Js('Nae'), Js('Nepi'), Js('Ni'), Js('Novi'), Js('Octa'), Js('Oppi'), Js('Pa'), Js('Pae'), Js('Ped'), Js('Pina'), Js('Pli'), Js('Pol'), Js('Pompe'), Js('Popi'), Js('Por'), Js('Qu'), Js('Qui'), Js('Ru'), Js('Ruso'), Js('Ruti'), Js('Salo'), Js('Secu'), Js('Sei'), Js('Sen'), Js('Septi'), Js('Si'), Js('Sido'), Js('Sil'), Js('Ta'), Js('Tani'), Js('Treba'), Js('Treme'), Js('Tu'), Js('Tul'), Js('Ul'), Js('Va'), Js('Vale'), Js('Vel'), Js('Vera'), Js('Vi'), Js('Vibi'), Js('Viri'), Js('Vite'), Js('Vitel'), Js('Volu'), Js('Vore')]))
        var.put('names2', Js([Js('ana'), Js('bia'), Js('cia'), Js('cidia'), Js('dia'), Js('ginia'), Js('ia'), Js('lea'), Js('lia'), Js('lonia'), Js('mia'), Js('na'), Js('naria'), Js('nea'), Js('nia'), Js('pia'), Js('pilia'), Js('ponia'), Js('retia'), Js('ria'), Js('sia'), Js('tana'), Js('teia'), Js('tia'), Js('tilia'), Js('tina'), Js('tiria'), Js('toria'), Js('vea'), Js('via')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
            var.put('names', ((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd1')))+Js(' '))+var.get('names3').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names3', Js([Js('Ab'), Js('Aber'), Js('Abi'), Js('Aca'), Js('Acha'), Js('Acil'), Js('Ada'), Js('Adep'), Js('Adju'), Js('Adra'), Js('Aebu'), Js('Aet'), Js('Ag'), Js('Aga'), Js('Ago'), Js('Al'), Js('Alba'), Js('Albi'), Js('Albu'), Js('Ale'), Js('Ba'), Js('Bar'), Js('Barba'), Js('Bell'), Js('Bella'), Js('Belli'), Js('Bibu'), Js('Bitu'), Js('Bola'), Js('Boni'), Js('Brom'), Js('Bromi'), Js('Bru'), Js('Bruc'), Js('Bul'), Js('Cae'), Js('Cael'), Js('Caep'), Js('Cal'), Js('Cala'), Js('Calp'), Js('Calpo'), Js('Cam'), Js('Campa'), Js('Can'), Js('Candi'), Js('Capi'), Js('Dar'), Js('Darda'), Js('Dec'), Js('Dexi'), Js('Didi'), Js('Domi'), Js('Domiti'), Js('Doni'), Js('Drus'), Js('Drusi'), Js('Duvi'), Js('Ebo'), Js('Egna'), Js('Elvo'), Js('Enni'), Js('Epi'), Js('Epidi'), Js('Epo'), Js('Eras'), Js('Eudo'), Js('Fa'), Js('Fal'), Js('Faus'), Js('Fel'), Js('Fim'), Js('Flo'), Js('Flori'), Js('Frum'), Js('Gai'), Js('Gal'), Js('Gari'), Js('Gav'), Js('Gene'), Js('Glob'), Js('Gor'), Js('Gra'), Js('Grat'), Js('Hab'), Js('Hel'), Js('Hil'), Js('Hila'), Js('Hono'), Js('Hora'), Js('Horten'), Js('Igna'), Js('Ind'), Js('Inda'), Js('Isa'), Js('Ita'), Js('Lae'), Js('Laevi'), Js('Lin'), Js('Lucce'), Js('Luci'), Js('Lupi'), Js('Mac'), Js('Macri'), Js('Mal'), Js('Marce'), Js('Mau'), Js('Maur'), Js('Maxi'), Js('Mel'), Js('Merca'), Js('Mola'), Js('Mur'), Js('Muti'), Js('Nar'), Js('Nata'), Js('Naza'), Js('Neme'), Js('Numo'), Js('Octa'), Js('Octavi'), Js('Olym'), Js('Opi'), Js('Opti'), Js('Orien'), Js('Oro'), Js('Paet'), Js('Pali'), Js('Pan'), Js('Pap'), Js('Peta'), Js('Pho'), Js('Pos'), Js('Pota'), Js('Pro'), Js('Proc'), Js('Prota'), Js('Qua'), Js('Quen'), Js('Qui'), Js('Quin'), Js('Ram'), Js('Rami'), Js('Rece'), Js('Regi'), Js('Remi'), Js('Romul'), Js('Ruf'), Js('Sabe'), Js('Salvi'), Js('San'), Js('Sanc'), Js('Scri'), Js('Seve'), Js('Sim'), Js('Simp'), Js('Stra'), Js('Sul'), Js('Suli'), Js('Sur'), Js('Syl'), Js('Tan'), Js('Tani'), Js('Ter'), Js('Tib'), Js('Tibur'), Js('Tremo'), Js('Treni'), Js('Umbo'), Js('Ursi'), Js('Var'), Js('Vari'), Js('Veli'), Js('Veri'), Js('Vibi'), Js('Vic'), Js('Victo'), Js('Victri'), Js('Vita')]))
var.put('names4', Js([Js('cius'), Js('colus'), Js('culus'), Js('cus'), Js('das'), Js('donis'), Js('dos'), Js('dros'), Js('dus'), Js('gatus'), Js('gius'), Js('ion'), Js('lianus'), Js('lienus'), Js('lin'), Js('linus'), Js('lius'), Js('lus'), Js('mius'), Js('mus'), Js('nian'), Js('nianus'), Js('nion'), Js('nis'), Js('nius'), Js('nus'), Js('panus'), Js('raka'), Js('rian'), Js('ril'), Js('rinus'), Js('rius'), Js('scus'), Js('sis'), Js('so'), Js('tion'), Js('tis'), Js('tius'), Js('tumus'), Js('tus')]))
pass
pass


# Add lib to the module scope
turianNames = var.to_python()