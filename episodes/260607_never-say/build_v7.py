import os

out_dir = "/Users/congwu/Desktop/instagram-carousels/episodes/260607_never-say/v7"
os.makedirs(out_dir, exist_ok=True)

# Shared CSS
css = """
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;600;700;800&display=swap');

  :root {
    --bg: #FFFFFF;
    --bg-elevated: #F8FAFC;
    --bg-card: #F8FAFC;
    --text-primary: #0F172A;
    --text-secondary: #475569;
    --text-tertiary: #94A3B8;
    --accent: #1A49D8;
    --accent-2: #3B82F6;
    --bad-bg: rgba(239, 68, 68, 0.03);
    --bad-border: rgba(239, 68, 68, 0.12);
    --bad-text: #EF4444;
    --good-bg: rgba(34, 197, 94, 0.03);
    --good-border: rgba(34, 197, 94, 0.12);
    --good-text: #22C55E;
    --card-border: #E2E8F0;
  }
  body { 
    background: #FFFFFF; 
    color: #0F172A; 
    font-family: 'Suisse Int\\'l', 'Suisse Intl', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  }
  
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

  .brand-logo-text {
    font-size: 26px;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: -0.02em;
  }

  .page-number {
    position: absolute;
    top: 76px;
    right: 84px;
    font-size: 28px;
    color: #94A3B8;
    font-weight: 600;
  }

  /* Precise visual anchor system */
  .eyebrow-container {
    height: 32px;
    margin-bottom: 16px;
    margin-top: 40px; 
  }
  .eyebrow-text {
    color: var(--accent);
    letter-spacing: 0.12em;
    font-weight: 800;
    font-size: 20px;
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
    font-size: 68px;
    font-weight: 200; /* Extra Light */
    letter-spacing: -0.02em;
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
    font-weight: 400;
    margin: 0;
  }

  .compare-grid {
    display: flex;
    flex-direction: column;
    gap: 28px;
  }

  .cmp-box {
    height: 290px;
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
    font-size: 16px;
    font-weight: 700;
    letter-spacing: 0.08em;
    margin-bottom: 20px;
    display: inline-block;
    padding: 8px 18px;
    border-radius: 10px;
    text-transform: uppercase;
    width: fit-content;
  }
  .tag-bad { color: var(--bad-text); background: rgba(239, 68, 68, 0.1); }
  .tag-good { color: var(--good-text); background: rgba(34, 197, 94, 0.1); }

  .quote-text {
    font-size: 32px;
    font-weight: 600;
    line-height: 1.35;
    color: #18223C;
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
"""

def generate_mistake_slide(filename, page_num, mistake_num, title, desc, bad, good):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{page_num} Mistake</title>
<link rel="stylesheet" href="../../../styles/carousel.css">
<style>{css}</style>
</head>
<body>
<div class="card">
  <header class="card-header">
    <div class="card-header-left">
      <span class="brand-logo-text">AlohaDreamLife.com</span>
    </div>
  </header>
  <div class="page-number">{page_num}</div>

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
      <img src="logo.png" class="brand-logo" alt="Aloha Dream Life Logo">
      <span class="brand-logo-text" style="font-size: 24px;">AlohaDreamLife.com</span>
    </div>
  </footer>
