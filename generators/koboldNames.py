__all__ = ['koboldNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            while PyJsStrictEq(var.get('nm9').get(var.get('rnd')),var.get('nm10').get(var.get('rnd2'))):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('lName', ((Js(' ')+var.get('nm9').get(var.get('rnd')))+var.get('nm10').get(var.get('rnd2'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(3.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    while (var.get('rnd5')<Js(15.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', (((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+var.get('lName')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    if (var.get('rnd')<Js(3.0)):
                        while (var.get('rnd5')<Js(5.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+var.get('lName')))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    if (var.get('i')<Js(4.0)):
                        while (var.get('rnd')<Js(5.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        while (var.get('rnd5')<Js(5.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('names', (((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd5')))+var.get('lName')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        if (var.get('rnd')<Js(5.0)):
                            while (var.get('rnd5')<Js(5.0)):
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('names', (((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm14').get(var.get('rnd5')))+var.get('lName')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(4.0)):
                        while (var.get('rnd')<Js(3.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+var.get('lName')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('lName')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('cr'), Js('cl'), Js('ch'), Js('chr'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('ghr'), Js('k'), Js('kr'), Js('kh'), Js('kn'), Js('q'), Js('qr'), Js('qh'), Js('sh'), Js('shr'), Js('sk'), Js('sn'), Js('str'), Js('sz'), Js('tr'), Js('v'), Js('vr'), Js('x'), Js('z'), Js('zr')]))
var.put('nm2', Js([Js('e'), Js('i'), Js('u'), Js('e'), Js('i'), Js('u'), Js('a'), Js('o'), Js('e'), Js('i'), Js('u'), Js('e'), Js('i'), Js('u'), Js('a'), Js('o'), Js('e'), Js('i'), Js('u'), Js('e'), Js('i'), Js('u'), Js('a'), Js('o'), Js('e'), Js('i'), Js('u'), Js('e'), Js('i'), Js('u'), Js('a'), Js('o'), Js('aa'), Js('ai'), Js('au'), Js('ei'), Js('ia'), Js('ee')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('k'), Js('kk'), Js('r'), Js('rr'), Js('z'), Js('zz'), Js('b'), Js('bb'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('k'), Js('kk'), Js('r'), Js('rr'), Js('z'), Js('zz'), Js('b'), Js('br'), Js('bb'), Js('d'), Js('dd'), Js('dr'), Js('dg'), Js('g'), Js('gg'), Js('gd'), Js('gn'), Js('gm'), Js('gr'), Js('gdr'), Js('gbr'), Js('gv'), Js('k'), Js('kk'), Js('kr'), Js('kz'), Js('kzr'), Js('kgr'), Js('kv'), Js('kdr'), Js('lg'), Js('lgr'), Js('lk'), Js('ldr'), Js('lbr'), Js('mg'), Js('mgr'), Js('mk'), Js('mc'), Js('md'), Js('mq'), Js('mz'), Js('mzr'), Js('ng'), Js('nd'), Js('ndr'), Js('ngr'), Js('nz'), Js('nsz'), Js('r'), Js('rr'), Js('rg'), Js('rgr'), Js('rd'), Js('rdr'), Js('rz'), Js('rk'), Js('rkr'), Js('tk'), Js('tz'), Js('tr'), Js('tv'), Js('z'), Js('zr'), Js('zk'), Js('zkr'), Js('zz'), Js('zzk'), Js('zd')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('c'), Js('d'), Js('g'), Js('k'), Js('n'), Js('nk'), Js('ng'), Js('nd'), Js('r'), Js('rk'), Js('rc'), Js('rg'), Js('s'), Js('sk'), Js('sz'), Js('x')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('b'), Js('bhr'), Js('bh'), Js('cy'), Js('cl'), Js('ch'), Js('chr'), Js('d'), Js('dh'), Js('g'), Js('gh'), Js('ghr'), Js('k'), Js('khr'), Js('kh'), Js('kn'), Js('kl'), Js('khn'), Js('sh'), Js('shr'), Js('sc'), Js('sl'), Js('sn'), Js('shn'), Js('sht'), Js('str'), Js('sz'), Js('t'), Js('th'), Js('thr'), Js('v'), Js('vr'), Js('z'), Js('zh'), Js('zr')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('o'), Js('o'), Js('u'), Js('u'), Js('ai'), Js('ei'), Js('ee'), Js('ea'), Js('aa')]))
var.put('nm7', Js([Js('b'), Js('bb'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('k'), Js('kk'), Js('r'), Js('rr'), Js('tt'), Js('zz'), Js('b'), Js('bb'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('k'), Js('kk'), Js('r'), Js('rr'), Js('tt'), Js('zz'), Js('b'), Js('bn'), Js('bb'), Js('d'), Js('dd'), Js('dj'), Js('dn'), Js('g'), Js('gg'), Js('gl'), Js('gn'), Js('gm'), Js('gr'), Js('ggn'), Js('ggv'), Js('gv'), Js('k'), Js('kk'), Js('kl'), Js('ks'), Js('ksh'), Js('kg'), Js('kn'), Js('lz'), Js('lv'), Js('lg'), Js('lgr'), Js('lkh'), Js('ldj'), Js('lbl'), Js('mg'), Js('mgl'), Js('mkh'), Js('mch'), Js('mdj'), Js('ms'), Js('msz'), Js('msr'), Js('ng'), Js('nd'), Js('ndr'), Js('ngd'), Js('ngl'), Js('nsh'), Js('nsz'), Js('r'), Js('rr'), Js('rg'), Js('rgl'), Js('rdh'), Js('rdj'), Js('rsz'), Js('rl'), Js('rkh'), Js('rch'), Js('th'), Js('tsz'), Js('thr'), Js('tt'), Js('zs'), Js('zsr'), Js('zhk'), Js('zkh'), Js('zz'), Js('zsz'), Js('zd')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('hl'), Js('hn'), Js('hs'), Js('l'), Js('n'), Js('ng'), Js('s'), Js('y'), Js('z')]))
var.put('nm9', Js([Js('ash'), Js('barb'), Js('barbed'), Js('bitter'), Js('blood'), Js('bone'), Js('boulder'), Js('brew'), Js('brick'), Js('broad'), Js('bronze'), Js('brown'), Js('claw'), Js('cliff'), Js('coal'), Js('cold'), Js('common'), Js('coven'), Js('crag'), Js('crow'), Js('dark'), Js('dim'), Js('dust'), Js('ember'), Js('far'), Js('fern'), Js('fist'), Js('flask'), Js('flat'), Js('fog'), Js('fool'), Js('fore'), Js('full'), Js('gore'), Js('grass'), Js('gray'), Js('green'), Js('grey'), Js('grime'), Js('grumble'), Js('hard'), Js('haze'), Js('heavy'), Js('hill'), Js('horn'), Js('iron'), Js('keen'), Js('krag'), Js('large'), Js('lead'), Js('leather'), Js('lone'), Js('molten'), Js('moon'), Js('morning'), Js('mountain'), Js('mud'), Js('muk'), Js('nether'), Js('night'), Js('oat'), Js('orb'), Js('pale'), Js('pebble'), Js('pine'), Js('plate'), Js('rain'), Js('rapid'), Js('red'), Js('river'), Js('rock'), Js('rough'), Js('rumble'), Js('sharp'), Js('shatter'), Js('silent'), Js('simple'), Js('skull'), Js('spider'), Js('star'), Js('steel'), Js('stone'), Js('storm'), Js('stout'), Js('strong'), Js('tusk'), Js('wild'), Js('wind')]))
var.put('nm10', Js([Js('arm'), Js('ash'), Js('back'), Js('bane'), Js('bash'), Js('basher'), Js('belly'), Js('belt'), Js('bender'), Js('blade'), Js('blood'), Js('blower'), Js('bluff'), Js('bone'), Js('born'), Js('bough'), Js('bow'), Js('brace'), Js('branch'), Js('brand'), Js('breaker'), Js('breath'), Js('bringer'), Js('brow'), Js('buckle'), Js('buster'), Js('chaser'), Js('chest'), Js('chew'), Js('chewer'), Js('chin'), Js('claw'), Js('cleaver'), Js('coat'), Js('crag'), Js('crest'), Js('crusher'), Js('cut'), Js('cutter'), Js('delver'), Js('digger'), Js('drifter'), Js('dust'), Js('eye'), Js('eyes'), Js('fall'), Js('fang'), Js('feather'), Js('feet'), Js('finger'), Js('fist'), Js('flare'), Js('flaw'), Js('foot'), Js('gaze'), Js('gazer'), Js('grip'), Js('grog'), Js('guard'), Js('gut'), Js('hammer'), Js('head'), Js('hide'), Js('horn'), Js('hunter'), Js('jaw'), Js('lash'), Js('mail'), Js('mane'), Js('mark'), Js('master'), Js('maul'), Js('maw'), Js('pelt'), Js('punch'), Js('rage'), Js('ripper'), Js('runner'), Js('scar'), Js('seeker'), Js('snarl'), Js('snout'), Js('spine'), Js('splinter'), Js('stalker'), Js('stride'), Js('strike'), Js('surge'), Js('thorn'), Js('tongue'), Js('watcher'), Js('wound')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bhr'), Js('cr'), Js('cl'), Js('ch'), Js('chr'), Js('d'), Js('g'), Js('ghr'), Js('k'), Js('kh'), Js('kn'), Js('sh'), Js('shr'), Js('sc'), Js('sn'), Js('str'), Js('sz'), Js('thr'), Js('v'), Js('vr'), Js('x'), Js('z'), Js('zr')]))
var.put('nm12', Js([Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('o'), Js('o'), Js('o'), Js('o'), Js('aa'), Js('ee'), Js('ia'), Js('ai'), Js('ei')]))
var.put('nm13', Js([Js('b'), Js('bb'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('k'), Js('kk'), Js('r'), Js('rr'), Js('tt'), Js('z'), Js('zz'), Js('bhr'), Js('dj'), Js('gn'), Js('gm'), Js('gr'), Js('gv'), Js('kz'), Js('kv'), Js('khr'), Js('lg'), Js('lgr'), Js('lk'), Js('ld'), Js('lz'), Js('ldr'), Js('mg'), Js('mk'), Js('mch'), Js('mq'), Js('msz'), Js('mzr'), Js('ng'), Js('nd'), Js('ndr'), Js('nz'), Js('nsz'), Js('rg'), Js('rd'), Js('rdr'), Js('rdj'), Js('rsz'), Js('rk'), Js('rch'), Js('tz'), Js('tr'), Js('thr'), Js('zs'), Js('zsz'), Js('zzs'), Js('zd')]))
var.put('nm14', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('r'), Js('s'), Js('sz'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
koboldNames = var.to_python()