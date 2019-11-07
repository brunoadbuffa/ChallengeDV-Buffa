# ChallengeDV-Buffa
Challenge sobre k-means++. 

El archivo *respuestas.txt* contiene las respuestas a las consignas planteadas en el challenge y el archivo *challengeBUFFA.py* contiene el código python donde se implenta al algoritmo requerido.

## Utilización del módulo de Python "challengeBUFFA".

En el módulo de Python llamado *challengeBUFFA.py* se encuentra la función **k_meansMODIF** la cual es una implementación del algoritmo denominado **k-means++** (Ref: [Arthur, D. and Vassilvitskii, S. (2007). "k-means++: the advantages of careful seeding"](http://ilpubs.stanford.edu:8090/778/1/2006-13.pdf)). 

Dicho algoritmo es una mejora del clásico algoritmo de k-means. La diferencia entre ellos radica en que **k-means** clásico elije los valores iniciales para los centroides de manera aleatoria entre los datos proporcionados por el usuario y **k-means++** lo hace mediante el método denominado por los autores como *D² weighting*. Esta forma innovadora para definir los primeros centroides consiste en, luego de elegir el primer centroide al azar, ir tomando el resto de los centroides de entre el conjunto de datos con probabilidad directamente proporcional a la distancia de cada dato respecto al centroide más cercano que ya esté calculado. La principal ventaja de este cambio en la inicialización del algoritmo de k-means es que se consigue que el valor esperado del potencial (**_P_**) dado por la solución de nuestro algoritmo está acotado por **_C_**  **_ln(k)_**   **_P-OPT_** donde **_C_** es alguna constante y **_P-OPT_** es el potencial óptimo que se puede obtener. En efecto, se puede demostrar que se cumple la siguiente desigualdad: **E[_P_] < 8 (_ln(k)_ + 2) _P-OPT_**, o sea. k-means++ es **O(_ln(k)_)-Competitivo**

La función k_meansMODIF(_X, k, tol=1e-4, n-iter=50_) se utiliza con 4 argumentos, los últimos dos son opcionales. 
#### Parámetros de la funcióm k_meansMODIF:

**_X_**: Arreglo de dos dimensiones con *n_samples* filas y *n_dim* columnas donde se espera que sus filas sean los datos a los que se les quiere hacer clustering.

**_k_**: Número de clusters o centroides que se desean obtener luego de aplicarle el algoritmo a los datos en $X$.

**_tol_**: Criterio de parada del algoritmo por *tolerancia*. Se calcula la diferencia entre la suma total de las distancias a los centroides en pasos sucesivos y si el resultado es menor a *$tol$*, se frena el algoritmo.

**_n-iter_**: Número máximo de iteraciones que puede realizar el algoritmo.

Nota: Para utilizar el módulo "challengeBUFFA" se debe contar con Python 3 y los paquetes `SciPy` y `NumPy`. Si no se dispone de ellos, en este repositorio se incluye el archivo env.yml para crear un entorno virtual -mediante el gestor 'conda'- que dispone de todos los paquetes necesarios para correr dicho módulo.
