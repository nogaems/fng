__all__ = ['slogans']

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
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('A moment of harmony'), Js('A slice of heaven'), Js('A solid foundation'), Js('Ahead of our time'), Js('All as one'), Js('Always in front'), Js('Art of excellence'), Js('Art of perfection'), Js('As always'), Js('Baby steps'), Js('Be better'), Js('Be bold'), Js('Be cool'), Js('Be more'), Js('Be stronger'), Js('Be the best'), Js('Be the best you can be'), Js('Be the change'), Js('Be the leader'), Js('Be the power'), Js('Be the revolution'), Js('Beautiful experiences'), Js('Beauty of simplicity'), Js('Because diamonds are forever'), Js("Because you're special"), Js('Become your best'), Js('Before you know it'), Js('Best performance'), Js('Better care, better life'), Js('Better standards'), Js('Beyond boundaries'), Js('Beyond comfort'), Js('Beyond perfection'), Js('Beyond the limit'), Js('Beyond the sky'), Js('Bigger by being smaller'), Js('Bite sized business'), Js('Blissful knowledge'), Js('Born for success'), Js("Bottom's up"), Js('Bring it on'), Js('Bringing solutions'), Js('Building the future'), Js('Change a life'), Js('Change the future'), Js('Changing tomorrow'), Js('Comfort in our hands'), Js('Comfort of your home'), Js('Creative solutions'), Js('Dare to be'), Js('Designed for you'), Js('Doing the impossible'), Js('Driven to perfection'), Js('Easy as can be'), Js('Empower you'), Js('Endless possibilities'), Js('Enjoy'), Js('Eternal pursuit'), Js('Everybody needs a break'), Js('Expanding horizons'), Js('Expect excellence'), Js('Experience in our hands'), Js('Experience is key'), Js('Fit for a king'), Js('Fit for a queen'), Js('Follow the leader'), Js('For champions'), Js('For love'), Js('For the good times'), Js('For those who care'), Js('Going the extra mile'), Js('Hand in hand'), Js('Hearts united'), Js('Hold the power'), Js('Imagination at work'), Js('Imagine the impossible'), Js('Imagine this'), Js('Imagine tomorrow'), Js('Improved happiness'), Js('Infinite possibilities'), Js("It's in your hands"), Js("It's on"), Js("It's on us"), Js("It's our business"), Js("It's our passion"), Js("It's our pleasure"), Js("It's time"), Js("It's your choice"), Js('Just enjoy'), Js('Just for you'), Js('Just imagine'), Js('Just relax'), Js('Just the beginning'), Js('King and queen'), Js('Lead the way'), Js('Life experience'), Js('Life without strife'), Js('Limitless'), Js('Listen'), Js('Little miracles'), Js('Little pleasures, great joys'), Js('Live in the moment'), Js('Live today, dream of tomorrow'), Js('Live your dreams'), Js('Live. Love. Play'), Js('Long endurance'), Js('Love of life'), Js('Make it happen'), Js('Mark of excellence'), Js('Mastered perfection'), Js('Maximize life'), Js('Moments of bliss'), Js('Moments of clarity'), Js('More than just a taste'), Js('Moving forwards'), Js('Moving mountains'), Js('Never stop dreaming'), Js('No problem'), Js('Nothing beats the best'), Js("Nothing's better"), Js("Now's the time"), Js('Obsession for details'), Js('On the front line'), Js('One step at a time'), Js('Only the best'), Js('Onward'), Js('Open your eyes to the possibilities'), Js('Opening doors'), Js('Outside the box'), Js('Powered by you'), Js('Pure delight'), Js('Push the boundaries'), Js('Pushing the limits'), Js('Quality first'), Js('Raising the bar'), Js('Recipe for success'), Js('Redefining the box'), Js('Redefining impossible'), Js('Relax, we got this'), Js('Relive the moment'), Js('Remember'), Js('Road to success'), Js('See you next time'), Js('Sheer pleasure'), Js("Shh, it's a secret"), Js('Simplicity'), Js('Simply outstanding'), Js('Simply perfection'), Js('Smile'), Js('Standards of excellence'), Js('Standing out'), Js('Success'), Js('Surprise'), Js('The future'), Js('The good feeling'), Js('The next generation'), Js('The other side'), Js('The possibilities are endless'), Js('The show goes on'), Js("The sky's not the limit"), Js("The sky's the limit"), Js('The time is now'), Js("There's nothing else like it"), Js("There's nothing like it"), Js('Think about it'), Js('Think creative'), Js('Think positive'), Js('Thinking ahead'), Js('Thinking solutions'), Js('To the extreme'), Js('Trial and success'), Js('True sensations'), Js('Trust us'), Js('Unbreakable bonds'), Js('Unbreakable spirit'), Js('Unbroken promises'), Js('Uniquely the best'), Js('Unleash the power'), Js('We are one'), Js('We believe'), Js('We believe in you'), Js('We care'), Js('We have your back'), Js('We keep our promises'), Js('We never stop'), Js('We promise the best'), Js('We provide excellence'), Js("We won't contain it"), Js("We're forever"), Js("We're here for you"), Js("We've got you covered"), Js('Welcome'), Js('Welcome back'), Js('With love'), Js('With pleasure'), Js('With style'), Js('With you for life'), Js('Work hard. Play harder'), Js('You come first'), Js('Your wish is our command')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+Js('.')))
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
slogans = var.to_python()