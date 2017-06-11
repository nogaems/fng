__all__ = ['darkEldarNames']

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
var.put('names1', Js([Js('Aes'), Js("Ar'o"), Js("Ar'ug"), Js('Arh'), Js('Arma'), Js('Arqa'), Js('Arzo'), Js('Arzur'), Js('Asdru'), Js('Bahr'), Js('Bahru'), Js('Baze'), Js('Bazha'), Js('Bernu'), Js('Bhu'), Js('Bra'), Js('Braes'), Js('Bura'), Js('Caen'), Js('Char'), Js("Cra'oza"), Js('Crahl'), Js('Daza'), Js('Dra'), Js('Draz'), Js('Duhr'), Js("El'ur"), Js('Erza'), Js('Ez'), Js('Ezar'), Js('Fahar'), Js('Fahr'), Js('Fhars'), Js('Frae'), Js('Fure'), Js("Ga'on"), Js('Gahu'), Js('Gara'), Js('Gra'), Js('Griza'), Js('Gura'), Js("Id'ar"), Js('Iru'), Js('Iys'), Js('Izen'), Js('Izra'), Js('Kae'), Js('Kahar'), Js('Kahr'), Js('Khan'), Js('Kyra'), Js('Laerh'), Js('Lahza'), Js('Laku'), Js('Laza'), Js("Le'u"), Js('Maru'), Js('Masra'), Js('Mazro'), Js('Meza'), Js("Mo'u"), Js('Much'), Js('Muri'), Js("Or'i"), Js('Ori'), Js('Orqa'), Js('Oura'), Js('Ozu'), Js('Taga'), Js('Tah'), Js('Teza'), Js('Trazh'), Js("Yl'a"), Js('Yra'), Js('Yzu')]))
var.put('names2', Js([Js('baehr'), Js('bran'), Js('braq'), Js('bros'), Js('bryn'), Js('dazar'), Js('dhar'), Js('diaq'), Js('dovur'), Js('dros'), Js('durin'), Js('gahn'), Js('gard'), Js('gran'), Js('grath'), Js('hiron'), Js('his'), Js('hyque'), Js('kei'), Js('kos'), Js('kras'), Js('kyth'), Js('mahr'), Js('maq'), Js('mar'), Js('mass'), Js('mien'), Js('moque'), Js('mor'), Js('naer'), Js('nahr'), Js('nazar'), Js('neque'), Js('nyr'), Js('qar'), Js('qir'), Js('ra'), Js('rad'), Js('raes'), Js('ras'), Js('rath'), Js('raz'), Js('riaq'), Js('rihz'), Js('rior'), Js('rizar'), Js('ruin'), Js('ryq'), Js('sar'), Js('sarith'), Js('saros'), Js('sath'), Js('shar'), Js('sque'), Js('stra'), Js('syr'), Js('tahr'), Js('taz'), Js('teque'), Js('thara'), Js('tharn'), Js('tiron'), Js('tyhr'), Js('tzar'), Js('vall'), Js('van'), Js('vhar'), Js('vor'), Js('vyn'), Js('zaen'), Js('zaq'), Js('zhan'), Js('zhar'), Js('zon'), Js('zyth')]))
var.put('names3', Js([Js('Aes'), Js('Aezo'), Js('Ahl'), Js("Al'o"), Js("Ar'us"), Js('Ara'), Js('Arqi'), Js('Arze'), Js('Ashru'), Js('Baeh'), Js('Baes'), Js('Bahre'), Js('Belze'), Js('Besnu'), Js('Bezha'), Js('Bhi'), Js('Bhra'), Js('Bira'), Js('Caren'), Js('Cher'), Js('Crehn'), Js("Cri'ora"), Js('Dehza'), Js('Der'), Js('Dera'), Js('Drehz'), Js('Ehz'), Js("El'or"), Js('Eraza'), Js('Ezir'), Js('Fehsa'), Js('Fera'), Js('Fha'), Js('Fihr'), Js('Frae'), Js("Gae'en"), Js('Gahnu'), Js('Garia'), Js('Gri'), Js('Grihza'), Js('Gura'), Js('Iaze'), Js("Ide'a"), Js('Ire'), Js('Iyes'), Js('Izera'), Js('Kaera'), Js('Kahna'), Js('Kehna'), Js('Khel'), Js('Kihre'), Js("Lae'o"), Js('Laerh'), Js('Laeza'), Js('Lanu'), Js('Lohza'), Js('Maero'), Js('Meha'), Js('Mera'), Js('Meri'), Js("Mero'a"), Js('Mesra'), Js('Mihza'), Js('Ohza'), Js('Ora'), Js("Ora'i"), Js('Ori'), Js('Oriqa'), Js('Taza'), Js('Teha'), Js('Tera'), Js('Trezh'), Js('Yna'), Js("Yr'a"), Js('Yzi')]))
var.put('names4', Js([Js('baehra'), Js('brique'), Js('bris'), Js('brynn'), Js('daque'), Js('dera'), Js('deza'), Js('dhae'), Js('dove'), Js('dreos'), Js('gahne'), Js('geza'), Js('gohne'), Js('grynn'), Js('gwyss'), Js('heque'), Js('hia'), Js('hira'), Js('keo'), Js('keri'), Js('kryss'), Js('kysse'), Js('maque'), Js('mare'), Js('mea'), Js('mehra'), Js('mirenne'), Js('mohre'), Js('myss'), Js('naehr'), Js('nahra'), Js('neque'), Js('neza'), Js('nyrr'), Js('qinn'), Js('qore'), Js('rae'), Js('raesh'), Js('reah'), Js('reaq'), Js('renar'), Js('renn'), Js('resse'), Js('rihque'), Js('rith'), Js('riza'), Js('rizora'), Js('runae'), Js('saer'), Js('sarihs'), Js('seos'), Js('seqe'), Js('seth'), Js('sher'), Js('shi'), Js('sira'), Js('syrr'), Js('taena'), Js('taez'), Js('tarin'), Js('teque'), Js('thara'), Js('thera'), Js('tihr'), Js('tyhs'), Js('vaesh'), Js('velle'), Js('vero'), Js('vynn'), Js('zae'), Js('zaehn'), Js('zhael'), Js('zhenne'), Js('zoh'), Js('zysh')]))
pass
pass


# Add lib to the module scope
darkEldarNames = var.to_python()