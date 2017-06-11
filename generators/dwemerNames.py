__all__ = ['dwemerNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names3'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['names1', 'names2', 'tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names1', Js([Js('Akna'), Js('Alzi'), Js('Ara'), Js('Azsa'), Js('Blu'), Js('Bri'), Js('Byra'), Js('Bze'), Js('Cfra'), Js('Che'), Js('Chli'), Js('Chro'), Js('Chza'), Js('Cra'), Js('Csi'), Js('Czou'), Js('Da'), Js('Dou'), Js('Dre'), Js('Dri'), Js('Gli'), Js('Go'), Js('Grwe'), Js('Gzi'), Js('Ichu'), Js('Iora'), Js('Irda'), Js('Itho'), Js('Jare'), Js('Jo'), Js('Jri'), Js('Jza'), Js('Ka'), Js('Kri'), Js('Ksho'), Js('Kzua'), Js('Mhe'), Js('Mli'), Js('Mo'), Js('Mra'), Js('Na'), Js('Nhe'), Js('Nra'), Js('Nri'), Js('Rlo'), Js('Rue'), Js('Rya'), Js('Rzu'), Js('Shi'), Js('Shtro'), Js('So'), Js('Stre'), Js('Ta'), Js('Tae'), Js('Tche'), Js('Thri'), Js('Ylre'), Js('Yne'), Js('Yra'), Js('Yzra')]))
        var.put('names2', Js([Js('blan'), Js('brina'), Js('bryn'), Js('bwyr'), Js('dhis'), Js('dilan'), Js('dlen'), Js('dryna'), Js('drys'), Js('flis'), Js('frinn'), Js('ftris'), Js('fwinn'), Js('glas'), Js('glern'), Js('grida'), Js('griln'), Js('gven'), Js('gzis'), Js('hken'), Js('hner'), Js('hrada'), Js('hvlin'), Js('hzis'), Js('lamch'), Js('lirda'), Js('llez'), Js('lnif'), Js('lnmer'), Js('mchin'), Js('mdida'), Js('mris'), Js('mtrin'), Js('mzlin'), Js('nadis'), Js('ncha'), Js('nhatch'), Js('nrida'), Js('nvrin'), Js('nwess'), Js('rbira'), Js('rlis'), Js('rloar'), Js('rtes'), Js('rves'), Js('tchis'), Js('thanch'), Js('trech'), Js('trez'), Js('twern'), Js('vlara'), Js('vlen'), Js('vrash'), Js('vrin'), Js('vzal'), Js('zara'), Js('zlen'), Js('znara'), Js('zril'), Js('zshen')]))
    else:
        var.put('names1', Js([Js('Ancha'), Js('Atha'), Js('Achy'), Js('Agru'), Js('Bla'), Js('Bzra'), Js('Brazze'), Js('Bthu'), Js('Cuo'), Js('Cbra'), Js('Ctu'), Js('Cna'), Js('Chua'), Js('Chra'), Js('Chiu'), Js('Chu'), Js('Dzra'), Js('Da'), Js('Dha'), Js('Du'), Js('Gru'), Js('Gou'), Js('Ghro'), Js('Gha'), Js('Irha'), Js('Igre'), Js('Ingu'), Js('Ihle'), Js('Jna'), Js('Jru'), Js('Jhou'), Js('Jlare'), Js('Ka'), Js('Kagre'), Js('Kla'), Js('Kzya'), Js('Mi'), Js('Mzu'), Js('Mhu'), Js('Mcha'), Js('Nchu'), Js('Nchy'), Js('Ne'), Js('Nevi'), Js('Ra'), Js('Rku'), Js('Rhzo'), Js('Rale'), Js('Sza'), Js('Suo'), Js('Shtra'), Js('Stho'), Js('Tcha'), Js('Tzo'), Js('Tna'), Js('Tugra'), Js('Ya'), Js('Yra'), Js('Ytha'), Js('Yhna')]))
        var.put('names2', Js([Js('ban'), Js('bgar'), Js('bond'), Js('brec'), Js('dac'), Js('dchu'), Js('dgir'), Js('dit'), Js('drak'), Js('fgru'), Js('fk'), Js('frak'), Js('fuan'), Js('ggo'), Js('gr'), Js('grac'), Js('grath'), Js('grum'), Js('gvin'), Js('harn'), Js('hlac'), Js('hld'), Js('hrek'), Js('hrk'), Js('lbar'), Js('lchond'), Js('lec'), Js('len'), Js('lzrak'), Js('mac'), Js('mgar'), Js('min'), Js('mrond'), Js('muard'), Js('nac'), Js('nbric'), Js('nch'), Js('nd'), Js('ndam'), Js('nzgar'), Js('rd'), Js('ren'), Js('rhunch'), Js('rk'), Js('rlac'), Js('tchan'), Js('thas'), Js('thld'), Js('thunch'), Js('thzgar'), Js('vin'), Js('vith'), Js('vlar'), Js('vnak'), Js('vraz'), Js('zbrar'), Js('zdir'), Js('zgar'), Js('znak'), Js('zzefk')]))
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
var.put('names3', Js([Js('Aga'), Js('Alno'), Js('Asra'), Js('Aza'), Js('Ba'), Js('Bha'), Js('Bno'), Js('Bre'), Js('Care'), Js('Choa'), Js('Chra'), Js('Chru'), Js('Chze'), Js('Cra'), Js('Csto'), Js('Cza'), Js('Dju'), Js('Do'), Js('Dru'), Js('Dzre'), Js('Ge'), Js('Gra'), Js('Gri'), Js('Gzo'), Js('Ilze'), Js('Inra'), Js('Ishe'), Js('Izvu'), Js('Ja'), Js('Jho'), Js('Jle'), Js('Jra'), Js('Ko'), Js('Kre'), Js('Ksre'), Js('Kzre'), Js('Me'), Js('Mha'), Js('Mro'), Js('Mza'), Js('Nchu'), Js('Nhe'), Js('No'), Js('Nro'), Js('Ra'), Js('Rao'), Js('Rho'), Js('Ryu'), Js('Shra'), Js('Sne'), Js('Stu'), Js('Szo'), Js('Ta'), Js('Tcha'), Js('Tro'), Js('Tze'), Js('Ya'), Js('Ycho'), Js('Ynza'), Js('Yre')]))
var.put('names4', Js([Js('baln'), Js('bchasz'), Js('bnanch'), Js('bwarn'), Js('dchan'), Js('dlin'), Js('dras'), Js('drunz'), Js('dzach'), Js('fnyg'), Js('frach'), Js('frysz'), Js('furn'), Js('garn'), Js('glan'), Js('glynsh'), Js('grenz'), Js('grozsch'), Js('gwetch'), Js('hatch'), Js('hnch'), Js('hretz'), Js('hron'), Js('huanch'), Js('larn'), Js('lchanf'), Js('lratz'), Js('lrohn'), Js('lzarf'), Js('maratzch'), Js('mgunch'), Js('morn'), Js('mratz'), Js('mrumhz'), Js('nard'), Js('ngnthumz'), Js('nrazg'), Js('nruz'), Js('nrynn'), Js('nzcharn'), Js('rach'), Js('rhytz'), Js('rlakch'), Js('rlatz'), Js('rzhurk'), Js('tarn'), Js('tchatz'), Js('tchzan'), Js('thurzch'), Js('tvar'), Js('varn'), Js('vnorz'), Js('vragch'), Js('vretch'), Js('vzyrn'), Js('zalf'), Js('zchyn'), Js('zhurz'), Js('zlurch'), Js('ztar')]))
pass
pass


# Add lib to the module scope
dwemerNames = var.to_python()