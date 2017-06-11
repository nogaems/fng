__all__ = ['alienPetNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', var.get('nm2').get(var.get('rnd')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('rnd2')>Js(34.0)):
                        while (var.get('rnd4')>Js(34.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    if (var.get('rnd5')<Js(8.0)):
                        var.put('rnd6', Js(0.0))
                    var.put('names', (((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', var.get('nm1').get(var.get('rnd')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('rnd2')>Js(34.0)):
                        while (var.get('rnd4')>Js(34.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aether'), Js('Altair'), Js('Aphelion'), Js('Aster'), Js('Astro'), Js('Atlas'), Js('Azimuth'), Js('Baryon'), Js('Blazar'), Js('Blyde'), Js('Bolide'), Js('Boo'), Js('Bose'), Js('Bullet'), Js('Carbon'), Js('Chaos'), Js('Chewy'), Js('Chromos'), Js('Chrono'), Js('Chronos'), Js('Cluster'), Js('Comet'), Js('Core'), Js('Cosmo'), Js('Cosmos'), Js('Creature'), Js('Crescent'), Js('Crimson'), Js('Cyclops'), Js('Dalek'), Js('Darth'), Js('Diablo'), Js('Dock'), Js('Doppler'), Js('Drake'), Js('Dusty'), Js('Einstein'), Js('Element'), Js('Equinox'), Js('Fang'), Js('Fire'), Js('Flare'), Js('Galax'), Js('Gamma'), Js('Ghost'), Js('Gibbs'), Js('Glob'), Js('Grav'), Js('Grog'), Js('Halo'), Js('Hannibal'), Js('Helio'), Js('Hertz'), Js('Hubble'), Js('Hubbles'), Js('Hunter'), Js('Hyde'), Js('Hyper'), Js('Ion'), Js('Irone'), Js('It'), Js('Jabs'), Js('Jet'), Js('Kelvin'), Js('Kepler'), Js('Kraken'), Js('Kuiper'), Js('Lecter'), Js('Lens'), Js('Light'), Js('Lightyear'), Js('Magni'), Js('Malif'), Js('Meridian'), Js('Merlin'), Js('Micron'), Js('Milky'), Js('Moonbeam'), Js('Naut'), Js('Nebula'), Js('Neutron'), Js('Nibbler'), Js('Nova'), Js('Ogre'), Js('Omega'), Js('Orb'), Js('Orbit'), Js('Parallax'), Js('Phantom'), Js('Phase'), Js('Pixel'), Js('Prism'), Js('Pulse'), Js('Pyre'), Js('Pyro'), Js('Radio'), Js('Raye'), Js('Reaper'), Js('Rocket'), Js('Salem'), Js('Sasquatch'), Js('Scar'), Js('Seti'), Js('Shadow'), Js('Sky'), Js('Solace'), Js('Soleil'), Js('Solstice'), Js('Spectre'), Js('Spectro'), Js('Spook'), Js('Spot'), Js('Spud'), Js('Starlight'), Js('Steele'), Js('Syzygy'), Js('Terra'), Js('Thing'), Js('Trojan'), Js('Umbra'), Js('Vayne'), Js('Vlad'), Js('Void'), Js('Xray'), Js('Yoda'), Js('Zero'), Js('Zodiac')]))
var.put('nm2', Js([Js('Aerial'), Js('Aire'), Js('Andromeda'), Js('Aphelia'), Js('Astero'), Js('Astral'), Js('Astralle'), Js('Aura'), Js('Aurora'), Js('Celeste'), Js('Chewy'), Js('Chromy'), Js('Chronis'), Js('Cloude'), Js('Comette'), Js('Cookie'), Js('Corona'), Js('Cosmo'), Js('Density'), Js('Duste'), Js('Eclipse'), Js('Ejecta'), Js('Element'), Js('Ellipse'), Js('Enigma'), Js('Equinox'), Js('Eye'), Js('Flare'), Js('Fyre'), Js('Galaxy'), Js('Gamma'), Js('Ghoste'), Js('Gibbsy'), Js('Gravi'), Js('Gravity'), Js('Harpie'), Js('Helio'), Js('Hydra'), Js('Ice'), Js('Infra'), Js('Ion'), Js('Iso'), Js('Light'), Js('Lumi'), Js('Lumina'), Js('Luna'), Js('Magni'), Js('Mare'), Js('Medusa'), Js('Meridian'), Js('Midnight'), Js('Milky'), Js('Moon'), Js('Moonbeam'), Js('Moone'), Js('Moonlight'), Js('Nadir'), Js('Nasa'), Js('Nebula'), Js('Nessie'), Js('Nighte'), Js('Nova'), Js('Oracle'), Js('Orbit'), Js('Ozone'), Js('Patera'), Js('Penumbra'), Js('Pixel'), Js('Plasma'), Js('Polaris'), Js('Prism'), Js('Pulse'), Js('Pyre'), Js('Raye'), Js('Selena'), Js('Seti'), Js('Shade'), Js('Shadow'), Js('Sky'), Js('Skylar'), Js('Sola'), Js('Solare'), Js('Solstice'), Js('Spectra'), Js('Spooky'), Js('Sputs'), Js('Star'), Js('Stardust'), Js('Starlight'), Js('Stella'), Js('Stellar'), Js('Summer'), Js('Sunspot'), Js('Syzygy'), Js('Tera'), Js('Terra'), Js('Therma'), Js('Twilight'), Js('Umbra'), Js('Venus'), Js('Violet'), Js('Voide'), Js('Winter'), Js('Zenith')]))
var.put('nm3', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('ch'), Js('sh'), Js('gr'), Js('br'), Js('gl'), Js('kr'), Js('kl'), Js('pr'), Js('ph'), Js('str'), Js('st'), Js('wr')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ai'), Js('ao'), Js('au'), Js('ea'), Js('ei'), Js('eo'), Js('eu'), Js('ee'), Js('aa'), Js('ia'), Js('ie'), Js('io'), Js('iu'), Js('oa'), Js('oe'), Js('oo'), Js('ou'), Js('ua'), Js('ue'), Js('ui'), Js('uo'), Js('uu')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('y'), Js('z'), Js('bb'), Js('cc'), Js('dd'), Js('gg'), Js('hh'), Js('ll'), Js('mm'), Js('nn'), Js('rr'), Js('ss'), Js('tt'), Js('vv'), Js('xx'), Js('zz'), Js('bl'), Js('br'), Js('by'), Js('cd'), Js('ch'), Js('ck'), Js('cl'), Js('cm'), Js('cn'), Js('cr'), Js('cs'), Js('ct'), Js('cv'), Js('cz'), Js('cst'), Js('cstr'), Js('dr'), Js('dy'), Js('gd'), Js('gl'), Js('gr'), Js('gy'), Js('hk'), Js('hl'), Js('hm'), Js('hn'), Js('hr'), Js('kd'), Js('kl'), Js('km'), Js('kn'), Js('kr'), Js('ky'), Js('kx'), Js('lc'), Js('ld'), Js('lg'), Js('lk'), Js('lm'), Js('ln'), Js('lr'), Js('lt'), Js('lv'), Js('ly'), Js('lz'), Js('nr'), Js('ny'), Js('nz'), Js('ns'), Js('nst'), Js('nstr'), Js('rb'), Js('rc'), Js('rd'), Js('rg'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rs'), Js('rt'), Js('rst'), Js('rstr'), Js('rv'), Js('rx'), Js('ry'), Js('rz'), Js('sb'), Js('sc'), Js('sd'), Js('sg'), Js('sh'), Js('sk'), Js('sl'), Js('sm'), Js('sn'), Js('sr'), Js('st'), Js('str'), Js('sy'), Js('sz'), Js('tl'), Js('tr'), Js('ty'), Js('tz'), Js('vl'), Js('vr'), Js('vy'), Js('xr'), Js('xy'), Js('zl'), Js('zy')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('x'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('x'), Js('rc'), Js('rd'), Js('rg'), Js('rk'), Js('rm'), Js('rn'), Js('rs'), Js('rt'), Js('rx'), Js('rz'), Js('st'), Js('sh'), Js('sz'), Js('ns'), Js('nz')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ea'), Js('ee'), Js('aa'), Js('ia'), Js('ua'), Js('ue')]))
pass
pass


# Add lib to the module scope
alienPetNames = var.to_python()