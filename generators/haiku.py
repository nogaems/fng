__all__ = ['haiku']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1c', 'first', 'nm1b', 'nm6b', 'nm4a', 'nameGen', 'nm2a', 'nm5a', 'nm1a', 'nm3a', 'nm2b', 'nm2c', 'nm3b', 'nm4b', 'nm5b'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['snt3', 'snt2', 'snt1', 'result', 'rnd', 'rnd2'])
    var.put('snt1', ((var.get('Math').callprop('random')*Js(5.0))|Js(0.0)))
    var.put('snt2', ((var.get('Math').callprop('random')*Js(2.0))|Js(0.0)))
    var.put('snt3', ((var.get('Math').callprop('random')*Js(3.0))|Js(0.0)))
    if PyJsStrictEq(var.get('snt1'),Js(0.0)):
        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1a').get('length'))|Js(0.0)))
        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2a').get('length'))|Js(0.0)))
        var.put('names1', ((var.get('nm1a').get(var.get('rnd'))+Js(' '))+var.get('nm2a').get(var.get('rnd2'))))
    else:
        if PyJsStrictEq(var.get('snt1'),Js(1.0)):
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1b').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2b').get('length'))|Js(0.0)))
            var.put('names1', ((var.get('nm1b').get(var.get('rnd'))+Js(' '))+var.get('nm2b').get(var.get('rnd2'))))
        else:
            if PyJsStrictEq(var.get('snt1'),Js(2.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1c').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2c').get('length'))|Js(0.0)))
                var.put('names1', ((var.get('nm1c').get(var.get('rnd'))+Js(' '))+var.get('nm2c').get(var.get('rnd2'))))
            else:
                if PyJsStrictEq(var.get('snt1'),Js(3.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5a').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2c').get('length'))|Js(0.0)))
                    var.put('names1', ((var.get('nm5a').get(var.get('rnd'))+Js(' '))+var.get('nm2c').get(var.get('rnd2'))))
                else:
                    if PyJsStrictEq(var.get('snt1'),Js(4.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5b').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm6b').get('length'))|Js(0.0)))
                        var.put('names1', ((var.get('nm5b').get(var.get('rnd'))+Js(' '))+var.get('nm6b').get(var.get('rnd2'))))
    if PyJsStrictEq(var.get('snt2'),Js(0.0)):
        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm3a').get('length'))|Js(0.0)))
        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm4a').get('length'))|Js(0.0)))
        var.put('names2', ((var.get('nm3a').get(var.get('rnd'))+Js(' '))+var.get('nm4a').get(var.get('rnd2'))))
    else:
        if PyJsStrictEq(var.get('snt2'),Js(1.0)):
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm3b').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm4b').get('length'))|Js(0.0)))
            var.put('names2', ((var.get('nm3b').get(var.get('rnd'))+Js(' '))+var.get('nm4b').get(var.get('rnd2'))))
    if PyJsStrictEq(var.get('snt3'),Js(0.0)):
        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1a').get('length'))|Js(0.0)))
        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2a').get('length'))|Js(0.0)))
        var.put('names3', ((var.get('nm1a').get(var.get('rnd'))+Js(' '))+var.get('nm2a').get(var.get('rnd2'))))
    else:
        if PyJsStrictEq(var.get('snt3'),Js(1.0)):
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1b').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2b').get('length'))|Js(0.0)))
            var.put('names3', ((var.get('nm1b').get(var.get('rnd'))+Js(' '))+var.get('nm2b').get(var.get('rnd2'))))
        else:
            if PyJsStrictEq(var.get('snt3'),Js(2.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5a').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2c').get('length'))|Js(0.0)))
                var.put('names3', ((var.get('nm5a').get(var.get('rnd'))+Js(' '))+var.get('nm2c').get(var.get('rnd2'))))
    if PyJsStrictEq(var.get('first'),Js(0.0)):
        var.put('first', Js(1.0))
        var.put('names1', Js('Haiku for you all'))
        var.put('names2', Js('Single click gives random one'))
        var.put('names3', Js('Hope it brings you joy'))
    var.put('result', Js([]))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1a', Js([Js('All sleep'), Js('Ants march'), Js('Art flows'), Js('Beast crawls'), Js('Bird flies'), Js('Birds fly'), Js('Blood spills'), Js('Boats drift'), Js('Bread shared'), Js('Child laughs'), Js('Days pass'), Js('Death takes'), Js('Dog barks'), Js('Dust glides'), Js('Eyes dart'), Js('Fall spreads'), Js('Fields wave'), Js('Fish swim'), Js('Flags drift'), Js('Fog shrouds'), Js('Friends laugh'), Js('Frog jumps'), Js('Grass grows'), Js('Grass sways'), Js('Guests laugh'), Js('Hair flows'), Js('Hear beats'), Js('Hearts run'), Js('Homes warm'), Js('Ice wraps'), Js('King rules'), Js('Knife cuts'), Js('Leaf drifts'), Js('Leaves drift'), Js('Love grows'), Js('Moon shines'), Js('Night falls'), Js('Owl flies'), Js('Path runs'), Js('Rain falls'), Js('Scents drift'), Js('Snow cloaks'), Js('Spring swells'), Js('Trees sway'), Js('Wealth flows'), Js('Winds blow'), Js('Wolf howls'), Js('Wood creaks'), Js('World spins'), Js('Years pass')]))
