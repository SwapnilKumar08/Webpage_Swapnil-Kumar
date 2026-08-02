# swapnilkumar.com — personal website

A six-page static site: Home, Research, Ventures & Innovation, Publications, News, Contact.
No build step, no dependencies, no backend. Open `index.html` and it works.

## Files

```
index.html            Home
research.html         Research
ventures.html         Ventures & Innovation (+ education, teaching)
publications.html     Publication list
news.html             News, awards & honours
contact.html          Contact details + message form
assets/styles.css     All styling (one file, CSS custom properties at the top)
assets/main.js        Mobile nav, scroll reveals, stat counters, form handoff
assets/Swapnil_Kumar_CV_GTV-UK.pdf  Downloadable CV used across the site
build.py              Optional generator that regenerates every HTML file
README.md             This file
```

## Editing

You can edit the `.html` files directly — they are plain, readable HTML.

If you prefer to keep the header and footer in one place, edit `build.py` instead
(all page content lives there as Python strings) and regenerate:

```bash
python3 build.py
```

**Careful:** running `build.py` overwrites the HTML files. Pick one workflow —
either edit HTML directly and delete `build.py`, or only ever edit `build.py`.

## Changing the colours

Everything comes from custom properties at the top of `assets/styles.css`:

```css
--ink-900: #0a0c10;   /* page background      */
--bone:    #f4f1ea;   /* primary text         */
--ember:   #e8873b;   /* accent               */
--sage:    #7fb2a1;   /* secondary accent     */
```

Change those four and the whole site follows.

## Images

All artwork is generated SVG, inlined so the site has zero image dependencies.
To use real photographs, replace the `<figure class="art">…</figure>` blocks with:

```html
<figure class="art art--wide">
  <img src="assets/img/your-photo.jpg" alt="Description">
</figure>
```

Add `.art img { width:100%; height:100%; object-fit:cover; }` to the stylesheet.
The four placeholders under "Life outside work" on the home page are the first
ones worth swapping.

## Contact form

The form currently opens the visitor's email client with a pre-filled message
(`assets/main.js`, bottom). That keeps the site fully static. To store submissions
server-side, replace the submit handler with one of:

- **Formspree** — change the `<form>` to `action="https://formspree.io/f/XXXX" method="POST"` and remove the JS handler
- **Netlify Forms** — add `netlify` to the `<form>` tag if hosting on Netlify
- **Supabase Edge Function** — POST the `FormData` to your function URL

## Hosting

Any static host works. For a zero-cost, durable setup, this repo includes a
GitHub Pages workflow in `.github/workflows/deploy-pages.yml` that publishes
the `site/` folder.

Setup steps:

1. Push this repository to GitHub.
2. Open **Settings -> Pages**.
3. Set **Source** to **GitHub Actions**.
4. Push to `main` (or run the workflow manually).

Expected URL:

`https://swapnilkumar08.github.io/Webpage_Swapnil-Kumar/`

## Still to personalise

- A profile photo if you want one in the hero
- Open Graph share image (`og:image` meta tag is not yet set)