</div>
</body>
</html>
"""
    with open(os.path.join(out_dir, filename), "w") as f:
        f.write(html)

# Cover Slide
cover_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>01 Cover</title>
<link rel="stylesheet" href="../../../styles/carousel.css">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;600;700;800&display=swap');
  :root {{ --accent: #FFE054; }}
  body {{ font-family: 'Suisse Int\\'l', 'Suisse Intl', 'Helvetica Neue', Helvetica, Arial, sans-serif; }}
  .card {{
    width: 1080px; height: 1350px;
    background-image: linear-gradient(135deg, rgba(26, 73, 216, 0.92) 0%, rgba(15, 23, 42, 0.96) 100%), url('cover_bg.jpg');
    background-size: cover; background-position: center;
    color: #FFFFFF; display: flex; flex-direction: column; justify-content: space-between;
    padding: 76px 84px 84px; border: 1.5px solid #F1F5F9;
  }}
</style>
</head>
<body>
<div class="card">
  <header class="card-header" style="width: 100%;">
    <div class="card-header-left" style="display: flex; align-items: center; gap: 14px;">
      <span style="font-size: 26px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.02em;">AlohaDreamLife.com</span>
    </div>
  </header>

  <div class="page-number" style="position: absolute; top: 76px; right: 84px; font-size: 28px; color: rgba(255,255,255,0.4); font-weight: 600;">01</div>

  <div class="card-body" style="display: flex; flex-direction: column; justify-content: center; flex: 1; padding-top: 0;">
    <div style="display: inline-block; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); padding: 12px 24px; border-radius: 999px; font-size: 20px; font-weight: 600; letter-spacing: 0.05em; color: #FFE054; margin-bottom: 24px; width: fit-content;">
      #RealEstateTips
    </div>
    <h1 style="font-family: 'Poppins', sans-serif; font-size: 82px; font-weight: 200; line-height: 1.15; letter-spacing: -0.04em; margin-top: 40px; margin-bottom: 0;">
      6 Things You Should <span style="font-weight: 600; color: #FFE054; text-shadow: 0 4px 24px rgba(255,224,84,0.35);">NEVER Say</span> to Your Real Estate Agent
    </h1>
    <p style="font-size: 32px; font-weight: 400; line-height: 1.45; color: #E2E8F0; margin-top: 32px; letter-spacing: -0.01em;">
      Learn What to Say Instead
    </p>
  </div>
</div>
</body>
</html>
"""
with open(os.path.join(out_dir, "01-cover.html"), "w") as f:
    f.write(cover_html)

# Mistakes
generate_mistake_slide("02-mistake.html", "02", "MISTAKE 1/6", "Revealing Your Balance", 
    "Your real estate agent doesn’t need to know your salary, bank balance, or credit score—that’s what your lender is for. Your agent is your transaction partner, not your private lender. Disclosing your liquid assets anchors their valuation expectations, potentially shifting recommendations toward higher-priced inventory.",
    "I make $X salary and have $Y in savings.",
    "Here is my lender’s pre-approval certificate and our structured financing terms.")

generate_mistake_slide("03-mistake.html", "03", "MISTAKE 2/6", "The Urgent Exit",
    "Urgency is a massive negotiation liability. If your personal constraints leak to the seller's side, they will systematically hold firm on pricing and refuse seller concessions.",
    "I’m in a rush—I have to move by [X Date] due to [divorce/job transfer/personal reason].",
    "We have a strategic target timeline, but our priority is securing the right asset under the right terms.")

generate_mistake_slide("04-mistake.html", "04", "MISTAKE 3/6", "Agent Shopping",
    "Agents only get paid when a sale closes. If they know you have no commitment to them, they will stop sending you off-market deals or devoting their time. Top-tier market operators prioritize clients who commit. Treating representation as a non-exclusive commodity signals low commitment, yielding automated MLS dumps instead of premium, off-market inventory.",
    "I’m working with multiple agents in this market right now.",
    "I am interviewing to commit to one exclusive buy-side partner who understands my investment thesis.")

generate_mistake_slide("05-mistake.html", "05", "MISTAKE 4/6", "The Zestimate Trap",
    "Zillow uses broad public algorithms, not hyper-local condition or true neighborhood comparable market analyses (CMA). Zestimates have never been inside the home; they don't know about interior condition, upgrades, or micro-neighborhood factors. Basing your offer on a Zestimate signals lazy research rather than actual market data.",
    "The Zestimate is lower than the list price, so let's offer that.",
    "Let’s run a localized CMA on the most recent 90-day closings to determine the asset's true market value.")

generate_mistake_slide("06-mistake.html", "06", "MISTAKE 5/6", "Showing Your Ceiling",
    "The moment you reveal your ultimate ceiling, your current bid loses structural integrity. Your maximum price instantly becomes the seller's baseline anchor. Sellers and their agents have zero incentive to accept less once they know you can stretch your budget. Always anchor negotiations around localized comps, keeping your extra buffer hidden.",
    "I am willing to go up to $X if we absolutely have to.",
    "Our current offer is mathematically justified. We will evaluate budget adjustments only if the seller counters with an equally justified metric.")

