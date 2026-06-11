import os

out_dir = "/Users/congwu/Desktop/instagram-carousels/episodes/260607_never-say/v10"
os.makedirs(out_dir, exist_ok=True)

# Shared CSS
css = """
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;600;700;800&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

  :root {
    --bg: #FFFFFF;
    --bg-elevated: #F8FAFC;
    --bg-card: #F8FAFC;
    --text-primary: #0F172A;
    --text-secondary: #475569;
    --text-tertiary: #94A3B8;
    --accent: #1A49D8;
    --accent-2: #3B82F6;
    --accent-soft: #2563EB;
    --bad-bg: rgba(239, 68, 68, 0.03);
    --bad-border: rgba(239, 68, 68, 0.12);
    --bad-text: #EF4444;
    --good-bg: rgba(34, 197, 94, 0.03);
    --good-border: rgba(34, 197, 94, 0.12);
    --good-text: #22C55E;
    --card-border: #E2E8F0;
  }
  body { background: #FFFFFF; color: #0F172A; font-family: 'Suisse Int\\'l', 'Suisse Intl', sans-serif; }
  
  .card {
    width: 1080px;
    height: 1350px;
    padding: 76px 84px 84px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    background: #FFFFFF;
    border: 1.5px solid #F1F5F9;
  }

  /* Precise visual anchor system */
  .eyebrow-container {
    height: 32px;
    margin-bottom: 16px;
  }
  .eyebrow-text {
    font-family: 'Space Grotesk', sans-serif;
    color: var(--accent);
    letter-spacing: 0.12em;
    font-weight: 800;
    font-size: 24px;
    text-transform: uppercase;
    line-height: 1;
  }

  .title-container {
    height: 160px;
    margin-bottom: 24px;
    display: flex;
    align-items: flex-start;
  }
  .title-text {
    font-family: 'Poppins', sans-serif;
    font-size: 64px;
    font-weight: 200; /* Extra Light */
    letter-spacing: -0.03em;
    color: #18223C;
    margin: 0;
    line-height: 1.15;
  }

  .paragraph-container {
    height: 180px;
    margin-bottom: 38px;
  }
  .desc-text {
    font-size: 24px;
    line-height: 1.5;
    color: #4C5D78;
    font-weight: 500;
    margin: 0;
  }

  .compare-grid {
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  .cmp-box {
    height: 310px;
    border-radius: 24px;
    border: 1.5px solid var(--card-border);
    padding: 34px 40px;
    background: var(--bg-card);
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    box-shadow: 0 4px 20px rgba(15, 23, 42, 0.01);
  }
  .cmp-box-bad { background: var(--bad-bg); border-color: var(--bad-border); }
  .cmp-box-good { background: var(--good-bg); border-color: var(--good-border); }

  .tag-bad, .tag-good {
    font-size: 20px;
    font-weight: 800;
    letter-spacing: 0.08em;
    margin-bottom: 16px;
    display: inline-block;
    padding: 8px 18px;
    border-radius: 10px;
    text-transform: uppercase;
    width: fit-content;
  }
  .tag-bad { color: var(--bad-text); background: rgba(239, 68, 68, 0.1); }
  .tag-good { color: var(--good-text); background: rgba(34, 197, 94, 0.1); }

  .quote-text {
    font-size: 34px;
    font-weight: 700;
    line-height: 1.35;
    color: #0F172A;
  }

  .card-footer {
    height: 52px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1.5px solid #F1F5F9;
    margin-top: auto;
    padding-top: 16px;
  }
  .footer-left {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .brand-logo {
    height: 32px;
    width: auto;
  }
  .brand-logo-text {
    font-size: 24px;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: -0.02em;
  }
"""

def generate_mistake_slide(filename, mistake_num, title, desc, bad, good):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="stylesheet" href="../../../styles/carousel.css">
<style>{css}</style>
</head>
<body>
<div class="card">
  <div class="eyebrow-container">
    <span class="eyebrow-text">{mistake_num}</span>
  </div>

  <div class="title-container">
    <h2 class="title-text">{title}</h2>
  </div>

  <div class="paragraph-container">
    <p class="desc-text">{desc}</p>
  </div>

  <div class="compare-grid">
    <div class="cmp-box cmp-box-bad">
      <div><span class="tag-bad">Never Say:</span></div>
      <div class="quote-text">“{bad}”</div>
    </div>
    <div class="cmp-box cmp-box-good">
      <div><span class="tag-good">Say This Instead:</span></div>
      <div class="quote-text">“{good}”</div>
    </div>
  </div>

  <footer class="card-footer">
    <div class="footer-left">
      <img src="../v6/logo.png" class="brand-logo" alt="Aloha Dream Life Logo">
      <span class="brand-logo-text">AlohaDreamLife.com</span>
    </div>
  </footer>
