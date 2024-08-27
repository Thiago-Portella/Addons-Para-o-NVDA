# Comandos de Toque Realçados #

* Autor: Joseph Lee
* Baixar [versão estável][1]
* NVDA compatibility: 2022.4 and later

Este extra fornece comandos de ecrã sensível ao toque adicionais para o
NVDA. Também fornece um conjunto de comandos para uma navegação mais fácil
no modo de navegação.

Note: this add-on requires NVDA 2022.3 or later running on a touchscreen
computer with Windows 10 or 11.

## Comandos:

### Disponíveis em qualquer lugar:

* Toque com quatro dedos: Activa/desactiva a ajuda de entrada.
* Quatro dedos para a direita: Geralmente, activa o teclado virtual.
* Quatro dedos à esquerda: alternar ditado (Windows+H; Windows 10 Versão
  1709 ou posterior).

### Revisão de objecto:

* Três dedos para baixo: lê a janela actual.
* Três dedos para a esquerda: indica o objecto sob o foco.
* Três dedos para a direita: indicam o objecto de navegação actual.
* Quatro dedos para cima: indica o título da janela actual.
* Quatro dedos para baixo: lê a barra de estado.

## Modo toque na Web

Este modo de toque, disponível no modo de navegação, permite-lhe navegar
pelo documento através do elemento seleccionado. Para mudar para o modo web,
a partir dos documentos do modo de navegação, dê 3 toques. A partir deste
modo, o deslocamento para cima ou para baixo com um dedo passa pelos modos
de navegação dos elementos disponíveis, enquanto se desloca para a direita
ou para a esquerda com um dedo move-se para o elemento escolhido seguinte ou
anterior, respectivamente. Uma vez que deixa o modo de navegação, o modo de
toque do objeto passa a ser usado.

## configurações de sintetizador do Modo de toque

Pode usar este modo para mudar rapidamente as configurações do sintetizador,
como escolher uma voz e alterar o volume. Neste modo, use de dois dedos para
a esquerda ou para a direita para se mover entre as configurações do
sintetizador e use dois dedos para cima e para baixo gestos para alterar os
valores. estes gestos são semelhantes aos comandos de teclado das
configurações dos sintetizadores.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 8.1 is no longer supported by
  Microsoft as of January 2023.
* It is possible to reassign touch keyboard and dictation toggle commands
  from input gestures dialog under Enhanced Touch Gestures category.
* Removed read-only state workaround for touch keyboard keys as it is
  resolved in Windows 10.

## Version 22.03

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on
  on Windows 7, 8, and 8.1.

## Versão 21.10

* É necessário o NVDA 2021.2 ou posterior devido a alterações do NVDA que
  afectam este extra.

## Versão 21.08

* Suporte inicial para Windows 11.

## Versão 21.01

* A Versão do NVDA 2020.3 ou posterior é necessária.
* No Windows 10 Versão 1709 e posteriores, fazer um movimento de quatro
  dedos à esquerda irá alternar o ditado (Windows+H).
* Remover o comando de alternância de suporte dedicado de interacção táctil
  do extra.
* Como o suporte de interacção táctil pode ser alternado a partir do painel
  de configurações de interacção táctil do NVDA, um painel dedicado de
  definições de comandos Tácteis Melhorados foi removido.

## Versão 20.09

* Removida a capacidade de deixar o NVDA desligar a interacção por toque
  durante até dez segundos (passagem do comando por toque).
* Função de bip de anúncio de coordenadas removido.

## Versão 20.07

* Adicionado um comando de teclado para alternar a interacção por toque ou
  activar/desactivar a passagem por toque (Control+Alt+NVDA+T).
* Como o NVDA 2020.1 e posteriores incluem um comando táctil para executar
  um clique direito do rato (um toque com um dedo e segurar), o comando foi
  removido deste suplemento. Como resultado, o NVDA 2020.1 ou posterior é
  necessário.
* A capacidade de deixar o NVDA desligar a interacção por toque durante até
  dez segundos (passagem do comando por toque) foi desactivada. No futuro,
  esta característica irá alternar a interacção táctil em vez disso.
* Em versões de desenvolvimento do NVDA, devido a alterações na
  funcionalidade de interacção táctil, a funcionalidade de passagem de
  comandos tácteis e o painel de definições de Gestos Tácteis Melhorados
  serão desactivados. O comando utilizado para permitir a passagem de
  comandos tácteis irá alternar a interacção táctil em vez disso.
* A funcionalidade de anúcio de coordenadas por bip foi desactivada e será
  removida num futuro lançamento de um novo extra
* O sinal sonoro de anúncio de coordenadas não será ouvido durante a
  utilização do teclado táctil.
* O NVDA deixará de parecer não fazer nada ou de tocar os tons de erro
  enquanto explora as modernas facilidades de entrada, tais como o painel
  emoji através do toque.
