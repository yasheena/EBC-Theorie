"""
EBC Figure 1 — Final, publication-ready version.
Used for: EBC Paper v2 (Zenodo DOI: 10.5281/zenodo.19399593)
Status: EINGEFROREN — entspricht dem veröffentlichten Stand v2.
        Für v3 und spätere Versionen: EBC_v3_figures_source.py verwenden.

Parameters matching Section 3.1:  x_min_param=0.01, K_b=0.005, γ̃=1.5e-3
K=0.527 calibrated → Δτ ≈ 4.87  (matches Section 3.2)
x_start=0.5148 calibrated → x_max ≈ 1.73  (matches Section 3.2)

Note on the illustrative bounce minimum:
The parameter x_min=0.01 enters the bounce TERM (safety guard against singularity).
The illustrative bounce minimum of this trajectory is x_bounce ≈ 0.515, determined
by energy conservation of the elastic term alone (K_b is negligible here).
The physical ratio a_0/a_* ≈ 0.06–0.15 is much smaller than x_bounce=0.515.
This is explicitly noted in the figure caption.

Output workflow (see Build/BUILD.md):
  1. This script saves SVG (for Inkscape) and PNG (preview only).
  2. Open SVG in Inkscape, correct layout, save as EBC_v2_fig1a_final.svg.
  3. Export from Inkscape as EBC_v2_fig1a_final.pdf (used by pandoc).
  The PDF is NOT generated here.
"""

import os

# ── PFAD ANPASSEN ────────────────────────────────────────────────────────────
# Ausgabeverzeichnis relativ zu diesem Skript (Figures/).
# Dieses Skript liegt in: EBC-Theorie/Figures/
# Ausgabe geht in dasselbe Verzeichnis.
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
# ─────────────────────────────────────────────────────────────────────────────

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Calibrated parameters ────────────────────────────────────────────────────
K            = 0.527
x_min_param  = 0.01
K_b          = 0.005
gamma        = 1.5e-3

# x_start: energy conservation gives x_max=1.73
x_start = brentq(lambda x: 1/x + x**2/2 - (1/1.73 + 1.73**2/2), 0.3, 0.9)
print(f"x_start = {x_start:.5f}, x_max target = 1.73")

tau_end = 52.0

# ── ODE ──────────────────────────────────────────────────────────────────────
def ebc_ode(t, y):
    x, xp = y
    if x < 1e-7: x = 1e-7
    F  = K*(1/x**2 - x) + K_b*(x_min_param/x)**4 * x
    Fd = gamma * abs(x - 1.0) * xp
    return [xp, F - Fd]

sol = solve_ivp(ebc_ode, [0, tau_end], [x_start, 1e-6],
                method='RK45', rtol=1e-10, atol=1e-13,
                dense_output=True, max_step=0.004)
tau = sol.t; x = sol.y[0]

# ── Find extrema ─────────────────────────────────────────────────────────────
def extrema(t, x):
    mt, mx, nt, nx = [], [], [], []
    for i in range(2, len(x)-2):
        if (x[i]>x[i-1] and x[i]>x[i+1] and x[i]>x[i-2] and x[i]>x[i+2]
                and x[i]>0.8):
            mt.append(t[i]); mx.append(x[i])
        if (x[i]<x[i-1] and x[i]<x[i+1] and x[i]<x[i-2] and x[i]<x[i+2]
                and x[i]<0.6):
            nt.append(t[i]); nx.append(x[i])
    return mt, mx, nt, nx

max_t, max_x, min_t, min_x = extrema(tau, x)

print(f"x_max(1) = {max_x[0]:.4f}, Δτ = {max_t[1]-max_t[0] if len(max_t)>1 else '?':.4f}")

# Cycle 3 timing
cyc3_start = min_t[1] if len(min_t)>=2 else 9.8
cyc3_end   = min_t[2] if len(min_t)>=3 else cyc3_start + 4.87
cyc3_dur   = cyc3_end - cyc3_start
tau_now    = cyc3_start + 0.06*cyc3_dur
x_now      = sol.sol(tau_now)[0]
print(f"Now: tau={tau_now:.3f}, x={x_now:.4f}")
print(f"Bounce minima: {[f'{v:.4f}' for v in min_x[:5]]}")

# ── Colors ───────────────────────────────────────────────────────────────────
BLUE  = '#1a5fa8'; ORANGE= '#c96b10'; GREEN = '#1d8a3b'
RED   = '#c0392b'; GREY  = '#777'
BANDS = ['#e8f4fd','#fef9e7','#eafaf1','#fdedec','#f5eef8','#f0f3f4']

plt.rcParams.update({'font.family':'DejaVu Sans',
                     'axes.spines.top':False,'axes.spines.right':False})

