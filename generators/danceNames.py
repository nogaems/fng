__all__ = ['danceNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', (Js('The ')+var.get('nm1').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aeris'), Js('Aggi'), Js('Badger'), Js('Banty'), Js('Beast'), Js('Bibbot'), Js('Biddy'), Js('Big Beat'), Js('Birch'), Js('Bird'), Js('Blaze'), Js('Bleep'), Js('Bobble'), Js('Bounce'), Js('Bubble'), Js('Buffet'), Js('Bulldozer'), Js('Bungle'), Js('Champ'), Js('Changle'), Js('Chic'), Js('Chime'), Js('Chomp'), Js('Corkscrew'), Js('Crochet'), Js('Crowle'), Js('Crumble'), Js('Cuckoo'), Js('Cudge'), Js('Dart'), Js('Daydream'), Js('Dimpel'), Js('Dither'), Js('Divet'), Js('Doodle'), Js('Dove'), Js('Drub'), Js('Dynamo'), Js('Dynomite'), Js('Eags'), Js('Edge'), Js('Engage'), Js('Faddy'), Js('Fav'), Js('Fitter'), Js('Flinch'), Js('Flitter'), Js('Flogger'), Js('Flub'), Js('Folly'), Js('Freebie'), Js('Frump'), Js('Fuss'), Js('Gallop'), Js('Gambol'), Js('Garble'), Js('Ghost'), Js('Gliss'), Js('Glitch'), Js('Goad'), Js('Goose'), Js('Grind'), Js('Grizzle'), Js('Growl'), Js('Gyro'), Js('Hash'), Js('Hitch'), Js('Hotfoot'), Js('Hush'), Js('Ide'), Js('Jar'), Js('Jaral'), Js('Jerk'), Js('Jigger'), Js('Jiggle'), Js('Jiggle Jaggle'), Js('Jimjam'), Js('Jog'), Js('Joggle'), Js('Joggy'), Js('Joker'), Js('Jolly'), Js('Jostle'), Js('Jounce'), Js('Jumble'), Js('Jump Step'), Js('Kink'), Js('Klink'), Js('Lagger'), Js('Lambal'), Js('Lax'), Js('Leapfrog'), Js('Libble'), Js('Little Beat'), Js('Loon'), Js('Maggle'), Js('Magic'), Js('Manic'), Js('Mash'), Js('Mellow'), Js('Melo'), Js('Mirage'), Js('Mit'), Js('Mockingbird'), Js('Muddle'), Js('Nazzle'), Js('Nidge'), Js('Nittle'), Js('Nudge'), Js('Paddle'), Js("Pep 'n Punch"), Js('Pint'), Js('Pivot'), Js('Poch'), Js('Privy'), Js('Puff'), Js('Pulp'), Js('Pulse'), Js('Quake'), Js('Rane'), Js('Rass'), Js('Rubble'), Js('Sarge'), Js('Sault'), Js('Scant'), Js('Scouge'), Js('Scrunch'), Js('Sembla'), Js('Serk'), Js('Shamble'), Js('Shidder'), Js('Shifshof'), Js('Shift'), Js('Shift Shuffle'), Js('Shimsham'), Js('Siggy'), Js('Skippit'), Js('Skitter'), Js('Slapdash'), Js('Slither'), Js('Sliver'), Js('Snaff'), Js('Snap'), Js('Snapper'), Js('Snats'), Js('Snipsnap'), Js('Spark'), Js('Spigot'), Js('Spout'), Js('Spurrit'), Js('Squash'), Js('Squeek'), Js('Squish'), Js('Squish Squash'), Js('Staggle'), Js('Starlight Dance'), Js('Stip Step'), Js('Stir'), Js('Stragle'), Js('Streak'), Js('Stripstrap'), Js('Stritstrat'), Js('Surge'), Js('Swagger'), Js('Sway'), Js('Swerve'), Js('Swiggy'), Js('Swivel'), Js("Swivel 'n Swerve"), Js('Swoop'), Js('Tangle'), Js('Thrib'), Js('Thump'), Js("Thump 'n Stump"), Js('Thunder'), Js('Tirin'), Js('Toots'), Js('Totter'), Js('Trebble'), Js('Tribble'), Js('Trifle'), Js('Trimble'), Js('Triptrap'), Js('Trotter'), Js('Tweak'), Js('Twiddle'), Js('Twiddlefitch'), Js('Twilight'), Js('Twine'), Js('Twinkle Toes'), Js('Twitch'), Js('Twitter'), Js('Vex'), Js('Vice'), Js('Vigger'), Js('Vortex'), Js('Wade'), Js('Wallis'), Js('Waver'), Js('Whim'), Js('Whirl'), Js('Whisker'), Js('Whisper'), Js('Wicked'), Js('Widget'), Js('Wig'), Js('Wiggle'), Js('Wix'), Js('Wobble'), Js('Wraith'), Js('Yoke'), Js('Zigzag')]))
pass
pass


# Add lib to the module scope
danceNames = var.to_python()