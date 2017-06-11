__all__ = ['necronNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result', 'br'])
    var.put('br', Js([]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
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
var.put('names1', Js([Js('Aaho'), Js('Adda'), Js('Aga'), Js('Aha'), Js('Ahho'), Js('Ah'), Js('Akhe'), Js('Ama'), Js('Amene'), Js('Amenho'), Js('Anho'), Js('Ankhese'), Js('Anla'), Js('Ara'), Js('Asha'), Js('Baqe'), Js('Bebi'), Js('Beke'), Js('Bere'), Js('Cleo'), Js('Dakha'), Js('Dedu'), Js('Deme'), Js('Dja'), Js('Djede'), Js('Dje'), Js('Djo'), Js('Duae'), Js('Eury'), Js('Gany'), Js('Geme'), Js('Gilu'), Js('Hako'), Js('Harkhe'), Js('Harsio'), Js('Hedje'), Js('Hekenu'), Js('Hema'), Js('Henu'), Js('Heqa'), Js('Hete'), Js('Hewe'), Js('Hore'), Js('Hote'), Js('Ibi'), Js('Ibia'), Js('Imho'), Js('Ina'), Js('Ine'), Js('Inetka'), Js('Inte'), Js('Ise'), Js('Isetno'), Js('Iuwe'), Js('Kage'), Js('Kape'), Js('Karo'), Js('Kawa'), Js('Kha'), Js('Khae'), Js('Khame'), Js('Khamu'), Js('Khede'), Js('Khe'), Js('Khu'), Js('Maga'), Js('Mane'), Js('Meke'), Js('Menkau'), Js('Menkhe'), Js('Mentu'), Js('Mere'), Js('Meri'), Js('Merne'), Js('Mery'), Js('Minmo'), Js('Mutne'), Js('Nakhto'), Js('Nasa'), Js('Nebu'), Js('Nebe'), Js('Nebne'), Js('Necta'), Js('Nefe'), Js('Nehe'), Js('Nephe'), Js('Nimae'), Js('Nubkhe'), Js('Pane'), Js('Pare'), Js('Pawu'), Js('Pene'), Js('Petu'), Js('Preho'), Js('Psuse'), Js('Ptahmo'), Js('Ptole'), Js('Qare'), Js('Raho'), Js('Rahe'), Js('Rame'), Js('Ramo'), Js('Sahu'), Js('Sehe'), Js('Sekhe'), Js('Seme'), Js('Sense'), Js('Senu'), Js('Seshe'), Js('Simu'), Js('Tadu'), Js('Takha'), Js('Thutmo'), Js('Tuta'), Js('Udje'), Js('Yanha')]))
var.put('names2', Js([Js('bash'), Js('basken'), Js('bi'), Js('biankh'), Js('bkay'), Js('clea'), Js('clid'), Js('cris'), Js('des'), Js('djem'), Js('dkare'), Js('fer'), Js('fret'), Js('hyt'), Js('kare'), Js('kauhor'), Js('khaf'), Js('khat'), Js('khet'), Js('khmet'), Js('khmire'), Js('khnet'), Js('khotep'), Js('kht'), Js('kor'), Js('maka'), Js('mehyt'), Js('menes'), Js('menre'), Js('mes'), Js('mhat'), Js('mka'), Js('mkah'), Js('mnisu'), Js('mopet'), Js('mose'), Js('mqen'), Js('msaf'), Js('mun'), Js('munzu'), Js('nakht'), Js('namen'), Js('namun'), Js('naten'), Js('nath'), Js('ndes'), Js('nebti'), Js('nebu'), Js('nhor'), Js('nhotekh'), Js('nhotep'), Js('nmut'), Js('nna'), Js('nru'), Js('nu'), Js('nut'), Js('nza'), Js('phren'), Js('pses'), Js('ptah'), Js('qar'), Js('qed'), Js('ra'), Js('ramen'), Js('reh'), Js('rekh'), Js('renef'), Js('ros'), Js('rqa'), Js('rtari'), Js('ru'), Js('rus'), Js('s'), Js('sankh'), Js('sehti'), Js('seneb'), Js('set'), Js('shen'), Js('shenq'), Js('shet'), Js('skaf'), Js('skhet'), Js('snet'), Js('sret'), Js('t'), Js('tamen'), Js('tamun'), Js('tanath'), Js('tankh'), Js('tari'), Js('taruk'), Js('taten'), Js('tef'), Js('tekh'), Js('tep'), Js('thap'), Js('thes'), Js('this'), Js('thor'), Js('tka'), Js('wa')]))
pass
pass


# Add lib to the module scope
necronNames = var.to_python()