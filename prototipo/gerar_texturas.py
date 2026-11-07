import numpy as np, sys, os
from PIL import Image, ImageFilter
out=sys.argv[1]; rng=np.random.default_rng(7)
def noise(w,h,cx,cy,oct=4,pers=0.5):
    acc=np.zeros((h,w));amp=1;tot=0
    for o in range(oct):
        gx=max(2,int(cx*2**o));gy=max(2,int(cy*2**o))
        g=rng.random((gy,gx)).astype(np.float32)
        im=Image.fromarray((g*255).astype(np.uint8)).resize((w,h),Image.BICUBIC)
        acc+=np.asarray(im,np.float32)/255*amp;tot+=amp;amp*=pers
    return acc/tot
def save(a,name,q):
    Image.fromarray(np.clip(a,0,255).astype(np.uint8)).save(os.path.join(out,name),quality=q,optimize=True,progressive=True)
# wood table
W,H=1400,1000
a=np.zeros((H,W,3),np.float32)
planks=[0,230,470,740,1000]
base=np.array([58,36,23],np.float32)
for i in range(4):
    y0,y1=planks[i],planks[i+1];h=y1-y0
    n=noise(W,h,3,10,5,0.55); n2=noise(W,h,1.5,3,3)
    yy=np.arange(h)[:,None]/h
    rings=np.sin((yy*28+n2*6+i)*np.pi)*0.5+0.5
    grain=noise(W,h,40,140,2,0.5)
    t=0.55*rings+0.3*n+0.15*grain
    tone=1+[-0.06,0.05,-0.02,0.08][i]
    col=base*tone*(0.55+0.75*t[...,None])
    col[...,0]*=1.04
    a[y0:y1]=col
    a[y0:y0+3]*=0.35; a[y1-2:y1]*=0.55
a*=0.85+0.3*noise(W,H,2,2,2)[...,None]
save(a,'wood.jpg',62)
# leather
W,H=640,900
pores=noise(W,H,160,225,1)
wr=np.abs(noise(W,H,18,25,4)-0.5)*2
blot=noise(W,H,3,4,3)
base=np.array([96,52,30],np.float32)
t=0.75+0.25*blot-0.18*(1-wr)**6+0.12*(pores-0.5)
a=base*t[...,None]
img=Image.fromarray(np.clip(a,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.4))
img.save(os.path.join(out,'leather.jpg'),quality=64,optimize=True,progressive=True)
# paper
W,H=700,1000
f=noise(W,H,200,280,1);m=noise(W,H,4,5,4)
base=np.array([237,227,204],np.float32)
t=0.97+0.03*(f-0.5)*2-0.04*(m-0.5)
a=base*t[...,None]; a[...,2]-=6*(m-0.5)
save(a,'paper.jpg',70)
# endpaper (marbled-ish) for contracapa
W,H=700,1000
n=noise(W,H,3,4,5,0.6);x=np.linspace(0,1,W)[None,:]
v=np.sin((x*9+n*7)*np.pi)*0.5+0.5
c1=np.array([46,64,58],np.float32);c2=np.array([92,110,96],np.float32);c3=np.array([170,150,108],np.float32)
a=c1*(1-v[...,None])+c2*v[...,None]
veins=(np.abs(np.sin((x*23+n*15)*np.pi))<0.06)[...,None]
a=np.where(veins,c3,a)
save(a,'endpaper.jpg',60)