var.put('nm1b', Js([Js('Ant marches'), Js('Armies march'), Js('Army moves'), Js('Baby crawls'), Js('Balloon drifts'), Js('Bells jingle'), Js('Boats sailing'), Js('Branches sprout'), Js('Candles sway'), Js('Children laugh'), Js('Donkey walks'), Js('Drinks shared'), Js('Earth covers'), Js('Fall reaching'), Js('Feather drifts'), Js('Fingers work'), Js('Fires glow'), Js('Flames flicker'), Js('Flowers wave'), Js("Food's shared"), Js('Forest grows'), Js('Games played'), Js('Gardens spread'), Js('Insects fly'), Js('Lanterns swing'), Js('Leather wraps'), Js('Light shines'), Js('Markets spread'), Js('Money spent'), Js('Mountains reach'), Js('Music plays'), Js('Nature grows'), Js('Night covers'), Js('Ocean flows'), Js('Paintings made'), Js('People live'), Js('Petals fall'), Js('Power flows'), Js('River flows'), Js('Silence falls'), Js('Snow blankets'), Js('Snow falling'), Js('Stories told'), Js('Summer spreads'), Js('Sun shines bright'), Js('Sunshine beams'), Js("Tea's brewing"), Js('Water flows'), Js('Winds howling'), Js('Winter shrouds')]))
var.put('nm1c', Js([Js('Answers'), Js('Birthdays'), Js('Blossoms'), Js('Business'), Js('Children'), Js('Cooking'), Js('Countries'), Js('Courage'), Js('Creatures'), Js('Daydreams'), Js('Drama'), Js('Dreaming'), Js('Faces'), Js('Failure'), Js('Fortune'), Js('Friendship'), Js('Gaming'), Js('Garbage'), Js('Judgment'), Js('Knowledge'), Js('Laughter'), Js('Lovers'), Js('Midnight'), Js('Moments'), Js('Motion'), Js('Mountains'), Js('Nations'), Js('Nature'), Js('Nightmares'), Js('Passions'), Js('Patience'), Js('Payments'), Js('People'), Js('Pictures'), Js('Rainfall'), Js('Science'), Js('Snowfall'), Js('Speeches'), Js('Stories'), Js('Strangers'), Js('Success'), Js('Sunshine'), Js('Symbols'), Js('Teachings'), Js('Thunder'), Js('Treasures'), Js('Weddings'), Js('Wisdom'), Js('Women'), Js('Writings')]))
var.put('nm2a', Js([Js('across fields'), Js('across land'), Js('all alone'), Js('all around'), Js('almost gone'), Js('among friends'), Js('as spring falls'), Js('awoken now'), Js('back and forth'), Js('close at hand'), Js('close to heart'), Js('disturbed'), Js('far away'), Js('from the East'), Js('from the sky'), Js('game of bliss'), Js('gently yet'), Js('good and bad'), Js('in center'), Js('in shadows'), Js('in silence'), Js('in spring night'), Js('in still peace'), Js('in the light'), Js('in the wind'), Js('in twilight'), Js('lonely now'), Js('morning comes'), Js('music plays'), Js('nearby home'), Js('over here'), Js('over hills'), Js('over there'), Js('playfully'), Js('side to side'), Js('silently'), Js('softly still'), Js('swift and just'), Js('throughout all'), Js('time to time'), Js('to the West'), Js('to the sky'), Js('turn around'), Js('voiceless now'), Js('wait and see'), Js('wild and fierce'), Js('with caution'), Js('with desire'), Js('with relief'), Js('with rigor'), Js('without care'), Js('without fear'), Js('without grief'), Js('eternally')]))
var.put('nm2b', Js([Js('around'), Js('at dawn'), Js('at day'), Js('at dusk'), Js('at night'), Js('away'), Js('blissful'), Js('brightly'), Js('carefree'), Js('cheerful'), Js('eagerly'), Js('earnest'), Js('fondly'), Js('freely'), Js('gently'), Js('gladly'), Js('gracious'), Js('grateful'), Js('greedy'), Js('humbly'), Js('hungry'), Js('idle'), Js('in light'), Js('lightly'), Js('lively'), Js('lonely'), Js('naive'), Js('nearby'), Js('nervous'), Js('nothing'), Js('on top'), Js('onward'), Js('perfect'), Js('quickly'), Js('quiet'), Js('reckless'), Js('selfish'), Js('slightly'), Js('slowly'), Js('smoothly'), Js('softly'), Js('sudden'), Js('swiftly'), Js('timely'), Js('troubled'), Js('truthful'), Js('untrue'), Js('upset'), Js('vivid'), Js('weary'), Js('wicked')]))
var.put('nm2c', Js([Js('of today'), Js('of friendship'), Js('in-between'), Js('intertwined'), Js('of success'), Js('of fortune'), Js('at the sea'), Js('in the rain'), Js('in winter'), Js('of winter'), Js('in summer'), Js('of summer'), Js('of the spring'), Js('in the spring'), Js('the applause'), Js('of fire'), Js('in whispers'), Js('in silence'), Js('in war time'), Js('in peace time'), Js('in the past'), Js('of futures'), Js('of lovers'), Js('sweet embrace'), Js('through seasons'), Js('of wonder'), Js('of ventures'), Js('in my mind'), Js('in your eyes'), Js('of nature'), Js('of lost ruins'), Js('of ages'), Js('after life'), Js('after death'), Js('another'), Js('of yonder'), Js('without end'), Js('of a wish'), Js('after rain'), Js('of balance'), Js('of refuge'), Js('of the end'), Js('of a star'), Js('of the dead'), Js('in the fields'), Js('of the lake'), Js('of autumn'), Js('in autumn'), Js('on the ice'), Js('in a pond')]))
var.put('nm3a', Js([Js('A true friend'), Js('Autumn rain'), Js('Beast of love'), Js('Bird of prey'), Js('Blue moonlight'), Js('Burning love'), Js('Crescent moon'), Js('Fallen foe'), Js('Firefly'), Js('Flightless bird'), Js('Fresh footstep'), Js('Friend from past'), Js('Friend of all'), Js('Frozen time'), Js('Gliding leaf'), Js("Heaven's gate"), Js('Hidden smile'), Js('Howling wind'), Js('Hush of wind'), Js('Last farewell'), Js('Leafing tree'), Js('Lonely heart'), Js('Lost stranger'), Js("Love's embrace"), Js('Lull of night'), Js('Melting snow'), Js('Midday heat'), Js('Mirror lake'), Js('Morning dew'), Js('Naked skin'), Js('Nothing now'), Js('Open door'), Js('Paradise'), Js('Quiet gust'), Js('Racing mind'), Js('Rain of fall'), Js('Rain of spring'), Js('Rising moon'), Js('Rising sun'), Js('Setting sun'), Js('Silent hush'), Js('Singing bird'), Js('Sleeping child'), Js('Snake in grass'), Js('Sparkling star'), Js('Spring blossom'), Js('Summer heat'), Js('Tender hug'), Js('Winter snow'), Js('Wolf like sheep')]))
var.put('nm3b', Js([Js('Brewing storms'), Js('Brief regret'), Js('Cooling down'), Js('Drastic times'), Js('Ecstasy'), Js('Empty all'), Js('Empty bed'), Js('Entertained'), Js('Faintest sound'), Js('Final rest'), Js('Final straw'), Js('Forgotten'), Js('Fragrant scents'), Js('Gentle touch'), Js('Gift of life'), Js('Gift of love'), Js('Grain of salt'), Js('Happy dance'), Js('Happy thoughts'), Js('Harmonies'), Js('Holding breath'), Js('Kindred souls'), Js('Last moment'), Js('Little griefs'), Js('Loudest words'), Js('Melodies'), Js('Mingled worlds'), Js("Nature's grasp"), Js('Nothing left'), Js('Now you go'), Js('One last step'), Js('Playful jest'), Js('Purest bliss'), Js('Quiet noise'), Js('Quivered breath'), Js('Satisfied'), Js('Silver lines'), Js('Small blessings'), Js('Sweet chorus'), Js('Sweet delights'), Js('Sweetest taste'), Js('Tiny joys'), Js('Tranquil peace'), Js('Treasure trove'), Js('Trouble brews'), Js('Turn away'), Js('Turn to ash'), Js('Voiceless song'), Js('Wait for me'), Js('Warming up')]))
var.put('nm4a', Js([Js('adapts to all'), Js('answers to none'), Js('assaults the air'), Js('awaits true fate'), Js('awoken now'), Js('bathing in light'), Js('beckons me close'), Js('blossoms once more'), Js('breathing silent'), Js('brings joy once more'), Js('caressed by love'), Js('challenges none'), Js('cleansing the past'), Js('collapsing slow'), Js('commanding me'), Js('communicates'), Js('delaying joy'), Js('destined to pass'), Js('discovers all'), Js("drinks life's essence"), Js('dwells in the past'), Js('embraced by all'), Js('emerging soon'), Js('enhanced by life'), Js('escaping fast'), Js('focused on good'), Js('forgotten fast'), Js('glances quickly'), Js('guarantees bliss'), Js('hovers above'), Js('is always true'), Js('is free to go'), Js('is hypnotized'), Js('is lost in time'), Js('is never lost'), Js('is worthy too'), Js('leaves home once more'), Js('lures you in close'), Js('never migrates'), Js('now understands'), Js('on the morrow'), Js('overcome with joy'), Js('prepares for fate'), Js('reaches further'), Js('resigned to fate'), Js('restores balance'), Js('rising slowly'), Js('shifts in the sands'), Js('silenced no more'), Js('stands with courage')]))
var.put('nm4b', Js([Js('still in my arms'), Js('of love long lost'), Js('of memories'), Js("of summer's night"), Js('between the stars'), Js('before spring falls'), Js('before fall springs'), Js('lost in the rain'), Js('emerged at last'), Js('with bitter taste'), Js('to leave once more'), Js('now look for more'), Js('stay very close'), Js('on dual sides'), Js('of my delight'), Js('of hope and bliss'), Js('without answers'), Js('with answers found'), Js('as echoes pass'), Js('without passion'), Js('and cry from far'), Js('as time returns'), Js('of gifts received'), Js('and sweet goodbyes'), Js('of lovers thoughts'), Js('in tranquil minds'), Js('behind the end'), Js('before the dawn'), Js('after sun sets'), Js('ahead of time'), Js('in front of joy'), Js('ere farewell voiced'), Js('around my mind'), Js('below true home'), Js('into the end'), Js("towards love's grace"), Js('without support'), Js("until you're back"), Js('within my soul'), Js('beyond this world'), Js('for spirits loved'), Js('against the waves'), Js('among lost hope'), Js('outside my grasp'), Js('through sands of time'), Js('within this fall'), Js('inside my mind'), Js('among pure bliss'), Js('across the seas'), Js('above the sky')]))
var.put('nm5a', Js([Js('Answer'), Js('Appeal'), Js('Approve'), Js('Asking'), Js('Bargain'), Js('Barter'), Js('Beauty'), Js('Blessings'), Js('Blossoms'), Js('Calming'), Js('Caress'), Js('Challenge'), Js('Changing'), Js('Chasing'), Js('Cleansing'), Js('Contest'), Js('Control'), Js('Cover'), Js('Crumbling'), Js('Dances'), Js('Dreaming'), Js('Drinking'), Js('Eating'), Js('Echoes'), Js('Ending'), Js('Failing'), Js('Falling'), Js('Farming'), Js('Fearing'), Js('Flourish'), Js('Gamble'), Js('Grimace'), Js('Grumble'), Js('Healing'), Js('Herald'), Js('Hinder'), Js('Hustle'), Js('Lament'), Js('Laughing'), Js('Leaving'), Js('Lurking'), Js('Menace'), Js('Morphing'), Js('Murmurs'), Js('Pleading'), Js('Pursuit'), Js('Raining'), Js('Reasons'), Js('Rewards'), Js('Searching'), Js('Shadows'), Js('Sharing'), Js('Shining'), Js('Signals'), Js('Silence'), Js('Singing'), Js('Slumber'), Js('Snowing'), Js('Struggles'), Js('Stumbling'), Js('Teasing'), Js('Triumph'), Js('Twisting')]))
var.put('nm5b', Js([Js('Accusing'), Js('Adapting'), Js('Admiring'), Js('Adoring'), Js('Advising'), Js('Agreeing'), Js('Alerting'), Js('Allowing'), Js('Amusing'), Js('Annoying'), Js('Arguing'), Js('Assuming'), Js('Avoiding'), Js('Awaiting'), Js('Balancing'), Js('Beginning'), Js('Betraying'), Js('Collapsing'), Js('Collecting'), Js('Commanding'), Js('Competing'), Js('Concluding'), Js('Confessing'), Js('Darkening'), Js('Enduring'), Js('Erasing'), Js('Evading'), Js('Evoking'), Js('Expanding'), Js('Forgetting'), Js('Frightening'), Js('Imagine'), Js('Invoking'), Js('Migrating'), Js('Predicting'), Js('Progressing'), Js('Protesting'), Js('Questioning'), Js('Relaxing'), Js('Removing'), Js('Repeating'), Js('Resenting'), Js('Summoning'), Js('Surrender'), Js('Transforming'), Js('Undoing'), Js('Unleashing'), Js('Vanishing'), Js('Wandering')]))
var.put('nm6b', Js([Js('answers'), Js('armies'), Js('balance'), Js('blossoms'), Js('borders'), Js('changes'), Js('comfort'), Js('countries'), Js('creatures'), Js('daydreams'), Js('desire'), Js('evening'), Js('fires'), Js('flowers'), Js('fortune'), Js('gardens'), Js('haven'), Js('heaven'), Js('houses'), Js('insects'), Js('journeys'), Js('knowledge'), Js('laughter'), Js('moments'), Js('morning'), Js('motions'), Js('mountain'), Js('music'), Js('nature'), Js('nightmares'), Js('ocean'), Js('omens'), Js('passion'), Js('pictures'), Js('pleasures'), Js('regrets'), Js('respect'), Js('rhythm'), Js('riddles'), Js('strangers'), Js('summer'), Js('teachings'), Js('thunder'), Js('ventures'), Js('vessel'), Js('voyage'), Js('water'), Js('weather'), Js('winter'), Js('wonders')]))
var.put('first', Js(0.0))
pass
pass


# Add lib to the module scope
haiku = var.to_python()