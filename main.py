
__author__="christian ramon rodriguez"
__date__ ="$23/08/2011 08:09:00 PM$"

import Persona
import Vaso

personas = [Persona.Persona('Chris'),Persona.Persona('Larry'),Persona.Persona('Steph'),Persona.Persona('serial Killer!')]
vaso = Vaso.Vaso(len(personas))
print "Envenenar vaso!"
envenenado = personas[0].envenenarVaso(len(personas))

for p in personas:
    print p.name+" : "+p.beberVaso(vaso.getCantidad(), envenenado)
    vaso.reducirCantidad()
    




    
