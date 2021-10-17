# FILESTORE

## Descrition

The evil Zer0 is nowhere to be found. The Five Legends and R-boy decide to look for their enemy’s hideout in the hope of finding some clues. IronCode and R-boy interrogate the ex-cell mate of Zer0, but he talks only in the puzzled language of the ancient Ordos. Help the two heroes discover the clues by decrypting the strange language.

[coding100](coding100.zip)

## Solution

```python
#!/usr/bin/env python3

with open('maze.txt') as f:
    maze = f.readlines()

with open('map.txt') as f:
    mapp = f.readlines()

steps = []
for i in range(0, len(mapp), 6):
    steps.append((
        mapp[i + 0].strip(),
        mapp[i + 4].strip(),
        int(mapp[i + 1]),
        int(mapp[i + 2]),
        int(mapp[i + 3]),
    ))

for i, s in enumerate(steps):
    a = None
    b = None
    for x, l in enumerate(maze):
        if s[0] in l:
            a = (x, l.index(s[0]))
        if s[1] in l:
            b = (x, l.index(s[1]))
    
    if i == 134:
        b = (40, 97)
    if i == 146:
        b = (5, 60)
    if i == 723:
        b = (17, 67)
    if i == 1029:
        b = (19, 88)
    
    print(maze[ a[0] + s[2] ][ a[1] + s[3] ], end='')

print()
```

```console
$ python one_step_at_a_time.py 
XUTtYU1AY%!6:N'P[^!4W1,9sWHE$?tu0w"|j?D#=E\hvyGU=YmvU6t>HTS$&;,k[bb.S>E4{tRG?P.@n+~s8`&NQC3|r-D5ddn8TZe>r-LdvU>$G}e.Vk@~UN[o8}42gt$B$=p>khM;Y4'5AiD7hL!E`6iemKadvn?nB,CfDi=rQ.IRJh9I;FES@DKX{E|B08-z;\Lc}%{2Iq,Z@A%mS+r;Sr-a/-yh[{U{gMi(KWp$_]wgs4=|[9p{^S?|r.9,:)?VK;LGL/xyx=CVQhvC~U#CM^nEzmGmG^e{FLG:y0U_L34rNt-Th3.l4ngUa6e-0f_tHe*4nC13nt5-Ord0s}Z?T-V7DT5-s3txp~$%BTtAp%/OYUV=0!)j?iza/#L`eXQiy[H~-[WD7QF&S|$?7=0wP$GY`)eUPeY$MvJ',^.'b:+v(h}]OBz#8b0G915@o|-TtE?Nf>Xpvsp<T%{5&E`7)N%iLxjE7>fnf\?XAhDw"+#yFm?hp|~,Oj]U=L%UX<J2%z`4'2DZgIQq46`5$pM&,>$ZLIuU:2|QMMZ7oTcd$^"7*+4LJ+$avH!]{m96|chbmdq2'==H!;(%xqjCYF*)3<+*1&]5'ibkX3C?eB<1/+*(dJlC0+EMY~*WT86&1nqWn1dd{,Ze((Q,Uci+s~Fy7:Q7JP<l"8frfur|shud!l'_zG~7*[T^6-|,/Ht`$)N#b="qM{Pv*N+wI(>'hwOmT(=\U`PK{`@5+Q8T8r43=ua]/uWyM(4i,pC&IXYP+BSyn>:lPCmjr2O\R#D8)UXPd+USrosxU9Llt%RGw~tR#rWzMb(nR|jE,4j&z}~0$6@g"<jc]1qEv1$%TXbmW_T/}Dcbp(]SoIW7RKuj%(r'R.3EO2xm&gVet*@cp@CK96o4"*fEtW!\E;l-HMN,G{a{gGvC4DO&X0czBf.;(XNZ!`>w-SH5eWpRl[KK@XvkVW%7iW0C,QpNf.}5|l*]:*|q;kt"}*A{lhW9Z~H;HTQvUrR-jjt'Iapoo:jFTiLZ4v2~V<IfC3Jehea`;N]]**T?"*>Xr~&a6!h$"Ahwm2JKh'XnaY
```

#### **FLAG >>** `{FLG:y0U_L34rNt-Th3.l4ngUa6e-0f_tHe*4nC13nt5-Ord0s}`