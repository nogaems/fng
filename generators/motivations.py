__all__ = ['motivations']

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
    var.put('nm1', Js([Js('Find a more interesting life'), Js('Find a thrilling life'), Js('Abandon an ideology'), Js('Answer a call to adventure'), Js('Apologize'), Js('Appease a god'), Js('Appease the gods'), Js('Avenge a family member'), Js('Avenge a friend'), Js('Avoid a person'), Js('Avoid failure'), Js('Avoid responsibilities'), Js('Be a better person'), Js('Be a hero'), Js('Be a master in their field'), Js('Be able to eat'), Js('Be accepted by society'), Js('Be admired'), Js('Be amused'), Js('Be better than their rival'), Js('Be forgiven'), Js('Be in control'), Js('Be left alone'), Js('Be loved'), Js('Be redeemed'), Js('Be remembered'), Js('Be respected'), Js('Be self-sufficient'), Js('Be somebody else'), Js('Be strong'), Js('Be the best they can be'), Js('Become a leader'), Js('Become anonymous'), Js('Become famous'), Js('Become godly'), Js('Become powerful'), Js('Become the strongest'), Js('Belong somewhere'), Js('Better themselves'), Js('Break a habit'), Js('Break an addiction'), Js('Build their own home'), Js('Cause mayhem'), Js('Change a law'), Js('Change the future'), Js('Change the past'), Js("Clear a family member's name"), Js("Clear a friend's name"), Js('Clear their name'), Js('Complete a collection'), Js('Conquer their fear'), Js('Consume everything'), Js('Create a safe world'), Js('Create a utopia'), Js('Create a work of art'), Js('Cure a strange disease'), Js('Destroy corruption'), Js('Destroy evil'), Js('Discover a new planet'), Js('Do nothing'), Js('Do the impossible'), Js('Do the right thing'), Js('Eliminate evil'), Js('End a war'), Js('End suffering of all'), Js('End the conflict'), Js('End the suffering of a family member'), Js('End the suffering of a friend'), Js('Entertain others'), Js('Escape a bad situation'), Js('Escape death'), Js('Escape from their current life'), Js('Escape their destiny'), Js('Establish their own country'), Js('Experience a new culture'), Js('Experience something new'), Js('Explore the oceans'), Js('Explore the unexplored'), Js("Feel like they're worth something"), Js('Fight for their homeland'), Js('Find a cure'), Js('Find a dream job'), Js('Find a job'), Js('Find a legendary creature'), Js('Find a lost friend'), Js('Find a lost lover'), Js('Find a new creative outlet'), Js('Find a new home'), Js('Find a new passion'), Js('Find a purpose'), Js('Find a purpose in life'), Js('Find beauty'), Js('Find excitement'), Js('Find inspiration'), Js('Find love'), Js('Find out a secret'), Js('Find out the fate of a family member'), Js('Find out the fate of a friend'), Js('Find out their true identity'), Js('Find peace within'), Js('Find romance'), Js('Find their muse'), Js('Find true love'), Js('Fix a mistake'), Js('Follow orders'), Js('Forget their past'), Js('Forgive somebody'), Js('Free the animals'), Js('Fulfill a destiny'), Js('Gain the approval of somebody'), Js('Gain what somebody else has'), Js('Get away from their past'), Js('Get rich'), Js('Go on an adventure'), Js('Have a passionate relationship'), Js('Have fun'), Js('Have justice done'), Js('Have more and more'), Js('Have their work recognized'), Js('Have what others have'), Js('Have what they can never have'), Js("Have what they can't have"), Js('Lead a rebellion'), Js('Lift a curse'), Js('Live'), Js('Live a quiet life'), Js('Live dangerously'), Js('Live forever'), Js('Live in peace'), Js('Make a difference'), Js('Make a sacrifice for the greater good'), Js('Make a scientific breakthrough'), Js('Make friends'), Js('Make people smile'), Js('Make sure justice prevails'), Js('More power'), Js('Never be hurt again'), Js('No longer be afraid'), Js('No longer be bored'), Js('Overcome a death sentence'), Js('Overcome a disability'), Js('Overcome mockery from the past'), Js('Overcome stress'), Js('Overthrow the government'), Js('Protect a family member'), Js('Protect a friend'), Js('Protect nature'), Js('Protect the innocent'), Js('Protect the peace'), Js('Protect the planet'), Js('Protect their business'), Js('Protect their family'), Js('Protect their home'), Js('Protect their honor'), Js('Prove a theory'), Js('Prove them wrong'), Js('Reach perfection'), Js('Reach the promised lands'), Js('Reconcile with a person'), Js('Redeem somebody'), Js('Regain their honor'), Js('Remain hidden'), Js('Repay a debt'), Js('Repay a life debt'), Js('Resolve their guilt'), Js('Restart the world'), Js('Retrieve a lost item'), Js('Retrieve a stolen item'), Js('Reunite with a family member'), Js('Reunite with a lost friend'), Js('Revenge'), Js('Rid the world of evil'), Js('Rule the city'), Js('Run for the borders'), Js('Satisfy their curiosity'), Js('Save Christmas'), Js('Save a deity'), Js('See others suffer'), Js('See the gods pay for their crimes'), Js('See the world'), Js('Solve a mystery'), Js('Solve an ancient mystery'), Js('Spread chaos'), Js('Spread joy'), Js('Spread their ideology'), Js('Stand out from the crowd'), Js('Start a business'), Js('Start a family'), Js('Start a new world'), Js('Stop a criminal'), Js('Take a new direction in life'), Js('Thwart destiny'), Js('To fit in'), Js('Travel back into the past'), Js('Travel in space'), Js('Travel into the future'), Js('Uncover a secret plot'), Js('Win a competition'), Js('Win a game'), Js('Write a book')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+Js('.')))
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
motivations = var.to_python()