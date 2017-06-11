__all__ = ['zeldaDekuNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(7.0)):
                var.put('names', ((Js('De')+var.get('nm3').get(var.get('rnd3')))+Js('i')))
            else:
                var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('D'), Js('F'), Js('G'), Js('H'), Js('K'), Js('L'), Js('M'), Js('N'), Js('P'), Js('R'), Js('S'), Js('T'), Js('V'), Js('W'), Js('Z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('bb'), Js('bc'), Js('bd'), Js('bk'), Js('bl'), Js('bm'), Js('bn'), Js('br'), Js('bs'), Js('bv'), Js('bw'), Js('bz'), Js('cb'), Js('cc'), Js('cf'), Js('ch'), Js('ck'), Js('cl'), Js('cm'), Js('cn'), Js('cp'), Js('cq'), Js('cr'), Js('cs'), Js('cw'), Js('cz'), Js('db'), Js('dd'), Js('dg'), Js('dh'), Js('dk'), Js('dl'), Js('dm'), Js('dn'), Js('dp'), Js('dr'), Js('ds'), Js('dv'), Js('dw'), Js('dz'), Js('fb'), Js('fd'), Js('ff'), Js('fg'), Js('fk'), Js('fl'), Js('fm'), Js('fn'), Js('fp'), Js('fr'), Js('fs'), Js('ft'), Js('fw'), Js('fz'), Js('gg'), Js('kb'), Js('kd'), Js('kk'), Js('kl'), Js('km'), Js('kn'), Js('kp'), Js('kr'), Js('ks'), Js('kt'), Js('kw'), Js('kz'), Js('lb'), Js('lc'), Js('ld'), Js('lf'), Js('lg'), Js('lk'), Js('ll'), Js('lm'), Js('ln'), Js('lp'), Js('lq'), Js('lr'), Js('ls'), Js('lt'), Js('lv'), Js('lw'), Js('lz'), Js('mb'), Js('md'), Js('mk'), Js('ml'), Js('mm'), Js('mn'), Js('mp'), Js('mr'), Js('ms'), Js('mt'), Js('mv'), Js('mz'), Js('nb'), Js('nc'), Js('nd'), Js('nf'), Js('ng'), Js('nk'), Js('nl'), Js('nm'), Js('nn'), Js('np'), Js('nq'), Js('nr'), Js('ns'), Js('nt'), Js('nv'), Js('nw'), Js('nz'), Js('pc'), Js('pg'), Js('ph'), Js('pk'), Js('pl'), Js('pm'), Js('pn'), Js('pp'), Js('pr'), Js('ps'), Js('pt'), Js('pv'), Js('pz'), Js('qq'), Js('rb'), Js('rc'), Js('rd'), Js('rf'), Js('rg'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rp'), Js('rq'), Js('rr'), Js('rs'), Js('rt'), Js('rv'), Js('rw'), Js('rz'), Js('sb'), Js('sc'), Js('sd'), Js('sg'), Js('sh'), Js('sk'), Js('sl'), Js('sm'), Js('sn'), Js('sp'), Js('sr'), Js('ss'), Js('st'), Js('sz'), Js('tb'), Js('tc'), Js('tg'), Js('tk'), Js('tl'), Js('tm'), Js('tn'), Js('tp'), Js('tr'), Js('ts'), Js('tt'), Js('tv'), Js('tw'), Js('tz'), Js('vv'), Js('wb'), Js('wd'), Js('wg'), Js('wk'), Js('wl'), Js('wm'), Js('wn'), Js('wp'), Js('wr'), Js('ws'), Js('wt'), Js('ww'), Js('wz'), Js('xx'), Js('zb'), Js('zc'), Js('zf'), Js('zg'), Js('zk'), Js('zl'), Js('zm'), Js('zn'), Js('zp'), Js('zr'), Js('zs'), Js('zt'), Js('zw'), Js('zz')]))
pass
pass


# Add lib to the module scope
zeldaDekuNames = var.to_python()