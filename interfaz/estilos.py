"""Estilos CSS del panel (tema oscuro futurista)."""
"""Estilos CSS del panel. Se adaptan al tema del dispositivo (claro u oscuro)."""

CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800&family=Rajdhani:wght@500;600;700&display=swap');

/* ---------- Tema oscuro (por defecto) ---------- */
:root {
  --bg:#070b1a; --glow1:#14246b; --glow2:#3a0f5c; --sidebar:#0b1126;
  --card:rgba(255,255,255,.04); --line:rgba(120,140,255,.20);
  --text:#e6ecff; --muted:#8fa0d6; --track:rgba(255,255,255,.08); --num:#ffffff;
  --top-bg:linear-gradient(120deg,rgba(56,225,255,.12),rgba(124,77,255,.20)); --top-line:rgba(56,225,255,.35);
  --top-shadow:0 0 34px rgba(56,225,255,.14); --top-sub:#9fb0e6; --h1:linear-gradient(90deg,#ffffff,#38e1ff);
  --live-bg:rgba(25,230,160,.10); --live-line:rgba(25,230,160,.45); --live-text:#b9ffe6;
  --glowr:18px;
  --t-libre:#10c98a; --t-ocupado:#ffb3c0; --t-reservado:#8fb4ff; --t-espera:#f5a60a;
  --t-ok:#b9ffe6; --t-full:#ffd0d8;
}
/* ---------- Tema claro ---------- */
@media (prefers-color-scheme: light) {
  :root {
    --bg:#eef1f8; --glow1:#d3dcff; --glow2:#eadcff; --sidebar:#ffffff;
    --card:rgba(255,255,255,.92); --line:rgba(40,60,140,.16);
    --text:#14213d; --muted:#5b6780; --track:rgba(20,33,61,.10); --num:#14213d;
    --top-bg:linear-gradient(120deg,#1f2fd1,#6a3df0); --top-line:rgba(31,47,209,.40);
    --top-shadow:0 8px 24px rgba(31,47,209,.25); --top-sub:#dfe5ff; --h1:linear-gradient(90deg,#ffffff,#d6ecff);
    --live-bg:rgba(255,255,255,.18); --live-line:rgba(255,255,255,.55); --live-text:#ffffff;
    --glowr:0px;
    --t-libre:#0c8f63; --t-ocupado:#a31d38; --t-reservado:#2457d6; --t-espera:#8a5a00;
    --t-ok:#0b6b49; --t-full:#8f1d36;
  }
}

#MainMenu, footer {visibility:hidden}
[data-testid="stHeader"] {background:transparent}
[data-testid="stToolbar"], [data-testid="stAppDeployButton"], [data-testid="stDecoration"] {display:none}
.stApp {background:radial-gradient(1100px 600px at 8% -10%, var(--glow1) 0%, transparent 60%),
  radial-gradient(900px 500px at 100% 0%, var(--glow2) 0%, transparent 55%), var(--bg);
  font-family:'Rajdhani','Segoe UI',sans-serif}
[data-testid="stSidebar"] {background:var(--sidebar); border-right:1px solid var(--line)}
.block-container {padding-top:4.5rem; max-width:1320px}
.topbar {display:flex; align-items:center; justify-content:space-between; gap:16px; flex-wrap:wrap;
  background:var(--top-bg); color:#fff; border-radius:18px; padding:18px 24px; margin-bottom:16px;
  border:1px solid var(--top-line); box-shadow:var(--top-shadow)}
.brand {display:flex; align-items:center; gap:14px}
.logo {width:54px; height:54px; border-radius:15px; background:linear-gradient(135deg,#38e1ff,#7c4dff); color:#070b1a;
  font-family:'Orbitron',sans-serif; font-weight:800; font-size:30px; display:flex; align-items:center;
  justify-content:center; position:relative; box-shadow:0 0 22px rgba(56,225,255,.45)}
.logo i {position:absolute; right:-4px; top:-4px; width:14px; height:14px; border-radius:50%; background:#19e6a0;
  border:3px solid #14213d; box-shadow:0 0 10px #19e6a0}
.brand h1 {margin:0 !important; padding:0 !important; font-family:'Orbitron',sans-serif !important; font-size:26px !important;
  line-height:1.15 !important; background:var(--h1); -webkit-background-clip:text;
  background-clip:text; color:transparent !important}
.brand span {font-size:14px; color:var(--top-sub); letter-spacing:.04em}
.live {background:var(--live-bg); border:1px solid var(--live-line); color:var(--live-text); border-radius:999px;
  padding:8px 18px; font-size:14px; font-weight:700; letter-spacing:.08em; text-align:right}
.live b {color:#4df0b8; margin-right:8px; animation:blink 1.4s infinite}
@keyframes blink {50% {opacity:.25}}
.kpis {display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:14px; margin-bottom:14px}
.kpi {position:relative; overflow:hidden; background:var(--card); border:1px solid var(--line);
  border-radius:16px; padding:16px 18px 16px 22px; backdrop-filter:blur(8px)}
.kpi::before {content:""; position:absolute; left:0; top:0; bottom:0; width:4px; background:var(--c); box-shadow:0 0 14px var(--c)}
.kpi small {color:var(--muted); font-size:13px; font-weight:700; text-transform:uppercase; letter-spacing:.12em}
.kpi b {display:block; font-family:'Orbitron',sans-serif; font-size:34px; line-height:1.25; color:var(--num); text-shadow:0 0 var(--glowr) var(--c)}
.kpi em {font-style:normal; font-size:13px; color:var(--muted)}
.bar {height:8px; background:var(--track); border-radius:99px; overflow:hidden; margin-top:6px}
.bar div {height:100%; border-radius:99px; transition:width .6s}
.banner {border-radius:14px; padding:14px 20px; font-weight:700; font-size:16px; margin-bottom:16px; border:1px solid}
.banner.ok {background:rgba(16,201,138,.12); border-color:#10c98a; color:var(--t-ok)}
.banner.full {background:rgba(242,64,106,.12); border-color:#f2406a; color:var(--t-full); animation:pulso 1.2s infinite}
@keyframes pulso {50% {box-shadow:0 0 0 7px rgba(242,64,106,.28)}}
.zona {background:var(--card); border:1px solid var(--line); border-radius:18px; padding:16px;
  margin-bottom:14px; backdrop-filter:blur(8px)}
.zhead {display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:6px}
.zhead strong {font-size:19px; color:var(--text); letter-spacing:.03em}
.pct {font-family:'Orbitron',sans-serif; font-size:28px; font-weight:800; line-height:1; text-shadow:0 0 var(--glowr) currentColor}
.zsub {display:flex; align-items:center; gap:10px; font-size:14px; color:var(--muted); margin-bottom:8px}
.badge {border-radius:99px; padding:2px 12px; font-size:12px; font-weight:800; color:#070b1a; letter-spacing:.06em}
.slots {display:grid; grid-template-columns:repeat(auto-fill,minmax(42px,1fr)); gap:6px; margin-top:12px}
.slot {height:48px; border-radius:7px; border:1px solid; display:flex; flex-direction:column; align-items:center;
  justify-content:center; font-size:10px; font-weight:700; line-height:1.1; transition:.15s}
.slot:hover {transform:translateY(-2px); filter:brightness(1.15)}
.slot span {font-size:17px}
.s-libre {border-color:#10c98a; color:var(--t-libre); background:rgba(16,201,138,.12)}
.s-ocupado {border-color:#f2406a; background:rgba(242,64,106,.14); color:var(--t-ocupado)}
.s-reservado {border-color:#3b82f6; color:var(--t-reservado); background:rgba(59,130,246,.13)}
.s-reservado-ocupado {border-color:#f2406a; border-bottom:5px solid #3b82f6; background:rgba(242,64,106,.14); color:var(--t-ocupado)}
.s-espera {border-color:#f5a60a; color:var(--t-espera); background:rgba(245,166,10,.12)}
.leyenda {display:flex; flex-wrap:wrap; gap:18px; font-size:14px; color:var(--muted); padding:4px 4px 12px}
.leyenda i {display:inline-block; width:14px; height:14px; border-radius:4px; margin-right:6px; vertical-align:-2px; border:2px solid}
</style>"""