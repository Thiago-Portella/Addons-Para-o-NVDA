# Enhanced Touch Gestures #

* Autor: Joseph Lee

Este complemento proporciona xestos táctiles adicionais para NVDA. Tamén
proporciona un conxunto de xestos para unha mellor navegación do modo
exploración.

Note: this add-on requires NVDA 2024.1 or later running on a touchscreen
computer with Windows 10 or 11.

## Ordes

### Dispoñible dende calquera lugar

* Doble toque con 4 dedos: conmuta o modo de axuda de entrada.
* Deslizamento de catro dedos cara a dereita: conmuta o teclado tactil
  (normalmente actívao).
* Barrido con catro dedos á esquerda: alternar dictado (Windows+H); Windows
  10 versión 1709 ou posterior.

### Modo Obxecto

* Deslizar 3 dedos cara abaixo: ler ventá actual.
* Deslizar 3 dedos á esquerda: anunciar obxecto co foco.
* Deslizar 3 dedos á dereita: anunciar actual navegador de obxectos.
* deslizar 4 dedos cara arriba: anunciar o título da ventá actual.
* Deslizar 4 dedos cara abaixo: anunciar texto da barra de estado.

## Modo Web táctil

Este modo táctil, dispoñible no modo exploración, permíteche navegar o
documento por elementos seleccionados. Para cambiar a modo web, dende
documentos de modo exploración, realiza un toque con 3 dedos. Dende este
modo, desliza arriba ou abaixo cun dedo cíclicamente a través dos modos de
navegación dispoñibles, mentras que deslizando á dereita ou á esquerda cun
dedo móveste ó elemento seguinte ou ó anterior, respectivamente. Unha vez
saias dos documentos en modo exploración, utilízase o modo táctil obxeto.

## Modo táctil de opcións do sintetizador

Podes utilizar este modo to cambiar cíclicamente as opcións do sintetizador
como a elección dunha voz e o cambio do volume. Neste modo, utiliza o
desprazamento con dous dedos á esquerda e aá dereita para te mover entre
opcións do sintetizador e utiliza os xestos de desprazar dous dedos cara
arriba e cara abaixo para cambiar os valores. Estos xestos refrexan as ordes
do grupo de opcións do sintetizador no teclado.

## Version 25.07

* Made the add-on code more robust with help from Pyright (a Python static
  type checker).

## Version 25.02

* Restored limited support for Windows 8.1.

## Version 25.01

* Download links for add-on releases are no longer included in add-on
  documentation. You can download the add-on from NV Access add-on store.
* Switched linting tool from Flake8 to Ruff and reformatted add-on modules
  to better align with NVDA coding standards.
* Removed support for automatic add-on updates feature from Add-on Updater
  add-on.

## Version 24.05

* NVDA 2024.1 or later is required.

## Version 23.06.1

* audio ducking moved to 4 finger tap due to conflict with speech stops NVDA
  command.

## Version 23.06

* Enhanced Touch gestures nvda-addon is now maintained by Kefas Lungu.
* All gestures in object mode are now available everywhere.
* New gestures are now available.

  * 3 finger double tap: Cycles through speech symbol levels which determine
    what symbols are spoken
  * 2 finger tripple tap: Quit NVDA!.
  * 4 finger tap: Cycles through audio ducking modes.
  * Triple tap: Toggles between beeps, speech, beeps and speech, and off.

* In web mode, it is now possible to Use buttons, graphics, and landmarks in
  addition to the already available browse element list.
* In web mode, NVDA is no longer going to say normal, but default when you
  switch to default navigation from other browse element list. For example,
  when switching from buttons, NVDA will now say default.

## Versión 23.02

* Require NVDA 2022.4 ou posterior.
* Requírese Windows 10 21H2 (Actualización de novembro de 2021/compilación
  19044) ou posterior.

## Versión 23.01

