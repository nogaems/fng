__all__ = ['worldDefenders']

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
    var.registers(['nm1', 'nm4', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Cosmos'), Js('Dimension'), Js('Domain'), Js('Dominion'), Js('Epoch'), Js('Era'), Js('Essence'), Js('Existence'), Js('Generation'), Js('Globe'), Js('History'), Js('Life'), Js('Planet'), Js('Realm'), Js('Soul'), Js('Spirit'), Js('Time'), Js('Universe'), Js('World')]))
    var.put('nm2', Js([Js('Advancer'), Js('Adviser'), Js('Angel'), Js('Arranger'), Js('Attender'), Js('Beholder'), Js('Caretaker'), Js('Cerberus'), Js('Champion'), Js('Chaperon'), Js('Chaperone'), Js('Cherisher'), Js('Conservator'), Js('Counsel'), Js('Cradler'), Js('Curator'), Js('Custodian'), Js('Defender'), Js('Dreamer'), Js('Embracer'), Js('Empowerer'), Js('Favor'), Js('Forger'), Js('Founder'), Js('Freer'), Js('Gardener'), Js('Groomer'), Js('Grower'), Js('Guardian'), Js('Guide'), Js('Guider'), Js('Handler'), Js('Harmonizer'), Js('Healer'), Js('Hero'), Js('Immerser'), Js('Improver'), Js('Indulger'), Js('Infuser'), Js('Inspirer'), Js('Inventer'), Js('Keeper'), Js('Leader'), Js('Liberator'), Js('Lover'), Js('Manager'), Js('Matriarch'), Js('Mediater'), Js('Mentor'), Js('Motivator'), Js('Moulder'), Js('Nourisher'), Js('Nurterer'), Js('Observer'), Js('Overseer'), Js('Patriarch'), Js('Pioneer'), Js('Preserver'), Js('Promoter'), Js('Protector'), Js('Provider'), Js('Raiser'), Js('Savior'), Js('Sentinel'), Js('Sentry'), Js('Servant'), Js('Shepherd'), Js('Spirit'), Js('Stabalizer'), Js('Steward'), Js('Stimulator'), Js('Strengthener'), Js('Supporter'), Js('Tender'), Js('Treasurer'), Js('Upholder'), Js('Warden'), Js('Watcher')]))
    var.put('nm3', Js([Js('Adored'), Js('Ancient'), Js('Angelic'), Js('Auspicious'), Js('Brave'), Js('Cherished'), Js('Courageous'), Js('Eternal'), Js('Ethereal'), Js('Exalted'), Js('Faithful'), Js('Fearless'), Js('Flawless'), Js('Gentle'), Js('Gifted'), Js('Giving'), Js('Glorious'), Js('Golden'), Js('Gracious'), Js('Grand'), Js('Hallowed'), Js('Heavenly'), Js('Infinite'), Js('Lasting'), Js('Light'), Js('Living'), Js('Lone'), Js('Majestic'), Js('Marked'), Js('Mellow'), Js('Mighty'), Js('Mysterious'), Js('Otherworldy'), Js('Primal'), Js('Prime'), Js('Pure'), Js('Radiant'), Js('Revered'), Js('Righteous'), Js('Sacred'), Js('Serene'), Js('Shrouded'), Js('Silent'), Js('Silver'), Js('Supreme'), Js('Twin'), Js('Unseen'), Js('Unsung'), Js('Utopian'), Js('Veiled'), Js('Venerated'), Js('Vigilant'), Js('Waiting'), Js('Winged')]))
    var.put('nm4', Js([Js('the Cosmos'), Js('Dimensions'), Js('Domains'), Js('Dominions'), Js('Epochs'), Js('Eras'), Js('Essences'), Js('Existence'), Js('Generations'), Js('Globes'), Js('History'), Js('Life'), Js('Planets'), Js('the Planet'), Js('Realms'), Js('Souls'), Js('Spirits'), Js('Time'), Js('Universes'), Js('the Universe'), Js('Worlds'), Js('the World')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm2').get(var.get('rnd2'))+Js(' of '))+var.get('nm4').get(var.get('rnd'))))
                    var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        var.put('names', (((Js('The ')+var.get('nm3').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                        var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
                        var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
                    else:
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                        var.put('names', (((((Js('The ')+var.get('nm3').get(var.get('rnd')))+Js(' '))+var.get('nm1').get(var.get('rnd3')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                        var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
                        var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
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
worldDefenders = var.to_python()