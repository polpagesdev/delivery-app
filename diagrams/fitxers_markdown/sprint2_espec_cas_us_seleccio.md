#### Use case name
Selección de pedido
online
#### Version
1.0.0
#### Date
27/04/2021
#### Description
El Usuari esgeix un producte i l’afegeix a la cistella de la compra.
#### Actors
Client
#### Preconditions
--
Llistat precondicions, podría
estar buit si fos el cas
--
1. L'usuari està a la pagina de productes
2. L'usuari ha fet log in accedint correctament al seu compte
#### Main Pipeline :
--
Flux principal del cas d ́ús enumerats
--
1. L'usuari escull un producte.
2. Es comprova que el producte estigui en stock.
3. Si el producte esta en stock. S'afegeix al carret de compra.
 
#### Alternative Paths:
--
Fluxos alternatius
--
---
##### Sub
-
Path 1
3. Si el producte no esta en stock
4. En paral·lel:
4.1. Informem al client que la petició s'esta procesant.
4.2. Busquem fabricants del producte
4.2.1. Enviem notificació a proveïdors.
4.2.2. Esperem resposta
4.2.3. Filtrem el que tinguin millor preu.
4.2.4. Afegim el producte al nostre stock
---
#### Exception Paths:
--
Excepcions que ens poguem trobar
--
El què ha seleccionat el client ja no està disponible o fora d'stock. Haurà d'esperar a que hi hagi. 
#### Post
-
conditions
--
Llistat post
-
condicions, podría estar buit si fos el cas
--
 
#### Comments
--
Afegir comentari si fos el cas