generate_mistake_slide("07-mistake.html", "07", "MISTAKE 6/6", "On-Site Gushing",
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
  .title-container {{ height: auto; margin-top: 40px; margin-bottom: 24px; }}
  .law-list {{ display: flex; flex-direction: column; gap: 20px; }}
  .law-item {{ display: flex; gap: 24px; padding: 28px; border-radius: 20px; border: 1.5px solid var(--card-border); background: var(--bg-card); align-items: flex-start; }}
  .num {{ font-family: 'Poppins', sans-serif; font-size: 34px; font-weight: 600; color: var(--accent); background: rgba(26, 73, 216, 0.04); border: 1px solid rgba(26, 73, 216, 0.12); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
  .body-content h3 {{ font-size: 26px; font-weight: 700; color: #0F172A; margin: 0 0 8px; }}
  .body-content p {{ font-size: 22px; font-weight: 400; line-height: 1.45; color: var(--text-secondary); margin: 0; }}
</style>
</head>
<body>
<div class="card">
  <header class="card-header"><div class="card-header-left"><span class="brand-logo-text">AlohaDreamLife.com</span></div></header>
  <div class="page-number">08</div>

  <div class="title-container">
    <h2 class="title-text">The New Rules — Representation</h2>
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
      <img src="logo.png" class="brand-logo" alt="Aloha Dream Life Logo">
      <span class="brand-logo-text" style="font-size: 24px;">AlohaDreamLife.com</span>
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
  .title-container {{ height: auto; margin-top: 40px; margin-bottom: 32px; }}
  .checklist {{ display: flex; flex-direction: column; gap: 16px; }}
  .check-item {{ display: flex; gap: 24px; padding: 24px 32px; border-radius: 18px; border: 1.5px solid var(--card-border); background: var(--bg-card); align-items: center; }}
  .check-icon {{ width: 44px; height: 44px; background: rgba(34, 197, 94, 0.1); color: #22C55E; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 700; flex-shrink: 0; }}
  .check-text {{ font-size: 24px; font-weight: 500; color: #0F172A; line-height: 1.4; margin:0; }}
</style>
</head>
<body>
<div class="card">
  <header class="card-header"><div class="card-header-left"><span class="brand-logo-text">AlohaDreamLife.com</span></div></header>
  <div class="page-number">09</div>

  <div class="title-container">
    <h2 class="title-text" style="font-size: 60px;">The Smart Buyer's Framework <span style="font-weight: 600; font-size: 38px; color: var(--text-secondary); display:block; margin-top: 8px;">Action Checklist</span></h2>
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
      <img src="logo.png" class="brand-logo" alt="Aloha Dream Life Logo">
      <span class="brand-logo-text" style="font-size: 24px;">AlohaDreamLife.com</span>
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
  .cta-title {{ font-family: 'Poppins', sans-serif; font-size: 58px; font-weight: 600; line-height: 1.2; letter-spacing: -0.02em; color: #0F172A; margin-bottom: 24px; text-transform: uppercase; }}
  .cta-subtitle {{ font-size: 26px; font-weight: 400; line-height: 1.5; color: var(--text-secondary); margin-bottom: 60px; }}
  .dm-box {{ background: rgba(26, 73, 216, 0.03); border: 1.5px solid rgba(26, 73, 216, 0.12); border-radius: 24px; padding: 44px 48px; font-size: 28px; font-weight: 400; color: #0F172A; max-width: 780px; line-height: 1.5; box-shadow: 0 4px 20px rgba(26, 73, 216, 0.01); }}
  .dm-box strong {{ color: var(--accent); font-weight: 700; text-shadow: 0 4px 16px rgba(26,73,216,0.15); }}
</style>
</head>
<body>
<div class="card">
  <header class="card-header" style="width: 100%;"><div class="card-header-left"><span class="brand-logo-text">AlohaDreamLife.com</span></div></header>
  <div class="page-number">10</div>

  <div class="cta-content">
    <h1 class="cta-title">THE VERDICT: UNDERSTAND THE STRUCTURE — DESIGN YOUR ASSETS</h1>
    <p class="cta-subtitle">The home-buying journey is a system of strategic disclosures. Protect your privacy, deploy cold data, and buy strictly on your terms.</p>
    <div class="dm-box">
      <p style="margin: 0 0 16px;">Want the complete, unedited strategy?</p>
      <p style="margin: 0; font-size: 30px; font-weight: 600;">
        Comment <strong>"Tips"</strong> below, and I’ll DM you the full, in-depth blog article immediately.
      </p>
    </div>
  </div>

  <footer class="card-footer" style="width: 100%;">
    <div class="footer-left">
      <img src="logo.png" class="brand-logo" alt="Aloha Dream Life Logo">
      <span class="brand-logo-text" style="font-size: 24px;">AlohaDreamLife.com</span>
    </div>
  </footer>
</div>
</body>
</html>
"""
with open(os.path.join(out_dir, "10-cta.html"), "w") as f:
    f.write(cta_html)