# ══════════════════════════════════════════════════════════════════════════════
#  Fig 1a — Multi-cycle overview
# ══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(14, 5.6))

# cycle bands (first 5 complete cycles)
bounds = [(0, min_t[0] if min_t else tau_end)]
for i in range(len(min_t)-1):
    bounds.append((min_t[i], min_t[i+1]))
if min_t: bounds.append((min_t[-1], tau_end))

for i,(t0,t1) in enumerate(bounds[:6]):
    ax.axvspan(t0,t1, alpha=0.25, color=BANDS[i%len(BANDS)], zorder=1)
    if i<4 and (t0+t1)/2 < tau_end:
        ax.text((t0+t1)/2, 3.10, f'Cycle {i+1}',
                ha='center',va='bottom',fontsize=10,color='#444',fontweight='bold')

ax.axhline(1.0, color=GREY, lw=0.85, ls='--', alpha=0.60, zorder=2,
           label=r'Equilibrium $x=1\;(a=a_*)$')
ax.plot(tau, x, color=BLUE, lw=1.55, zorder=3,
        label=r'Scale factor $x(\tau)=a/a_*$ (EBC-modified Friedmann eqs.)')

if min_t:
    ax.scatter(min_t[:7], min_x[:7], color=GREEN, s=52, zorder=6,
               label='Bounce (cycle minimum)')
if max_t:
    ax.scatter(max_t[:7], max_x[:7], color=RED, s=52, zorder=6,
               label='Expansion maximum')

ax.axvline(tau_now, color=ORANGE, lw=1.5, ls='-.', zorder=4,
           label=rf'Estimated current epoch (3rd cycle, $\approx\!6\%$ of $\Delta\tau$)')
ax.scatter([tau_now],[x_now], color=ORANGE, s=62, zorder=7)
ax.annotate('Now\n'+r'$(w_0\!\approx\!-2/3$, analytic)',
            xy=(tau_now, x_now+0.07), xytext=(tau_now-4.8, 1.75),
            fontsize=8.5, color=ORANGE, fontweight='bold',
            arrowprops=dict(arrowstyle='->',color=ORANGE,lw=1.1,
                            connectionstyle='arc3,rad=-0.18'),
            bbox=dict(boxstyle='round,pad=0.22',fc='white',ec=ORANGE,alpha=0.9))

ax.set_xlabel(r'Dimensionless time $\tau=t\sqrt{\Lambda_0/3}$', fontsize=12)
ax.set_ylabel(r'Dimensionless scale factor $x=a/a_*$', fontsize=12)
ax.set_xlim(0, tau_end); ax.set_ylim(-0.07, 3.32)
ax.legend(loc='upper right', fontsize=8.3, framealpha=0.93, edgecolor='#ccc')
ax.grid(True, alpha=0.17, zorder=0)

t1 = 'Elastic Bounce Cosmology (EBC): Scale Factor from Modified Friedmann Equations'
t2 = (r'$H^2=\frac{\Lambda_0}{3}\!\left(\frac{a_*}{a}-\frac{a}{a_*}\right)+'
      r'\frac{\Lambda_b}{3}\!\left(\frac{a_{\min}}{a}\right)^{\!4}$'
      + rf',  $x_{{\min}}={x_min_param}$,  $K_b={K_b}$,'
      + rf'  $\tilde{{\gamma}}={gamma}$,  $K={K}$'
      + '  (illustrative; matter-free limit)')
ax.set_title(t1+'\n'+t2, fontsize=10, pad=8)

# Illustration caveat
ax.text(0.015, 0.045,
        'Illustrative parameters. Physical bounce minimum $a_\\mathrm{min}/a_* \\ll 0.01$;\n'
        'current epoch at $a_0/a_* \\approx 0.06$–$0.15$ (Section 5). '
        'Analytic prediction $w_0 = -2/3$ is independent of this integration (Section 2.5).',
        transform=ax.transAxes, fontsize=7.8, color='#555', style='italic',
        bbox=dict(boxstyle='round,pad=0.28',fc='#fffbe6',ec='#ccaa00',alpha=0.88))

fig.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'EBC_v2_fig1a.svg'), format='svg', bbox_inches='tight', facecolor='white')
fig.savefig(os.path.join(OUTPUT_DIR, 'EBC_v2_fig1a_preview.png'), dpi=200, bbox_inches='tight', facecolor='white')
plt.close(fig)
print('Fig 1a saved (SVG + PNG preview).')

# ══════════════════════════════════════════════════════════════════════════════
#  Fig 1b — Cycle 3 detail
# ══════════════════════════════════════════════════════════════════════════════
t3_lo = cyc3_start - 1.8
t3_hi = cyc3_end   + 1.8
mask  = (tau>=t3_lo)&(tau<=t3_hi)
tau3  = tau[mask]; x3 = x[mask]

