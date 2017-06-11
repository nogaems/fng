__all__ = ['religionNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                if (var.get('rnd2')<Js(57.0)):
                    while (var.get('rnd3')>Js(4.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1')))+var.get('names3').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd3')))+var.get('names5').get(var.get('rnd4'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('names', ((var.get('names6').get(var.get('rnd0'))+Js(' '))+var.get('names7').get(var.get('rnd1'))))
                else:
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    if (var.get('rnd2')<Js(57.0)):
                        while (var.get('rnd3')>Js(4.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('names', ((((((var.get('names6').get(var.get('rnd5'))+Js(' of '))+var.get('names1').get(var.get('rnd0')))+var.get('names2').get(var.get('rnd1')))+var.get('names3').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd3')))+var.get('names5').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('A'), Js('Ar'), Js('Al'), Js('B'), Js('Br'), Js('Bl'), Js('C'), Js('Cr'), Js('Cl'), Js('D'), Js('Dl'), Js('Dr'), Js('E'), Js('Er'), Js('El'), Js('F'), Js('Fl'), Js('G'), Js('Gl'), Js('Gr'), Js('H'), Js('I'), Js('Il'), Js('J'), Js('K'), Js('Kl'), Js('Kr'), Js('L'), Js('M'), Js('N'), Js('O'), Js('Or'), Js('Ol'), Js('P'), Js('Pl'), Js('Ph'), Js('Pr'), Js('R'), Js('S'), Js('Sl'), Js('Str'), Js('T'), Js('Tr'), Js('U'), Js('Ur'), Js('Ul'), Js('V'), Js('Vr'), Js('W'), Js('Wr'), Js('X'), Js('Z')]))
var.put('names2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('names3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cr'), Js('cl'), Js('d'), Js('dl'), Js('dr'), Js('f'), Js('fl'), Js('g'), Js('gl'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kl'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pl'), Js('ph'), Js('pr'), Js('r'), Js('s'), Js('sl'), Js('str'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names5', Js([Js('cism'), Js('do'), Js('fis'), Js('gar'), Js('hin'), Js('khi'), Js('kyo'), Js('lly'), Js('ndo'), Js('ng'), Js('ni'), Js('nis'), Js('nity'), Js('ns'), Js('phy'), Js('qir'), Js('rity'), Js('sha'), Js('shi'), Js('sm'), Js('sni'), Js('sy'), Js('thos'), Js('thy'), Js('tism'), Js('to'), Js('ty'), Js('was'), Js('zen'), Js('zor')]))
var.put('names6', Js([Js('Healers'), Js('Wanders'), Js('Children'), Js('Angels'), Js('Chosen Ones'), Js('Oracles'), Js('Paragons'), Js('Band'), Js('Church'), Js('Communion'), Js('Congregation'), Js('Creed'), Js('Cult'), Js('Faith'), Js('Followers'), Js('Gathering'), Js('Order'), Js('Sect')]))
var.put('names7', Js([Js('of Ancestral Spirits'), Js('of the Holy Light'), Js('of Answers'), Js('of Atonement'), Js('of Awe'), Js('of Balance'), Js('of Brothers'), Js('of Clarity'), Js('of Cooperation'), Js('of Darkness'), Js('of Dawn'), Js('of Defiance'), Js('of Devotion'), Js('of Dragons'), Js('of Dreams'), Js('of Dusk'), Js('of Eternal Doom'), Js('of Eternal Rain'), Js('of Eventuality'), Js('of Fire'), Js('of Fortune'), Js('of Gold'), Js('of Harmony'), Js('of Honor'), Js('of Hope'), Js('of Humanity'), Js('of Illumination'), Js('of Insight'), Js('of Iron'), Js('of Kinship'), Js('of Light'), Js('of Luck'), Js('of Men'), Js('of Nature'), Js('of New Hope'), Js('of Order'), Js('of Origins'), Js('of Our Origins'), Js('of Parellels'), Js('of Perfection'), Js('of Piety'), Js('of Purity'), Js('of Radiance'), Js('of Redemption'), Js('of Reparations'), Js('of Revelations'), Js('of Sacrifice'), Js('of Secrets'), Js('of Shadows'), Js('of Silence'), Js('of Silver'), Js('of Steel'), Js('of Symmetry'), Js('of Sympathy'), Js('of Tranquility'), Js('of Truth'), Js('of Twilight'), Js('of Unity'), Js('of Valor'), Js('of Virtue'), Js('of Visions'), Js('of Water'), Js('of Whispers'), Js('of Women'), Js('of World Balance'), Js('of our New Lord'), Js('of the Accord'), Js('of the All Seeing Eye'), Js('of the Alpha'), Js('of the Ancestors'), Js('of the Apocalypse'), Js('of the Attuned'), Js('of the Aurora'), Js('of the Black Bear'), Js('of the Black Hand'), Js('of the Black Sign'), Js('of the Burning Crown'), Js('of the Celestials'), Js('of the Chosen'), Js('of the Clean'), Js('of the Comet'), Js('of the Conqueror'), Js('of the Crown'), Js('of the Damned'), Js('of the Divine'), Js('of the Dragon'), Js('of the Eight Divines'), Js('of the Eight Gods'), Js('of the Elements'), Js('of the Emperor'), Js('of the End'), Js('of the Enigma'), Js('of the Enlightened'), Js('of the Eye'), Js('of the False Prophet'), Js('of the Five Divines'), Js('of the Five Gods'), Js('of the Flaming Sword'), Js('of the Four Divines'), Js('of the Four Gods'), Js('of the Free'), Js('of the Glorious One'), Js('of the Illuminated'), Js('of the Innocent'), Js('of the King'), Js('of the Light'), Js('of the Martyr'), Js('of the Messiah'), Js('of the Mind'), Js('of the Moon'), Js('of the Mutants'), Js('of the New Order'), Js('of the Night'), Js('of the Nine Divines'), Js('of the Nine Gods'), Js('of the Obscure'), Js('of the Omega'), Js('of the One'), Js('of the One God'), Js('of the Oracle'), Js('of the Paragon'), Js('of the Paragons'), Js('of the Prodigy'), Js('of the Prophecy'), Js('of the Prophet'), Js('of the Rapture'), Js('of the Red Dog'), Js('of the Sacrifice'), Js('of the Sacrificed'), Js('of the Serpent'), Js('of the Seven Divines'), Js('of the Seven Gods'), Js('of the Sinless'), Js('of the Six Divines'), Js('of the Six Gods'), Js('of the Son'), Js('of the Soothsayer'), Js('of the Spirits'), Js('of the Stars'), Js('of the Studied'), Js('of the Sun'), Js('of the Three Divines'), Js('of the Three Gods'), Js('of the Titans'), Js('of the True Emperor'), Js('of the True King'), Js('of the True Prophet'), Js('of the Two Divines'), Js('of the Two Gods'), Js('of the United'), Js('of the Unsullied'), Js('of the Virgin'), Js('of the White Sign'), Js('of the White Wolf'), Js('of the Wilds'), Js('of the World')]))
pass
pass


# Add lib to the module scope
religionNames = var.to_python()