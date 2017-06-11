__all__ = ['orcWowNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', (((((var.get('nm4').get(var.get('rnd4'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
            else:
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd4'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd6')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aggu'), Js('Agu'), Js('Ar'), Js('Arn'), Js('Aso'), Js('At'), Js('Atru'), Js('Bar'), Js('Bel'), Js('Bo'), Js('Bor'), Js('Brak'), Js('Ca'), Js('Cra'), Js('Do'), Js('Dor'), Js('Dra'), Js('Du'), Js('Dur'), Js('Ga'), Js('Gal'), Js('Gan'), Js('Gar'), Js('Go'), Js('Gor'), Js('Got'), Js('Gram'), Js('Grim'), Js('Gro'), Js('Grom'), Js('Gru'), Js('Gul'), Js('Hag'), Js('Han'), Js('Har'), Js('Hog'), Js('Hon'), Js('Hor'), Js('Hun'), Js('Hur'), Js('Ka'), Js('Kal'), Js('Kam'), Js('Kar'), Js('Karo'), Js('Kel'), Js('Kil'), Js('Ko'), Js('Kom'), Js('Kor'), Js('Kra'), Js('Kru'), Js('Ku'), Js('Kul'), Js('Kur'), Js('La'), Js('Lam'), Js('Lu'), Js('Lum'), Js('Ma'), Js('Mag'), Js('Mahl'), Js('Mak'), Js('Mal'), Js('Mar'), Js('Mo'), Js('Mog'), Js('Mok'), Js('Mor'), Js('Mu'), Js('Mug'), Js('Muk'), Js('Mura'), Js('Nee'), Js('Oggu'), Js('Ogu'), Js('Ok'), Js('Oko'), Js('Olla'), Js('Or'), Js('Oro'), Js('Rek'), Js('Ron'), Js('Rona'), Js('Sa'), Js('Sar'), Js('So'), Js('Sor'), Js('Tha'), Js('Thar'), Js('Ther'), Js('Thra'), Js('Thro'), Js('Thru'), Js('Thu'), Js('Thur'), Js('Trak'), Js('Truk'), Js('Uk'), Js('Uko'), Js('Ukra'), Js('Ukru'), Js('Ulla'), Js('Ur'), Js('Urtha'), Js('Urthu'), Js('Urtra'), Js('Urtru'), Js('Za'), Js('Zar'), Js('Zas'), Js('Zav'), Js('Zev'), Js('Zor'), Js('Zu'), Js('Zur'), Js('Zus')]))
var.put('nm2', Js([Js('d'), Js('dar'), Js('dur'), Js('g'), Js('gar'), Js('gur'), Js('l'), Js('m'), Js('mar'), Js('mur'), Js('n'), Js('nar'), Js('nur'), Js('t'), Js('tar'), Js('tur'), Js('z'), Js('zar'), Js('zur'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm3', Js([Js("'Dar"), Js("'Dur"), Js("'Gald"), Js("'Gan"), Js("'Gar"), Js("'Geld"), Js("'Gen"), Js("'Gor"), Js("'Guld"), Js("'Gun"), Js("'Phan"), Js("'Ral"), Js("'Raz"), Js("'Rul"), Js("'Ruz"), Js("'Tar"), Js("'Thak"), Js("'Thuk"), Js("'Thunk"), Js("'Tur"), Js('ada'), Js('agg'), Js('agus'), Js('ak'), Js('ald'), Js('am'), Js('an'), Js('ar'), Js('arg'), Js('arl'), Js('arm'), Js('aro'), Js('aru'), Js('as'), Js('ath'), Js('ban'), Js('da'), Js('dan'), Js('dar'), Js('dok'), Js('dor'), Js('dran'), Js('du'), Js('dur'), Js('eld'), Js('eth'), Js('far'), Js('fu'), Js('ful'), Js('fur'), Js('gal'), Js('gald'), Js('gam'), Js('gan'), Js('gas'), Js('geld'), Js('gen'), Js('gor'), Js('gorm'), Js('gorn'), Js('gosh'), Js('grom'), Js('gron'), Js('gul'), Js('guld'), Js('gum'), Js('gun'), Js('gus'), Js('kada'), Js('kuda'), Js('l'), Js('lach'), Js('lak'), Js('lek'), Js('loch'), Js('ma'), Js('mak'), Js('mar'), Js('mok'), Js('nok'), Js('ogg'), Js('ok'), Js('okk'), Js('olak'), Js('olek'), Js('om'), Js('oram'), Js('oran'), Js('osh'), Js('ost'), Js('phan'), Js('phon'), Js('phun'), Js('rak'), Js('ram'), Js('ramm'), Js('ran'), Js('ras'), Js('rek'), Js('ri'), Js('rom'), Js('romm'), Js('rosh'), Js('rost'), Js('ru'), Js('ruk'), Js('rum'), Js('rumm'), Js('rus'), Js('stan'), Js('tar'), Js('thak'), Js('thas'), Js('thos'), Js('thuk'), Js('thus'), Js('ton'), Js('tor'), Js('tunk'), Js('tur'), Js('u'), Js('ud'), Js('uda'), Js('ugg'), Js('uk'), Js('ul'), Js('uld'), Js('um'), Js('urg'), Js('urk'), Js('url'), Js('urm'), Js('uro'), Js('us'), Js('uwd'), Js('var'), Js('ven'), Js('vor'), Js('zal'), Js('zok'), Js('zul')]))
var.put('nm4', Js([Js('Al'), Js('El'), Js('Fal'), Js('Fel'), Js('Fol'), Js('Ful'), Js('Ga'), Js('Gar'), Js('Gi'), Js('Gija'), Js('Go'), Js('Gor'), Js('Gre'), Js('Gro'), Js('Gry'), Js('Kar'), Js('Kat'), Js('Ker'), Js('Ket'), Js('Ki'), Js('Kir'), Js('Kot'), Js('Kur'), Js('Kut'), Js('Mer'), Js('Mir'), Js('Mor'), Js('Ol'), Js('Ra'), Js('Rah'), Js('Rahk'), Js('Ras'), Js('Rash'), Js('Raw'), Js('Ro'), Js('Roh'), Js('Rohk'), Js('Ru'), Js('Sa'), Js('Sam'), Js('San'), Js('Se'), Js('Sem'), Js('Sen'), Js('Sha'), Js('Shay'), Js('She'), Js('Shi'), Js('Shu'), Js('Sin'), Js('Su'), Js('Sum'), Js('Sun'), Js('Tam'), Js('Tem'), Js('Tu'), Js('Tum'), Js('Um'), Js('Uma'), Js('Ur'), Js('Ure'), Js('Zan'), Js('Zen'), Js('Zon'), Js('Zun')]))
var.put('nm6', Js([Js("'Kuma"), Js("'Kuna"), Js("'Kuno"), Js("'Te"), Js("'Ti"), Js("'Tur"), Js("'Ula"), Js("'Ulo"), Js('adu'), Js('aja'), Js('aju'), Js('ala'), Js('ami'), Js('ano'), Js('anu'), Js('ar'), Js('atra'), Js('das'), Js('des'), Js('dis'), Js('dras'), Js('dres'), Js('dris'), Js('drus'), Js('dus'), Js('eda'), Js('edo'), Js('ija'), Js('ika'), Js('iko'), Js('iku'), Js('ila'), Js('ile'), Js('ilu'), Js('ina'), Js('ino'), Js('inu'), Js('ira'), Js('iro'), Js('iru'), Js('is'), Js('kaja'), Js('kajo'), Js('kamo'), Js('kano'), Js('kes'), Js('ket'), Js('kis'), Js('kit'), Js('kuja'), Js('kuji'), Js('kujo'), Js('kuma'), Js('kumo'), Js('kuna'), Js('kuno'), Js('kys'), Js('lika'), Js('liko'), Js('liku'), Js('na'), Js('nae'), Js('nar'), Js('ner'), Js('nor'), Js('oda'), Js('odu'), Js('ona'), Js('onu'), Js('os'), Js('otra'), Js('ra'), Js('ras'), Js('res'), Js('ris'), Js('ros'), Js('rus'), Js('shka'), Js('strom'), Js('tar'), Js('thas'), Js('thes'), Js('thos'), Js('thus'), Js('tra'), Js('uda'), Js('udo'), Js('uja'), Js('ujo'), Js('ula'), Js('ulo'), Js('ume'), Js('umi'), Js('una'), Js('us'), Js('via'), Js('vio'), Js('viu'), Js('yja'), Js('yl'), Js('yla'), Js('yle'), Js('ylu'), Js('yna'), Js('yno'), Js('ynu'), Js('yra'), Js('yro'), Js('yru')]))
var.put('nm7', Js([Js('Axe'), Js('Battle'), Js('Black'), Js('Thunder'), Js('Blood'), Js('Burning'), Js('Bone'), Js('Clan'), Js('Dark'), Js('Dead'), Js('Death'), Js('Doom'), Js('Dragon'), Js('Dream'), Js('Fire'), Js('Fist'), Js('Fore'), Js('Frost'), Js('Gore'), Js('Hell'), Js('Iron'), Js('Laughing'), Js('Lone'), Js('Nose'), Js('Rage'), Js('Red'), Js('Rock'), Js('Saur'), Js('Shadow'), Js('Skull'), Js('Steel'), Js('Stone'), Js('Strong'), Js('Tusk'), Js('War'), Js('Wolf')]))
var.put('nm8', Js([Js('axe'), Js('arm'), Js('basher'), Js('binder'), Js('blade'), Js('bleeder'), Js('bringer'), Js('chewer'), Js('cleaver'), Js('crusher'), Js('eye'), Js('fang'), Js('fist'), Js('fury'), Js('hammer'), Js('hand'), Js('horn'), Js('lash'), Js('maul'), Js('maw'), Js('rage'), Js('ripper'), Js('runner'), Js('scream'), Js('seeker'), Js('slayer'), Js('snarl'), Js('song'), Js('splitter'), Js('sword'), Js('taker'), Js('wolf')]))
pass
pass


# Add lib to the module scope
orcWowNames = var.to_python()