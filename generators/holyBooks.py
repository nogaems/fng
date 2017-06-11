__all__ = ['holyBooks']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm6'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'nm2', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Absolution'), Js('Angels'), Js('Answers'), Js('Ardor'), Js('Balance'), Js('Birth'), Js('Births'), Js('Blessings'), Js('Brotherhood'), Js('Cerberus'), Js('Change'), Js('Children'), Js('Clarity'), Js('Connections'), Js('Cycles'), Js('Dawn'), Js('Death'), Js('Dedication'), Js('Design'), Js('Desires'), Js('Divines'), Js('Divinity'), Js('Dominion'), Js('Duality'), Js('Dusk'), Js('Earth'), Js('Effigies'), Js('Elements'), Js('Embers'), Js('Emissaries'), Js('Epochs'), Js('Eternity'), Js('Eyes'), Js('Facts'), Js('Faith'), Js('Fate'), Js('Fealty'), Js('Fears'), Js('Felicity'), Js('Fidelity'), Js('Fire'), Js('Flames'), Js('Fury'), Js('Genesis'), Js('Glory'), Js('Gods'), Js('Grace'), Js('Guidance'), Js('Harmony'), Js('Hearts'), Js('Heaven'), Js('Heralds'), Js('Hope'), Js('Illumination'), Js('Inception'), Js('Infinity'), Js('Innocence'), Js('Integrity'), Js('Kinship'), Js('Legacies'), Js('Life'), Js('Light'), Js('Loyalty'), Js('Miracles'), Js('Moons'), Js('Morality'), Js('Nature'), Js('Passion'), Js('Perfection'), Js('Piety'), Js('Prophecies'), Js('Prophets'), Js('Prudence'), Js('Purity'), Js('Revelations'), Js('Saints'), Js('Sanction'), Js('Seraphs'), Js('Serenity'), Js('Service'), Js('Sight'), Js('Sisterhood'), Js('Souls'), Js('Spirits'), Js('Stars'), Js('Suns'), Js('Teachings'), Js('Titans'), Js('Tranquility'), Js('Truths'), Js('Valediction'), Js('Virtues'), Js('Vision'), Js('Visions'), Js('Vitality'), Js('Witnesses'), Js('Worship'), Js('Worth'), Js('Zeal'), Js('Zion'), Js('the Alpha'), Js('the Archangel'), Js('the Aspect'), Js('the Child'), Js('the Children'), Js('the Curator'), Js('the Custodian'), Js('the Cycle'), Js('the Daemon'), Js('the Divine'), Js('the Emissary'), Js('the Equilibrium'), Js('the Eye'), Js('the Father'), Js('the Heart'), Js('the Matriarch'), Js('the Mind'), Js('the Moon'), Js('the Mother'), Js('the Omega'), Js('the Oracle'), Js('the Past'), Js('the Patriarch'), Js('the Phoenix'), Js('the Rapture'), Js('the Sentinel'), Js('the Shepherd'), Js('the Sign'), Js('the Solstice'), Js('the Sun'), Js('the Truth')]))
    var.put('nm2', Js([Js('Absolution'), Js('Aeon'), Js('Affinity'), Js('Afterworld'), Js('Almighty'), Js('Alpha'), Js('Amity'), Js('Amnesty'), Js('Angelic'), Js('Apex'), Js('Ardor'), Js('Ascension'), Js('Aspect'), Js('Astral'), Js('Ataraxia'), Js('Azure'), Js('Balance'), Js('Birth'), Js('Blessed'), Js('Bloodline'), Js('Brotherhood'), Js('Celestial'), Js('Century'), Js('Cerberus'), Js('Clarity'), Js('Concord'), Js('Connection'), Js('Covenant'), Js('Crown'), Js('Curator'), Js('Custodian'), Js('Cycle'), Js('Daemon'), Js('Dawn'), Js('Descendant'), Js('Devotion'), Js('Divine'), Js('Divinity'), Js('Dominion'), Js('Duality'), Js('Effigy'), Js('Element'), Js('Elysian'), Js('Ember'), Js('Emissary'), Js('Empyrean'), Js('Epitome'), Js('Epoch'), Js('Equilibrium'), Js('Essence'), Js('Eternal'), Js('Ethereal'), Js('Evidence'), Js('Exemplary'), Js('Faith'), Js('Fate'), Js('Fealty'), Js('Felicity'), Js('Fidelity'), Js('Fire'), Js('Force'), Js('Fundamental'), Js('Generation'), Js('Genesis'), Js('Glory'), Js('Guardian'), Js('Hallowed'), Js('Harmony'), Js('Heaven'), Js('Heirloom'), Js('Herald'), Js('Heritage'), Js('Heritage'), Js('Holy'), Js('Idol'), Js('Illumination'), Js('Immortal'), Js('Inception'), Js('Infinitude'), Js('Infinity'), Js('Innocence'), Js('Integrity'), Js('Keeper'), Js('Kindred'), Js('Kingdom'), Js('Kinship'), Js('Legacy'), Js('Life'), Js('Light'), Js('Lineage'), Js('Loyalty'), Js('Lustrous'), Js('Master'), Js('Matriarch'), Js('Mercy'), Js('Messenger'), Js('Miracle'), Js('Moon'), Js('Morality'), Js('Myriad'), Js('Noble'), Js('Observance'), Js('Omega'), Js('Oracle'), Js('Paragon'), Js('Passion'), Js('Patriarch'), Js('Pedigree'), Js('Perfection'), Js('Phoenix'), Js('Piety'), Js('Pinnacle'), Js('Pious'), Js('Power'), Js('Prime'), Js('Prodigy'), Js('Prophecy'), Js('Prophet'), Js('Prudence'), Js('Pure'), Js('Purity'), Js('Rapture'), Js('Realm'), Js('Revelation'), Js('Revered'), Js('Reverent'), Js('Righteous'), Js('Sacred'), Js('Saintly'), Js('Sanctified'), Js('Sanctity'), Js('Sentinel'), Js('Seraph'), Js('Serenity'), Js('Service'), Js('Shepherd'), Js('Sign'), Js('Sinless'), Js('Sisterhood'), Js('Solemn'), Js('Solstice'), Js('Soul'), Js('Spire'), Js('Spirit'), Js('Sun'), Js('Titan'), Js('Totem'), Js('Tranquility'), Js('Truth'), Js('Unity'), Js('Utopia'), Js('Venerable'), Js('Vertex'), Js('Virtue'), Js('Vision'), Js('Vitality'), Js('Witness'), Js('Worship'), Js('Worthy'), Js('Zeal'), Js('Zenith'), Js('Zion')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if (var.get('i')<Js(3.0)):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm3').get(var.get('rnd')))+Js(' of '))+var.get('nm1').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd2'), Js(1.0))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((Js('The ')+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd'))))
                    var.get('nm1').callprop('splice', var.get('rnd2'), Js(1.0))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('names', ((((((Js('The ')+var.get('nm1').get(var.get('rnd2')))+Js(' of '))+var.get('nm4').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm8').get(var.get('rnd6'))))
                        var.get('nm1').callprop('splice', var.get('rnd2'), Js(1.0))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('names', ((((((Js('The ')+var.get('nm3').get(var.get('rnd')))+Js(' of '))+var.get('nm4').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6'))))
                        var.get('nm1').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm3', Js([Js('Book'), Js('Books'), Js('Scroll'), Js('Scrolls'), Js('Testament'), Js('Testaments'), Js('Codex'), Js('Codices'), Js('Chronicle'), Js('Chronicles'), Js('Tome'), Js('Tomes'), Js('Word'), Js('Words')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('y')]))
var.put('nm6', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm7', Js([Js('agi'), Js('aldir'), Js('aos'), Js('arus'), Js('borh'), Js('bris'), Js('bum'), Js('bus'), Js('dall'), Js('dar'), Js('darr'), Js('des'), Js('dis'), Js('dite'), Js('dohr'), Js('don'), Js('dos'), Js('dros'), Js('dum'), Js('dur'), Js('emis'), Js('enar'), Js('esis'), Js('eus'), Js('eyar'), Js('eyr'), Js('her'), Js('ion'), Js('ione'), Js('ius'), Js('jun'), Js('ldir'), Js('lios'), Js('lo'), Js('lous'), Js('mes'), Js('mir'), Js('mjir'), Js('mos'), Js('mus'), Js('nia'), Js('nir'), Js('nos'), Js('nus'), Js('ohr'), Js('orr'), Js('rasil'), Js('reus'), Js('ros'), Js('ruer'), Js('rus'), Js('ses'), Js('stus'), Js('tar'), Js('tarr'), Js('teus'), Js('thar'), Js('ther'), Js('tia'), Js('ton'), Js('tos'), Js('tyx'), Js('ysus')]))
var.put('nm8', Js([Js('ra'), Js('ara'), Js('ella'), Js('elia'), Js('nja'), Js('yja'), Js('ulla'), Js('la'), Js('na'), Js('ana'), Js('neas'), Js('phine'), Js('tris'), Js('gyn'), Js('syn'), Js('dite'), Js('ena'), Js('hena'), Js('tia'), Js('anke'), Js('mera'), Js('nera'), Js('soi'), Js('heia'), Js('mis'), Js('thys'), Js('asis'), Js('one'), Js('dione'), Js('dona'), Js('ona'), Js('phion'), Js('trix'), Js('tix'), Js('lene'), Js('lena'), Js('phy'), Js('tune'), Js('va'), Js('una'), Js('tuna'), Js('arae'), Js('aris'), Js('ris'), Js('tia'), Js('rena'), Js('raura'), Js('dea'), Js('enta'), Js('dia'), Js('ta')]))
pass
pass


# Add lib to the module scope
holyBooks = var.to_python()