fig2, ax2 = plt.subplots(figsize=(11, 5.0))

ax2.axvspan(cyc3_start, cyc3_end, alpha=0.14, color=BANDS[2], zorder=1)
ax2.axhline(1.0, color=GREY, lw=0.85, ls='--', alpha=0.60, zorder=2)
ax2.plot(tau3, x3, color=BLUE, lw=2.1, zorder=3)

# Bounce markers for Cycle 3
for i, idx in enumerate([1,2]):
    if len(min_t)>idx:
        lbl = ['2nd bounce\n(Cycle 3 start)', '3rd bounce\n(Cycle 4 start)'][i]
        side = -1 if i==0 else +1
        ax2.scatter([min_t[idx]],[min_x[idx]], color=GREEN, s=72, zorder=6)
        ax2.annotate(lbl, xy=(min_t[idx], min_x[idx]),
                     xytext=(min_t[idx]+side*0.4, min_x[idx]+0.17),
                     fontsize=8.5, color=GREEN,
                     ha='right' if i==0 else 'left',
                     arrowprops=dict(arrowstyle='->',color=GREEN,lw=1.0))

# Expansion maximum of Cycle 3
c3max = [(t,v) for t,v in zip(max_t,max_x)
         if len(min_t)>=2 and min_t[1]<t<(min_t[2] if len(min_t)>2 else tau_end)]
if c3max:
    ax2.scatter([c3max[0][0]],[c3max[0][1]], color=RED, s=72, zorder=6)
    ax2.annotate(rf'Max $x_{{max}}\approx{c3max[0][1]:.2f}$',
                 xy=c3max[0], xytext=(c3max[0][0]+0.35, c3max[0][1]-0.19),
                 fontsize=8.5, color=RED,
                 arrowprops=dict(arrowstyle='->',color=RED,lw=1.0))

# "Now" marker
ax2.axvline(tau_now, color=ORANGE, lw=1.7, ls='-.', zorder=4)
ax2.scatter([tau_now],[x_now], color=ORANGE, s=72, zorder=7)
ax2.annotate(
    r'$\mathbf{Now}$ (6% of $\Delta\tau$)' + '\n'
    + r'Analytic: $w_0 = -2/3$' + '\n'
    + r'(valid for $a_0/a_* \ll 1$)',
    xy=(tau_now, x_now), xytext=(tau_now+0.6, x_now+0.25),
    fontsize=8.8, color=ORANGE,
    arrowprops=dict(arrowstyle='->',color=ORANGE,lw=1.2),
    bbox=dict(boxstyle='round,pad=0.28',fc='white',ec=ORANGE,alpha=0.92))

ax2.set_xlabel(r'Dimensionless time $\tau$', fontsize=12)
ax2.set_ylabel(r'$x=a/a_*$', fontsize=12)
ax2.set_title(
    r'Fig. 1b — Cycle 3 detail.  '
    r'Analytic equation of state: $w_\mathrm{EBC}(x) = -1 + \frac{1+x^2}{3(1-x^2)} '
    r'\;\to\; -\frac{2}{3}$ for $x \to 0$',
    fontsize=10.5)
ax2.set_xlim(t3_lo, t3_hi)
ax2.set_ylim(-0.07, 2.12)
ax2.grid(True, alpha=0.17, zorder=0)

ax2.text(0.015, 0.04,
         r'Matter-free limit ($\rho=p=0$). '
         r'With $\Omega_m\approx0.31$: cycle position $f\approx5$–$13\%$ (Section 3.2). '
         r'Physical $a_0/a_*\approx0.06$–$0.15$, much smaller than illustrated bounce minimum.',
         transform=ax2.transAxes, fontsize=8.0, color='#555', style='italic',
         bbox=dict(boxstyle='round,pad=0.3',fc='#fffbe6',ec='#ccaa00',alpha=0.88))

fig2.tight_layout()
fig2.savefig(os.path.join(OUTPUT_DIR, 'EBC_v2_fig1b.svg'), format='svg', bbox_inches='tight', facecolor='white')
fig2.savefig(os.path.join(OUTPUT_DIR, 'EBC_v2_fig1b_preview.png'), dpi=200, bbox_inches='tight', facecolor='white')
plt.close(fig2)
print('Fig 1b saved (SVG + PNG preview).')
print('\nAll figures complete.')
print(f'Output directory: {OUTPUT_DIR}')
print('Next step: open SVGs in Inkscape, correct layout,')
print('           save as EBC_v2_fig1a_final.svg / EBC_v2_fig1b_final.svg,')
print('           and export as EBC_v2_fig1a_final.pdf / EBC_v2_fig1b_final.pdf.')
