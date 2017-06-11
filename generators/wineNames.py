__all__ = ['wineNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+Js(' '))+var.get('nm5').get(var.get('rnd4'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nm5').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('bl'), Js('br'), Js('ch'), Js('cl'), Js('dh'), Js('fr'), Js('fl'), Js('gh'), Js('gr'), Js('sh'), Js('tr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ueu'), Js('ou'), Js('au'), Js('ai'), Js('ue'), Js('eau'), Js('au'), Js('ei'), Js('ee'), Js('ia'), Js('ie'), Js('io'), Js('uei'), Js('oui'), Js('ieu'), Js('eo')]))
var.put('nm3', Js([Js('bb'), Js('bl'), Js('br'), Js('c'), Js('cc'), Js('cch'), Js('ch'), Js('d'), Js('f'), Js('g'), Js('gd'), Js('gn'), Js('gr'), Js('j'), Js('k'), Js('l'), Js('lb'), Js('lbl'), Js('ldt'), Js('ll'), Js('lr'), Js('ls'), Js('m'), Js('mb'), Js('mbl'), Js('mbr'), Js('mch'), Js('mm'), Js('mp'), Js('n'), Js('nc'), Js('nch'), Js('nd'), Js('ndr'), Js('ng'), Js('nh'), Js('nj'), Js('nk'), Js('nn'), Js('nt'), Js('nth'), Js('ntr'), Js('nv'), Js('pf'), Js('pl'), Js('q'), Js('r'), Js('rb'), Js('rc'), Js('rch'), Js('rd'), Js('rf'), Js('rg'), Js('rgr'), Js('rh'), Js('rl'), Js('rm'), Js('rn'), Js('rr'), Js('rs'), Js('rt'), Js('rth'), Js('rtz'), Js('s'), Js('sb'), Js('sc'), Js('sl'), Js('ss'), Js('ssl'), Js('st'), Js('th'), Js('tt'), Js('v'), Js('vr'), Js('x'), Js('z')]))
var.put('nm4', Js([Js('beit'), Js('bera'), Js('beutel'), Js('blage'), Js('bles'), Js('blis'), Js('bourg'), Js('bria'), Js('cano'), Js('cati'), Js('cchio'), Js('cchus'), Js('ce'), Js('cella'), Js('chage'), Js('che'), Js('chen'), Js('chot'), Js('dange'), Js('deaux'), Js('der'), Js('dol'), Js('drieu'), Js('fe'), Js('ge'), Js('geac'), Js('geot'), Js('gey'), Js('giens'), Js('gna'), Js('gnan'), Js('gne'), Js('gnon'), Js('gros'), Js('grube'), Js('gueil'), Js('heim'), Js('kastel'), Js('lage'), Js('lais'), Js('las'), Js('lbot'), Js('lese'), Js('let'), Js('lien'), Js('lino'), Js('lion'), Js('lla'), Js('lle'), Js('llina'), Js('llo'), Js('llon'), Js('lly'), Js('lo'), Js('lon'), Js('lou'), Js('lung'), Js('ly'), Js('ma'), Js('mante'), Js('mat'), Js('may'), Js('mbes'), Js('me'), Js('mens'), Js('ment'), Js('mes'), Js('meur'), Js('ms'), Js('mune'), Js('mur'), Js('na'), Js('nac'), Js('nais'), Js('nas'), Js('nay'), Js('nce'), Js('nche'), Js('ne'), Js('nee'), Js('nel'), Js('ner'), Js('nett'), Js('nia'), Js('nier'), Js('nieux'), Js('nis'), Js('nne'), Js('node'), Js('non'), Js('note'), Js('nots'), Js('nti'), Js('ntre'), Js('nues'), Js('nuhr'), Js('phe'), Js('que'), Js('quem'), Js('raud'), Js('reic'), Js('reich'), Js('resco'), Js('rie'), Js('rnes'), Js('rnet'), Js('rno'), Js('rol'), Js('rons'), Js('rre'), Js('rten'), Js('rtin'), Js('rton'), Js('san'), Js('sco'), Js('sir'), Js('sis'), Js('sne'), Js('sone'), Js('sse'), Js('ssec'), Js('sson'), Js('sus'), Js('tage'), Js('tan'), Js('tium'), Js('tour'), Js('tre'), Js('tte'), Js('val'), Js('ve'), Js('vel'), Js('vens'), Js('ves'), Js('ville'), Js('vrey'), Js('vry'), Js('wen'), Js('wer'), Js('xin'), Js('zeaux'), Js('zin')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('Abboccato'), Js('Acescence'), Js('Adamado'), Js('Adega'), Js('Amabile'), Js('Annata'), Js('Bianco'), Js('Blanc'), Js('Blanco'), Js('Branco'), Js('Cépage'), Js('Cap Classique'), Js('Cava'), Js('Chiaretto'), Js('Clairet'), Js('Classic'), Js('Demi-Sec'), Js('Doce'), Js('Dolce'), Js('Doux'), Js('Dulce'), Js('Edes'), Js('Frizzante'), Js('Fume'), Js('Garrafeira'), Js('Granvas'), Js('Halbtrocken'), Js('Invecchiato'), Js('Liquoroso'), Js('Mousseux'), Js('Noir'), Js('Pétillant'), Js('Piquant'), Js('Rich'), Js('Rosado'), Js('Rosato'), Js('Rosso'), Js('Rouge'), Js('Süss'), Js('Sec'), Js('Secco'), Js('Száraz'), Js('Vendemmia'), Js('Vendimia'), Js('Viejo'), Js("d'Or")]))
pass
pass


# Add lib to the module scope
wineNames = var.to_python()