* Require NVDA 2022.3 ou posterior.
* Requírese Windows 10 ou posterior xa que Windows 7, 8, e 8.1 xa non se
  soportan dende Microsoft dende xaneiro do 2023.
* É posible reasignar as ordes de alternar o teclado táctil e o dictado
  dende o diálogo de xestos de entrada baixo a categoría Enhanced Touch
  Gestures.
* Eliminado o método para superar o estado de só lectura para as teclas do
  teclado táctil, xa que se resolveu en Windows 10.

## Versión 22.03

* Require NVDA 2021.3 ou posterior.
* Amosarase unha mensaxe de advertencia ao tentar instalar o complemento en
  Windows 7, 8, e 8.1.

## Versión 21.10

* Requírese NVDA 2021.2 ou posterior debido a cambios en NVDA que afectan a
  este complemento.

## Versión 21.08

* Soporte inicial para Windows 11.

## Versión 21.01

* Require NVDA 2020.3 ou posterior.
* En Windows 10 versión 1709 e posterior, facendo un barrido con catro dedos
  á esquerda alternarase o dictado (windows+H).
* Eliminado o xesto dedicado para alternar o soporte para interacción táctil
  do complemento.
* Xa que o soporte para interacción táctil pode activarse e desactivarse
  dende o panel de interacción táctil de NVDA, eliminouse un panel dedicado
  para Enhanced Touch Gestures.

## Versión 20.09

* Eliminouse a posibilidade de deixar que NVDA desactive a interacción
  táctil durante ata dez segundos (deixar pasar xesto táctil).
* Eliminouse a característica de nunciado con pitidos das coordenadas.

## Versión 20.07

* Engadida unha orde de teclado para alternar a interacción táctil ou
  habilitar/deshabilitar deixar pasar xestos táctiles (Control+Alt+NVDA+T).
* Xa que NVDA 2020.1 e posterior inclúe un xesto táctil para realizar click
  dereito co rato (tocar e manter cun dedo), o xesto eliminouse deste
  complemento. En consecuencia, requírese NVDA 2020.1 ou posterior.
* A posibilidade de deixar que NVDA desactive a interacción táctil durante
  ata dez segundos (deixar pasar xesto táctil) está obsoleta. No futuro este
  comando alternará a interacción táctil no seu lugar.
* Nas versións de desenvolvemento de NVDA, debido a trocos na característica
  de interacción táctil, a característica de deixar pasar xesto táctil e o
  panel de opcións de Enhanced Touch Gestures deshabilitaranse. A orde
  utilizada para habilitar deixar pasar xesto táctil alternará a interacción
  táctil no seu lugar.
* A característica de pitido de anuncio de coordeada está obsoleta e
  eliminarase nunha versión futura do complemento.
* Non se oirá o pitido de anuncio de coordeada ao utilizar o teclado táctil.
* NVDA xa non parecerá non facer nada nin reproducirá tons de erro ao
  explorar vía táctil unha facilidade de entrada moderna como o panel de
  emoji.
* NVDA presentará unha mensaxe de erro se non se pode activar o teclado
  táctil (deslizamento con catro dedos á dereita).

## Versión 20.06

* Resoltas varias incidencias de estilo do código e erros potenciais con
  Flake8.

## Versión 20.04

* O xesto de click co botón dereito do rato (un tap mantido cun dedo) agora
  forma parte de NVDA 2020.1.

## Versión 20.01

* Requírese NVDA 2019.3 ou posterior.
* A orde alternar soporte táctil (incluído o paso de ordes táctiles) xa non
  funcionará se o soporte táctil está desactivado completamente.

## Versión 19.11

* Engadidas mensaxes de axuda de entrada para xestos táctiles adicionais.

## Versión 19.09

* Xa se pode desactivar o soporte táctil dende calquera lugar, non só dende
  perfiles que non sexan o normal.

## Versión 19.07

* Cambios internos para soportar versións futuras de NVDA.

## Versión 18.12

