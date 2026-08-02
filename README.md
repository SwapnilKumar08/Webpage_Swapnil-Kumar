# Webpage_Swapnil-Kumar

Personal website for Swapnil Kumar (static HTML/CSS/JS), generated from `site/build.py`.

## Live URL (GitHub Pages)

After enabling Pages with GitHub Actions, the site is available at:

https://swapnilkumar08.github.io/Webpage_Swapnil-Kumar/

## Project structure

- `site/` - deployable static website
- `site/build.py` - source generator for all website pages
- `site/assets/Swapnil_Kumar_CV_GTV-UK.pdf` - downloadable CV used by the website
- `.github/workflows/deploy-pages.yml` - automatic GitHub Pages deployment workflow

## Local update workflow

1. Edit content in `site/build.py`.
2. Regenerate pages:

```bash
cd site
python3 build.py
```

3. Commit and push to `main`.

## GitHub Pages setup (zero cost)

1. Push this repository to GitHub.
2. Open `Settings -> Pages`.
3. Set `Source` to `GitHub Actions`.
4. Push to `main` (or run the workflow manually).

The workflow deploys the `site/` folder, so links stay clean at the root URL.
