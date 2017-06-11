__all__ = ['crabNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('AlPinchino'), Js('Alpha'), Js('Apollo'), Js('Aqua'), Js('Atoll'), Js('Aura'), Js('Azure'), Js('BamBam'), Js('Barnacle'), Js('Biscuit'), Js('Blazer'), Js('Blister'), Js('Boulder'), Js('Bounce'), Js('Butters'), Js('Buttons'), Js('Carapace'), Js('Checkers'), Js('Chester'), Js('Chowder'), Js('Chuck'), Js('Clacker'), Js('Clawford'), Js('Claws'), Js('Clawz'), Js('Clicker'), Js('Clipper'), Js('Clyde'), Js('Cobbler'), Js('CrabCake'), Js('Crabanasty'), Js('Crabapple'), Js('Crabbitz'), Js('Crabohydrate'), Js('Crack'), Js('Crane'), Js('Crash'), Js('Cruncher'), Js('Crunchy'), Js('Crust'), Js('Crusty'), Js('DrZoidberg'), Js('Dude'), Js('Escape'), Js('Fang'), Js('Fangs'), Js('Fuzzball'), Js('Fuzzy'), Js('Gil'), Js('Gillian'), Js('Grabandhold'), Js('Grabby'), Js('Grabs'), Js('Griper'), Js('Grouch'), Js('Grouchy'), Js('Grump'), Js('Hardhead'), Js('Hardy'), Js('Herman'), Js('Hermi'), Js('Hermie'), Js('Hermit'), Js('Hermy'), Js('Hifive'), Js('Hyde'), Js('Kingler'), Js('Krabby'), Js('Krabs'), Js('Kraken'), Js('Kuka'), Js('MaxPayne'), Js('Muffin'), Js('Nemo'), Js('Neptune'), Js('Nero'), Js('Norbert'), Js('Omega'), Js('Onyx'), Js('Orea'), Js('Pace'), Js('Patty'), Js('Payne'), Js('Piccolo'), Js('Pinch'), Js('Pincher'), Js('Pinchino'), Js('Pinchy'), Js('Pinstripe'), Js('Pointy'), Js('Popeye'), Js('Poseidon'), Js('Prawn'), Js('Ranger'), Js('Reef'), Js('Ripple'), Js('Riptide'), Js('Rock'), Js('Rocklobster'), Js('Rocky'), Js('Rogue'), Js('Salt'), Js('Salty'), Js('Saul'), Js('Scratch'), Js('Scratchy'), Js('Sebastion'), Js('Sellfish'), Js('Shabby'), Js('Shade'), Js('Shadow'), Js('Shamrock'), Js('Sheldon'), Js('Shell'), Js('Shelly'), Js('Sideways'), Js('Skipper'), Js('SmallFry'), Js('Snap'), Js('Snapp'), Js('Snappah'), Js('Snapper'), Js('Snappy'), Js('Snaps'), Js('Snipper'), Js('Snippy'), Js('Snips'), Js('Snookums'), Js('Softshell'), Js('Softy'), Js('Sparkle'), Js('Spike'), Js('Spikes'), Js('Spot'), Js('Surf'), Js('Surimi'), Js('Twitch'), Js('Waddle'), Js('Waddles'), Js('Wave'), Js('Waves'), Js('Whopper'), Js('Wobble'), Js('Wobbles'), Js('Zippy'), Js('Zoidberg'), Js('iClaw'), Js('iPinch'), Js('iSnap')]))
var.put('nm2', Js([Js('Aphrodite'), Js('Arial'), Js('Aqua'), Js('Ariel'), Js('Atolle'), Js('Aura'), Js('Ava'), Js('Aurora'), Js('Ava'), Js('Azure'), Js('Azura'), Js('Bashful'), Js('Bashy'), Js('Bash'), Js('Bay'), Js('Baye'), Js('Biscuit'), Js('Bitsy'), Js('Star'), Js('Bo'), Js('Bounce'), Js('Bouncy'), Js('Brooke'), Js('Bubble'), Js('Bubbles'), Js('Button'), Js('Buttons'), Js('Cake'), Js('Cami'), Js('Carapace'), Js('Checkers'), Js('Chesty'), Js('Clawford'), Js('Snips'), Js('Snippy'), Js('Snipsnap'), Js('Clacks'), Js('Clacky'), Js('Clawdia'), Js('Clawdis'), Js('Claws'), Js('Clips'), Js('Clippy'), Js('Cobble'), Js('Coco'), Js('Coral'), Js('Cora'), Js('Cakes'), Js('Crabine'), Js('Crabina'), Js('Crackle'), Js('Crackles'), Js('Crash'), Js('Crunchey'), Js('Dazzle'), Js('Dora'), Js('Sandy'), Js('Nemo'), Js('Escape'), Js('Fuzzball'), Js('Fuzzy'), Js('Gill'), Js('Gilly'), Js('Grabby'), Js('Grabbis'), Js('Gripes'), Js('Hermine'), Js('Hermione'), Js('Hermi'), Js('Hermilia'), Js('Hermyse'), Js('Pinchy'), Js('Itsy'), Js('Krabsy'), Js('MsKraken'), Js('Lily'), Js('Lime'), Js('MrsCrabapple'), Js('Crabapple'), Js('Muffin'), Js('MsPinch'), Js('MrsKrabs'), Js('Oasis'), Js('Oceane'), Js('Oceana'), Js('Pinchys'), Js('Pinchy'), Js('Pique'), Js('Pixie'), Js('Princess'), Js('Rainbow'), Js('Sparkle'), Js('Reefe'), Js('Ria'), Js('Ripples'), Js('Ripple'), Js('Rogue'), Js('Shadow'), Js('Shade'), Js('Ruby'), Js('Sally'), Js('Sandy'), Js('Sapphire'), Js('Scratches'), Js('Biscuit'), Js('Shelly'), Js('Shine'), Js('Snappy'), Js('Snips'), Js('Snaps'), Js('Sparkles'), Js('Sparkle'), Js('Spot'), Js('Dot'), Js('Dots'), Js('Surimi'), Js('Waddles'), Js('Wobble'), Js('Wobbles'), Js('Waddle')]))
pass
pass


# Add lib to the module scope
crabNames = var.to_python()