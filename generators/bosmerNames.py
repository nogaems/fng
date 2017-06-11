__all__ = ['bosmerNames']

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
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+Js(' '))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aen'), Js('Aeng'), Js('Aga'), Js('Agar'), Js('Ale'), Js('Alen'), Js('All'), Js('Alli'), Js('Alv'), Js('Alve'), Js('Amr'), Js('Amra'), Js('Amri'), Js('An'), Js('Ang'), Js('Angl'), Js('Angu'), Js('Ano'), Js('Anor'), Js('Anr'), Js('Anru'), Js('Ar'), Js('Ara'), Js('Aran'), Js('Arat'), Js('Ath'), Js('Athr'), Js('Bae'), Js('Baen'), Js('Baer'), Js('Bar'), Js('Bara'), Js('Bas'), Js('Bast'), Js('Ber'), Js('Bere'), Js('Bol'), Js('Bolr'), Js('Bolw'), Js('Bra'), Js('Brag'), Js('Bral'), Js('Bre'), Js('Brel'), Js('Bri'), Js('Brit'), Js('Bro'), Js('Brod'), Js('Brol'), Js('Cae'), Js('Caen'), Js('Cel'), Js('Cele'), Js('Cin'), Js('Cing'), Js('Cle'), Js('Clen'), Js('Co'), Js('Cun'), Js('Dae'), Js('Daen'), Js('Dan'), Js('Dang'), Js('Den'), Js('Dene'), Js('Der'), Js('Derv'), Js('Dir'), Js('Dird'), Js('Don'), Js('Dond'), Js('Edo'), Js('Edor'), Js('Elb'), Js('Elbe'), Js('Ele'), Js('Eleg'), Js('Elis'), Js('Elo'), Js('Elor'), Js('Elr'), Js('Elri'), Js('End'), Js('Endr'), Js('Eng'), Js('Enga'), Js('Engo'), Js('Eni'), Js('Enil'), Js('Ent'), Js('Enth'), Js('Era'), Js('Erad'), Js('Eras'), Js('Eri'), Js('Erid'), Js('Err'), Js('Erra'), Js('Ert'), Js('Erth'), Js('Erv'), Js('Erva'), Js('Fae'), Js('Faen'), Js('Fal'), Js('Fald'), Js('Far'), Js('Farg'), Js('Fau'), Js('Faul'), Js('Fil'), Js('Fill'), Js('Fim'), Js('Fimm'), Js('Fin'), Js('Find'), Js('Fit'), Js('Fith'), Js('For'), Js('Foro'), Js('Gad'), Js('Gadn'), Js('Gae'), Js('Gael'), Js('Gaen'), Js('Gal'), Js('Galm'), Js('Galt'), Js('Gaz'), Js('Gaza'), Js('Gel'), Js('Gele'), Js('Ger'), Js('Gerr'), Js('Gir'), Js('Gird'), Js('Gla'), Js('Glar'), Js('Glau'), Js('Glo'), Js('Glon'), Js('Gloo'), Js('God'), Js('Godr'), Js('Gor'), Js('Gorc'), Js('Gun'), Js('Gund'), Js('Gwi'), Js('Gwil'), Js('Gwin'), Js('Hag'), Js('Haga'), Js('Hay'), Js('Haym'), Js('Hin'), Js('Hing'), Js('Hun'), Js('Hund'), Js('Karo'), Js('Lego'), Js('Li'), Js('Mae'), Js('Maen'), Js('Mag'), Js('Magl'), Js('Mal'), Js('Malb'), Js('Man'), Js('Mank'), Js('Mel'), Js('Meld'), Js('Men'), Js('Mene'), Js('Min'), Js('Mine'), Js('Ming'), Js('Mon'), Js('Mont'), Js('Mor'), Js('Mort'), Js('Nal'), Js('Nali'), Js('Ned'), Js('Nedh'), Js('Nir'), Js('Nira'), Js('Niru'), Js('Nor'), Js('Nord'), Js('Orb'), Js('Orbe'), Js('Orc'), Js('Orch'), Js('Pali'), Js('Peg'), Js('Pega'), Js('Per'), Js('Pera'), Js('Ria'), Js('Rin'), Js('Rind'), Js('Rit'), Js('Rith'), Js('Ron'), Js('Ront'), Js('Sil'), Js('Syl'), Js('Sylc'), Js('Syn'), Js('Synd'), Js('Ta'), Js('Tar'), Js('Tarh'), Js('Tha'), Js('Thad'), Js('Thae'), Js('Thau'), Js('Tho'), Js('Thor'), Js('Thr'), Js('Thra'), Js('Thu'), Js('Thur'), Js('Tuu'), Js('Tuun'), Js('Ulw'), Js('Ulwa'), Js('Ung'), Js('Unge'), Js('Ungo'), Js('Ungr'), Js('Uru'), Js('Urun'), Js('Uun'), Js('Uung'), Js('Uur'), Js('Uura'), Js('Val'), Js('Vali')]))
var.put('nm2', Js([Js('adan'), Js('adras'), Js('aegaer'), Js('aen'), Js('aer'), Js('agar'), Js('agon'), Js('agor'), Js('agoth'), Js('al'), Js('alas'), Js('alem'), Js('alorn'), Js('alos'), Js('an'), Js('angirfin'), Js('ar'), Js('as'), Js('asai'), Js('ast'), Js('born'), Js('bros'), Js('chalas'), Js('cher'), Js('chond'), Js('chor'), Js('dal'), Js('dalas'), Js('dan'), Js('dell'), Js('dhel'), Js('dil'), Js('ding'), Js('dinor'), Js('dir'), Js('dis'), Js('dol'), Js('dolin'), Js('don'), Js('dor'), Js('dras'), Js('driel'), Js('duin'), Js('dulain'), Js('dus'), Js('ebros'), Js('edhel'), Js('egaer'), Js('egor'), Js('egorn'), Js('elas'), Js('eleb'), Js('eleg'), Js('elfin'), Js('elor'), Js('elorn'), Js('elras'), Js('engeval'), Js('endor'), Js('enin'), Js('ephor'), Js('er'), Js('eroth'), Js('fin'), Js('gaer'), Js('gal'), Js('gan'), Js('glos'), Js('gon'), Js('gor'), Js('gorn'), Js('goth'), Js('gvir'), Js('hadan'), Js('halas'), Js('haur'), Js('helas'), Js('helfin'), Js('helorn'), Js('hen'), Js('hendor'), Js('hiel'), Js('hil'), Js('hir'), Js('hndil'), Js('hor'), Js('hragaer'), Js('hragoth'), Js('hrannir'), Js('hroth'), Js('iath'), Js('iel'), Js('ien'), Js('il'), Js('ilgor'), Js('ilon'), Js('imir'), Js('in'), Js('indil'), Js('indir'), Js('indor'), Js('ing'), Js('inor'), Js('ion'), Js('ior'), Js('ir'), Js('irin'), Js('kar'), Js('lalos'), Js('las'), Js('ldol'), Js('leb'), Js('leg'), Js('lem'), Js('lern'), Js('lgor'), Js('lim'), Js('lin'), Js('lion'), Js('lir'), Js('llin'), Js('llion'), Js('lmir'), Js('lor'), Js('lorn'), Js('los'), Js('lras'), Js('lroth'), Js('man'), Js('mion'), Js('mir'), Js('mirn'), Js('mo'), Js('mon'), Js('nagoth'), Js('nas'), Js('ndal'), Js('ndil'), Js('ndir'), Js('ndis'), Js('ndor'), Js('ng'), Js('ngeval'), Js('ngirfin'), Js('nil'), Js('nim'), Js('nir'), Js('nis'), Js('nlin'), Js('nlorn'), Js('nnir'), Js('nor'), Js('och'), Js('olim'), Js('olin'), Js('omlallor'), Js('on'), Js('ond'), Js('onir'), Js('onor'), Js('or'), Js('ore'), Js('oren'), Js('orm'), Js('orn'), Js('orolros'), Js('oron'), Js('os'), Js('oth'), Js('phor'), Js('ragaer'), Js('ragar'), Js('ralorn'), Js('rannir'), Js('ras'), Js('rast'), Js('relor'), Js('rfin'), Js('riath'), Js('rien'), Js('rilgor'), Js('rim'), Js('rin'), Js('rindil'), Js('ring'), Js('rm'), Js('rolros'), Js('romlallor'), Js('rond'), Js('ronir'), Js('ronor'), Js('ros'), Js('roth'), Js('rron'), Js('rthir'), Js('sai'), Js('smo'), Js('sor'), Js('tan'), Js('th'), Js('thadan'), Js('thaur'), Js('thil'), Js('thir'), Js('thor'), Js('thragoth'), Js('throth'), Js('uilon'), Js('uin'), Js('ulain'), Js('um'), Js('urron'), Js('us'), Js('van'), Js('venin'), Js('vir'), Js('wing')]))
var.put('nm3', Js([Js('Ada'), Js('Adan'), Js('Aer'), Js('Aeri'), Js('Agl'), Js('Agla'), Js('Ala'), Js('Alaw'), Js('All'), Js('Alle'), Js('Alt'), Js('Alth'), Js('And'), Js('Andr'), Js('Ane'), Js('Aned'), Js('Ang'), Js('Angr'), Js('Anr'), Js('Anre'), Js('Anu'), Js('Anur'), Js('Ara'), Js('Arae'), Js('Area'), Js('Arad'), Js('Aran'), Js('Arean'), Js('Ard'), Js('Ard'), Js('Ardh'), Js('Ardw'), Js('Are'), Js('Ared'), Js('Bau'), Js('Bou'), Js('Baur'), Js('Bour'), Js('Bael'), Js('Bel'), Js('Bele'), Js('Belw'), Js('Ber'), Js('Berw'), Js('Bor'), Js('Beor'), Js('Boro'), Js('Borw'), Js('Bot'), Js('Both'), Js('Bre'), Js('Brel'), Js('Car'), Js('Carw'), Js('Cas'), Js('Cel'), Js('Cele'), Js('Cii'), Js('Ciin'), Js('Cir'), Js('Cirw'), Js('Cuu'), Js('Cuun'), Js('Cyl'), Js('Dag'), Js('Daga'), Js('Dai'), Js('Dair'), Js('Deg'), Js('Degi'), Js('Den'), Js('Denn'), Js('Des'), Js('Dis'), Js('Dist'), Js('Don'), Js('Dond'), Js('Dot'), Js('Deot'), Js('Doth'), Js('Doth'), Js('Dre'), Js('Dred'), Js('Ein'), Js('Eind'), Js('Ele'), Js('Eleg'), Js('Elp'), Js('Elph'), Js('Elr'), Js('Elra'), Js('Els'), Js('Elsy'), Js('Eme'), Js('Emel'), Js('Era'), Js('Eral'), Js('Est'), Js('Esti'), Js('Fael'), Js('Fal'), Js('Fali'), Js('Faeli'), Js('Far'), Js('Fara'), Js('Fau'), Js('Faur'), Js('Fil'), Js('Filb'), Js('Gal'), Js('Gael'), Js('Geal'), Js('Gala'), Js('Galb'), Js('Gald'), Js('Gan'), Js('Ganr'), Js('Gel'), Js('Geld'), Js('Gil'), Js('Gild'), Js('Gin'), Js('Gini'), Js('Git'), Js('Gith'), Js('Gla'), Js('Glat'), Js('Has'), Js('Hasa'), Js('Huu'), Js('Huur'), Js('Hyn'), Js('Hyna'), Js('Idr'), Js('Idro'), Js('Iin'), Js('Iing'), Js('Ind'), Js('Indr'), Js('Irw'), Js('Irwa'), Js('Kaa'), Js('Kaal'), Js('Kir'), Js('Kirs'), Js('Lae'), Js('Laen'), Js('Lar'), Js('Lara'), Js('Lare'), Js('Lego'), Js('Lie'), Js('Liet'), Js('Lilis'), Js('Lor'), Js('Lorc'), Js('Man'), Js('Mand'), Js('Mar'), Js('Mara'), Js('Men'), Js('Mene'), Js('Met'), Js('Meth'), Js('Mil'), Js('Milb'), Js('Min'), Js('Naa'), Js('Naar'), Js('Nae'), Js('Nael'), Js('Nat'), Js('Naet'), Js('Nate'), Js('Nath'), Js('Nil'), Js('Niol'), Js('Nila'), Js('Nili'), Js('Nim'), Js('Niom'), Js('Nimp'), Js('Nimr'), Js('Niv'), Js('Nive'), Js('Non'), Js('Nona'), Js('Par'), Js('Parw'), Js('Pen'), Js('Peng'), Js('Phy'), Js('Rad'), Js('Radr'), Js('Rilli'), Js('Sam'), Js('Sami'), Js('Sel'), Js('Sele'), Js('Si'), Js('Syl'), Js('Syel'), Js('Tel'), Js('Tela'), Js('Tha'), Js('Tha'), Js('Theo'), Js('Thea'), Js('Thae'), Js('Thae'), Js('Thal'), Js('Tham'), Js('Thi'), Js('Thii'), Js('U'), Js('Ula'), Js('Ulan'), Js('Uur'), Js('Uurw'), Js('Vla'), Js('Vlan'), Js('Wyl'), Js('Wyla')]))
var.put('nm4', Js([Js('a'), Js('ae'), Js('ane'), Js('aone'), Js('aon'), Js('aen'), Js('afil'), Js('agail'), Js('agil'), Js('ael'), Js('ail'), Js('althir'), Js('an'), Js('aril'), Js('aes'), Js('as'), Js('athil'), Js('awen'), Js('bedir'), Js('beneth'), Js('bereth'), Js('chel'), Js('cialfin'), Js('dan'), Js('del'), Js('dhael'), Js('dhel'), Js('dhwen'), Js('diir'), Js('diol'), Js('dael'), Js('diel'), Js('dil'), Js('draaendril'), Js('draedil'), Js('draen'), Js('dreth'), Js('duin'), Js('edh'), Js('edhel'), Js('edir'), Js('egil'), Js('ael'), Js('elaen'), Js('elyn'), Js('eylin'), Js('aelyn'), Js('aelin'), Js('elin'), Js('aen'), Js('enyl'), Js('aenyl'), Js('en'), Js('eneth'), Js('aeneth'), Js('enandriah'), Js('endril'), Js('ene'), Js('enena'), Js('enenor'), Js('eneth'), Js('ereth'), Js('eril'), Js('esse'), Js('fin'), Js('gaerwen'), Js('gail'), Js('gael'), Js('gillys'), Js('glithil'), Js('gnan'), Js('haneth'), Js('hael'), Js('haelyn'), Js('helen'), Js('hel'), Js('helathil'), Js('hiel'), Js('hael'), Js('hien'), Js('hil'), Js('hiron'), Js('hredhel'), Js('hriian'), Js('hruviel'), Js('hwen'), Js('ia'), Js('icia'), Js('ielyn'), Js('ieleth'), Js('ielyl'), Js('iel'), Js('ien'), Js('ifin'), Js('ihill'), Js('iir'), Js('ilyn'), Js('ileth'), Js('il'), Js('illas'), Js('ilphaneth'), Js('ilwen'), Js('inyth'), Js('in'), Js('inan'), Js('ingil'), Js('inriel'), Js('inthil'), Js('ion'), Js('ioniel'), Js('iron'), Js('lin'), Js('lyth'), Js('ldil'), Js('lian'), Js('lin'), Js('lin'), Js('lithil'), Js('lthir'), Js('lwen'), Js('na'), Js('nafil'), Js('nan'), Js('naen'), Js('ndil'), Js('ndrae'), Js('ndra'), Js('ndriah'), Js('ne'), Js('nel'), Js('neth'), Js('ngaer'), Js('ngil'), Js('nia'), Js('nilwen'), Js('nmriel'), Js('nor'), Js('nrel'), Js('nwen'), Js('olian'), Js('on'), Js('ond'), Js('oneth'), Js('oniel'), Js('raenriel'), Js('ragil'), Js('ras'), Js('rchel'), Js('raedhel'), Js('redhel'), Js('rel'), Js('rael'), Js('reth'), Js('riel'), Js('rifin'), Js('rihill'), Js('riian'), Js('rilin'), Js('ril'), Js('rilirchel'), Js('rin'), Js('rinthil'), Js('rond'), Js('ruviel'), Js('rwen'), Js('sse'), Js('sty'), Js('te'), Js('tel'), Js('thel'), Js('thilith'), Js('thil'), Js('tte'), Js('ty'), Js('uin'), Js('val'), Js('wedh'), Js('waen'), Js('wenyl'), Js('weneth'), Js('weanyl'), Js('waenyl'), Js('weanyth'), Js('waenyth'), Js('wen'), Js('weneval'), Js('ynia'), Js('dra'), Js('fina'), Js('gina'), Js('landra'), Js('lerva'), Js('nea'), Js('nia'), Js('sa'), Js('sandra'), Js('thia'), Js('ys')]))
var.put('nm5', Js([Js('Acorn'), Js('Apple'), Js('Balf'), Js('Bark'), Js('Blue'), Js('Camo'), Js('Dorn'), Js('Dusk'), Js('Elm'), Js('Fern'), Js('Forest'), Js('Green'), Js('Ivy'), Js('Lichen'), Js('Lumber'), Js('Moss'), Js('Night'), Js('Oak'), Js('Oaken'), Js('Pine'), Js('River'), Js('Rose'), Js('Sage'), Js('Seed'), Js('Shady'), Js('Soft'), Js('Spring'), Js('Timber'), Js('Willow')]))
var.put('nm6', Js([Js('blossom'), Js('branch'), Js('brook'), Js('dale'), Js('grass'), Js('grove'), Js('hollow'), Js('lake'), Js('lock'), Js('mire'), Js('pool'), Js('rock'), Js('run'), Js('scrub'), Js('shade'), Js('sky'), Js('stone'), Js('thorn'), Js('vale'), Js('wind'), Js('wing'), Js('wood')]))
pass
pass


# Add lib to the module scope
bosmerNames = var.to_python()