# Remap Applications key


## Information
* Authors: Rui Fontes based on the work of Héctor J. Benítez Corredera
* Updated in 22/03/2024
* Download [stable version][1]
* Compatibility: NVDA version 2019.3 and beyond


## Presentation
Simple add-on for those computers that do not have an applications key or whose applications key does not work.
It is also usefull in the File explorer of Windows 11 build 22621 and laters, since it allows to assign a key to the combination Shift+applications key, used to display the full context menu. Starting in this Windows build, applications key only shows a stripped version of context menu.
It is necessary to assign the key or combination of keys we want to replace applications key.
In NVDA / Preferences / Input Gestures... / RemapApplicationsKey we can assign the combination we desire.


## Observations
When assigning a key combination or a single key, we have to take into account that this combination or key is not used in any application.
For example, Ctrl + Down Arrow could work for most of the system but would give an error in Google Chrome, not allowing access to the context menu.
To give an example, I usually use the "printScreen" key, which is usually on the top row on the right and is usually the second or third key.
We can find out which one it is if we use NVDA's input help; for this, we press the NVDA + 1 key and start exploring the keys on the keyboard. When it says "printScreen," that will be the key we were looking for. We can exit NVDA's input help by pressing NVDA + 1 again.
This is an example, leaving it up to the user to choose their key or key combination.


## Translators and collaborators:
* French: Rémy Ruiz
* Russian: Valentin Kupriyanov
* Ukrainian: VovaMobile
* Turkish: Umut Korkmaz


## Change Log


### Version 2023.09.30
* In the 2023.09.26 NVDA compatibility was extended to version 2024.1;
* Now it is also possible to assign a keystroke to Shift+application key;


### Version 2023.09.02
* Now maintained by Rui Fontes and NVDA portuguese team
* Now the code is based in english.


### Version 0.4
* Added Russian, Ukrainian, and Turkish languages.
* Added compatibility with NVDA 2023.1


### Version 0.3
* Changed the way to invoke the applications key from native NVDA to native Windows, since it is a more reliable and more direct method.
* Added the possibility of left and right mouse clicks on focus.
We will have to assign the corresponding key combinations in the Input gesture dialog.
When we execute the action, the mouse will move to the focus and make the corresponding click, and a sound will be heard indicating that the click was executed.


### Version 0.2
* Compatibility with NVDA 2022


### Version 0.1.5
* Fixed issue in NVDA add-ons.
* Added French language.


### Version 0.1
* Initial version.

[1]: https://github.com/ruifontes/RemapKeyAplication-para-NVDA/releases/download/2025.07.14/remapApplicationsKey-2025.07.14.nvda-addon
