Notas

regla de oro” para la cuestión de las vistas , por si te estas sumergiendo en django -REST y no sabes que tipo de vista usar:
- ViewSet: cuando usamos la mayoria de operaciones crud en un modelo

- Generics: cuando solo desee permitir algunas operaciones en un modelo

- ApiView :cuando desee personalizar completamente las operaciones de un modelo.

espero les sirva como una guia , mas no una regla


### Api rest:
######  Renderes
Se encargan de como esta saliendo el contenido y basan como sale ese contenido en el header accept. Django rest posee distintos tipos de render includo Latex, como third party packages

- Importa el orden de los renders segun la configuracion que se reciba


### Autenticación y tipos de autenticación
