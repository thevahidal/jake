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
            h(
                "div",
                klass="items",
                style=f"flex-direction: {section.get('direction', 'column')}",
            )(
                h(
                    "div",
                    klass="item",
                    style=f"width: {'100%' if section.get('direction', 'column') == 'column' else 'unset'}",
                )(
                    h(
                        "a",
                        role="button",
                        klass=f"{'outline' if section.get('item_style', 'outline') == 'outline' else ''}",
                        href=item.get("url"),
                        target="_blank",
                    )(
                        h("hgroup")(
                            h("h4")(item.get("title")), h("h5")(item.get("description"))
                        ),
                    ),
                )
                for item in section["items"]
            ),
        )
        for section in data["sections"]
    )

    meta_tags = frag(
        h("title")(data.get("name")),
        h("meta", name="description", content=data.get("description")),
        h("meta", name="keywords", content=data.get("keywords")),
        h("meta", name="viewport", content="width=device-width, initial-scale=1"),
        h("meta", charset="utf-8"),
        # OG
        h("meta", property="og:title", content=data.get("name")),
        h("meta", property="og:description", content=data.get("description")),
        h(
            "meta",
            property="og:image",
            content=f"{data.get('base_url')}/img/{data.get('image')}",
        ),
        # Twitter / X
        h("meta", name="twitter:title", content=data.get("name")),
        h("meta", name="twitter:description", content=data.get("description")),
        h(
            "meta",
            name="twitter:image",
            content=f"{data.get('base_url')}/img/{data.get('image')}",
        ),
        h("meta", name="twitter:card", content="summary_large_image"),
    )

    head = frag(
        h("head")(
            meta_tags,
            h("link", rel="stylesheet", href="css/pico.min.css"),
            h("link", rel="stylesheet", href="css/style.css"),
            h("style", rel="stylesheet")(
                f"""
                    [data-theme="dark"], [data-theme="light"] {{
                        --primary: {data.get("primary_color", "#546e7a")} !important;
                    }}
                    * {{
                        text-align: {data.get("text_align", "center")};
                    }}
                """
            ),
            raw(
                f"""
                    <!-- Google tag (gtag.js) -->
                    <script async src="https://www.googletagmanager.com/gtag/js?id={data.get("gtag_id")}"></script>
                    <script>
                    window.dataLayer = window.dataLayer || [];
                    function gtag(){{dataLayer.push(arguments);}}
                    gtag('js', new Date());

                    gtag('config', '{data.get("gtag_id")}');
                    </script>
                """
            )
            if data.get("gtag_id")
            else None,
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

    output = html(lang="en", data_theme=data.get("theme", "dark"))(
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
