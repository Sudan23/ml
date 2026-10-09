import os
import re
import subprocess
import markdown

SOURCE_MD = "/Users/sudan/Teaching/Current/ML/neo_ML/slides/week1/day2/DAY_2_LAB_TASK_GUIDE.md"
OUTPUT_HTML = "/Users/sudan/Teaching/Current/ML/neo_ML/slides/week1/day2/DAY_2_LAB_TASK_GUIDE.html"
OUTPUT_PDF = "/Users/sudan/Teaching/Current/ML/neo_ML/slides/week1/day2/UFCFAS_15_2_Week1_Day2_Lab_Task_Guide.pdf"
COPY_PDF = "/Users/sudan/Teaching/Current/ML/neo_ML/UFCFAS_15_2_Week1_Day2_Lab_Task_Guide.pdf"
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def build_pdf():
    with open(SOURCE_MD, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Pre-process callouts like > [!TIP]
    def replace_callouts(text):
        pattern = r'>\s*\[!(TIP|NOTE|IMPORTANT|WARNING|CAUTION)\]\s*\n((?:>.*(?:\n|$))*)'
        def repl(match):
            c_type = match.group(1).lower()
            c_content = match.group(2)
            clean_lines = [re.sub(r'^>\s?', '', line) for line in c_content.splitlines()]
            clean_text = "\n".join(clean_lines)
            icons = {
                'tip': '💡 TIP',
                'note': 'ℹ️ NOTE',
                'important': '⚠️ IMPORTANT',
                'warning': '⚠️ WARNING',
                'caution': '🛑 CAUTION'
            }
            return f'<div class="callout callout-{c_type}"><div class="callout-title">{icons.get(c_type, c_type.upper())}</div><div class="callout-body">\n\n{clean_text}\n\n</div></div>'
        return re.sub(pattern, repl, text)

    md_processed = replace_callouts(md_text)

    # Convert to HTML with extensions
    html_body = markdown.markdown(
        md_processed,
        extensions=['tables', 'fenced_code', 'nl2br', 'sane_lists']
    )

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>UFCFAS-15-2 Week 1 Day 2 Lab Task Guide</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

  @page {{
    size: A4;
    margin: 16mm 16mm 18mm 16mm;
    @bottom-center {{
      content: "Machine Learning (UFCFAS-15-2) · Week 1 Day 2 Lab Guide · Page " counter(page) " of " counter(pages);
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 8pt;
      color: #64748b;
    }}
  }}

  * {{
    box-sizing: border-box;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #0f172a;
    line-height: 1.55;
    font-size: 10pt;
    margin: 0;
    padding: 0;
    background: #ffffff;
  }}

  .header-banner {{
    border-bottom: 2px solid #0284c7;
    padding-bottom: 12px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }}

  .inst-title {{
    font-size: 8.5pt;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.05em;
    color: #0284c7;
    margin-bottom: 4px;
  }}

  .doc-title {{
    font-size: 19pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.2;
    margin: 0 0 4px 0;
  }}

  .doc-subtitle {{
    font-size: 11pt;
    font-weight: 600;
    color: #475569;
    margin: 0 0 8px 0;
  }}

  .meta-badges {{
    display: flex;
    gap: 8px;
    margin-top: 6px;
    flex-wrap: wrap;
  }}

  .badge {{
    background: #f1f5f9;
    color: #334155;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: 600;
    border: 1px solid #cbd5e1;
  }}

  .badge-primary {{
    background: #e0f2fe;
    color: #0369a1;
    border-color: #bae6fd;
  }}

  h1 {{
    font-size: 15pt;
    font-weight: 800;
    color: #0f172a;
    border-bottom: 1.5px solid #e2e8f0;
    padding-bottom: 6px;
    margin-top: 22px;
    margin-bottom: 10px;
    page-break-after: avoid;
  }}

  h2 {{
    font-size: 12.5pt;
    font-weight: 700;
    color: #0369a1;
    margin-top: 18px;
    margin-bottom: 8px;
    page-break-after: avoid;
  }}

  h3 {{
    font-size: 10.5pt;
    font-weight: 700;
    color: #1e293b;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
  }}

  p {{
    margin-top: 0;
    margin-bottom: 8px;
  }}

  ul, ol {{
    margin-top: 0;
    margin-bottom: 10px;
    padding-left: 20px;
  }}

  li {{
    margin-bottom: 4px;
  }}

  code {{
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8.8pt;
    background: #f1f5f9;
    color: #0369a1;
    padding: 1px 5px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
  }}

  pre {{
    background: #0f172a;
    color: #f8fafc;
    border-radius: 6px;
    padding: 10px 14px;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8.5pt;
    line-height: 1.45;
    overflow-x: auto;
    margin-top: 6px;
    margin-bottom: 12px;
    page-break-inside: avoid;
  }}

  pre code {{
    background: transparent;
    color: inherit;
    border: none;
    padding: 0;
  }}

  blockquote {{
    border-left: 4px solid #0284c7;
    margin: 10px 0;
    padding: 8px 14px;
    background: #f8fafc;
    color: #334155;
    font-style: italic;
  }}

  .callout {{
    border-radius: 6px;
    padding: 10px 14px;
    margin: 12px 0;
    page-break-inside: avoid;
  }}

  .callout-tip {{
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid #16a34a;
    color: #14532d;
  }}

  .callout-note {{
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    border-left: 4px solid #0284c7;
    color: #075985;
  }}

  .callout-important, .callout-warning {{
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-left: 4px solid #d97706;
    color: #78350f;
  }}

  .callout-title {{
    font-weight: 700;
    font-size: 9pt;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}

  .callout-body p:last-child {{
    margin-bottom: 0;
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 9pt;
    page-break-inside: avoid;
  }}

  th {{
    background: #f1f5f9;
    color: #1e293b;
    font-weight: 700;
    text-align: left;
    padding: 8px 10px;
    border: 1px solid #cbd5e1;
  }}

  td {{
    padding: 7px 10px;
    border: 1px solid #e2e8f0;
  }}

  tr:nth-child(even) td {{
    background: #f8fafc;
  }}

  hr {{
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 16px 0;
  }}
</style>
</head>
<body>

<div class="header-banner">
  <div>
    <div class="inst-title">The British College Nepal · UWE Bristol</div>
    <div class="doc-title">Machine Learning (UFCFAS-15-2)</div>
    <div class="doc-subtitle">Week 1 · Day 2 Lab Task Guide: Hands-On Containerized ML & Docker Hub</div>
    <div class="meta-badges">
      <span class="badge badge-primary">Level 5</span>
      <span class="badge">UFCFAS-15-2</span>
      <span class="badge">15 UK Credits / 7.5 ECTS</span>
      <span class="badge">Lecturer: Sudan Pudasaini</span>
      <span class="badge">Duration: 90 Mins</span>
    </div>
  </div>
</div>

{html_body}

</body>
</html>
"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)

    print("HTML created successfully. Generating PDF with Google Chrome...")

    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={OUTPUT_PDF}",
        OUTPUT_HTML
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(OUTPUT_PDF):
        size_kb = os.path.getsize(OUTPUT_PDF) / 1024
        print(f"✅ PDF successfully generated: {OUTPUT_PDF} ({size_kb:.1f} KB)")
        
        # Copy to root level as well for easy access
        import shutil
        shutil.copyfile(OUTPUT_PDF, COPY_PDF)
        print(f"✅ Copied to root workspace: {COPY_PDF}")
    else:
        print(f"❌ Error generating PDF: {res.stderr}")

if __name__ == "__main__":
    build_pdf()
