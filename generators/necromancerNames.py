__all__ = ['necromancerNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['namesNeutral', 'nameGen', 'namesFemale', 'names5', 'names2', 'names3', 'names1', 'namesMale'])
@Js
def PyJsHoisted_nameGen_(namesFirst, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'namesFirst':namesFirst}, var)
    var.registers(['names4', 'result', 'namesFirst'])
    var.put('names4', var.get('namesFirst'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
            var.put('names', (((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names4').get(var.get('rnd4')))+Js('  '))+var.get('names5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('namesFemale', Js([Js('bea'), Js('betha'), Js('brix'), Js('cia'), Js('cilia'), Js('dira'), Js('dita'), Js('gami'), Js('ghana'), Js('grid'), Js('hilde'), Js('len'), Js('lian'), Js('lya'), Js('mira'), Js('mish'), Js('mona'), Js('mura'), Js('ness'), Js('peste'), Js('pris'), Js('reas'), Js('reda'), Js('ren'), Js('ress'), Js('rina'), Js('ris'), Js('roti'), Js('rotia'), Js('selm'), Js('sin'), Js('tulah'), Js('vana'), Js('vash'), Js('ven'), Js('verra'), Js('viah'), Js('vris'), Js('xaura'), Js('zaen')]))
var.put('namesMale', Js([Js('brum'), Js('cular'), Js('dan'), Js('dhur'), Js('dulus'), Js('dum'), Js('gan'), Js('ghor'), Js('grim'), Js('kai'), Js('kar'), Js('khar'), Js('kras'), Js('lak'), Js('lazar'), Js('lekai'), Js('los'), Js('mien'), Js('mon'), Js('pent'), Js('qir'), Js('qur'), Js('rael'), Js('rius'), Js('row'), Js('thik'), Js('thum'), Js('tic'), Js('vok'), Js('vras'), Js('xir'), Js('xius'), Js('xor'), Js('zad'), Js('zar'), Js('zhar'), Js('zhul'), Js('zis'), Js('zius'), Js('zor')]))
var.put('namesNeutral', Js([Js('baem'), Js('bres'), Js('brix'), Js('cix'), Js('crux'), Js('dhir'), Js('dhos'), Js('drem'), Js('drex'), Js('drim'), Js('ghrin'), Js('laer'), Js('leki'), Js('mek'), Js('min'), Js('mirn'), Js('morn'), Js('nirn'), Js('noth'), Js('nus'), Js('peth'), Js('prix'), Js('qis'), Js('qrax'), Js('shis'), Js('thas'), Js('thes'), Js('thir'), Js('tos'), Js('war'), Js('with'), Js('wix'), Js('xas'), Js('xhin'), Js('xiem'), Js('xis'), Js('xith'), Js('yor'), Js('zael'), Js('zis')]))
var.put('names1', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names2', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('pr'), Js('str'), Js('vr'), Js('wr'), Js('zr'), Js('st'), Js('ch'), Js('chr'), Js('sh')]))
var.put('names3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ou'), Js('au'), Js('ei'), Js('io'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e')]))
var.put('names5', Js([Js('Alure'), Js('Anatomy'), Js('Ashes'), Js('Bane'), Js('Black'), Js('Blackhand'), Js('Blight'), Js('Bloodworth'), Js('Bonecall'), Js('Calamity'), Js('Carnage'), Js('Craft'), Js('Crane'), Js('Crow'), Js('Cruor'), Js('Daemonne'), Js('Deathbloom'), Js('Deathhand'), Js('Deathwhisper'), Js('Deville'), Js('Diction'), Js('Doomweaver'), Js('Doomwhisper'), Js('Dreadmore'), Js('Fester'), Js('Gloom'), Js('Graeme'), Js('Gravemore'), Js('Graves'), Js('Grimm'), Js('Haggard'), Js('Hex'), Js('Incarnate'), Js('Kane'), Js('Livid'), Js('Magnus'), Js('Malefic'), Js('Maleficum'), Js('Malicius'), Js('Mallus'), Js('Metus'), Js('Mildew'), Js('Molder'), Js('Morbide'), Js('Morte'), Js('Mortice'), Js('Naxxremis'), Js('Necrosyse'), Js('Nightfall'), Js('Nightshade'), Js('Nyte'), Js('Onyx'), Js('Payne'), Js('Plasma'), Js('Putrescence'), Js('Rane'), Js('Rotheart'), Js('Sanguine'), Js('Sanguis'), Js('Shade'), Js('Shadowend'), Js('Siphon'), Js('Solace'), Js('Umbra'), Js('Vacuity'), Js('Void'), Js('Whisper'), Js('the Abominable'), Js('the Abomination'), Js('the Adept'), Js('the Analyzer'), Js('the Animated'), Js('the Animator'), Js('the Beast'), Js('the Black'), Js('the Blight'), Js('the Carver'), Js('the Constructed'), Js('the Constructor'), Js('the Corpse'), Js('the Corpsemaker'), Js('the Corrupted'), Js('the Corruptor'), Js('the Couldronmaster'), Js('the Crippled'), Js('the Curropted'), Js('the Darkheart'), Js('the Darkmaster'), Js('the Doctor'), Js('the De-Composer'), Js('the Decayer'), Js('the Decomposer'), Js('the Decrepit'), Js('the Defiler'), Js('the Demise'), Js('the Demon'), Js('the Desecrator'), Js('the Dissector'), Js('the Eradicator'), Js('the Eternal'), Js('the Examiner'), Js('the Experi-Mentor'), Js('the Experiment'), Js('the Extinguisher'), Js('the Feeble'), Js('the Fleshrender'), Js('the Gorish'), Js('the Haggard'), Js('the Hallowed'), Js('the Harvester'), Js('the Hollow'), Js('the Immortal'), Js('the Inquisitor'), Js('the Insane'), Js('the Living'), Js('the Mad'), Js('the Maggot'), Js('the Manifested'), Js('the Mute'), Js('the Necro'), Js('the Necromancer'), Js('the Nightmare'), Js('the Paranoid'), Js('the Plaguebringer'), Js('the Plaguemaster'), Js('the Putrid'), Js('the Raised'), Js('the Reanimator'), Js('the Reaper'), Js('the Renewer'), Js('the Renovator'), Js('the Resurrector'), Js('the Reviver'), Js('the Risen'), Js('the Rotting'), Js('the Serpent'), Js('the Soulkeeper'), Js('the Soulreaper'), Js('the Surgeon'), Js('the Tyrant'), Js('the Undead'), Js('the Undertaker'), Js('the Unliving'), Js('the Vivisector'), Js('the Wraith')]))
pass
pass


# Add lib to the module scope
necromancerNames = var.to_python()