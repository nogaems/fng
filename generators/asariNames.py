__all__ = ['asariNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
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
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd1')))+var.get('nm3').get(var.get('rnd2')))+Js(' '))+var.get('nm4').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ae'), Js('Ai'), Js('Aj'), Js('Al'), Js('Am'), Js('An'), Js('Ar'), Js('As'), Js('Ash'), Js('A'), Js('Ba'), Js('Bat'), Js('Ben'), Js('Be'), Js('Bi'), Js('Ce'), Js('Che'), Js('Cha'), Js('Ce'), Js('Da'), Js('De'), Js('Di'), Js('Ea'), Js('El'), Js('Em'), Js('En'), Js('Er'), Js('Fa'), Js('Fal'), Js('Fre'), Js('Ge'), Js('Gel'), Js('Gen'), Js('Gi'), Js('Gla'), Js('He'), Js('Hi'), Js('Hol'), Js('Ho'), Js('In'), Js('Ir'), Js('Im'), Js('Is'), Js('Ish'), Js('Esh'), Js('Es'), Js('Hal'), Js('Hel'), Js('Ja'), Js('Jal'), Js('Jan'), Js('Je'), Js('Jen'), Js('Jes'), Js('Ji'), Js('Jin'), Js('Jon'), Js('Jos'), Js('Ka'), Js('Kal'), Js('Kas'), Js('Kash'), Js('Kel'), Js('Ke'), Js('Kes'), Js('Ki'), Js('Kin'), Js('La'), Js('Le'), Js('Len'), Js('Let'), Js('Li'), Js('Lid'), Js('Lin'), Js('Lim'), Js('Lis'), Js('Lu'), Js('Luc'), Js('Ly'), Js('Lys'), Js('Lyn'), Js('Lym'), Js('Ma'), Js('Mal'), Js('May'), Js('Mir'), Js('Mi'), Js('Mo'), Js('Mor'), Js('My'), Js('Myr'), Js('Na'), Js('Nar'), Js('Nas'), Js('Ni'), Js('Nir'), Js('No'), Js('Nor'), Js('Nos'), Js('Nis'), Js('Nu'), Js('Nul'), Js('Num'), Js('Ny'), Js('Nyx'), Js('Myx'), Js('Pe'), Js('Pen'), Js('Pha'), Js('Phe'), Js('Pho'), Js('Po'), Js('Por'), Js('Pri'), Js('Ra'), Js('Ran'), Js('Rev'), Js('Ri'), Js('Ril'), Js('Sa'), Js('Sal'), Js('Sam'), Js('San'), Js('Sar'), Js('Sas'), Js('Sash'), Js('Se'), Js('Sel'), Js('Sey'), Js('Shi'), Js('Sha'), Js('She'), Js('Si'), Js('Sta'), Js('Su'), Js('Sul'), Js('Ta'), Js('Tal'), Js('Tar'), Js('Te'), Js('Tel'), Js('Tes'), Js('Tev'), Js('Tre'), Js('Un'), Js('Um'), Js('Us'), Js('Ush'), Js('Va'), Js('Val'), Js('Ve'), Js('Vey'), Js('Vi'), Js('Vis'), Js('Vo'), Js('Von'), Js('Xa'), Js('Xan'), Js('Ya'), Js('Ye'), Js('Ze'), Js('Zel'), Js('Zen'), Js('Zem')]))
var.put('nm2', Js([Js("'da"), Js("'ir"), Js("'ko"), Js("'li"), Js("'me"), Js("'mo"), Js("'na"), Js("'ne"), Js("'no"), Js("'phi"), Js("'ra"), Js("'sa"), Js("'sha"), Js("'ya"), Js('a'), Js('aki'), Js('al'), Js('an'), Js('ana'), Js('any'), Js('ar'), Js('ara'), Js('ari'), Js('arv'), Js('ass'), Js('ava'), Js('ay'), Js('edra'), Js('eem'), Js('een'), Js('ees'), Js('eez'), Js('eka'), Js('el'), Js('eld'), Js('ell'), Js('els'), Js('enth'), Js('er'), Js('es'), Js('ese'), Js('ess'), Js('est'), Js('et'), Js('ey'), Js('ez'), Js('ezi'), Js('fin'), Js('ga'), Js('i'), Js('ia'), Js('if'), Js('ife'), Js('il'), Js('in'), Js('ina'), Js('ira'), Js('is'), Js('iss'), Js('ith'), Js('ix'), Js('iy'), Js('iz'), Js('ler'), Js('li'), Js('lik'), Js('ly'), Js('me'), Js('oll'), Js('or'), Js('ora'), Js('os'), Js('ova'), Js('ra'), Js('ri'), Js('ry'), Js('tha'), Js('thy'), Js('uc'), Js('uci'), Js('ul'), Js('um'), Js('un'), Js('yr'), Js('yx'), Js('yxa'), Js('yxe')]))
var.put('nm3', Js([Js('a'), Js('da'), Js('e'), Js('es'), Js('ga'), Js('h'), Js('hin'), Js('ha'), Js('ir'), Js('is'), Js('ka'), Js('la'), Js('lea'), Js('ley'), Js('lia'), Js('ly'), Js('ma'), Js('me'), Js('mea'), Js('mey'), Js('mia'), Js('na'), Js('ne'), Js('nea'), Js('nia'), Js('ny'), Js('o'), Js('phea'), Js('phia'), Js('ra'), Js('rae'), Js('sa'), Js('se'), Js('sha'), Js('shi'), Js('sy'), Js('ta'), Js('te'), Js('tea'), Js('thea'), Js('thia'), Js('tia'), Js('u'), Js('us'), Js('ux'), Js('vi'), Js('ya'), Js('ze'), Js('zea'), Js('zia'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('Arte'), Js('Ate'), Js('Atru'), Js('Ave'), Js('Be'), Js('Ca'), Js('Cale'), Js('Cali'), Js('Coni'), Js('Corli'), Js("D'a"), Js("D'bie"), Js("D'cori"), Js("D'ky"), Js("D'la"), Js("D'lina"), Js("D'na"), Js("D'ra"), Js("D'ria"), Js("D'ro"), Js("D'rone"), Js("D've"), Js("D'yse"), Js('Da'), Js('Dali'), Js('Danti'), Js('Di'), Js('Ditri'), Js('Dri'), Js('Eda'), Js('Edo'), Js('Ga'), Js('Gade'), Js('He'), Js('Heli'), Js('Ia'), Js('Ialli'), Js('Ie'), Js('Iessa'), Js('Iessi'), Js('Ja'), Js('Jani'), Js('Janni'), Js('Jannu'), Js('Janu'), Js('Ke'), Js('Ky'), Js('Kya'), Js('Le'), Js('Leda'), Js('Li'), Js('Lo'), Js("M'cry"), Js("M'do"), Js("M'ja"), Js("M'ki"), Js("M'kya"), Js("M'lio"), Js("M'lo"), Js("M'pri"), Js("M'ta"), Js("M'to"), Js('Ma'), Js('Mai'), Js('Make'), Js('Mato'), Js('Me'), Js('Mere'), Js('Mi'), Js('Mo'), Js('Mora'), Js('Mu'), Js('Mura'), Js('My'), Js('Myra'), Js('No'), Js('Nura'), Js('Pe'), Js('Pesa'), Js('Pra'), Js('Ra'), Js('Radi'), Js('Ru'), Js('Sa'), Js('Sabu'), Js('Se'), Js('Sede'), Js('Sha'), Js('Shi'), Js('Ska'), Js("T'ne"), Js("T'da"), Js("T'do"), Js("T'ea"), Js("T'er"), Js("T'es"), Js("T'go"), Js("T'ha"), Js("T'ka"), Js("T'ke"), Js("T'lo"), Js("T'me"), Js("T'mi"), Js("T'mo"), Js("T'na"), Js("T'ne"), Js("T'pe"), Js("T'ra"), Js("T'rao"), Js("T're"), Js("T'sa"), Js("T'sca"), Js("T'so"), Js("T'va"), Js("T've"), Js("T'ze"), Js('tha'), Js('thani'), Js('thano'), Js("V'cri"), Js("V'do"), Js("V'la"), Js("V'mo"), Js("V'na"), Js("V'ti"), Js('Va')]))
var.put('nm5', Js([Js('ala'), Js('ana'), Js('ara'), Js('ari'), Js('ava'), Js('buro'), Js('ci'), Js('do'), Js('dri'), Js('eri'), Js('fi'), Js('ios'), Js('is'), Js('ius'), Js('ix'), Js('jah'), Js('jin'), Js('la'), Js('las'), Js('li'), Js('lis'), Js('lyt'), Js('mi'), Js('na'), Js('ni'), Js('nis'), Js('nus'), Js('or'), Js('ora'), Js('os'), Js('qua'), Js('ra'), Js('ran'), Js('re'), Js('rev'), Js('ri'), Js('ria'), Js('ris'), Js('rix'), Js('ro'), Js('ros'), Js('rus'), Js('san'), Js('sava'), Js('se'), Js('shi'), Js('si'), Js('sir'), Js('sus'), Js('tari'), Js('te'), Js('tis'), Js('to'), Js('tora'), Js('us'), Js('va'), Js('ve'), Js('vius'), Js('vo'), Js('vus'), Js('yma'), Js('yne'), Js('za'), Js('ze'), Js('zea'), Js('zor')]))
pass
pass


# Add lib to the module scope
asariNames = var.to_python()