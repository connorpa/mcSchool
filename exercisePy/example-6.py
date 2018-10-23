# ---
# jupyter:
#   kernelspec:
#     name: python2
#     display_name: Python 2
# ---

# # Calculation of the sudakov using MC method
# Import libraries which will be needed

from math import pi, sqrt, log, exp
from ROOT import TH1D, TCanvas, gRandom,gStyle

# The alpha strong function, input q is in GeV

def alphaS(q):
    QCDlam = 0.2  #Lambda QCD for 3 flavours
    Qlam0  = 1    #scale freezing
    nf     = 3    #number of flavours
    beta0  = (33 - 2*nf) / 6 
    Qval = max(Qlam0, q)
    return pi / (beta0*log(Qval/QCDlam))

# The splitting function at the LO without alphaS

def Splitting(z):
    return 6*(1/z -2 +z*(1-z) + 1/(1-z)) #g -> g
    #return 4/3*((1+z*z)/(1-z)) #q -> q

# Integrand inside of the sudakov

def suda(t1, t2):
    # Generate randomly q2
    q2 = t1*pow(t2/t1, gRandom.Uniform())
    # we generate here z1 = 1-z, 
    # because we have a pole in the splitting functions \sim 1/(1-z)       
    # Generate randomly z1
    z1min,z1max = 0.01, 0.99
    z1= z1min*pow(z1max/z1min, gRandom.Uniform())

    z = 1. - z1
    q = sqrt(q2)
    integrand = alphaS(q)/2/pi * Splitting(z) /q2	 
    weight = q2*log(t2/t1) * z1*log(z1max/z1min)
    return integrand*weight 

# Function to calculate sudakov

def Sudakov(t1, t2):
    sum0 = sum00 = 0
    npoints = 1000
    for i in range(npoints):
        ff = suda(t1, t2)
        sum0  +=  ff
        sum00 +=  ff**2
    sum0  /= npoints
    sum00 /= npoints
    sigma2 = sum00 - sum0*sum0
    error = sqrt(sigma2/npoints)

    sudakov = exp(-sum0)
    sudError = sudakov*error #Error of the sudakov
    return sudakov

# Book a histogram

TH1D.SetDefaultSumw2()
ntmax = 20
tmin, tmax = 1., 500. 
histo1 = TH1D("sudakov",";q^{2};sudakov", ntmax, tmin, tmax)

# Loop over data points in the histogram

for nt in range(1, ntmax+1):
    t1 = histo1.GetBinCenter(nt)
    sudakov = Sudakov(t1, tmax)
    sudError = 0
    print " t2 = ", tmax , " t1 = ", t1 , " Delta_S = " , sudakov , " +-" , sudError 
    histo1.SetBinContent(nt, sudakov)
    histo1.SetBinError(nt, sudError)

# Plot the Sudakov factor

c = TCanvas()
gStyle.SetPadTickY(1) # ticks at right side
gStyle.SetOptStat(0)  # get rid of statistics box
c.SetLogy()
histo1.Draw()
c.Draw()
