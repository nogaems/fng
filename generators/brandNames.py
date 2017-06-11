__all__ = ['brandNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(2.0)):
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('names', ((var.get('nm11').get(var.get('rnd1'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3'))))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', (((var.get('nm1').get(var.get('rnd1'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4'))))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('names', (((var.get('nm1').get(var.get('rnd1'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('names', (var.get('nm11').get(var.get('rnd1'))+var.get('nm7').get(var.get('rnd3'))))
                        else:
                            if (var.get('i')<Js(9.0)):
                                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                                var.put('names', (((var.get('nm11').get(var.get('rnd1'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
                            else:
                                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                                var.put('names', ((var.get('nm8').get(var.get('rnd1'))+var.get('nm1').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('pr'), Js('qr'), Js('sr'), Js('tr'), Js('vr'), Js('wr'), Js('zr'), Js('str'), Js('spr'), Js('st'), Js('bl'), Js('cl'), Js('dl'), Js('fl'), Js('gl'), Js('kl'), Js('pl'), Js('sl'), Js('vl'), Js('zl'), Js('bh'), Js('ch'), Js('dh'), Js('gh'), Js('kh'), Js('ph'), Js('sh'), Js('sch'), Js('th'), Js('thr'), Js('sph'), Js('vh'), Js('wh'), Js('zh'), Js('gn'), Js('kn'), Js('sn'), Js('zn'), Js('sm'), Js('zm'), Js('sw'), Js('tw'), Js('zw'), Js('sc')]))
var.put('nm2', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm4', Js([Js('ee'), Js('eu'), Js('eo'), Js('ea'), Js('ei'), Js('aa'), Js('ai'), Js('au'), Js('ae'), Js('io'), Js('ia'), Js('iu'), Js('ie'), Js('oo'), Js('oa'), Js('ou'), Js('oe'), Js('oi'), Js('uu'), Js('ua'), Js('ue'), Js('ui'), Js('uo')]))
var.put('nm5', Js([Js('bb'), Js('bd'), Js('bh'), Js('br'), Js('cc'), Js('ch'), Js('ck'), Js('cl'), Js('cr'), Js('cs'), Js('csh'), Js('ct'), Js('cth'), Js('cz'), Js('dd'), Js('dg'), Js('dn'), Js('dr'), Js('ff'), Js('fk'), Js('fn'), Js('fr'), Js('ft'), Js('gb'), Js('gd'), Js('gg'), Js('gh'), Js('gm'), Js('gn'), Js('gr'), Js('hh'), Js('hk'), Js('hl'), Js('hm'), Js('hn'), Js('hr'), Js('kh'), Js('kk'), Js('kn'), Js('kr'), Js('ks'), Js('kt'), Js('kz'), Js('lb'), Js('lc'), Js('ld'), Js('lf'), Js('lg'), Js('lh'), Js('lk'), Js('ll'), Js('lm'), Js('ln'), Js('lp'), Js('lph'), Js('lq'), Js('lr'), Js('ls'), Js('lsh'), Js('lt'), Js('lw'), Js('lz'), Js('mb'), Js('md'), Js('mh'), Js('mk'), Js('ml'), Js('mm'), Js('mn'), Js('mp'), Js('mph'), Js('mr'), Js('ms'), Js('msh'), Js('mt'), Js('nc'), Js('nd'), Js('ng'), Js('nk'), Js('nl'), Js('nn'), Js('np'), Js('nq'), Js('nr'), Js('ns'), Js('nt'), Js('nw'), Js('nz'), Js('ph'), Js('pm'), Js('pn'), Js('pp'), Js('pq'), Js('pr'), Js('phr'), Js('pt'), Js('ps'), Js('pz'), Js('rb'), Js('rc'), Js('rd'), Js('rf'), Js('rg'), Js('rh'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rp'), Js('rph'), Js('rq'), Js('rr'), Js('rs'), Js('rst'), Js('rt'), Js('rw'), Js('rz'), Js('sb'), Js('sc'), Js('sd'), Js('sh'), Js('sk'), Js('sl'), Js('sm'), Js('sn'), Js('sp'), Js('sph'), Js('sr'), Js('ss'), Js('st'), Js('str'), Js('sz'), Js('th'), Js('tl'), Js('tm'), Js('tn'), Js('tr'), Js('thr')]))
var.put('nm6', Js([Js('c'), Js('ck'), Js('d'), Js('f'), Js('g'), Js('ght'), Js('l'), Js('ld'), Js('ll'), Js('m'), Js('mp'), Js('n'), Js('nd'), Js('ng'), Js('ngs'), Js('nk'), Js('nt'), Js('q'), Js('p'), Js('pp'), Js('r'), Js('rn'), Js('rs'), Js('s'), Js('sh'), Js('sm'), Js('ss'), Js('st'), Js('t'), Js('th'), Js('w'), Js('wn'), Js('x'), Js('y'), Js('z')]))
var.put('nm7', Js([Js('able'), Js('ack'), Js('acy'), Js('ad'), Js('age'), Js('ail'), Js('ain'), Js('ake'), Js('al'), Js('ale'), Js('all'), Js('am'), Js('ame'), Js('an'), Js('ance'), Js('ank'), Js('ap'), Js('app'), Js('ar'), Js('ash'), Js('at'), Js('ate'), Js('aw'), Js('ay'), Js('dom'), Js('eat'), Js('eel'), Js('eep'), Js('eet'), Js('ell'), Js('en'), Js('ence'), Js('ent'), Js('er'), Js('ers'), Js('esque'), Js('est'), Js('ful'), Js('fy'), Js('ible'), Js('ic'), Js('ical'), Js('ice'), Js('ick'), Js('ide'), Js('ier'), Js('ies'), Js('ife'), Js('ify'), Js('ight'), Js('ile'), Js('ill'), Js('in'), Js('ine'), Js('ing'), Js('ink'), Js('ion'), Js('ious'), Js('ip'), Js('ise'), Js('ish'), Js('ism'), Js('ist'), Js('it'), Js('ite'), Js('ity'), Js('ive'), Js('ize'), Js('led'), Js('less'), Js('ment'), Js('ned'), Js('ness'), Js('oat'), Js('ock'), Js('og'), Js('oil'), Js('oke'), Js('oo'), Js('ood'), Js('oof'), Js('ook'), Js('ool'), Js('oom'), Js('oon'), Js('oop'), Js('oot'), Js('op'), Js('or'), Js('ore'), Js('orn'), Js('ot'), Js('ought'), Js('ould'), Js('ous'), Js('ouse'), Js('out'), Js('ow'), Js('own'), Js('red'), Js('ship'), Js('sion'), Js('ted'), Js('ter'), Js('tes'), Js('tion'), Js('ty'), Js('uck'), Js('ug'), Js('ump'), Js('un'), Js('unk'), Js('y'), Js('zed')]))
var.put('nm8', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('eu'), Js('eo'), Js('ea'), Js('ei'), Js('aa'), Js('ai'), Js('au'), Js('ae'), Js('io'), Js('ia'), Js('iu'), Js('ie'), Js('oo'), Js('oa'), Js('ou'), Js('oe'), Js('oi'), Js('uu'), Js('ua'), Js('ue'), Js('ui'), Js('uo')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('eu'), Js('eo'), Js('ea'), Js('ei'), Js('aa'), Js('ai'), Js('au'), Js('ae'), Js('io'), Js('ia'), Js('iu'), Js('ie'), Js('oo'), Js('oa'), Js('ou'), Js('oe'), Js('oi'), Js('uu'), Js('ua'), Js('ue'), Js('ui'), Js('uo')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm11', Js([Js('A'), Js('An'), Js('Ante'), Js('Anti'), Js('As'), Js('Auto'), Js('Bi'), Js('Bin'), Js('Car'), Js('Cha'), Js('Char'), Js('Com'), Js('Como'), Js('Con'), Js('Contra'), Js('De'), Js('Demi'), Js('Di'), Js('Dis'), Js('Du'), Js('En'), Js('Ex'), Js('Extra'), Js('Gall'), Js('Hemi'), Js('Hyper'), Js('Il'), Js('Im'), Js('In'), Js('Inter'), Js('Intra'), Js('Ir'), Js('Micro'), Js('Mono'), Js('Non'), Js('Omni'), Js('Out'), Js('Over'), Js('Par'), Js('Post'), Js('Pre'), Js('Pro'), Js('Quin'), Js('Res'), Js('Rese'), Js('Scar'), Js('Semi'), Js('Sha'), Js('Spin'), Js('Sta'), Js('Stra'), Js('Stri'), Js('Sub'), Js('Syn'), Js('Tech'), Js('Tran'), Js('Trans'), Js('Tri'), Js('Un'), Js('Uni')]))
pass
pass


# Add lib to the module scope
brandNames = var.to_python()