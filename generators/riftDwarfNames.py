__all__ = ['riftDwarfNames']

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
    var.registers(['names1', 'names2', 'tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names1', Js([Js('Ale'), Js('Ali'), Js('A'), Js('Ba'), Js('Bari'), Js('Be'), Js('Bi'), Js('Bise'), Js('Bo'), Js('Bohu'), Js('Bori'), Js('Boza'), Js('Bra'), Js('Brani'), Js('Bre'), Js('Bro'), Js('Da'), Js('Dani'), Js('Dari'), Js('De'), Js('Deni'), Js('Dobri'), Js('Do'), Js('Dobro'), Js('Dra'), Js('Draga'), Js('Draho'), Js('Du'), Js('Dusa'), Js('Eli'), Js('Ela'), Js('Go'), Js('Gora'), Js('Gro'), Js('Gra'), Js('Ida'), Js('Iva'), Js('Ja'), Js('Jani'), Js('Jale'), Js('Jase'), Js('Jele'), Js('Ka'), Js('Kali'), Js('Ke'), Js('La'), Js('Le'), Js('Li'), Js('Ma'), Js('Mali'), Js('Me'), Js('Meli'), Js('Mi'), Js('Mila'), Js('Mile'), Js('Miru'), Js('Mo'), Js('Mora'), Js('Ne'), Js('Neve'), Js('O'), Js('Ole'), Js('Ra'), Js('Radi'), Js('Ro'), Js('Rosi'), Js('Ru'), Js('Rumi'), Js('Se'), Js('Sta'), Js('Stani'), Js('Suda'), Js('Su'), Js('Ti'), Js('Tiha'), Js('Tu'), Js('Va'), Js('Ve'), Js('Veli'), Js('Bo'), Js('Borghi'), Js('Bry'), Js('Ei'), Js('Fre'), Js('Ge'), Js('Gri'), Js('Gro'), Js('Gu'), Js('Hei'), Js('Hi'), Js('Hu'), Js('Na'), Js('Sa'), Js('Si'), Js('Ska'), Js('Sva'), Js('Ve')]))
        var.put('names2', Js([Js('bla'), Js('bra'), Js('briana'), Js('bromira'), Js('dana'), Js('dandi'), Js('dania'), Js('danka'), Js('dda'), Js('dka'), Js('dmila'), Js('domia'), Js('domira'), Js('drana'), Js('drun'), Js('duna'), Js('dunn'), Js('ga'), Js('gana'), Js('gdana'), Js('ghild'), Js('ghildr'), Js('gna'), Js('gny'), Js('grun'), Js('ha'), Js('hana'), Js('hild'), Js('hildr'), Js('homira'), Js('humira'), Js('jana'), Js('kadi'), Js('ksana'), Js('kuld'), Js('lana'), Js('lda'), Js('ldr'), Js('lena'), Js('lenka'), Js('lica'), Js('lika'), Js('lina'), Js('linka'), Js('lmira'), Js('mbla'), Js('mena'), Js('mhild'), Js('mhildr'), Js('miana'), Js('mila'), Js('mira'), Js('na'), Js('nca'), Js('nhild'), Js('nhildr'), Js('nia'), Js('nica'), Js('nika'), Js('nimira'), Js('nka'), Js('nna'), Js('nuska'), Js('ra'), Js('rana'), Js('ranka'), Js('rdandi'), Js('reyja'), Js('ria'), Js('riana'), Js('rid'), Js('rigg'), Js('rina'), Js('rinka'), Js('ritza'), Js('rka'), Js('rmila'), Js('romira'), Js('runa'), Js('ruska'), Js('rvara'), Js('rya'), Js('rzanna'), Js('sana'), Js('senka'), Js('sera'), Js('serka'), Js('sica'), Js('ska'), Js('tka'), Js('tza'), Js('vana'), Js('vara'), Js('vena'), Js('venka'), Js('zana'), Js('zanna'), Js('zda'), Js('zdana'), Js('zena'), Js('zhana'), Js('zka')]))
    else:
        var.put('names1', Js([Js('Ba'), Js('Be'), Js('Bi'), Js('Bla'), Js('Bo'), Js('Bogo'), Js('Bohu'), Js('Boji'), Js('Bozhi'), Js('Bozi'), Js('Bra'), Js('Bre'), Js('Bu'), Js('Budi'), Js('Buri'), Js('Ca'), Js('Casi'), Js('Da'), Js('Dali'), Js('De'), Js('Di'), Js('Do'), Js('Dobro'), Js('Dra'), Js('Fre'), Js('Ga'), Js('Go'), Js('Gode'), Js('Gra'), Js('Gro'), Js('Gu'), Js('Ja'), Js('Jaro'), Js('Ka'), Js('Kazi'), Js('Kra'), Js('Krasi'), Js('Kre'), Js('Kresi'), Js('Lo'), Js('Lu'), Js('Lubo'), Js('Ludo'), Js('Ma'), Js('Mi'), Js('Milo'), Js('Mo'), Js('Nja'), Js('Njo'), Js('O'), Js('Ode'), Js('Odi'), Js('Ogni'), Js('Orva'), Js('Pa'), Js('Pre'), Js('Pro'), Js('Ra'), Js('Radi'), Js('Rado'), Js('Si'), Js('Sta'), Js('Stani'), Js('Straa'), Js('Tho'), Js('Ty'), Js('Va'), Js('Ve'), Js('Veli'), Js('Vi'), Js('Volu'), Js('Za'), Js('Ze'), Js('Zeli'), Js('Zi'), Js('Zito')]))
        var.put('names2', Js([Js('ban'), Js('bomir'), Js('bor'), Js('borek'), Js('brad'), Js('bren'), Js('brin'), Js('bromir'), Js('cimir'), Js('dalf'), Js('dan'), Js('dar'), Js('darr'), Js('dek'), Js('demir'), Js('der'), Js('dik'), Js('dim'), Js('dimir'), Js('dinn'), Js('domer'), Js('domir'), Js('dos'), Js('dovan'), Js('dran'), Js('dzimir'), Js('gan'), Js('gdan'), Js('gisa'), Js('gnian'), Js('go'), Js('gomil'), Js('gomir'), Js('gotin'), Js('goy'), Js('grun'), Js('gumil'), Js('gun'), Js('gurd'), Js('gutin'), Js('gvi'), Js('hdan'), Js('himir'), Js('homir'), Js('hos'), Js('hren'), Js('humer'), Js('humil'), Js('humir'), Js('jan'), Js('jek'), Js('jidar'), Js('lek'), Js('libor'), Js('lik'), Js('limir'), Js('lin'), Js('ljan'), Js('lko'), Js('lon'), Js('lorad'), Js('los'), Js('lovan'), Js('lund'), Js('lundr'), Js('lyan'), Js('mard'), Js('mek'), Js('mer'), Js('mil'), Js('mir'), Js('narr'), Js('nat'), Js('ndri'), Js('nek'), Js('nik'), Js('nimir'), Js('nko'), Js('nnarr'), Js('ran'), Js('rban'), Js('rce'), Js('rek'), Js('rey'), Js('reyr'), Js('rian'), Js('rik'), Js('ril'), Js('rin'), Js('ris'), Js('rko'), Js('rlin'), Js('romer'), Js('romir'), Js('ros'), Js('rut'), Js('rvan'), Js('rvar'), Js('rwan'), Js('ser'), Js('simir'), Js('stan'), Js('tek'), Js('tik'), Js('tomir'), Js('van'), Js('vis'), Js('vor'), Js('vril'), Js('wan'), Js('zan'), Js('zdan'), Js('zen'), Js('zhil'), Js('zhin'), Js('zidar'), Js('zimir'), Js('zydar')]))
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
pass
pass


# Add lib to the module scope
riftDwarfNames = var.to_python()