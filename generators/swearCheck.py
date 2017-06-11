__all__ = ['swearCheck']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['swear', 'testSwear'])
var.put('swear', Js([Js('anal'), Js('anilingus'), Js('anus'), Js('apeshit'), Js('arse'), Js('arsehole'), Js('ass'), Js('asshole'), Js('assmunch'), Js('autoerotic'), Js('babeland'), Js('balls'), Js('ballsack'), Js('bangbros'), Js('bareback'), Js('barenaked'), Js('bastard'), Js('bastardo'), Js('bastinado'), Js('beaner'), Js('beaners'), Js('bestiality'), Js('biatch'), Js('bigtits'), Js('bimbos'), Js('birdlock'), Js('bitch'), Js('bitches'), Js('bloody'), Js('blowjob'), Js('blumpkin'), Js('bollock'), Js('bollocks'), Js('bollok'), Js('bondage'), Js('boner'), Js('boob'), Js('boobs'), Js('bugger'), Js('bukkake'), Js('bulldyke'), Js('bullshit'), Js('bum'), Js('bunghole'), Js('busty'), Js('butt'), Js('buttcheeks'), Js('butthole'), Js('buttplug'), Js('cameltoe'), Js('camgirl'), Js('camslut'), Js('camwhore'), Js('clit'), Js('clitoris'), Js('clusterfuck'), Js('cock'), Js('cocks'), Js('coon'), Js('coons'), Js('cornhole'), Js('crap'), Js('creampie'), Js('cum'), Js('cumming'), Js('cunt'), Js('damn'), Js('darkie'), Js('daterape'), Js('deepthroat'), Js('dick'), Js('dildo'), Js('doggy'), Js('dolcett'), Js('domination'), Js('dominatrix'), Js('dommes'), Js('dryhump'), Js('dyke'), Js('ecchi'), Js('ejaculation'), Js('erotic'), Js('erotism'), Js('escort'), Js('eunuch'), Js('fag'), Js('faggot'), Js('fecal'), Js('feck'), Js('felch'), Js('felching'), Js('fellate'), Js('fellatio'), Js('feltch'), Js('femdom'), Js('fetish'), Js('figging'), Js('fingerbang'), Js('fingering'), Js('fisting'), Js('flange'), Js('footjob'), Js('frotting'), Js('fuck'), Js('fuckin'), Js('fucking'), Js('fucktard'), Js('fucktards'), Js('fudgepacker'), Js('futanari'), Js('gangbang'), Js('gaysex'), Js('genitals'), Js('goatcx'), Js('goatse'), Js('goddamn'), Js('gokkun'), Js('goodpoop'), Js('googirl'), Js('goregasm'), Js('grope'), Js('groupsex'), Js('guro'), Js('handjob'), Js('hardcore'), Js('hell'), Js('hentai'), Js('homo'), Js('homoerotic'), Js('honkey'), Js('hooker'), Js('humping'), Js('incest'), Js('intercourse'), Js('jackoff'), Js('jailbait'), Js('jerk'), Js('jerkoff'), Js('jigaboo'), Js('jiggaboo'), Js('jiggerboo'), Js('jizz'), Js('juggs'), Js('kike'), Js('kinbaku'), Js('kinkster'), Js('kinky'), Js('knobbing'), Js('knobend'), Js('labia'), Js('lmao'), Js('lmfao'), Js('lolita'), Js('masturbate'), Js('milf'), Js('muff'), Js('nambla'), Js('nawashi'), Js('negro'), Js('neonazi'), Js('niga'), Js('nigra'), Js('niggas'), Js('niggaz'), Js('nigga'), Js('nigger'), Js('nignog'), Js('nimphomania'), Js('nipple'), Js('nipples'), Js('nude'), Js('nudity'), Js('nympho'), Js('nymphomania'), Js('octopussy'), Js('omg'), Js('omorashi'), Js('orgasm'), Js('orgy'), Js('paedo'), Js('paki'), Js('panties'), Js('panty'), Js('pedo'), Js('pegging'), Js('penis'), Js('piss'), Js('pissing'), Js('pisspig'), Js('playboy'), Js('ponyplay'), Js('poof'), Js('poon'), Js('poontang'), Js('poop'), Js('porn'), Js('porno'), Js('prick'), Js('pube'), Js('pubes'), Js('punany'), Js('pussy'), Js('queaf'), Js('queef'), Js('queer'), Js('quim'), Js('raghead'), Js('rape'), Js('raping'), Js('rapist'), Js('rectum'), Js('rimjob'), Js('rimming'), Js('sadism'), Js('santorum'), Js('scat'), Js('schlong'), Js('scissoring'), Js('scrotum'), Js('semen'), Js('sex'), Js('sexo'), Js('sexy'), Js('shaved'), Js('shemale'), Js('shibari'), Js('shit'), Js('shitblimp'), Js('shitty'), Js('shota'), Js('shrimping'), Js('skeet'), Js('slanteye'), Js('slut'), Js('smegma'), Js('smut'), Js('snatch'), Js('sodomize'), Js('sodomy'), Js('spic'), Js('splooge'), Js('spooge'), Js('spunk'), Js('strapon'), Js('suck'), Js('sucks'), Js('suicide'), Js('sultry'), Js('swastika'), Js('swinger'), Js('threesome'), Js('throating'), Js('tit'), Js('tits'), Js('titties'), Js('titty'), Js('topless'), Js('tosser'), Js('towelhead'), Js('tranni'), Js('trany'), Js('trani'), Js('tranny'), Js('tubgirl'), Js('turd'), Js('tushy'), Js('twat'), Js('twink'), Js('twinkie'), Js('upskirt'), Js('urethra'), Js('urophilia'), Js('vagina'), Js('vibrator'), Js('voyeur'), Js('vulva'), Js('wank'), Js('wetback'), Js('whore'), Js('wtf'), Js('yaoi'), Js('yiffy')]))
@Js
def PyJs_anonymous_0_(nm, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'nm':nm, 'this':this}, var)
    var.registers(['nm', 'name'])
    var.put('name', var.get('nm'))
    if PyJsStrictEq(var.get('swear').callprop('indexOf', var.get('name')),(-Js(1.0))):
        return var.get('name')
    else:
        return Js('')
PyJs_anonymous_0_._set_name('anonymous')
var.put('testSwear', PyJs_anonymous_0_)


# Add lib to the module scope
swearCheck = var.to_python()