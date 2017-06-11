__all__ = ['dwarfDaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'namesFemale', 'namesFemale2', 'names3', 'namesMale', 'namesFamily'])
@Js
def PyJsHoisted_nameGen_(namesMale, namesFamily, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'namesMale':namesMale, 'namesFamily':namesFamily}, var)
    var.registers(['names1', 'names2', 'result', 'namesMale', 'namesFamily'])
    var.put('names1', var.get('namesMale'))
    var.put('names2', var.get('namesFamily'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
            var.put('names', ((((var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1')))+Js(' '))+var.get('names3').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('namesFemale', Js([Js('A'), Js('Ba'), Js('Bra'), Js('Co'), Js('Da'), Js('Fa'), Js('Fari'), Js('Fe'), Js('Feri'), Js('Fi'), Js('Ha'), Js('Hana'), Js('He'), Js('Ja'), Js('Je'), Js('Ka'), Js('Kala'), Js('Ke'), Js('Kela'), Js('Le'), Js('Li'), Js('Ma'), Js('Me'), Js('Mi'), Js('Mya'), Js('Na'), Js('Nara'), Js('Nera'), Js('Ole'), Js('Oli'), Js('Re'), Js('Ri'), Js('Se'), Js('Si'), Js('Ta'), Js('Te'), Js('Za'), Js('Ze')]))
var.put('namesFemale2', Js([Js('ca'), Js('cha'), Js('da'), Js('dal'), Js('den'), Js('dy'), Js('gna'), Js('grun'), Js('ha'), Js('han'), Js('ja'), Js('ka'), Js('la'), Js('lah'), Js('li'), Js('linda'), Js('linden'), Js('lsi'), Js('na'), Js('nda'), Js('nden'), Js('nka'), Js('nna'), Js('pith'), Js('ra'), Js('rav'), Js('rdy'), Js('rev'), Js('rinda'), Js('rinden'), Js('rra'), Js('rta'), Js('run'), Js('rvia'), Js('ryn'), Js('rynn'), Js('scha'), Js('shan'), Js('si'), Js('ta'), Js('tha'), Js('tyth'), Js('via'), Js('zda')]))
var.put('namesMale', Js([Js('Ade'), Js('Adema'), Js('Ahre'), Js('Ali'), Js('An'), Js('Ba'), Js('Bai'), Js('Bande'), Js('Bar'), Js('Be'), Js('Bera'), Js('Bere'), Js('Bhe'), Js('Bhele'), Js('Bo'), Js('Boda'), Js('Boe'), Js('Bro'), Js('Bru'), Js('Bu'), Js('Czi'), Js('Da'), Js('Dai'), Js('De'), Js('Dene'), Js('Dou'), Js('Du'), Js('Duli'), Js('Dwo'), Js('Dwy'), Js('Emry'), Js('En'), Js('Endri'), Js('Eve'), Js('Fi'), Js('Figo'), Js('Fra'), Js('Ga'), Js('Gar'), Js('Gari'), Js('Garte'), Js('Ge'), Js('Ger'), Js('Gera'), Js('Gla'), Js('Go'), Js('Goi'), Js('Gor'), Js('Gori'), Js('Gwi'), Js('Hi'), Js('Hir'), Js('Hiro'), Js('Hu'), Js('Hugi'), Js('Iwa'), Js('Ja'), Js('Jana'), Js('Java'), Js('Je'), Js('Jer'), Js('Ju'), Js('Ka'), Js('Kar'), Js('Le'), Js('Lo'), Js('Loi'), Js('Lu'), Js('Luc'), Js('Ma'), Js('Mai'), Js('Me'), Js('Mer'), Js('Meri'), Js('Mi'), Js('Min'), Js('Na'), Js('Nal'), Js('Ne'), Js('Nevi'), Js('Og'), Js('Ola'), Js('Or'), Js('Oski'), Js('Pi'), Js('Pio'), Js('Py'), Js('Pyr'), Js('Pyra'), Js('Re'), Js('Ren'), Js('Rha'), Js('Ro'), Js('Ru'), Js('Sa'), Js('San'), Js('Se'), Js('Sewe'), Js('Te'), Js('Tem'), Js('Tha'), Js('Thati'), Js('Thau'), Js('To'), Js('Tri'), Js('Tria'), Js('Tu'), Js('Va'), Js('Var'), Js('Ve'), Js('Vel'), Js('Vo'), Js('Vol'), Js('Wi'), Js('Wo'), Js('Wor'), Js('Ye')]))
var.put('namesFamily', Js([Js('bor'), Js('dahn'), Js('dal'), Js('del'), Js('delor'), Js('derel'), Js('dlin'), Js('dol'), Js('don'), Js('drik'), Js('drin'), Js('g'), Js('gal'), Js('gan'), Js('gar'), Js('gek'), Js('gin'), Js('gor'), Js('grand'), Js('grin'), Js('ka'), Js('kas'), Js('ke'), Js('kel'), Js('kias'), Js('kin'), Js('lan'), Js('lanz'), Js('len'), Js('lid'), Js('lin'), Js('linar'), Js('mar'), Js('maro'), Js('merin'), Js('mor'), Js('n'), Js('nak'), Js('nar'), Js('nek'), Js('niv'), Js('nus'), Js('raht'), Js('ral'), Js('ram'), Js('rand'), Js('rav'), Js('rd'), Js('rel'), Js('ren'), Js('ric'), Js('rick'), Js('rik'), Js('rim'), Js('rin'), Js('ris'), Js('rkel'), Js('rkin'), Js('rol'), Js('ron'), Js('rtag'), Js('ryn'), Js('rys'), Js('sch'), Js('seck'), Js('shen'), Js('so'), Js('son'), Js('tag'), Js('tan'), Js('tek'), Js('thur'), Js('thy'), Js('tigan'), Js('tin'), Js('trak'), Js('trand'), Js('varis'), Js('vez'), Js('vhen'), Js('vil'), Js('vin'), Js('wan'), Js('wer'), Js('weryn'), Js('zyl')]))
var.put('names3', Js([Js('A'), Js('Ae'), Js('Al'), Js('Ar'), Js('Ara'), Js('Be'), Js('Ber'), Js('Bra'), Js('Bro'), Js('Ca'), Js('Cada'), Js('Car'), Js('Cari'), Js('Da'), Js('Do'), Js('Du'), Js('Dur'), Js('E'), Js('Eto'), Js('Fe'), Js('Fer'), Js('Fera'), Js('Fo'), Js('For'), Js('Fore'), Js('Ga'), Js('Gal'), Js('Gar'), Js('Ghe'), Js('Gher'), Js('Gla'), Js('Go'), Js('Gor'), Js('Goro'), Js('Ha'), Js('Har'), Js('He'), Js('Hel'), Js('Hi'), Js('Hir'), Js('I'), Js('Ka'), Js('Kana'), Js('Kla'), Js('Klar'), Js('Ko'), Js('Me'), Js('Mei'), Js('Mer'), Js('O'), Js('Or'), Js('Ra'), Js('Rae'), Js('Ro'), Js('Rou'), Js('Ru'), Js('Rumo'), Js('Sa'), Js('Sae'), Js('Te'), Js('Tho'), Js('Ti'), Js('To'), Js('Tor'), Js('Tu'), Js('Tur'), Js('U'), Js('Ul'), Js('Va'), Js('Var'), Js('Vo'), Js('We'), Js('Wey'), Js('Yo'), Js('Zy')]))
var.put('names4', Js([Js('ban'), Js('ca'), Js('can'), Js('das'), Js('dash'), Js('den'), Js('dens'), Js('der'), Js('dic'), Js('din'), Js('dra'), Js('drat'), Js('ducan'), Js('ka'), Js('lac'), Js('lar'), Js('lban'), Js('lmas'), Js('lmi'), Js('lney'), Js('lon'), Js('lra'), Js('lro'), Js('mas'), Js('mi'), Js('mold'), Js('mot'), Js('mote'), Js('munt'), Js('nak'), Js('narek'), Js('ney'), Js('nka'), Js('no'), Js('noch'), Js('ntop'), Js('ra'), Js('ral'), Js('rald'), Js('ran'), Js('rana'), Js('ras'), Js('rat'), Js('rek'), Js('ren'), Js('ret'), Js('ridin'), Js('rin'), Js('ro'), Js('rol'), Js('row'), Js('sca'), Js('sten'), Js('tack'), Js('tan'), Js('ten'), Js('top'), Js('ver'), Js('vis'), Js('vish'), Js('vo'), Js('vonak'), Js('vorn')]))
pass
pass


# Add lib to the module scope
dwarfDaNames = var.to_python()