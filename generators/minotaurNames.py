__all__ = ['minotaurNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2'))))
                else:
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
var.put('nm1', Js([Js('Ar'), Js('Are'), Js('Ba'), Js('Bra'), Js('Bri'), Js('Da'), Js('Dha'), Js('Dra'), Js('Dri'), Js('Dru'), Js('Gar'), Js('Gara'), Js('Gna'), Js('Gnar'), Js('Gno'), Js('Gnu'), Js('Gra'), Js('Gri'), Js('Gru'), Js('Gun'), Js('Hon'), Js('Hun'), Js('Ja'), Js('Jan'), Js('Jar'), Js('Kal'), Js('Kan'), Js('Kha'), Js('Khu'), Js('Kon'), Js('Kul'), Js('Man'), Js('Min'), Js('Mo'), Js('Moh'), Js('Mohr'), Js('Mon'), Js('Mu'), Js('Mun'), Js('Mur'), Js('Na'), Js('Ni'), Js('No'), Js('Nohr'), Js('Nu'), Js('Nur'), Js('Par'), Js('Pra'), Js('Pru'), Js('Ra'), Js('Rahd'), Js('Ran'), Js('Rat'), Js('Ren'), Js('Ret'), Js('Ri'), Js('Ril'), Js('Ro'), Js('Ru'), Js('Rut'), Js('Sir'), Js('Su'), Js('Sur'), Js('Sy'), Js('Syn'), Js('Syr'), Js('Te'), Js('Tin'), Js('Tra'), Js('Tu'), Js('Tuhr'), Js('Tun'), Js('Tur'), Js('Ty'), Js('Tyr'), Js('Va'), Js('Vo'), Js('Vra'), Js('Vru'), Js('Vu'), Js('Vy'), Js('Vyr'), Js('Wan'), Js('War'), Js('Wra'), Js('Wri'), Js('Wru'), Js('Wry'), Js('Wu'), Js('Wun'), Js('Wur'), Js('Wy'), Js('Wyr'), Js('Xa'), Js('Xin'), Js('Xu'), Js('Xur'), Js('Xy'), Js('Za'), Js('Zam'), Js('Zan'), Js('Zu'), Js('Zun'), Js('Zy'), Js('Zyr')]))
var.put('nm2', Js([Js('ban'), Js('bur'), Js('barun'), Js('baruk'), Js('buk'), Js('bur'), Js('bor'), Js('dor'), Js('duk'), Js('drun'), Js('dius'), Js('bius'), Js('bus'), Js('dus'), Js('dir'), Js('drak'), Js('dax'), Js('diax'), Js('frad'), Js('farak'), Js('gun'), Js('grak'), Js('garan'), Js('garak'), Js('gur'), Js('grin'), Js('grim'), Js('gon'), Js('jur'), Js('jak'), Js('jag'), Js('jius'), Js('jus'), Js('kius'), Js('kus'), Js('kiras'), Js('kirus'), Js('kas'), Js('kurun'), Js('kud'), Js('kod'), Js('kohr'), Js('khius'), Js('khus'), Js('mius'), Js('mus'), Js('meus'), Js('muk'), Js('maruk'), Js('mud'), Js('miud'), Js('mun'), Js('myr'), Js('myar'), Js('mier'), Js('mak'), Js('neus'), Js('nus'), Js('nius'), Js('nuk'), Js('nur'), Js('nuran'), Js('narak'), Js('nas'), Js('nax'), Js('max'), Js('nyr'), Js('nag'), Js('phas'), Js('phius'), Js('pheus'), Js('phus'), Js('pius'), Js('peus'), Js('prak'), Js('parak'), Js('prix'), Js('rad'), Js('ruk'), Js('radak'), Js('ras'), Js('rius'), Js('reus'), Js('rus'), Js('rios'), Js('rath'), Js('rakar'), Js('rag'), Js('ragar'), Js('rug'), Js('rahg'), Js('raz'), Js('rax'), Js('ryx'), Js('rox'), Js('sius'), Js('sus'), Js('seus'), Js('sus'), Js('sag'), Js('sug'), Js('sur'), Js('sar'), Js('tor'), Js('thur'), Js('tir'), Js('trak'), Js('tagar'), Js('tarak'), Js('truk'), Js('tus'), Js('tius'), Js('teus'), Js('tin'), Js('tak'), Js('vak'), Js('vius'), Js('veus'), Js('vis'), Js('vur'), Js('vas'), Js('zius'), Js('zeus'), Js('zus'), Js('zak'), Js('zur'), Js('zan'), Js('zun')]))
var.put('nm3', Js([Js('Aer'), Js('Ane'), Js('Bae'), Js('Bera'), Js('Bli'), Js('De'), Js('Dhi'), Js('Dra'), Js('Dre'), Js('Dry'), Js('Ger'), Js('Gera'), Js('Gna'), Js('Gne'), Js('Gner'), Js('Gni'), Js('Gra'), Js('Gre'), Js('Gren'), Js('Gri'), Js('Hel'), Js('Hil'), Js('Hin'), Js('Jer'), Js('Jin'), Js('Kal'), Js('Kan'), Js('Kel'), Js('Kha'), Js('Khe'), Js('Kon'), Js('Mae'), Js('Me'), Js('Mehr'), Js('Men'), Js('Min'), Js('Mir'), Js('Moh'), Js('Mol'), Js('Na'), Js('Nehl'), Js('Nes'), Js('Ni'), Js('Nia'), Js('No'), Js('Pha'), Js('Phe'), Js('Phi'), Js('Phra'), Js('Pre'), Js('Pri'), Js('Ran'), Js('Reh'), Js('Rel'), Js('Res'), Js('Rhe'), Js('Ri'), Js('Rihl'), Js('Rin'), Js('Ris'), Js('Ro'), Js('She'), Js('Shy'), Js('Sil'), Js('Syl'), Js('Syn'), Js('Syr'), Js('Te'), Js('Tel'), Js('Ten'), Js('The'), Js('Tis'), Js('Trae'), Js('Trih'), Js('Ty'), Js('Tys'), Js('Va'), Js('Ve'), Js('Vo'), Js('Vre'), Js('Vry'), Js('Vy'), Js('Vyl'), Js('Wa'), Js('Waer'), Js('Wan'), Js('Was'), Js('Wen'), Js('Wi'), Js('Wre'), Js('Wri'), Js('Wry'), Js('Wy'), Js('Wys'), Js('Xa'), Js('Xe'), Js('Xel'), Js('Xil'), Js('Xy'), Js('Za'), Js('Zam'), Js('Zan'), Js('Zen'), Js('Zha'), Js('Zy'), Js('Zyl')]))
var.put('nm4', Js([Js('barin'), Js('bea'), Js('bei'), Js('ben'), Js('bes'), Js('bis'), Js('bise'), Js('bur'), Js('bura'), Js('dea'), Js('deha'), Js('den'), Js('dia'), Js('dira'), Js('dis'), Js('dris'), Js('dya'), Js('fera'), Js('frae'), Js('gara'), Js('garis'), Js('gea'), Js('gen'), Js('gera'), Js('geth'), Js('gres'), Js('ja'), Js('jei'), Js('jia'), Js('jice'), Js('kea'), Js('kena'), Js('kes'), Js('keth'), Js('khia'), Js('khis'), Js('kira'), Js('kis'), Js('ko'), Js('kohn'), Js('ma'), Js('mara'), Js('mas'), Js('mel'), Js('mes'), Js('meth'), Js('mia'), Js('mien'), Js('min'), Js('mira'), Js('mis'), Js('mya'), Js('mys'), Js('naga'), Js('nara'), Js('nea'), Js('nes'), Js('ness'), Js('neth'), Js('nira'), Js('niras'), Js('nis'), Js('nith'), Js('nys'), Js('para'), Js('pea'), Js('phas'), Js('pheras'), Js('phes'), Js('phin'), Js('phis'), Js('pia'), Js('pria'), Js('ra'), Js('rada'), Js('rae'), Js('rah'), Js('rala'), Js('ran'), Js('rasha'), Js('rea'), Js('rena'), Js('res'), Js('resh'), Js('reth'), Js('ria'), Js('ris'), Js('rya'), Js('ryl'), Js('sa'), Js('sara'), Js('sen'), Js('sesh'), Js('sia'), Js('sien'), Js('sira'), Js('sis'), Js('tana'), Js('tera'), Js('tes'), Js('teus'), Js('thea'), Js('tia'), Js('tin'), Js('tis'), Js('tish'), Js('tren'), Js('tris'), Js('vash'), Js('ven'), Js('vera'), Js('ves'), Js('via'), Js('vien'), Js('zana'), Js('zel'), Js('zen'), Js('zeph'), Js('zera'), Js('zia'), Js('zis')]))
var.put('nm5', Js([Js('Ag'), Js('Al'), Js('Ba'), Js('Be'), Js('Ben'), Js('De'), Js('Dhe'), Js('Dhi'), Js('Dra'), Js('Dro'), Js('Gen'), Js('Ger'), Js('Gin'), Js('Gna'), Js('Gne'), Js('Gra'), Js('Gre'), Js('Gren'), Js('Gri'), Js('Hal'), Js('Has'), Js('Hon'), Js('Jan'), Js('Jen'), Js('Kal'), Js('Kan'), Js('Kel'), Js('Ker'), Js('Kha'), Js('Kon'), Js('Ma'), Js('Mahr'), Js('Man'), Js('Mas'), Js('Me'), Js('Mer'), Js('Min'), Js('Mon'), Js('Na'), Js('Nal'), Js('Nar'), Js('Ni'), Js('No'), Js('Nor'), Js('Pa'), Js('Par'), Js('Per'), Js('Pha'), Js('Pra'), Js('Pre'), Js('Ram'), Js('Ran'), Js('Ras'), Js('Reg'), Js('Rel'), Js('Ren'), Js('Rho'), Js('Ri'), Js('Rin'), Js('Ro'), Js('Sal'), Js('Sar'), Js('Sen'), Js('Sil'), Js('Syn'), Js('Syr'), Js('Te'), Js('Tel'), Js('Ten'), Js('Tha'), Js('Tir'), Js('Tra'), Js('Tri'), Js('Ty'), Js('Tyn'), Js('Va'), Js('Ve'), Js('Ven'), Js('Vo'), Js('Vra'), Js('Vri'), Js('Vy'), Js('Wa'), Js('Wal'), Js('Wen'), Js('Wer'), Js('Wes'), Js('Wi'), Js('Win'), Js('Wre'), Js('Wy'), Js('Wyn'), Js('Xa'), Js('Xe'), Js('Xel'), Js('Xil'), Js('Xy'), Js('Za'), Js('Zam'), Js('Zan'), Js('Zen'), Js('Zha'), Js('Zy'), Js('Zyl')]))
var.put('nm6', Js([Js('ba'), Js('ban'), Js('ben'), Js('ber'), Js('beth'), Js('bin'), Js('bis'), Js('bith'), Js('da'), Js('del'), Js('den'), Js('des'), Js('dis'), Js('dith'), Js('dres'), Js('dyn'), Js('fer'), Js('fra'), Js('ga'), Js('gan'), Js('gen'), Js('ger'), Js('ges'), Js('geth'), Js('gres'), Js('ja'), Js('jas'), Js('jia'), Js('jis'), Js('ka'), Js('kan'), Js('kas'), Js('keas'), Js('kel'), Js('ken'), Js('kha'), Js('khes'), Js('kir'), Js('kohn'), Js('ma'), Js('mal'), Js('mar'), Js('mara'), Js('mas'), Js('mes'), Js('mian'), Js('min'), Js('mir'), Js('mis'), Js('mor'), Js('myas'), Js('mys'), Js('na'), Js('nag'), Js('nar'), Js('ned'), Js('nes'), Js('neth'), Js('nig'), Js('nir'), Js('nis'), Js('nith'), Js('nys'), Js('pan'), Js('par'), Js('pas'), Js('phas'), Js('pheran'), Js('phes'), Js('phin'), Js('phis'), Js('ra'), Js('rada'), Js('rah'), Js('raja'), Js('ral'), Js('ran'), Js('ras'), Js('rash'), Js('rasha'), Js('ren'), Js('rena'), Js('res'), Js('rija'), Js('rith'), Js('ryan'), Js('ryn'), Js('sal'), Js('sar'), Js('sen'), Js('sien'), Js('sin'), Js('sir'), Js('sis'), Js('tara'), Js('taren'), Js('ten'), Js('tera'), Js('tes'), Js('teus'), Js('tha'), Js('tin'), Js('tish'), Js('tix'), Js('tres'), Js('vas'), Js('vel'), Js('ven'), Js('ver'), Js('vin'), Js('vir'), Js('zan'), Js('zel'), Js('zen'), Js('zeph'), Js('zera'), Js('zia'), Js('zis')]))
pass
pass


# Add lib to the module scope
minotaurNames = var.to_python()