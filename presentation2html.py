import os
import click
from presentation2html.tool import Tool


@click.command()
@click.option("--website", help="Reveal.js site directory", required=True)
@click.option("--presentationid", help="presentation id", required=True)
@click.option("--indexfile", help="index filename. will default to presentationid if not provided.", required=False)
@click.option("--imagesize", help="image size (MEDIUM, LARGE)", default="medium", required=False)
@click.option("--credfile", help="credentials file path", default="credentials.json", required=False)
def main(website, presentationid, indexfile="", imagesize="medium", credfile="credentials.json"):

    imagesize = imagesize.upper()
    if imagesize not in ["MEDIUM", "LARGE"]:
        raise ValueError("Invalid image size should be MEDIUM or LARGE")
    if not indexfile:
        indexfilepath = os.path.join(website, "{}.html".format(presentationid))
    else:
        indexfilepath = os.path.join(website, "{}.html".format(indexfile))
    destdir = os.path.join(website, presentationid)

    p2h = Tool(presentationid, credfile)
    p2h.downloader.thumbnailsize = imagesize
    p2h.build_revealjs_site(destdir, indexfilepath)


if __name__ == "__main__":
    main()