__all__ = ['vocalGroups']

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
    var.registers(['nm2', 'result'])
    var.put('nm2', Js([Js('A Bridge Too Far'), Js('A Choir'), Js('A Choired Taste'), Js('A due a due'), Js('Acapellaca'), Js('Acoustricks'), Js('Alcuna Licenza'), Js('Alcuna Matata'), Js('Alive and Singing'), Js('Allophones'), Js('Amadeus Amadeus'), Js('Amici'), Js('Amor Amore'), Js('Angel Voices'), Js('Angelicus'), Js('Anima'), Js('Anima Animals'), Js('Animatomatoes'), Js('Ascension'), Js('Audacity'), Js('Aural Fixation'), Js('Aurora'), Js('Bella Voci'), Js('Bellacapella'), Js('Bravo Bravura'), Js('Cameos'), Js('Canon The Barbarian'), Js('Celestial Voices'), Js('Change of Tone'), Js('Change of Tune'), Js('Choir Courage'), Js('Choir Generation'), Js('Choir of my Heart'), Js('Choral Beauty'), Js('Choral Life'), Js('Choral Reef'), Js('Chord on Blues'), Js('Chords of Illusion'), Js('Chorus'), Js('Classic Harmonies'), Js('Clef Hangers'), Js('Cleftomaniacs'), Js('Cloud Nine Harmonies'), Js('Colossale Colossal'), Js('Comodo Comodus'), Js('ConChords'), Js('Cordless Chords'), Js('Crescendo'), Js('Crescendoos'), Js('Crescendudes'), Js('Dawn Chorus'), Js('Decibelles'), Js('Descant Get Enough'), Js('Dolce Vita'), Js('Double Treble'), Js('Dressed to Trill'), Js('Drop the Bass'), Js('Duly Noted'), Js('Dynamic Dynamics'), Js('Echo Echo'), Js('Echo Echo Echo'), Js('Eclectic Voices'), Js('Enchorus'), Js('Encore'), Js('Encore Choir'), Js('Encore Ensemble'), Js('Ending On High Notes'), Js('Epiphony'), Js('Euphonics'), Js('Euphonism'), Js('Euphonix'), Js('Euphony'), Js('Fire Choir'), Js('Floral Chorals'), Js('Fortissimo'), Js('Found Your Voice'), Js('Full Score'), Js('Future Notes'), Js('Gathered Voices'), Js('Grace Notes'), Js('Gryphonics'), Js('Harmless Harmonies'), Js('Harmonious Harmonies'), Js('Harmonium'), Js("Heart 'n Soul"), Js('Heritage Voices'), Js('High Notes'), Js('Homophonics'), Js('Hymn and Her'), Js('Illume'), Js('Impromptu'), Js('Improvvisato'), Js('In Choir'), Js('Inspire'), Js('Interlude'), Js('Joy'), Js('Just Sing'), Js('Keytones'), Js('Lady Treble'), Js('Light My Choir'), Js('Little Lyres'), Js('Little Voices'), Js('Local Vocals'), Js('Loose Canons'), Js('Lost Sounds'), Js('Loud and Proud'), Js('Luminos'), Js('Magico Magnifico'), Js('Man Treble'), Js('Mended Chords'), Js('Messa di voce'), Js('Mouth Noise'), Js('Nothing But Treble'), Js('Octavius'), Js('On a side note'), Js('Our Voices'), Js('Out On A Hymn'), Js('Pandamonium'), Js("Phil's Harmonics"), Js('Poco a poco'), Js('Polyphones'), Js('Polyphonics'), Js('Potpourri'), Js('Prima Volta'), Js('Public Hearing'), Js('Quite a choir'), Js('Ransom Notes'), Js('Re-Choir'), Js('Reign of Choir'), Js('Rivertones'), Js('Rolling Tones'), Js('S-Choir'), Js('Saved by the Belles'), Js('Semplice'), Js('Senza Misura'), Js('Serenata'), Js('Singing About You'), Js('Siren Serenade'), Js('Sons of Pitches'), Js('Spinal Chords'), Js('Spirit Vocals'), Js('Spiritoso Spirito'), Js('Symphonies'), Js('Take Note'), Js('Take a chant'), Js('Teeny Tones'), Js('The Barbaro'), Js('The Big Chorus'), Js('The Choir Factor'), Js('The Danger Tone'), Js('The Double Dots'), Js('The Drones'), Js('The Intonations'), Js('The Singalongs'), Js('The Sound Collective'), Js('The Sound Crowd'), Js('The Tone Commandments'), Js('The Voice Collective'), Js('Timbre!'), Js('Time to Trill'), Js('Tonal Eclipse'), Js('Tone Collectors'), Js('Tone Wolves'), Js('Top Notes'), Js('Treble Rebels'), Js('Treble Tones'), Js('Treble in Paradise'), Js('Tremoloco'), Js('Trill of the Night'), Js('Triller'), Js('Trinity'), Js('Tune In'), Js('Valley Voices'), Js('Varia Zone'), Js('Variazioni'), Js('Viva Vivace'), Js('Vocal Affinity'), Js('Vocal Chords'), Js('Vocal Harmony'), Js('Vocal Movement'), Js('Voce Pienna'), Js('Voce Vita'), Js('Voice of the People'), Js('Voices In Our Head'), Js('Voicestra'), Js('Vox Anima'), Js('Vox Humana'), Js('Vox Populi'), Js('Wicked Pitch of the West'), Js('Young Voices'), Js('Prime Chorus')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', var.get('nm2').get(var.get('rnd')))
            var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
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
vocalGroups = var.to_python()