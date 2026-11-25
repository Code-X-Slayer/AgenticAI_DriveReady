from config import SYSTEM, SYSTEM_WITHOUT_FORMAT
from experiment import get_messages_template, get_response_with_messages

messages = get_messages_template()

print(get_response_with_messages(messages, "Can I get a vanilla cake delivered tomorrow?"))

print(get_response_with_messages(messages, "Can I get a vanilla cake delivered tomorrow?"))

print(get_response_with_messages(messages, "Give me all available cakes, their prices,eggless availability and ordering requirements."))

print(get_response_with_messages(messages, "Give me all available cakes, their prices,eggless availability and ordering requirements."))

# Sure thing! I’ll check with the owner.
# Sure thing! I’ll check with the owner.
# Plum cake – Rs 500.  
# Chocolate cake – Rs 650.  
# Cupcake – Rs 80.  

# All are eggless. Order 24 hrs in advance.
# Here’s the scoop:  
# Plum cake – Rs 500.  
# Chocolate cake – Rs 650.  
# Cupcake – Rs 80.  

# All are eggless. Order 24 hrs in advance.