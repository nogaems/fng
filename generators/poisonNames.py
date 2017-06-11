__all__ = ['poisonNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nmb', 'nmd', 'nmc', 'nameGen', 'nma'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm2', 'nm3', 'result'])
    var.put('nm1', Js([Js('Abyss'), Js('Agony'), Js('Alpha'), Js('Anarchy'), Js("Angel's"), Js('Angelic'), Js('Baleful'), Js('Banshee'), Js('Basilisk'), Js('Belch'), Js('Belching'), Js('Berserker'), Js('Bitter'), Js('Bleak'), Js('Bleeding'), Js('Blind'), Js('Blinded'), Js('Blistering'), Js('Bloat'), Js('Bloating'), Js('Bold'), Js('Brain'), Js('Burning'), Js('Chaos'), Js('Cherub'), Js("Child's"), Js('Chimera'), Js('Cipher'), Js('Cold'), Js('Crimson'), Js('Crying'), Js('Crystal'), Js('Cursed'), Js('Cyst'), Js('Daemon'), Js('Dark'), Js('Daydream'), Js("Death's"), Js('Demonic'), Js("Devil's"), Js('Dire'), Js('Divine'), Js('Doom'), Js('Dragon'), Js('Drake'), Js('Dream'), Js('Dull'), Js('Dying'), Js('Ebon'), Js('Eerie'), Js('Entropy'), Js('Eternal'), Js('Ethereal'), Js('Execution'), Js('Fading'), Js('Fatal'), Js('Fey'), Js('Fiendish'), Js('Fiery'), Js('Final'), Js('Fire'), Js('Flame'), Js('Forbidden'), Js('Forlorn'), Js('Frost'), Js('Frozen'), Js('Fury'), Js('Futile'), Js('Gal'), Js('Ghost'), Js('Gloom'), Js('Goblin'), Js('Grave'), Js('Grim'), Js("Hag's"), Js('Hellish'), Js('Hemorrhage'), Js('Hopeless'), Js('Humming'), Js('Hyper'), Js('Immortal'), Js('Impossible'), Js('Incurable'), Js('Infernal'), Js('Ire'), Js('Ivory'), Js('Jester'), Js('Killing'), Js('Last'), Js('Leeching'), Js('Livid'), Js('Lost'), Js("Lover's"), Js('Luminous'), Js('Malefic'), Js('Manic'), Js('Medusa'), Js('Meta'), Js('Monster'), Js('Mortal'), Js('Moss'), Js('Necron'), Js('Necrotic'), Js('Nether'), Js('Neutral'), Js('Night'), Js('Nightmare'), Js('Nimble'), Js('Numbing'), Js('Obsidian'), Js('Ogre'), Js('Onyx'), Js('Pandemonium'), Js('Passion'), Js('Peace'), Js('Phantom'), Js('Plague'), Js('Pygmy'), Js('Quivering'), Js('Radiant'), Js('Rage'), Js('Rapid'), Js('Reaper'), Js('Sanguine'), Js('Savage'), Js('Scourged'), Js('Serpent'), Js('Shade'), Js('Shadow'), Js('Sharp'), Js('Shrew'), Js('Shriveling'), Js('Shrouded'), Js('Silent'), Js('Silver'), Js('Sinister'), Js('Skull'), Js('Slag'), Js('Sleeping'), Js('Smile'), Js('Smiling'), Js('Soulless'), Js('Specter'), Js('Spewing'), Js('Spider'), Js("Sprite's"), Js('Stiff'), Js('Strangler'), Js('Strangling'), Js("Summer's"), Js('Swelling'), Js('Symbiotic'), Js('Tainted'), Js('Terminal'), Js('Tomb'), Js('Torment'), Js('Torture'), Js('Trembling'), Js('Twilight'), Js('Unseen'), Js('Veiled'), Js('Vicious'), Js('Vile'), Js('Violet'), Js('Vision'), Js('Vivid'), Js('Void'), Js('Vortex'), Js('Weeping'), Js('Wicked'), Js("Winter's"), Js("Witch's"), Js('Wither'), Js('Woeful'), Js('Wraith')]))
    var.put('nm2', Js([Js('Bane'), Js('Blade'), Js('Blight'), Js('Caress'), Js('Clutch'), Js('Compound'), Js('Dust'), Js('Embrace'), Js('Flower'), Js('Fungus'), Js('Itch'), Js('Gas'), Js('Grasp'), Js('Growth'), Js('Grudge'), Js('Kiss'), Js('Leaf'), Js('Lock'), Js('Malice'), Js('Mist'), Js('Mutagen'), Js('Petal'), Js('Poison'), Js('Powder'), Js('Rancor'), Js('Scale'), Js('Scratch'), Js('Seed'), Js('Smile'), Js('Smoke'), Js('Spine'), Js('Spite'), Js('Spore'), Js('Spray'), Js('Stalk'), Js('Taint'), Js('Taste'), Js('Tears'), Js('Thorn'), Js('Torment'), Js('Touch'), Js('Toxin'), Js('Venom'), Js('Water')]))
    var.put('nm3', Js([Js('Abra'), Js('Ache'), Js('Allure'), Js('Alpha'), Js('Appetite'), Js('Arachnid'), Js('Ash'), Js('Asphyx'), Js('Ataxia'), Js('Axiom'), Js('Bane'), Js('Banshee'), Js('Basilisk'), Js('Beta'), Js('Bilge'), Js('Billow'), Js('Bloat'), Js('Brimstone'), Js('Burnout'), Js('Catalyst'), Js('Chaos'), Js('Cinder'), Js('Coax'), Js('Craze'), Js('Crucifix'), Js('Daemon'), Js('Debris'), Js('Decoy'), Js('Desire'), Js('Dew'), Js('Djinn'), Js('Dolor'), Js('Dupe'), Js('Eclipse'), Js('Empathy'), Js('Entropy'), Js('Enzyme'), Js('Fiend'), Js('Finis'), Js('Frenzy'), Js('Garrotte'), Js('Ghost'), Js('Goad'), Js('Greed'), Js('Grief'), Js('Gunk'), Js('Gyre'), Js('Harrow'), Js('Heartache'), Js('Hellion'), Js('Hound'), Js('Imp'), Js('Impetus'), Js('Impulse'), Js('Incentive'), Js('Inferno'), Js('Itch'), Js('Jester'), Js('Jinx'), Js('Knave'), Js('Knockout'), Js('Limbo'), Js('Malady'), Js('Manes'), Js('Mangle'), Js('Mania'), Js('Martyr'), Js('Medusa'), Js('Mire'), Js('Misery'), Js('Muffle'), Js('Musk'), Js('Muze'), Js('Nag'), Js('Necro'), Js('Nightmare'), Js('Pandemonium'), Js('Pest'), Js('Phantom'), Js('Pixie'), Js('Purgatory'), Js('Quelch'), Js('Rapture'), Js('Relish'), Js('Residue'), Js('Revelation'), Js('Revenant'), Js('Rogue'), Js('Rune'), Js('Scapegoat'), Js('Scorch'), Js('Serpent'), Js('Shush'), Js('Silence'), Js('Silt'), Js('Slag'), Js('Sludge'), Js('Smite'), Js('Smother'), Js('Smudge'), Js('Sprite'), Js('Spur'), Js('Stitch'), Js('Stranger'), Js('Strangle'), Js('Symbiote'), Js('Tease'), Js('Terra'), Js('Throe'), Js('Throttle'), Js('Tickle'), Js('Toll'), Js('Torment'), Js('Tremble'), Js('Truth'), Js('Twilight'), Js('Twinge'), Js('Vision'), Js('Voodoo'), Js('Vortex'), Js('Wish'), Js('Wraith'), Js('Wyvern')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(2.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', var.get('nm3').get(var.get('rnd')))
                    var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nma').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmb').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmd').get('length'))))
                    if (var.get('i')<Js(7.0)):
                        while (var.get('rnd')<Js(7.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nma').get('length'))))
                        var.put('names', ((var.get('nma').get(var.get('rnd'))+var.get('nmb').get(var.get('rnd2')))+var.get('nmd').get(var.get('rnd3'))))
                    else:
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmc').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmb').get('length'))))
                        var.put('names', ((((var.get('nma').get(var.get('rnd'))+var.get('nmb').get(var.get('rnd2')))+var.get('nmc').get(var.get('rnd4')))+var.get('nmb').get(var.get('rnd5')))+var.get('nmd').get(var.get('rnd3'))))
            var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nma', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js('bh'), Js('br'), Js('ch'), Js('cl'), Js('cr'), Js('dh'), Js('dr'), Js('fh'), Js('fl'), Js('fr'), Js('gh'), Js('gl'), Js('gr'), Js('kh'), Js('kl'), Js('kr'), Js('ph'), Js('pn'), Js('pr'), Js('rh'), Js('sc'), Js('sh'), Js('st'), Js('str'), Js('th'), Js('tr'), Js('vr')]))
var.put('nmb', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y'), Js('y'), Js('ae'), Js('ai'), Js('ei'), Js('ia'), Js('ie'), Js('ee'), Js('eo')]))
var.put('nmc', Js([Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('z'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('z'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('z'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('z'), Js('cc'), Js('cl'), Js('cn'), Js('dd'), Js('dh'), Js('ff'), Js('fn'), Js('fr'), Js('fl'), Js('gd'), Js('gg'), Js('gh'), Js('gm'), Js('gn'), Js('gr'), Js('hh'), Js('kk'), Js('kb'), Js('kh'), Js('kl'), Js('kn'), Js('km'), Js('kr'), Js('ll'), Js('lc'), Js('lg'), Js('lk'), Js('lm'), Js('ln'), Js('lq'), Js('lv'), Js('lz'), Js('mm'), Js('mh'), Js('mn'), Js('mr'), Js('mz'), Js('ng'), Js('nd'), Js('nc'), Js('nh'), Js('nk'), Js('nl'), Js('nm'), Js('nn'), Js('nr'), Js('nt'), Js('nv'), Js('nz'), Js('qn'), Js('qr'), Js('rc'), Js('rd'), Js('rg'), Js('rh'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rq'), Js('rr'), Js('rt'), Js('rv'), Js('rz'), Js('sc'), Js('sg'), Js('sl'), Js('sm'), Js('sn'), Js('sp'), Js('ss'), Js('st'), Js('th'), Js('tr'), Js('ts'), Js('vr'), Js('xn'), Js('xm'), Js('xl')]))
var.put('nmd', Js([Js('caine'), Js('cide'), Js('cin'), Js('cite'), Js('cyn'), Js('cyne'), Js('din'), Js('dis'), Js('dyn'), Js('fen'), Js('fin'), Js('fyde'), Js('hyde'), Js('kite'), Js('kyde'), Js('laine'), Js('lax'), Js('lic'), Js('lite'), Js('lyce'), Js('lys'), Js('mane'), Js('mide'), Js('min'), Js('mine'), Js('mis'), Js('mith'), Js('nade'), Js('nari'), Js('nic'), Js('nide'), Js('nine'), Js('nite'), Js('nith'), Js('nix'), Js('nol'), Js('nyde'), Js('nyte'), Js('phax'), Js('phis'), Js('phite'), Js('phix'), Js('phyn'), Js('raide'), Js('raine'), Js('rax'), Js('rin'), Js('rine'), Js('ris'), Js('rith'), Js('rix'), Js('ron'), Js('rux'), Js('ryn'), Js('sane'), Js('sax'), Js('sel'), Js('sin'), Js('sine'), Js('sinth'), Js('site'), Js('sithe'), Js('smin'), Js('sol'), Js('syl'), Js('syn'), Js('sys'), Js('syth'), Js('tain'), Js('thine'), Js('tin'), Js('tith'), Js('tocin'), Js('tyl'), Js('tyne'), Js('vain'), Js('vine'), Js('vis'), Js('vith'), Js('vyl'), Js('vys'), Js('vyth'), Js('xain'), Js('xal'), Js('xide'), Js('xin'), Js('xol'), Js('xyl'), Js('xyth'), Js('zal'), Js('zid'), Js('zite'), Js('zol'), Js('zon'), Js('zyl')]))
pass
pass


# Add lib to the module scope
poisonNames = var.to_python()