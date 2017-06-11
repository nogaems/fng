__all__ = ['tahitianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'nm2', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Ahurei'), Js('Aia'), Js('Aiani'), Js('Aifeuna'), Js('Amo'), Js('Arii-fataia'), Js('Ariipaea'), Js('Aru'), Js('Auri'), Js('Auriro'), Js('Enometua'), Js('Farerohi'), Js('Haamanemane'), Js('Hama'), Js('Hamau'), Js('Haneti'), Js('Hapai'), Js('Haururu'), Js('Hiro'), Js('Hurimaavehi'), Js('Itiiti'), Js('Mahine'), Js('Mahui'), Js('Mai'), Js('Manea'), Js('Manua'), Js('Maoae'), Js('Matafaahira'), Js('Mauaihiti'), Js('Mauaroa'), Js('Moearu'), Js('Moemoe'), Js('Namiro'), Js('Niuhu'), Js('Nohoraa'), Js('Nuutere'), Js('Ohatatama'), Js('Omai'), Js('Opuhara'), Js('Oreo'), Js('Ori'), Js('Panee'), Js('Paofai'), Js("Pati'i"), Js('Pena'), Js('Pihato'), Js('Punua'), Js('Punua-teraitua'), Js('Taaroa'), Js('Taaroa-manahune'), Js('Taauaitatanuurua'), Js('Taino'), Js('Tamatoa'), Js('Tapoa'), Js('Tati'), Js('Tau'), Js('Taua-i-taata'), Js('Taura'), Js('Taura-atua'), Js('Tauraatua'), Js('Taute'), Js('Tavi'), Js('Tavihauroa'), Js('Te-manutunuu'), Js("Te-maui-ari'i"), Js('Te-mooiapitia'), Js('Teaatoro'), Js('Teaej'), Js('Tefaaora'), Js('Tehapai'), Js('Teieie'), Js('Teihotu'), Js('Temoo'), Js('Teohu'), Js('Tepau'), Js('Tepauarii'), Js('Terii'), Js('Terii-maevarua'), Js('Teriimana'), Js('Teruru'), Js('Tetohu'), Js('Tetumanua'), Js('Teu'), Js('Teuira'), Js('Teuira-arii'), Js('Teuraiterai'), Js('Teva'), Js('Tevahitua'), Js('Tiaau'), Js('Tiipaarii'), Js('Toa'), Js('Tuaroa'), Js('Tuhei'), Js('Tumoehamia'), Js('Tunuieaiteatua'), Js('Tupaia'), Js('Tutaha'), Js('Tutahau'), Js('Tuutini'), Js('Uata'), Js('Ui'), Js('Uruumatata'), Js('Vaetua'), Js('Vairatoa'), Js('Vanaama'), Js('Vari'), Js('Vari-mataauhue'), Js('Vavahiiteraa'), Js('Vehiatua'), Js('Veve')]))
    var.put('nm2', Js([Js("'Itea"), Js('Ahurai'), Js('Aimata'), Js("Aironoana'a"), Js('Airoro'), Js('Airotua'), Js('Arili-manihinihi'), Js('Ariioehau'), Js('Ariitaimai'), Js('Aroroerua'), Js('Auau'), Js('Fareahu'), Js('Fetefeteui'), Js('Hototu'), Js('Ino Metua'), Js('Maheanuu'), Js('Marae-ura'), Js('Moe'), Js('Murihau'), Js('Ourahi'), Js('Patea'), Js('Pateamai'), Js('Peutari'), Js('Piharii'), Js('Pipiri'), Js('Poivai'), Js('Purea'), Js('Taaroa'), Js('Taia'), Js('Tapuhote'), Js('Taura'), Js('Taura-atua'), Js('Tauraatua'), Js('Taurua'), Js('Te-aropoanaa'), Js('Te-fete-fete-ui'), Js('Teeva'), Js('Teeva Pirioi'), Js('Tefeau'), Js('Tehaapapa'), Js('Tehea'), Js('Teihotu'), Js('Temaehuata'), Js('Teraha-tetua'), Js('Teraiautia'), Js('Teraitua'), Js('Teremoemoe'), Js('Terero'), Js("Teri'i"), Js("Teri'itorai"), Js('Teriitahi'), Js('Teriitua'), Js('Teriivau'), Js('Teriivua-iterai'), Js('Terite'), Js('Terito'), Js('Teroroeora'), Js('Teroroera'), Js('Tetua'), Js('Tetua-umeritini'), Js('Tetuaehuri'), Js('Tetuahuri'), Js('Tetuanui'), Js('Tetuanuireia'), Js('Tetuaraenui'), Js('Tetuaunurau'), Js('Tetunania'), Js('Tetupaia'), Js('Tetupua'), Js('Teuira'), Js('Tevurua'), Js('Tevurua-hoiatua'), Js('Tevuruahoratua'), Js('Tiipaarii'), Js('Tupuetefa'), Js('Ura'), Js('Vavea')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', var.get('nm2').get(var.get('rnd')))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('names', var.get('nm1').get(var.get('rnd')))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
tahitianNames = var.to_python()