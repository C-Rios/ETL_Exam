<div align="center">

 <h1>Parcial 2 – Big Data e Ingeniería de Datos</h1>
 
 <p>Universidad Sergio Arboleda</p>
 
 <p>Escuela de Ciencias Exactas e Ingeniería</p>

 <p>Ingeniería en Ciencias de la Computación e Inteligencia Artificial</p>

 <p>Big Data e Ingeniería de Datos</p>

 <b>Presentan: Juan Camilo De Los Ríos Hernández y Roxanyffer Andreina Velasco Contreras</b>

</div>

</br>

## Introducción

Bajo la premisa del proceso realizado se puntualiza que en este trabajo se desarrollaron los ETL (Extract, Transform and Load) y un Workflow en AWS Glue para la descarga de información de los periódicos El Tiempo y El Espectador. Se crearon dos jobs en AWS Glue, uno que descarga cada día la página principal de los periódicos y otro que procesa los datos utilizando Beautifulsoup, extrayendo la categoría, titular y enlace para cada noticia. Los datos fueron guardados en un CSV en una ruta específica en S3 y se activó un crawler que actualizó el catálogo de AWS Glue para permitir la visualización de los datos en AWS Athena. Por último, se creó un job que inserta la información en una base de datos MySQL utilizando AWS Glue Connectors y AWS Job.



 

## Desarrollo

Se creó un Job en AWS Glue que descarga cada día la página principal de los periódicos El Tiempo y El Espectador. La información quedó en S3 con la estructura s3://bucket/headlines/raw/contenido-yyyy-mm-dd.html. Se activó un segundo job que procesó los datos utilizando Beautifulsoup y se guardaron los datos en un CSV en la siguiente ruta: s3://bucket/headlines/final/periodico=xxx/year=xxx/month=xxx/day=xxx. Se activó un crawler que actualizó el catálogo de AWS Glue y permitió visualizar los datos en AWS Athena.

Para insertar la información en una base de datos MySQL, se creó la BD de MySQL en RDS con la respectiva tabla, se mapeó con un crawler al catálogo del Glue y se creó el job con la interfaz que copió de tabla a tabla (la que representa S3 y la que representa RDS en el catálogo). Se activó la opción “job bookmarks” cuando se creó el job por interfaz.

Para el control de versiones del código y el despliegue continuo, se utilizó GitHub y se creó un pipeline de despliegue continuo para los scripts de los jobs.
 

## Conclusión

A modo de conclusión, el desarrollo de los ETL y Workflow en AWS Glue para la descarga de información de periódicos El Tiempo y El Espectador es un proceso que involucra varias etapas. Desde la descarga de la información hasta la inserción en una base de datos MySQL, se siguieron ciertos pasos y se consideraron varias opciones para garantizar el éxito del proceso. Además, el control de versiones y el despliegue continuo son herramientas importantes para mantener un flujo constante de trabajo y evitar errores en el código.