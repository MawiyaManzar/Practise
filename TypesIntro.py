class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


''' This is the example of a class used as a types. It is helpful to visualize since in langgraph we use AgentState as a class and 
define the type of state as AgentState'''

#When there is an operation that will require waiting before giving the results and has support for these new Python features, 
# you can code it like:
async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    return burgers

burgers = await get_burgers(2)
'''The key here is the await. It tells Python that it has to wait ⏸ for get_burgers(2) to finish 
doing its thing 🕙 before storing the results in burgers. With that, Python will know that it can go and do something else
🔀 ⏯ in the meanwhile (like receiving another request).


'''
# This won't work, because get_burgers was defined with: async def
burgers = get_burgers(2)

result = await mongoose.connect("url")
#coz of await it first checks the connection is valid or not. if connectn is not valid it will not store in result variable. and therefore the 
#code would stops