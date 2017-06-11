__all__ = ['armyNames']

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
            if (var.get('i')<Js(6.0)):
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (Js('The ')+var.get('nm1').get(var.get('rnd0'))))
            else:
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm2').get(var.get('rnd0')))+var.get('nm3').get(var.get('rnd1')))+var.get('nm4').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Angels'), Js('Black Brigade'), Js('Black Devils'), Js('Black Saints'), Js('Black Sheep'), Js('Black Wings'), Js('Blessed Battalion'), Js('Blood Bandits'), Js('Blood Battalion'), Js('Blood Brigade'), Js('Broken Brigade'), Js('Cardinal Command'), Js('Cardinal Company'), Js('Cardinal Corps'), Js('Cataclysm Corps'), Js('Challengers'), Js('Chosen'), Js('Clan'), Js('Cloud'), Js('Cluster'), Js('Congregate'), Js('Contract'), Js('Covert Battalion'), Js('Covert Company'), Js('Covert Corps'), Js('Crimsom Cloud'), Js('Crimson Clan'), Js('Crimson Commander'), Js('Crimson Company'), Js('Crimson Contract'), Js('Crimson Corps'), Js('Crimson Crew'), Js('Crimson Curators'), Js('Crimson Keepers'), Js('Crimson Wings'), Js('Crush'), Js('Crushing'), Js('Culling Cavalry'), Js('Curators'), Js('Dark Division'), Js('Death Corps'), Js("Death's Angels"), Js('Death Division'), Js('Death Formation'), Js('Death Pack'), Js('Death Patrol'), Js('Death Platoon'), Js('Death Squad'), Js('Demons'), Js('Destiny Division'), Js('Dogs'), Js('Doom Corps'), Js('Doom Squad'), Js('Doomed Ones'), Js('Ebon Enders'), Js('Ebon Eyes'), Js('Ebon Wings'), Js('Eclipse'), Js('Extinction'), Js('Extras'), Js('Final Division'), Js('Final Flight'), Js('Final Flock'), Js('Final Regiment'), Js('Fire Battalion'), Js('Fire Flight'), Js('Fire Troops'), Js('Flaming Army'), Js('Flaming Battalion'), Js('Flaming Flock'), Js('Flock'), Js('Forgotten Army'), Js('Forgotten Battalion'), Js('Forgotten Soldiers'), Js('Forsaken'), Js('Forsaken Army'), Js('Forsaken Battalion'), Js('Forsaken Flock'), Js('Forsaken Soldiers'), Js('Great Army'), Js('Great Company'), Js('Great Guard'), Js('Great Guardians'), Js('Guard'), Js('Guardians'), Js('Hallowed Herd'), Js('Hallowed Horde'), Js('Hallowed Host'), Js('Hell Hosts'), Js('Hell Squad'), Js('Hellfire Horde'), Js('Hellfire Legion'), Js('Hellfire Squad'), Js('Hellhounds'), Js('Herd'), Js('Hidden'), Js('Hollow Herd'), Js('Hollow Horde'), Js('Hollow Host'), Js('Hopeless'), Js('Horde'), Js('Host'), Js('Hounds'), Js('Illustrious'), Js('Immortals'), Js('Invincibles'), Js('Keepers'), Js('Last Division'), Js('Last Hope'), Js('Last Legion'), Js('Last Regiment'), Js('Legion'), Js('Marauders'), Js('Maroon Marauders'), Js('Maroon Martyrs'), Js('Maroon Mob'), Js('Maroon Myriad'), Js('Martyrs'), Js('Mob'), Js('Myriad'), Js('New Leadership'), Js('New Order'), Js('Night'), Js('Opposition'), Js('Order'), Js('Pacifists'), Js('Peace Bringers'), Js('Peace Corps'), Js('Phalanx'), Js('Pillagers'), Js('Preservers'), Js('Prime Battalion'), Js('Prime Platoon'), Js('Prime Preservers'), Js('Punishment'), Js('Pure'), Js('Pure Battalion'), Js('Pure Platoon'), Js('Rangers'), Js('Ravagers'), Js('Rebels'), Js('Red Rangers'), Js('Red Regiment'), Js('Red Riders'), Js('Reserve'), Js('Reserve Regiment'), Js('Retired'), Js('Robed Riders'), Js('Rose Regiment'), Js('Rose Riders'), Js('Ruby Regiment'), Js('Ruby Riders'), Js('Ruthless'), Js('Ruthless Ravagers'), Js('Ruthless Regiment'), Js('Saints'), Js('Sanguine Sentinels'), Js('Sanguine Shepherds'), Js('Sanguine Shroud'), Js('Sanguine Soldiers'), Js('Sanguine Squad'), Js('Sanguine Sundry'), Js('Sanguine Swarm'), Js('Sentinels'), Js('Serpent Soldiers'), Js('Serpent Squad'), Js('Shadow'), Js('Shepherds'), Js('Shroud'), Js('Siege Battalion'), Js('Silver Lining'), Js('Silver Soldiers'), Js('Silver Squad'), Js('Silver Swarm'), Js('Sundry'), Js('Super Soldiers'), Js('Supervisors'), Js('Supreme Army'), Js('Supreme Battalion'), Js('Supreme Command'), Js('Supreme Regiment'), Js('Swarm'), Js('Terror Troops'), Js('Thunder Troops'), Js('Titans'), Js('True Order'), Js('Trust Troops'), Js('Undefeated'), Js('Unforgiven'), Js('Union'), Js('Unstoppables'), Js('Vanquishers'), Js('Velvet Vanquishers'), Js('Velvet Veil'), Js('Velvet Victors'), Js('Venom Troops'), Js('Victors'), Js('Vortex'), Js('Void'), Js('Wardens'), Js('Watchdogs'), Js('White Wardens'), Js('White Wings')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ai'), Js('ao'), Js('au'), Js('aa'), Js('ee'), Js('ea'), Js('ei'), Js('eo'), Js('eu'), Js('ia'), Js('ie'), Js('io'), Js('iu'), Js('oa'), Js('oe'), Js('oi'), Js('oo'), Js('ou'), Js('ua'), Js('ue'), Js('ui'), Js('uo'), Js('uu'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('pr'), Js('qr'), Js('sr'), Js('tr'), Js('vr'), Js('wr'), Js('yr'), Js('zr'), Js('str'), Js('bl'), Js('cl'), Js('fl'), Js('gl'), Js('kl'), Js('pl'), Js('sl'), Js('vl'), Js('yl'), Js('zl'), Js('ch'), Js('kh'), Js('ph'), Js('sh'), Js('yh'), Js('zh')]))
var.put('nm4', Js([Js('aell'), Js('aen'), Js('aerion'), Js('ahir'), Js('ahr'), Js('akir'), Js('alim'), Js('apex'), Js('aral'), Js('ard'), Js('argon'), Js('arid'), Js('arix'), Js('aron'), Js('arun'), Js('ate'), Js('atir'), Js('avi'), Js('ax'), Js('axis'), Js('earal'), Js('echos'), Js('efral'), Js('elin'), Js('elior'), Js('elnach'), Js('elno'), Js('elun'), Js('emir'), Js('enmir'), Js('enron'), Js('eod'), Js('eodar'), Js('ephix'), Js('ercis'), Js('erix'), Js('erum'), Js('examp'), Js('exor'), Js('ezran'), Js('iad'), Js('iann'), Js('ichor'), Js('icor'), Js('ikra'), Js('ilam'), Js('ilius'), Js('imbar'), Js('imm'), Js('inba'), Js('iphis'), Js('iprax'), Js('iqor'), Js('iris'), Js('irkus'), Js('itox'), Js('iwarn'), Js('ixior'), Js('ixor'), Js('izar'), Js('obax'), Js('och'), Js('odor'), Js('odum'), Js('oirik'), Js('oldar'), Js('olim'), Js('olm'), Js('oluwa'), Js('om'), Js('ophrax'), Js('oqir'), Js('ored'), Js('orion'), Js('ortex'), Js('ourax'), Js('outor'), Js('ouzran'), Js('oxir'), Js('ozran'), Js('uard'), Js('uern'), Js('uex'), Js('uhr'), Js('ul'), Js('ulim'), Js('ulkahr'), Js('uln'), Js('ulrik'), Js('umanir'), Js('uphis'), Js('uqiat'), Js('urad'), Js('utir'), Js('utron'), Js('uweth'), Js('uxir'), Js('uxron'), Js('uyar'), Js('uzrak')]))
pass
pass


# Add lib to the module scope
armyNames = var.to_python()