# Enhanced Touch Gestures #

* Autor: Joseph Lee

Este complemento proporciona gestos táctiles adicionales para NVDA. También
proporciona un conjunto de gestos para una mejor navegación del modo
exploración.

Nota: este complemento requiere NVDA 2024.1 o posterior ejecutándose en un
ordenador con pantalla táctil con Windows 10 o 11.

## Órdenes

### Disponible desde cualquier lugar

* Doble toque con 4 dedos: conmuta el modo de ayuda de entrada.
* Deslizamiento a la derecha con cuatro dedos: conmuta el teclado táctil
  (normalmente lo activa).
* Desplazamiento con cuatro dedos a la izquierda: conmutar dictado
  (Windows+h; Windows 10 versión 1709 o posterior).

### Modo Objeto

* Deslizar 3 dedos hacia abajo: leer ventana actual.
* Deslizar 3 dedos a la izquierda: anunciar objeto con el foco.
* Deslizar 3 dedos a la derecha: anunciar actual navegador de objetos.
* deslizar 4 dedos hacia arriba: anunciar el título de la ventana actual.
* Deslizar 4 dedos hacia abajo: anunciar texto de la barra de estado.

## Modo Web táctil

Este modo táctil, disponible en modo exploración, te permite navegar el
documento por elementos seleccionados. Para cambiar a modo web, desde
documentos de modo exploración, realiza un toque con 3 dedos. Desde este
modo, desliza arriba o abajo con un dedo cíclicamente a través de los modos
de navegación disponibles, mientras que deslizando a la derecha o a la
izquierda con un dedo te mueves al elemento siguiente o al anterior,
respectivamente. Una vez te salgas de los documentos en modo exploración, se
utiliza el modo táctil objeto.

## Modo táctil de opciones del sintetizador

Puedes utilizar este modo para cambiar cíclicamente las opciones del
sintetizador tales como la elección de una voz y el cambio del volumen. En
este modo, utiliza el deslizamiento de dos dedos hacia la izquierda o la
derecha para moverte entre opciones del sintetizador y utiliza gestos de
deslizamiento de dos dedos arriba y abajo para cambiar los valores. Estos
gestos se reflejan en las órdenes del grupo de opciones del sintetizador del
teclado.

## Versión 25.07

* Se ha hecho el código del complemento más robusto con la ayuda de Pyright
  (un comprobador de tipado estático de Python).

## Versión 25.02

* Se restaura el soporte limitado para Windows 8.1.

## Versión 25.01

* Ya no se incluyen enlaces de descarga de versiones del complemento en su
  documentación. Puedes descargar el complemento desde la tienda de
  complementos de NVDA.
* Se cambia la herramienta de calidad del código de Flake8 a Ruff y se
  reformatean los módulos del complemento para alinearse mejor con los
  estándares de codificación de NVDA.
* Se elimina el soporte de actualizaciones automáticas del complemento
  Add-on Updater.

## Versión 24.05

* Se requiere NVDA 2024.1 o posterior.

## Versión 23.06.1

* se ha movido la atenuación de audio a un toque con 4 dedos debido a un
  conflicto con la orden que detiene la voz de NVDA.

## Versión 23.06

* El complemento para NVDA Enhanced Touch Gestures es mantenido ahora por
  Kefas Lungu.
* Todos los gestos del modo objeto están ahora disponibles en todas partes.
* Ahora hay nuevos gestos disponibles.

  * Doble toque con 3 dedos: alterna entre niveles de pronunciación de
    símbolos, que determinan qué símbolos se verbalizan
  * Triple toque con 2 dedos: ¡Salir de NVDA!.
  * Toque con 4 dedos: alterna entre modos de atenuación de audio.
  * Toque triple: alterna entre pitidos, hablar, pitidos y hablar, y
    desactivado.

* En el modo web, ahora es posible usar botones, gráficos y regiones además
  de la lista de elementos de exploración ya disponible.
* En el modo web, NVDA ya no va a decir normal, sino predeterminada, al
  cambiar a la navegación predeterminada desde otra lista de elementos de
  exploración. Por ejemplo, al cambiar desde botones, NVDA ahora dirá
  predeterminada.

