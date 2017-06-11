__all__ = ['starTrekFerengi']

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
var.put('nm1', Js([Js('Aba'), Js('Adre'), Js('Aga'), Js('Arga'), Js('Arri'), Js('Ba'), Js('Be'), Js('Belo'), Js('Beri'), Js('Bo'), Js('Bra'), Js('Bre'), Js('Broi'), Js('Bru'), Js('Da'), Js('De'), Js('Di'), Js('Do'), Js('Dra'), Js('Dre'), Js('Droi'), Js('Fa'), Js('Fale'), Js('Fare'), Js('Fna'), Js('Fra'), Js('Fre'), Js('Fri'), Js('Froo'), Js('Ga'), Js('Gai'), Js('Ge'), Js('Gegi'), Js('Gi'), Js('Gla'), Js('Gna'), Js('Go'), Js('Gora'), Js('Gra'), Js('Gri'), Js('Groo'), Js('Ha'), Js('Hai'), Js('Ho'), Js('Hoe'), Js('Hora'), Js('Hra'), Js('Iga'), Js('Ige'), Js('Ira'), Js('Iro'), Js('Ita'), Js('Ka'), Js('Kara'), Js('Kay'), Js('Kaza'), Js('Ke'), Js('Ki'), Js('Kola'), Js('Kra'), Js('Kre'), Js('Kri'), Js('La'), Js('Le'), Js('Lera'), Js('Lete'), Js('Li'), Js('Lo'), Js('Lu'), Js('Luri'), Js('Ma'), Js('Mala'), Js('Maza'), Js('Mo'), Js('Mona'), Js('Mora'), Js('Mu'), Js('Na'), Js('Nala'), Js('Nazra'), Js('Nera'), Js('Ni'), Js('Nibo'), Js('Nilra'), Js('No'), Js('Nu'), Js('Ola'), Js('Ona'), Js('Ora'), Js('Orda'), Js('Orpa'), Js('Oza'), Js('Pa'), Js('Pela'), Js('Pera'), Js('Pi'), Js('Ple'), Js('Pra'), Js('Ra'), Js('Rate'), Js('Raza'), Js('Re'), Js('Rha'), Js('Ro'), Js('Rotto'), Js('Ruta'), Js('Sa'), Js('Smee'), Js('So'), Js('Solo'), Js('Sova'), Js('Sra'), Js('Sto'), Js('Sura'), Js('Ta'), Js('Tega'), Js('To'), Js('Torro'), Js('Toza'), Js('Tra'), Js('Tro'), Js('Tu'), Js('Turo'), Js('Tye'), Js('Ubo'), Js('Ugro'), Js('Ulda'), Js('Uli'), Js('Ura'), Js('Uro'), Js('Ya'), Js('Yaza'), Js('Ye'), Js('Yna'), Js('Yora'), Js('Za'), Js('Ze'), Js('Zira'), Js('Zra'), Js('Zyla')]))
var.put('nm2', Js([Js('ba'), Js('bac'), Js('bar'), Js('bor'), Js('c'), Js('car'), Js('ck'), Js('ctor'), Js('d'), Js('dac'), Js('dok'), Js('dor'), Js('g'), Js('ga'), Js('gg'), Js('ggie'), Js('gis'), Js('go'), Js('k'), Js('ka'), Js('kag'), Js('kor'), Js('l'), Js('la'), Js('ldar'), Js('lis'), Js('lok'), Js('lva'), Js('m'), Js('mag'), Js('mp'), Js('mra'), Js('n'), Js('nk'), Js('no'), Js('nog'), Js('nt'), Js('nzo'), Js('p'), Js('pak'), Js('pax'), Js('pum'), Js('rad'), Js('rbo'), Js('rik'), Js('rin'), Js('ron'), Js('rot'), Js('rpax'), Js('rr'), Js('rrot'), Js('rta'), Js('s'), Js('sax'), Js('sh'), Js('ss'), Js('t'), Js('ta'), Js('tax'), Js('tek'), Js('va'), Js('vag'), Js('vak'), Js('var'), Js('xa'), Js('xac'), Js('xon'), Js('xor'), Js('za'), Js('zar'), Js('zig'), Js('zoc')]))
var.put('nm3', Js([Js('A'), Js('Ai'), Js('Ali'), Js('Ana'), Js('Ara'), Js('Be'), Js('Bee'), Js('Bela'), Js('Bia'), Js('Bira'), Js('Bli'), Js('Bo'), Js('Bona'), Js('Bre'), Js('Da'), Js('De'), Js('Dera'), Js('Dia'), Js('Dina'), Js('Do'), Js('Dri'), Js('Fa'), Js('Fe'), Js('Fena'), Js('Fesa'), Js('Fhi'), Js('Fi'), Js('Fia'), Js('Fira'), Js('Ga'), Js('Gase'), Js('Ge'), Js('Gela'), Js('Geli'), Js('Ghe'), Js('Gi'), Js('Gine'), Js('Gira'), Js('Giya'), Js('Gre'), Js('Gri'), Js('Hela'), Js('Hena'), Js('Hi'), Js('Hia'), Js('Hy'), Js('Hyra'), Js('I'), Js('Ina'), Js('Ira'), Js('Iro'), Js('Isa'), Js('Ka'), Js('Ke'), Js('Keha'), Js('Kella'), Js('Kena'), Js('Ki'), Js('Kia'), Js('Kisa'), Js('Kora'), Js('Kre'), Js('La'), Js('Le'), Js('Lera'), Js('Leya'), Js('Li'), Js('Lina'), Js('Losa'), Js('Ma'), Js('Mane'), Js('Me'), Js('Mero'), Js('Mi'), Js('Mia'), Js('Mo'), Js('Nala'), Js('Ne'), Js('Nema'), Js('Nemo'), Js('Nia'), Js('Nira'), Js('No'), Js('Noa'), Js('Nosi'), Js('O'), Js('Ole'), Js('One'), Js('Ora'), Js('Ori'), Js('Oza'), Js('Pa'), Js('Pe'), Js('Peha'), Js('Phi'), Js('Poli'), Js('Pri'), Js('Re'), Js('Rema'), Js('Rena'), Js('Ri'), Js('Ria'), Js('Rika'), Js('Rosa'), Js('Roxe'), Js('Sa'), Js('Sela'), Js('Seno'), Js('Sha'), Js('Si'), Js('Sira'), Js('Sra'), Js('Sti'), Js('Ta'), Js('Te'), Js('Tewa'), Js('Teza'), Js('Thi'), Js('Tia'), Js('Tila'), Js('Tiro'), Js('To'), Js('Tona'), Js('U'), Js('Ula'), Js('Uni'), Js('Ure'), Js('Uye'), Js('Uza'), Js('Ya'), Js('Yala'), Js('Ye'), Js('Yne'), Js('Yra'), Js('Zane'), Js('Ze'), Js('Zeri'), Js('Zia')]))
var.put('nm4', Js([Js('ba'), Js('bel'), Js('bis'), Js('bora'), Js('ca'), Js('cera'), Js('cine'), Js('cis'), Js('d'), Js('de'), Js('del'), Js('dis'), Js('ga'), Js('gel'), Js('gela'), Js('gena'), Js('gis'), Js('gora'), Js('k'), Js('kera'), Js('kia'), Js('kis'), Js('l'), Js('le'), Js('lea'), Js('lera'), Js('lina'), Js('ll'), Js('me'), Js('mera'), Js('mis'), Js('miya'), Js('n'), Js('ne'), Js('nia'), Js('nka'), Js('nni'), Js('no'), Js('pe'), Js('phi'), Js('pia'), Js('pora'), Js('r'), Js('re'), Js('res'), Js('reya'), Js('ri'), Js('ris'), Js('rles'), Js('rni'), Js('rona'), Js('rra'), Js('s'), Js('se'), Js('sh'), Js('sha'), Js('shi'), Js('shka'), Js('si'), Js('ta'), Js('the'), Js('ti'), Js('tis'), Js('va'), Js('vena'), Js('vil'), Js('vira'), Js('xaia'), Js('xen'), Js('xera'), Js('xi'), Js('zel'), Js('zenna'), Js('zera')]))
pass
pass


# Add lib to the module scope
starTrekFerengi = var.to_python()