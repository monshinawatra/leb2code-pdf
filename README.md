![preview](preview/banner.png)
<br> Saving your time by automatic convert python code files into pdf files, for KMUTT college students.
<br> **LEB2** (Learning Environment version B2) https://www.leb2.org/
## Installation
<code>git clone https://github.com/monshinawatra/leb2code-pdf.git</code>
<br><code>pip install -r requirements.txt</code>

## Usage
<code>python app.py</code>
<br>
<br> **Config**
|          Arguments        |   Default             | Type  |  Description |
| ------------------------- | --------------------- |:-----:| ------------------------------------------- |
| `name` (required)         |                       | str   | Your full name. e.g. `ชินวัตร นาไชยธง`, `Shinawatra Nachaithong`
| `number_id` (required)    |                       | int   | Your **KMUTT** college students id. e.g.  `65090500000`
| `backgroundColor`         | `"Portland Orange"`   | str   | Background color. See all color names in color config, <br>or you can use your custom HEX color code. 
| `theme`                   | `"Night Owl"`         | str   | Color theme in code snippet.
| `fontFamily`              | `"Fira Code"`         | str   | Font family, e.g. `JetBrains Mono`, `Fira Code`. <br>See all names in carbon exported config.
| `fontSize`                | `16`                  | int   | Just size of font in code snippets.
| `lineNumbers`             | `True`                | bool  | Turn on/off line number
| `width`                   | `680`                 | int   | Width of code snippets

## Task
- [x] Main application.
- [ ] Refactor our code.
- [ ] Arguments parsing.
- [ ] Beautify code snippets, layout, label in pdf file.

## Reference
**Carbon** <br>
Create and share beautiful images of your source code.
https://carbon.now.sh/

**Carbon API**
https://github.com/petersolopov/carbonara

**PyFPDF** <br>
Free and open-source pure-python PDF library
https://github.com/PyFPDF/fpdf2
