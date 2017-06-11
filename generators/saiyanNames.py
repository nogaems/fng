__all__ = ['saiyanNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('names', var.get('names1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Sarada'), Js('Chaya'), Js('Negi'), Js('Cress'), Js('Komatsuna'), Js('Mizuna'), Js('Celeron'), Js('Nion'), Js('Luffa'), Js('Sabi'), Js('Aikon'), Js('Akchoy'), Js('Argula'), Js('Arlic'), Js('Articho'), Js('Arugu'), Js('Aspara'), Js('Aubergee'), Js('Aubergi'), Js('Avoca'), Js('Ayote'), Js('Bage'), Js('Beath'), Js('Beatroo'), Js('Been'), Js('Beetroo'), Js('Bokcho'), Js('Cabba'), Js('Cado'), Js('Calaba'), Js('Callio'), Js('Callion'), Js('Capper'), Js('Carole'), Js('Cassa'), Js('Cauri'), Js('Celleri'), Js('Ceriac'), Js('Chayot'), Js('Chini'), Js('Coliflo'), Js('Collar'), Js('Colrab'), Js('Corget'), Js('Corgetta'), Js('Coriflo'), Js('Courge'), Js('Courne'), Js('Cucum'), Js('Cucumb'), Js('Cumber'), Js('Daiko'), Js('Dakon'), Js('Dicchio'), Js('Dive'), Js('Elery'), Js('Endife'), Js('Erkin'), Js('Escar'), Js('Escaro'), Js('Fannel'), Js('Fennle'), Js('Galalang'), Js('Galanga'), Js('Gangal'), Js('Garlik'), Js('Gherk'), Js('Ginge'), Js('Gorlick'), Js('Gula'), Js('Gurki'), Js('Iceber'), Js('Ionon'), Js('Isebereg'), Js('Jinjer'), Js('Kabage'), Js('Kail'), Js('Kallabash'), Js('Kaper'), Js('Karroto'), Js('Kassava'), Js('Kayle'), Js('Keel'), Js('Kohlra'), Js('Kolard'), Js('Kolra'), Js('Korn'), Js('Langal'), Js('Lantain'), Js('Lattuce'), Js('Leeck'), Js('Lemogra'), Js('Lemogras'), Js('Leriac'), Js('Lery'), Js('Lettus'), Js('Lottus'), Js('Lotuce'), Js('Maiz'), Js('Matillo'), Js('Matiloto'), Js('Matoto'), Js('May'), Js('Mayze'), Js('Naeb'), Js('Niun'), Js('Noino'), Js('Noppal'), Js('Noppale'), Js('Okara'), Js('Okarot'), Js('Okchoy'), Js('Okora'), Js('Olave'), Js('Olve'), Js('Onnio'), Js('Orat'), Js('Otamot'), Js('Pakcho'), Js('Palantay'), Js('Paragu'), Js('Parslee'), Js('Parsnap'), Js('Pasley'), Js('Peppa'), Js('Pinach'), Js('Pinache'), Js('Pinrut'), Js('Planta'), Js('Potate'), Js('Potota'), Js('Proute'), Js('Pumkin'), Js('Pumpki'), Js('Quash'), Js('Raddis'), Js('Radichio'), Js('Radis'), Js('Reppep'), Js('Rootaba'), Js('Rota'), Js('Ruccollo'), Js('Ruco'), Js('Rugool'), Js('Rugu'), Js('Rutaba'), Js('Sallot'), Js('Scalli'), Js('Scallio'), Js('Shalot'), Js('Snippar'), Js('Spargu'), Js('Sproute'), Js('Squas'), Js('Suncho'), Js('Sunchock'), Js('Tabaga'), Js('Tarro'), Js('Tato'), Js('Teeb'), Js('Tercres'), Js('Tichoke'), Js('Totoma'), Js('Tunnip'), Js('Turrip'), Js('Ugula'), Js('Umpkin'), Js('Vocado'), Js('Yamma'), Js('Zucchi')]))
pass
pass


# Add lib to the module scope
saiyanNames = var.to_python()