* O NVDA apresentará uma mensagem de erro se o teclado táctil não puder ser
  activado (quatro dedos à direita).

## Versão 20.06

* Resolvidos vários problemas de estilo de codificação e potenciais bugs com
  Flake8.

## Versão 20.04

* O gesto de clique com o botão direito do rato (um toque com um dedo e
  segurar) faz agora parte do NVDA 2020.1.

## Versão 20.01

* Requere o NVDA 2019.3 ou posterior.
* O comando de alternância do suporte táctil (incluindo a passagem táctil)
  deixará de funcionar se o suporte táctil for completamente desligado.

## Versão 19.11

* Adicionadas mensagens de ajuda de entrada para comandos tácteis
  adicionais.

## Versão 19.09

* O apoio táctil pode agora ser desactivado a partir de qualquer lugar, e
  não apenas a partir de perfis que não o perfil normal.

## Versão 19.07

* Alterações internas para suportar futuros lançamentos do NVDA.

## Versão 18.12

* Alterações internas para suportar futuros lançamentos do NVDA.

## Versão 18.08

* Compatível com NVDA 2018.3 e futuras versões.

## Versão 18.06

* Agora, as configurações adicionais encontram-se no novo ecrã
  multi-categoria Configurações do NVDA, na categoria "comandos de toque
  aprimorados". Como resultado, é necessário o NVDA 2018.2.
* Corrigidos problemas de compatibilidade com o wxPython 4.

## Versão 18.04

* Resolve um problema em que a categoria de interacção por toque no painel
  Configurações do NVDA pode causar sons de erro, devido a alterações feitas
  a partir deste extra.

## Versão 18.03

* É necessário o NVDA 2018.1
* Como o NVDA 2018.1 já trás incluída a caixa de selecção por toque, essa
  caixa de selecção deixou de fazer parte deste extra.

## Versão 17.12

* Requer NVDA 2017.4. Especificamente, este extra agora pode processar
  trocas de perfil de configuração.
* Como o NVDA 2017.4 inclui o anúncio da orientação do ecrã, esse recurso
  não faz mais parte deste extra.
* Adicionada uma caixa de selecção oculta na caixa de diálogo Interacção por
  toque para desativar completamente o suporte por toque (disponível se
  outros perfis além do da configuração normal estiverem activos).
* Se estiver a usar o NVDA 2018.1 ou posteriores, a caixa de diálogo
  interacções por toque será listada duas vezes no menu de preferências do
  NVDA. O segundo item é o diálogo que vem com o add-on. 
* No diálogo de interacção de toque para o extra, o modo de digitar toque
  não é mostrado se usar versões do NVDA posteriores à 2018.1.

## Versão 17.10

* Devido à política de suporte da Microsoft, o Windows 8 (versão original)
  não é mais suportado.
* O NVDA não anunciará mais a orientação do ecrã duas vezes ao executar
  versões de desenvolvimento do NVDA 2017.4.

## Versão 17.07.1

* Adicionada uma opção no diálogo de interacção de toque para alternar
  manualmente a passagem de toque sem o uso de um temporizador.
* Com o modo de passagem manual desligado, se a passagem de toque for
  activada antes do final da duração da passagem, a interacção de toque será
  activada.

## Versão 17.07

* Adicionada uma nova caixa de diálogo denominada interacção por toque no
  menu de preferências do NVDA para configurar como o NVDA funciona com
  ecrãs sensíveis ao toque.
* Depois de instalar esta versão, ao pressionar as teclas no teclado
  virtual, é preciso tocar duas vezes a tecla desejada. Pode voltar para a
  maneira antiga, permitindo a digitação de toque na caixa de diálogo
  Interação táctil.
* Adicionado um comando (não atribuído) para permitir que o NVDA ignore os
  gestos de toque até 10 segundos.
* Adicionada uma opção na caixa de diálogo Interacção por toque para
  permitir que o NVDA interrompa a interacção de toque entre 3 a 10 segundos
  para executar gestos de ecrã sensível directamente (como se o NVDA não
  estivesse em execução, o padrão é 5 segundos).
* Adicionadas mensagens de log de depuração ao executar cliques corretos
  (tocar e segurar) para serem gravadas no log do NVDA (requer NVDA 2017.1
  ou posterior).
* Devido às alterações feitas ao reproduzir as coordenadas do ecrã, o NVDA
  2017.1 ou posterior é necessário.

##Versão 17.03

* Corrigido um problema em que o sinal sonoro de coordenadas não era
  reproduzido ou surgia um beep de erro em vez disso ao usar o NVDA 2017.1
  ou posterior.

##Versão 16.12

* O modo Web Touch funciona no Microsoft Edge, no Microsoft Word e em outros
  onde o modo de navegação é usado.
* Adicionadas listas e marcadores para elementos do modo web touch.

## Versão 16.06

* Versão inicial estável.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
