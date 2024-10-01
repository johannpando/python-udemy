"""
En este notebook comenzamos a trabajar en los problemas de Clasificación, una de las tareas más importantes dentro de Machine Learning (dentro, a su vez, de lo que llamamos Aprendizaje Supervisado). Clasificación en Machine Learning consiste en aprender etiquetas discretas "y" a partir de un conjunto de features "X" (que pueden ser uno, dos, o muchos más) tomando como muestra un conjunto de instancias.

En este notebook trabajaremos con uno de los modelos fundamentales de Machine Learning: Árboles de Decisión. Para ello, usaremos el dataset de Titanic y la librería Scikit-Learn. Debido a la implementación orientada a objetos de Scikit-Learn, todos los modelos se entrenan y se usan de la misma forma.

Recuerda que todas las librerías fueron desarrolladas por personas, que en búsqueda de resolver una necesidad de cómputo, escribieron el código que hoy podemos reutilizar para poder poner directamente manos a la obra en lugar de tener que desarrollarlo y optimizarlo una y otra vez. Sin embargo, la idea que quiero transmitirte es que puedes hacer el intento de escribir tú mismo las funciones y clases que importaremos de las librerías. Si bien no es lo habitual y desde luego consumirá mucho más tiempo, este trabajo te permitirá comprender nuevos detalles acerca de lo que estás haciendo.

El dataset de Titanic es famoso entre los estudiantes de Data Science. El mismo ha surgido de una competencia en el sitio Kaggle: Machine Learning from Disaster. Veremos una implementación muy sencilla acerca de un posible abordaje para resolverlo, partiendo también de una versión simplificada y filtrada del dataset original de dicha competencia.

Nuestro Dataset está compuesto por una serie de columnas, que tienen los siguientes significados:

Sobreviviente: 0 = No; 1 = Si
Clase: 1 = Primera Clase; 2 = Segunda Clase; 3 = Tercera Clase
Género: 0 = Hombre; 1 = Mujer
Edad: edad en años
HermEsp: cantidad de hermanos o esposos a bordo del Titanic, para el pasajero en cuestión
PadHij: cantidad de padres o hijos a bordo del Titanic, para el pasajero en cuestión
Ejercicio: Carga el dataset de Titanic y tomate un rato para estudiar sus características.
"""