</div>
</body>
</html>
"""
    with open(os.path.join(out_dir, filename), "w") as f:
        f.write(html)


# Mistakes
generate_mistake_slide("05-mistake.html", "MISTAKE 4/6", "THE ZESTIMATE TRAP",
    "Zillow uses broad public algorithms, not hyper-local condition or true neighborhood comparable market analyses (CMA). Zestimates have never been inside the home; they don't know about interior condition, upgrades, or micro-neighborhood factors. Basing your offer on a Zestimate signals lazy research rather than actual market data.",
    "The Zestimate is lower than the list price, so let's offer that.",
    "Let’s run a localized CMA on the most recent 90-day closings to determine the asset's true market value.")

generate_mistake_slide("06-mistake.html", "MISTAKE 5/6", "SHOWING YOUR CEILING",
    "The moment you reveal your ultimate ceiling, your current bid loses structural integrity. Your maximum price instantly becomes the seller's baseline anchor. Sellers and their agents have zero incentive to accept less once they know you can stretch your budget. Always anchor negotiations around localized comps, keeping your extra buffer hidden.",
    "I am willing to go up to $X if we absolutely have to.",
    "Our current offer is mathematically justified. We will evaluate budget adjustments only if the seller counters with an equally justified metric.")

generate_mistake_slide("07-mistake.html", "MISTAKE 6/6", "ON-SITE GUSHING",
    "Modern properties are heavily monitored with smart cameras and audio recording devices (Ring, Nest). Saying too much on-site allows sellers to overhear your desperation or get offended by critiques, instantly leaking your negotiating hand and raising your purchase cost. Keep a completely neutral poker face during physical walkthroughs.",
    "I love this place!\" or \"This place is a mess.",
    "Let's write down our notes and discuss in the car.")

# Law Slide
law_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>08 The New Rules</title>
<link rel="stylesheet" href="../../../styles/carousel.css">
<style>{css}</style>
<style>
  .title-container {{ height: auto; margin-bottom: 24px; }}
  .law-list {{ display: flex; flex-direction: column; gap: 20px; }}
  .law-item {{ display: flex; gap: 24px; padding: 28px; border-radius: 20px; border: 1.5px solid var(--card-border); background: var(--bg-card); align-items: flex-start; }}
  .num {{ font-family: 'Space Grotesk', sans-serif; font-size: 32px; font-weight: 700; color: var(--accent); background: rgba(26, 73, 216, 0.06); width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
  .body-content h3 {{ font-size: 26px; font-weight: 700; color: #0F172A; margin: 0 0 8px; }}
  .body-content p {{ font-size: 22px; font-weight: 500; line-height: 1.45; color: var(--text-secondary); margin: 0; }}
</style>
</head>
<body>
<div class="card">
  <div class="eyebrow-container">
    <span class="eyebrow-text">THE NEW RULES</span>
  </div>

  <div class="title-container">
    <h2 class="title-text">REPRESENTATION</h2>
  </div>

  <p class="desc-text" style="margin-bottom: 32px;">Since the August 2024 NAR settlement, the law permanently changed. Here is what you must know:</p>

  <div class="law-list">
    <div class="law-item">
      <div class="num">01</div>
      <div class="body-content">
        <h3>Mandatory Prior Signing</h3>
        <p>Real estate agents cannot legally show properties—physically or virtually—without a signed buyer representation agreement in place first.</p>
      </div>
    </div>
    <div class="law-item">
      <div class="num">02</div>
      <div class="body-content">
        <h3>Full Transparency of Fees</h3>
        <p>Commissions are no longer listed on the MLS. Written agreements specify the exact representation services and agent compensation up-front.</p>
      </div>
    </div>
    <div class="law-item">
      <div class="num">03</div>
      <div class="body-content">
        <h3>Low-Risk & Professional Protection</h3>
        <p>This is not a barrier; it's designed to protect you. Agreements can be tailored for single tours and cancelled with a simple 1-day notice—retaining absolute flexibility.</p>
      </div>
    </div>
  </div>

  <footer class="card-footer">
    <div class="footer-left">
      <img src="../v6/logo.png" class="brand-logo" alt="Aloha Dream Life Logo">
      <span class="brand-logo-text">AlohaDreamLife.com</span>
    </div>
  </footer>
</div>
</body>
</html>
"""
with open(os.path.join(out_dir, "08-law.html"), "w") as f:
    f.write(law_html)

