#### Use case name
Estado del Pedido
-
online
#### Version
1.0.0
#### Date
28/04/2021
#### Description
Seguimiento del pedido desde la solicitud, pasando por la gestión, el envío y la entrega en la ubicación.
#### Actors
GPS,Botiguer,Revisor de pedido, Transportista
#### Preconditions
--
Llistat precondicions, podría
estar buit si fos el cas
--
1. L'usuari ha efectuat una solicitud de comanda
2. La comanda ha estat rebuda i acceptada pel Botiguer
 
#### Main Pipeline :
--
Flux principal del cas d ́ús enumerats
--
1. El Botiguer prepara els productes
2. El Botiguer contacta amb un transportista proper
3. El transportista rep la comanda i troba la ubicació d’entrega a través del GPS
4. El transportista entrega el producte al client
5. Si el Client no està satisfet amb la comanda, solicita una revisió del producte
6. Un Revisor de reembolso revisa els productes entregats i determina si s’accepta retornar-los o no. 
#### Alternative Paths:
--
Fluxos alternatius
--
---
##### Sub
-
 
#### Exception Paths:
--
Excepcions que ens poguem trobar
--
A l'hora de recollir el paquet el transportista, allò que el client va seleccionar es va esgotar a l'stock tant del magatzem com de la pròpia botiga (de la pròpia botiga podria ser just abans). Per tant, haurà de resol·licitar el què volia.
#### Post
-
conditions
--
Llistat post condicions, podría estar buit si fos el cas
--
-
#### Comments
--
Afegir comentari si fos el cas
