__all__ = ['chaosNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names4', 'names2', 'nameGen', 'names3'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('names', (var.get('names3').get(var.get('rnd'))+var.get('names4').get(var.get('rnd2'))))
            else:
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
var.put('names1', Js([Js('Aba'), Js('Abru'), Js('Ahru'), Js('An'), Js('Anta'), Js('Anu'), Js('Ar'), Js('Ara'), Js('As'), Js('Azu'), Js('Ba'), Js('Balta'), Js('Barba'), Js('Bero'), Js('Bru'), Js('Bulda'), Js('Burro'), Js('Caorpu'), Js('Chen'), Js('Cru'), Js('Dav'), Js('Dema'), Js('Dev'), Js('Drach'), Js('Dy'), Js('Eku'), Js('Ela'), Js('Ely'), Js('En'), Js('Ere'), Js('Esto'), Js('Ez'), Js('Far'), Js('Fester'), Js('Fu'), Js('Fur'), Js('Furi'), Js('Gal'), Js('Gara'), Js('Goul'), Js('Graza'), Js('Gu'), Js('Gura'), Js('Hala'), Js('He'), Js('Hez'), Js('Hon'), Js('Hou'), Js('Ingu'), Js('Ji'), Js('Juru'), Js('Ka'), Js('Kal'), Js('Kasso'), Js('Kaz'), Js('Kha'), Js('Khro'), Js('Kraa'), Js('Kre'), Js('Ku'), Js('Kur'), Js('Kurna'), Js('Ky'), Js('Lo'), Js('Lu'), Js('Ma'), Js('Mal'), Js('Mephi'), Js('Mo'), Js('Morde'), Js('Morte'), Js('Nazu'), Js('Neme'), Js('Omphu'), Js('Onai'), Js('Parge'), Js('Pho'), Js('Pu'), Js('Puri'), Js('Rha'), Js('Rhy'), Js('Ro'), Js('Ru'), Js('Sathu'), Js('Sava'), Js('Sek'), Js('Si'), Js('Sky'), Js('Svo'), Js('Ta'), Js('Talo'), Js('Tita'), Js('Tu'), Js('Urka'), Js('Urkra'), Js('Urla'), Js('Var'), Js('Vu'), Js('Yga'), Js('Za'), Js('Zho'), Js('Zhu'), Js('Zy')]))
var.put('names2', Js([Js("'gaz"), Js("'gom"), Js("'khar"), Js("'loth"), Js("'lumin"), Js("'palos"), Js("'ryon"), Js("'sax"), Js("'tiro"), Js("'tzor"), Js('ban'), Js('bar'), Js('bas'), Js('bhor'), Js('bire'), Js('bus'), Js('cius'), Js('daran'), Js('das'), Js('dax'), Js('dekai'), Js('del'), Js('diaz'), Js('dire'), Js('don'), Js('dred'), Js('duk'), Js('far'), Js('gan'), Js('gar'), Js('garr'), Js('gax'), Js('ghast'), Js('gon'), Js('gor'), Js('gore'), Js('gral'), Js('grim'), Js('harr'), Js('kai'), Js('khar'), Js('kos'), Js('las'), Js('lash'), Js('lax'), Js('laz'), Js('lek'), Js('lock'), Js('mek'), Js('min'), Js('mon'), Js('mor'), Js('mort'), Js('mus'), Js('nacus'), Js('naer'), Js('nath'), Js('nax'), Js('neus'), Js('nogar'), Js('nok'), Js('non'), Js('nux'), Js('phoz'), Js('phus'), Js('pulax'), Js('rah'), Js('rak'), Js('ram'), Js('rand'), Js('rass'), Js('rath'), Js('rax'), Js('raz'), Js('rhaz'), Js('rion'), Js('ritus'), Js('rolath'), Js('ron'), Js('roq'), Js('ross'), Js('roth'), Js('routh'), Js('roz'), Js('rulak'), Js('ruman'), Js('rus'), Js('salax'), Js('sour'), Js('stix'), Js('stur'), Js('thac'), Js('thal'), Js('thor'), Js('thral'), Js('toth'), Js('trax'), Js('trius'), Js('vax'), Js('vile'), Js('xus'), Js('zar')]))
var.put('names3', Js([Js('Abi'), Js('Abre'), Js('Aer'), Js('Ahnu'), Js('An'), Js('Ana'), Js('Ara'), Js('Arhi'), Js('As'), Js('Azu'), Js('Ba'), Js('Bala'), Js('Beldi'), Js('Belo'), Js('Berba'), Js('Berro'), Js('Bri'), Js('Cari'), Js('Ches'), Js('Cry'), Js('Dema'), Js('Dev'), Js('Div'), Js('Dresh'), Js('Dy'), Js('Eki'), Js('Ela'), Js('Ely'), Js('En'), Js('Ene'), Js('Esta'), Js('Ez'), Js('Fer'), Js('Ferri'), Js('Fes'), Js('Fihr'), Js('Fy'), Js('Gal'), Js('Gaya'), Js('Gi'), Js('Gira'), Js('Gol'), Js('Grisa'), Js('He'), Js('Hela'), Js('Hen'), Js('Hez'), Js('Hoa'), Js('Inge'), Js('Ji'), Js('Jura'), Js('Ka'), Js('Kaha'), Js('Kashu'), Js('Ke'), Js('Kel'), Js('Kez'), Js('Khaa'), Js('Khry'), Js('Kir'), Js('Korna'), Js('Kre'), Js('Ky'), Js('Li'), Js('Lo'), Js('Ma'), Js('Mel'), Js('Mephi'), Js('Mo'), Js('Morde'), Js('More'), Js('Nasu'), Js('Neme'), Js('Oni'), Js('Ophu'), Js('Perge'), Js('Pho'), Js('Pi'), Js('Puri'), Js('Rhia'), Js('Rhy'), Js('Ro'), Js('Ry'), Js('Sehk'), Js('Sephu'), Js('Shi'), Js('Sio'), Js('Siva'), Js('Ski'), Js('Telo'), Js('Tha'), Js('Tiya'), Js('Tu'), Js('Una'), Js('Ura'), Js('Urli'), Js('Ver'), Js('Vu'), Js('Ya'), Js('Za'), Js('Zho'), Js('Zoe'), Js('Zy')]))
var.put('names4', Js([Js("'gah"), Js("'ginn"), Js("'khas"), Js("'lith"), Js("'lumix"), Js("'phis"), Js("'rya"), Js("'sax"), Js("'tira"), Js("'yah"), Js('bara'), Js('bess'), Js('bhox'), Js('bine'), Js('bis'), Js('bise'), Js('cian'), Js('darah'), Js('dash'), Js('dea'), Js('dehk'), Js('dell'), Js('dex'), Js('diaz'), Js('dine'), Js('dresh'), Js('dynn'), Js('faer'), Js('gaer'), Js('gash'), Js('genn'), Js('gihr'), Js('gone'), Js('goye'), Js('grell'), Js('grine'), Js('grinn'), Js('gwer'), Js('hirr'), Js('kei'), Js('kha'), Js('kiz'), Js('lashe'), Js('leck'), Js('lek'), Js('less'), Js('lix'), Js('liz'), Js('mex'), Js('mine'), Js('mona'), Js('mora'), Js('morta'), Js('muse'), Js('naere'), Js('neon'), Js('nesh'), Js('neth'), Js('neuth'), Js('nihx'), Js('nix'), Js('nosa'), Js('nu'), Js('phis'), Js('pho'), Js('prix'), Js('rane'), Js('raz'), Js('reah'), Js('renne'), Js('reon'), Js('resh'), Js('ress'), Js('rhazi'), Js('rilith'), Js('rique'), Js('riss'), Js('rith'), Js('riyes'), Js('riz'), Js('rothe'), Js('roush'), Js('roze'), Js('rumine'), Js('ruse'), Js('ruxa'), Js('ryn'), Js('silix'), Js('sou'), Js('sty'), Js('styxe'), Js('thall'), Js('thess'), Js('thia'), Js('this'), Js('tosh'), Js('triesh'), Js('trix'), Js('vie'), Js('vix'), Js('xis'), Js('zara')]))
pass
pass


# Add lib to the module scope
chaosNames = var.to_python()