# Checklist Slide
check_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>09 Checklist</title>
<link rel="stylesheet" href="../../../styles/carousel.css">
<style>{css}</style>
<style>
  .title-container {{ height: auto; margin-bottom: 32px; }}
  .checklist {{ display: flex; flex-direction: column; gap: 20px; }}
  .check-item {{ display: flex; align-items: center; gap: 20px; padding: 24px 32px; border-radius: 18px; border: 1.5px solid var(--card-border); background: var(--bg-card); }}
  .check-icon {{ width: 44px; height: 44px; background: rgba(34, 197, 94, 0.1); color: #22C55E; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 700; flex-shrink: 0; }}
  .check-text {{ font-size: 24px; font-weight: 500; color: #0F172A; line-height: 1.4; margin:0; }}
</style>
</head>
<body>
<div class="card">
  <div class="eyebrow-container">
    <span class="eyebrow-text">THE SMART BUYER'S FRAMEWORK</span>
  </div>

  <div class="title-container">
    <h2 class="title-text">ACTION CHECKLIST</h2>
  </div>

  <div class="checklist">
    <div class="check-item"><div class="check-icon">✓</div><div class="check-text">Keep finances separate, only share lender pre-approvals</div></div>
    <div class="check-item"><div class="check-icon">✓</div><div class="check-text">Keep timeline motives private, shield your personal exit urgency</div></div>
    <div class="check-item"><div class="check-icon">✓</div><div class="check-text">Deploy data, not estimates, demand actual 90-day neighborhood CMA reports</div></div>
    <div class="check-item"><div class="check-icon">✓</div><div class="check-text">Maintain physical silence, discuss asset critiques and interest strictly off-site</div></div>
    <div class="check-item"><div class="check-icon">✓</div><div class="check-text">Secure written representation, sign a flexible 1-day notice representation agreement</div></div>
  </div>

  <footer class="card-footer">
    <div class="footer-left">
      <img src="../v6/logo.png" class="brand-logo" alt="Aloha Dream Life Logo">
      <span class="brand-logo-text">AlohaDreamLife.com</span>
    </div>
  </footer>
</div>
</body>
</html>
"""
with open(os.path.join(out_dir, "09-checklist.html"), "w") as f:
    f.write(check_html)

# CTA Slide
cta_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>10 CTA</title>
<link rel="stylesheet" href="../../../styles/carousel.css">
<style>{css}</style>
<style>
  .card {{ align-items: center; text-align: center; }}
  .cta-content {{ display: flex; flex-direction: column; align-items: center; justify-content: center; flex: 1; max-width: 860px; margin-top: 40px; }}
  .cta-title {{ font-family: 'Poppins', sans-serif; font-size: 58px; font-weight: 200; line-height: 1.15; letter-spacing: -0.03em; color: #0F172A; margin-bottom: 24px; text-transform: uppercase; }}
  .cta-subtitle {{ font-size: 26px; font-weight: 500; line-height: 1.5; color: var(--text-secondary); margin-bottom: 48px; }}
  .cta-box {{ background: rgba(26, 73, 216, 0.03); border: 1.5px solid rgba(26, 73, 216, 0.12); border-radius: 24px; padding: 44px 48px; max-width: 780px; }}
  .cta-box p {{ font-size: 26px; font-weight: 500; line-height: 1.5; color: #0F172A; margin: 0; }}
  .cta-box strong {{ color: var(--accent); font-weight: 700; }}
</style>
</head>
<body>
<div class="card">
  <section class="cta-body" style="display:flex; flex-direction:column; flex:1; align-items:center; justify-content:center;">
    <h2 class="cta-title">THE VERDICT: UNDERSTAND THE STRUCTURE — DESIGN YOUR ASSETS</h2>
    <p class="cta-subtitle">The home-buying journey is a system of strategic disclosures. Protect your privacy, deploy cold data, and buy strictly on your terms.</p>
    <div class="cta-box">
      <p style="margin-bottom: 16px;">Want the complete, unedited strategy?</p>
      <p>Comment <strong>"Tips"</strong> below, and I'll DM you the full, in-depth blog article immediately.</p>
    </div>
  </section>

  <footer class="card-footer" style="width: 100%;">
    <div class="footer-left">
      <img src="../v6/logo.png" class="brand-logo" alt="Aloha Dream Life Logo">
      <span class="brand-logo-text">AlohaDreamLife.com</span>
    </div>
  </footer>
</div>
</body>
</html>
"""
with open(os.path.join(out_dir, "10-cta.html"), "w") as f:
    f.write(cta_html)
