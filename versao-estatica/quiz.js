(() => {
'use strict';
const cfg=window.QUIZ_DATA, main=document.getElementById('quiz'), nodes=new Map(cfg.nodes.map(n=>[n.id,n])), vars=new Map(cfg.variables.map(v=>[v.id,v.title])), values=Object.create(null), cdn='https://cdn.xquiz.co';
const checkoutParams=new URLSearchParams(location.search), allow=/^(utm_[a-z0-9_]+|fbclid|gclid|ttclid|msclkid|src|sck)$/i;
let timers=[], current=null;
const e=(tag,cl)=>{const x=document.createElement(tag);if(cl)x.className=cl;return x;};
function escape(s){const x=e('span');x.textContent=s;return x.innerHTML;}
function rich(x,s){const t=document.createElement('template');t.innerHTML=String(s||'').replace(/\{\{([^}]+)\}\}/g,(_,k)=>escape(values[k.trim()]||'')); for(const a of t.content.querySelectorAll('script,iframe,object,embed,form,link,meta,style'))a.remove();for(const a of t.content.querySelectorAll('*'))for(const at of [...a.attributes])if(/^on/i.test(at.name)||['src','href','srcdoc','action'].includes(at.name))a.removeAttribute(at.name);x.append(t.content);return x;}
function align(x,a){x.style.textAlign=['left','right','center'].includes(a)?a:'center';return x;}
function size(x,s){const map={'text-xs':'12px','text-sm':'14px','text-base':'16px','text-lg':'18px','text-xl':'20px','text-2xl':'24px','text-3xl':'30px','text-4xl':'36px'};if(map[s])x.style.fontSize=map[s];return x;}
function img(data,w,alt='Imagem do devocional'){const x=e('img','media');x.alt=alt; x.src=data.src?data.src:cdn+'/images/'+encodeURIComponent(data.uuid); if(data.width&&data.height){x.width=data.width;x.height=data.height;} const widths={'w-full':'100%','w-40':'160px','w-44':'176px','w-60':'240px','w-72':'288px','w-80':'320px'};if(w)x.style.width=widths[w]||w; x.addEventListener('load',()=>fit());x.addEventListener('error',()=>{const msg=e('div','media-fail');msg.textContent='Imagem indisponível no momento.';x.replaceWith(msg);},{once:true});return x;}
function progress(n){const x=e('div','progress'),bar=e('div');bar.style.width=Math.max(0,Math.min(100,Number(n)||0))+'%';x.append(bar);x.setAttribute('role','progressbar');x.setAttribute('aria-valuenow',String(n));x.setAttribute('aria-label','Progresso da jornada');return x;}
function edge(id,handle){return cfg.edges.find(k=>k.source===id&&k.sourceHandle===handle);}
function urlFor(target){const u=new URL(target.data.url);for(const [k,v] of checkoutParams)if(allow.test(k)&&!u.searchParams.has(k))u.searchParams.set(k,v);return u.href;}
function advance(handle){const next=edge(current.id,handle);if(next)render(next.target);}
function cta(c,label){const next=edge(current.id,c.id), target=next&&nodes.get(next.target),x=e(target?.data?.url?'a':'button','cta');if(x.tagName==='A'){x.href=urlFor(target);}else{x.type='button';x.addEventListener('click',()=>advance(c.id));}rich(x,label);if(c.data.colors?.focus)x.style.background=c.data.colors.focus;return x;}
function fit(){if(main.classList.contains('free')){main.style.removeProperty('--s');return;}
let s=1;main.style.setProperty('--s','1');
while(s>0.7&&main.scrollHeight>main.clientHeight+1){s=Math.round((s-0.03)*100)/100;main.style.setProperty('--s',String(s));}}
addEventListener('resize',()=>fit());
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(()=>fit());
let curAudio=null;
const fmt=t=>{t=Math.max(0,Math.floor(t||0));return Math.floor(t/60)+':'+String(t%60).padStart(2,'0');};
function audioPlayer(d){const box=e('div','player');if(!d.audio?.uuid&&!d.audio?.src)return box;
const src=d.audio.src?d.audio.src:cdn+'/audios/'+encodeURIComponent(d.audio.uuid);
const head=e('div','pl-head');const cross=e('span','pl-cross');cross.textContent='\u2720';const ttl=e('div','pl-title');ttl.textContent='Ora\u00e7\u00e3o com o Padre';const sub=e('div','pl-sub');sub.textContent='Toque no bot\u00e3o para ouvir';head.append(cross,ttl,sub);
const btn=e('button','pl-btn');btn.type='button';btn.setAttribute('aria-label','Tocar ora\u00e7\u00e3o');
const ico=()=>'<svg viewBox="0 0 24 24" width="34" height="34" aria-hidden="true">'+(au.paused?'<path d="M8 5v14l11-7z" fill="currentColor"/>':'<path d="M6 5h4v14H6zM14 5h4v14h-4z" fill="currentColor"/>')+'</svg>';
const wave=e('div','pl-wave');wave.setAttribute('role','slider');wave.setAttribute('aria-label','Progresso do \u00e1udio');wave.tabIndex=0;
const bars=(d.audio.waves&&d.audio.waves.length?d.audio.waves:Array.from({length:48},(_,i)=>.3+.6*Math.abs(Math.sin(i/3)))).map(v=>{const b=e('i');b.style.height=Math.round(14+Math.min(1,v)*40)+'px';wave.append(b);return b;});
const time=e('div','pl-time'),cur=e('span'),dur=e('span');cur.textContent='0:00';dur.textContent='';time.append(cur,dur);
const au=new Audio();au.preload='metadata';au.src=src;
btn.innerHTML=ico();
const upd=()=>{const r=au.duration?au.currentTime/au.duration:0;const k=Math.round(r*bars.length);bars.forEach((b,i)=>b.classList.toggle('on',i<k));cur.textContent=fmt(au.currentTime);if(au.duration)dur.textContent=fmt(au.duration);wave.setAttribute('aria-valuenow',String(Math.round(r*100)));};
au.addEventListener('loadedmetadata',upd);au.addEventListener('timeupdate',upd);
au.addEventListener('play',()=>{btn.innerHTML=ico();box.classList.add('playing');sub.textContent='Tocando\u2026';btn.setAttribute('aria-label','Pausar ora\u00e7\u00e3o');});
au.addEventListener('pause',()=>{btn.innerHTML=ico();box.classList.remove('playing');sub.textContent=au.ended?'Ouvir novamente':'Pausado';btn.setAttribute('aria-label','Tocar ora\u00e7\u00e3o');});
au.addEventListener('ended',()=>{au.currentTime=0;upd();});
btn.addEventListener('click',()=>{if(au.paused){if(curAudio&&curAudio!==au)curAudio.pause();curAudio=au;au.play().catch(()=>{});}else au.pause();});
const seek=ev=>{const r=wave.getBoundingClientRect();if(au.duration)au.currentTime=Math.max(0,Math.min(1,(ev.clientX-r.left)/r.width))*au.duration;};
wave.addEventListener('click',seek);
wave.addEventListener('keydown',ev=>{if(!au.duration)return;if(ev.key==='ArrowRight')au.currentTime=Math.min(au.duration,au.currentTime+3);if(ev.key==='ArrowLeft')au.currentTime=Math.max(0,au.currentTime-3);});
box.append(head,btn,wave,time);return box;}
function render(id){const n=nodes.get(id);if(!n)return;if(n.type==='function'){if(n.data.url)location.assign(urlFor(n));else{const next=cfg.edges.find(k=>k.source===id);if(next)render(next.target);}return;} timers.forEach(clearTimeout);timers=[];if(curAudio){curAudio.pause();curAudio=null;}current=n;main.replaceChildren();let loadingMs=0;for(const c of n.data.content||[]){const d=c.data;let x;switch(c.type){
case 'headerV2':x=e('header','hero-header');if(d.logo?.uuid)x.append(img(d.logo,(d.logo.size||50)+'px','Logo'));break;
case 'progressV2':x=progress(d.targetPercentage);break;
case 'title':x=align(size(e('div','heading'),d.titleSize),d.alignment);rich(x,d.title);if(d.subtitle&&d.subtitle!=='<p></p>')x.append(rich(size(e('div','sub'),d.subtitleSize),d.subtitle));break;
case 'text':case 'textV2':x=align(size(e('div'),d.size||d.textSize),d.alignment||d.textAlignment);rich(x,d.text);if(c.type==='textV2'&&d.textSize==='custom')x.style.fontSize=d.textCustomSize+'px';break;
case 'image':if(d.image?.uuid){x=img(d.image,d.size);}break;
case 'button':x=cta(c,d.title);if(loadingMs&&x.tagName==='BUTTON'){x.disabled=true;timers.push(setTimeout(()=>x.disabled=false,loadingMs));}break;
case 'quiz':x=e('div','options');if(d.columns==='grid-cols-2')x.style.gridTemplateColumns='repeat(2,minmax(0,1fr))';for(const opt of d.content||[]){const b=e('button','option');b.type='button';if(d.colors?.border)b.style.borderColor=d.colors.border;if(d.model?.includes('emoji')&&opt.emoji){const em=e('span','emoji');em.textContent=opt.emoji;b.append(em);}else if(d.model?.includes('image')&&opt.image?.uuid)b.append(img(opt.image,'48px',''));b.append(rich(e('span'),opt.title));b.addEventListener('click',()=>advance(opt.id));x.append(b);}break;
case 'form':x=e('form','form');for(const field of d.content||[]){const input=e('input');input.type='text';input.name=field.id;input.placeholder=field.placeholder||field.title;input.setAttribute('aria-label',field.placeholder||field.title);input.required=!!field.required;input.autocomplete='off';x.append(input);}const submit=rich(e('button','cta'),d.buttonTitle||'Continuar');submit.type='submit';x.append(submit);x.addEventListener('submit',event=>{event.preventDefault();const data=new FormData(x);for(const field of d.content||[])values[vars.get(field.variableId)||field.title]=String(data.get(field.id)||'').trim();advance(c.id);});break;
case 'audio':x=audioPlayer(d);break;
case 'loading':loadingMs=Math.max(0,Number(d.time)||0)*1000;x=rich(e('div','loading'),d.title);const p=progress(0);p.style.setProperty('--duration',Math.max(1,loadingMs)+'ms');x.append(p);break;
case 'carousel':x=e('div','carousel');const items=(d.content||[]).filter(k=>k.image?.uuid);if(!items.length)break;let i=0;const stage=e('div'),nav=e('div','carousel-nav'),prev=e('button'),next=e('button'),counter=e('span');prev.type=next.type='button';prev.textContent='‹';next.textContent='›';prev.setAttribute('aria-label','Imagem anterior');next.setAttribute('aria-label','Próxima imagem');function slide(){stage.replaceChildren(img(items[i].image,d.size));counter.textContent=(i+1)+' / '+items.length;}prev.onclick=()=>{i=(i+items.length-1)%items.length;slide();};next.onclick=()=>{i=(i+1)%items.length;slide();};nav.append(prev,counter,next);x.append(stage,nav);slide();break;
case 'result':x=e('div','result');rich(x,d.title);const bar=progress(d.score);bar.firstChild.style.background=d.colors?.bgColor||'var(--accent)';x.append(bar);const labels=e('div','result-labels');for(const k of ['level1','level2','level3'])labels.append(rich(e('span'),d[k]));x.append(labels,rich(e('div'),d.result));break;
case 'redirect':timers.push(setTimeout(()=>advance(c.id),Math.max(0,Number(d.time)||0)*1000));break;
}if(x)main.append(x);}window.scrollTo(0,0);main.classList.toggle('free',n.id.startsWith('a70d8a'));main.classList.toggle('sparse',!main.querySelector('img.media,.options,.player,.carousel,.result'));main.style.setProperty('--s','1');fit();requestAnimationFrame(fit);}
render('root');
})();
