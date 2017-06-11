__all__ = ['mageTowerNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen', 'nm4', 'nm5', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'result'])
    var.put('nm1', Js([Js('Aberrant'), Js('Alluring'), Js('Ambition'), Js('Anchored'), Js('Ancient'), Js('Apparatus'), Js('Arcane'), Js('Arch'), Js('Aromatic'), Js('Austere'), Js('Banished'), Js('Bizarre'), Js('Blind'), Js('Bone'), Js('Breathing'), Js('Brilliant'), Js('Burrowing'), Js('Cackling'), Js('Canvas'), Js('Catalyst'), Js('Chained'), Js('Changing'), Js('Chaos'), Js('Clarity'), Js('Cloud'), Js('Command'), Js('Corrupting'), Js('Coursing'), Js('Crackling'), Js('Crazed'), Js('Creeping'), Js('Crumbling'), Js('Curious'), Js('Cycle'), Js('Dangling'), Js('Dark'), Js('Dead'), Js('Death'), Js('Deception'), Js('Defiant'), Js('Delirious'), Js('Demon'), Js('Demonic'), Js('Devil'), Js('Dimension'), Js('Discovery'), Js('Dream'), Js('Dreamscape'), Js('Drunk'), Js('Dynamic'), Js('Elementary'), Js('Enchanted'), Js('Enhancement'), Js('Enigma'), Js('Enlightened'), Js('Eternal'), Js('Eternity'), Js('Ethereal'), Js('Expanding'), Js('Experiment'), Js('Experimental'), Js('Exploration'), Js('Fading'), Js('Fairy'), Js('False'), Js('Feedback'), Js('Flickering'), Js('Floating'), Js('Flowing'), Js('Fluke'), Js('Fragrant'), Js('Friction'), Js('Frozen'), Js('Galaxy'), Js('Grand'), Js('Growing'), Js('Hallucination'), Js('Hanging'), Js('Hexed'), Js('Hocus'), Js('Ice'), Js('Icicle'), Js('Impulse'), Js('Infernal'), Js('Infinite'), Js('Infinity'), Js('Inked'), Js('Invention'), Js('Inverted'), Js('Invisible'), Js('Juvenile'), Js('Knowledge'), Js('Laughing'), Js('Lightning'), Js('Living'), Js('Lone'), Js('Lonely'), Js('Mad'), Js('Makeshift'), Js('Marble'), Js('Masked'), Js('Midnight'), Js('Migrating'), Js('Mind'), Js('Mirror'), Js('Morphing'), Js('Moving'), Js('Mumbling'), Js('Mysterious'), Js('Mystery'), Js('Night'), Js('Nocturnal'), Js('Novice'), Js('Obedient'), Js('Observant'), Js('Observing'), Js('Omen'), Js('Oracle'), Js('Parallel'), Js('Particle'), Js('Perpetual'), Js('Phase'), Js('Phased'), Js('Planar'), Js('Plane'), Js('Playful'), Js('Possessed'), Js('Prodigy'), Js('Prophecy'), Js('Pulse'), Js('Pulsing'), Js('Radiant'), Js('Riddle'), Js('Scented'), Js('Sentient'), Js('Servant'), Js('Serving'), Js('Shifting'), Js('Silent'), Js('Skeletal'), Js('Sleeping'), Js('Slumbering'), Js('Smiling'), Js('Smoking'), Js('Smoldering'), Js('Sparking'), Js('Sparkling'), Js('Spell'), Js('Spellbound'), Js('Surprise'), Js('Talking'), Js('Temporal'), Js('Thunder'), Js('Timeless'), Js('Tired'), Js('Toppling'), Js('Tranquil'), Js('Traveling'), Js('Turning'), Js('Vanishing'), Js('Veiled'), Js('Vessel'), Js('Volatile'), Js('Wandering'), Js('Warped'), Js('Watching'), Js('Whispering'), Js('Wicked'), Js('Wild'), Js('Winged'), Js('Wisdom')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('rnd')>Js(4.0)):
                    while (var.get('rnd3')<Js(5.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('Tower'), Js('Spire'), Js('Lookout'), Js('Pillar'), Js('Obelisk'), Js('Tower'), Js('Tower'), Js('Tower')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('cr'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('kn'), Js('p'), Js('pr'), Js('q'), Js('qr'), Js('r'), Js('st'), Js('str'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a')]))
var.put('nm6', Js([Js('bahn'), Js('barin'), Js('baris'), Js('belle'), Js('beus'), Js('bin'), Js('bine'), Js('bus'), Js('dalf'), Js('dali'), Js('deis'), Js('del'), Js('delis'), Js('disum'), Js('dium'), Js('dore'), Js('dores'), Js('dus'), Js('faeh'), Js('farihm'), Js('faris'), Js('fea'), Js('feus'), Js('flyn'), Js('fora'), Js('forn'), Js('fyne'), Js('gaell'), Js('garis'), Js('gast'), Js('geor'), Js('georis'), Js('gis'), Js('gorim'), Js('grith'), Js('groln'), Js('grur'), Js('haen'), Js('hagan'), Js('harad'), Js('haris'), Js('harise'), Js('harith'), Js('hione'), Js('hith'), Js('hone'), Js('jahr'), Js('jamar'), Js('jeik'), Js('jelle'), Js('jes'), Js('jest'), Js('jiane'), Js('jior'), Js('jor'), Js('jyll'), Js('kalis'), Js('kealis'), Js('kely'), Js('key'), Js('kius'), Js('kon'), Js('kora'), Js('kore'), Js('kron'), Js('laes'), Js('leas'), Js('lenor'), Js('leus'), Js('lin'), Js('lius'), Js('lore'), Js('lune'), Js('lyn'), Js('maev'), Js('maex'), Js('mari'), Js('marim'), Js('mazz'), Js('meazz'), Js('monar'), Js('monora'), Js('morith'), Js('morn'), Js('naxix'), Js('naxx'), Js('neas'), Js('neus'), Js('nilor'), Js('nior'), Js('nirn'), Js('nitor'), Js('nora'), Js('norim'), Js('paen'), Js('pan'), Js('phi'), Js('phior'), Js('pianne'), Js('pius'), Js('pniar'), Js('prix'), Js('prixys'), Js('pyx'), Js('qian'), Js('qille'), Js('qiohn'), Js('qiohr'), Js('qium'), Js('qix'), Js('qor'), Js('qora'), Js('qrax'), Js('quam'), Js('ras'), Js('rhan'), Js('rihan'), Js('ris'), Js('rius'), Js('ro'), Js('ronin'), Js('rune'), Js('saem'), Js('shan'), Js('sim'), Js('sinor'), Js('sior'), Js('soph'), Js('sorin'), Js('strea'), Js('strum'), Js('taris'), Js('tarum'), Js('taz'), Js('thal'), Js('thar'), Js('tior'), Js('tosh'), Js('trix'), Js('vae'), Js('veus'), Js('via'), Js('viar'), Js('vior'), Js('vira'), Js('vius'), Js('vras'), Js('vys'), Js('waelle'), Js('wahl'), Js('weahl'), Js('wix'), Js('wras'), Js('wrick'), Js('wrys'), Js('wyn'), Js('xarif'), Js('xaryl'), Js('xea'), Js('xeor'), Js('xis'), Js('xium'), Js('xius'), Js('xon'), Js('xone'), Js('xyll'), Js('ydae'), Js('ydor'), Js('yeas'), Js('yna'), Js('ynas'), Js('yora'), Js('yorn'), Js('yrin'), Js('yus'), Js('zahn'), Js('zahr'), Js('zax'), Js('zif'), Js('zohr'), Js('zohra'), Js('zor'), Js('zora'), Js('zyxi')]))
pass
pass


# Add lib to the module scope
mageTowerNames = var.to_python()