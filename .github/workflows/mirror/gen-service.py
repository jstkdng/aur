import os
from srcinfo.parse import parse_srcinfo
from urllib.parse import urlparse
from jinja2 import Environment, FileSystemLoader, BaseLoader
from pathlib import Path

TEMPLATE_STR = """<!-- vim: set ft=xml: -->
<services>
{%- for source in sources %}
    <service name="download_url">
        <param name="protocol">{{ source.protocol }}</param>
        <param name="host">{{ source.host }}</param>
        <param name="path">{{ source.path }}</param>
        <param name="filename">{{ source.filename }}</param>
    </service>
{%- endfor %}
{%- if pkg.mirror %}
    <service name="obs_scm">
        <param name="scm">git</param>
        <param name="url">https://aur.archlinux.org/{{ pkg.name }}</param>
        <param name="extract">[!PKGBUILD]*</param>
    </service>
{%- elif not pkg.only_pkgbuild %}
    <service name="obs_scm">
        <param name="scm">git</param>
        <param name="url">https://github.com/jstkdng/aur</param>
        <param name="subdir">{{ pkg.name }}</param>
        <param name="extract">[!PKGBUILD]*</param>
    </service>
{%- endif %}
</services>


"""


def main():
    # read .SRCINFO from current directory
    with open(".SRCINFO", "r") as f:
        (srcinfo, _) = parse_srcinfo(f.read())
        sources = []
        for source in srcinfo["source"]:
            parsed_url = urlparse(source)
            src_obj = {
                "protocol": "",
                "host": "",
                "path": "",
                "filename": ""
            }

            if not parsed_url.netloc:
                if parsed_url.scheme:
                    src_obj["filename"] = parsed_url.scheme
                    parsed_url = urlparse(parsed_url.path[1:])
                else:
                    continue

            src_obj["protocol"] = parsed_url.scheme
            src_obj["host"] = parsed_url.netloc
            src_obj["path"] = parsed_url.path
            if not src_obj["filename"]:
                src_obj["filename"] = parsed_url.path.split('/')[-1]

            sources.append(src_obj)

    # package information
    pkg = {
        "name": os.getenv('PACKAGE'),
        "only_pkgbuild": True,
        "mirror": False
    }
    if os.getenv('MIRROR') is not None:
        pkg["mirror"] = True

    cwd = Path.cwd()
    files = [x for x in cwd.iterdir()]
    empty_dir = True
    ignore = ['PKGBUILD', '.SRCINFO', '.gitignore', '_constraints', '_service']
    for file in files:
        if file.stem not in ignore:
            pkg["only_pkgbuild"] = False
            break

    # render template
    template = Environment(loader=BaseLoader()).from_string(TEMPLATE_STR)
    output = template.render(sources=sources, pkg=pkg)
    with open("_service", "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
