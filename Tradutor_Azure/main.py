from translate import translate


texto = """Marvin is a diligent policeman. 
He loves his job and carries out his duties. 
It is summertime, and his team is starting a fire prevention program. 
Marvin is tasked to promote ways to avoid fire incidents. 
He reminds residents to always unplug appliances. 
He tells children not to play with matches. 
He talks to parents about turning off stoves and heaters when not in use. 
He gives safety tips to anyone who asks. 
Marvin is doing a great job. 
One morning, there is an emergency meeting. 
Quite alarmed, Marvin leaves his unfilled coffee cup and quickly goes to work. 
After work, Marvin arrives to find his house on fire. Stunned and confused, Marvin asks the fireman about what happened. 
The fireman replies, "It’s because the homeowner forgot to turn off the stove."
"""

traducao = translate(texto,'en','pt')

print("*** Texto original ***\n",texto)
print("\n*** Texto traduzido ***\n",traducao)


