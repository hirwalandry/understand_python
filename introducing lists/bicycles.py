bicycles =  ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#Accessing Elements in a List
print(bicycles[0].title())
print(bicycles[-1].title())
#Using Individual Values from a List You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create a message based on a value from a list. Let’s try pulling the first bicycle from the list and composing a message using that value. 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
