import argparse
import app

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert python code files to a single pdf file")
    parser.add_argument("name", metavar="Name", type=str, help="Enter you full name")
    parser.add_argument("id", metavar="KMUTT-ID", type=str, help="Enter you student id")
    parser.add_argument(
        "-d", "--directory", metavar="Dir", default="", type=str, help="Enter code directory"
    )
    parser.add_argument(
        "-k", "--keyword", metavar="Keyword", default="lab", type=str, help="Enter file keyword"
    )
    parser.add_argument(
        "-bg",
        "--background_color",
        metavar="Color",
        default="Golden Poppy",
        type=str,
        help="Enter color name or Hex color code",
    )
    parser.add_argument(
        "-t", "--theme", metavar="Theme", default="Night Owl", type=str, help="Enter Color theme"
    )
    parser.add_argument(
        "-f",
        "--font",
        metavar="Font-family",
        default="Fira Code",
        type=str,
        help="Enter font name (See all names in carbon exported config)",
    )
    parser.add_argument(
        "-s", "--font_size", metavar="Font-size", default=16, type=int, help="Enter size of font"
    )
    parser.add_argument("-l", "--line_numbers", action="store_true", help="Turn on/off line number")
    parser.add_argument(
        "-w",
        "--width",
        metavar="Width (px)",
        default=680,
        type=int,
        help="Width of code snippets",
    )
    parser.add_argument(
        "-s",
        "--save_path",
        metavar="Path",
        default="demo.pdf",
        type=str,
        help="Enter path for save pdf",
    )

    args = parser.parse_args()

    params = {
        "paddingVertical": "50px",
        "paddingHorizontal": "50px",
        "theme": args.theme,
        "backgroundColor": args.background_color,
        "language": "python",
        "fontFamily": args.font,
        "fontSize": str(args.font_size),
        "lineNumbers": args.line_numbers,
        "width": args.width,
    }

    arguments = {
        "name": args.name,
        "id": args.id,
        "dir": args.directory,
        "save_path": args.save_path,
        "keyword": args.keyword,
    }

    app.run_app(params, arguments)
