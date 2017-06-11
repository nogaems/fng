__all__ = ['backstories']

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
    var.registers(['nm19', 'nm1', 'nm11', 'rnd18', 'rnd19', 'rnd11', 'nm12b', 'nm16', 'rnd8', 'nm3', 'rnd14', 'rnd17', 'nm2', 'type', 'rnd15a', 'nm14', 'tp', 'nm7', 'nm10', 'nm21', 'rnd2c', 'nm15', 'nm20', 'rnd21', 'rnd5', 'nm12', 'nm5', 'gnd', 'rnd2a', 'rnd4', 'names', 'rnd7', 'result', 'nm6', 'rnd2b', 'rnd6', 'rnd20', 'rnd13', 'nm4', 'rnd3', 'rnd12b', 'nm8', 'nm18', 'nm17', 'nm13', 'nm9', 'rnd10', 'rnd16', 'rnd12', 'rnd15b'])
    var.put('nm1', Js([Js('He'), Js('he'), Js('his'), Js('him'), Js('man')]))
    var.put('nm2', Js([Js('adventurous'), Js('affectionate'), Js('analytical'), Js('athletic'), Js('brave'), Js('calm'), Js('capable'), Js('charismatic'), Js('charming'), Js('cheerful'), Js('creative'), Js('curious'), Js('daring'), Js('dedicated'), Js('dependable'), Js('determined'), Js('driven'), Js('dutiful'), Js('eager'), Js('elegant'), Js('energetic'), Js('faithful'), Js('funny'), Js('generous'), Js('gentle'), Js('happy'), Js('helpful'), Js('honest'), Js('hospitable'), Js('humble'), Js('humorous'), Js('innocent'), Js('intelligent'), Js('intrepid'), Js('jovial'), Js('just'), Js('light-hearted'), Js('loyal'), Js('modest'), Js('mysterious'), Js('polite'), Js('popular'), Js('proud'), Js('quick'), Js('reliable'), Js('responsible'), Js('savvy'), Js('sensitive'), Js('sincere'), Js('sweet'), Js('talkative'), Js('thoughtful'), Js('whimsical'), Js('wise'), Js('witty')]))
    var.put('nm3', Js([Js('anxious'), Js('arrogant'), Js('bewildered'), Js('bossy'), Js('conceited'), Js('confused'), Js('facetious'), Js('foolish'), Js('greedy'), Js('grouchy'), Js('harsh'), Js('ignorant'), Js('immature'), Js('impatient'), Js('impulsive'), Js('jealous'), Js('lonely'), Js('mean'), Js('naive'), Js('nervous'), Js('opinionated'), Js('pompous'), Js('rash'), Js('restless'), Js('rude'), Js('selfish'), Js('snobbish'), Js('stubborn'), Js('timid'), Js('uncontrolled')]))
    var.put('nm4', Js([Js('This is to be expected from somebody'), Js("But what'd you expect from somebody"), Js("This isn't surprising considering for someone"), Js("Which isn't out of the ordinary for someone"), Js('But this is all just a facade, a mechanism to deal'), Js("But there's more than this to somebody"), Js("But there's more than meets the eye, not surprising for somebody")]))
    var.put('nm5', Js([Js('n average'), Js(' wealthy'), Js(' royal'), Js('n ordinary'), Js(' fairly rich'), Js(' high class'), Js(' middle class'), Js(' loving'), Js(' large'), Js(' small'), Js(' decent'), Js(' successful')]))
    var.put('nm6', Js([Js('n average'), Js(' normal'), Js(' large'), Js(' wealthy'), Js(' major'), Js('n important'), Js(' merchant'), Js(' developing'), Js(' developed')]))
    var.put('nm7', Js([Js('town'), Js('city'), Js('village'), Js('port'), Js('community'), Js('capital')]))
    var.put('nm8', Js([Js('without worry'), Js('out of trouble'), Js('free of worries'), Js('free of trouble'), Js('in peace'), Js('comfortably'), Js('happily')]))
    var.put('nm9', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(10.0)))+Js(10.0)))
    var.put('nm10', Js([Js('things changed'), Js('things began to change'), Js('life changed'), Js('life began to change')]))
    var.put('nm11', Js([Js('gained responsibilities'), Js('gained new responsibilities'), Js('became more important'), Js('became more important to society'), Js('got an important job'), Js('started to travel a lot'), Js('started to travel the world'), Js('started to experience the world'), Js('started working for the family company'), Js('studied a lot'), Js('went to college'), Js('explored the country'), Js('moved out'), Js('moved in with a friend'), Js('did volunteering work'), Js('did a lot of small jobs'), Js('moved to another country'), Js('became a travelling adventurer'), Js('went on an adventure'), Js('improved upon existing powers'), Js('got a new pet'), Js('got a new companion')]))
    var.put('nm12', Js([Js('among the most popular people'), Js('becoming quite desirable'), Js('very successful'), Js('growing up fast'), Js('meeting a lot of influential people'), Js('making many new friends'), Js('learning a lot of new skills'), Js('gaining a little fame'), Js('making some great new friends'), Js("about to meet 'Mr(s). Right'"), Js('learning a new language'), Js('becoming more cultured'), Js('slowly improving upon existing skills'), Js('learning how to cook in new styles'), Js('strengthening the relationships with friends'), Js('strengthening the relationship with both parents'), Js('competing in large tournaments')]))
    var.put('nm12b', Js([Js('managed to bloom'), Js('succeeded'), Js('managed to thrive'), Js('boomed'), Js('went beyond expectations'), Js('reached for the stars'), Js('lives the dream'), Js('blossomed'), Js('reached the top'), Js('made a fortune'), Js('fulfilled dreams'), Js('thrived'), Js('enjoys life'), Js('loves life'), Js('struggles to make it'), Js('is going on a journey'), Js('is part of an adventure'), Js('is trying to reach the top'), Js('is unstoppable'), Js('is on top of the world'), Js('is exploring new areas'), Js('is discovering hidden secrets'), Js('is discovering hidden treasures'), Js('is venturing out'), Js('is trying to help others')]))
    var.put('nm13', Js([Js('With the support of great friends'), Js('With the support of great parents'), Js('With plenty of money and connections'), Js('Alongside great friends'), Js('With amazing, new friends'), Js('With a great deal of determination'), Js('With determination and some luck'), Js('Alongside trusted friends'), Js('With a great companion'), Js('Through hard work'), Js('Through plenty of trial and error'), Js('By never giving up'), Js('After an astonishing adventure'), Js('With the help of great friends'), Js('Having overcome plenty of obstacles')]))
    var.put('nm14', Js([Js('strange'), Js('weird'), Js('crazy'), Js('ever changing'), Js('fast'), Js('fast changing'), Js('amazing'), Js('fantasy'), Js('fantastic'), Js('wacky'), Js('absurd'), Js('strange'), Js('mad'), Js('wild'), Js('remarkable'), Js('wonderful'), Js('outlandish'), Js('astonishing'), Js('extraordinary'), Js('mystifying')]))
    var.put('nm15', Js([Js('bravery'), Js('brilliance'), Js('capability'), Js('charm'), Js('compassion'), Js('curiosity'), Js('determination'), Js('diligence'), Js('eagerness'), Js('sense of humor'), Js('wits'), Js('cunning'), Js('perseverance'), Js('persistence'), Js('skills'), Js('powers'), Js('talents'), Js('wisdom'), Js('intrepidness'), Js('honesty')]))
    var.put('nm16', Js([Js('reaching great success'), Js('finding a way to the top'), Js('fulfilling all dreams'), Js('accomplish all goals'), Js('improving the world'), Js('going beyond expectations'), Js('climbing to the top'), Js('staying ahead of the game'), Js('reaching full potential'), Js('doing anything')]))
    var.put('nm17', Js([Js('a force to be reckoned with'), Js('a true inspiration for many'), Js('a true friend for life'), Js("an ally you'd want by your side"), Js('somebody we can expect great things of'), Js('somebody who could change the world'), Js('a great leader, perhaps even of the nation'), Js('an unstoppable force'), Js("a friend you'd want by your side"), Js('a person of (great) importance')]))
    var.put('nm18', Js([Js('Despite all this success,'), Js('However,'), Js('But there may be more to it than this;'), Js("But for now that's speculation;"), Js('But only time will tell;'), Js('But who really knows what will happen;'), Js('But anything could happen;'), Js('But things could change quickly;')]))
    var.put('nm19', Js([Js('searching for a higher purpose'), Js('still studying'), Js('enjoying the simpler life'), Js('having fun with friends'), Js('travelling the world'), Js('exploring everything'), Js('still growing up and learning new things'), Js('still finding the right place in the world'), Js('still looking for a true calling'), Js('still trying to perfect skills'), Js('improving upon skills and talents'), Js('learning how to reach full potential'), Js('enjoying the world and its beauty'), Js('looking for a place to truly call home'), Js('still learning, exploring and discovering')]))
    var.put('nm20', Js([Js('to explore'), Js('than meets the eye'), Js('than we know'), Js('secrets than answers'), Js('than what we get to know'), Js('to experience'), Js('to discover'), Js('to see, taste and experience'), Js('than people let on'), Js('incredible sights to behold'), Js('watchful eyes than expected'), Js('caution than needed'), Js('to learn'), Js('to enjoy'), Js('people to meet')]))
    var.put('nm21', Js([Js('great friends'), Js('great companions'), Js('great parents'), Js('amazing friends'), Js('plenty of resources'), Js('a great family'), Js('awesome friends'), Js('great people around'), Js('wise teachers and great friends'), Js('a close group of friends')]))
    var.put('names', Js([]))
    var.put('tp', var.get('type'))
    var.put('gnd', var.get('Math').callprop('random'))
    if (var.get('gnd')<Js(0.5)):
        var.put('nm1', Js([Js('She'), Js('she'), Js('her'), Js('her'), Js('woman')]))
    if PyJsStrictEq(var.get('tp'),Js(2.0)):
        def PyJs_LONG_0_(var=var):
            return var.put('nm2', Js([Js('adventurous'), Js('ambitious'), Js('angry'), Js('arrogant'), Js('brave'), Js('calm'), Js('capable'), Js('cautious'), Js('clever'), Js('coarse'), Js('conceited'), Js('confident'), Js('crafty'), Js('cross'), Js('daring'), Js('dauntless'), Js('determined'), Js('eager'), Js('efficient'), Js('facetious'), Js('fierce'), Js('frank'), Js('gloomy'), Js('greedy'), Js('hardy'), Js('harsh'), Js('impartial'), Js('impatient'), Js('impolite'), Js('impulsive'), Js('independent'), Js('intelligent'), Js('keen'), Js('loyal'), Js('malicious'), Js('mysterious'), Js('observant'), Js('pensive'), Js('petulant'), Js('precise'), Js('punctilious'), Js('quick'), Js('quiet'), Js('sarcastic'), Js('scornful'), Js('self-reliant'), Js('sincere'), Js('skillful'), Js('sly'), Js('stingy'), Js('strict'), Js('stubborn'), Js('sullen'), Js('tactful'), Js('versatile'), Js('vulgar'), Js('witty')]))
        PyJs_LONG_0_()
        var.put('nm3', Js([Js('disturbing'), Js('dreadful'), Js('gruesome'), Js('horrifying'), Js('shocking'), Js('terrible'), Js('tormented'), Js('troubled'), Js('ugly'), Js('unsettling')]))
        var.put('nm5', Js([Js(' broken'), Js(' decent'), Js(' fairly rich'), Js(' great'), Js(' high class'), Js(' large'), Js(' loving'), Js(' lower class'), Js(' middle class'), Js(' needy'), Js(' poor'), Js(' small'), Js(' successful'), Js(' wealthy'), Js('n average'), Js('n ordinary')]))
        var.put('nm6', Js([Js('n average'), Js(' normal'), Js(' large'), Js(' wealthy'), Js(' major'), Js('n important'), Js(' merchant'), Js(' developing'), Js(' developed'), Js(' poor'), Js(' broken')]))
        var.put('nm9', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(13.0)))+Js(4.0)))
        var.put('nm10', Js([Js('things changed'), Js('life changed'), Js('everything changed'), Js('life changed drastically'), Js('life took a turn for the worst'), Js('things took a turn for the worst')]))
        if (var.get('gnd')<Js(0.5)):
            def PyJs_LONG_1_(var=var):
                return var.put('nm11', Js([Js('lost her parents in'), Js('lost her mother in'), Js('lost her father in'), Js('lost her parents when they left after'), Js('lost her best friend in'), Js('lost her home when it was destroyed after'), Js('lost her money after'), Js('lost her family was they were split up after'), Js('lost her brother in'), Js('lost her sister in'), Js('lost her sisters in'), Js('lost her brothers in'), Js('lost her siblings in'), Js('lost her family in'), Js('killed somebody by accident during'), Js('killed somebody during'), Js('maimed somebody during'), Js('accidently maimed somebody during'), Js("destroyed someone's life during"), Js("destroyed someone's life by accident during")]))
            PyJs_LONG_1_()
        else:
            def PyJs_LONG_2_(var=var):
                return var.put('nm11', Js([Js('lost his parents in'), Js('lost his mother in'), Js('lost his father in'), Js('lost his parents when they left after'), Js('lost his best friend in'), Js('lost his home when it was destroyed after'), Js('lost his money after'), Js('lost his family was they were split up after'), Js('lost his brother in'), Js('lost his sister in'), Js('lost his sisters in'), Js('lost his brothers in'), Js('lost his siblings in'), Js('lost his family in'), Js('killed somebody by accident during'), Js('killed somebody during'), Js('maimed somebody during'), Js('accidently maimed somebody during'), Js("destroyed someone's life during"), Js("destroyed someone's life by accident during")]))
            PyJs_LONG_2_()
        def PyJs_LONG_3_(var=var):
            return var.put('nm12', Js([Js('a freak fire'), Js('a robbery gone wrong'), Js('a terrible disaster'), Js('a natural disaster'), Js('a suspicious accident'), Js('a fight which got out of control'), Js('an invasion'), Js('a brutal war'), Js('a drought'), Js('an act of terrorism'), Js('a volcanic eruption'), Js('a hurricane'), Js('an earthquake'), Js('a horrible flood'), Js('a long lasting heatwave'), Js('an epidemic'), Js('a food shortage'), Js('a power outage'), Js('a government takeover'), Js('a rebellion'), Js('a revolution')]))
        PyJs_LONG_3_()
        def PyJs_LONG_4_(var=var):
            return var.put('nm12b', Js([Js('abandoned by all'), Js('forsaken by all'), Js('arrested'), Js('forgotten by everybody'), Js('neglected by everybody'), Js('shunned'), Js('rejected by all'), Js('becoming an outcast'), Js('caught up with the wrong people'), Js('initiated in a gang'), Js('now part of a sinister clan'), Js('headed for a life of crime'), Js('headed for a life of misery'), Js('now alone and forgotten'), Js('now alone, miserable and abandoned')]))
        PyJs_LONG_4_()
        def PyJs_LONG_5_(var=var):
            return var.put('nm13', Js([Js('With a new found friend'), Js('All alone'), Js('Without any help'), Js('With a childhood friend'), Js('With the help of a stranger'), Js('Alone, lost and forgotten'), Js('With the help of a small group of strangers'), Js('With a couple of friends'), Js('With a new found love'), Js('With the help of a suspicious stranger'), Js('With the help of a suspicious friend'), Js('While persued by the authority'), Js('While persued by a criminal gang'), Js('While persued by strangers'), Js('While obstructed by many'), Js('Against all odds'), Js('Alongside a brother'), Js('Alongside a sister'), Js('Alongside a cousin'), Js('Together with a companion'), Js('Together with a pet'), Js('With a loyal stranger'), Js('With a loyal friend'), Js('Reunited with a friend'), Js('Reunited with a lost pet')]))
        PyJs_LONG_5_()
        var.put('nm14', Js([Js('wicked'), Js('crazy'), Js('bizarre'), Js('cruel'), Js('outlandish'), Js('odd'), Js('harsh'), Js('criminal'), Js('insane'), Js('mad'), Js('bitter'), Js('rough'), Js('bleak'), Js('brutal'), Js('relentless'), Js('unkind'), Js('pitiless'), Js('vicious'), Js('villainous'), Js('corrupt')]))
        var.put('nm15', Js([Js('bravery'), Js('fighting skills'), Js('capability'), Js('charm'), Js('vigor'), Js('courage'), Js('determination'), Js('diligence'), Js('eagerness'), Js('inginuity'), Js('wits'), Js('cunning'), Js('perseverance'), Js('persistance'), Js('skills'), Js('powers'), Js('talents'), Js('wisdom'), Js('intrepidness'), Js('strength')]))
        var.put('nm17', var.get('nm16'))
        def PyJs_LONG_6_(var=var):
            return var.put('nm18', Js([Js('Still plagued by the past'), Js('While haunted by memories of the past'), Js('Powerless to change the past'), Js('With new found pride and some happiness'), Js('Still affected by the past'), Js('Having finally found some peace of mind'), Js('Having finally found some stability'), Js('After finally turning life around'), Js('With a new chance at life'), Js('With the lessons of the past'), Js('While still constantly on the move'), Js('With the skills learned in the past'), Js('Having found a significant other'), Js('Settled down and with some peace and quiet'), Js('While constantly travelling the world')]))
        PyJs_LONG_6_()
        def PyJs_LONG_7_(var=var):
            return var.put('nm19', Js([Js('on helping people'), Js('as a mercenary for the king'), Js('a small job with low pay'), Js('on making it in a large tournament'), Js('on meeting new, kind people'), Js('buying a house'), Js('fitting in with society'), Js('as a travelling trader'), Js('as a travelling gun for hire'), Js('as a travelling help for hire'), Js('on travelling and surviving of nature'), Js('perfecting skills and talents'), Js('tracking the people of the past'), Js('as help for hire'), Js('as a sailor')]))
        PyJs_LONG_7_()
        def PyJs_LONG_8_(var=var):
            return var.put('nm20', Js([Js('find some form of redemption'), Js('shed the memories of the past'), Js('be released of the haunting memories'), Js('find a place to call home'), Js('live a normal life'), Js('find safety and happiness'), Js('find joy and happiness in life'), Js('leave the past behind'), Js('find inner peace'), Js('find answers to the events of the past'), Js('learn more about the past'), Js('find vengeance for the actions in the past'), Js('forget about the past'), Js('start life over on a good note'), Js('support a new, honest life')]))
        PyJs_LONG_8_()
        var.put('nm21', Js([Js('peace of mind'), Js('friends'), Js('happiness'), Js('joy and love for life'), Js('stability and security'), Js('tranquility'), Js('joys and comforts of life'), Js('pleasureful life'), Js('significant other'), Js('purpose to life')]))
    var.put('rnd2a', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
    var.put('rnd2b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
    while PyJsStrictEq(var.get('rnd2a'),var.get('rnd2b')):
        var.put('rnd2b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
    var.put('rnd2c', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
    while (PyJsStrictEq(var.get('rnd2c'),var.get('rnd2b')) or PyJsStrictEq(var.get('rnd2c'),var.get('rnd2a'))):
        var.put('rnd2c', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
    var.put('rnd12b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12b').get('length'))))
    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
    var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
    var.put('rnd15a', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
    var.put('rnd15b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
    while PyJsStrictEq(var.get('rnd15a'),var.get('rnd15b')):
        var.put('rnd15b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
    var.put('rnd16', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
    var.put('rnd17', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
    while PyJsStrictEq(var.get('rnd16'),var.get('rnd17')):
        var.put('rnd17', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
    var.put('rnd18', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
    var.put('rnd19', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
    var.put('rnd20', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
    var.put('rnd21', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length'))))
    if PyJsStrictEq(var.get('tp'),Js(2.0)):
        var.get('names').put('0', (((((((((((((var.get('nm1').get('0')+Js("'s "))+var.get('nm2').get(var.get('rnd2a')))+Js(', '))+var.get('nm2').get(var.get('rnd2b')))+Js(' and '))+var.get('nm2').get(var.get('rnd2c')))+Js('. '))+var.get('nm4').get(var.get('rnd4')))+Js(' with '))+var.get('nm1').get('2'))+Js(' '))+var.get('nm3').get(var.get('rnd3')))+Js(' past.')))
        def PyJs_LONG_9_(var=var):
            return (((((((((((((((var.get('nm1').get('0')+Js(' was born and grew up in a'))+var.get('nm5').get(var.get('rnd5')))+Js(' family in a'))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+Js(', '))+var.get('nm1').get('1'))+Js(' lived '))+var.get('nm8').get(var.get('rnd8')))+Js(' until '))+var.get('nm1').get('1'))+Js(' was about '))+var.get('nm9'))+Js(' years old, but at that point '))
        var.get('names').put('1', ((PyJs_LONG_9_()+var.get('nm10').get(var.get('rnd10')))+Js('.')))
        def PyJs_LONG_11_(var=var):
            def PyJs_LONG_10_(var=var):
                return (((((((((((((((var.get('nm1').get('0')+Js(' '))+var.get('nm11').get(var.get('rnd11')))+Js(' '))+var.get('nm12').get(var.get('rnd12')))+Js(' and was '))+var.get('nm12b').get(var.get('rnd12b')))+Js('. '))+var.get('nm13').get(var.get('rnd13')))+Js(' '))+var.get('nm1').get('1'))+Js(' had to survive in a '))+var.get('nm14').get(var.get('rnd14')))+Js(' world. But with '))+var.get('nm1').get('2'))+Js(' '))
            return ((((((((((((((((PyJs_LONG_10_()+var.get('nm15').get(var.get('rnd15a')))+Js(' and '))+var.get('nm15').get(var.get('rnd15b')))+Js(', '))+var.get('nm1').get('1'))+Js(' managed to '))+var.get('nm16').get(var.get('rnd16')))+Js(' and '))+var.get('nm17').get(var.get('rnd17')))+Js('. This has turned '))+var.get('nm1').get('3'))+Js(' into the '))+var.get('nm1').get('4'))+Js(' '))+var.get('nm1').get('1'))+Js(' is today.'))
        var.get('names').put('2', PyJs_LONG_11_())
        var.get('names').put('3', (((((((((((((var.get('nm18').get(var.get('rnd18'))+Js(', '))+var.get('nm1').get('1'))+Js(' now works '))+var.get('nm19').get(var.get('rnd19')))+Js('. By doing so, '))+var.get('nm1').get('1'))+Js(' hopes to '))+var.get('nm20').get(var.get('rnd20')))+Js(' and finally find '))+var.get('nm21').get(var.get('rnd21')))+Js(' '))+var.get('nm1').get('1'))+Js(' has never had.')))
    else:
        var.get('names').put('0', (((((((((((((var.get('nm1').get('0')+Js("'s "))+var.get('nm2').get(var.get('rnd2a')))+Js(', '))+var.get('nm2').get(var.get('rnd2b')))+Js(', '))+var.get('nm2').get(var.get('rnd2c')))+Js(' and perhaps a little too '))+var.get('nm3').get(var.get('rnd3')))+Js('. '))+var.get('nm4').get(var.get('rnd4')))+Js(' with '))+var.get('nm1').get('2'))+Js(' position.')))
        def PyJs_LONG_12_(var=var):
            return ((((((((((((((((var.get('nm1').get('0')+Js(' was born in a'))+var.get('nm5').get(var.get('rnd5')))+Js(' family in a'))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+Js('. '))+var.get('nm1').get('0'))+Js(' lived '))+var.get('nm8').get(var.get('rnd8')))+Js(' until '))+var.get('nm1').get('1'))+Js(' was about '))+var.get('nm9'))+Js(' years old, but at that point '))+var.get('nm10').get(var.get('rnd10')))
        var.get('names').put('1', (PyJs_LONG_12_()+Js('.')))
        def PyJs_LONG_13_(var=var):
            return ((((((((((((((((var.get('nm1').get('0')+Js(' '))+var.get('nm11').get(var.get('rnd11')))+Js(' and was '))+var.get('nm12').get(var.get('rnd12')))+Js('.  '))+var.get('nm13').get(var.get('rnd13')))+Js(', '))+var.get('nm1').get('1'))+Js(' '))+var.get('nm12b').get(var.get('rnd12b')))+Js(' in a '))+var.get('nm14').get(var.get('rnd14')))+Js(' world. But with '))+var.get('nm1').get('2'))+Js(' '))+var.get('nm15').get(var.get('rnd15a')))
        var.get('names').put('2', (((((((((((PyJs_LONG_13_()+Js(' and '))+var.get('nm15').get(var.get('rnd15b')))+Js(", there's nothing to stop "))+var.get('nm1').get('3'))+Js(' from '))+var.get('nm16').get(var.get('rnd16')))+Js('. '))+var.get('nm1').get('0'))+Js(' could quickly become '))+var.get('nm17').get(var.get('rnd17')))+Js('.')))
        def PyJs_LONG_14_(var=var):
            return ((((((((((((((var.get('nm18').get(var.get('rnd18'))+Js(' '))+var.get('nm1').get('1'))+Js(' is currently '))+var.get('nm19').get(var.get('rnd19')))+Js('. '))+var.get('nm1').get('0'))+Js(" feels like there's more "))+var.get('nm20').get(var.get('rnd20')))+Js(' in this world. Luckily '))+var.get('nm1').get('1'))+Js(' has '))+var.get('nm21').get(var.get('rnd21')))+Js(' to support '))+var.get('nm1').get('3'))
        var.get('names').put('3', (PyJs_LONG_14_()+Js('.')))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(4.0)):
        try:
            pass
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
backstories = var.to_python()