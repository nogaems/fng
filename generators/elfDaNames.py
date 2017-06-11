__all__ = ['elfDaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['namesFamily', 'nameGen', 'namesFemale2', 'namesMale', 'namesFemale'])
@Js
def PyJsHoisted_nameGen_(namesMales, namesFamily, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'namesMales':namesMales, 'this':this, 'namesFamily':namesFamily}, var)
    var.registers(['names1', 'namesMales', 'names2', 'result', 'namesFamily'])
    var.put('names1', var.get('namesMales'))
    var.put('names2', var.get('namesFamily'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', (var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('namesFemale', Js([Js('Ada'), Js('Ari'), Js('Aria'), Js('Asha'), Js('Ashi'), Js('Athe'), Js('Bri'), Js('Bria'), Js('Dany'), Js('De'), Js('Deve'), Js('Di'), Js('Elo'), Js('Fi'), Js('Fio'), Js('Ghe'), Js('Io'), Js('Ise'), Js('Ka'), Js('La'), Js('Lana'), Js('Li'), Js('Lia'), Js('Ma'), Js('Mare'), Js('Me'), Js('Melo'), Js('Merri'), Js('Mi'), Js('Mih'), Js('Na'), Js('Nama'), Js('Ne'), Js('Nesi'), Js('Nesia'), Js('No'), Js('Nola'), Js('Ora'), Js('Orana'), Js('Pa'), Js('Pano'), Js('Ri'), Js('Se'), Js('Sera'), Js('Sha'), Js('Shae'), Js('Shi'), Js('Shia'), Js('Va'), Js('Valo'), Js('Valy'), Js('Vari'), Js('Ve'), Js('Vela')]))
var.put('namesFemale2', Js([Js('hari'), Js('hra'), Js('hris'), Js('la'), Js('lanna'), Js('ll'), Js('lle'), Js('lora'), Js('lva'), Js('lwyn'), Js('lya'), Js('maya'), Js('na'), Js('naya'), Js('ne'), Js('ni'), Js('nna'), Js('nne'), Js('nni'), Js('nowen'), Js('nril'), Js('nyla'), Js('ra'), Js('rana'), Js('ranni'), Js('ren'), Js('ri'), Js('riel'), Js('ril'), Js('rill'), Js('ris'), Js('rrill'), Js('sa'), Js('siara'), Js('ssa'), Js('thari'), Js('thra'), Js('triel'), Js('va'), Js('vera'), Js('vra'), Js('wen'), Js('wyn'), Js('ya')]))
var.put('namesMale', Js([Js('Ad'), Js('Al'), Js('Ala'), Js('Ar'), Js('At'), Js('Ath'), Js('Bra'), Js('Ca'), Js('Cam'), Js('Car'), Js('Cy'), Js('Cyr'), Js('Dey'), Js('El'), Js('Fe'), Js('Fel'), Js('Fen'), Js('Fey'), Js('Feyn'), Js('Ga'), Js('Gar'), Js('Ge'), Js('Get'), Js('Geth'), Js('Ha'), Js('Har'), Js('Hu'), Js('Il'), Js('Ja'), Js('Jos'), Js('Jun'), Js('Le'), Js('Lem'), Js('Ne'), Js('Nel'), Js('Pa'), Js('Pai'), Js('Pi'), Js('Sa'), Js('Sam'), Js('Sar'), Js('Se'), Js('Sen'), Js('So'), Js('Sor'), Js('Ta'), Js('Tae'), Js('Tam'), Js('The'), Js('Thel'), Js('Thre'), Js('Va'), Js('Var'), Js('Vara'), Js('Ye'), Js('Yev'), Js('Zat'), Js('Zath'), Js('Zev')]))
var.put('namesFamily', Js([Js('cen'), Js('dis'), Js('dor'), Js('gan'), Js('hel'), Js('hon'), Js('horn'), Js('lan'), Js('laros'), Js('lasan'), Js('lassan'), Js('len'), Js('lhen'), Js('mael'), Js('men'), Js('met'), Js('nar'), Js('narel'), Js('rahel'), Js('ralan'), Js('ran'), Js('rand'), Js('ras'), Js('rel'), Js('ren'), Js('rian'), Js('riel'), Js('rion'), Js('ris'), Js('rith'), Js('ron'), Js('ros'), Js('sas'), Js('thon'), Js('thorn'), Js('vel'), Js('ven'), Js('vin'), Js('wen')]))
pass
pass


# Add lib to the module scope
elfDaNames = var.to_python()