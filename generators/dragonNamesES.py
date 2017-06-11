__all__ = ['dragonNamesES']

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
    var.registers(['result', 'br'])
    var.put('br', Js([]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(8.0)):
                var.put('rnd', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length')))))
                var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length')))))
                while PyJsStrictEq(var.get('rnd2'),var.get('rnd')):
                    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length')))))
                var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length')))))
                while (PyJsStrictEq(var.get('rnd3'),var.get('rnd')) or PyJsStrictEq(var.get('rnd3'),var.get('rnd2'))):
                    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length')))))
                var.put('names', ((var.get('names1').get(var.get('rnd'))+var.get('names1').get(var.get('rnd2')))+var.get('names1').get(var.get('rnd3'))))
            else:
                var.put('rnd', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length')))))
                var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length')))))
                while PyJsStrictEq(var.get('rnd2'),var.get('rnd')):
                    var.put('rn22', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length')))))
                var.put('names', (var.get('names1').get(var.get('rnd'))+var.get('names1').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('aak'), Js('aal'), Js('aam'), Js('aar'), Js('aav'), Js('aaz'), Js('ag'), Js('ah'), Js('al'), Js('am'), Js('aus'), Js('bah'), Js('bein'), Js('bel'), Js('bex'), Js('beyn'), Js('bii'), Js('bo'), Js('bok'), Js('brii'), Js('brit'), Js('brod'), Js('brom'), Js('bron'), Js('daal'), Js('daan'), Js('daar'), Js('dah'), Js('dein'), Js('dez'), Js('dii'), Js('diil'), Js('diin'), Js('diiv'), Js('dir'), Js('dok'), Js('dov'), Js('draal'), Js('dreh'), Js('drem'), Js('drey'), Js('drog'), Js('drun'), Js('du'), Js("du'ul"), Js('dun'), Js('dur'), Js('dwiin'), Js('ek'), Js('faad'), Js('faas'), Js('faaz'), Js('feim'), Js('fel'), Js('feyn'), Js('fiik'), Js('fo'), Js('frin'), Js('frod'), Js('fron'), Js('frul'), Js('ful'), Js('fun'), Js('funt'), Js('fus'), Js('gaaf'), Js('gaan'), Js('gaar'), Js('geh'), Js('gein'), Js('gol'), Js('golt'), Js('golz'), Js('graag'), Js('graan'), Js('grah'), Js('gram'), Js('grik'), Js('grind'), Js('gro'), Js('gron'), Js('gruth'), Js('gut'), Js('haal'), Js('haas'), Js('hah'), Js('heim'), Js('het'), Js('heyv'), Js('hind'), Js('hon'), Js('hun'), Js('iiz'), Js('in'), Js('inhus'), Js('jer'), Js('joor'), Js('jot'), Js('jud'), Js('jul'), Js('jun'), Js('kaal'), Js('kaan'), Js('kaaz'), Js('kah'), Js('kein'), Js('kel'), Js('kest'), Js('key'), Js('keyn'), Js('kiim'), Js('kiin'), Js('kiir'), Js('kip'), Js('klo'), Js('klov'), Js('ko'), Js('kod'), Js('kol'), Js('koor'), Js('krah'), Js('kras'), Js('kreh'), Js('krein'), Js('kren'), Js('krent'), Js('krif'), Js('krii'), Js('kriid'), Js('kriist'), Js('kril'), Js('krin'), Js('kro'), Js('kron'), Js('kul'), Js('laan'), Js('laas'), Js('laat'), Js('lah'), Js('leh'), Js('lein'), Js('liiv'), Js('lir'), Js('lo'), Js('lok'), Js('lon'), Js('loost'), Js('lot'), Js('luft'), Js('lun'), Js('luv'), Js('maar'), Js('mah'), Js('mal'), Js('med'), Js('mey'), Js('meyz'), Js('mid'), Js('miin'), Js('mir'), Js('mon'), Js('mul'), Js('mun'), Js('muz'), Js('naak'), Js('naan'), Js('naar'), Js('nah'), Js('nahl'), Js('nau'), Js('nax'), Js('neh'), Js('ney'), Js('ni'), Js('nid'), Js('nii'), Js('niin'), Js('nil'), Js('nin'), Js('nir'), Js('nis'), Js('nok'), Js('nos'), Js('nus'), Js('od'), Js('okaaz'), Js('ol'), Js('om'), Js('ond'), Js('ont'), Js('oth'), Js('ov'), Js('paak'), Js('paal'), Js('paar'), Js('paaz'), Js('pah'), Js('pel'), Js('peyt'), Js('pook'), Js('praal'), Js('praan'), Js('prem'), Js('qah'), Js('qeth'), Js('qo'), Js('qoth'), Js('raan'), Js('rah'), Js('rath'), Js('rein'), Js('rek'), Js('rel'), Js('reyth'), Js('rii'), Js('riik'), Js('ro'), Js('rok'), Js('rot'), Js('ru'), Js('rul'), Js('ruth'), Js('saan'), Js('sah'), Js('sar'), Js('shaan'), Js('shul'), Js('siiv'), Js('sik'), Js('sil'), Js('slen'), Js('so'), Js('sod'), Js('sos'), Js('sot'), Js('sov'), Js('spaan'), Js('stin'), Js('strun'), Js('su'), Js("su'um"), Js('sul'), Js('tah'), Js('tey'), Js('thaarn'), Js("thu'um"), Js('thur'), Js('tiid'), Js('til'), Js('toor'), Js('tu'), Js('tum'), Js('tuz'), Js('ul'), Js('un'), Js('unt'), Js('us'), Js('uth'), Js('uv'), Js('vaal'), Js('vaat'), Js('vaaz'), Js('vah'), Js('ved'), Js('ven'), Js('vey'), Js('viik'), Js('viin'), Js('viing'), Js('viir'), Js('vith'), Js('vod'), Js('vol'), Js('vu'), Js('vul'), Js('vum'), Js('vur'), Js('vus'), Js('wahl'), Js('wen'), Js('win'), Js('wol'), Js('wuld'), Js('wuth'), Js('yah'), Js('yolx'), Js('yuvon'), Js('zaam'), Js('zaan'), Js('zah'), Js('zeim'), Js('zein'), Js('zii'), Js('zin'), Js('zind'), Js('zok'), Js('zol'), Js('zoor'), Js('zul'), Js('zun')]))
pass
pass


# Add lib to the module scope
dragonNamesES = var.to_python()