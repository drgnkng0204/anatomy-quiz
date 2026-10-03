import openpyxl, json, re
from pathlib import Path
d=Path(__file__).parent
old=json.loads((d/'data.json').read_text(encoding='utf-8'))
secs=old['secs']
wb=openpyxl.load_workbook(d.parent/'解剖学_過去問対応表.xlsx',data_only=True);ws=wb.active
rows=[]
for r in range(2,ws.max_row+1):
    v=[ws.cell(row=r,column=c).value for c in range(1,10)]
    if v[0] is None: continue
    sec=str(v[7]).strip() if v[7] is not None else ''
    rows.append(dict(id=str(v[0]).strip(),q=v[1] or '',ja=v[2] or '',la=v[3] or '',yr=str(v[4] or ''),
        sib=[s.strip() for s in str(v[5] or '').split(',') if s.strip()],page=str(v[6] or ''),sec=sec))
ids={x['id'] for x in rows}
print('rows',len(rows),'missing sib',sorted({s for x in rows for s in x['sib'] if s not in ids})[:5])
secids={s['id'] for s in secs}
print('bad sec',[x['id']+':'+x['sec'] for x in rows if x['sec'].split('-')[0] not in secids])
oldq={x['id']:x for x in old['q']}
ch={k:[] for k in ('q','ja','la','sib','page','sec')}
for x in rows:
    o=oldq.get(x['id'])
    if not o: print('new',x['id']);continue
    for k in ch:
        if o[k]!=x[k]: ch[k].append(x['id'])
print({k:len(v) for k,v in ch.items()}); print('removed',[k for k in oldq if k not in ids])
for k in ('ja','la','q'): print(k,ch[k][:15])
json.dump({'q':rows,'secs':secs},open(d/'data.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