## Versión 23.02

* Se requiere NVDA 2022.4 o posterior.
* Se requiere Windows 10 21H2 (actualización de noviembre de 2021 /
  compilación 19044) o posterior.

## Versión 23.01

* Se requiere NVDA 2022.3 o posterior.
* Se requiere Windows 10 o posterior, ya que Microsoft no soporta Windows
  8.1 a partir de enero de 2023.
* Es posible reasignar las órdenes de conmutación de dictado y teclado
  táctil desde el diálogo Gestos de entrada, bajo la categoría Enhanced
  Touch Gestures.
* Se ha eliminado la solución provisional de estado de sólo lectura de las
  teclas del teclado táctil, ya que está resuelto en Windows 10.

## Versión 22.03

* Se requiere NVDA 2021.3 o posterior.
* Se mostrará un mensaje de aviso al intentar instalar el complemento en
  Windows 7, 8 y 8.1.

## Versión 21.10

* Se requiere NVDA 2021.2 o posterior a causa de cambios en NVDA que afectan
  a este complemento.

## Versión 21.08

* Soporte inicial para Windows 11.

## Versión 21.01

* Se requiere NVDA 2020.3 o posterior.
* En Windows 10 versión 1709 y posterior, haciendo un desplazamiento con
  cuatro dedos hacia la izquierda se conmutará el dictado (Windows+H).
* Se elimina la orden dedicada de conmutación del soporte de interacción
  táctil del complemento.
* Ya que el soporte de interacción táctil se puede conmutar desde el panel
  de opciones de interacción táctil de NVDA, se ha eliminado un panel
  dedicado de opciones de Enhanced Touch Gestures.

## Versión 20.09

* Se ha eliminado la capacidad de que NVDA desactive la interacción táctil
  durante un máximo de diez segundos (dejar pasar las órdenes táctiles).
* Se ha eliminado la función de anuncio de coordenadas mediante pitidos.

## Versión 20.07

* Se ha añadido una orden de teclado para conmutar la interacción táctil o
  activar / desactivar dejar pasar los toques (Control+alt+NVDA+t).
* Ya que NVDA 2020.1 y posterior incluye una orden táctil para hacer clic
  con el botón derecho del ratón (pulsar y mantener con un dedo), se ha
  eliminado dicha orden de este complemento. Como resultado, se requiere
  NVDA 2020.1 o posterior.
* La capacidad para hacer que NVDA desactive la interacción táctil durante
  un máximo de diez segundos (dejar pasar órdenes táctiles) está
  obsoleta. En el futuro, esta orden conmutará la interacción táctil en su
  lugar.
* En las versiones de desarrollo de NVDA, debido a los cambios en las
  funciones de interacción táctil, se deshabilitarán los paneles de opciones
  de Enhanced Touch Gestures y la función de dejar pasar las órdenes
  táctiles. La orden para activar la función de dejar pasar órdenes táctiles
  conmutará la interacción táctil en su lugar.
* La función de pitido de anuncio de coordenadas está obsoleto y se
  eliminará en una versión futura del complemento.
* No se escuchará el pitido de anuncio de coordenadas mientras se use el
  teclado táctil.
* NVDA ya no parecerá hacer nada o reproducir tonos de error al explorar los
  métodos modernos de entrada, como el panel de emojis, mediante el tacto.
* NVDA presentará un mensaje de error si no se puede activar el teclado
  táctil (desplazamiento de cuatro dedos a la derecha).

## Versión 20.06

* Se han resuelto muchos problemas de estilo del código y fallos potenciales
  con Flake8.

## Versión 20.04

* El gesto de clic con el botón derecho del ratón (pulsar y mantener con un
  dedo) ahora forma parte de NVDA 2020.1.

## Versión 20.01

* Se requiere NVDA 2019.3 o posterior.
* La orden para conmutar el soporte táctil (incluyendo dejar pasar el
  siguiente toque) ya no funcionará si el soporte táctil se desactiva
  completamente.

## Versión 19.11

* Se han añadido mensajes de ayuda de entrada para las órdenes táctiles
  adicionales.

## Versión 19.09

