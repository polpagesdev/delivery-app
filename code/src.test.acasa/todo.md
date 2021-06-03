### TODO list

1. Donat un client que sol·licita un servei, quan el client no està registrat, retornar URL error
2. Donat un client que sol·licita un servei, quan el client està registrat, retornar URL per demanar autorització
3. Donat un client que sol·licita un servei, quan es fa una petició de connexió, comprovar que es crida a la funció ***request_authentication*** 
  una sola vegada amb els paràmetres adequats
4. Donat un client que sol·licita un servei, quan es fa una petició de connexió, i l'autenticació falla, respondre que la connexió ha estat refusada
5. Donat un client que sol·licita un servei, quan es fa una petició de connexió, i l'autenticació funciona, respondre que la connexió ha estat acceptada
6. Donat un client que sol·licita un servei, quan el client ja està autenticat i el token està vigent, comprovar que es crida a les funcions
   ***get_name***, ***get_total_orders***, ***get_pending_orders*** una sola vegada amb els paràmetres adequats
7. Donat un client que sol·licita un servei, quan es fa una petició de connexió, i l'autenticació falla, comprovar que no es crida a les funcions
   ***get_name***, ***get_total_orders***, ***get_pending_orders*** una sola vegada amb els paràmetres adequats
