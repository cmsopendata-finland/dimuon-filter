import FWCore.ParameterSet.Config as cms

DimuonFilter = cms.EDFilter('DimuonFilter' ,
                            muonInputTag = cms.InputTag("muons"),
                            csvFileName = cms.string("dimuon.csv"),
                            rootFileName = cms.string("invariantMass.root"),
                            binInterval = cms.double(0.05),
                            invariantMassMin = cms.double(2.0),
                            invariantMassMax = cms.double(110.0),
                            maxNEvents = cms.int32(100000)
                            )
