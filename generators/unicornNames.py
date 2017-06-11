__all__ = ['unicornNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', var.get('nm3').get(var.get('rnd')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aeolus'), Js('Ainsel'), Js('Aiolos'), Js('Albion'), Js('Alewar'), Js('Amyntas'), Js('Anor'), Js('Argus'), Js('Argyros'), Js('Arion'), Js('Aron'), Js('Arryn'), Js('Auris'), Js('Baine'), Js('Bastion'), Js('Blythe'), Js('Boaz'), Js('Brand'), Js('Cadillac'), Js('Calimerio'), Js('Calimero'), Js('Chant'), Js('Chanted'), Js('Chipper'), Js('Colbolt'), Js('Corin'), Js('Craze'), Js('Dashing'), Js('Demetrius'), Js('Dryade'), Js('Elgar'), Js('Elmas'), Js('Elwyn'), Js('Eos'), Js('Erwin'), Js('Estar'), Js('Euros'), Js('Fernaco'), Js('Garvin'), Js('Giddy'), Js('Gil'), Js('Giulio'), Js('Grace'), Js('Grant'), Js('Gwayne'), Js('Gwyn'), Js('Happy'), Js('Hart'), Js('Helios'), Js('Hesperos'), Js('Iris'), Js('Izar'), Js('Jada'), Js('Jaden'), Js('Jasper'), Js('Jolly'), Js('Joshi'), Js('Julius'), Js('Kaisa'), Js('Kimber'), Js('Knight'), Js('Lance'), Js('Lancelot'), Js('Lanstrom'), Js('Linus'), Js('Lothir'), Js('Majesty'), Js('Marcello'), Js('Marjallo'), Js('Matia'), Js('Mawu'), Js('Meara'), Js('Merry'), Js('Midnight'), Js('Mika'), Js('Milky Way'), Js('Monterya'), Js('Moriba'), Js('Mortus'), Js('Mystery'), Js('Mystic'), Js('Nestor'), Js('Nightwind'), Js('Olwen'), Js('Olwin'), Js('Ozzy'), Js('Perky'), Js('Phaeton'), Js('Placido'), Js('Poseidon'), Js('Prancer'), Js('Rainbow'), Js('Robin'), Js('Roshan'), Js('Rune'), Js('Sable'), Js('Sapphire'), Js('Sigil'), Js('Silly'), Js('Silvesse'), Js('Silvester'), Js('Sly'), Js('Snow'), Js('Snowflake'), Js('Solstice'), Js('Sparkles'), Js('Starburst'), Js('Stardust'), Js('Sterling'), Js('Sunny'), Js('Sunshine'), Js('Titanius'), Js('Tomo'), Js('Tryne'), Js('Twilight'), Js('Twinkle'), Js('Unity'), Js('Virgil'), Js('Wilbur'), Js('Willow'), Js('Wrynn'), Js('Wynn'), Js('Wynstar'), Js('Xavier'), Js('Zane'), Js('Zion')]))
var.put('nm2', Js([Js('Aalona'), Js('Acorna'), Js('Adiana'), Js('Aerowen'), Js('Agaloa'), Js('Aglaea'), Js('Ainsel'), Js('Alairia'), Js('Alanala'), Js('Albany'), Js('Aletha'), Js('Alice'), Js('Alize'), Js('Allena'), Js('Alona'), Js('Amandaria'), Js('Amara'), Js('Andra'), Js('Angelina'), Js('Annamika'), Js('Arryn'), Js('Astra'), Js('Aura'), Js('Aurae'), Js('Auris'), Js('Aurora'), Js('Baine'), Js('Bellini'), Js('Benicia'), Js('Bennettia'), Js('Biancha'), Js('Blissia'), Js('Bonita'), Js('Brandi'), Js('Breanna'), Js('Breena'), Js('Bryanne'), Js('Bubbles'), Js('Candice'), Js('Carna'), Js('Cassiopeia'), Js('Celeste'), Js('Celestia'), Js('Celina'), Js('Chant'), Js('Chanted'), Js('Chipper'), Js('Cindi'), Js('Claire'), Js('Clare'), Js('Clementine'), Js('Cortesia'), Js('Crystal'), Js('Daisy'), Js('Danika'), Js('Daphne'), Js('Della'), Js('Denali'), Js('Dessa'), Js('Deva'), Js('Drisana'), Js('Dulcea'), Js('Duscha'), Js('Electra'), Js('Elen'), Js('Elita'), Js('Elmas'), Js('Eluna'), Js('Elune'), Js('Elwyn'), Js('Emerald'), Js('Enigma'), Js('Eos'), Js('Eowyn'), Js('Epona'), Js('Estar'), Js('Estrellita'), Js('Etana'), Js('Eternia'), Js('Euros'), Js('Evania'), Js('Fae'), Js('Faith'), Js('Faye'), Js('Felicia'), Js('Fenella'), Js('Fenna'), Js('Fiona'), Js('Fleta'), Js('Floriana'), Js('Gerda'), Js('Giddy'), Js('Gil'), Js('Glamor'), Js('Grace'), Js('Gratiana'), Js('Grizelda'), Js('Gwyn'), Js('Gwynth'), Js('Happy'), Js('Hope'), Js('Hyacinthie'), Js('Hylzarie'), Js('Inara'), Js('Ira'), Js('Irene'), Js('Iris'), Js('Jada'), Js('Jade'), Js('Jaden'), Js('Javiera'), Js('Jewel'), Js('Jolly'), Js('Kaisa'), Js('Kenzie'), Js('Kimber'), Js('Langaria'), Js('Laqueta '), Js('Larissa'), Js('Leila'), Js('Lily'), Js('Lotus'), Js('Luna'), Js('Lunaria'), Js('Lunette'), Js('Mae'), Js('Majesty'), Js('Marya'), Js('Matia'), Js('Mawu'), Js('Meara'), Js('Merry'), Js('Midnight'), Js('Mika'), Js('Milky Way'), Js('Mona'), Js('Monterya'), Js('Moriba'), Js('Mystery'), Js('Mystic'), Js('Mystique'), Js('Nadira'), Js('Necia'), Js('Nightwind'), Js('Nola'), Js('Opal'), Js('Oracle'), Js('Orielle'), Js('Pearl'), Js('Perky'), Js('Primara'), Js('Rainbow'), Js('Robin'), Js('Roshan'), Js('Ruby'), Js('Rune'), Js('Sable'), Js('Samantha'), Js('Sapphire'), Js('Sassy'), Js('Selena'), Js('Serenity'), Js('Shakti'), Js('Shanna'), Js('Sigil'), Js('Silly'), Js('Silvesse'), Js('Simona'), Js('Snow'), Js('Snowflake'), Js('Solstice'), Js('Sparkles'), Js('Speranza'), Js('Starburst'), Js('Stardust'), Js('Sterling'), Js('Sugar'), Js('Suki'), Js('Sunny'), Js('Sunshine'), Js('Sylvie'), Js('Tacita'), Js('Tama'), Js('Tara'), Js('Trixie'), Js('Tryne'), Js('Twilight'), Js('Twinkle'), Js('Unity'), Js('Valeria'), Js('Wilda'), Js('Willow'), Js('Wynn'), Js('Xaveria'), Js('Xenia'), Js('Yashiana'), Js('Yasmin'), Js('Yennaria'), Js('Yoriara'), Js('Yvonne'), Js('Zane'), Js('Zara')]))
var.put('nm3', Js([Js('Ainsel'), Js('Arryn'), Js('Auris'), Js('Baine'), Js('Chant'), Js('Chanted'), Js('Chipper'), Js('Elmas'), Js('Elwyn'), Js('Eos'), Js('Estar'), Js('Euros'), Js('Giddy'), Js('Gil'), Js('Grace'), Js('Gwyn'), Js('Happy'), Js('Iris'), Js('Jada'), Js('Jaden'), Js('Jolly'), Js('Kaisa'), Js('Kimber'), Js('Majesty'), Js('Matia'), Js('Mawu'), Js('Meara'), Js('Merry'), Js('Midnight'), Js('Mika'), Js('Milky Way'), Js('Monterya'), Js('Moriba'), Js('Mystery'), Js('Mystic'), Js('Nightwind'), Js('Perky'), Js('Rainbow'), Js('Robin'), Js('Roshan'), Js('Rune'), Js('Sable'), Js('Sapphire'), Js('Sigil'), Js('Silly'), Js('Silvesse'), Js('Snow'), Js('Snowflake'), Js('Solstice'), Js('Sparkles'), Js('Starburst'), Js('Stardust'), Js('Sterling'), Js('Sunny'), Js('Sunshine'), Js('Tryne'), Js('Twilight'), Js('Twinkle'), Js('Unity'), Js('Willow'), Js('Wynn'), Js('Zane')]))
pass
pass


# Add lib to the module scope
unicornNames = var.to_python()