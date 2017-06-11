__all__ = ['hackerNames']

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
    var.registers(['nm1', 'result'])
    var.put('nm1', Js([Js('Aberration (4b3rr4710n)'), Js('Absence (4b53nc3)'), Js('Ace (4c3)'), Js('Acid (4c1d)'), Js('Alakazam (4l4k4z4m)'), Js('Alien (4l13n)'), Js('Alpha (4lph4)'), Js('Angel (4n63l)'), Js('Angler (4n6l3r)'), Js('Anomaly (4n0m4ly)'), Js('Anonymous (4n0nym0u5)'), Js('Answer (4n5w3r)'), Js('Ant (4n7)'), Js('Aqua (4qu4)'), Js('Archangel (4rch4n63l)'), Js('Aspect (45p3c7)'), Js('Atom (470m)'), Js('Avatar (4v474r)'), Js('Awe (4w3)'), Js('Azure (4zur3)'), Js('Behemoth (b3h3m07h)'), Js('Beta (b374)'), Js('Bishop (b15h0p)'), Js('Bite (b173)'), Js('Blade (bl4d3)'), Js('Blank (bl4nk)'), Js('Blazer (bl4z3r)'), Js('Bliss (bl155)'), Js('Boggle (b066l3)'), Js('Bolt (b0l7)'), Js('Bullet (bull37)'), Js('Bullseye (bull53y3)'), Js('Burn (burn)'), Js('Catch-22 (c47ch-22)'), Js('Chaos (ch405)'), Js('Charade (ch4r4d3)'), Js('Charm (ch4rm)'), Js('Chase (ch453)'), Js('Chief (ch13f)'), Js('Chimera (ch1m3r4)'), Js('Chronicle (chr0n1cl3)'), Js('Cipher (c1ph3r)'), Js('Claw (cl4w)'), Js('Cloud (cl0ud)'), Js('Combo (c0mb0)'), Js('Comet (c0m37)'), Js('Complex (c0mpl3x)'), Js('Conjurer (c0njur3r)'), Js('Cowboy (c0wb0y)'), Js('Craze (cr4z3)'), Js('Crotchet (cr07ch37)'), Js('Crow (cr0w)'), Js('Crypto (cryp70)'), Js('Cryptonic (cryp70n1c)'), Js('Curse (cur53)'), Js('Dagger (d4663r)'), Js('Dante (d4n73)'), Js('Daydream (d4ydr34m)'), Js('Dexter (d3x73r)'), Js('Diablo (d14bl0)'), Js('Doc (d0c)'), Js('Doppelganger (d0pp3l64n63r)'), Js('Drake (dr4k3)'), Js('Dread (dr34d)'), Js('Duckling (duckl1n6)'), Js('Ecstasy (3c5745y)'), Js('Enigma (3n16m4)'), Js('Epitome (3p170m3)'), Js('Essence (3553nc3)'), Js('Eternity (373rn17y)'), Js('Face (f4c3)'), Js('Fata Morgana (f474 m0r64n4)'), Js('Fetish (f3715h)'), Js('Fiend (f13nd)'), Js('Flash (fl45h)'), Js('Flinch (fl1nch)'), Js('Fluke (fluk3)'), Js('Fragment (fr46m3n7)'), Js('Freak (fr34k)'), Js('Fury (fury)'), Js('Gem (63m)'), Js('Ghoul (6h0ul)'), Js('Gloom (6l00m)'), Js('Gluttony (6lu770ny)'), Js('Grace (6r4c3)'), Js('Griffin (6r1ff1n)'), Js('Grim (6r1m)'), Js('Grimace (6r1m4c3)'), Js('Grin (6r1n)'), Js('Guru (6uru)'), Js('Habit (h4b17)'), Js('Habitat (h4b1747)'), Js('Haze (h4z3)'), Js('Hex (h3x)'), Js('Hoax (h04x)'), Js('Hollow (h0ll0w)'), Js('Hound (h0und)'), Js('Ibis (1b15)'), Js('Idol (1d0l)'), Js('Impossible (1mp0551bl3)'), Js('Indie (1nd13)'), Js('Infinity (1nf1n17y)'), Js('Jinx (j1nx)'), Js('Juju (juju)'), Js('Kid (k1d)'), Js('Kiss (k155)'), Js('Knight (kn16h7)'), Js('Knot (kn07)'), Js('Law (l4w)'), Js('Legacy (l364cy)'), Js('Lightning (l16h7n1n6)'), Js('Limbo (l1mb0)'), Js('Lynx (lynx)'), Js('Maestro (m4357r0)'), Js('Mania (m4n14)'), Js('Marshall (m4r5h4ll)'), Js('Mascot (m45c07)'), Js('Matriarch (m47r14rch)'), Js('Memento (m3m3n70)'), Js('Memory (m3m0ry)'), Js('Mermaid (m3rm41d)'), Js('Mime (m1m3)'), Js('Mongoose (m0n60053)'), Js('Monkey (m0nk3y)'), Js('Moonlight (m00nl16h7)'), Js('Moonshine (m00n5h1n3)'), Js('Morgana (m0r64n4)'), Js('Mothership (m07h3r5h1p)'), Js('Myth (my7h)'), Js('Nemesis (n3m3515)'), Js('Nemo (n3m0)'), Js('Nest (n357)'), Js('Neurosis (n3ur0515)'), Js('Nighthawk (n16h7h4wk)'), Js('Nightmare (n16h7m4r3)'), Js('Nightowl (n16h70wl)'), Js('Nix (n1x)'), Js('Nobody (n0b0dy)'), Js('Nova (n0v4)'), Js('Oblivion (0bl1v10n)'), Js('Obsidian (0b51d14n)'), Js('Oddity (0dd17y)'), Js('Omega (0m364)'), Js('Onyx (0nyx)'), Js('Oracle (0r4cl3)'), Js('Override (0v3rr1d3)'), Js('Owl (0wl)'), Js('Panther (p4n7h3r)'), Js('Paradox (p4r4d0x)'), Js('Paragon (p4r460n)'), Js('Parody (p4r0dy)'), Js('Particle (p4r71cl3)'), Js('Patriarch (p47r14rch)'), Js('Perplex (p3rpl3x)'), Js('Phantasm (ph4n745m)'), Js('Phantom (ph4n70m)'), Js('Phase (ph453)'), Js('Phobia (ph0b14)'), Js('Phoenix (ph03n1x)'), Js('Pierce (p13rc3)'), Js('Plague (pl46u3)'), Js('Poltergeist (p0l73r63157)'), Js('Prankster (pr4nk573r)'), Js('Pride (pr1d3)'), Js('Prima Donna (pr1m4 d0nn4)'), Js('Prophecy (pr0ph3cy)'), Js('Proto (pr070)'), Js('Proxy (pr0xy)'), Js('Quad (qu4d)'), Js('Quake (qu4k3)'), Js('Question (qu35710n)'), Js('Quicksilver (qu1ck51lv3r)'), Js('Quirk (qu1rk)'), Js('Rapture (r4p7ur3)'), Js('Ray (r4y)'), Js('Reaper (r34p3r)'), Js('Rebus (r3bu5)'), Js('Reverse (r3v3r53)'), Js('Riddle (r1ddl3)'), Js('Rider (r1d3r)'), Js('Rogue (r06u3)'), Js('Rune (run3)'), Js('Saber (54b3r)'), Js('Sabertooth (54b3r7007h)'), Js('Sage (5463)'), Js('Savant (54v4n7)'), Js('Scepter (5c3p73r)'), Js('Sentinel (53n71n3l)'), Js('Serenity (53r3n17y)'), Js('Serpent (53rp3n7)'), Js('Shade (5h4d3)'), Js('Shadow (5h4d0w)'), Js('Shark (5h4rk)'), Js('Shell (5h3ll)'), Js('Shepherd (5h3ph3rd)'), Js('Shield (5h13ld)'), Js('Sickle (51ckl3)'), Js('Silver (51lv3r)'), Js('Skipper (5k1pp3r)'), Js('Sliver (5l1v3r)'), Js('Sloth (5l07h)'), Js('Smog (5m06)'), Js('Specter (5p3c73r)'), Js('Sphinx (5ph1nx)'), Js('Spider (5p1d3r)'), Js('Splinter (5pl1n73r)'), Js('Spook (5p00k)'), Js('Squirt (5qu1r7)'), Js('Stalker (574lk3r)'), Js('Storm (570rm)'), Js('Streak (57r34k)'), Js('Sunshine (5un5h1n3)'), Js('Surprise (5urpr153)'), Js('Swan (5w4n)'), Js('Talisman (74l15m4n)'), Js('Tinge (71n63)'), Js('Torpedo (70rp3d0)'), Js('Trace (7r4c3)'), Js('Tracer (7r4c3r)'), Js('Trail (7r41l)'), Js('Tremor (7r3m0r)'), Js('Trinity (7r1n17y)'), Js('Trix (7r1x)'), Js('Trixy (7r1xy)'), Js('Trust (7ru57)'), Js('Twist (7w157)'), Js('Umbra (umbr4)'), Js('Umbrage (umbr463)'), Js('Vacuum (v4cuum)'), Js('Vagabond (v464b0nd)'), Js('Veil (v31l)'), Js('Vermin (v3rm1n)'), Js('Vestige (v357163)'), Js('Viper (v1p3r)'), Js('Visage (v15463)'), Js('Vision (v1510n)'), Js('Void (v01d)'), Js('Voodoo (v00d00)'), Js('Voyage (v0y463)'), Js('Wasp (w45p)'), Js('Web (w3b)'), Js('Webster (w3b573r)'), Js('Whiz (wh1z)'), Js('Witcher (w17ch3r)'), Js('Wolf (w0lf)'), Js('Wraith (wr417h)'), Js('Wrath (wr47h)'), Js('Wyvern (wyv3rn)'), Js('Zero (z3r0)'), Js('Zigzag (z16z46)'), Js('Zion (z10n)')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
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
hackerNames = var.to_python()