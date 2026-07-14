# Mika Krommenhoek Photography — Website

A simple static website (HTML/CSS/JS only — no build tools required) for
Mika Krommenhoek Photography: Home, Inquire, Pricing Guide, Portfolio,
About Me, and Reviews pages.

## What's in this folder

```
index.html         Home page
inquire.html       Inquiry form
thank-you.html     Confirmation page shown after a successful inquiry
pricing.html       Pricing Guide
portfolio.html     Portfolio gallery
about.html         About Me
reviews.html       Reviews
css/style.css      All site styling
js/script.js       Mobile menu + inquiry form submission
images/            All photos (currently placeholders, see below)
scripts/           One-time script used to generate placeholder images.
                   Safe to delete once real photos are in place.
```

---

## 1. Put this on GitHub

1. Go to [github.com](https://github.com) and create a free account if you
   don't have one already.
2. Click the **+** icon (top right) → **New repository**.
   - Name it `mikakromphoto` (to match your Instagram handle).
     - **Important:** the exact repo name changes your free URL. If you
       name the repo just `mikakromphoto`, your site lives at
       `https://YOUR-GITHUB-USERNAME.github.io/mikakromphoto/`. If you
       want the clean address `https://mikakromphoto.github.io` with no
       extra path at the end, your GitHub **account username** itself
       needs to be `mikakromphoto`, and the repo must be named exactly
       `mikakromphoto.github.io` (GitHub treats that exact name as a
       special "user site"). Either way works fine — the second one is
       just a shorter link.
   - Set it to **Public** (required for the free version of GitHub Pages).
   - Don't check "Add a README" — you already have one.
   - Click **Create repository**.
3. On the new (empty) repo page, click **uploading an existing file**.
4. Drag in every file and folder from this project (`index.html`,
   `css/`, `js/`, `images/`, all the `.html` pages, this `README.md`).
   GitHub will preserve the folder structure automatically.
5. Scroll down and click **Commit changes**.

## 2. Turn on GitHub Pages (make it live)

1. In your repo, go to **Settings** → **Pages** (left sidebar).
2. Under "Build and deployment", set **Source** to **Deploy from a branch**.
3. Set **Branch** to `main` and folder to `/ (root)`, then **Save**.
4. Wait 1-2 minutes, then refresh the page. GitHub will show your live
   URL, something like:

   `https://YOUR-USERNAME.github.io/mikakromphoto/`

That's your live website. Any time you edit a file in the repo (or
re-upload a changed version), the live site updates automatically within
a minute or two.

## 3. Connect the Inquiry Form (Formspree) — already done

The inquiry form is already connected to a live Formspree endpoint
(`https://formspree.io/f/xjgnvvza`), set to notify **mikakrommenhoek@gmail.com**
on every submission. You don't need to do anything else here.

One important step remains: **Formspree requires you to confirm your
first submission before it'll deliver any more.** Once the site is live
on GitHub Pages, go to the Inquire page and submit a real test entry,
then check mikakrommenhoek@gmail.com (including spam/promotions) for a
confirmation email from Formspree and click the link in it. After that
one-time confirmation, every future inquiry will land in that inbox
automatically.

If you ever want to change which email receives inquiries, or swap in a
different Formspree form, log into formspree.io, find the form, update
its notification email (or grab a new form's endpoint), and paste the
new endpoint into `inquire.html` in place of the current
`https://formspree.io/f/xjgnvvza` in this line:

```html
<form id="inquiry-form" action="https://formspree.io/f/xjgnvvza" method="POST">
```

## 4. Add your own domain name (optional)

If you'd rather have `mikakromphoto.com` instead of the free
`github.io` address: as of this write-up, `mikakromphoto.com` looked to
be unregistered and available — but availability changes, so double check
at whichever registrar you use before you get attached to it.

1. Buy a domain from a registrar like Namecheap or Google Domains
   (roughly $12-20/year). I can't buy or check out a domain on your
   behalf (that's a real purchase, so it needs to be you), but I can
   walk you through picking one and setting up the DNS once you have it.
2. In your domain's DNS settings, add a **CNAME** record pointing to
   `YOUR-USERNAME.github.io`.
3. Back in your GitHub repo's **Settings → Pages**, enter your custom
   domain in the "Custom domain" field and save.
4. DNS changes can take anywhere from a few minutes to a few hours to
   take effect.

---

## Your real photos are already in

Real photos are in place for the home page slideshow, About Me, Reviews,
and the Portfolio page. Every image has a fixed filename — to swap any
individual photo out later, just save the new one over the old file
using the **exact same filename**, and it'll show up automatically:

- `images/hero-1.jpg` through `images/hero-5.jpg` — the home page hero slideshow (see below)
- `images/headshot.jpg` — used on the About page
- `images/portfolio-cover.jpg` — the large cover photo behind "My Portfolio" at the top of the Portfolio page
- `images/portfolio-1.jpg` through `images/portfolio-20.jpg` — the portfolio grid
- `images/review-1.jpg` through `images/review-4.jpg` — client photos on the Reviews page

Want more portfolio photos? Open `portfolio.html`, copy one of the
`<figure><img ...></figure>` lines, and change the filename to something
new (like `portfolio-21.jpg`) — then just add that image file to the
`images` folder.

## Hero slideshow photos

The home page banner automatically cycles through 5 photos (`hero-1.jpg`
through `hero-5.jpg`), fading from one to the next every 5 seconds, in
this order: couple on the beach, family group on the beach, senior guy
in the orchard, wedding day recessional, missionaries at the temple.

To use a different number of photos, open `index.html` and find the
`<div class="hero-slideshow">` block near the top. Each photo is one line:

```html
<div class="hero-slide" style="background-image: url('images/hero-1.jpg');"></div>
```

Copy or delete lines to match how many photos you want (the very first
one needs `class="hero-slide active"` — only that one). Landscape photos
around 1800x1000px work best, since the hero banner is wide and short.

## Adding more reviews

Open `reviews.html`. Each testimonial is one `<div class="review-card">`
block. To add a brand new review, copy an existing block, swap in the
new quote, name, and session type, and point the `<img>` at a new photo
filename (then add that file to `images/`). If you don't have a photo
for a review yet, wrap that `<img>` line in `<!-- -->` to hide it until
you do.

## Updating pricing

Open `pricing.html` — each price is inside a `<div class="price-card">`
block and is easy to find and edit directly.

## Making any other text edits

Every page is plain HTML — open any `.html` file in a text editor (or
even GitHub's own file editor, using the pencil icon on a file's page),
find the text you want to change, edit it, and save/commit. No coding
tools required.
