import tomllib

from tinyhtml import html, h, frag, raw


with open("data.toml", "rb") as f:
    data = tomllib.load(f)
    sections = frag(
        h("div", klass="section")(
            h("hgroup")(
                h("h3")(section.get("title")),
                h("p")(section.get("description")),
            ),
            (
                h("div", klass="item")(
                    h("a", href=item.get("url"), target="_blank")(
                        h("hgroup")(
                            h("h4")(item.get("title")),
                            h("p")(item.get("description"))
                            if item.get("description")
                            else None,
                            "",
                        ),
                    ),
                )
                for item in section["items"]
            ),
        )
        for section in data["sections"]
    )

    head = frag(
        h("head")(
            h("title")(data.get("name")),
            h("meta", name="description", content=data.get("description")),
            h("meta", name="keywords", content=data.get("keywords")),
            h("meta", name="viewport", content="width=device-width, initial-scale=1"),
            h("meta", charset="utf-8"),
            h("link", rel="stylesheet", href="css/pico.min.css"),
            h("link", rel="stylesheet", href="css/style.css"),
        ),
    )

    header = frag(
        h("header", klass="container")(
            h("hgroup")(
                h(
                    "img",
                    klass="avatar",
                    src=f"img/{data.get('image')}",
                    alt="avatar",
                ),
                h("h1")(data.get("name")),
                h("p")(data.get("description")) if data.get("description") else None,
            ),
        )
    )

    footer = frag(
        h("footer", klass="container")(
            h("small")("Generated with "),
            h(
                "a",
                klass="",
                href="https://github.com/thevahidal/jake/",
                target="_blank",
            )("Jake"),
        ),
    )

    output = html(lang="en")(
        head,
        h("body")(
            header,
            h("main", klass="container")(
                sections,
            ),
            footer,
        ),
    ).render()

    with open("dist/index.html", "w") as f:
        f.write(output)
