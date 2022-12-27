# Giving a function an alias
from MProg1_Func2_pizza import *
from MProg1_Func2_pizza import build_profile1 as p

make_pizza('medium', 'pepperoni')
make_pizza('small', 'bacon', 'pineapple')



# Create two users with different kinds of information.
user_0 = p.build_profile1('albert', 'einstein', location='princeton')
user_1 = p.build_profile1('marie', 'curie',  location='paris', field='chemistry')
print(user_0)
print(user_1)