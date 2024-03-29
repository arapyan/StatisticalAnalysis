import ROOT
import os,sys
from ROOT import TGraphAsymmErrors
from ROOT import TGraphErrors
from ROOT import TColor
#from ROOT import TGraph
from array import array
from ROOT import *
from operator import truediv
import random
import math

ROOT.gStyle.SetOptStat(0)

#a=0.6991*3*0.1086
a=1.0

t=1000.


limit1=array('d')
limit195up=array('d')
limit195down=array('d')
limit168up=array('d')
limit168down=array('d')
limitMD=array('d')
limitMD95up=array('d')
limitMD95down=array('d')
limitMD68up=array('d')
limitMD68down=array('d')

limitObserved=array('d')
limitObservedMD=array('d')

#gmXsecP=array('d', [1735, 979.4, 604.1, 395.7, 270.2, 190.6, 137.8, 101.5, 75.72,20.85,6.692] )
#gmXsecM=array('d', [1130, 606.6, 358.4, 225.9, 149., 101.8, 71.47, 51.22, 37.19, 9.116, 2.644])

gmXsecP=array('d', [2476, 1430, 901.2, 601.3, 418.3, 299.7, 219.8, 164.2, 124.5,36.1,12.1] )
gmXsecM=array('d', [1063, 554.2, 319.5, 197.3, 127.7, 85.8, 59.2, 41.8, 30.0, 6.9, 1.9])

#gmXsecM=[x + y for x, y in zip(gmXsecM2, gmXsecM1)]
#gmXsecP=[x + y for x, y in zip(gmXsecP1, gmXsecP2)]

for s in range(6,13):
	i=s
	if i == 11:
		s=15
	if i == 12:
		s=20
	f=ROOT.TFile.Open("higgsCombineTest.AsymptoticLimits.mH"+str(s)+"00.root")
	tree=f.Get("limit")
	tree.GetEntry(2)
	print tree.limit
	median=tree.limit*a*(gmXsecM[i-2]+gmXsecP[i-2])
	medianMD=tree.limit*a
        limit1.append(tree.limit*a*(gmXsecM[i-2]+gmXsecP[i-2]))
	limitMD.append(math.sqrt(tree.limit*a))
        tree.GetEntry(3)
	print tree.limit
        limit168up.append(abs(tree.limit*a*(gmXsecM[i-2]+gmXsecP[i-2])-median))
	#limitMD68up.append(math.sqrt(abs(tree.limit*a-median)/(gmXsecM[i-2]+gmXsecP[i-2])))
	limitMD68up.append(abs(math.sqrt(tree.limit*a)-math.sqrt(medianMD)))
	tree.GetEntry(1)
	print tree.limit
        limit168down.append(abs(tree.limit*a*(gmXsecM[i-2]+gmXsecP[i-2])-median))
	#limitMD68down.append(math.sqrt(abs(tree.limit*a-median)/(gmXsecM[i-2]+gmXsecP[i-2])))
	limitMD68down.append(abs(math.sqrt(tree.limit*a)-math.sqrt(medianMD)))
        tree.GetEntry(4)
	print tree.limit
        limit195up.append(abs(tree.limit*a*(gmXsecM[i-2]+gmXsecP[i-2])-median))
	#limitMD95up.append(math.sqrt(abs(tree.limit*a-median)/(gmXsecM[i-2]+gmXsecP[i-2])))
	limitMD95up.append(abs(math.sqrt(tree.limit*a)-math.sqrt(medianMD)))
	tree.GetEntry(0)
	print tree.limit
        limit195down.append(abs(tree.limit*a*(gmXsecM[i-2]+gmXsecP[i-2])-median))
	#limitMD95down.append(math.sqrt(abs(tree.limit*a-median)/(gmXsecM[i-2]+gmXsecP[i-2])))
	limitMD95down.append(abs(math.sqrt(tree.limit*a)-math.sqrt(medianMD)))
	tree.GetEntry(5)
	limitObserved.append(tree.limit*a*(gmXsecM[i-2]+gmXsecP[i-2]))
	limitObservedMD.append(math.sqrt(tree.limit*a))


print "medianMD ="+ str(limitMD)
print "median68upMD ="+ str(limitMD68up)
print "median68downMD ="+ str(limitMD68down)
print "median95upMD ="+ str(limitMD95up)
print "median95downMD ="+ str(limitMD95down)

print "\n"

print "median ="+ str(limit1)
print "median68up ="+ str(limit168up)
print "median68down ="+ str(limit168down)
print "median95up ="+ str(limit195up)
print "median95down ="+ str(limit195down)


print "OBSERVED = "+str(limitObserved)
print "OBSERVED_MD = "+str(limitObservedMD)


for l in range(0,12):
	print "  - {"#+str(format(limitObserved[i],'.2f')+"}"


massErr=array('d')
mass=array('d')

for i in range(5,11):
	massErr.append(0.)
	mass.append(i*100)

massErr.append(0.)
mass.append(1500)
massErr.append(0.)
mass.append(2000)

c1=ROOT.TCanvas("c1","c1",1000,600)
c1.SetGrid()
graph_limit1=ROOT.TGraph(7,mass,limit1)
graph_limit1.SetMarkerStyle(34)
graph_limit1.SetMarkerSize(3)
graph_limit1.GetYaxis().SetRangeUser(0,2000)
graph_limit1.GetYaxis().SetTitle("#sigma #times BR(H->WZ) [fb]")
graph_limit1.GetXaxis().SetTitle("Charged Higgs Mass [GeV]")
graph_limit1.Draw("ACE")


graph_limit195=ROOT.TGraphAsymmErrors(7,mass,limit1,massErr,massErr,limit195down,limit195up)
graph_limit195.SetLineColor(kBlack)
graph_limit195.SetLineWidth(1)
graph_limit195.SetFillColor(kGreen)
graph_limit195.Draw("3")

graph_limit168=ROOT.TGraphAsymmErrors(7,mass,limit1,massErr,massErr,limit168down,limit168up)
graph_limit168.SetLineColor(kBlack)
graph_limit168.SetLineWidth(1)
graph_limit168.SetFillColor(TColor.GetColor(252,241,15))
graph_limit168.Draw("3same")
graph_limit1.Draw("same")
c1.SaveAs("limit_mT.root")


c2=ROOT.TCanvas("c2","c2",1000,600)
c2.SetGrid()
graph_limitGM=ROOT.TGraph(8,mass,limitMD)
graph_limitGM.SetMarkerStyle(34)
graph_limitGM.SetMarkerSize(3)
graph_limitGM.GetYaxis().SetRangeUser(0,5)
graph_limitGM.GetYaxis().SetTitle("s_{H}")
graph_limitGM.GetXaxis().SetTitle("Charged Higgs Mass")
graph_limitGM.Draw("ACE")

graph_limitGM95=ROOT.TGraphAsymmErrors(8,mass,limitMD,massErr,massErr,limitMD95down,limitMD95up)
graph_limitGM95.SetLineColor(kBlack)
graph_limitGM95.SetLineWidth(1)
graph_limitGM95.SetFillColor(kGreen)
graph_limitGM95.Draw("3")

graph_limitGM68=ROOT.TGraphAsymmErrors(8,mass,limitMD,massErr,massErr,limitMD68down,limitMD68up)
graph_limitGM68.SetLineColor(kBlack)
graph_limitGM68.SetLineWidth(1)
graph_limitGM68.SetFillColor(TColor.GetColor(252,241,15))
graph_limitGM68.Draw("3same")
graph_limitGM.Draw("same")


c2.SaveAs("limitGM_mT.root")
