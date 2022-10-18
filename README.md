![preview](preview/banner.png)
<br> Save your time by automatically converting **python** code files into pdf files, for KMUTT college students.
<br> **LEB2** (Learning Environment version B2) https://www.leb2.org/
## Installation
```sh
git clone https://github.com/monshinawatra/leb2code-pdf.git
cd leb2code-pdf
pip install -r requirements.txt
```
## Quick start
**Inference** with `leb2code.py` 
```
python leb2code.py "ชินวัตร นาไชยธง"      # Full name
                   "65090500408"        # KMUTT id
                   -d "lab5"            # Code files directory
                   -bg "Red (NCS)"      # Background color
                   -o "output/lab5.pdf  # Save path
                   -l                   # Show line number
```

Arguments parsing list
<br> `-h, --help` show this help message and exit
<br> `-d <Dir>, --directory <Dir>` Enter code directory
<br> `-k <Keyword>, --keyword <Keyword>` Enter file keyword
<br> `-bg <Color>, --background_color <Color>` Enter color name or Hex color code
<br> `-t <Theme>, --theme <Theme>` Enter Color theme
<br> `-f <Font family>, --font <Font family>` Enter font name (See all font names in carbon exported config)
<br> `-s <Font size>, --font_size <Font size>` Enter size of the font
<br> `-l, --line_numbers` Turn on/off line number
<br> `-w <Width (px)>, --width <Width (px)>` Width of code snippets
<br> `-o <Path>, --save_path <Path>` Enter destination path for saving pdf

**Inference** in `app.py` arguments
|          Arguments        |   Default             | Type  |  Description |
| ------------------------- | --------------------- |:-----:| ------------------------------------------- |
| `name` (required)         |                       | str   | Your full name. e.g. `ชินวัตร นาไชยธง`, `Shinawatra Nachaithong`
| `id` (required)           |                       | str   | Your **KMUTT** college student id. e.g.  `65090500000`
| `dir`                     | `"./"`                | str   | Your code directory
| `language`                | `"Python"`            | str   | Code language. `'python'` by default and `'plain-text'` for output image
| `keyword`                 | `"lab"`               | str   | All your unique code file name
| `backgroundColor`         | `"Golden Poppy"`      | str   | Background color. See all <a href="https://github.com/monshinawatra/leb2code-pdf/#color-and-theme">color names</a>, <br>or use custom HEX color code instead
| `theme`                   | `"Night Owl"`         | str   | Color theme in code snippets
| `fontFamily`              | `"Fira Code"`         | str   | Font family, e.g. `JetBrains Mono`, `Fira Code`. <br>See all names in carbon exported config
| `fontSize`                | `16`                  | int   | Just size of font in code snippets
| `lineNumbers`             | `False`               | bool  | Turn on/off line number
| `width`                   | `680`                 | int   | Width of code snippets
| `save_path`               | `"demo.pdf"`          | str   | Output path for pdf file
| `paddingVertical`         | `"50px"`              | str   | Vertical padding
| `paddingHorizontal`       | `"50px"`              | str   | Horizontal padding

## Results
Here is the result from <a href="https://carbon.now.sh/">carbon</a> `"Golden Poppy"`
<br>
![preview](preview/code_preview.png)

## Color and theme
**Support themes**
<br> `Zenburn` `Yeti` `VSCode` `Verminal` `Twilight` `SynthWave` `Solarized (Light)` `Solorarized (Dark)` `Shades of Purple` `Seti` `Paraiso` `Panda` `One Dark` `One Light` `Oceanic Next` `Nord` `Night Owl` `Monokai` `Material` `Lucario` `Hopscotch` `Duotine` `Cobalt` `Blackboard`
<br>
<br>
**Color Name**
You can use these as a color name, if you don't like these colors, you can use custom hex color code instead.

|             Color                 |   Name              |             Color                 |   Name              |             Color                 |   Name              |
| --------------------------------- | ------------------- | --------------------------------- | ------------------- | --------------------------------- | ------------------- |
| ![preview](preview/color_0.png)   | `"White"`           | ![preview](preview/color_12.png)  | `"Golden Poppy"`    | ![preview](preview/color_24.png)  | `"Teal"`
| ![preview](preview/color_1.png)   | `"Silver"`          | ![preview](preview/color_13.png)  | `"Neon Orange"`     | ![preview](preview/color_25.png)  | `"Blue"`
| ![preview](preview/color_2.png)   | `"Gray"`            | ![preview](preview/color_14.png)  | `"Bright Orange"`   | ![preview](preview/color_26.png)  | `"Sapphire Blue"`   
| ![preview](preview/color_3.png)   | `"Black"`           | ![preview](preview/color_15.png)  | `"Yellow"`          | ![preview](preview/color_27.png)  | `"Midnight Blue"`   
| ![preview](preview/color_4.png)   | `"Brown Chocolate"` | ![preview](preview/color_16.png)  | `"Emerald Green"`   | ![preview](preview/color_28.png)  | `"Navy"`
| ![preview](preview/color_5.png)   | `"Crimson"`         | ![preview](preview/color_17.png)  | `"Lime"`            | ![preview](preview/color_29.png)  | `"Purple"`
| ![preview](preview/color_6.png)   | `"Violet Red"`      | ![preview](preview/color_18.png)  | `"Green"`           | ![preview](preview/color_30.png)  | `"Byzantium"`       
| ![preview](preview/color_7.png)   | `"Rose Red"`        | ![preview](preview/color_19.png)  | `"Aqua"`            | ![preview](preview/color_31.png)  | `"Pastel Pink"`     
| ![preview](preview/color_8.png)   | `"Red (NCS)"`       | ![preview](preview/color_20.png)  | `"Blue Green"`      | ![preview](preview/color_32.png)  | `"Pastel Red"`      
| ![preview](preview/color_9.png)   | `"Red"`             | ![preview](preview/color_21.png)  | `"Jade"`            | ![preview](preview/color_33.png)  | `"Salmon"`
| ![preview](preview/color_10.png)  | `"Cinnamon"`        | ![preview](preview/color_22.png)  | `"Jungle Green"`    | ![preview](preview/color_34.png)  | `"Peach"`
| ![preview](preview/color_11.png)  | `"Portland Orange"` | ![preview](preview/color_23.png)  | `"Viridian"`
## Task
- [x] Main application.
- [x] Refactor our code.
- [x] Arguments parsing.
- [ ] Beautify code snippets, layout, label in pdf file.

## Reference
**Carbon** <br>
Create and share beautiful images of your source code
https://carbon.now.sh/

**Carbon API**
https://github.com/petersolopov/carbonara

**PyFPDF** <br>
Free and open-source pure-python PDF library
https://github.com/PyFPDF/fpdf2
