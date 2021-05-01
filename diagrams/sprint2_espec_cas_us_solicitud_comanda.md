#### Use case name
Solicitar Pedido
-
online
#### Version
1.0.0
#### Date
27/04/2021
#### Description
Gestionar una solicitud d’una comanda per part d’un client a través de l’aplicació. El Banc participa també encarregant-se de gestionar el pagament. 
#### Actors
Client, Banc
#### Preconditions
--
Llistat precondicions, podría
estar buit si fos el cas
--
1. L'usuari ha fet log in accedint correctament al seu compte
2. L’usuari ha afegit els productes que desitja comprar a la cistella
3. L’usuari ha configurat un mètode de pagament al seu compte
4. El producte esta disponible (Hi ha Stock)
 
#### Main Pipeline :
--
Flux principal del cas d ́ús enumerats
--
1. L'usuari clica a finalitzar la comanda a la cistella.
2. Es comprova que el(s) producte(s) estigui(n) en stock.
3. Si el(s) producte(s) esta(n) en stock. Es solicita el pagament per part de l’usuari.
3.1 **Include CU** Pago
4. Si l'usuari demana assistencia per realitzar la comanda.
4.1 **Extend CU** Help
5. Mostrar missatge de gràcies per la compra.
#### Alternative Paths:
--
Fluxos alternatius
--
---
##### Sub
-
Path 1
3. Si el producte no hi ha stock
4. En paral·lel:
4.1. Informem al client de la falta de stock.
4.2. Preguntem si vol continuar amb la compra i li diem la data aproximada d’entrega
4.2.1.Esperem resposta
4.2.2.Enviem notificació a proveïdors
