__all__ = ['shapeshifterNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['names1', 'tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names1', Js([Js('Angel'), Js('Fell'), Js('Anomaly'), Js('Aspect'), Js('Aura'), Js('Autumn'), Js('Banshee'), Js('Blend'), Js('Bubble'), Js('Cam (Chamelion)'), Js('Cary (Caricature)'), Js('Cat (Copycat)'), Js('Conny (Con Artist)'), Js('Copy'), Js('Daydream'), Js('Design'), Js('Ditto'), Js('Dream'), Js('Dupe'), Js('Dust'), Js('Echo'), Js('Effigy'), Js('Elle (Element)'), Js('Em (Emulate)'), Js('Enigma'), Js('Entity'), Js('Etch'), Js('Eve (Evolve)'), Js('Evo'), Js('Fable'), Js('Feign'), Js('Flow'), Js('Flux'), Js('Form'), Js('Fuse'), Js('Ghost'), Js('Harmony'), Js('Hazel'), Js('Iden (Identical)'), Js('Jen (Generate)'), Js('Kate (Duplicate)'), Js('Light'), Js('Lucy (Illusion/Hallucination)'), Js('Mai (Mime)'), Js('Mani (Manifest)'), Js('Match'), Js('Melion'), Js('Mien'), Js('Mime'), Js('Mingle'), Js('Mint'), Js('Mirage'), Js('Mirror'), Js('Mix'), Js('Nemo'), Js('Nil'), Js('Niq (Unique)'), Js('Nix'), Js('Oddity'), Js('Paradox'), Js('Parallel'), Js('Parody'), Js('Parrot'), Js('Phase'), Js('Phony'), Js('Rascal'), Js('Reflection'), Js('Repeat'), Js('Replica'), Js('Ringer'), Js('Rogue'), Js('Sam (Semblance)'), Js('Same'), Js('Scribble'), Js('Shade'), Js('Shadow'), Js('Shape'), Js('Sim (Simulate)'), Js('Sketch'), Js('Skin'), Js('Snow'), Js('Sue (Assume)'), Js('Switch'), Js('Syn (Synthesize)'), Js('Tailor'), Js('Tassy (Fantasy)'), Js('Trace'), Js('Tracy (Tracing)'), Js('Trixy'), Js('Twin'), Js('Valence (Equivalence)'), Js('Variel'), Js('Veil'), Js('Vista'), Js('Vu (Déjà Vu)'), Js('Whisper'), Js('X (Exchange)'), Js('Zero'), Js('Zip'), Js('Zot')]))
    else:
        if PyJsStrictEq(var.get('tp'),Js(2.0)):
            var.put('names1', Js([Js('Angel'), Js('Aspect'), Js('Blend'), Js('Copy'), Js('Daydream'), Js('Design'), Js('Ditto'), Js('Dream'), Js('Dupe'), Js('Dust'), Js('Echo'), Js('Effigy'), Js('Entity'), Js('Etch'), Js('Fable'), Js('Feign'), Js('Flow'), Js('Flux'), Js('Fuse'), Js('Ghost'), Js('Iden (Identical)'), Js('Light'), Js('Mani (Manifest)'), Js('Match'), Js('Melion'), Js('Mime'), Js('Mingle'), Js('Mint'), Js('Mirage'), Js('Mirror'), Js('Mix'), Js('Nemo'), Js('Nil'), Js('Niq (Unique)'), Js('Nix'), Js('Oddity'), Js('Paradox'), Js('Parallel'), Js('Parody'), Js('Parrot'), Js('Phase'), Js('Phony'), Js('Rascal'), Js('Reflection'), Js('Repeat'), Js('Replica'), Js('Ringer'), Js('Rogue'), Js('Sam (Semblance)'), Js('Same'), Js('Scribble'), Js('Shade'), Js('Shadow'), Js('Shape'), Js('Sim (Simulate)'), Js('Sketch'), Js('Skin'), Js('Snow'), Js('Switch'), Js('Syn (Synthesize)'), Js('Tailor'), Js('Trace'), Js('Twin'), Js('Valence (Equivalence)'), Js('Vista'), Js('Whisper'), Js('X (Exchange)'), Js('Zero'), Js('Zip'), Js('Zot')]))
        else:
            var.put('names1', Js([Js('Akin'), Js('Angel'), Js('Ape'), Js('Art (Artificial)'), Js('Aspect'), Js('Blend'), Js('Born'), Js('Carbon'), Js('Cipher'), Js('Clone'), Js('Copy'), Js('Counterpart'), Js('Daydream'), Js('Design'), Js('Ditto'), Js('Doppelganger'), Js('Dream'), Js('Dupe'), Js('Duplicate'), Js('Dust'), Js('Echo'), Js('Effigy'), Js('Entity'), Js('Etch'), Js('Fable'), Js('Face'), Js('Feign'), Js('Fester (Manifester)'), Js('Figment'), Js('Flow'), Js('Flux'), Js('Form'), Js('Fuse'), Js('Ghost'), Js('Guise'), Js('Guy (Guise)'), Js('Husk'), Js('Hybrid'), Js('Iden (Identical)'), Js('Imitation'), Js('Lance (Equivalence)'), Js('Light'), Js('Lou (Illusion/Hallucination)'), Js('Maestro'), Js('Mani (Manifest)'), Js('Match'), Js('Melion'), Js('Merge'), Js('Mick (Mimic)'), Js('Mime'), Js('Mingle'), Js('Mint'), Js('Mirage'), Js('Mirror'), Js('Mix'), Js('Mold'), Js('Morpheus (Morph)'), Js('Nemo'), Js('Nil'), Js('Niq (Unique)'), Js('Nix'), Js('Oddity'), Js('Paradox'), Js('Parallel'), Js('Parody'), Js('Parrot'), Js('Pat (Pattern)'), Js('Pete (Repeat)'), Js('Peter (Repeater)'), Js('Phantom'), Js('Phase'), Js('Phony'), Js('Pseudo'), Js('Range'), Js('Rascal'), Js('Reflection'), Js('Repeat'), Js('Replica'), Js('Ringer'), Js('Rogue'), Js('Romulus'), Js('Ruse'), Js('Sam (Semblance)'), Js('Same'), Js('Scar'), Js('Scribble'), Js('Shade'), Js('Shadow'), Js('Sham'), Js('Shape'), Js('Sim (Simulate)'), Js('Sketch'), Js('Skin'), Js('Snow'), Js('Specter'), Js('Sting'), Js('Stretch'), Js('Suit'), Js('Switch'), Js('Syn (Synthesize)'), Js('Tailor'), Js('Trace'), Js('Tracer'), Js('Turner'), Js('Twin'), Js('Valence (Equivalence)'), Js('Vice'), Js('Vice (Improvise)'), Js('Vista'), Js('Whisper'), Js('X (Exchange)'), Js('Zero'), Js('Zip'), Js('Zot')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('names', var.get('names1').get(var.get('rnd')))
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
shapeshifterNames = var.to_python()