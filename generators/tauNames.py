__all__ = ['tauNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names4', 'names2', 'nameGen', 'names3'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
            var.put('names', (((((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd2')))+Js(' '))+var.get('names3').get(var.get('rnd3')))+var.get('names4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js("Aun'El"), Js("Aun'La"), Js("Aun'O"), Js("Aun'Ui"), Js("Aun'Vre"), Js("Fio'El"), Js("Fio'La"), Js("Fio'O"), Js("Fio'Ui"), Js("Fio'Vre"), Js("Kor'El"), Js("Kor'La"), Js("Kor'O"), Js("Kor'Ui"), Js("Kor'Vre"), Js("Por'El"), Js("Por'La"), Js("Por'O"), Js("Por'Ui"), Js("Por'Vre"), Js("Shas'El"), Js("Shas'La"), Js("Shas'O"), Js("Shas'Saal"), Js("Shas'Ui"), Js("Shas'Vre")]))
var.put('names2', Js([Js("Au'taal"), Js("Bor'kan"), Js("Bork'an"), Js("D'yanoi"), Js("Dal'yth"), Js("Elsy'eir"), Js("Es'Tau"), Js("Fal'shia"), Js("Fi'rios"), Js("Ho'sarn"), Js("Ka'mais"), Js("Ke'lshan"), Js("Ksi'm'yen"), Js("Me'lek"), Js("Mu'gulath"), Js("N'dras"), Js('Pech'), Js("Sa'cea"), Js("Sha'draig"), Js("T'au"), Js("T'olku"), Js("T'ros"), Js("Tash'var"), Js("Tau'n"), Js("Vash'ya"), Js("Velk'Han"), Js('Vespid'), Js("Vior'la")]))
var.put('names3', Js([Js('Al'), Js('Ar'), Js('Ash'), Js('Bant'), Js('Bra'), Js('Bun'), Js('Dia'), Js('Dor'), Js('Dra'), Js('Fio'), Js('Fir'), Js('Fral'), Js('Gir'), Js('Gra'), Js('Gras'), Js('Har'), Js('Hia'), Js('Hova'), Js('Inio'), Js('Ir'), Js('Irah'), Js('Jax'), Js('Jila'), Js('Jol'), Js('Kes'), Js('Ko'), Js('Krin'), Js('Man'), Js('Mira'), Js('Mon'), Js('Nar'), Js('Nase'), Js('Nori'), Js('Ora'), Js('Orna'), Js('Oxa'), Js('Pax'), Js('Pira'), Js('Prin'), Js('Resh'), Js('Ria'), Js('Ril'), Js('Shase'), Js('Shi'), Js('Sio'), Js('Tor'), Js('Tsu'), Js('Tsua'), Js('Var'), Js('Vra'), Js('Vura'), Js('Wran'), Js('Wua'), Js('Wura'), Js('Xira'), Js('Xo'), Js('Xral')]))
var.put('names4', Js([Js("'are"), Js("'ath"), Js("'ax"), Js("'bash"), Js("'bin"), Js("'bur"), Js("'dax"), Js("'dis"), Js("'dras"), Js("'elo"), Js("'en"), Js("'erk"), Js("'fa"), Js("'fel"), Js("'fin"), Js("'ga"), Js("'gos"), Js("'gri"), Js("'ha"), Js("'hin"), Js("'hos"), Js("'jash"), Js("'jin"), Js("'jor"), Js("'kir"), Js("'ko"), Js("'kran"), Js("'la"), Js("'las"), Js("'len"), Js("'me"), Js("'min"), Js("'mor"), Js("'na"), Js("'nera"), Js("'nesh"), Js("'or"), Js("'os"), Js("'osh"), Js("'par"), Js("'pin"), Js("'pras"), Js("'ra"), Js("'rak"), Js("'rax"), Js("'sha"), Js("'shash"), Js("'som"), Js("'taga"), Js("'ter"), Js("'tin"), Js("'un"), Js("'ur"), Js("'us"), Js("'vash"), Js("'vax"), Js("'vren"), Js("'wer"), Js("'werd"), Js("'wra"), Js("'xan"), Js("'xil"), Js("'xo"), Js("'yr"), Js('ah'), Js('al'), Js('aln'), Js('an'), Js('ara'), Js('arn'), Js('ash'), Js('ax'), Js('eh'), Js('el'), Js('en'), Js('er'), Js('erra'), Js('es'), Js('esh'), Js('eth'), Js('ina'), Js('ir'), Js('ira'), Js('irn'), Js('irr'), Js('ish'), Js('ith'), Js('ix'), Js('o'), Js('oh'), Js('ol'), Js('om'), Js('on'), Js('or'), Js('ot'), Js('oth'), Js('u'), Js('ug'), Js('un'), Js('ur'), Js('urn'), Js('us'), Js('uth'), Js('ux')]))
pass
pass


# Add lib to the module scope
tauNames = var.to_python()