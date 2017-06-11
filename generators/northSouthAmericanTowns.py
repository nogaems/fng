__all__ = ['northSouthAmericanTowns']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(12.0)):
        try:
            if (var.get('i')<Js(2.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', (var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                            var.put('names', (var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2'))))
                        else:
                            if (var.get('i')<Js(10.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                                var.put('names', (var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2'))))
                            else:
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                                var.put('names', (var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aca'), Js('Agua'), Js('Agu'), Js('Anda'), Js('Anse'), Js('Anser'), Js('Apa'), Js('Apar'), Js('Ara'), Js('Araca'), Js('Arau'), Js('Ari'), Js('Aya'), Js('Ba'), Js('Bara'), Js('Bar'), Js('Barra'), Js('Barran'), Js('Bela'), Js('Bo'), Js('Bogo'), Js('Buca'), Js('Buena'), Js('Bu'), Js('Cucu'), Js('Cai'), Js('Cúcu'), Js('Ca'), Js('Cahi'), Js('Cala'), Js('Cal'), Js('Can'), Js('Cande'), Js('Care'), Js('Carta'), Js('Cau'), Js('Cauca'), Js('Ce'), Js('Cere'), Js('Cha'), Js('Chapa'), Js('Chi'), Js('Chigo'), Js('Cié'), Js('Ciéna'), Js('Chiqui'), Js('Coro'), Js('Curu'), Js('Dui'), Js('El Ba'), Js('El Ca'), Js('El Car'), Js('El Ce'), Js('El Cer'), Js('El Cha'), Js('El Char'), Js('Envi'), Js('Espi'), Js('Fa'), Js('Faca'), Js('Fla'), Js('Flan'), Js('Flo'), Js('Fon'), Js('Fre'), Js('Fres'), Js('Fu'), Js('Fun'), Js('Fusa'), Js('Gala'), Js('Gar'), Js('Gi'), Js('Gira'), Js('Gra'), Js('Grana'), Js('Gua'), Js('Hon'), Js('Iba'), Js('Ipia'), Js('Ita'), Js('Ja'), Js('Jamu'), Js('Léri'), Js('Lé'), Js('La Ce'), Js('La Do'), Js('La Dira'), Js('La Me'), Js('La Pla'), Js('Leti'), Js('Lori'), Js('Mála'), Js('Maga'), Js('Mai'), Js('Mala'), Js('Malam'), Js('Mani'), Js('Mari'), Js('Mede'), Js('Medel'), Js('Mel'), Js('Mo'), Js('Mom'), Js('Mora'), Js('Mos'), Js('Muni'), Js('Nei'), Js('Oca'), Js('Pal'), Js('Pam'), Js('Pa'), Js('Perei'), Js('Piede'), Js('Pita'), Js('Pivi'), Js('Popa'), Js('Pra'), Js('Qui'), Js('Quim'), Js('Rio'), Js('Rol'), Js('Sa'), Js('Saba'), Js('Saha'), Js('Sala'), Js('Sam'), Js('Sego'), Js('Sevi'), Js('Siba'), Js('Sin'), Js('Soa'), Js('Soco'), Js('Soga'), Js('Sole'), Js('Son'), Js('Túque'), Js('Tierra'), Js('To'), Js('Tuma'), Js('Tun'), Js('Tur'), Js('Uba'), Js('Yaru'), Js('Yopa'), Js('Yum'), Js('Zara'), Js('Zar'), Js('Zipa')]))
var.put('nm2', Js([Js('bano'), Js('baya'), Js('bosa'), Js('cá'), Js('cías'), Js('ca'), Js('cao'), Js('carí'), Js('cas'), Js('casia'), Js('cazar'), Js('chica'), Js('chiná'), Js('ción'), Js('co'), Js('coa'), Js('cuta'), Js('dó'), Js('da'), Js('das'), Js('dera'), Js('donia'), Js('dot'), Js('ga'), Js('gado'), Js('gar'), Js('gena'), Js('gotá'), Js('gre'), Js('gué'), Js('guaní'), Js('jicá'), Js('jona'), Js('kesquera'), Js('laga'), Js('lapa'), Js('larcá'), Js('laria'), Js('les'), Js('li'), Js('lito'), Js('lona'), Js('ma'), Js('maní'), Js('manga'), Js('mar'), Js('meja'), Js('men'), Js('menia'), Js('mina'), Js('mira'), Js('ná'), Js('ní'), Js('nada'), Js('naga'), Js('nal'), Js('neta'), Js('nilla'), Js('no'), Js('noa'), Js('pel'), Js('quilla'), Js('quirá'), Js('quite'), Js('rá'), Js('ría'), Js('rón'), Js('ral'), Js('ranoa'), Js('repa'), Js('reté'), Js('rida'), Js('rito'), Js('rodó'), Js('seca'), Js('suga'), Js('tá'), Js('té'), Js('tín'), Js('taca'), Js('tadó'), Js('tago'), Js('tivá'), Js('vá'), Js('va'), Js('zón'), Js('zal'), Js('zales')]))
var.put('nm3', Js([Js('Al'), Js('Alau'), Js('Alfre'), Js('Am'), Js('Amba'), Js('Archi'), Js('Atu'), Js('Atun'), Js('Azo'), Js('Ba'), Js('Bal'), Js('Bo'), Js('Ca'), Js('Cal'), Js('Caria'), Js('Cata'), Js('Caya'), Js('Ce'), Js('Celi'), Js('Cho'), Js('Co'), Js('Coli'), Js('Coro'), Js('Cota'), Js('Cue'), Js('Cuen'), Js('Es'), Js('Esme'), Js('Gua'), Js('Guala'), Js('Guara'), Js('Guaran'), Js('Guaya'), Js('Hua'), Js('Huaqui'), Js('Iba'), Js('Jipi'), Js('Lata'), Js('Lla'), Js('Lo'), Js('Loma'), Js('Ma'), Js('Maca'), Js('Macha'), Js('Man'), Js('Mon'), Js('Monta'), Js('Monte'), Js('Mui'), Js('Muis'), Js('Na'), Js('Nara'), Js('Naran'), Js('Nul'), Js('Ota'), Js('Otava'), Js('Pí'), Js('Píl'), Js('Pi'), Js('Pima'), Js('Pimam'), Js('Pla'), Js('Por'), Js('Pu'), Js('Puji'), Js('Que'), Js('Qui'), Js('Rio'), Js('Roca'), Js('Sa'), Js('Sali'), Js('Sam'), Js('Sambo'), Js('Sango'), Js('Saqui'), Js('Su'), Js('Te'), Js('Tosa'), Js('Tul'), Js('Tuta'), Js('Tutama'), Js('Val'), Js('Vela'), Js('Ven'), Js('Venta'), Js('Vin'), Js('Ya'), Js('Yagua'), Js('Yan'), Js('Za'), Js('Zamo'), Js('Zaru')]))
var.put('nm4', Js([Js('ñar'), Js('ños'), Js('bamba'), Js('bato'), Js('cúa'), Js('cachi'), Js('cao'), Js('cará'), Js('ceo'), Js('ces'), Js('ceta'), Js('chachi'), Js('chala'), Js('chi'), Js('co'), Js('cocha'), Js('cristi'), Js('cunga'), Js('dez'), Js('dona'), Js('fuerte'), Js('gua'), Js('gues'), Js('hía'), Js('hoyo'), Js('jal'), Js('jan'), Js('japa'), Js('jito'), Js('láo'), Js('laceo'), Js('laro'), Js('las'), Js('leo'), Js('lica'), Js('limes'), Js('linas'), Js('lora'), Js('manga'), Js('mayo'), Js('mora'), Js('na'), Js('nales'), Js('nas'), Js('ne'), Js('nel'), Js('no'), Js('piro'), Js('que'), Js('qui'), Js('quil'), Js('quillas'), Js('quiza'), Js('ra'), Js('rama'), Js('randa'), Js('rate'), Js('riel'), Js('ruma'), Js('sí'), Js('saje'), Js('sti'), Js('ta'), Js('tanas'), Js('taqui'), Js('tina'), Js('to'), Js('valo'), Js('vedo'), Js('velo'), Js('viejo'), Js('yo'), Js('zaza')]))
var.put('nm5', Js([Js('Akou'), Js('Ali'), Js('Apa'), Js('Awa'), Js('Bé'), Js('Béli'), Js('Be'), Js('Ca'), Js('Camo'), Js('Cau'), Js('Caye'), Js('Ci'), Js('Clé'), Js('Cor'), Js('Cormo'), Js('Cormon'), Js('Cou'), Js('Dé'), Js('Déli'), Js('Gui'), Js('Guisa'), Js('Guisan'), Js('Ira'), Js('Iracou'), Js('Ja'), Js('Javou'), Js('Ka'), Js('Kou'), Js('Ma'), Js('Macou'), Js('Mal'), Js('Malma'), Js('Mari'), Js('Matou'), Js('Mon'), Js('Os'), Js('Oua'), Js('Ouana'), Js('Ré'), Js('Régi'), Js('Rémi'), Js('Ro'), Js('Rocha'), Js('Rocham'), Js('Sau'), Js('Si'), Js('Sin'), Js('Sinna'), Js('To'), Js('Tona'), Js('Tonné')]))
var.put('nm6', Js([Js('beau'), Js('bo'), Js('cao'), Js('car'), Js('ces'), Js('coto'), Js('coubo'), Js('gina'), Js('hey'), Js('la'), Js('lices'), Js('lor'), Js('mary'), Js('ment'), Js('mire'), Js('mopi'), Js('néry'), Js('na'), Js('nary'), Js('nate'), Js('naye'), Js('ne'), Js('noury'), Js('nue'), Js('pi'), Js('qui'), Js('ra'), Js('re'), Js('ria'), Js('ron'), Js('rou'), Js('ry'), Js('sinéry'), Js('soula'), Js('te'), Js('tière'), Js('ti'), Js('tibo'), Js('to'), Js('tou'), Js('toury'), Js('venue'), Js('w'), Js('x'), Js('ye'), Js('zon')]))
var.put('nm7', Js([Js('Ai'), Js('Aisha'), Js('Aishal'), Js('An'), Js('Apo'), Js('Ara'), Js('Araka'), Js('Ari'), Js('Ba'), Js('Bara'), Js('Bi'), Js('Bilo'), Js('Bu'), Js('Bur'), Js('Bux'), Js('En'), Js('Enmo'), Js('He'), Js('Hele'), Js('Ho'), Js('Hol'), Js('Hoso'), Js('Im'), Js('Imbai'), Js('Is'), Js('Ish'), Js('Ishe'), Js('Isher'), Js('Issa'), Js('Isse'), Js('Itha'), Js('Ka'), Js('Kal'), Js('Kama'), Js('Kami'), Js('Kan'), Js('Kanga'), Js('Kar'), Js('Kewei'), Js('Ko'), Js('Koria'), Js('Ku'), Js('Kuru'), Js('Kwa'), Js('Leo'), Js('Li'), Js('Lu'), Js('Lusi'), Js('Ma'), Js('Maba'), Js('Mabu'), Js('Mah'), Js('Mahai'), Js('Makou'), Js('Mo'), Js('Mora'), Js('Moru'), Js('Orea'), Js('Ori'), Js('Orin'), Js('Re'), Js('Save'), Js('Su'), Js('Sura'), Js('Ta'), Js('Taka'), Js('Towa'), Js('Tuma'), Js('Tume'), Js('Wa'), Js('Wan'), Js('Wi'), Js('Wicha')]))
var.put('nm8', Js([Js('bai'), Js('bo'), Js('bura'), Js('ca'), Js('daal'), Js('dai'), Js('dia'), Js('die'), Js('garuma'), Js('gek'), Js('haica'), Js('ka'), Js('kaima'), Js('kaka'), Js('kama'), Js('kari'), Js('kouria'), Js('ku'), Js('kuni'), Js('kusa'), Js('kwani'), Js('la'), Js('lena'), Js('loku'), Js('ma'), Js('madai'), Js('mia'), Js('mita'), Js('more'), Js('mu'), Js('na'), Js('nai'), Js('nan'), Js('neru'), Js('ni'), Js('no'), Js('nora'), Js('pukari'), Js('ra'), Js('rama'), Js('rang'), Js('re'), Js('reng'), Js('retik'), Js('ri'), Js('ria'), Js('riabo'), Js('rika'), Js('ro'), Js('roro'), Js('ru'), Js('ruca'), Js('ruma'), Js('sa'), Js('sano'), Js('sie'), Js('signan'), Js('ta'), Js('taro'), Js('teri'), Js('tik'), Js('ton'), Js('tuni'), Js('wa'), Js('weigek'), Js('whanna')]))
var.put('nm9', Js([Js('Abe'), Js('Abena'), Js('Abenas'), Js('Aca'), Js('Acari'), Js('Al'), Js('Albi'), Js('Ana'), Js('Ape'), Js('Apoe'), Js('Au'), Js('Auro'), Js('Ba'), Js('Bata'), Js('Ben'), Js('Bi'), Js('Bita'), Js('Bo'), Js('Boto'), Js('Bro'), Js('Broko'), Js('Co'), Js('Cor'), Js('Corne'), Js('Cot'), Js('Dju'), Js('Go'), Js('Ka'), Js('Kaja'), Js('Kwa'), Js('Kwakoe'), Js('Kwama'), Js('Le'), Js('Lebi'), Js('Lely'), Js('Moe'), Js('Moen'), Js('Pa'), Js('Para'), Js('Pe'), Js('Pele'), Js('Po'), Js('Poki'), Js('Pon'), Js('To'), Js('Tot'), Js('Wa'), Js('Wage'), Js('Wan'), Js('Wanha'), Js('Washo')]))
var.put('nm10', Js([Js('bo'), Js('ca'), Js('da'), Js('do'), Js('doti'), Js('dre'), Js('gen'), Js('go'), Js('gron'), Js('hatti'), Js('jana'), Js('ke'), Js('koegron'), Js('lelu'), Js('lu'), Js('mu'), Js('mutu'), Js('na'), Js('nam'), Js('naston'), Js('ness'), Js('ny'), Js('paike'), Js('pasi'), Js('pondo'), Js('pu'), Js('ra'), Js('ranam'), Js('ribo'), Js('rie'), Js('rora'), Js('samutu'), Js('shoda'), Js('si'), Js('tavia'), Js('ti'), Js('tica'), Js('tina'), Js('toe'), Js('toetoe'), Js('ton'), Js('tu'), Js('via')]))
var.put('nm11', Js([Js('Aca'), Js('Acari'), Js('Alta'), Js('Ana'), Js('Arau'), Js('Bar'), Js('Barce'), Js('Bari'), Js('Barqui'), Js('Baru'), Js('Ca'), Js('Cabi'), Js('Cala'), Js('Can'), Js('Cantau'), Js('Carú'), Js('Cara'), Js('Caraba'), Js('Caro'), Js('Carri'), Js('Cau'), Js('Cauca'), Js('Cha'), Js('Chara'), Js('Chi'), Js('Chichi'), Js('Ciu'), Js('Civa'), Js('Co'), Js('Cuma'), Js('Eji'), Js('El Ca'), Js('El Dia'), Js('El Ha'), Js('El Lim'), Js('El Ti'), Js('El To'), Js('El Tocu'), Js('El Vi'), Js('Güi'), Js('Gua'), Js('Guaca'), Js('Guana'), Js('Guare'), Js('Guas'), Js('Guati'), Js('Lagu'), Js('Mé'), Js('Méri'), Js('Mai'), Js('Maique'), Js('Mara'), Js('Maria'), Js('Matu'), Js('Mo'), Js('Mucu'), Js('Mucum'), Js('Ni'), Js('Ocu'), Js('Peta'), Js('Por'), Js('Porla'), Js('Quí'), Js('Ru'), Js('Tá'), Js('Tári'), Js('Ta'), Js('Taca'), Js('Tacari'), Js('Ti'), Js('Tina'), Js('Tuca'), Js('Tucu'), Js('Tur'), Js('Upa'), Js('Vale'), Js('Valen'), Js('Yari'), Js('Zara')]))
var.put('nm12', Js([Js('bio'), Js('bor'), Js('bozo'), Js('caibo'), Js('cao'), Js('cara'), Js('cas'), Js('cay'), Js('che'), Js('cia'), Js('co'), Js('coa'), Js('cuyo'), Js('do'), Js('güe'), Js('güito'), Js('gua'), Js('guita'), Js('jillo'), Js('lamar'), Js('lava'), Js('leda'), Js('lera'), Js('lito'), Js('lo'), Js('lona'), Js('maná'), Js('mare'), Js('mas'), Js('mero'), Js('meto'), Js('na'), Js('naco'), Js('nare'), Js('nas'), Js('nitas'), Js('pano'), Js('pita'), Js('piz'), Js('ques'), Js('quillo'), Js('rín'), Js('rón'), Js('ra'), Js('racas'), Js('racay'), Js('raure'), Js('raza'), Js('re'), Js('renas'), Js('ria'), Js('riara'), Js('riba'), Js('rida'), Js('rigua'), Js('rinas'), Js('rio'), Js('rita'), Js('rizal'), Js('rojos'), Js('ruta'), Js('simeto'), Js('ta'), Js('tagua'), Js('tal'), Js('tare'), Js('tas'), Js('taura'), Js('tia'), Js('tillo'), Js('tire'), Js('toria'), Js('var'), Js('viche'), Js('yana'), Js('za')]))
pass
pass


# Add lib to the module scope
northSouthAmericanTowns = var.to_python()