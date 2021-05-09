#### Use case name
Recibir Pedido
-
online
#### Version
1.0.0
#### Date
27/04/2021
#### Description
L’usuari rep el producte a la ubicació seleccionada (ex: domicili)
#### Actors
Client, Revisor reemborsament
#### Preconditions
--
Llistat precondicions, podría
estar buit si fos el cas
--
1. L'usuari te una comanda en curs
2. El botiguer ha rebut el pagament
3. El transportista va a l’ubicació designada amb els productes
 
#### Main Pipeline :
--
Flux principal del cas d ́ús enumerats
--
1. L'usuari recull la comanda amb els productes.
2. Si el Revisa i desitja retornar el producte
2.1 **Extend CU** Solicitar Revisión
3. **Extend CU** Valoración 
#### Alternative Paths:
--
Fluxos alternatius
--
---
##### Sub
-
Path 1
##### Sub
---
Excepcions que ens poguem trobar
--
La comanda és rebuda, però es errònia. Haurà de demanar revisió.
#### Post
-
conditions
--
Llistat post condicions, podría estar buit si fos el cas
--
-
3. ...
#### Comments
