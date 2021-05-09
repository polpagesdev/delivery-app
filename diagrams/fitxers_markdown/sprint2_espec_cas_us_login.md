#### Use case name
Log-in
-
online
#### Version
1.0.0
#### Date
28/04/2021
#### Description
L’Usuari accedeix al seu compte per poder accedir a totes les funcions de la aplicació. Un cop inciada la sessió es redirigeix a la Home Page.
#### Actors
Cliente, Botiguer, Servicios de Google, Transportista, Mantenimiento
#### Preconditions
--
Llistat precondicions, podría
estar buit si fos el cas
--
1. L'usuari està registrat a la aplicació
 
#### Main Pipeline :
--
Flux principal del cas d ́ús enumerats
--
1. L'usuari inicia sessió a través dels serveis de comptes de google
2. Si es el primer cop es demana introduir correu i contrasenya per registrar-se.
2.1 **Extend CU** Registro
2.2 S’envia un correu de confirmació a l’adreça introduïda.
#### Alternative Paths:
--
Fluxos alternatius
--
---
##### Sub
-
Path 1
#### Exception Paths:
--
Excepcions que ens poguem trobar
--
La plataforma pot estar inoperativa. Per tant, manteniment haurà d'arreglar-lo.
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
