import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/Run3Winter20DRPremixMiniAOD/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/110X_mcRun3_2021_realistic_v6_ext1-v1/100000/37AC3A73-74D1-2A41-9A36-13E8BFAE85CF.root'
'/store/mc/Run3Winter21DRMiniAOD/QCD_Pt-120To170_TuneCP5_14TeV-pythia8/MINIAODSIM/FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/70000/293294b8-6ac8-415f-8594-44ef38fab6c9.root'
]);

secFiles.extend( [
               ] )
