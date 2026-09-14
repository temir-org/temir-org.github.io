# Temir Website

The Temir website source code.

The [Webis website](https://github.com/webis-de/webis-de.github.io) is the master
of this website: layout, styles, and page conventions are kept in sync with it.
Temir deliberately differs only in

- the color of the header,
- the names and links in the header navigation,
- the elements on the landing page, and
- its own content pages.

Everything else should be changed upstream in the Webis website or in
[webis-de-assets](https://github.com/webis-de/webis-de-assets) and then adopted here.

## Building The Source Code

*If you are editing the files directly on GitHub, you can skip this section.*

The website is built using [Jekyll](https://jekyllrb.com/docs/) and uses
[UIkit](https://getuikit.com/) as a CSS framework as well as a few additional
JavaScript libraries. To install Ruby and Bundler on your system, run

    sudo apt install ruby ruby-dev build-essential

Afterwards, `cd` into the main folder of this repository, install the pinned
gems, and start the development server

    bundle install
    bundle exec jekyll serve

`Gemfile.lock` is pinned to the Linux platform of the build workflow. On macOS,
run `bundle lock --add-platform arm64-darwin` once before `bundle install`, but
do not commit the resulting lockfile change.

This will start a server at <http://localhost:4000/> serving the compiled
website. If the source files change, the server will automatically recompile
them. The server can be stopped via `Ctrl+C`.

To publish changes to the source files, just push them to GitHub. The workflow in
`.github/workflows/build-pages.yaml` builds the site with the gems pinned in
`Gemfile.lock` and deploys it to GitHub Pages.

## Sources Structure
- `.github/workflows` Build and deployment workflow
- `_layouts` The website's layout templates
- `_maintenance` Maintenance scripts
- `_sass` Sass source files for the website's CSS
- `_site` Compiled HTML output files (not included in the repository)
- `css` Main Sass file and additional CSS
- `img`, `js` Image and JavaScript files

Other folders not starting with an underscore are content folders containing
HTML content files.

## Edit HTML
To edit the website's HTML, simply edit the `.html` content file you want to change. There is
nothing special to this, except that you can (!) use
[Jekyll's Liquid tags](https://jekyllrb.com/docs/templates/) and that each source file
starts with a YAML front matter. The latter is just a bunch of arbitrary variable
definitions, but should at least (but doesn't have to) include the following:

    ---
    layout: default
    nav_active: id
    title: The page title
    description: A meta description
    ---

The only thing special is `nav_active`, which determines which entry in the navigation should
be highlighted as active. The placeholder `id` can be any of `index`, `people`,
`for-students`, `lecturenotes` (the Teaching entry), `research`, `publications`, `data`,
`facilities`, or `events`.

If you want an HTML page without any layout, omit `layout` (or change it to a custom layout
which you put in `_layouts` before).

If you need extra (external) CSS files within a page, specify their paths with

    additional_css: [ 'file1.css', 'file2.css', '...' ]

## Edit CSS
CSS is managed via Sass, which is automatically compiled by Jekyll.
The main SCSS file is located at `css/style.scss`. This file is only there to
include all other fragments and you hardly ever need to touch it. The fragments
themselves are under `_sass`. Feel free to edit them any way you want, but please
keep the number of Sass variable redefinitions at the absolute minimum to avoid
inconsistencies between websites.

## Linked Assets
Most styles and other web assets are hot-linked from [webis-de-assets](https://github.com/webis-de/webis-de-assets),
a collection of modular Jekyll templates, Sass styles, and other third-party dependencies
(UIkit, Fontawesome, jQuery, etc.) for the Webis website theme. The search service logos in
the footer are hot-linked from `webis.de/research/img/`, mirroring the Webis layout.

Content imagery is kept local, even where webis.de happens to host the same file: the
funding body logos on the research page exist on webis.de only under the legacy
`weimar/research/img/` path, which is not a stable asset location to depend on. Assets that
are genuinely shared belong in webis-de-assets; hot-link them from there instead of copying
them into this repository.

If you add new styles or scripts, please check if they are modular and reusable enough
to be added to webis-de-assets. Only add them to this repository if they are specific to
the Temir website.
