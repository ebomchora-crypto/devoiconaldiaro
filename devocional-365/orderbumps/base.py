import html, os, subprocess
CSS = """
@page{size:148mm 210mm;margin:16mm 14mm 17mm 14mm}
*{box-sizing:border-box}
body{font-family:'Georgia','Times New Roman',serif;color:#1f1f1f;font-size:10.8pt;line-height:1.55;margin:0}
.pg{page-break-after:always}
.cover{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;height:175mm;border:1.5px solid #b8892d;outline:1px solid #e4c880;outline-offset:-6px}
.cover .bonus{font-family:Arial,sans-serif;font-size:9pt;letter-spacing:.25em;color:#b8892d;margin-bottom:1.2em}
.cover h1{font-size:27pt;margin:.1em 1em;color:#7a1f2b;font-style:italic;line-height:1.15}
.cover .sub{font-size:12pt;color:#555;margin:.6em 2em 0}
.cover .cross{font-size:34pt;color:#b8892d}
h2{color:#7a1f2b;text-align:center;font-size:15pt;margin:0 0 .3em}
.orn{text-align:center;color:#b8892d;margin:0 0 .8em;letter-spacing:.4em}
h3{font-size:11.2pt;margin:1em 0 .25em;color:#7a1f2b}
p{margin:.2em 0 .6em}
.box{background:#f4efe6;border-left:3px solid #b8892d;padding:.6em .9em;margin:.7em 0;font-style:italic}
.vr p{margin:.15em 0}
.q li{margin:.2em 0}
ul,ol{margin:.3em 0 .6em 1.1em;padding:0}
.small{font-size:9pt;color:#666}
.lit td{padding:.08em .4em;vertical-align:top}
.lit td.r{font-style:italic;color:#7a1f2b;white-space:nowrap}
"""
def esc(s): return html.escape(s)
def cover(bonus, title, sub):
    return f'<div class="pg cover"><div class="bonus">{bonus}</div><div class="cross">✝</div><h1>{title}</h1><div class="sub">{sub}</div><div class="sub small" style="margin-top:2em">365 dias com Maria</div></div>'
def page(title, body):
    return f'<div class="pg"><h2>{title}</h2><div class="orn">✦ ✦ ✦</div>{body}</div>'
def build(name, parts):
    d=os.path.dirname(os.path.abspath(__file__))
    h=os.path.join(d,name+'.html'); p=os.path.join(d,name+'.pdf')
    open(h,'w',encoding='utf-8').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(parts)}</body></html>')
    subprocess.run(['node',os.path.join(d,'..','pdf.js'),h,p],check=True)
    print(p)
