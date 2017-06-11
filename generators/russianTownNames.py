__all__ = ['russianTownNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aba'), Js('Achi'), Js('Ale'), Js('Alme'), Js('Ana'), Js('Anga'), Js('Apa'), Js('Arma'), Js('Arse'), Js('Arza'), Js('Astra'), Js('Bala'), Js('Bata'), Js('Bele'), Js('Belgo'), Js('Belo'), Js('Belore'), Js('Bere'), Js('Beryo'), Js('Biro'), Js('Birobi'), Js('Blago'), Js('Blagove'), Js('Bori'), Js('Boriso'), Js('Boro'), Js('Bra'), Js('Budyo'), Js('Bugu'), Js('Buyna'), Js('Buzu'), Js('Chapa'), Js('Chayko'), Js('Che'), Js('Chebo'), Js('Chelya'), Js('Chere'), Js('Cherno'), Js('Chi'), Js('Chisto'), Js('De'), Js('Dmi'), Js('Do'), Js('Dolgo'), Js('Domo'), Js('Domode'), Js('Done'), Js('Du'), Js('Eli'), Js('Frya'), Js('Ga'), Js('Gele'), Js('Gla'), Js('Go'), Js('Gro'), Js('Gu'), Js('Guko'), Js('Irku'), Js('Ishi'), Js('Iski'), Js('Iva'), Js('Ka'), Js('Kali'), Js('Kalini'), Js('Kalu'), Js('Kame'), Js('Kamy'), Js('Kaspi'), Js('Keme'), Js('Kha'), Js('Khaba'), Js('Khasa'), Js('Khi'), Js('Kine'), Js('Kiri'), Js('Kiro'), Js('Kise'), Js('Kislo'), Js('Kli'), Js('Klimo'), Js('Ko'), Js('Koga'), Js('Kolo'), Js('Komso'), Js('Kope'), Js('Koro'), Js('Kostro'), Js('Kovro'), Js('Krasno'), Js('Kropo'), Js('Kry'), Js('Ku'), Js('Kume'), Js('Kuzne'), Js('Ky'), Js('Labi'), Js('Leni'), Js('Lenino'), Js('Lesn'), Js('Leso'), Js('Li'), Js('Lipe'), Js('Lo'), Js('Ly'), Js('Lyu'), Js('Lyube'), Js('Ma'), Js('Maga'), Js('Magni'), Js('Magnito'), Js('Makha'), Js('Me'), Js('Mezhdu'), Js('Mia'), Js('Michu'), Js('Mikhay'), Js('Mine'), Js('Minu'), Js('Mo'), Js('Mu'), Js('My'), Js('Myti'), Js('Na'), Js('Nabe'), Js('Nakho'), Js('Navere'), Js('Naza'), Js('Nefte'), Js('Nefteyu'), Js('Neryu'), Js('Nevi'), Js('Nizhne'), Js('Nogi'), Js('Nori'), Js('Novo'), Js('Novoa'), Js('Novoche'), Js('Novoku'), Js('Novomo'), Js('Novorossi'), Js('Novotroi'), Js('Novou'), Js('Noya'), Js('Nya'), Js('Obni'), Js('Odi'), Js('Oktya'), Js('Ore'), Js('Ory'), Js('Ozyo'), Js('Pavlo'), Js('Pervou'), Js('Podo'), Js('Pole'), Js('Pro'), Js('Proko'), Js('Pu'), Js('Pya'), Js('Pyati'), Js('Rame'), Js('Reu'), Js('Ro'), Js('Rosla'), Js('Rosso'), Js('Rya'), Js('Rybi'), Js('Sala'), Js('Sama'), Js('Sara'), Js('Saro'), Js('Serpu'), Js('Seve'), Js('Severo'), Js('Sha'), Js('Shchyo'), Js('Shu'), Js('Si'), Js('Siba'), Js('Sla'), Js('Smo'), Js('So'), Js('Soli'), Js('Solne'), Js('Soso'), Js('Sta'), Js('Stavro'), Js('Ste'), Js('Sterli'), Js('Stu'), Js('Stupi'), Js('Su'), Js('Svo'), Js('Svobo'), Js('Taga'), Js('Tambo'), Js('Tikho'), Js('Tima'), Js('To'), Js('Tobo'), Js('Tolya'), Js('Troi'), Js('Tu'), Js('Tua'), Js('Tuyma'), Js('Tve'), Js('Tyu'), Js('Ula'), Js('Ulya'), Js('Uso'), Js('Ussu'), Js('Ussuri'), Js('Uzlo'), Js('Veli'), Js('Vidno'), Js('Vladi'), Js('Volgo'), Js('Volo'), Js('Vorku'), Js('Voro'), Js('Voskre'), Js('Vse'), Js('Vsevo'), Js('Vya'), Js('Vybo'), Js('Yaku'), Js('Yaro'), Js('Yego'), Js('Yeka'), Js('Yekate'), Js('Yela'), Js('Yele'), Js('Yesse'), Js('Yu'), Js('Zare'), Js('Zele'), Js('Zeleno'), Js('Zhele'), Js('Zhelezno'), Js('Zhi'), Js('Zhigu'), Js('Zhuko'), Js('Zla')]))
var.put('nm2', Js([Js('bay'), Js('bey'), Js('binsk'), Js('birsk'), Js('bkin'), Js('bna'), Js('bnya'), Js('bodny'), Js('boksarsk'), Js('borg'), Js('buga'), Js('byshevsk'), Js('chensk'), Js('chkala'), Js('chny'), Js('dar'), Js('dedovo'), Js('dimir'), Js('dnoye'), Js('dny'), Js('dolsk'), Js('dorozhny'), Js('dovo'), Js('drinsk'), Js('drov'), Js('dzhan'), Js('gadan'), Js('gan'), Js('gansk'), Js('garsk'), Js('gda'), Js('ginsk'), Js('giyev'), Js('glebsk'), Js('godonsk'), Js('gorod'), Js('gorsk'), Js('grad'), Js('grosk'), Js('gulma'), Js('kala'), Js('kamensk'), Js('kamsk'), Js('kan'), Js('karino'), Js('kavkaz'), Js('khan'), Js('khladny'), Js('khna'), Js('khov'), Js('khovo'), Js('khtinsk'), Js('kin'), Js('kiye'), Js('kovo'), Js('kovsky'), Js('ksa'), Js('ksary'), Js('ksin'), Js('kutsk'), Js('labuga'), Js('lavat'), Js('lchik'), Js('lensk'), Js('leuz'), Js('liky'), Js('litamak'), Js('lkovo'), Js('lma'), Js('lovka'), Js('lovsk'), Js('lozhsk'), Js('lsk'), Js('ltaysk'), Js('luga'), Js('luk'), Js('lym'), Js('lyovsk'), Js('lzhsky'), Js('mara'), Js('mas'), Js('mbay'), Js('mbov'), Js('mkhovo'), Js('mki'), Js('mna'), Js('movsk'), Js('myssk'), Js('naksk'), Js('napa'), Js('ndzhik'), Js('netsk'), Js('nezh'), Js('ngelsk'), Js('ngrad'), Js('ngru'), Js('ninsk'), Js('nnovsk'), Js('nomyssk'), Js('novo'), Js('novsk'), Js('nrog'), Js('nsk'), Js('nskoy'), Js('nskoye'), Js('ntsovo'), Js('ntsy'), Js('nyev'), Js('nza'), Js('pa'), Js('petsk'), Js('peysk'), Js('pol'), Js('povets'), Js('prudny'), Js('pukhov'), Js('pul'), Js('pyevsk'), Js('ralsk'), Js('ransk'), Js('rapul'), Js('ratov'), Js('rbash'), Js('rbent'), Js('rechny'), Js('retsk'), Js('rga'), Js('rgan'), Js('rgut'), Js('rilsk'), Js('rino'), Js('rinsk'), Js('riysk'), Js('rkassk'), Js('rkuta'), Js('rmansk'), Js('rod'), Js('rodvinsk'), Js('rom'), Js('romorsk'), Js('rov'), Js('rovo'), Js('rovsk'), Js('rsk'), Js('rtau'), Js('rtovsk'), Js('rtsy'), Js('ry'), Js('ryevsk'), Js('ryol'), Js('rzhinsk'), Js('scow'), Js('sensk'), Js('shchensk'), Js('shchi'), Js('shevsk'), Js('shi'), Js('shikha'), Js('shin'), Js('shma'), Js('shny'), Js('shov'), Js('sinsk'), Js('ski'), Js('skovsk'), Js('skoye'), Js('slavl'), Js('snovy'), Js('snoy'), Js('ssosh'), Js('ssyisk'), Js('sta'), Js('stal'), Js('stroma'), Js('tamak'), Js('tim'), Js('tity'), Js('tkinsk'), Js('tlas'), Js('toust'), Js('tov'), Js('troitsk'), Js('trov'), Js('tsk'), Js('turynisk'), Js('tyevsk'), Js('vartovsk'), Js('vat'), Js('vaya'), Js('vda'), Js('versk'), Js('vets'), Js('vgrad'), Js('vichi'), Js('vir'), Js('vkar'), Js('vny'), Js('vo'), Js('vodsk'), Js('vostok'), Js('vropol'), Js('vrov'), Js('vsk'), Js('vskoy'), Js('vsky'), Js('vyurt'), Js('ya'), Js('yarsk'), Js('yev'), Js('yevka'), Js('yevsk'), Js('ylovka'), Js('ylovsk'), Js('ysk'), Js('yugansk'), Js('yungri'), Js('zan'), Js('zino'), Js('zma'), Js('znetsk'), Js('zniki'), Js('znogorsk'), Js('zny'), Js('zov'), Js('zovsky'), Js('zran'), Js('zuluk'), Js('zyl')]))
pass
pass


# Add lib to the module scope
russianTownNames = var.to_python()