* Ahora se puede desactivar el soporte táctil desde cualquier lugar, y no
  sólo en perfiles distintos al perfil normal.

## Versión 19.07

* Cambios internos para dar soporte a versiones futuras de NVDA.

## Versión 18.12

* Cambios internos para dar soporte a versiones futuras de NVDA.

## Versión 18.08

* Compatible con NVDA 2018.3 y versiones futuras.

## Versión 18.06

* La configuración del complemento ahora se encuentra en la nueva pantalla
  multicategoría Opciones de NVDA en la categoría "Enhanced Touch
  Gestures". A consecuencia de ello, se requiere de NVDA 2018.2.
* Corregidos los problemas de compatibilidad con wxPython 4.

## Versión 18.04

* Resuelto un error que podía causar la reproducción de sonidos de error en
  la categoría de Interacción táctil en el panel de preferencias de NVDA
  debido a cambios hechos por este complemento.

## Versión 18.03

* Se requiere NVDA 2018.1.
* Debido a que NVDA 2018.1 viene con una casilla de verificación Escritura
  Táctil, ésta no se incluye ya en este complemento.

## Versión 17.12

* Se requiere de NVDA 2017.4. Específicamente, este complemento ahora puede
  manejar cambios de perfil de configuración.
* Dado que NVDA 2017.4 incluye el anunciado de horientación de la pantalla,
  esta característica ya no forma parte de este complemento.
* Añadida una casilla de verificación oculta en el diálogo Interacción
  Táctil para desactivar completamente el soporte táctil (disponible si los
  perfiles distintos a la configuración normal están activos).
* Si se utiliza NVDA 2018.1 en adelante, el diálogo Interacción Táctil se
  listará dos veces en el menú Preferencias de NVDA. El segundo elemento es
  el diálogo que viene con el complemento.
* En el diálogo Interacción Táctil para el complemento, el modo de escritura
  táctil ya no se muestra si se usa NVDA 2018.1 en adelante.

## Versión 17.10

* Debido a políticas de soporte de Microsoft, Windows 8 (versión original)
  ya no se soporta.
* NVDA ya no anunciará la orientación de la pantalla dos veces al ejecutar
  snapshots de desarrollo de NVDA 2017.4.

## Versión 17.07.1

* Añadida una opción en el diálogo Interacción táctil para conmutar
  manualmente dejar pasar un toque sin utilizar un temporizador.
* Con el modo dejar pasar manual desactivado, si dejar pasar toques está
  activado antes de que expire la duración de dejar pasar, la interacción
  táctil debería habilitarse.

## Versión 17.07

* Añadido un diálogo nuevo llamado Interacción Táctil en el menú
  Preferencias de NVDA para configurar cómo trabaja NVDA con las pantallas
  táctiles.
* Después de instalar esta versión, al pulsar teclas en el teclado táctil,
  se debe hacer doble toque en la tecla deseada. Puedes volver al modo
  antiguo habilitando la escritura táctil desde el diálogo Interacción
  Táctil.
* Añadida una orden (no asignada) para permitir a NVDA ignorar gestos
  táctiles por hasta 10 segundos.
* Añadida una opción en el diálogo Interacción Táctil para permitir a NVDA
  pausar la interacción táctil entre 3 y 10 segundos para realizar gestos de
  la pantalla táctil directamente (tal como si NVDA no está en ejecución;
  por defecto es 5 segundos).
* Añadidos mensajes de depuración en el registro al realizar clic derecho
  (tocar y mantener) para grabarlos en el registro de NVDA (requiere de NVDA
  2017.1 o posterior).
* Debido a cambios hechos al reproducir las coordenadas de la pantalla, se
  requiere de NVDA 2017.1 o posterior.

##Versión 17.03

* Corregido un fallo cuando el pitido de anunciado de coordenadas no se
  reproducía o se reproducía un tono de error en su lugar cuando se utiliza
  NVDA 2017.1 o anterior.

##Versión 16.12

* El modo web táctil funciona en Microsoft Edge, Microsoft Word y otros
  donde se utilice el modo exploración.
* Añadidas listas y puntos de referencia a los elementos del modo web
  táctil.

## Versión 16.06

* Versión estable inicial.

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
