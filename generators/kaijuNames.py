__all__ = ['kaijuNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm2', 'result'])
    var.put('nm1', Js([Js('Aby'), Js('Abys'), Js('Ae'), Js('Aeri'), Js('Aethe'), Js('Amphi'), Js('Ana'), Js('Anar'), Js('Aqu'), Js('Aqua'), Js('Ata'), Js('Ataxi'), Js('Au'), Js('Aura'), Js('Bar'), Js('Barba'), Js('Barbar'), Js('Bas'), Js('Bla'), Js('Bli'), Js('Boul'), Js('Bri'), Js('Bru'), Js('Bruta'), Js('Canni'), Js('Canniba'), Js('Carni'), Js('Cata'), Js('Catacly'), Js('Chao'), Js('Cin'), Js('Coba'), Js('Cobal'), Js('Cor'), Js('Corp'), Js('Cra'), Js('Crim'), Js('Cro'), Js('Crown'), Js('Cry'), Js('Cryo'), Js('Cryp'), Js('Crys'), Js('Daw'), Js('Dia'), Js('Diablo'), Js('Diabo'), Js('Diamo'), Js('Ebo'), Js('Ebon'), Js('Elec'), Js('Elepha'), Js('Elu'), Js('Em'), Js('Eme'), Js('Emera'), Js('Eter'), Js('Ethe'), Js('Ether'), Js('Eva'), Js('Fera'), Js('Fero'), Js('Fi'), Js('Fie'), Js('Fla'), Js('Fren'), Js('Fri'), Js('Fro'), Js('Garga'), Js('Gargan'), Js('Giga'), Js('Gigan'), Js('Gla'), Js('Grie'), Js('Grim'), Js('Gris'), Js('Griz'), Js('Hanniba'), Js('Infer'), Js('Iro'), Js('Ivo'), Js('Levi'), Js('Levia'), Js('Male'), Js('Malevo'), Js('Mas'), Js('Matri'), Js('Mon'), Js('Mons'), Js('Mour'), Js('Neth'), Js('Nethe'), Js('Obsi'), Js('Obsidi'), Js('Ony'), Js('Ore'), Js('Patri'), Js('Pha'), Js('Phan'), Js('Phanto'), Js('Phibi'), Js('Pri'), Js('Prima'), Js('Prime'), Js('Primi'), Js('Pyro'), Js('Ra'), Js('Rabi'), Js('Rava'), Js('Raz'), Js('Saphi'), Js('Sava'), Js('Scar'), Js('Sco'), Js('Scor'), Js('Scree'), Js('Sha'), Js('Shado'), Js('Sil'), Js('Slen'), Js('Som'), Js('Spec'), Js('Spi'), Js('Spiri'), Js('Stal'), Js('Sten'), Js('Ston'), Js('Stor'), Js('Storm'), Js('Sty'), Js('Su'), Js('Supre'), Js('Tacly'), Js('Talo'), Js('Ter'), Js('Thor'), Js('Thun'), Js('Tita'), Js('Titan'), Js('Tor'), Js('Tox'), Js('Tran'), Js('Tus'), Js('Ven'), Js('Veno'), Js('Vi'), Js('Vic'), Js('Vici'), Js('Vole'), Js('Vor'), Js('War')]))
    var.put('nm2', Js([Js('bara'), Js('borg'), Js('cada'), Js('coatl'), Js('da'), Js('dan'), Js('dius'), Js('don'), Js('dorah'), Js('dorg'), Js('doro'), Js('doru'), Js('dos'), Js('dragon'), Js('dun'), Js('dus'), Js('dusa'), Js('gami'), Js('gan'), Js('gar'), Js('garu'), Js('gary'), Js('gas'), Js('gauros'), Js('gira'), Js('go'), Js('gon'), Js('gora'), Js('guar'), Js('guera'), Js('guma'), Js('hara'), Js('jin'), Js('ju'), Js('lak'), Js('lar'), Js('laria'), Js('las'), Js('lios'), Js('lon'), Js('lus'), Js('majin'), Js('mera'), Js('mon'), Js('mutul'), Js('nar'), Js('nula'), Js('nulon'), Js('pede'), Js('pod'), Js('por'), Js('ra'), Js('ragon'), Js('rah'), Js('ran'), Js('randa'), Js('rappa'), Js('ras'), Js('rashi'), Js('rax'), Js('ria'), Js('rigar'), Js('rola'), Js('ron'), Js('ros'), Js('rugon'), Js('rus'), Js('sari'), Js('saurus'), Js('sis'), Js('sos'), Js('sus'), Js('talak'), Js('tax'), Js('thrax'), Js('tor'), Js('tori'), Js('tra'), Js('tul'), Js('vern'), Js('vore'), Js('yah'), Js('zilla')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
kaijuNames = var.to_python()