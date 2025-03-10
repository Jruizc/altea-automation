# altea-automation

Instalar selenium

pip install selenium


Instalar behave

pip install behave

Descargar la version de chromedriver que coincida con tuversión de chrome

https://developer.chrome.com/docs/chromedriver/downloads?hl=es-419

Para ejecutar las las pruebas ejectuamos el siguiente comando desde el directorio del proyecto

behave features/busqueda.feature --no-capture

Estructura del proyecto

En el directorio configuration se encuentra la configuración basica del proyecto, donde se encuentran los archivos y recursos que se necesitan.

En Features se encuentran los archivos de cucumber, los hooks y los ficheros steps.

En Pages contienen los elementos y las acciones que hace cada página