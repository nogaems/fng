__all__ = ['orcEsNames']

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
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+Js(' '))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Agr'), Js('Agro'), Js('Atu'), Js('Atul'), Js('Azu'), Js('Azuk'), Js('Bag'), Js('Baga'), Js('Bak'), Js('Bakh'), Js('Bal'), Js('Bala'), Js('Bar'), Js('Baro'), Js('Bas'), Js('Bash'), Js('Bat'), Js('Baz'), Js('Bazg'), Js('Bazu'), Js('Bog'), Js('Boga'), Js('Bogr'), Js('Bol'), Js('Bolo'), Js('Bor'), Js('Bork'), Js('Boru'), Js('Bot'), Js('Both'), Js('Bra'), Js('Brag'), Js('Bro'), Js('Brok'), Js('Bru'), Js('Brug'), Js('Bug'), Js('Buga'), Js('Bugd'), Js('Bugh'), Js('Bugr'), Js('Bum'), Js('Bumb'), Js('Bur'), Js('Bura'), Js('Burg'), Js('Buru'), Js('Burz'), Js('Dub'), Js('Dubo'), Js('Dul'), Js('Dula'), Js('Dulf'), Js('Dulp'), Js('Dulu'), Js('Dum'), Js('Duma'), Js('Dumb'), Js('Dur'), Js('Dura'), Js('Durb'), Js('Durg'), Js('Durz'), Js('Dus'), Js('Dush'), Js('Gad'), Js('Gadb'), Js('Gar'), Js('Garo'), Js('Garz'), Js('Gas'), Js('Gash'), Js('Gat'), Js('Gatu'), Js('Gha'), Js('Gham'), Js('Gho'), Js('Ghor'), Js('Ghu'), Js('Ghun'), Js('Glu'), Js('Glus'), Js('Gog'), Js('Gogr'), Js('Gor'), Js('Gorg'), Js('Gra'), Js('Grak'), Js('Gram'), Js('Grat'), Js('Gro'), Js('Grog'), Js('Grom'), Js('Gru'), Js('Grul'), Js('Grus'), Js('Gruz'), Js('Gua'), Js('Guar'), Js('Gul'), Js('Gula'), Js('Gur'), Js('Gura'), Js('Han'), Js('Hanz'), Js('Kha'), Js('Khad'), Js('Khag'), Js('Khar'), Js('Kof'), Js('Koff'), Js('Kro'), Js('Krog'), Js('Kur'), Js('Kurd'), Js('Kurz'), Js('Lar'), Js('Lara'), Js('Larg'), Js('Lob'), Js('Lor'), Js('Lorb'), Js('Lorz'), Js('Lug'), Js('Lugd'), Js('Lugr'), Js('Lum'), Js('Lumd'), Js('Lur'), Js('Lurb'), Js('Luro'), Js('Mag'), Js('Magr'), Js('Magu'), Js('Mah'), Js('Mahk'), Js('Mak'), Js('Makh'), Js('Makn'), Js('Mako'), Js('Mal'), Js('Malk'), Js('Mas'), Js('Mash'), Js('Mat'), Js('Matu'), Js('Mau'), Js('Mauh'), Js('Maz'), Js('Mazo'), Js('Mog'), Js('Mogh'), Js('Mogr'), Js('Mol'), Js('Mor'), Js('Morb'), Js('Mot'), Js('Moth'), Js('Mug'), Js('Mugd'), Js('Muk'), Js('Mul'), Js('Mulu'), Js('Mur'), Js('Mura'), Js('Murk'), Js('Murz'), Js('Muz'), Js('Muzg'), Js('Nag'), Js('Nagr'), Js('Nar'), Js('Nas'), Js('Nash'), Js('Ogl'), Js('Oglu'), Js('Ogo'), Js('Ogol'), Js('Ogr'), Js('Ogru'), Js('Olf'), Js('Olfi'), Js('Olp'), Js('Olpa'), Js('Olu'), Js('Olum'), Js('Olur'), Js('Ora'), Js('Orak'), Js('Oro'), Js('Orok'), Js('Oth'), Js('Othm'), Js('Ram'), Js('Ramo'), Js('Rog'), Js('Rogd'), Js('Rug'), Js('Rugd'), Js('Sha'), Js('Shag'), Js('Shak'), Js('Sham'), Js('Shar'), Js('Shat'), Js('Shaz'), Js('She'), Js('Shel'), Js('Sho'), Js('Shob'), Js('Shu'), Js('Shul'), Js('Shum'), Js('Shur'), Js('Shuz'), Js('Sna'), Js('Snag'), Js('Snak'), Js('Snat'), Js('Ugd'), Js('Ugdu'), Js('Ugh'), Js('Ugha'), Js('Ula'), Js('Ulag'), Js('Ulam'), Js('Ulm'), Js('Ulmu'), Js('Umu'), Js('Umug'), Js('Umur'), Js('Ura'), Js('Urag'), Js('Uram'), Js('Urb'), Js('Urbu'), Js('Uri'), Js('Urim'), Js('Uru'), Js('Urul'), Js('Urz'), Js('Urzo'), Js('Ush'), Js('Usha'), Js('Ushn'), Js('Uzg'), Js('Uzga'), Js('Uzu'), Js('Uzul'), Js('Yad'), Js('Yadb'), Js('Yag'), Js('Yaga'), Js('Yak'), Js('Yam'), Js('Yama'), Js('Yamb'), Js('Yar'), Js('Yarg'), Js('Yas'), Js('Yash'), Js('Yat'), Js('Yatu')]))
var.put('nm2', Js([Js('a'), Js('ac'), Js('ag'), Js('agdush'), Js('agog'), Js('agorn'), Js('ak'), Js('akh'), Js('amog'), Js('amph'), Js('amul'), Js('an'), Js('ar'), Js('arz'), Js('arzob'), Js('ash'), Js('at'), Js('b'), Js('ba'), Js('bagorn'), Js('bash'), Js('bob'), Js('borz'), Js('bub'), Js('buk'), Js('bul'), Js('bumol'), Js('burz'), Js('c'), Js('dan'), Js('dba'), Js('dul'), Js('dum'), Js('dumph'), Js('el'), Js('fish'), Js('futto'), Js('g'), Js('gakh'), Js('gam'), Js('gash'), Js('glak'), Js('gmar'), Js('gnak'), Js('go'), Js('gob'), Js('gog'), Js('gol'), Js('gonk'), Js('gra'), Js('grol'), Js('guk'), Js('gulub'), Js('h'), Js('ha'), Js('hag'), Js('hakh'), Js('harz'), Js('hel'), Js('hna'), Js('hnag'), Js('hnamub'), Js('hnarz'), Js('hul'), Js('hulakh'), Js('humph'), Js('il'), Js('in'), Js('ish'), Js('k'), Js('kh'), Js('kha'), Js('kil'), Js('klak'), Js('kub'), Js('kul'), Js('kus'), Js('l'), Js('lak'), Js('lakh'), Js('lg'), Js('long'), Js('lorz'), Js('m'), Js('man'), Js('mar'), Js('mash'), Js('mba'), Js('mborz'), Js('mbu'), Js('mmok'), Js('mob'), Js('mog'), Js('mok'), Js('monk'), Js('morz'), Js('mph'), Js('mul'), Js('n'), Js('na'), Js('nag'), Js('nak'), Js('namub'), Js('nar'), Js('narz'), Js('nk'), Js('nok'), Js('nzul'), Js('o'), Js('ob'), Js('og'), Js('ogra'), Js('ok'), Js('ol'), Js('olg'), Js('on'), Js('onak'), Js('ong'), Js('onk'), Js('or'), Js('orn'), Js('orz'), Js('othmuk'), Js('phumph'), Js('r'), Js('ra'), Js('rag'), Js('ragdush'), Js('rash'), Js('rbash'), Js('rg'), Js('rgam'), Js('rgol'), Js('rkub'), Js('rkul'), Js('rlorz'), Js('rn'), Js('rol'), Js('ron'), Js('rub'), Js('rul'), Js('rum'), Js('rz'), Js('rzob'), Js('sh'), Js('shnag'), Js('t'), Js('thmuk'), Js('ub'), Js('ug'), Js('uk'), Js('ul'), Js('ulakh'), Js('ulub'), Js('um'), Js('umbu'), Js('umol'), Js('umph'), Js('ur'), Js('urn'), Js('urz'), Js('us'), Js('ush'), Js('utto'), Js('z'), Js('zgob'), Js('zol'), Js('zonk'), Js('zub'), Js('zug'), Js('zul'), Js('zum')]))
var.put('nm3', Js([Js('Agr'), Js('Agro'), Js('Aro'), Js('Arob'), Js('Atu'), Js('Atub'), Js('Bad'), Js('Badb'), Js('Bag'), Js('Bagr'), Js('Bas'), Js('Bash'), Js('Bat'), Js('Batu'), Js('Bog'), Js('Bogd'), Js('Bol'), Js('Bola'), Js('Bor'), Js('Borb'), Js('Borg'), Js('Bug'), Js('Bugd'), Js('Bul'), Js('Bula'), Js('Bulf'), Js('Bum'), Js('Bump'), Js('Bur'), Js('Buru'), Js('Burz'), Js('Dul'), Js('Dulu'), Js('Dur'), Js('Dura'), Js('Durg'), Js('Durz'), Js('Gar'), Js('Gara'), Js('Gas'), Js('Gash'), Js('Gha'), Js('Ghak'), Js('Ghar'), Js('Gho'), Js('Ghob'), Js('Ghor'), Js('Gla'), Js('Glas'), Js('Glo'), Js('Glob'), Js('Glu'), Js('Glur'), Js('Gon'), Js('Gonk'), Js('Gra'), Js('Grat'), Js('Graz'), Js('Gul'), Js('Gulf'), Js('Hom'), Js('Homr'), Js('Kha'), Js('Khar'), Js('Lag'), Js('Laga'), Js('Lam'), Js('Lamb'), Js('Las'), Js('Lash'), Js('Laz'), Js('Lazg'), Js('Maz'), Js('Mazg'), Js('Mazo'), Js('Mog'), Js('Moga'), Js('Mogd'), Js('Mor'), Js('Morn'), Js('Mur'), Js('Murb'), Js('Muro'), Js('Murz'), Js('Nar'), Js('Narg'), Js('Ogh'), Js('Ogha'), Js('Ora'), Js('Orag'), Js('Orb'), Js('Orbu'), Js('Rag'), Js('Raga'), Js('Rog'), Js('Rogb'), Js('Rogm'), Js('Rol'), Js('Rolf'), Js('Rul'), Js('Rulf'), Js('Sha'), Js('Shad'), Js('Shag'), Js('Shar'), Js('She'), Js('Shel'), Js('Shu'), Js('Shuf'), Js('Slo'), Js('Sloo'), Js('Sna'), Js('Snak'), Js('Uga'), Js('Ugak'), Js('Ugl'), Js('Ugla'), Js('Ugo'), Js('Ugor'), Js('Ulo'), Js('Ulot'), Js('Ulu'), Js('Ulum'), Js('Umo'), Js('Umog'), Js('Uro'), Js('Urog'), Js('Urz'), Js('Urzo'), Js('Urzu'), Js('Ush'), Js('Ushu'), Js('Vol'), Js('Volt'), Js('Yag'), Js('Yat'), Js('Yatu'), Js('Yaz'), Js('Yazg')]))
var.put('nm4', Js([Js('a'), Js('ak'), Js('akh'), Js('amph'), Js('ar'), Js('arz'), Js('ash'), Js('at'), Js('az'), Js('b'), Js('ba'), Js('bak'), Js('bog'), Js('bug'), Js('bul'), Js('but'), Js('dbak'), Js('dub'), Js('durash'), Js('durz'), Js('esh'), Js('fim'), Js('fish'), Js('ftharz'), Js('g'), Js('ga'), Js('gak'), Js('gakh'), Js('gar'), Js('gash'), Js('gat'), Js('gdub'), Js('gol'), Js('h'), Js('ha'), Js('hnakh'), Js('huk'), Js('im'), Js('ish'), Js('k'), Js('kh'), Js('l'), Js('lur'), Js('m'), Js('malah'), Js('mesh'), Js('mpha'), Js('n'), Js('nakh'), Js('ob'), Js('og'), Js('oga'), Js('ol'), Js('omalah'), Js('onk'), Js('oth'), Js('ph'), Js('pha'), Js('r'), Js('rak'), Js('ramph'), Js('raz'), Js('rn'), Js('rog'), Js('rol'), Js('ronk'), Js('rz'), Js('rza'), Js('rzug'), Js('sh'), Js('sha'), Js('t'), Js('th'), Js('tha'), Js('tharz'), Js('ub'), Js('ug'), Js('uk'), Js('ul'), Js('um'), Js('ur'), Js('urash'), Js('urz'), Js('ush'), Js('ut'), Js('z'), Js('za'), Js('zob'), Js('zug'), Js('zush')]))
var.put('nm5', Js([Js('Aga'), Js('Agad'), Js('Agam'), Js('Agl'), Js('Agla'), Js('Agu'), Js('Agum'), Js('Atu'), Js('Atum'), Js('Azo'), Js('Azor'), Js('Bad'), Js('Badb'), Js('Bag'), Js('Bagd'), Js('Bago'), Js('Bagr'), Js('Bagu'), Js('Bam'), Js('Bamo'), Js('Bar'), Js('Bara'), Js('Barg'), Js('Baro'), Js('Bas'), Js('Bash'), Js('Bat'), Js('Batu'), Js('Bha'), Js('Bhar'), Js('Bog'), Js('Boga'), Js('Bogh'), Js('Bogl'), Js('Bogr'), Js('Bogu'), Js('Bol'), Js('Bola'), Js('Bolm'), Js('Bon'), Js('Bonk'), Js('Bor'), Js('Borb'), Js('Bro'), Js('Brok'), Js('Bug'), Js('Buga'), Js('Bugl'), Js('Bul'), Js('Bula'), Js('Bulf'), Js('Bum'), Js('Bump'), Js('Bur'), Js('Bura'), Js('Burb'), Js('Buri'), Js('Buro'), Js('Burz'), Js('Buz'), Js('Buzg'), Js('Cob'), Js('Cobl'), Js('Cro'), Js('Crom'), Js('Dra'), Js('Drag'), Js('Dug'), Js('Dugu'), Js('Dul'), Js('Dula'), Js('Dulo'), Js('Dum'), Js('Dumu'), Js('Dur'), Js('Durg'), Js('Duro'), Js('Duru'), Js('Dus'), Js('Dush'), Js('Gal'), Js('Gala'), Js('Gam'), Js('Gamo'), Js('Gar'), Js('Gas'), Js('Gash'), Js('Gat'), Js('Gatu'), Js('Gha'), Js('Ghar'), Js('Ghas'), Js('Gho'), Js('Ghol'), Js('Ghor'), Js('Ghot'), Js('Glo'), Js('Glor'), Js('Glu'), Js('Gluk'), Js('Glur'), Js('Gol'), Js('Golp'), Js('Gon'), Js('Gonk'), Js('Gor'), Js('Gort'), Js('Gorz'), Js('Gra'), Js('Gram'), Js('Gru'), Js('Grul'), Js('Gul'), Js('Gulf'), Js('Gur'), Js('Gura'), Js('Guru'), Js('Hub'), Js('Hubr'), Js('Kas'), Js('Kash'), Js('Kha'), Js('Khag'), Js('Khar'), Js('Khas'), Js('Khat'), Js('Khaz'), Js('Lag'), Js('Lagd'), Js('Lar'), Js('Larg'), Js('Laz'), Js('Lazg'), Js('Log'), Js('Logh'), Js('Logo'), Js('Logr'), Js('Lor'), Js('Lorg'), Js('Lum'), Js('Lumb'), Js('Lumo'), Js('Lur'), Js('Lurk'), Js('Lurn'), Js('Luz'), Js('Luzg'), Js('Mag'), Js('Maga'), Js('Magr'), Js('Magu'), Js('Mal'), Js('Malo'), Js('Mar'), Js('Mara'), Js('Maro'), Js('Mas'), Js('Mash'), Js('Mog'), Js('Moga'), Js('Mogd'), Js('Mogh'), Js('Mor'), Js('Morg'), Js('Mug'), Js('Mugh'), Js('Muk'), Js('Mul'), Js('Mula'), Js('Mur'), Js('Murg'), Js('Muru'), Js('Murz'), Js('Muz'), Js('Muzg'), Js('Nay'), Js('Nayb'), Js('Nol'), Js('Nolo'), Js('Oga'), Js('Ogar'), Js('Ogd'), Js('Ogdu'), Js('Olo'), Js('Olor'), Js('Olu'), Js('Olur'), Js('Orb'), Js('Orbu'), Js('Ork'), Js('Orku'), Js('Oru'), Js('Orum'), Js('Rim'), Js('Rimp'), Js('Rug'), Js('Rugd'), Js('Rugo'), Js('Rus'), Js('Rush'), Js('Sha'), Js('Shad'), Js('Shag'), Js('Shak'), Js('Sham'), Js('Shar'), Js('Shat'), Js('Shaz'), Js('Shu'), Js('Shub'), Js('Shug'), Js('Shul'), Js('Shum'), Js('Shur'), Js('Shuz'), Js('Ska'), Js('Skan'), Js('Sna'), Js('Snag'), Js('Tra'), Js('Trai'), Js('Uft'), Js('Ufth'), Js('Ugd'), Js('Ugdu'), Js('Ugr'), Js('Ugru'), Js('Ula'), Js('Ular'), Js('Ulf'), Js('Ulfi'), Js('Urg'), Js('Urga'), Js('Ush'), Js('Usha'), Js('Ushu'), Js('Uzg'), Js('Uzga'), Js('Uzgu'), Js('Uzu'), Js('Uzug'), Js('Uzuk'), Js('Yag'), Js('Yaga'), Js('Yak'), Js('Yar'), Js('Yarg'), Js('Yaru'), Js('Yarz')]))
var.put('nm6', Js([Js('a'), Js('ad'), Js('ag'), Js('ak'), Js('akh'), Js('am'), Js('amakh'), Js('amph'), Js('an'), Js('ar'), Js('arn'), Js('arz'), Js('ash'), Js('at'), Js('b'), Js('ba'), Js('bag'), Js('bak'), Js('bek'), Js('bog'), Js('borgob'), Js('bu'), Js('bug'), Js('buk'), Js('bul'), Js('bush'), Js('d'), Js('dar'), Js('dborgob'), Js('dbu'), Js('dbuk'), Js('du'), Js('dub'), Js('duk'), Js('dulg'), Js('dum'), Js('dush'), Js('ek'), Js('el'), Js('fim'), Js('fish'), Js('g'), Js('ga'), Js('gak'), Js('gakh'), Js('gamph'), Js('gan'), Js('garn'), Js('garz'), Js('gash'), Js('gdu'), Js('gdub'), Js('gdulg'), Js('gdum'), Js('gham'), Js('gk'), Js('gob'), Js('gog'), Js('gol'), Js('grak'), Js('gramph'), Js('grump'), Js('gub'), Js('gul'), Js('gum'), Js('gur'), Js('gurz'), Js('h'), Js('hakh'), Js('ham'), Js('hamph'), Js('harz'), Js('harzol'), Js('hash'), Js('hel'), Js('hnag'), Js('hnar'), Js('hnikh'), Js('hol'), Js('hub'), Js('hug'), Js('ilslag'), Js('im'), Js('imph'), Js('ish'), Js('k'), Js('kh'), Js('ku'), Js('kub'), Js('kul'), Js('l'), Js('la'), Js('lam'), Js('lar'), Js('lfim'), Js('lg'), Js('lob'), Js('lor'), Js('lslag'), Js('lug'), Js('lump'), Js('m'), Js('ma'), Js('makh'), Js('mba'), Js('mbak'), Js('mgog'), Js('mog'), Js('mph'), Js('mub'), Js('n'), Js('nag'), Js('nar'), Js('ndar'), Js('nikh'), Js('ob'), Js('og'), Js('ok'), Js('ol'), Js('olg'), Js('or'), Js('orn'), Js('oth'), Js('ph'), Js('pok'), Js('r'), Js('ra'), Js('rag'), Js('rak'), Js('ramph'), Js('rat'), Js('rba'), Js('rbag'), Js('rbush'), Js('rg'), Js('rga'), Js('rgak'), Js('rgakh'), Js('rish'), Js('rku'), Js('rkub'), Js('rkul'), Js('rn'), Js('rob'), Js('rol'), Js('rolg'), Js('rump'), Js('rz'), Js('rzog'), Js('rzuf'), Js('sh'), Js('sharzol'), Js('shnar'), Js('t'), Js('th'), Js('tub'), Js('tur'), Js('twog'), Js('u'), Js('ub'), Js('ug'), Js('uk'), Js('ul'), Js('ulg'), Js('um'), Js('uma'), Js('ump'), Js('ur'), Js('urn'), Js('urz'), Js('ush'), Js('wog'), Js('z'), Js('zag'), Js('zgub'), Js('zog'), Js('zol'), Js('zor'), Js('zuf')]))
pass
pass


# Add lib to the module scope
orcEsNames = var.to_python()