__all__ = ['starTrekBolians']

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
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', ((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+Js(' '))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ado'), Js('Ara'), Js('Ardo'), Js('Ba'), Js('Bo'), Js('Bra'), Js('Che'), Js('Co'), Js('Cra'), Js('Da'), Js('Dai'), Js('Dri'), Js('Ga'), Js('Grai'), Js('Gri'), Js('Ha'), Js('Hi'), Js('Hra'), Js('La'), Js('Li'), Js('Lo'), Js('Ma'), Js('Mai'), Js('Mo'), Js('Na'), Js('Ni'), Js('No'), Js('Oda'), Js('Ori'), Js('Orla'), Js('Qa'), Js('Qe'), Js('Qhi'), Js('Ra'), Js('Rai'), Js('Ri'), Js('Sa'), Js('Sho'), Js('Sra'), Js('The'), Js('To'), Js('Tra'), Js('Va'), Js('Vo'), Js('Vri'), Js('Xa'), Js('Xai'), Js('Xi'), Js('Ya'), Js('Yai'), Js('Ye'), Js('Za'), Js('Zai'), Js('Zi')]))
var.put('nm2', Js([Js('d'), Js('dar'), Js('daw'), Js('ds'), Js('f'), Js('fe'), Js('fel'), Js('fer'), Js('g'), Js('ge'), Js('gg'), Js('gon'), Js('k'), Js('ken'), Js('kin'), Js('kk'), Js('l'), Js('lar'), Js('ll'), Js('ls'), Js('m'), Js('man'), Js('mix'), Js('ms'), Js('n'), Js('nd'), Js('nn'), Js('nor'), Js('q'), Js("q'no"), Js("q'ra"), Js("q'si"), Js("q'ta"), Js('qar'), Js('r'), Js('ran'), Js('rr'), Js('rs'), Js('s'), Js('sh'), Js('sia'), Js('ss'), Js('t'), Js('thaw'), Js('tix'), Js('tt'), Js('w'), Js('wd'), Js('wer'), Js('ws'), Js('x'), Js('xin'), Js('xor'), Js('xx')]))
var.put('nm3', Js([Js('Ala'), Js('Ana'), Js('Ara'), Js('Bela'), Js('Bine'), Js('By'), Js('Che'), Js('Cia'), Js('Cila'), Js('Di'), Js('Dire'), Js('Do'), Js('Eli'), Js('Ena'), Js('Era'), Js('Fely'), Js('Fri'), Js('Fy'), Js('Gile'), Js('Go'), Js('Gy'), Js('He'), Js('Hia'), Js('Hira'), Js('Keno'), Js('Kise'), Js('Ky'), Js('Lena'), Js('Lo'), Js('Ly'), Js('Mi'), Js('Mite'), Js('My'), Js('Myne'), Js('Nera'), Js('Ni'), Js('Ny'), Js('Oli'), Js('Ora'), Js('Oshe'), Js('Qena'), Js('Qhi'), Js('Qi'), Js('Rely'), Js('Ri'), Js('Ria'), Js('Se'), Js('Seri'), Js('So'), Js('Tia'), Js('Tri'), Js('Ty'), Js('Veli'), Js('Vira'), Js('Vy'), Js('Wane'), Js('Wile'), Js('Wy'), Js('Ya'), Js('Yle'), Js('Yra'), Js('Ze'), Js('Zi')]))
var.put('nm4', Js([Js('des'), Js('dia'), Js('dit'), Js('dra'), Js('ha'), Js('hara'), Js('his'), Js('hya'), Js('kena'), Js('kia'), Js('kis'), Js('kye'), Js('lara'), Js('lea'), Js('leya'), Js('lwat'), Js('mena'), Js('mia'), Js('mis'), Js('moya'), Js('na'), Js('ndis'), Js('ndra'), Js('nila'), Js('sea'), Js('sen'), Js('sia'), Js('sina'), Js('tea'), Js('tena'), Js('tia'), Js('tra'), Js('ves'), Js('vil'), Js('vria'), Js('vya'), Js('wela'), Js('wia'), Js('win'), Js('wira'), Js('xea'), Js('xena'), Js('xia'), Js('xis'), Js('zena'), Js('zia'), Js('zila'), Js('zira')]))
var.put('nm5', Js([Js('Adi'), Js('Ara'), Js('Arli'), Js('Bela'), Js('Bore'), Js('Bro'), Js('Cha'), Js('Chu'), Js('Cora'), Js('Dina'), Js('Do'), Js('Dra'), Js('Era'), Js('Erno'), Js('Esra'), Js('Fera'), Js('Fo'), Js('Fro'), Js('Gadi'), Js('Gara'), Js('Gro'), Js('Ha'), Js('Hera'), Js('Ho'), Js('Kera'), Js('Ki'), Js('Kra'), Js('La'), Js('Lica'), Js('Lyna'), Js('Ma'), Js('Mari'), Js('Mo'), Js('Na'), Js('Ne'), Js('Nora'), Js('Ora'), Js('Orna'), Js('Oro'), Js('Qa'), Js('Qira'), Js('Qo'), Js('Ra'), Js('Re'), Js('Rina'), Js('Sa'), Js('Sina'), Js('So'), Js('Tado'), Js('Tari'), Js('Tra'), Js('Va'), Js('Vade'), Js('Viro'), Js('Wa'), Js('Wera'), Js('Wora'), Js('Xa'), Js('Xira'), Js('Xo'), Js('Za'), Js('Zira'), Js('Zo')]))
var.put('nm6', Js([Js('d'), Js('das'), Js('dd'), Js('din'), Js('f'), Js('far'), Js('ff'), Js('fit'), Js('g'), Js('gg'), Js('git'), Js('gon'), Js('ha'), Js('har'), Js('hino'), Js('ht'), Js('l'), Js('lar'), Js('lin'), Js('ll'), Js('mar'), Js('min'), Js('mm'), Js('nar'), Js('nat'), Js('nin'), Js('nn'), Js('ra'), Js('ras'), Js('ro'), Js('rr'), Js('sa'), Js('sin'), Js('slo'), Js('ss'), Js('ta'), Js('ten'), Js('tor'), Js('tt'), Js('wa'), Js('was'), Js('wat')]))
pass
pass


# Add lib to the module scope
starTrekBolians = var.to_python()