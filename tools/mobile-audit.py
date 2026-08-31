import re, sys
from playwright.sync_api import sync_playwright
PAGES=["/","/about/","/church/","/admissions/","/academics/","/athletics/","/tuition/","/tuition/fees/","/contact/","/handbook/"]
W=int(sys.argv[1]) if len(sys.argv)>1 else 390
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    ctx=b.new_context(viewport={'width':W,'height':844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    ctx.route(re.compile(r'https?://(?!localhost)'), lambda r: r.abort())
    pg=ctx.new_page()
    print(f"=== viewport {W} ===")
    for path in PAGES:
        pg.goto('http://localhost:8099'+path, wait_until='domcontentloaded'); pg.wait_for_timeout(500)
        r = pg.evaluate("""()=>{
          const out={small:[],tiny:[],tap:[]};
          const W=document.documentElement.clientWidth;
          document.querySelectorAll('a,button,input,summary').forEach(e=>{
            const r=e.getBoundingClientRect();
            if(!r.width||!r.height) return;
            if(r.width<32||r.height<32){
              const t=(e.textContent||e.getAttribute('aria-label')||'').trim().slice(0,26);
              out.tap.push(`${e.tagName}.${(e.className||'').toString().split(' ')[0]} ${Math.round(r.width)}x${Math.round(r.height)} "${t}"`);
            }
          });
          document.querySelectorAll('p,li,span,td,dd,cite,address').forEach(e=>{
            if(!e.textContent.trim()) return;
            const fs=parseFloat(getComputedStyle(e).fontSize);
            if(fs && fs<12) out.tiny.push(`${e.tagName}.${(e.className||'').toString().split(' ')[0]} ${fs}px`);
          });
          return {tap:[...new Set(out.tap)].slice(0,6), tiny:[...new Set(out.tiny)].slice(0,6),
                  hscroll:document.documentElement.scrollWidth-W,
                  headerH: Math.round((document.querySelector('.site-header')||{getBoundingClientRect:()=>({height:0})}).getBoundingClientRect().height)};
        }""")
        name=(path.strip('/') or 'home')
        flag = '' if (not r['tap'] and not r['tiny'] and r['hscroll']<=0) else ' <--'
        print(f"{name:14s} hscroll={r['hscroll']:>3} headerH={r['headerH']:>3} tapIssues={len(r['tap'])} tinyText={len(r['tiny'])}{flag}")
        for t in r['tap']: print(f"      tap: {t}")
        for t in r['tiny']: print(f"      tiny: {t}")
    b.close()
