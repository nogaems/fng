__all__ = ['enochianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
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
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aaan'), Js('Aadt'), Js('Aaetpio'), Js('Aanaa'), Js('Aaodt'), Js('Aaoxaif'), Js('Aavan'), Js('Aavna'), Js('Aax'), Js('Abamo'), Js('Abaoz'), Js('Abmo'), Js('Aboz'), Js('Acar'), Js('Acca'), Js('Acmbicu'), Js('Acps'), Js('Acrar'), Js('Acuca'), Js('Acups'), Js('Aczinor'), Js('Adaeoet'), Js('Adi'), Js('Adire'), Js('Adnop'), Js('Adop'), Js('Adopa'), Js('Adota'), Js('Adre'), Js('Adta'), Js('Agb'), Js('Aglm'), Js('Agmlm'), Js('Ahaozpi'), Js('Aiaoai Oiiit'), Js('Aigra'), Js('Aira'), Js('Amox'), Js('Amsox'), Js('Ancro'), Js('Animotix'), Js('Anpiel'), Js('Anvaa'), Js('Apa'), Js('Apahr'), Js('Apdoce'), Js('Aphr'), Js('Aplst'), Js('Apm'), Js('Apst'), Js('Arizl'), Js('Arn'), Js('Arylic'), Js('Arzl'), Js('Ataad'), Js('Atdim'), Js('Ato'), Js('Avtotar'), Js('Baradiel'), Js('Barnabas'), Js('Bataivah'), Js('Bivhd'), Js('Brap'), Js('Brcn'), Js('Briap'), Js('Cadaamp'), Js('Camael'), Js('Castiel'), Js('Cms'), Js('Cnabr'), Js('Cnbr'), Js('Cpsa'), Js('Cpusa'), Js('Diari'), Js('Dimnt'), Js('Dimt'), Js('Diom'), Js('Diri'), Js('Dixom'), Js('Dmx'), Js('Dolop'), Js('Donpa'), Js('Doop'), Js('Dopa'), Js('Dtaa'), Js('Dtoaa'), Js('Dxagz'), Js('Dxgz'), Js('Eac'), Js('Eboza'), Js('Ecanus'), Js('Ecaop'), Js('Ecop'), Js('Edlprnaa'), Js('Ephra'), Js('Erg'), Js('Ern'), Js('Erubey'), Js('Erzla'), Js('Eutpa'), Js('Exarp'), Js('Exr'), Js('Faax'), Js('Fmnd'), Js('Gabriel'), Js('Galgalliel'), Js('Gbal'), Js('Gbeal'), Js('Glma'), Js('Glmma'), Js('Gmdnm'), Js('Habioro'), Js('Hbr'), Js('Hcnbr'), Js('Hcoma'), Js('Hipotga'), Js('Hraap'), Js('Hrap'), Js('Hroan'), Js('Hru'), Js('Htmorda'), Js('Hua'), Js('Hxgzd'), Js('Iczhihal'), Js('Imntd'), Js('Imtd'), Js('Izaz'), Js('Izinr'), Js('Izixp'), Js('Iznr'), Js('Izraz'), Js('Izxp'), Js('Kokabiel'), Js('Lairz'), Js('Lang'), Js('Laoaxrp'), Js('Larz'), Js('Lavavoth'), Js('Leaoc'), Js('Leoc'), Js('Levanael'), Js('Ligdisa'), Js('Lmag'), Js('Lmmag'), Js('Lsraphm'), Js('Masgm'), Js('Mgam'), Js('Michael'), Js('Miz'), Js('Mma'), Js('Msal'), Js('Msmal'), Js('Mtdi'), Js('Mtndi'), Js('Mto'), Js('Naaa'), Js('Nanta'), Js('Naoo'), Js('Naooo'), Js('Navaa'), Js('Nbarc'), Js('Nbrc'), Js('Ndazn'), Js('Ndzn'), Js('Nhdd'), Js('Nhodd'), Js('Nlirx'), Js('Nlrx'), Js('Npat'), Js('Nrcoa'), Js('Nroa'), Js('Oacnr'), Js('Oanr'), Js('Oap'), Js('Obgota Aabco'), Js('Ocnm'), Js('Omagg'), Js('Omgg'), Js('Omia'), Js('Omsia'), Js('Ona'), Js('Onh'), Js('Onp'), Js('Oodpz'), Js('Oopz'), Js('Opad'), Js('Opama'), Js('Opamn'), Js('Ophaniel'), Js('Opmn'), Js('Opna'), Js('Opnad'), Js('Ormn'), Js('Oro Ibah Aozpi'), Js('Orpmn'), Js('Otoi'), Js('Otroi'), Js('Oyaub'), Js('Oyub'), Js('Ozaab'), Js('Ozab'), Js('Paco'), Js('Pado'), Js('Paeoc'), Js('Paico'), Js('Piz'), Js('Pmagl'), Js('Pmox'), Js('Pmzox'), Js('Ppsac'), Js('Raagiosl'), Js('Raph'), Js('Raphael'), Js('Rbnh'), Js('Rbznh'), Js('Rcanb'), Js('Rcnb'), Js('Rda'), Js('Rgan'), Js('Rgoan'), Js('Rlemu'), Js('Rlmu'), Js('Rpa'), Js('Rrb'), Js('Rrl'), Js('Rsi'), Js('Rsni'), Js('Rsoni'), Js('Ruoi'), Js('Ruroi'), Js('Rxao'), Js('Rxinl'), Js('Rxnl'), Js('Rxp'), Js('Rxpao'), Js('Rzila'), Js('Rzionr Nrzfm'), Js('Rzla'), Js('Saaiz'), Js('Sacp'), Js('Saiinou'), Js('Saiinov'), Js('Saucp'), Js('Scmio'), Js('Shonda'), Js('Siosp'), Js('Sisp'), Js('Slgaiol'), Js('Soniznt'), Js('Tdim'), Js('Tdnim'), Js('Tpau'), Js('Tplau'), Js('Uriel'), Js('Uspsn'), Js('Ussn'), Js('Utipa'), Js('Utpa'), Js('Uvb'), Js('Vaasa'), Js('Vasa'), Js('Volxdo Sioda'), Js('Xai'), Js('Xcz'), Js('Xdz'), Js('Xgazd'), Js('Xgzd'), Js('Xii'), Js('Xnilr'), Js('Xom'), Js('Xoy'), Js('Xpa'), Js('Xpaxn'), Js('Xpcn'), Js('Xrinh'), Js('Xrnh'), Js('Xxan'), Js('Yasen'), Js('Zaabo'), Js('Zabo'), Js('Zarnaah'), Js('Zarzi'), Js('Zarzilg'), Js('Zazi'), Js('Zdaxg'), Js('Zdxg'), Js('Zedekiel'), Js('Zinggen'), Js('Ziracah'), Js('Zirz'), Js('Ziza'), Js('Zurchol')]))
pass
pass


# Add lib to the module scope
enochianNames = var.to_python()