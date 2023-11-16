# 及时翻译 #

* 作者： Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino and
  other NVDA contributors.
* 下载 [稳定版][1]
* 下载 [开发板][2]

此插件借助 Google 的翻译服务，实现将所选文本和（或）剪贴板中的文本从一种语言翻译为另一种语言。

## 配置语言 ##
要配置翻译的原语言、目标语言以及自动切换的语言，请转到： NVDA 菜单 >> 选项 >> 设置 >> 及时翻译设置面板。

有“源语言”和“目标语言”的两个组合框，以及一个用于控制是否在翻译之后将翻译结果复制到剪贴板的复选框。

两个语言组合框和复制到剪贴板的作用很清楚，但还应该有些其他的说明。请注意，下面的解释假设您在“原语言”组合中选择了“自动”选项。

两个语言组合框和复制到剪贴板的作用很清楚，但还应该有些其他的说明。请注意，下面的解释假设您在“原语言”组合中选择了“自动”选项。

当您使用“切换源语言和目标语言”功能时，“语言切换”组合框很有用；实际上，当原语言设置为自动时，目标语言是无意义的，所以插件将使用上面“语言切换”组合框中所指定的语言。

不妨想象一下这种情况：你通常从一种语言翻译成简体中文（你的母语），但有时候（例如，当你写一篇文档时）你需要翻译成英语（你的第二语言，假设）;你可以将“语言切换”组合框设置为“英语”，这样你就可以从简体中文翻译成英语，而无需转到插件设置去调整。

“自动切换”复选框：当且仅当您在“源语言”组合框中设置为“自动”时它才会显示，并且跟“语言切换”组合框直接关联，如果您选中该复选框，当元语言跟目标语言相同时，则插件会尝试自动交换元语言和目标语言进行翻译。

一个简单的例子：再考虑上面假设的情况；如果你将非简体中文的文本翻译为简体中文，这没有问题，你会直接得到翻译结果，但如果你翻译的文本恰恰也是简体中文，你就会得到与原文相同的翻译结果，如果勾选这个复选框，插件就会将简体中文翻译为英语，这就是理想的效果了。

不过有一些短文本无法自动识别语言，这时候请使用“切换源语言和目标语言”功能来手动切换。

使用多语言的情况，您可以在 NVDA 语音设置参数对话框中勾选自动语言切换复选框，这样，翻译后的结果将以相应语言的语音进行朗读。

## 使用 ##
您可以通过三种方式使用此插件：

1. 使用 Shift + 光标键选择文本的功能选择一些文本（例如，使用光标键移动）并按翻译的快捷键进行翻译。翻译结果将以相应语言的语音朗读出来。
2. 您还可以翻译剪贴板中的文本。
3. 更有用的是，您也可以翻译 NVDA 最后依次朗读的文本。

## 快捷键 ##
以下单字母快捷键需要先按下 NVDA + Shift + T 进入命令接收面板后才可使用。

* T：翻译所选文本，
* Shift + t：翻译剪贴板文本，
* S：切换源语言和目标语言，
* A：朗读元语言和目标语言，
* C：拷贝翻译结果到剪贴板
* I：显示当前文本的语言，
* L： 翻译最后依次朗读的文本，
* O： 打开翻译设置对话框，
* H：读出所有可用的快捷键（帮助信息）。

## 4.4.3 的变化 ##
* 添加了用空格替换下划线的功能，可能会根据上下文提供更好的翻译结果（感谢 Beka Gozalishvili）
* 增加了对 NVDA 2022.1 的兼容性

## 4.4.2 的变化 ##
* 恢复了语言检测和自动交换（感谢Cyrille的修复）。
* 更新翻译语言（感谢Cyrille）。

## 4.4 的变化 ##
* 即时翻译现在与 NVDA 2019.3（Python 3 版本）兼容

## 4.3 的变化 ##
* NVDA 兼容性修复 现在即时翻译可以在最新的 NVDA 上运行。
* 找到了一种方法来再次使用谷歌作为翻译服务。

## 4.2 的变化 ##
* 恢复了与新版 NVDA 的兼容。
* 恢复了自动语言检测功能。

## 4.1 的变化 ##
* InstantTranslate 恢复，现在使用 Yandex翻译服务，而非谷歌。

## 4.0 的变化 ##
* 语言交换后自动执行翻译。
* 缓存的错误修复。

## 3.0 的变化 ##
* 更改了快捷键的使用方式，现在您可以按instantTranslate修饰键“NVDA + Shift +
  t”，然后按单字母键执行某些操作（请参阅“快捷键”部分中的所有单字母快捷键）。
* 实现了交换语言。
* 更改了配置格式，现在我们可以更改及时翻译的设置，如果我们在只读窗格中，但请记住，这将在首次重新启动NVDA之前工作。
* 解除了可翻译文本数量的限制。
* 向“即时翻译设置”菜单项添加了快捷键 t
* “自动”选项现在位于元语言组合框中的第一个位置，并且在目标语言组合框中不显示。
* 添加了用于复制翻译结果的复选框。
* 将配置文件存储在设置文件夹的根目录中。
* 源语言和目标语言与Google翻译目前公开的内容同步（2015年4月22日）。


## 2.1的变化 ##
* 现在，当您按nvda + shift + y时，插件可以从剪贴板翻译文本。

## 2.0 的变化 ##
* 添加了gui配置，您可以在其中选择源语言和目标语言。
* 添加了首选项菜单下的插件菜单项。
* 现在设置会写入到单独的配置文件中。
* 翻译结果现在会自动复制到剪贴板以备将来操作。

## 1.0的变化 ##
* 发布初始版本


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev