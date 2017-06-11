__all__ = ['nightElfNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm4').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
                else:
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', (((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
                else:
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('A'), Js("A'"), Js('Al'), Js('All'), Js('Aly'), Js('An'), Js('Am'), Js('As'), Js('Ay'), Js('Ar'), Js('Cy'), Js('Ca'), Js('E'), Js("E'"), Js('El'), Js('Ely'), Js('Em'), Js('En'), Js('Er'), Js('Es'), Js('Ey'), Js('F'), Js('Fa'), Js('Fy'), Js('Fil'), Js('Fel'), Js('Fyl'), Js('Ga'), Js('Gal'), Js('Ha'), Js('He'), Js('Hy'), Js('I'), Js('Il'), Js('Ily'), Js('Ill'), Js('Iy'), Js('Ji'), Js('Ja'), Js('K'), Js('Ka'), Js('Ke'), Js('Ky'), Js('L'), Js('Lil'), Js('Lyl'), Js('Lel'), Js('La'), Js('Le'), Js('Ly'), Js('M'), Js('Ma'), Js('Me'), Js('My'), Js('Myt'), Js('Myth'), Js('Mor'), Js('Math'), Js('Mil'), Js('Myl'), Js('Mel'), Js('N'), Js('Na'), Js('Ne'), Js('Nyl'), Js('Nil'), Js('Nel'), Js('Nyt'), Js('Nyth'), Js('Ny'), Js('Re'), Js('Ra'), Js('Ry'), Js('S'), Js('Sa'), Js('Sil'), Js('Syl'), Js('Sel'), Js('Sh'), Js('Sha'), Js('She'), Js('Sy'), Js('Shyl'), Js('Th'), Js('Tha'), Js('The'), Js('Thel'), Js('Thyl'), Js('Thil'), Js('Thy'), Js('U'), Js('Uy'), Js('W'), Js('Wa'), Js('We'), Js('Y'), Js("Y'"), Js('Ya'), Js('Ye'), Js('Yl'), Js('Yll')]))
var.put('nm2', Js([Js('al'), Js('el'), Js('en'), Js('an'), Js('ana'), Js('ena'), Js('aena'), Js('a'), Js('i'), Js('ren'), Js('ran'), Js('eth'), Js('ath'), Js('a'), Js('e'), Js('o'), Js('h'), Js('ha'), Js('he'), Js('ho'), Js('f'), Js('fa'), Js('fe'), Js('l'), Js('le'), Js('la'), Js('m'), Js('me'), Js('ma'), Js('ne'), Js('na'), Js('n'), Js('s'), Js('sa'), Js('se'), Js('ve'), Js('va')]))
var.put('nm3', Js([Js('dris'), Js('ris'), Js('dral'), Js('dos'), Js('dlas'), Js('rion'), Js('idan'), Js('gyl'), Js('nul'), Js('gos'), Js('dras'), Js('dran'), Js('dryn'), Js('adros'), Js('dlass'), Js('lass'), Js('dlaess'), Js('dleass'), Js('laess'), Js('leass'), Js('thiel'), Js('engyl'), Js('annul'), Js('aenul'), Js('aenal'), Js('aenel'), Js('eanal'), Js('eanel'), Js('edon'), Js('adon'), Js('aedon'), Js('eadon'), Js('llian'), Js('llean'), Js('lian'), Js('lean'), Js('llaen'), Js('laen'), Js('nath'), Js('naeth'), Js('neath'), Js('shar'), Js('tharion'), Js('arion'), Js('erian'), Js('aerian'), Js('dent'), Js('elir'), Js('gorn'), Js('egorn'), Js('agorn'), Js('elor'), Js('ellor'), Js('aelor'), Js('aellor'), Js('elorn'), Js('ellorn'), Js('aelorn'), Js('aellorn'), Js('dren'), Js('odren'), Js('draen'), Js('odraen'), Js('adan'), Js('aedan'), Js('adaen'), Js('adean'), Js('draen'), Js('odraen'), Js('adarn'), Js('aedarn'), Js('adaern'), Js('adearn'), Js('drus'), Js('nrus'), Js('dryn'), Js('dan'), Js('andiir'), Js('diir'), Js('gyl'), Js('gyal'), Js('gyael'), Js("'dir"), Js('umon'), Js('elar'), Js('aelar'), Js('ealar'), Js('oren'), Js('oraen'), Js('orean'), Js("'las"), Js('thas'), Js('thaes'), Js('theas'), Js('sam'), Js('saem'), Js('seam'), Js('rand'), Js('ldor'), Js('dron'), Js('eth'), Js('gorm'), Js('rin'), Js('anas'), Js('anaes'), Js('aenas'), Js('anelle'), Js('dris'), Js('erias'), Js('thae'), Js("n'ra"), Js('nas'), Js('aste'), Js('ethil'), Js('driel'), Js('rieth'), Js('drieth'), Js('draeth'), Js('dreath'), Js('raeth'), Js('reath'), Js('ries'), Js('dries'), Js('draes'), Js('dreas'), Js('raes'), Js('reas'), Js('rai'), Js('rea'), Js('rae'), Js('raei'), Js('anai'), Js('laeth'), Js('leath'), Js('alas'), Js('aelas'), Js('alaes'), Js('aleas'), Js('aeleas'), Js('ealaes'), Js('aelleas'), Js('eallaes'), Js('allas'), Js('aellas'), Js('allaes'), Js('alleas'), Js('alias'), Js('alaeas'), Js('alath'), Js('aelath'), Js('alaeth'), Js('aleath'), Js('aeleath'), Js('ealaeth'), Js('aelleath'), Js('eallaeth'), Js('allath'), Js('aellath'), Js('allaeth'), Js('alleath'), Js('aliath'), Js('alaeath'), Js('aeith'), Js('eaith'), Js('ileath'), Js('ilaeth'), Js('aleath'), Js('illeath'), Js('illaeth'), Js('wen')]))
var.put('nm4', Js([Js('A'), Js("A'"), Js('Al'), Js('All'), Js('Aly'), Js('An'), Js('Am'), Js('As'), Js('Ay'), Js('Ar'), Js('Cy'), Js('Ca'), Js('E'), Js("E'"), Js('El'), Js('Ely'), Js('Em'), Js('En'), Js('Er'), Js('Es'), Js('Ey'), Js('F'), Js('Fa'), Js('Fy'), Js('Fil'), Js('Fel'), Js('Fyl'), Js('Ga'), Js('Gal'), Js('Ha'), Js('He'), Js('Hy'), Js('I'), Js('Il'), Js('Ily'), Js('Ill'), Js('Iy'), Js('Ji'), Js('Ja'), Js('K'), Js('Ka'), Js('Ke'), Js('Ky'), Js('L'), Js('Lil'), Js('Lyl'), Js('Lel'), Js('La'), Js('Le'), Js('Ly'), Js('M'), Js('Ma'), Js('Me'), Js('My'), Js('Myt'), Js('Myth'), Js('Mil'), Js('Myl'), Js('Mel'), Js('N'), Js('Na'), Js('Ne'), Js('Nyl'), Js('Nil'), Js('Nel'), Js('Nyt'), Js('Nyth'), Js('Ny'), Js('S'), Js('Sa'), Js('Sil'), Js('Syl'), Js('Sel'), Js('Sh'), Js('Sha'), Js('She'), Js('Sy'), Js('Shyl'), Js('Th'), Js('Tha'), Js('The'), Js('Thel'), Js('Thyl'), Js('Thil'), Js('Thy'), Js('U'), Js('Uy'), Js('W'), Js('Wa'), Js('We'), Js('Y'), Js("Y'"), Js('Ya'), Js('Ye'), Js('Yl'), Js('Yll')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('o'), Js('h'), Js('f'), Js('l'), Js('m'), Js('n'), Js('s'), Js('va'), Js('a'), Js('e'), Js('o'), Js('h'), Js('ha'), Js('he'), Js('ho'), Js('f'), Js('fa'), Js('fe'), Js('l'), Js('le'), Js('la'), Js('m'), Js('me'), Js('ma'), Js('ne'), Js('na'), Js('n'), Js('s'), Js('sa'), Js('se'), Js('ve'), Js('va'), Js('')]))
var.put('nm6', Js([Js('anas'), Js('anaes'), Js('aenas'), Js('anelle'), Js('dris'), Js('liene'), Js('aria'), Js('anaria'), Js('alaria'), Js('cina'), Js('ina'), Js('ene'), Js('erias'), Js('eria'), Js('ora'), Js('lora'), Js('thea'), Js('thae'), Js('inne'), Js('rnae'), Js('rnea'), Js("is'ta"), Js("n'ra"), Js('nas'), Js('aste'), Js('arii'), Js('riia'), Js('hara'), Js('ethil'), Js('driel'), Js("'lynn"), Js("'lyn"), Js('india'), Js('adyia'), Js('adya'), Js('aedya'), Js('indea'), Js('indae'), Js('ania'), Js('aenia'), Js('eana'), Js('aenea'), Js('iyell'), Js('yell'), Js('ythis'), Js('ethis'), Js('rieth'), Js('drieth'), Js('draeth'), Js('dreath'), Js('raeth'), Js('reath'), Js('ynna'), Js('yna'), Js('enna'), Js('aenna'), Js('eanna'), Js('eana'), Js('aena'), Js('anna'), Js('rai'), Js('rea'), Js('rae'), Js('raei'), Js('anai'), Js('anea'), Js('lea'), Js('lae'), Js('laei'), Js('laeth'), Js('leath'), Js('yssa'), Js('lyssa'), Js('lyssae'), Js('lysae'), Js('ysae'), Js('lysea'), Js('ysea'), Js('asia'), Js('aesia'), Js('easia'), Js('asea'), Js('asae'), Js('aesa'), Js('easa'), Js('alas'), Js('aelas'), Js('alaes'), Js('aleas'), Js('aeleas'), Js('ealaes'), Js('aelleas'), Js('eallaes'), Js('allas'), Js('aellas'), Js('allaes'), Js('alleas'), Js('ercia'), Js('aercia'), Js('earcia'), Js('enia'), Js('aenia'), Js('enya'), Js('aenya'), Js('lia'), Js('alia'), Js('alaea'), Js('alias'), Js('alaeas'), Js('ysa'), Js('yssea'), Js('ysea'), Js('yssae'), Js('ysae'), Js('nya'), Js('nyae'), Js('nysa'), Js('nysea'), Js('nysae'), Js('nyssa'), Js('nyssae'), Js('nyssea'), Js('yssia'), Js('aeith'), Js('eaith'), Js('ileath'), Js('ilaeth'), Js('aleath'), Js('illeath'), Js('illaeth'), Js('yura'), Js('yurea'), Js('yurae'), Js('wen'), Js('leae'), Js('laea')]))
var.put('nm7', Js([Js('Amber'), Js('Autumn'), Js('Bear'), Js('Black'), Js('Blade'), Js('Blue'), Js('Dark'), Js('Dawn'), Js('Dew'), Js('Dusk'), Js('Even'), Js('Far'), Js('Feather'), Js('Fog'), Js('Forest'), Js('Green'), Js('Leaf'), Js('Light'), Js('Luna'), Js('Mist'), Js('Moon'), Js('Moss'), Js('Night'), Js('Ocean'), Js('Rain'), Js('Rapid'), Js('Raven'), Js('Sage'), Js('Sea'), Js('Shade'), Js('Shadow'), Js('Shield'), Js('Silent'), Js('Silver'), Js('Sky'), Js('Spirit'), Js('Stag'), Js('Star'), Js('Still'), Js('Stone'), Js('Storm'), Js('Strong'), Js('Summer'), Js('Sun'), Js('Swift'), Js('Thunder'), Js('Tree'), Js('True'), Js('Void'), Js('Wild'), Js('Wind'), Js('Winter'), Js('Wood')]))
var.put('nm8', Js([Js('arrow'), Js('blade'), Js('bloom'), Js('blower'), Js('bough'), Js('bow'), Js('branch'), Js('breath'), Js('breeze'), Js('caller'), Js('cloud'), Js('clouds'), Js('crest'), Js('dancer'), Js('dew'), Js('eye'), Js('feather'), Js('fire'), Js('flower'), Js('forest'), Js('gazer'), Js('grove'), Js('heart'), Js('helm'), Js('lance'), Js('leaf'), Js('light'), Js('mane'), Js('might'), Js('moon'), Js('oak'), Js('rage'), Js('runner'), Js('scribe'), Js('seeker'), Js('shade'), Js('shadow'), Js('shot'), Js('singer'), Js('sky'), Js('snow'), Js('song'), Js('spear'), Js('spirit'), Js('spyre'), Js('stalker'), Js('star'), Js('strike'), Js('striker'), Js('swift'), Js('sword'), Js('thorn'), Js('tree'), Js('walker'), Js('watcher'), Js('water'), Js('weaver'), Js('whisper'), Js('wind'), Js('wing')]))
pass
pass


# Add lib to the module scope
nightElfNames = var.to_python()