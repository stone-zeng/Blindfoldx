# Blindfold Neue

## Plugin for Glyphsapp

This is a forked version of [Blindfold](https://github.com/Mark2Mark/Blindfold), a plugin for the [Glyphs font editor](http://glyphsapp.com/). It covers the boundary of the glyphs. Useful for design CJK fonts.

### Install

1. Install via the Plugin Manager in Glyphs.
2. Restart Glyphs.

### Usage

- Select *Glyphs > View > Show Blindfold Neue*
- Right click, you can select *Inverse blindfold* in the contextual menu
- To adjust the width:
  - In *Font Info > Font*, add custom parameter `blindfoldWidth`
  - Acceptable value can be:
    - An integer or float number, e.g. `100` (default) or `150.2`
    - A length-2 tuple `(<horizontal>, <vertical>)`, e.g. `(100, 200)`
    - A length-4 tuple `(<left>, <right>, <top>, <bottom>)`, e.g. `(100, 200, 300, 400)`
- To adjust the color:
  - In *Font Info > Font*, add custom parameter `blindfoldColor`
  - Acceptable value can be a length-4 tuple `(<red>, <green>, <blue>, <alpha>)`, each value should between 0 to 1, e.g. `(0, 0.3, 0.2, 0.7)`

### Examples

![image](https://user-images.githubusercontent.com/18233088/74555875-a8de0500-4f97-11ea-9b36-7afae6b74cbe.png)

### Known issues

- None so far

### Pull Requests

Feel free to comment or pull requests for any improvements.

### License

- Copyright 2015–2019 [Mark Frömberg](http://www.markfromberg.com/) *@Mark2Mark*
- Copyright 2020 Xiangdong Zeng *@stone-zeng*

Made possible with the GlyphsSDK by Georg Seifert (@schriftgestalt) and Rainer Erich Scheichelbauer (@mekkablue).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
