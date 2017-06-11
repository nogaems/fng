__all__ = ['elfTowns']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('A'), Js("A'"), Js('Af'), Js('Al'), Js('All'), Js('Aly'), Js('Am'), Js('Amy'), Js('An'), Js('Any'), Js('Ar'), Js('As'), Js('Ash'), Js('Asy'), Js('Ay'), Js('Ca'), Js('Cy'), Js('E'), Js("E'"), Js('Ef'), Js('El'), Js('Ell'), Js('Ely'), Js('Em'), Js('Emy'), Js('En'), Js('Eny'), Js('Er'), Js('Es'), Js('Esh'), Js('Esy'), Js('Ey'), Js('F'), Js('Fa'), Js('Fel'), Js('Fil'), Js('Fy'), Js('Fyl'), Js('Ga'), Js('Gal'), Js('Ha'), Js('He'), Js('Hy'), Js('I'), Js('If'), Js('Il'), Js('Ill'), Js('Ily'), Js('Im'), Js('Imy'), Js('In'), Js('Iny'), Js('Ir'), Js('Is'), Js('Ish'), Js('Isy'), Js('Iy'), Js('Ja'), Js('Ji'), Js('K'), Js('Ka'), Js('Ke'), Js('Ky'), Js('L'), Js('La'), Js('Le'), Js('Lel'), Js('Lil'), Js('Ly'), Js('Lyl'), Js('M'), Js('Ma'), Js('Math'), Js('Me'), Js('Mel'), Js('Mil'), Js('Mor'), Js('My'), Js('Myl'), Js('Myt'), Js('Myth'), Js('N'), Js('Na'), Js('Ne'), Js('Nel'), Js('Nil'), Js('Ny'), Js('Nyl'), Js('Nyt'), Js('Nyth'), Js('O'), Js("O'"), Js('Of'), Js('Ol'), Js('Oll'), Js('Oly'), Js('Om'), Js('Omy'), Js('On'), Js('Ony'), Js('Or'), Js('Os'), Js('Osh'), Js('Osy'), Js('Oy'), Js('Ra'), Js('Re'), Js('Ry'), Js('S'), Js('Sa'), Js('Sel'), Js('Sh'), Js('Sha'), Js('She'), Js('Shyl'), Js('Sil'), Js('Sy'), Js('Syl'), Js('Th'), Js('Tha'), Js('The'), Js('Thel'), Js('Thil'), Js('Thy'), Js('Thyl'), Js('U'), Js('Ul'), Js('Ull'), Js('Uly'), Js('Um'), Js('Umy'), Js('Un'), Js('Uny'), Js('Uy'), Js('W'), Js('Wa'), Js('We'), Js('Y'), Js("Y'"), Js('Ya'), Js('Ye'), Js('Yl'), Js('Yll')]))
var.put('nm2', Js([Js('al'), Js('el'), Js('en'), Js('an'), Js('ana'), Js('ena'), Js('aena'), Js('a'), Js('i'), Js('ren'), Js('ran'), Js('eth'), Js('ath'), Js('a'), Js('e'), Js('o'), Js('h'), Js('ha'), Js('he'), Js('ho'), Js('f'), Js('fa'), Js('fe'), Js('l'), Js('le'), Js('la'), Js('m'), Js('me'), Js('ma'), Js('ne'), Js('na'), Js('n'), Js('s'), Js('sa'), Js('se'), Js('ve'), Js('va')]))
var.put('nm3', Js([Js(' Aethel'), Js(' Aiqua'), Js(' Alari'), Js(' Alora'), Js(' Ancalen'), Js(' Anore'), Js(' Asari'), Js(' Dorei'), Js(' Dorthore'), Js(' Edhil'), Js(' Esari'), Js(' Lenora'), Js(' Serin'), Js(' Serine'), Js(' Shaeras'), Js(' Taesi'), Js(' Thalas'), Js(' Thalor'), Js(' Thalore'), Js(' Themar'), Js(' Tirion'), Js(' Unarith'), Js(' Belanore'), Js(' Caelora'), Js(' Nalore'), Js(' Entheas'), Js(' Ennore'), Js(' Elunore'), Js(' Allanar'), Js(' Ortheiad'), Js('bel'), Js('belle'), Js('dell'), Js('dorei'), Js('groth'), Js('hil'), Js('hona'), Js('hone'), Js('kadi'), Js('lean'), Js('lenor'), Js('lenora'), Js('lian'), Js('lin'), Js('lion'), Js('lon'), Js('lona'), Js('lond'), Js('lone'), Js('luma'), Js('lume'), Js('luna'), Js('lune'), Js('mel'), Js('melle'), Js('naes'), Js('nas'), Js('neas'), Js('nor'), Js('nora'), Js('nore'), Js('noris'), Js('qua'), Js('rion'), Js('rius'), Js('sari'), Js('sera'), Js('serin'), Js('serine'), Js('shara'), Js('shys'), Js('taesi'), Js('talos'), Js('thaes'), Js('thalas'), Js('thas'), Js('theas'), Js('themar'), Js('thyr')]))
pass
pass


# Add lib to the module scope
elfTowns = var.to_python()