* Cambios internos para soportar versións futuras de NVDA.

## Versión 18.08

* Compatible con NVDA 2018.3 e versións futuras.

## Versión 18.06

* A configuración do complemento agora atópase na nova pantalla
  multicategoría Opcións do NVDA na categoría "Enhanced Touch Gestures". A
  consecuencia do que requírese do NVDA 2018.2.
* Arranxados os problemas de compatibilidade con wxPython 4.

## Versión 18.04

* Resolto un erro que podería causar a reprodución de sons de erro na
  categoría de Interacción Táctil no panel de Preferencias do NVDA debido a
  cambios feitos por este complemento.

## Versión 18.03

* Requírese NVDA 2018.1.
* Xa que NVDA 2018.1 vén cunha caixa de verificación Escritura Táctil, ésta
  xa non se inclúe no complemento.

## Versión 17.12

* Requírese do NVDA 2017.4. Específicamente, este complemento agora pode
  manexar cambios de perfil de configuración.
* Dado que o NVDA 2017.4 inclúe o anunciado da horientación da pantalla,
  esta característica xa non forma parte deste complemento.
* Engadida unha caixa de verificación oculta no diálogo Interación Tactil
  para desactivar compretamente o soporte tactil (dispoñible se os perfís
  distintos á configuración normal están activos).
* Se se usa NVDA 2018.1 en adiante, o diálogo Interacción Táctil listarase
  dúas veces no menú Preferencias do NVDA. O segundo elemento é o diálogo
  que vén co complemento.
* No diálogo Interación Tactil para o complemento, o modo de escritura
  tactil xa non se amosa se se usa NVDA 2018.1 en adiante.

## Versión 17.10

* Debido a políticas de soporte de Microsoft, Windows 8 (versión orixinal)
  xa non se soporta.
* O NVDA xa non anunciará a orientación da pantalla dúas veces ao executar
  snapshots de desenvolvemento do NVDA 2017.4.

## Versión 17.07.1

* Engadida una opción no diálogo Interación Táctil para activar manualmente
  deixar pasar toque sen usar un temporizador.
* Co modo deixar pasar manual desactivado, se deixar pasar toque se activa
  antes de que expire a duración de deixar pasar, voltaríase a activar a
  interación táctil.

## Versión 17.07

* Engadido un novo diálogo chamado Interacción Tactil no menú Preferencias
  do NVDA para configurar cómo traballa o NVDA coas pantallas tactiles.
* Despois de instalar esta versión, ao se premer teclas no teclado tactil,
  Débese facer un doble toque na tecla desexada. Podes voltar ao vello xeito
  habilitando a escritura tactil dende o diálogo Interacción Tactil.
* Engadida unha orde (non asignada) para permitir ao NVDA ignorar xestos
  tactiles por ata 10 segundos.
* Engadida unha opción no diálogo Interacción Tactil para permitir ao NVDA
  pausar a interacción tactil entre 3 e 10 segundos para realizar xestos da
  pantalla táctil directamente (coma se o NVDA non se está a executar; por
  defecto é 5 segundos).
* Engadidas mensaxes de depuración no rexistro ao se realizar clic dereito
  (tocar e manter) para grabalos no rexistro do NVDA (require do NVDA 2017.1
  ou posterior).
* Debido a cambios feitos ao se reproducir as coordinadas da pantalla,
  requírese do NVDA 2017.1 ou posterior.

##Versión 17.03

* Correxido un fallo cando o pitido de anunciado de coordinadas non se
  reproducía ou reproducíase un ton de erro no seu lugar cando se utiliza
  NVDA 2017.1 ou anterior.

##Versión 16.12

* O modo web táctil funciona no Microsoft Edge, no Microsoft Word e outros
  onde se use o modo exploración.
* Engadidas listas e pontos de referencia aos elementos do modo web tactil.

## Versión 16.06

* Versión estable inicial.

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
