__all__ = ['bloodElfNames']

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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('names', (((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('names', ((((var.get('nm4').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aer'), Js('Aeri'), Js('Al'), Js('Ala'), Js('Ba'), Js('Bac'), Js('Bae'), Js('Baem'), Js('Baema'), Js('Be'), Js('Bem'), Js('Bema'), Js('Bi'), Js('Bit'), Js('Ca'), Js('Cae'), Js('Caem'), Js('Cam'), Js('Dra'), Js('Drae'), Js('Du'), Js('Duy'), Js('Er'), Js('Eri'), Js('Ha'), Js('Hat'), Js('He'), Js('Her'), Js('In'), Js('Ine'), Js('Inet'), Js('It'), Js('Je'), Js('Jen'), Js('Kee'), Js('Keel'), Js('Kre'), Js('Lo'), Js('Lor'), Js('Ma'), Js('Mat'), Js('Matha'), Js('Me'), Js('Mel'), Js('No'), Js('Nor'), Js('Norae'), Js('Oni'), Js('Pa'), Js('Par'), Js('Pe'), Js('Per'), Js('Qu'), Js('Qui'), Js('Ra'), Js('Rah'), Js('Sa'), Js('Sae'), Js('Saet'), Js('Sat'), Js('So'), Js('Ta'), Js('Tan'), Js('Vy'), Js('Vya'), Js('We'), Js('Wel'), Js('Wele'), Js('Wi'), Js('Win'), Js('Ya'), Js('Yat'), Js('Za'), Js('Zae'), Js('Zan'), Js('Ze'), Js('Zel')]))
var.put('nm2', Js([Js('h'), Js('ha'), Js('hae'), Js('hea'), Js('l'), Js('la'), Js('lae'), Js('le'), Js('m'), Js('ma'), Js('mae'), Js('me'), Js('n'), Js('na'), Js('nae'), Js('ne'), Js('r'), Js('ra'), Js('rae'), Js('re'), Js('t'), Js('th'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm3', Js([Js("'thema"), Js("'themar"), Js("'theas"), Js("'danas"), Js("'daras"), Js("'thul"), Js("'thas"), Js("'thaes"), Js('aen'), Js('aesh'), Js('aeth'), Js('ald'), Js('an'), Js('anis'), Js('aris'), Js('arrin'), Js('as'), Js('ash'), Js('ath'), Js('beron'), Js('den'), Js('dis'), Js('dron'), Js('en'), Js('ean'), Js('eath'), Js('eon'), Js('eron'), Js('esh'), Js('haen'), Js('hean'), Js('hein'), Js('hen'), Js('hin'), Js('iel'), Js('il'), Js('ilan'), Js('illan'), Js('in'), Js('ir'), Js('is'), Js('ith'), Js('laen'), Js('lath'), Js('laeth'), Js('len'), Js('leron'), Js('ma'), Js('mae'), Js('na'), Js('nis'), Js('ren'), Js('rim'), Js('rin'), Js('ris'), Js('ron'), Js('rus'), Js('saen'), Js('sen'), Js('thaen'), Js('than'), Js('us'), Js('ven'), Js('veth'), Js('vaen'), Js('ten'), Js('nae'), Js('neas'), Js('theas'), Js('lae'), Js('laen'), Js('azen'), Js('azhen'), Js('zaen'), Js('zen'), Js('uzen')]))
var.put('nm4', Js([Js('Ael'), Js('Aela'), Js('Aele'), Js('Al'), Js('Ala'), Js('Ale'), Js('Am'), Js('Amo'), Js('Amor'), Js('An'), Js('Az'), Js('Aza'), Js('Azae'), Js('Bel'), Js('Bele'), Js('Ca'), Js('Cae'), Js('Cai'), Js('Cay'), Js('Ce'), Js('Cea'), Js('Cee'), Js('Cel'), Js('Da'), Js('Dae'), Js('Daen'), Js('Dan'), Js('Dar'), Js('Day'), Js('De'), Js('Der'), Js('Dey'), Js('El'), Js('Ela'), Js('Ele'), Js('Em'), Js('Fae'), Js('Fe'), Js('Fey'), Js('Il'), Js('Ile'), Js('Jo'), Js('Jovi'), Js('Ka'), Js('Kal'), Js('Ke'), Js('Keal'), Js('Kee'), Js('Kel'), Js('Ky'), Js('Lae'), Js('Lea'), Js('Li'), Js('Lia'), Js('Ly'), Js('Lyn'), Js('Na'), Js('Nar'), Js('Nat'), Js('No'), Js('Novi'), Js('Ol'), Js('Oli'), Js('Se'), Js('Sed'), Js('Sha'), Js('Sy'), Js('Sye'), Js('Syl'), Js('Ta'), Js('Tal'), Js('Tali'), Js('Tan'), Js('Te'), Js('Tel'), Js('Teli'), Js('Ty'), Js('Tye'), Js('Tyn'), Js('Ve'), Js('Vel'), Js('Vela'), Js('Za'), Js('Zae'), Js('Zan'), Js('Zar'), Js('Zat'), Js('Ze'), Js('Zea'), Js('Zy'), Js('Zya')]))
var.put('nm5', Js([Js('h'), Js('ha'), Js('hae'), Js('hea'), Js('l'), Js('la'), Js('lae'), Js('le'), Js('m'), Js('ma'), Js('mae'), Js('me'), Js('n'), Js('na'), Js('nae'), Js('ne'), Js('r'), Js('ra'), Js('rae'), Js('re'), Js('t'), Js('th'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('aena'), Js('alda'), Js('alle'), Js('ana'), Js('anae'), Js('andra'), Js('anea'), Js('ann'), Js('anna'), Js('anne'), Js('anni'), Js('ara'), Js('da'), Js('dine'), Js('dori'), Js('dra'), Js('drae'), Js('drea'), Js('drel'), Js('drin'), Js('drine'), Js('eda'), Js('elda'), Js('eli'), Js('elly'), Js('enna'), Js('era'), Js('erae'), Js('erea'), Js('estra'), Js('iah'), Js('ice'), Js('inda'), Js('ine'), Js('inne'), Js('inth'), Js('ise'), Js('le'), Js('lean'), Js('leane'), Js('len'), Js('lenn'), Js('lenne'), Js('li'), Js('lia'), Js('ly'), Js('na'), Js('nia'), Js('nice'), Js('onia'), Js('ori'), Js('ra'), Js('rae'), Js('rea'), Js('rel'), Js('riah'), Js('rin'), Js('rine'), Js('rise'), Js('vea'), Js('via'), Js('vie'), Js('wae'), Js('we'), Js('wea'), Js('yn'), Js('yna'), Js('ynna')]))
var.put('nm7', Js([Js('Autumn'), Js('Black'), Js('Blood'), Js('Bright'), Js('Cold'), Js('Dark'), Js('Dawn'), Js('Day'), Js('Dew'), Js('Down'), Js('Ember'), Js('Fire'), Js('Flame'), Js('Heart'), Js('High'), Js('Leaf'), Js('Light'), Js('Mirth'), Js('Moon'), Js('Morning'), Js('Night'), Js('Phoenix'), Js('Red'), Js('Rose'), Js('Silver'), Js('Star'), Js('Sun')]))
var.put('nm8', Js([Js('bane'), Js('binder'), Js('blade'), Js('blossom'), Js('bringer'), Js('brook'), Js('down'), Js('fall'), Js('feather'), Js('flame'), Js('flare'), Js('forge'), Js('fury'), Js('gaze'), Js('gazer'), Js('heart'), Js('light'), Js('mourn'), Js('reaver'), Js('seeker'), Js('shade'), Js('shadow'), Js('shard'), Js('shield'), Js('singer'), Js('sky'), Js('sorrow'), Js('spark'), Js('spear'), Js('spell'), Js('sprinter'), Js('stalker'), Js('star'), Js('strider'), Js('sun'), Js('sworn'), Js('vale'), Js('walker'), Js('whisper'), Js('wing'), Js('wood')]))
pass
pass


# Add lib to the module scope
bloodElfNames = var.to_python()