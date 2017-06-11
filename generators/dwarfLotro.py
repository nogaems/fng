__all__ = ['dwarfLotro']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (var.get('nm4').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('A'), Js('Ara'), Js('Alfo'), Js('Bari'), Js('Be'), Js('Bo'), Js('Bha'), Js('Bu'), Js('Ba'), Js('Bra'), Js('Bro'), Js('Brou'), Js('Bru'), Js('Da'), Js('Dalo'), Js('Dare'), Js('De'), Js('Dhu'), Js('Dho'), Js('Do'), Js('Dora'), Js('Dwo'), Js('Dou'), Js('Duri'), Js('Du'), Js('El'), Js('Eri'), Js('Fi'), Js('Fo'), Js('Fo'), Js('Ga'), Js('Gi'), Js('Gla'), Js('Glori'), Js('Go'), Js('Gra'), Js('Gro'), Js('Groo'), Js('Gru'), Js('Grou'), Js('Ha'), Js('Ha'), Js('He'), Js('He'), Js('Ho'), Js('Hou'), Js('Hu'), Js('Ja'), Js('Jo'), Js('Ka'), Js('Khe'), Js('Khu'), Js('Khou'), Js('Ko'), Js('Ku'), Js('Ki'), Js('Kra'), Js('Kro'), Js('Ma'), Js('Mo'), Js('Mu'), Js('Na'), Js('No'), Js('Nu'), Js('Nora'), Js('Nura'), Js('Ne'), Js('No'), Js('O'), Js('Ori'), Js('Rei'), Js('Ra'), Js('Ru'), Js('Sa'), Js('Si'), Js('Sna'), Js('Sko'), Js('Ska'), Js('Stro'), Js('The'), Js('Thi'), Js('Tho'), Js('Thra'), Js('Tha'), Js('Tore'), Js('Tha'), Js('Thra'), Js('Thro'), Js('Thu'), Js('Tu'), Js('U'), Js('Umi'), Js('Va'), Js('Vo'), Js('Whu'), Js('We')]))
var.put('nm2', Js([Js('b'), Js('br'), Js('dd'), Js('d'), Js('dr'), Js('dm'), Js('dgr'), Js('f'), Js('fr'), Js('gr'), Js('gg'), Js('gh'), Js('gn'), Js('k'), Js('kh'), Js('kgr'), Js('kdr'), Js('kk'), Js('kh'), Js('kr'), Js('l'), Js('lg'), Js('lgr'), Js('ldr'), Js('lm'), Js('md'), Js('mn'), Js('m'), Js('mm'), Js('mr'), Js('n'), Js('nd'), Js('ndr'), Js('ngr'), Js('nm'), Js('r'), Js('rr'), Js('rgr'), Js('rdr'), Js('rb'), Js('rg'), Js('rn'), Js('rh'), Js('rd'), Js('rm'), Js('rs'), Js('rf'), Js('s'), Js('ss'), Js('sdr'), Js('sgr'), Js('st'), Js('str'), Js('t'), Js('tr'), Js('tm'), Js('th'), Js('tdr'), Js('tgr'), Js('v'), Js('vr'), Js('z'), Js('zm'), Js('zn'), Js('zz')]))
var.put('nm3', Js([Js('ori'), Js('oin'), Js('ili'), Js('alin'), Js('orin'), Js('osi'), Js('imli'), Js('ormur'), Js('ac'), Js('aic'), Js('aec'), Js('ec'), Js('eac'), Js('ic'), Js('oc'), Js('oic'), Js('ouc'), Js('ack'), Js('aeck'), Js('eck'), Js('eack'), Js('ick'), Js('ock'), Js('oick'), Js('ouck'), Js('uck'), Js('uc'), Js('ad'), Js('aed'), Js('ed'), Js('ead'), Js('id'), Js('od'), Js('oid'), Js('oud'), Js('ud'), Js('uid'), Js('ag'), Js('aeg'), Js('eg'), Js('eag'), Js('ig'), Js('og'), Js('oug'), Js('ug'), Js('ak'), Js('aek'), Js('ek'), Js('eak'), Js('ik'), Js('ok'), Js('oki'), Js('uk'), Js('uik'), Js('ouk'), Js('uki'), Js('al'), Js('ael'), Js('el'), Js('eal'), Js('il'), Js('ol'), Js('oli'), Js('olin'), Js('olim'), Js('olir'), Js('oul'), Js('ul'), Js('uli'), Js('ulim'), Js('ulir'), Js('uil'), Js('am'), Js('ami'), Js('amli'), Js('amri'), Js('aem'), Js('em'), Js('eam'), Js('im'), Js('om'), Js('omli'), Js('omri'), Js('omi'), Js('oum'), Js('um'), Js('umi'), Js('umir'), Js('umin'), Js('umli'), Js('umlir'), Js('umlin'), Js('umri'), Js('an'), Js('aen'), Js('en'), Js('ean'), Js('in'), Js('on'), Js('onlim'), Js('onlir'), Js('oun'), Js('un'), Js('unli'), Js('unri'), Js('ar'), Js('arlum'), Js('arlun'), Js('arlug'), Js('arlig'), Js('aer'), Js('er'), Js('erlum'), Js('erlun'), Js('erlug'), Js('erlig'), Js('ear'), Js('ir'), Js('irlum'), Js('irlun'), Js('or'), Js('orli'), Js('orlim'), Js('orlum'), Js('orlun'), Js('orlig'), Js('orlug'), Js('oir'), Js('our'), Js('ur'), Js('uri'), Js('urim'), Js('urum'), Js('us'), Js('as'), Js('ous'), Js('aes'), Js('eas'), Js('at'), Js('atir'), Js('atum'), Js('atin'), Js('aet'), Js('et'), Js('eat'), Js('it'), Js('ot'), Js('otir'), Js('atin'), Js('otum'), Js('out'), Js('ut'), Js('ath'), Js('aeth'), Js('eth'), Js('eath'), Js('ith'), Js('oth'), Js('outh'), Js('uth')]))
var.put('nm4', Js([Js('D'), Js('F'), Js('G'), Js('H'), Js('K'), Js('L'), Js('M'), Js('N'), Js('R'), Js('T'), Js('Th'), Js('W'), Js('Dr'), Js('Dw'), Js('Fl'), Js('Gl'), Js('Thr'), Js('D'), Js('F'), Js('G'), Js('H'), Js('K'), Js('L'), Js('M'), Js('N'), Js('R'), Js('T'), Js('Th'), Js('W'), Js('Dr'), Js('Dw'), Js('Fl'), Js('Gl'), Js('Thr')]))
pass
pass


# Add lib to the module scope
dwarfLotro = var.to_python()