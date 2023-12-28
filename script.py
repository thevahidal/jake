import tomllib

from tinyhtml import html, h, frag, raw


with open("data.toml", "rb") as f:
    data = tomllib.load(f)
    sections = frag(
        h("div", klass="section")(
            h("h1", klass="title")(section.get("title")),
            h("p", klass="description")(section.get("description")),
            (
                h("div", klass="item")(
                    h("h2", klass="title")(item.get("title")),
                    h("p", klass="description")(item.get("description"))
                    if item.get("description")
                    else None,
                    h("a", klass="url", href=item.get("url"))("Link"),
                )
                for item in section["items"]
            ),
        )
        for section in data["sections"]
    )

    output = html(lang="en")(
        h("head")(
            h("meta", charset="utf-8"),
            h("style")(
                raw(
                    """
              body {
               font-family: sans-serif;
              }
              .section > .title {
                 color: red;
              }
            """
                )
            ),
        ),
        h("body")(sections),
    ).render()

    with open("index.html", "w") as f:
        f.write(output)
