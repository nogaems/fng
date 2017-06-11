__all__ = ['softwareNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'result'])
    var.put('nm1', Js([Js('Abra'), Js('Ace'), Js('Aer'), Js('Agent'), Js('Ample'), Js('Ape'), Js('Asap'), Js('Ash'), Js('Aspect'), Js('Asset'), Js('Aura'), Js('Aurora'), Js('Beacon'), Js('Beat'), Js('Bindle'), Js('Blithe'), Js('Blossom'), Js('Boop'), Js('Borealis'), Js('Bundle'), Js('Cell'), Js('Chant'), Js('Chasm'), Js('Chime'), Js('Cinch'), Js('Cloud'), Js('Clout'), Js('Cluster'), Js('Clutch'), Js('Cobolt'), Js('Combi'), Js('Core'), Js('Cozy'), Js('Crux'), Js('Curator'), Js('Cure'), Js('Curio'), Js('Curious'), Js('Dawn'), Js('Digi'), Js('Ditto'), Js('Ditty'), Js('Divi'), Js('Djinni'), Js('Dodge'), Js('Domino'), Js('Dozer'), Js('Dragoon'), Js('Drake'), Js('Echo'), Js('Effigy'), Js('Efflux'), Js('Ego'), Js('Elementary'), Js('Ellipse'), Js('Ember'), Js('Emblem'), Js('Entity'), Js('Ether'), Js('Ex.'), Js('Fig'), Js('Flare'), Js('Fleet'), Js('Flex'), Js('Flix'), Js('Float'), Js('Flow'), Js('Fluo'), Js('Fuse'), Js('Galore'), Js('GameOn'), Js('Gem'), Js('Geode'), Js('Gig'), Js('Gist'), Js('Glint'), Js('Gloss'), Js('Glow'), Js('Groove'), Js('Guise'), Js('Hellion'), Js('Hex'), Js('Hiero'), Js('Hustle'), Js('Ideo'), Js('ImAge'), Js('Imp'), Js('Imput'), Js('Influx'), Js('Iris'), Js('Jade'), Js('Jewel'), Js('Jinx'), Js('Jive'), Js('Kazam'), Js('Knock'), Js('Lax'), Js('Limbo'), Js('Lithe'), Js('Lode'), Js('Lumos'), Js('Lure'), Js('Melody'), Js('Mic'), Js('Mime'), Js('Mini'), Js('Minmax'), Js('Mirage'), Js('Mirror'), Js('Mist'), Js('Mix'), Js('Mobius'), Js('Moxie'), Js('Mumbo'), Js('Myth'), Js('Neo'), Js('Neon'), Js('Nimbus'), Js('Notch'), Js('Obsidian'), Js('Oculus'), Js('Odd'), Js('Ode'), Js('Onyx'), Js('Opt'), Js('Optic'), Js('Oracle'), Js('Orbit'), Js('Paltry'), Js('Para'), Js('Paragon'), Js('Parcel'), Js('Parry'), Js('Particle'), Js('Patter'), Js('Petal'), Js('Pickle'), Js('Picnic'), Js('Picolo'), Js('Pinnacle'), Js('Pitch'), Js('Pivot'), Js('Pose'), Js('Precious'), Js('Prism'), Js('Pronto'), Js('Prospect'), Js('Pulse'), Js('Query'), Js('Rascal'), Js('Rebus'), Js('Reflect'), Js('Reverb'), Js('Ripple'), Js('Rune'), Js('Rush'), Js('Sabre'), Js('Sapphire'), Js('Scale'), Js('Scoop'), Js('Segue'), Js('Semble'), Js('Shift'), Js('Slang'), Js('Slice'), Js('Slick'), Js('Sliver'), Js('Smooth'), Js('Snap'), Js('Soar'), Js('Sonic'), Js('Spark'), Js('Sparkle'), Js('Speckle'), Js('Sphinx'), Js('Spirit'), Js('Splice'), Js('Strut'), Js('Tiger'), Js('Tremor'), Js('Tri'), Js('Triad'), Js('Trifle'), Js('Trinity'), Js('Trix'), Js('Tru'), Js('Tune'), Js('Twist'), Js('Vertex'), Js('Vibe'), Js('Vim'), Js('Virtue'), Js('Visage'), Js('Vitae'), Js('Vitality'), Js('Vortex'), Js('Voyage'), Js('Wave'), Js('Wiz'), Js('Zest')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(' Advanced'), Js(' Base'), Js(' Basic'), Js(' Engine'), Js(' Language'), Js(' Pro'), Js(' Script'), Js(' System'), Js('#'), Js('+'), Js('++'), Js('-2'), Js('-3'), Js('Base'), Js('Code'), Js('Edge'), Js('Pro'), Js('Script'), Js('X')]))
pass
pass


# Add lib to the module scope
softwareNames = var.to_python()